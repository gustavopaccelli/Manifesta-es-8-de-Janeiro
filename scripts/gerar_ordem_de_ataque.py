# -*- coding: utf-8 -*-
"""A seção 'Ordem de ataque' de docs/PENDENCIAS-ANALITICAS.md, GERADA.

Fonte da verdade: `data/ordem_de_ataque.json`. Esta peça não decide nada — não
abre, não fecha e não ordena tarefa. Ela faz três coisas que a mão fazia mal:

1. **A seção em que a tarefa aparece é consequência do campo `estado`**, não de
   alguém lembrar de mover a linha. A 15 ficou listada como aberta dois dias
   depois de executada.
2. **Toda contagem sai de medição.** As da camada A vêm de
   `localizar_camada_a.py` (mesma função `estado()` do script que já gerava
   aquela linha); as de corpus vêm de `Fontes/MANIFESTO-CORPUS.csv`. A linha da
   17 declarava "números gerados" e carregava uma cifra de 30/09.
3. **A frase que conta as abertas é derivada da tabela.** Ela já dissera "seis"
   com cinco linhas.

**O que NÃO é medido fica declarado como não medido.** Cifra apurada uma vez,
por tentativa de rede ou leitura — quantas peças estão barradas no cliente, por
exemplo — vive em `medidos_a_mao`, e o bloco gerado imprime a data de cada uma.
Número à mão não desaparece por decreto: ou se mede, ou se datilografa a data
ao lado dele.

Uso:
    python scripts/gerar_ordem_de_ataque.py              # gera e grava
    python scripts/gerar_ordem_de_ataque.py --chaves     # lista as chaves
    python scripts/gerar_ordem_de_ataque.py --autoteste  # provas, sem gravar
"""
import csv
import io
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))

AGENDA = RAIZ / "docs/PENDENCIAS-ANALITICAS.md"
LEDGER = RAIZ / "data/ordem_de_ataque.json"
MANIFESTO = RAIZ / "Fontes/MANIFESTO-CORPUS.csv"

ABRE = ("<!-- ORDEM-DE-ATAQUE: gerado por scripts/gerar_ordem_de_ataque.py a partir "
        "de data/ordem_de_ataque.json. Não editar à mão: o ciclo sobrescreve. -->")
FECHA = "<!-- /ORDEM-DE-ATAQUE -->"

CHAVE = re.compile(r"\{\{(\w+)\}\}")
PALAVRA = {0: "nenhuma", 1: "uma", 2: "duas", 3: "três", 4: "quatro", 5: "cinco",
           6: "seis", 7: "sete", 8: "oito", 9: "nove", 10: "dez", 11: "onze",
           12: "doze", 13: "treze", 14: "catorze", 15: "quinze", 16: "dezesseis",
           17: "dezessete", 18: "dezoito", 19: "dezenove", 20: "vinte"}


def mil(n):
    """1832 -> '1.832'. O separador do projeto é o ponto."""
    return "{:,}".format(int(n)).replace(",", ".")


def ledger():
    return json.loads(io.open(LEDGER, encoding="utf-8").read())


def registro_leitura():
    """O modulo do censo de leitura, importado em vez de reimplementado.

    Mesma razao de `medir_camada_a` importar `localizar_camada_a`: uma lista de
    marcas, uma janela, um censo. Ele resolve caminhos relativos ao argumento,
    entao nao depende do diretorio de trabalho."""
    sys.path.insert(0, str(RAIZ / "scripts"))
    import gerar_registro_leitura as R
    return R


def censo():
    """As linhas do censo de estado de leitura (uma por peca do manifesto)."""
    linhas, _, _, _ = registro_leitura().censo(str(RAIZ))
    return linhas


LIDOS = ("LIDO_INTEGRAL", "LIDO_PARCIAL")


