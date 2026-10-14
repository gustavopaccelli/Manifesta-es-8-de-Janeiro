#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PT-02A e PT-03A: páginas erradas, achadas quando o conferidor endureceu.

Em 25/09/2026 o `scripts/conferir_paginas.py` passou a exigir que TODA
transcrição literal do registro seja localizada em ALGUMA página listada — antes
bastava uma casar e ele parava ali. Na primeira execução sob a regra nova, dois
registros reprovaram, e nos dois a página estava errada.

PT-02A — o registro citava "p. 3 e 9 do inteiro teor". A p. 3 é a autuação, a
folha de rosto com a lista de partes e advogados. O relatório do min. Marco
Aurélio começa na p. 6, e é ali que está a frase transcrita: "ocorrida após o
julgamento, pelo Plenário, do habeas corpus nº 126.292, relator o ministro Teori
Zavascki". A segunda transcrição, na p. 9, estava certa.

PT-03A — o registro ancorava só a p. 395, onde está o dispositivo da sentença.
A segunda transcrição, "a sentença condenou o ex-presidente por um único ato de
corrupção", está na **p. 348** do mesmo volume; o texto dizia apenas "o mesmo
volume registra", sem página. Acrescentada a página e nomeada no texto.

As duas páginas novas foram lidas no PDF antes desta correção. Nenhum fato,
status ou transcrição muda — só o número da página e a referência a ela.
Idempotente.

Uso:  python scripts/recodificar_paginas_pt02a_pt03a.py [--dry-run]
"""

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

# id -> [(campo, trecho antigo, trecho novo)]; substituição literal, uma vez.
CORRECOES = {
    "PT-02A": [
        ("fonte_pagina", "ADC 43/44/54: 3, 9", "ADC 43/44/54: 6, 9"),
        ("fonte_trecho",
         "Acórdão das ADC 43/44/54 (STF, 07/11/2019), p. 3 e 9 do inteiro teor",
         "Acórdão das ADC 43/44/54 (STF, 07/11/2019), p. 6 e 9 do inteiro teor"),
    ],
    "PT-03A": [
        ("fonte_pagina", "TRF-4: 395", "TRF-4: 348, 395"),
        ("fonte_trecho",
         "O mesmo volume registra que 'a sentença condenou o ex-presidente por um único "
         "ato de corrupção'.",
         "O mesmo volume registra, na p. 348, que 'a sentença condenou o ex-presidente por "
         "um único ato de corrupção'."),
    ],
}

NOTAS = {
    "PT-02A": (" CORREÇÃO DE PÁGINA EM 25/09/2026: o registro citava a p. 3 do acórdão das "
               "ADC 43/44/54, que é a autuação — folha de rosto com partes e advogados. A "
               "transcrição está na p. 6, onde começa o relatório do min. Marco Aurélio. "
               "Achado pelo conferir_paginas.py, na primeira execução sob a regra que exige "
               "localizar TODAS as transcrições."),
    "PT-03A": (" PÁGINA ACRESCENTADA EM 25/09/2026: a segunda transcrição do registro está na "
               "p. 348 do mesmo volume, e o campo ancorava apenas a p. 395, do dispositivo. "
               "Achado pelo conferir_paginas.py, na primeira execução sob a regra que exige "
               "localizar TODAS as transcrições."),
}

REVISAO = ("2026-09-25 (PT-02A, PT-03A) — correção de página, achada pelo conferir_paginas.py "
           "endurecido. PT-02A: 'ADC 43/44/54: 3, 9' passa a '6, 9' — a p. 3 é a autuação e a "
           "transcrição está na p. 6, onde começa o relatório. PT-03A: 'TRF-4: 395' passa a "
           "'348, 395' — a segunda transcrição está na p. 348 do volume. As duas páginas foram "
           "lidas no PDF antes da correção; nenhum fato, status ou transcrição alterado.")


def aplicar(dados):
    mudou = False
    for e in dados["eventos"]:
        itens = CORRECOES.get(e["id"])
        if not itens:
            continue
        for campo, antigo, novo in itens:
            atual = e.get(campo) or ""
            if novo in atual:
                continue
            if antigo not in atual:
                sys.exit("ABORTADO — {}.{} não contém o texto esperado:\n  {!r}".format(
                    e["id"], campo, antigo))
            e[campo] = atual.replace(antigo, novo, 1)
            mudou = True
            print("  {} {}: {!r} -> {!r}".format(e["id"], campo, antigo[:60], novo[:60]))
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
