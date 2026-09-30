#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
As duas figuras ainda dizem o que o codebook diz?

**ATENÇÃO AO ESCOPO: este script confere DUAS peças nomeadas, não a pasta.**
Desde 30/09/2026 `reports/figures/` tem dois regimes. As figuras da cronologia
— `figura_cronologia_8jan.svg` e `cronologia_8jan_interativa.html` — são feitas
à mão e é por isso que existem as checagens abaixo. As do campo
multiorganizacional são **geradas** por `scripts/desenhar_campo.py` a partir do
mesmo dicionário que alimenta a planilha, e não passam por aqui: peça gerada
não envelhece, e conferi-la seria conferir o gerador contra si mesmo.

A cronologia é a parte do aparato que **não** é gerada a partir do JSON: a
interativa carrega uma cópia manual dos 82 registros dentro do `<script>`, e o
SVG é rótulo por rótulo, em coordenadas absolutas.
Reescrevê-los como geradores seria o certo; enquanto não são, nada no ciclo
percebe que envelheceram.

E envelheceram: em 25/09/2026 as duas peças ainda traziam "+1.600 ações penais",
"1.402 condenados", "~4 mil na Praça", "9 km", "+100 acampamentos", "~1.200
presos" e a prorrogação de 03/07/2026 — sete cifras retiradas do codebook nas
rodadas de 16/08 e 11/09, publicadas por seis semanas numa figura que se
apresenta como a codificação completa.

Quatro checagens:
  1. cobertura     — todo id do JSON aparece numa das figuras;
  2. etiqueta      — o selo de status bate com `status_classe`;
  3. procedência   — ninguém diz "fonte primária" sem sê-lo no codebook;
  4. cifras mortas — nenhuma das retiradas voltou ao SVG.

Nada disto lê o *conteúdo* dos rótulos: uma cifra nova e errada passa. Isto pega
divergência declarada, não erro de transcrição.

Uso:  python scripts/conferir_figuras.py
"""

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"
HTML_P = RAIZ / "reports/figures/cronologia_8jan_interativa.html"
SVG_P = RAIZ / "reports/figures/figura_cronologia_8jan.svg"

# Vocabulário do codebook -> selo da figura, do mais fraco para o mais forte.
CLASSE = {"Inferência do analista": "inf", "Contextual": "ctx",
          "Confirmado": "ok", "Confirmado em fonte primária": "pri"}
FORCA = {"inf": 0, "ctx": 1, "ok": 2, "pri": 3}

# Registros que a figura agrupa num ponto só, por proximidade de datas.
COMPOSTOS = {
    "PT-03C/D": ["PT-03C", "PT-03D"],
    "PT-06A/B/C": ["PT-06A", "PT-06B", "PT-06C"],
    "PT-08A / PT-08B / PT-08C": ["PT-08A", "PT-08B", "PT-08C"],
}

# Cifras retiradas do codebook e que não podem reaparecer no SVG. Cada uma tem
# o registro onde foi retirada, para quem for investigar uma falha.
RETIRADAS = [
    ("mais de 1.600 ações penais", "PT-53 — 1.618 é audiência de custódia"),
    ("+1.600 ações penais", "PT-53 — o total é 1.335"),
    ("1.402 condenados", "PT-61 — são responsabilizados, não condenados"),
    ("~4 mil", "PT-34 — sem lastro primário, retirada em 16/08/2026"),
    ("(9 km)", "PT-24 — a marcha é de 7,9 km"),
    ("(+100)", "PT-12 — 'mais de 100 acampamentos' retirado"),
    ("~1.200 presos", "PT-52 — são 2.151 em flagrante nos dias 8 e 9"),
    ("131 ações extintas", "PT-61 — ausente da camada de texto do balanço"),
    ("prorrog. 03/07/2026", "PT-60 — sem decisão no corpus que a sustente"),
    ("75 sub-eventos", "contagem antiga"),
    ("81 sub-eventos", "contagem antiga"),
]

BLOCO = re.compile(r'\{id:"([^"]+)"[\s\S]*?st:"(\w+)"\}')
CAMPO = r'{}:"((?:[^"\\]|\\.)*)"'


def campo(bloco, nome):
    m = re.search(CAMPO.format(nome), bloco)
    return m.group(1) if m else ""


def main():
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    J = {e["id"]: e for e in dados["eventos"]}
    n_json = int(dados["metadados"]["n_subeventos"])
    html = HTML_P.read_text(encoding="utf-8")
    svg = SVG_P.read_text(encoding="utf-8")

    falhas = []
    cobertos = set()

    print("CONFERÊNCIA FIGURAS x CODEBOOK")
    print("=" * 78)

    # 1-3. cobertura, etiqueta e procedência, registro a registro
    for b in BLOCO.finditer(html):
        bloco, hid, selo = b.group(0), b.group(1), b.group(2)
        ids = COMPOSTOS.get(hid, [hid])
        desconhecidos = [i for i in ids if i not in J]
        if desconhecidos:
            falhas.append("{}: id inexistente no codebook — {}".format(
                hid, ", ".join(desconhecidos)))
            continue
        cobertos.update(ids)

        esperado = min((CLASSE[J[i]["status_classe"]] for i in ids), key=FORCA.get)
        if selo != esperado:
            falhas.append("{}: selo '{}', codebook diz '{}'".format(hid, selo, esperado))

        if "fonte primária" in campo(bloco, "src").lower():
            nao = [i for i in ids if J[i]["status_classe"] != "Confirmado em fonte primária"]
            if nao:
                falhas.append("{}: a fonte diz 'fonte primária', mas {} não é".format(
                    hid, ", ".join(nao)))

    for i in J:
        if i not in cobertos:
            falhas.append("{}: ausente do HTML".format(i))

    print("  1. cobertura    : {}/{} registros do codebook".format(len(cobertos), len(J)))
    print("  2. etiqueta     : selo x status_classe")
    print("  3. procedência  : 'fonte primária' só onde o codebook confirma")

    # 4. cifras retiradas
    print("  4. cifras mortas: {} verbetes procurados no SVG".format(len(RETIRADAS)))
    for cifra, motivo in RETIRADAS:
        if cifra in svg:
            falhas.append("SVG ainda traz «{}» — {}".format(cifra, motivo))

    # contagem declarada nas duas peças
    if "{} sub-eventos".format(n_json) not in html:
        falhas.append("HTML não declara os {} sub-eventos do codebook".format(n_json))
    if "({} sub-eventos)".format(n_json) not in svg:
        falhas.append("SVG não declara os {} sub-eventos do codebook".format(n_json))

    print("=" * 78)
    if falhas:
        print("FALHAS — {}:".format(len(falhas)))
        for f in falhas:
            print("  X  {}".format(f))
        print("\nAs figuras não são geradas: corrija à mão em reports/figures/ e")
        print("rode de novo. O codebook é a fonte da verdade, nunca a figura.")
        return 1
    print("OK — as duas figuras batem com os {} registros do codebook".format(len(J)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
