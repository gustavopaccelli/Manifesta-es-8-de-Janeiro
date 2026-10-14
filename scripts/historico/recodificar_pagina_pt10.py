#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PT-10: `fonte_pagina` tinha perdido a p. 1021 da CPMI.

Achado em 25/09/2026 por `scripts/conferir_relatorio.py`, na primeira execução:
a tabela da Etapa 2 do relatório cita "CPMI, p. 999, 1021 e 1023" e o campo
`fonte_pagina` do registro trazia apenas "CPMI: 999, 1023". A divergência não
era do relatório.

O próprio registro nomeia as três páginas em `fonte_trecho` e em
`status_verificacao` — só o campo estruturado, que é o que as ferramentas leem,
tinha ficado com duas. A p. 1021 foi lida no PDF antes desta correção e sustenta
a afirmação: ali o diretor-geral da PRF declara que "essa foi, talvez, a maior
manifestação do mundo, com 1,3 mil bloqueios montados" — a mesma cifra que a
p. 999 registra como "um total de 1.300 pontos de interdição no País", em outra
passagem do mesmo depoimento.

Nada além do campo de páginas muda. Idempotente: rodar duas vezes não duplica.

Uso:  python scripts/recodificar_pagina_pt10.py [--dry-run]
"""

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

ANTES = "CPMI: 999, 1023"
DEPOIS = "CPMI: 999, 1021, 1023"
REVISAO = ("2026-09-25 (PT-10) — fonte_pagina corrigido de 'CPMI: 999, 1023' para "
           "'CPMI: 999, 1021, 1023'. A p. 1021 era nomeada em fonte_trecho e em "
           "status_verificacao e faltava no campo estruturado; foi lida no PDF e "
           "sustenta a cifra dos bloqueios ('1,3 mil bloqueios montados'). Divergência "
           "achada por scripts/conferir_relatorio.py, na primeira execução.")


def aplicar(dados):
    mudou = False
    for e in dados["eventos"]:
        if e["id"] == "PT-10" and e.get("fonte_pagina") == ANTES:
            e["fonte_pagina"] = DEPOIS
            mudou = True
            print("  PT-10 fonte_pagina: {!r} -> {!r}".format(ANTES, DEPOIS))
    revisoes = dados["metadados"].setdefault("revisoes", [])
    if REVISAO not in revisoes:
        revisoes.append(REVISAO)
        mudou = True
        print("  metadados.revisoes: entrada de 25/09/2026 acrescentada")
    return mudou


def main():
    seco = "--dry-run" in sys.argv
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    if not aplicar(dados):
        print("nada a fazer — já aplicado")
        return 0
    if seco:
        print("--dry-run: nada escrito")
        return 0
    # Sem `newline`: é o que as migrações anteriores fizeram, e é o que mantém
    # o arquivo em CRLF nesta máquina. Forçar "\n" reescreveria o arquivo
    # inteiro e o diff engoliria a mudança de uma linha.
    JSON_P.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8")
    print("JSON gravado. Rode:  bash scripts/ciclo.sh")
    return 0


if __name__ == "__main__":
    sys.exit(main())
