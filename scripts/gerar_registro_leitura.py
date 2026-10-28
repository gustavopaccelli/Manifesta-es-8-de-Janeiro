#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""O REGISTRO DE ESTADO DE LEITURA DO CORPUS — e a guarda que faltava.

Emite: docs/referencial/05_REGISTRO-DE-LEITURA.md

POR QUE ESTE SCRIPT EXISTE, e a razao tem data. Em 21/10/2026 eu relatei ao
pesquisador que seis verbetes da Encyclopedia estavam "lidos-a-ler" -- e os seis
estavam LIDOS, com a leitura registrada em docs/analise/10. Copiei a lista da
§7.4 de docs/analise/09, escrita em 30/09, isto e, ANTES de o documento 10
existir. Era a terceira contagem copiada que errava na mesma semana, e a pior:
as outras perdiam item, esta declarou nao lido o que estava lido, e teria
mandado o pesquisador reler onze verbetes fichados.

O DEFEITO ESTRUTURAL que isso expos: o estado de leitura do corpus vivia em
PROSA, espalhada por sete documentos de analise escritos cada um na data da sua
propria leitura, e NADA no ciclo conferia coerencia entre eles.

O QUE ESTE SCRIPT FAZ, em tres camadas:

  1. MEDE o que e mensuravel. Das 69 pecas do manifesto, as que ancoram registro
     com `fonte_pagina` tem leitura parcial DEMONSTRAVEL -- o passo 9 do ciclo
     confere a transcricao contra a folha do PDF. Nao se declara o que se mede.
  2. LE a declaracao das demais, em data/estado_de_leitura.json, que e dado e
     nao prosa.
  3. CONFERE tres coisas, e a segunda e a que teria pego o meu erro.

AS TRES GUARDAS:

  G1 COBERTURA — toda peca do manifesto esta medida ou declarada, e toda peca
     declarada existe no manifesto. Pega fonte nova entrando sem estado, e
     declaracao que sobrevive a peca.
  G2 COERENCIA DE PROSA — nenhum documento de docs/ pode AFIRMAR nao-leitura de
     peca cujo estado e de leitura. **E a guarda que faltava.** Duas liberacoes,
     e as duas tem razao escrita: mencao historica DATADA (MARCAS_HISTORICAS),
     pelo mesmo critério que a checagem 7 usa para nome retirado; e negacao que
     senta ao lado de afirmacao (MARCAS_LEITURA_POSITIVA), porque dizer QUAL
     parte nao foi lida e o que LIDO_PARCIAL exige.
  G3 PROCEDENCIA DA LEITURA — peca declarada lida tem de dizer ONDE a leitura
     esta registrada, e o arquivo apontado tem de existir.

