#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
O relatório de pesquisa ainda diz o que o codebook diz?

`reports/process_tracing_8jan_relatorio.md` é escrito à mão e reproduz, em
prosa e em tabela, números que vivem no JSON. Já ficou para trás duas vezes:
em 11/09/2026 carregava "mais de 1.600 ações penais" e "1.402 condenados",
quase um mês depois de o codebook ter corrigido os dois; e a correção daquela
rodada alcançou a §3.2 mas não a §2.1, que seguiu com a marcha de "9 km".

Quatro checagens, escolhidas por produzirem pouco ruído — uma checagem de
rotina que grita à toa é abandonada, e aí não checa nada:

  1. cobertura   — a tabela da Etapa 2 tem uma linha por registro do codebook,
                   sem id desconhecido e sem repetição;
  2. páginas     — onde a tabela cita "Documento, p. N", N está entre as
                   páginas que o codebook ancora para aquele registro;
  3. cifras      — nenhuma cifra retirada reaparece como afirmação;
  4. caminhos    — todo caminho citado em `code span` existe em disco.

O que ele NÃO faz: ler a prosa. Um número novo e errado passa, e uma afirmação
causal sem lastro passa. Isto pega regressão declarada — a cifra que o codebook
já matou e o texto ressuscitou —, não erro de interpretação.