# ------------------------------------------------------------------- G4 ---
def guarda_g4(d):
    """G4: nenhum texto do LEDGER afirma nao-leitura de peca cujo estado e de
    leitura.

    NASCIDA EM 22/10/2026 (item 78), e a razao tem data: duas linhas desta
    secao estavam falsas havia catorze dias -- a tarefa 10 dizia "nenhuma lida"
    com as cinco peças do eixo lidas, e a tarefa 26 listava como decisao aberta
    a rota de Beach e Pedersen depois de ela ter sido EXECUTADA.

    **O pressuposto que eu dei para pedir esta guarda estava errado.** Eu disse
    que o ledger nao era vigiado porque nao esta em `docs/`. Mas a secao gerada
    E GRAVADA dentro de docs/PENDENCIAS-ANALITICAS.md, que a G2 vigia desde
    21/10. A G2 nao falhou por falta de cobertura -- falhou por tres defeitos
    de mecanica, e dois deles foram corrigidos nela mesma (vocabulario coletivo
    e janela de ressalva). O terceiro e a razao de esta guarda existir apesar
    disso: **a G2 ve a RENDERIZACAO e esta ve a FONTE.** Quem edita o ledger ve
    o erro apontado no texto que ele edita, com o numero da tarefa, em vez de
    num numero de linha de um arquivo gerado que ele nao deve editar a mao.
    """
    R = registro_leitura()
    linhas, _, decl, _ = R.censo(str(RAIZ))
    lidas = R.pecas_lidas(linhas, decl)

    unidades = []
    for i, par in enumerate(d.get("antes", []), 1):
        unidades.append(("ledger/antes[%d]" % i, par))
    for x in d["tarefas"]:
        unidades.append(("ledger/tarefa %s" % x["n"], x["texto"]))
    for i, par in enumerate(d.get("depois", []), 1):
        unidades.append(("ledger/depois[%d]" % i, par))
    return R.exame_de_prosa(unidades, lidas)


# --------------------------------------------------------------- medidas ---
def medir_camada_a():
    """Conta os 43 da camada A por estado de leitura, sem rede.

    Importa `localizar_camada_a` em vez de reimplementar: é o mesmo
    `estado()` que gera a planilha, e duas contagens do mesmo universo por
    dois códigos diferentes é como a cifra errada entra."""
    import localizar_camada_a as camada_a

    linhas = camada_a.carregar()
    por_estado = {}
    for r in linhas:
        por_estado[camada_a.estado(r["doi"])] = por_estado.get(camada_a.estado(r["doi"]), 0) + 1
    pend = [r for r in linhas if camada_a.estado(r["doi"]) == "PENDENTE"]
    return {
        "camada_a_total": len(linhas),
        "camada_a_lidos": por_estado.get("LIDO", 0),
        "camada_a_fichas": por_estado.get("FICHA", 0),
        "camada_a_impedidos": por_estado.get("IMPEDIDO", 0),
        "camada_a_pendentes": por_estado.get("PENDENTE", 0),
        "camada_a_mobilization": sum(1 for r in pend if "Mobilization" in r["veiculo"]),
    }


def medir_codebook():
    """O que falta ancorar no codebook, medido no JSON — a tarefa 26.

    `sem_pagina_pdf` é o subconjunto que dá trabalho de leitura: registro sem
    `fonte_pagina` cujo documento vinculado é PDF que existe no corpus. Quem
    não tem documento, ou cujo documento é `.md`, não se resolve por leitura e
    não entra nessa conta."""
    import conferir_paginas  # a linha de base dos parciais vive lá, e o passo 7 a vigia

    dados = json.loads(io.open(RAIZ / "process_tracing_8jan_eventos.json",
                               encoding="utf-8").read())
    eventos = dados["eventos"]
    sem_pagina = [e for e in eventos if not (e.get("fonte_pagina") or "").strip()]
    com_pdf = []
    for e in sem_pagina:
        for p in (e.get("fonte_local") or "").split(";"):
            p = p.strip()
            if p.lower().endswith(".pdf") and (RAIZ / p).exists():
                com_pdf.append(e)
                break
    # O campo 17 entrou em 16/10/2026 com 82 dos 83 registros vazios, e vazio
    # ali significa NÃO CODIFICADO. A conta sai daqui para que a linha da
    # tarefa 27 encolha sozinha a cada registro codificado: "faltam 82" escrito
    # à mão envelheceria no primeiro, que é como a linha da 17 envelheceu.
    sem_autonomia = [e for e in eventos if not (e.get("autonomia_movimento") or "").strip()]
    return {
        "registros": len(eventos),
        "registros_sem_pagina": len(sem_pagina),
        "registros_sem_pagina_palavra": PALAVRA.get(len(sem_pagina), str(len(sem_pagina))),
        "registros_sem_pagina_pdf": len(com_pdf),
        "registros_sem_pagina_pdf_palavra": PALAVRA.get(len(com_pdf), str(len(com_pdf))),
        "fragmentos_por_janela": conferir_paginas.PARCIAIS_BASE,
        "autonomia_codificados": len(eventos) - len(sem_autonomia),
        "autonomia_sem_codificar": len(sem_autonomia),
    }