Uso:  python scripts/gerar_registro_leitura.py
"""

import csv
import glob
import io
import json
import os
import re
import sys
from collections import defaultdict

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
os.chdir(RAIZ)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MANIFESTO = "Fontes/MANIFESTO-CORPUS.csv"
CODEBOOK = "process_tracing_8jan_eventos.json"
DECLARACAO = "data/estado_de_leitura.json"
SAIDA = "docs/referencial/05_REGISTRO-DE-LEITURA.md"

LIDOS = ("LIDO_INTEGRAL", "LIDO_PARCIAL")

# As formas pelas quais um documento AFIRMA nao-leitura. Minusculas; a busca
# ignora caixa, pela licao de 21/10 -- guarda sensivel a caixa e guarda pela
# metade.
MARCAS_NAO_LEITURA = [
    "não lido", "não lida", "não lidos", "não lidas",
    "não foi lido", "não foi lida", "não foram lidos", "não foram lidas",
    "lidos-a-ler", "lidas-a-ler", "não está lida", "não está lido",
    "coletado, não lido", "sem ter tê-la lido", "sem tê-la lido",
    "continuam fora do corpus", "continua fora do corpus",
    # ACRESCENTADAS EM 22/10/2026 (item 78): a forma COLETIVA da negacao,
    # que a lista nao tinha. A linha da tarefa 10 do ledger afirmava
    # "nenhuma lida" sobre CINCO pecas lidas e sobreviveu 14 dias dentro de
    # um arquivo que esta guarda vigia. Ela nao reprovou a linha: nao a
    # EXAMINOU, porque nenhuma marca casava. O vocabulario da negacao e
    # maior que a lista, e a lista cresce por medicao, nao por intuicao.
    "nenhuma lida", "nenhum lido", "nenhuma foi lida", "nenhum foi lido",
    "nenhuma delas lida", "nenhum deles lido",
    "nenhuma delas foi lida", "nenhum deles foi lido",
    # DELIBERADAMENTE FORA: "nenhuma das", que casa com "nenhuma das
    # catorze da coleta tratava de PT-08" -- afirmacao sobre CONTEUDO, nao
    # sobre leitura. Medido: ela sozinha produzia 10 falsos positivos.
]

# A MARCA QUE LIBERA A MENCAO HISTORICA, e e deliberadamente estreita. Uma linha
# que narra a troca de estado com DATA nao e afirmacao de estado atual -- e esse
# e o mesmo critério que a checagem 7 aplica a nome retirado. Se a linha nao
# traz nenhuma destas marcas, ela esta afirmando no PRESENTE.
MARCAS_HISTORICAS = [
    "errata", "até 20/10", "até 21/10", "até 19/10", "até 18/10",
    "deixou de", "passaram de", "passou de", "superado", "resolvido",
    "~~", "estava lido", "estavam lidos", "foram lidos", "foram lidas",
]

# A SEGUNDA LIBERACAO, e ela e SEMANTICA em vez de temporal: **uma negacao que
# senta ao lado de uma afirmacao e qualificacao, nao negacao.** A primeira versao
# desta guarda reprovou o proprio texto que eu escrevi para corrigi-la -- "lida
# em parte: capitulos 1 a 3 (...); capitulos 4 a 8 seguem nao lidos" --, porque
# ela via "nao lidos" e nao via "lida em parte" na mesma linha. Dizer QUAL parte
# nao foi lida e precisamente o que LIDO_PARCIAL exige; barrar isso ensinaria a
# nao declarar o recorte, que e o oposto do que o registro existe para obter.
MARCAS_LEITURA_POSITIVA = [
    "lido na fonte", "lida na fonte", "lidos na fonte", "lidas na fonte",
    "lido integral", "lida integral", "lidos integrais", "lidas integrais",
    "lido em parte", "lida em parte", "lidos em parte", "lidas em parte",
    "lido_parcial", "lido_integral",
]

def _mesmo(a, b):
    """Compara caminhos sem depender do separador.

    `glob` devolve `docs/referencial\\05_...` no Windows e `SAIDA` tem barra
    normal. Comparar as cadeias cruas deixaria a exclusao abaixo inerte --
    e guarda com exclusao inerte e pior que guarda sem exclusao, porque
    declara uma intencao que nao cumpre."""
    return (os.path.normcase(os.path.normpath(a))
            == os.path.normcase(os.path.normpath(b)))


# A G2 NAO VIGIA A PROPRIA SAIDA, e a razao e de 22/10/2026 (item 78).
# `emite()` grava a tabela de incoerencias dentro de SAIDA, que este glob
# inclui. Na primeira vez que a G2 acusou algo de verdade, ela publicou o
# trecho defeituoso no arquivo vigiado e a rodada seguinte acusou o RELATORIO
# -- com o defeito ja corrigido na fonte. **Guarda que publica o defeito no
# arquivo que ela vigia acusa-se a si mesma na rodada seguinte.** Defeito
# latente desde 21/10: o laco so nasce com a primeira acusacao verdadeira.
#
# Exclui-se so a propria saida. A grade funcional (02) tambem e gerada, mas a
# prosa dela vem de um dicionario escrito a mao no script: afirmacao de
# nao-leitura ali e defeito de verdade, e segue vigiada.
# `reports/` ENTRA EM 27/10/2026 (item 93). A G2 nasceu em 21/10 vigiando
# `docs/`, onde a prosa de analise vive, e o relatorio de pesquisa, a
# auditoria de fontes e a tabela-espelho ficaram fora. **Dois dos tres sao
# GERADOS**, e isso torna a vigilancia MAIS util, nao menos: afirmacao
# falsa ali e defeito do gerador, nao erro de digitacao, e defeito de
# gerador se repete a cada rodada.
#
# Medido antes de estender: ZERO incoerencias em 1.038 linhas. O risco
# aqui nao era conserto de conteudo -- era guarda INERTE, e a prova
# negativa injeta dentro de `reports/` para afasta-lo.
DOCS_VIGIADOS = [x for x in
                 sorted(glob.glob("docs/analise/*.md"))
                 + sorted(glob.glob("docs/referencial/*.md"))
                 + sorted(glob.glob("reports/**/*.md", recursive=True))
                 + ["docs/PENDENCIAS-ANALITICAS.md"]
                 if not _mesmo(x, SAIDA)]
assert any(x.replace("\\", "/").startswith("reports/")
           for x in DOCS_VIGIADOS), \
    "a G2 deixou de alcançar reports/ — confira o glob"
assert not any(_mesmo(x, SAIDA) for x in DOCS_VIGIADOS), \
    "a exclusão da própria saída ficou inerte — confira o separador"

# A JANELA DA RESSALVA, em caracteres, e ela foi MEDIDA em 22/10/2026 (item 78).
#
# O problema: a liberacao era avaliada na LINHA. Numa linha de 7.268 caracteres
# -- o texto da tarefa 26 do ledger -- um `~~` em qualquer ponto liberava
# qualquer afirmacao. Quatro liberacoes disparavam ali, nenhuma delas perto da
# afirmacao sobre Beach e Pedersen, e a decisao ficou listada como aberta
# depois de executada. **O escopo do perdao era maior que o escopo do exame.**
#
# Cortar por oracao nao serve, e a medicao mostrou por que: ERRATA BEM ESCRITA
# MORA NA FRASE SEGUINTE. A linha 126 de docs/analise/09 diz "continuam fora do
# corpus" e logo depois "ERRATA DE 21/10/2026: esta frase (...) deixou de
# valer". Cortar por oracao separa a errata da frase que ela corrige e reprova
# a pratica correta.
#
# Entao o escopo certo nao e unidade estrutural nenhuma: e PROXIMIDADE. Medida
# a distancia de cada uma das 119 afirmacoes de nao-leitura do repositorio ate
# a sua ressalva mais proxima, as legitimas chegam a 193 caracteres e a
# seguinte esta a 262 -- um vao de 69. O resultado e estavel de 150 a 250 e cai
# a zero em 300, quando um "deixou de" remoto volta a liberar o que nao devia.
# 200 e o meio do plato.
JANELA_RESSALVA = 200


def _ocorrencias(baixo, agulhas):
    """Todas as posicoes de todas as agulhas, em minusculas."""
    out = []
    for a in agulhas:
        i = baixo.find(a)
        while i >= 0:
            out.append((i, i + len(a), a))
            i = baixo.find(a, i + 1)
    return out


def _vizinha(pos, outras, janela):
    """A primeira ocorrencia a `janela` caracteres ou menos de `pos`."""
    a, b = pos
    for c, d, agulha in outras:
        if c < b and a < d:
            dist = 0
        elif d <= a:
            dist = a - d
        else:
            dist = c - b
        if dist <= janela:
            return agulha
    return None


def exame_de_prosa(unidades, lidas, janela=JANELA_RESSALVA):
    """Afirmacoes de nao-leitura de peca cujo estado e de leitura.

    `unidades` e um iteravel de (rotulo, texto) -- uma linha de documento, ou o
    texto de uma tarefa do ledger. `lidas` e {caminho: [termos]}.

    Devolve [(rotulo, termo, trecho)]. Uma afirmacao e acusada quando:
      - a marca de nao-leitura aparece no texto, E
      - NENHUMA ressalva -- historica ou de leitura positiva -- esta a `janela`
        caracteres ou menos dela, E
      - o nome de uma peca lida esta a `janela` caracteres ou menos dela.

    As tres distancias usam a mesma janela porque e o mesmo princípio: o que
    qualifica uma afirmacao tem de estar onde quem le a afirmacao o leia.
    """
    ressalvas = MARCAS_HISTORICAS + MARCAS_LEITURA_POSITIVA
    achados = []
    for rotulo, texto in unidades:
        baixo = texto.lower()
        marcas = _ocorrencias(baixo, MARCAS_NAO_LEITURA)
        if not marcas:
            continue
        rs = _ocorrencias(baixo, ressalvas)
        for cam, termos in sorted(lidas.items()):
            ts = _ocorrencias(baixo, [x.lower() for x in termos])
            if not ts:
                continue
            for a, z, marca in marcas:
                if _vizinha((a, z), rs, janela):
                    continue
                if _vizinha((a, z), ts, janela):
                    achados.append((rotulo, termos[0],
                                    texto[max(0, a - 70):z + 70].strip()))
                    break
    return achados



def censo(raiz="."):
    """O ESTADO DE LEITURA de cada peca do manifesto -- o censo UNICO.

    Extraido de main() em 22/10/2026 (item 78) para que
    gerar_ordem_de_ataque.py conte pelas MESMAS regras. Ate aqui o ledger
    dele mantinha um SEGUNDO censo, declarado a mao na chave `lidas`, e os
    dois divergiram: o eixo 14 constava "nenhuma lida" com as cinco lidas,
    e o eixo 13 constava tres lidas com dezoito lidas. Duas contagens do
    mesmo universo por dois codigos diferentes e como a cifra errada entra
    -- a regra que medir_camada_a() ja seguia e esta nao seguia.

    Devolve (linhas, falhas, decl, por_caminho).
    """
    man = list(csv.DictReader(io.open(os.path.join(raiz, MANIFESTO),
                                      encoding="utf-8-sig")))
    por_caminho = {x["caminho"]: x for x in man}
    dados = json.loads(io.open(os.path.join(raiz, CODEBOOK),
                               encoding="utf-8").read())
    decl = json.loads(io.open(os.path.join(raiz, DECLARACAO),
                              encoding="utf-8").read())
    pecas = decl["pecas"]

    # ------------------------------------------- camada 1: o que se MEDE
    regs = defaultdict(list)
    folhas = defaultdict(set)
    for e in dados["eventos"]:
        locais = [p.strip().replace("\\", "/")
                  for p in (e.get("fonte_local") or "").split(";") if p.strip()]
        for p in locais:
            regs[p].append(e["id"])
            for n in re.findall(r"\b(\d{1,4})\b", e.get("fonte_pagina") or ""):
                folhas[p].add(n)

    linhas, falhas = [], []
    for cam in sorted(por_caminho):
        if cam in regs:
            d = {
                "caminho": cam,
                "origem_do_estado": "MEDIDO",
                "estado": "LIDO_PARCIAL",
                "o_que": "ancora {} registro(s) com {} folha(s) citada(s); o "
                         "passo 9 do ciclo confere a transcrição contra a folha"
                         .format(len(regs[cam]), len(folhas[cam])),
                "registrado_em": "o próprio codebook (`fonte_pagina`)",
                "registros": " ".join(sorted(regs[cam])),
            }
        elif cam in pecas:
            p = pecas[cam]
            d = {
                "caminho": cam,
                "origem_do_estado": "DECLARADO",
                "estado": p["estado"],
                "o_que": p.get("o_que", ""),
                "registrado_em": p.get("registrado_em", ""),
                "registros": "",
            }
        else:
            # G1: peca no manifesto sem estado medido nem declarado
            falhas.append("G1 cobertura: {} está no manifesto e não tem estado "
                          "medido nem declarado".format(cam))
            continue
        d["paginas"] = por_caminho[cam]["paginas"]
        d["eixo"] = por_caminho[cam]["eixo"]
        linhas.append(d)

    # G1, a via inversa: declaracao que sobreviveu a peca
    for cam in pecas:
        if cam not in por_caminho:
            falhas.append("G1 cobertura: {} é declarado e NÃO está no manifesto"
                          .format(cam))

    return linhas, falhas, decl, por_caminho


def pecas_lidas(linhas, decl):
    """{caminho: [termos]} das pecas cujo estado EFETIVO e de leitura.

    O estado efetivo vem do censo, nao da declaracao: peca que ancora
    registro e MEDIDO e vence o que a declaracao dela disser. Os `termos`
    seguem vindo da declaracao, que e onde eles vivem."""
    efetivo = {x["caminho"]: x["estado"] for x in linhas}
    return {c: p.get("termos", []) for c, p in decl["pecas"].items()
            if efetivo.get(c, p["estado"]) in LIDOS}


def main():
    linhas, falhas, decl, por_caminho = censo()
    pecas = decl["pecas"]

    # ------------------------------------- G3: procedencia da leitura
    for d in linhas:
        if d["origem_do_estado"] != "DECLARADO" or d["estado"] not in LIDOS:
            continue
        ref = d["registrado_em"]
        if not ref:
            falhas.append("G3 procedência: {} é declarado {} e não diz ONDE a "
                          "leitura está registrada"
                          .format(d["caminho"], d["estado"]))
        elif not os.path.exists(ref.split("#")[0]):
            falhas.append("G3 procedência: {} aponta a leitura para {}, que não "
                          "existe".format(d["caminho"], ref))

    # ----------------- G2: nenhum documento afirma nao-leitura de peca lida
    lidas = pecas_lidas(linhas, decl)
    unidades = []
    for doc in DOCS_VIGIADOS:
        if not os.path.exists(doc):
            continue
        for i, linha in enumerate(io.open(doc, encoding="utf-8").read()
                                  .split("\n"), 1):
            unidades.append(("%s:%d" % (doc, i), linha))
    incoerencias = exame_de_prosa(unidades, lidas)

    # ------------------------------------------------------------- relatorio
    medidos = [d for d in linhas if d["origem_do_estado"] == "MEDIDO"]
    declarados = [d for d in linhas if d["origem_do_estado"] == "DECLARADO"]
    conta = defaultdict(int)
    for d in linhas:
        conta[d["estado"]] += 1

    print("REGISTRO DE ESTADO DE LEITURA")
    print("  peças no manifesto     : %d" % len(por_caminho))
    print("  estado MEDIDO          : %d  (ancoram registro)" % len(medidos))
    print("  estado DECLARADO       : %d  (não ancoram)" % len(declarados))
    for k in sorted(conta):
        print("    %-16s %d" % (k, conta[k]))
    print("  G2 incoerências de prosa: %d" % len(incoerencias))
    for rotulo, termo, txt in incoerencias:
        print("    X %s afirma não-leitura de «%s»" % (rotulo, termo))
        print("      %s" % txt[:150])

    if incoerencias:
        falhas.append("G2 coerência: {} documento(s) afirmam não-leitura de peça "
                      "declarada lida".format(len(incoerencias)))

    emite(linhas, medidos, declarados, conta, incoerencias, decl)
    print("  -> %s" % SAIDA)

    if falhas:
        print()
        print("FALHAS — %d:" % len(falhas))
        for f in falhas:
            print("  X  %s" % f)
        return 1
    print("  OK — cobertura, coerência de prosa e procedência da leitura")
    return 0


def emite(linhas, medidos, declarados, conta, incoerencias, decl):
    L = []
    w = L.append
    w("# Registro de estado de leitura do corpus")
    w("")
    w("> **Peça gerada por `scripts/gerar_registro_leitura.py`. Não edite à "
      "mão.** É a resposta a um defeito com data: em 21/10/2026 eu relatei seis "
      "verbetes como *\"lidos-a-ler\"* e **os seis estavam lidos**, porque "
      "copiei uma lista de 30/09 do documento que **pedia** a leitura em vez de "
      "abrir o que a **registrava**. O estado de leitura vivia em prosa "
      "espalhada por sete documentos, e nada no ciclo conferia.")
    w("")
    w("**{} peças no corpus. {} com estado MEDIDO, {} com estado DECLARADO.**"
      .format(len(linhas), len(medidos), len(declarados)))
    w("")
    w("## 1. Como o estado é estabelecido — e a maior parte não é declarada")
    w("")
    w("| Origem | Quantas | Como |")
    w("|:--|--:|:--|")
    w("| **MEDIDO** | {} | a peça **ancora registro** com `fonte_pagina`, e o "
      "passo 9 do ciclo confere a transcrição contra a folha do PDF. Leitura "
      "parcial **demonstrável**, não afirmada |".format(len(medidos)))
    w("| **DECLARADO** | {} | a peça **não ancora registro**: informa o desenho "
      "sem sustentar dado. O estado vive em `data/estado_de_leitura.json`, que "
      "é dado e não prosa |".format(len(declarados)))
    w("")
    w("| Estado | Peças |")
    w("|:--|--:|")
    for k in sorted(conta):
        w("| `{}` | {} |".format(k, conta[k]))
    w("")
    w("**Vocabulário.** `LIDO_INTEGRAL` · `LIDO_PARCIAL`, com o que foi lido · "
      "`NAO_LIDO` · `ILEGIVEL`, no corpus e sem camada de texto · "
      "`NAO_DECLARADO`, quando **nenhum documento do repositório registra o "
      "estado** — é confissão, não suposição.")
    w("")
    w("## 2. As três guardas, e a segunda é a que faltava")
    w("")
    w("| | O que confere | O que pega |")
    w("|:--|:--|:--|")
    w("| **G1** cobertura | toda peça do manifesto está medida ou declarada, e "
      "toda declaração existe no manifesto | fonte nova entrando sem estado; "
      "declaração que sobreviveu à peça |")
    w("| **G2** coerência de prosa | **nenhum documento de `docs/` afirma "
      "não-leitura de peça cujo estado é de leitura** | exatamente o erro de "
      "21/10/2026. Menção histórica datada fica livre pela marca de errata, pelo "
      "mesmo critério da checagem 7 do ciclo |")
    w("| **G3** procedência da leitura | peça declarada lida diz **onde** a "
      "leitura está registrada, e o arquivo existe | leitura afirmada sem lugar "
      "onde conferi-la |")
    w("")
    w("**G2 hoje: {} incoerência(s).**".format(len(incoerencias)))
    if incoerencias:
        w("")
        w("| Onde | Termo | Trecho |")
        w("|:--|:--|:--|")
        for rotulo, termo, trecho in incoerencias:
            w("| `{}` | {} | {} |".format(rotulo, termo,
                                          trecho[:120].replace("|", "\\|")))
    w("")
    w("## 3. O registro, peça por peça")
    w("")
    w("| Peça | Folhas | Estado | Origem | O que foi lido | Onde está "
      "registrado |")
    w("|:--|--:|:--|:--|:--|:--|")
    for d in sorted(linhas, key=lambda x: (x["eixo"], x["caminho"])):
        nome = d["caminho"].rsplit("/", 1)[-1]
        w("| `{}` | {} | **{}** | {} | {} | {} |".format(
            nome, d["paginas"], d["estado"], d["origem_do_estado"],
            (d["o_que"] or "—"), (d["registrado_em"] or "—")))
    w("")
    w("## 4. Peças que os documentos discutem e que NÃO estão no corpus")
    w("")
    w("**A afirmação de não-leitura sobre estas é legítima**, e é por estarem "
      "declaradas aqui que a guarda G2 não as confunde com peça lida.")
    w("")
    w("| Peça | Situação |")
    w("|:--|:--|")
    for k, v in decl["fora_do_corpus"].items():
        if k.startswith("_"):
            continue
        w("| **{}** | {} |".format(k, v))
    w("")
    io.open(SAIDA, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")


if __name__ == "__main__":
    sys.exit(main())
