#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PT-15 e PT-28: âncoras que a prosa declarava e o campo estruturado não tinha.

Achado em 25/09/2026 por `scripts/varrer_fonte_pagina.py`. Os dois registros
citavam, por extenso, páginas e documentos que o `fonte_pagina` e o
`fonte_local` não carregavam — e é o campo estruturado que a auditoria publica
e que o `conferir_paginas.py` abre no PDF.

PT-15 — a prosa diz "CPMI, p. 25, 53 e 274" e o campo trazia 25 e 53. A p. 274
foi lida antes desta correção: traz o atentado de 12/12/2022 e o pretexto
alegado, a prisão do cacique Tserere, que é exatamente o acréscimo que o
`status_verificacao` credita a ela.

PT-28 — o registro do *hoop test* citava DOIS documentos além da CPMI, sem
ancorar nenhum. Ambos foram lidos antes desta correção:

  Cappelli, p. 57, conclusão G — "o Comandante Geral da Polícia Militar do
  Distrito Federal esteve em campo atuando operacionalmente", "figurou entre
  os policiais militares feridos" e "perdeu a capacidade de liderar seus
  comandados diretos". É a contraprova que o mecanismo do registro discute.

  AP 2668, p. 495 e 497 — "a clara omissão de altos funcionários da Secretaria
  de Segurança Pública do Distrito Federal" e "a omissão dolosa do réu ANDERSON
  GUSTAVO TORRES também caracterizou o crime de golpe de Estado". É a moldura
  que o STF adotou, e que o registro reporta.

Por que o vínculo da AP 2668 sumiu: em 16/08/2026 o `fonte_local` de PT-28
apontava ERRADAMENTE para o acórdão no lugar da CPMI, e a correção daquela
rodada trocou um pelo outro em vez de somar. O `nota_auditoria` do registro
guarda esse histórico; esta rodada acrescenta o desfecho.

Nada de fato, status ou transcrição muda. Idempotente.

Uso:  python scripts/recodificar_ancoras_pt15_pt28.py [--dry-run]
"""

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

CPMI = "Fontes/04_T+1_Resposta-institucional/CPMI-8-de-Janeiro_Relatorio-Final_2023-10-17.pdf"
CAPPELLI = "Fontes/03_T0_8-de-janeiro/GDF-SSP_Relatorio-Interventor-Federal_Cappelli_2023-01-27.pdf"
AP2668 = "Fontes/04_T+1_Resposta-institucional/STF_AP-2668_Acordao_Condenacao_2025-09-11.pdf"

# id -> {campo: (valor esperado, valor novo)}
CORRECOES = {
    "PT-15": {
        "fonte_pagina": ("CPMI: 25, 53", "CPMI: 25, 53, 274"),
    },
    "PT-28": {
        "fonte_pagina": ("CPMI: 657", "CPMI: 657 | Cappelli: 57 | AP 2668: 495, 497"),
        "fonte_local": (CPMI, "; ".join([CPMI, CAPPELLI, AP2668])),
    },
}

NOTA_PT15 = (" ACRESCENTADO EM 25/09/2026: a p. 274, que o status_verificacao já nomeava, "
             "entrou no fonte_pagina. Divergência achada por scripts/varrer_fonte_pagina.py.")

NOTA_PT28 = (" ANCORAS ACRESCENTADAS EM 25/09/2026: o registro citava por extenso o Relatório "
             "do Interventor Federal (conclusão G, p. 57) e o acórdão da AP 2668 (p. 495 e 497) "
             "sem vincular nenhum dos dois. As três páginas foram lidas antes da correção. O "
             "vínculo da AP 2668 sumira na própria correção de 16/08/2026, que trocou o arquivo "
             "errado pelo certo em vez de somar os dois. Achado por "
             "scripts/varrer_fonte_pagina.py.")

REVISAO = ("2026-09-25 (PT-15, PT-28) — âncoras que a prosa declarava e o campo estruturado não "
           "tinha. PT-15: fonte_pagina passa de 'CPMI: 25, 53' para 'CPMI: 25, 53, 274'. PT-28: "
           "fonte_pagina passa de 'CPMI: 657' para 'CPMI: 657 | Cappelli: 57 | AP 2668: 495, "
           "497', e fonte_local passa a declarar os três arquivos. As quatro páginas novas foram "
           "lidas no PDF antes da correção. Nenhum fato, status ou transcrição alterado. "
           "Divergências achadas por scripts/varrer_fonte_pagina.py, que compara as páginas "
           "citadas na prosa dos registros com o campo fonte_pagina.")

NOTAS = {"PT-15": NOTA_PT15, "PT-28": NOTA_PT28}


def aplicar(dados):
    mudou = False
    for e in dados["eventos"]:
        campos = CORRECOES.get(e["id"])
        if not campos:
            continue
        for campo, (esperado, novo) in campos.items():
            atual = e.get(campo)
            if atual == novo:
                continue
            if atual != esperado:
                sys.exit("ABORTADO — {}.{} não está no estado esperado.\n  esperado: {!r}\n"
                         "  encontrado: {!r}".format(e["id"], campo, esperado, atual))
            e[campo] = novo
            mudou = True
            print("  {} {}: {!r} -> {!r}".format(e["id"], campo, esperado, novo))
        nota = NOTAS[e["id"]]
        atual = e.get("nota_auditoria") or ""
        if nota.strip() not in atual:
            e["nota_auditoria"] = (atual + nota).strip()
            mudou = True
            print("  {} nota_auditoria: registro da correção acrescentado".format(e["id"]))
    revisoes = dados["metadados"].setdefault("revisoes", [])
    if REVISAO not in revisoes:
        revisoes.append(REVISAO)
        mudou = True
        print("  metadados.revisoes: entrada de 25/09/2026 acrescentada")
    return mudou


def main():
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    if not aplicar(dados):
        print("nada a fazer — já aplicado")
        return 0
    if "--dry-run" in sys.argv:
        print("--dry-run: nada escrito")
        return 0
    # Sem `newline`: mantém o arquivo em CRLF, como as migrações anteriores.
    JSON_P.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8")
    print("JSON gravado. Rode:  bash scripts/ciclo.sh")
    return 0


if __name__ == "__main__":
    sys.exit(main())