def medir_corpus(censo_linhas):
    """Peças e páginas por eixo, do manifesto — que é o que a checagem 8 confere.

    REESCRITA EM 22/10/2026 (item 78). Antes recebia `lidas_por_eixo`, lido
    da chave `lidas` do ledger: um SEGUNDO censo de estado de leitura,
    declarado à mão ao lado do censo medido de `gerar_registro_leitura`. Os
    dois divergiram em silêncio nos dois eixos que a chave cobria — o 14
    constava "nenhuma lida" com as cinco lidas, o 13 constava três lidas
    com as dezoito lidas. **Duas contagens do mesmo universo por dois
    códigos diferentes é como a cifra errada entra**, que é a regra que
    `medir_camada_a` já seguia e esta não seguia.

    E mede DOIS predicados, porque a chave antiga confundia os dois: a
    lista nomeava peças que ANCORAM REGISTRO e a prosa gerada dizia "Três
    foram LIDAS". São referentes diferentes — no eixo 13, seis ancoram e
    dezoito estão lidas — e `faltam` subtraía ancoragem do total para
    chamar o resto de não lido. **A cifra correta no referente errado.**"""
    with io.open(MANIFESTO, encoding="utf-8-sig") as f:
        linhas = list(csv.DictReader(f))
    assert linhas, "manifesto vazio: rode gerar_manifesto_corpus.py"

    def paginas(itens):
        return sum(int(x["paginas"]) for x in itens)

    out = {}
    for chave, eixo in (("eixo13", "13_Bolsonarismo-mobilizacao"),
                        ("eixo14", "14_Livros-brasileiros")):
        peças = [x for x in linhas if x["eixo"] == eixo]
        assert peças, "eixo sem peça no manifesto: " + eixo
        out[chave + "_arquivos"] = len(peças)
        out[chave + "_paginas"] = mil(paginas(peças))

        # Cada fragmento declarado tem de casar com UMA peça. Fragmento que não
        # casa é peça renomeada — e aí a conta do que falta estaria errada em
        # silêncio, que é o defeito que este script existe para matar.
        # Os dois predicados, cada um no seu referente, e os dois MEDIDOS.
        do_eixo = [x for x in censo_linhas if x["eixo"] == eixo]
        assert len(do_eixo) == len(peças), \
            "o censo vê {} peças no eixo {} e o manifesto vê {}".format(
                len(do_eixo), eixo, len(peças))
        lidas = [x for x in do_eixo if x["estado"] in LIDOS]
        ancoram = [x for x in do_eixo if x["origem_do_estado"] == "MEDIDO"]
        restam = [x for x in peças
                  if x["caminho"] not in {y["caminho"] for y in lidas}]
        for nome, n in (("_lidas", len(lidas)), ("_ancoram", len(ancoram)),
                        ("_faltam", len(restam))):
            out[chave + nome] = n
            out[chave + nome + "_palavra"] = PALAVRA.get(n, str(n))
        out[chave + "_faltam_paginas"] = mil(paginas(restam))
    return out


def medir(d):
    """Todas as chaves disponíveis para `{{...}}`, com a procedência de cada uma."""
    abertas = [x for x in d["tarefas"] if x["estado"] == "aberta"]
    fechadas = [x for x in d["tarefas"] if x["estado"] == "fechada"]

    # A frase de natureza, derivada da tabela: agrupa na ordem em que a
    # natureza aparece, nunca na ordem alfabética, para que o texto não se
    # reembaralhe a cada geração.
    grupos = []
    for x in abertas:
        for g in grupos:
            if g[0] == x["natureza"]:
                g[1].append(x["n"])
                break
        else:
            grupos.append([x["natureza"], [x["n"]]])
    partes = ["{} (**{}**)".format(nat, ", ".join(ns)) for nat, ns in grupos]
    frase = partes[0] if len(partes) == 1 else \
        ", ".join(partes[:-1]) + " e " + partes[-1]

    chaves = {
        "abertas": str(len(abertas)),
        "abertas_palavra": PALAVRA[len(abertas)],
        "fechadas": str(len(fechadas)),
        "fechadas_palavra": PALAVRA.get(len(fechadas), str(len(fechadas))),
        "abertas_natureza": frase,
    }
    chaves.update(medir_codebook())
    chaves.update(medir_camada_a())
    chaves.update(medir_corpus(censo()))
    for k, v in d.get("medidos_a_mao", {}).items():
        chaves[k] = str(v["valor"])
    return {k: str(v) for k, v in chaves.items()}


