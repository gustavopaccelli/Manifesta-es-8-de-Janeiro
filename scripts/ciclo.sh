#!/usr/bin/env bash
# O ciclo completo, na ordem. Falha na primeira checagem que não passar.
#
# Substitui o Makefile que o padrão Cookiecutter Data Science prevê: não há
# make nesta máquina, e o ciclo é linear — quatro passos, sem grafo de
# dependências para resolver.
#
# Uso:  bash scripts/ciclo.sh            # amostra de 12 no passo 6
#       bash scripts/ciclo.sh --todos    # confere todos os registros com página
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONIOENCODING=utf-8

echo "== 1/7  gerar_codebook — JSON -> data/processed/ (CSV + XLSX)"
python scripts/gerar_codebook.py

echo "== 2/7  gerar_auditoria — JSON -> reports/AUDITORIA-FONTES.md"
python scripts/gerar_auditoria.py

echo "== 3/7  verificar_integridade — seis checagens estruturais"
python scripts/verificar_integridade.py

echo "== 4/7  conferir_figuras — as figuras de reports/figures/ x codebook"
python scripts/conferir_figuras.py

echo "== 5/7  conferir_relatorio — o relatório de pesquisa x codebook"
python scripts/conferir_relatorio.py

echo "== 6/7  conferir_paginas — transcrição x página no PDF"
python scripts/conferir_paginas.py "$@"

# O campo multiorganizacional declara entidades por fragmento de `ator_grupo` e
# `target_alvo`. Se um registro for reescrito, o fragmento deixa de ocorrer e o
# --autoteste aborta — é a checagem que impede a peça de envelhecer em silêncio.
echo "== 7/7  desenhar_campo --autoteste — o campo x codebook"
python scripts/desenhar_campo.py --autoteste

echo "== OK — ciclo completo sem falhas"
