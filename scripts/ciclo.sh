#!/usr/bin/env bash
# O ciclo completo, na ordem. Falha na primeira checagem que não passar.
#
# Substitui o Makefile que o padrão Cookiecutter Data Science prevê: não há
# make nesta máquina, e o ciclo é linear — onze passos, sem grafo de
# dependências para resolver.
#
# Uso:  bash scripts/ciclo.sh            # amostra de 12 no passo 7
#       bash scripts/ciclo.sh --todos    # confere todos os registros com página
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONIOENCODING=utf-8

echo "== 1/11  gerar_codebook — JSON -> data/processed/ (CSV + XLSX)"
python scripts/gerar_codebook.py

echo "== 2/11  gerar_auditoria — JSON -> reports/AUDITORIA-FONTES.md"
python scripts/gerar_auditoria.py

# A seção "Ordem de ataque" da agenda era escrita à mão e envelheceu três vezes
# em dezesseis dias — tarefa fechada listada como aberta, contagem de duas
# rodadas antes na linha que declarava os números como gerados. Agora sai de
# data/ordem_de_ataque.json, e as cifras saem de medição a cada ciclo.
echo "== 3/11  gerar_ordem_de_ataque — ledger -> docs/PENDENCIAS-ANALITICAS.md"
python scripts/gerar_ordem_de_ataque.py

# A TABELA-ESPELHO, acrescentada em 20/10/2026 a pedido do pesquisador. Ela
# responde o que o ciclo nao respondia: as figuras ainda dizem o que o codebook
# diz? conferir_figuras confere cobertura, selo, procedencia e cifra retirada --
# nao o texto do mecanismo (item 42.3). Gera antes das checagens para que a
# tabela esteja atual quando o passo 6 ler as figuras.
echo "== 4/11  gerar_tabela_espelho — figuras x codebook -> reports/ + data/processed/"
python scripts/gerar_tabela_espelho.py

# A GRADE FUNCIONAL DO ENQUADRAMENTO, acrescentada em 21/10/2026 a pedido do
# pesquisador. Ela e INFERENCIA declarada, nao dado -- e esta no ciclo por uma
# razao so: as tres guardas internas dela pegam deriva. Se um registro entrar ou
# sair, ou se um campo `framing_narrativa` deixar de ser vazio, o gerador cai e o
# documento nao envelhece em silencio, que e o modo de falha batizado daqui.
echo "== 5/11  gerar_grade_enquadramento — inferencia funcional -> docs/referencial/"
python scripts/gerar_grade_enquadramento.py
echo

echo "== 6/11  verificar_integridade — oito checagens estruturais"
python scripts/verificar_integridade.py

echo "== 7/11  conferir_figuras — as figuras de reports/figures/ x codebook"
python scripts/conferir_figuras.py

echo "== 8/11  conferir_relatorio — o relatório de pesquisa x codebook"
python scripts/conferir_relatorio.py

echo "== 9/11  conferir_paginas — transcrição x página no PDF"
# --todos por padrao desde 10/10/2026: a linha de base de casamento parcial
# (PARCIAIS_BASE) so vale no conjunto completo, e e ela que pega transcricao
# editada na cauda -- a falha que escapou da prova negativa de 09/10. Guarda
# que nao esta no caminho percorrido todo dia nao guarda nada. Um argumento
# explicito na linha de comando continua prevalecendo.
if [ $# -eq 0 ]; then set -- --todos; fi
python scripts/conferir_paginas.py "$@"

# O campo multiorganizacional declara entidades por fragmento de `ator_grupo` e
# `target_alvo`. Se um registro for reescrito, o fragmento deixa de ocorrer e o
# --autoteste aborta — é a checagem que impede a peça de envelhecer em silêncio.
echo "== 10/11  desenhar_campo --autoteste — o campo x codebook"
python scripts/desenhar_campo.py --autoteste

# O documento 11 cita registro e página à mão. Duas citações da primeira versão
# foram escritas por dedução de vizinhança, e estavam erradas — esta é a
# checagem que impede a terceira.
echo "== 11/11  conferir_hipoteses — o documento 11 x codebook"
python scripts/conferir_hipoteses.py

echo "== OK — ciclo completo sem falhas"