def preencher(texto, chaves, usadas=None):
    """Troca {{chave}} pelo valor medido.

    `{{Chave}}` com maiúscula inicial devolve o valor capitalizado — é o que
    permite começar frase com número escrito ("**Três foram lidas**") sem
    guardar a palavra duas vezes no ledger."""
    def troca(m):
        k = m.group(1)
        baixa = k[0].lower() + k[1:]
        if k in chaves:
            achada, valor = k, chaves[k]
        elif k[0].isupper() and baixa in chaves:
            achada, valor = baixa, chaves[baixa][:1].upper() + chaves[baixa][1:]
        else:
            raise KeyError("chave desconhecida em texto do ledger: {{" + k + "}}")
        if usadas is not None:
            usadas.add(achada)
        return valor
    return CHAVE.sub(troca, texto)


# ----------------------------------------------------------------- bloco ---
def linha(x, coluna_final):
    return "| {} | {} | {} | {} |".format(x["n"], x["texto"], x["itens"],
                                          x[coluna_final])


def montar(d):
    chaves, usadas = medir(d), set()

    def p(txt):
        return preencher(txt, chaves, usadas)

    out = ["## Ordem de ataque — revista em " + d["revisada"], ""]
    for par in d["antes"]:
        out += [p(par), ""]

    for titulo, estado, cab, col in (("### Fechadas", "fechada", "Quando", "quando"),
                                     ("### Abertas", "aberta", "Depende de", "depende")):
        out += [titulo, "",
                "| # | Tarefa | Item desta agenda | {} |".format(cab),
                "|:--|:--|:--|:--|"]
        out += [p(linha(x, col)) for x in d["tarefas"] if x["estado"] == estado]
        out += [""]

    for par in d["depois"]:
        out += [p(par), ""]

    # As cifras que não se medem entram com a data em que foram medidas. É o
    # contrário de esconder: a linha existe para que a próxima rodada veja a
    # idade do número sem precisar escavar o item que o produziu.
    mao = d.get("medidos_a_mao", {})
    citadas = {k: v for k, v in mao.items() if k in usadas}
    if citadas:
        itens = ["**{}** — {} (medido em {}, {})".format(
            v["valor"], v["o_que"], v["medido_em"], v["fonte"])
            for k, v in sorted(citadas.items())]
        out += ["> **Cifras desta seção que não são medidas a cada ciclo:** "
                + "; ".join(itens) + ". Todo o resto sai de medição na geração.", ""]

    return "\n".join(out).rstrip("\n")


def gravar(bloco):
    t = io.open(AGENDA, encoding="utf-8").read()
    assert t.count(ABRE) == 1 and t.count(FECHA) == 1, \
        "os marcadores de bloco não estão exatamente uma vez em " + AGENDA.name
    cabeca, resto = t.split(ABRE, 1)
    _, cauda = resto.split(FECHA, 1)
    novo = cabeca + ABRE + "\n\n" + bloco + "\n\n" + FECHA + cauda

    # Prova de contenção: fora dos marcadores, nada muda. Um gerador que
    # escreve num arquivo de 2.300 linhas escritas à mão precisa provar isso.
    assert novo.split(ABRE, 1)[0] == cabeca
    assert novo.split(FECHA, 1)[1] == cauda
    if novo == t:
        print("ordem de ataque: já em dia, nada a gravar")
        return False
    io.open(AGENDA, "w", encoding="utf-8", newline="\n").write(novo)
    return True