Uso:  python scripts/conferir_relatorio.py
"""

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"
MD_P = RAIZ / "reports/process_tracing_8jan_relatorio.md"

# Cifras que o codebook retirou ou substituiu, e o texto não pode voltar a
# afirmar. O segundo termo é o ACOMPANHANTE: se ele aparece na mesma linha, a
# linha está narrando a correção, não cometendo o erro, e é absolvida. É o que
# permite ao relatório registrar a própria história sem disparar alarme.
# Sem acompanhante (None) significa: não pode aparecer de jeito nenhum.
RETIRADAS = [
    ("mais de 1.600", "1.335", "PT-53 — 1.618 é audiência de custódia"),
    ("1.600 ações", "1.335", "PT-53 — o total é 1.335"),
    ("1.402 condenados", "responsabilizados", "PT-61 — 552 são ANPPs, sem condenação"),
    ("131 ações extintas", None, "PT-61 — ausente da camada de texto do balanço"),
    ("cerca de 4 mil", "3.000 a 5.500", "PT-34 — sem lastro primário"),
    ("~4 mil", "3.000 a 5.500", "PT-34 — sem lastro primário"),
    ("mais de 100 acampamentos", "todos os Estados", "PT-12 — sem lastro na CPMI"),
    ("9 km", "7,9 km", "PT-24 — a marcha é de 7,9 km pela via N1"),
    ("1.200 presos", "2.151", "PT-52 — são 2.151 em flagrante nos dias 8 e 9"),
    ("03/07/2026", "lastro", "PT-60 — prorrogação sem decisão no corpus"),
]

LINHA_TABELA = re.compile(r'^\|\s*\*{0,2}(PT-[0-9A-Z]+)\*{0,2}\s*\|')
# Só os números: o rótulo do documento é resolvido à parte, contra o codebook,
# porque a tabela o escreve de formas variadas — "Cappelli, conclusão B, p. 54",
# "Literatura comparada + CPMI, p. 614", "EP 169, p. 1, 36–38". Tentar recortá-lo
# por expressão regular produz rótulos como "B", e alarme falso.
CITACAO = re.compile(r'p\.\s*([0-9,\s–—-]*\d)')


def sem_blocos_de_codigo(texto):
    """Remove cercas ``` — elas desbalanceiam a contagem de crases."""
    return re.sub(r'^```[\s\S]*?^```', "", texto, flags=re.M)


def paginas_do_codebook(valor):
    """'CPMI: 646, 711 | Cappelli: 55' -> {'CPMI': {646, 711}, 'Cappelli': {55}}"""
    saida = {}
    for parte in (valor or "").split("|"):
        if ":" not in parte:
            continue
        rotulo, nums = parte.split(":", 1)
        paginas = {int(n) for n in re.findall(r'\d+', nums)}
        if paginas:
            saida[rotulo.strip()] = paginas
    return saida


def paginas_citadas(trecho):
    """'1, 36–38' -> {1, 36, 38}. De um intervalo guardam-se só as pontas: o
    relatório cita faixas ('p. 6–11') onde o codebook ancora páginas avulsas,
    e exigir o miolo produziria alarme falso."""
    saida = set()
    for item in re.split(r'[,\s]+', trecho.strip()):
        if not item:
            continue
        pontas = re.findall(r'\d+', item)
        if pontas:
            saida.add(int(pontas[0]))
            saida.add(int(pontas[-1]))
    return saida


def variantes(rotulo):
    """Como o rótulo do codebook pode aparecer escrito na tabela.

    'EP 169-Transferência' também é citado como 'EP 169'; 'Balanço 2026' é
    citado inteiro. O sufixo depois do hífen distingue duas peças do mesmo
    processo e a tabela costuma omiti-lo."""
    r = rotulo.strip()
    return {r, r.split("-")[0].strip()} - {""}


def rotulo_da_citacao(celula, fim, ancoras):
    """Qual documento a citação 'p. N' que termina em `fim` está ancorando?

    Regra: o rótulo do codebook cuja menção mais próxima precede a citação.
    Com um único documento ancorado, é ele — não há ambiguidade a resolver."""
    if len(ancoras) == 1:
        return next(iter(ancoras))
    melhor, pos_melhor = None, -1
    antes = celula[:fim].lower()
    for rotulo in ancoras:
        for v in variantes(rotulo):
            pos = antes.rfind(v.lower())
            if pos > pos_melhor:
                melhor, pos_melhor = rotulo, pos
    return melhor


def main():
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    J = {e["id"]: e for e in dados["eventos"]}
    n_json = int(dados["metadados"]["n_subeventos"])
    bruto = MD_P.read_text(encoding="utf-8")
    texto = sem_blocos_de_codigo(bruto)
    linhas = texto.split("\n")

    falhas = []

    print("CONFERÊNCIA RELATÓRIO x CODEBOOK")
    print("=" * 78)

    # ------------------------------------------------------ 1. cobertura
    try:
        inicio = texto.index("# ETAPA 2")
        fim = texto.index("# ETAPA 3")
    except ValueError:
        print("  X  não achei a tabela da Etapa 2 — o relatório mudou de estrutura")
        return 1

    tabela = [l for l in texto[inicio:fim].split("\n") if LINHA_TABELA.match(l)]
    ids = [LINHA_TABELA.match(l).group(1) for l in tabela]

    for i in ids:
        if i not in J:
            falhas.append("tabela cita {}, que não existe no codebook".format(i))
    for i in J:
        if i not in ids:
            falhas.append("{} está no codebook e fora da tabela da Etapa 2".format(i))
    for i in sorted({x for x in ids if ids.count(x) > 1}):
        falhas.append("{} aparece {} vezes na tabela".format(i, ids.count(i)))

    print("  1. cobertura : {} linhas na tabela da Etapa 2, {} registros no codebook".format(
        len(ids), len(J)))

    # -------------------------------------------------------- 2. páginas
    conferidas, sem_ancora = 0, 0
    for linha in tabela:
        pid = LINHA_TABELA.match(linha).group(1)
        if pid not in J:
            continue
        celula = linha.strip().strip("|").split("|")[-1]
        ancoras = paginas_do_codebook(J[pid].get("fonte_pagina"))
        for m in CITACAO.finditer(celula):
            citadas = paginas_citadas(m.group(1))
            if not citadas:
                continue
            if not ancoras:
                sem_ancora += 1
                falhas.append("{}: a tabela cita p. {} e o codebook não ancora página "
                              "nenhuma".format(pid, m.group(1).strip()))
                continue
            conferidas += 1
            rotulo = rotulo_da_citacao(celula, m.start(), ancoras)
            fora = citadas - ancoras[rotulo]
            if fora:
                falhas.append("{}: p. {} não está no que o codebook ancora para «{}» ({})"
                              .format(pid, ", ".join(str(n) for n in sorted(fora)),
                                      rotulo, sorted(ancoras[rotulo])))

    print("  2. páginas   : {} citações com número conferidas contra fonte_pagina".format(
        conferidas))

    # --------------------------------------------------------- 3. cifras
    for morta, vivo, motivo in RETIRADAS:
        for n, linha in enumerate(linhas, 1):
            if morta not in linha:
                continue
            if vivo is not None and vivo in linha:
                continue          # a linha narra a correção
            falhas.append("L{}: «{}» reaparece como afirmação — {}".format(n, morta, motivo))

    print("  3. cifras    : {} verbetes retirados procurados linha a linha".format(
        len(RETIRADAS)))

    # ------------------------------------------------------- 4. caminhos
    vistos = set()
    for linha in linhas:
        for c in re.findall(r'`([^`\n]+)`', linha):
            c = c.strip()
            if "/" not in c and not c.endswith(".json"):
                continue
            if any(ch in c for ch in " *?()"):
                continue
            vistos.add(c)
    for c in sorted(vistos):
        if not (RAIZ / c.rstrip("/")).exists():
            falhas.append("caminho citado não existe em disco: {}".format(c))

    print("  4. caminhos  : {} caminhos citados verificados em disco".format(len(vistos)))

    # contagem declarada no cabeçalho
    cabecalho = "\n".join(linhas[:6])
    if "{} sub-eventos".format(n_json) not in cabecalho:
        falhas.append("o cabeçalho não declara os {} sub-eventos do codebook".format(n_json))

    # AS TRES CIFRAS DO FECHAMENTO, acrescentadas em 29/10/2026.
    #
    # O paragrafo "Onde o projeto esta" declarava SETE cifras a mao, e
    # declarava tambem que este conferidor nao as cobria. Em 29/10 as
    # sete foram medidas e as sete estavam erradas -- 85/61/23/22/6.951/
    # 66/12.089 contra 87/69/17/25/7.092/75/12.644.
    #
    # O CRITERIO DE QUEM FICA E DO PESQUISADOR: cifra com relacao ao
    # processo ou a eventos dentro dele passa. Ficaram as tres da
    # CADEIA -- o numero de elos e a particao de classe, que qualifica
    # toda proposicao causal. Sairam as quatro de TAMANHO DE CORPUS,
    # que descrevem a leitura e nao o episodio, e que vivem no README
    # sob a decima checagem da integridade.
    #
    # VERIFICAR EM VEZ DE GERAR e a pratica da casa: a checagem 10 faz
    # o mesmo com o README. O efeito contra o envelhecimento e o mesmo
    # -- o ciclo cai -- e o texto continua sendo texto.
    _cl = {}
    for _ev in J.values() if isinstance(J, dict) else J:
        _k = _ev.get("status_classe")
        _cl[_k] = _cl.get(_k, 0) + 1
    for _rot, _n in (("deles em fonte primária citada por página",
                      _cl.get("Confirmado em fonte primária", 0)),
                     ("confirmados por outra via",
                      _cl.get("Confirmado", 0))):
        if "{} {}".format(_n, _rot) not in texto:
            falhas.append(
                "o fechamento não declara «{} {}» — é o que o codebook tem".format(_n, _rot))

    print("=" * 78)
    if falhas:
        print("FALHAS — {}:".format(len(falhas)))
        for f in falhas:
            print("  X  {}".format(f))
        print("\nO relatório é escrito à mão: corrija em reports/ e rode de novo.")
        print("Em qualquer divergência, prevalece o JSON.")
        return 1
    print("OK — o relatório bate com os {} registros do codebook".format(len(J)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