# -------------------------------------------------------------- autoteste ---
def autoteste():
    d = ledger()

    numeradas = [x["n"] for x in d["tarefas"] if x["n"] != "—"]
    assert len(numeradas) == len(set(numeradas)), \
        "número de tarefa repetido no ledger: " + str(sorted(numeradas))
    for x in d["tarefas"]:
        assert x["estado"] in ("aberta", "fechada"), x
        if x["estado"] == "fechada":
            assert x["quando"].startswith("✅"), "fechada sem data: " + x["n"]
            assert "depende" not in x, "fechada com dependência: " + x["n"]
        else:
            assert x.get("natureza") and x.get("depende"), \
                "aberta sem natureza ou sem dependência: " + x["n"]
    for v in d.get("medidos_a_mao", {}).values():
        for campo in ("valor", "o_que", "medido_em", "fonte"):
            assert campo in v, "medido_a_mao sem " + campo

    chaves = medir(d)
    assert chaves["camada_a_total"] == "43", chaves["camada_a_total"]
    soma = sum(int(chaves["camada_a_" + k])
               for k in ("lidos", "fichas", "impedidos", "pendentes"))
    assert soma == 43, "os quatro estados da camada A não somam 43: " + str(soma)

    # Prova negativa 1: chave inexistente aborta, em vez de sair no texto.
    try:
        preencher("{{nao_existe}}", chaves)
        raise AssertionError("chave desconhecida passou sem erro")
    except KeyError:
        pass

    # Prova negativa 2: fechar uma tarefa muda a contagem e a frase de natureza
    # — é o defeito de 15/10, e ele agora não sobrevive à geração.
    copia = json.loads(json.dumps(d))
    viva = next(x for x in copia["tarefas"] if x["estado"] == "aberta")
    viva.update(estado="fechada", quando="✅ 99/99")
    del viva["depende"]
    depois = medir(copia)
    assert depois["abertas"] == str(int(chaves["abertas"]) - 1), "a contagem não seguiu o estado"
    assert viva["n"] not in depois["abertas_natureza"], \
        "a frase de natureza continua citando tarefa fechada"

    # Prova negativa 3: número repetido é pego — foi o defeito de 29/09, a
    # tarefa 18 listada duas vezes.
    ns = [x["n"] for x in d["tarefas"] if x["n"] != "—"] + [d["tarefas"][0]["n"]]
    assert len(ns) != len(set(ns)), "a duplicata plantada não foi detectada"

    # G4, e as tres provas negativas dela. Mutam a COPIA pelo parser: o
    # arquivo nao e tocado, entao nao ha o que reverter.
    g4 = guarda_g4(d)
    if g4:
        print("G4 — %d afirmação(ões) de não-leitura de peça lida no ledger:" % len(g4))
        for rotulo, termo, trecho in g4:
            print("  X %s afirma não-leitura de «%s»" % (rotulo, termo))
            print("    %s" % trecho[:150])
        raise AssertionError("G4: o ledger afirma não-leitura de peça lida")

    R = registro_leitura()
    alvo = "Beach e Pedersen"

    def com_texto(txt):
        """A prova SUBSTITUI o texto da tarefa, nunca o estende.

        A primeira versão anexava, e a tarefa 1 tem `~~` no próprio título:
        a janela liberou a injeção — corretamente — e a prova culpou a guarda
        por um defeito que era da prova. **Prova negativa tem de controlar a
        própria vizinhança**, ou mede o vizinho em vez da guarda."""
        copia = json.loads(json.dumps(d))
        copia["tarefas"][0]["texto"] = txt
        return guarda_g4(copia)

    crua = "Prova negativa. " + alvo + " não está lida."
    # (a) afirmação CRUA ao lado do nome: tem de cair.
    assert com_texto(crua), "G4 não pegou afirmação crua de não-leitura"

    # (b) a MESMA afirmação com a ressalva ENCOSTADA: tem de passar, porque
    # errata bem escrita mora na frase seguinte e barrá-la ensinaria a não
    # escrever errata. Foi medido: a errata da linha 126 de docs/analise/09
    # está a zero caracteres da frase que corrige.
    assert not com_texto(
        crua + " **ERRATA DE 22/10/2026:** deixou de valer no mesmo dia."), \
        "G4 reprovou afirmação com errata encostada — a liberação quebrou"

    # (c) a MESMA afirmação com a MESMA ressalva ALÉM DA JANELA: tem de cair.
    # É o defeito de 21-22/10 em estado puro: na linha de 7.268 caracteres da
    # tarefa 26, um `~~` a 262 caracteres dava anistia ao parágrafo inteiro.
    assert com_texto(crua + (" palavra" * 60)
                     + " **ERRATA:** deixou de valer."), \
        ("G4 liberou afirmação cuja ressalva está além de %d caracteres — o "
         "escopo do perdão voltou a ser maior que o do exame"
         % R.JANELA_RESSALVA)

    bloco = montar(d)
    assert bloco.startswith("## Ordem de ataque — revista em ")
    assert "### Fechadas" in bloco and "### Abertas" in bloco
    assert "{{" not in bloco, "sobrou chave não substituída no bloco"
    assert bloco.count("\n| ") >= len(d["tarefas"]), "linha de tarefa perdida"
    print("autoteste OK — ledger íntegro, 43 na camada A, G4 limpa, "
          "seis provas negativas")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "--autoteste":
        autoteste()
    elif arg == "--chaves":
        for k, v in sorted(medir(ledger()).items()):
            print("  {{%s}}  ->  %s" % (k, v))
    else:
        autoteste()
        if gravar(montar(ledger())):
            print("ordem de ataque: seção regravada em docs/PENDENCIAS-ANALITICAS.md")
