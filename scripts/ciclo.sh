#!/usr/bin/env bash
# O ciclo completo, na ordem. Falha na primeira checagem que não passar.
#
# Substitui o Makefile que o padrão Cookiecutter Data Science prevê: não há
# make nesta máquina, e o ciclo é linear — catorze passos, sem grafo de
# dependências para resolver.
#
# Uso:  bash scripts/ciclo.sh            # amostra de 12 no passo 7
#       bash scripts/ciclo.sh --todos    # confere todos os registros com página
set -euo pipefail
cd "$(dirname "$0")/.."
export PYTHONIOENCODING=utf-8

echo "== 1/15  gerar_codebook — JSON -> data/processed/ (CSV + XLSX)"
python scripts/gerar_codebook.py

echo "== 2/15  gerar_auditoria — JSON -> reports/AUDITORIA-FONTES.md"
python scripts/gerar_auditoria.py

# A seção "Ordem de ataque" da agenda era escrita à mão e envelheceu três vezes
# em dezesseis dias — tarefa fechada listada como aberta, contagem de duas
# rodadas antes na linha que declarava os números como gerados. Agora sai de
# data/ordem_de_ataque.json, e as cifras saem de medição a cada ciclo.
echo "== 3/15  gerar_ordem_de_ataque — ledger -> docs/PENDENCIAS-ANALITICAS.md"
python scripts/gerar_ordem_de_ataque.py

# A TABELA-ESPELHO, acrescentada em 20/10/2026 a pedido do pesquisador. Ela
# responde o que o ciclo nao respondia: as figuras ainda dizem o que o codebook
# diz? conferir_figuras confere cobertura, selo, procedencia e cifra retirada --
# nao o texto do mecanismo (item 42.3). Gera antes das checagens para que a
# tabela esteja atual quando o passo 6 ler as figuras.
# AS DECISOES PENDENTES, acrescentado em 27/10/2026 (item 90). Irmao do passo
# anterior: um gera as TAREFAS abertas a partir do campo `estado`, este gera as
# DECISOES abertas do mesmo jeito. A razao tem data: em 25/10 a colheita das
# secoes "O que isto deixa" de cada item devolveu OITO pendencias ja resolvidas
# por itens posteriores -- aquelas secoes sao instantaneos datados, e o defeito
# era nao haver um lugar unico onde virar o bit. A guarda G-A confere que o
# ponteiro de secao de cada decisao EXISTE na agenda, porque ponteiro quebrado
# e a forma que o apodrecimento toma aqui.
echo "== 4/15  gerar_decisoes — ledger de decisoes -> docs/PENDENCIAS-ANALITICAS.md"
python scripts/gerar_decisoes.py
echo

# O PAINEL DE ESTADO, acrescentado em 27/10/2026 (item 91). Entra como ULTIMO
# gerador porque resume o que os outros produzem, e resumo vem depois do
# resumido. A razao de existir: o painel era escrito a mao, datava-se de 29/09,
# e a revisao do repositorio mediu que NENHUMA das suas cifras estava certa --
# inclusive uma que afirmava "sem remoto configurado" quando o remoto e
# PUBLICO, que e a premissa de toda a decisao de distribuicao de 21/10.
#
# Ele NAO repete a lista de tarefas nem de decisoes: aponta para as secoes que
# os passos irmaos geram, e DERIVA o numero de cada passo de `ciclo.sh` --
# porque numero de passo e a cifra que mais apodrece aqui, de oito a catorze em
# dezenove dias.
echo "== 5/15  gerar_painel — painel de estado -> docs/PENDENCIAS-ANALITICAS.md"
python scripts/gerar_painel.py
echo

echo "== 6/15  gerar_tabela_espelho — figuras x codebook -> reports/ + data/processed/"
python scripts/gerar_tabela_espelho.py

# A GRADE FUNCIONAL DO ENQUADRAMENTO, acrescentada em 21/10/2026 a pedido do
# pesquisador. Ela e INFERENCIA declarada, nao dado -- e esta no ciclo por uma
# razao so: as tres guardas internas dela pegam deriva. Se um registro entrar ou
# sair, ou se um campo `framing_narrativa` deixar de ser vazio, o gerador cai e o
# documento nao envelhece em silencio, que e o modo de falha batizado daqui.
# AS DIADES DO PROCESSO, acrescentado em 29/10/2026 (item 104). Ele existe para
# uma pergunta que nenhuma guarda fazia: **a declaracao de par e reciproca?** A
# checagem 6 confere que a remissao aponta para registro existente; so este
# passo confere que, se A declara diade com B, B declara com A -- que e a
# diferenca entre `vide tambem` e uma afirmacao sobre a estrutura do conflito.
echo "== 7/15  gerar_diades — pares do processo -> reports/TABELA-DIADES.md"
python scripts/gerar_diades.py
echo

echo "== 8/15  gerar_grade_enquadramento — inferencia funcional -> docs/referencial/"
python scripts/gerar_grade_enquadramento.py
echo

# O REGISTRO DE ESTADO DE LEITURA, acrescentado em 21/10/2026 a pedido do
# pesquisador, e a razao tem data: horas antes eu havia relatado seis verbetes
# como "lidos-a-ler" quando os seis estavam LIDOS, porque copiei uma lista de
# 30/09 do documento que PEDIA a leitura em vez do que a REGISTRAVA. O estado de
# leitura vivia em prosa espalhada por sete documentos e nada aqui conferia.
# A guarda G2 dele e a que faltava: nenhum documento pode afirmar nao-leitura de
# peca cujo estado e de leitura. Roda depois da grade porque nao depende dela, e
# antes das checagens estruturais porque e gerador.
echo "== 9/15  gerar_registro_leitura — estado de leitura -> docs/referencial/"
python scripts/gerar_registro_leitura.py
echo

echo "== 10/15  verificar_integridade — dez checagens estruturais"
python scripts/verificar_integridade.py

echo "== 11/15  conferir_figuras — as figuras de reports/figures/ x codebook"
python scripts/conferir_figuras.py

echo "== 12/15  conferir_relatorio — o relatório de pesquisa x codebook"
python scripts/conferir_relatorio.py

echo "== 13/15  conferir_paginas — transcrição x página no PDF"
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
echo "== 14/15  desenhar_campo --autoteste — o campo x codebook"
python scripts/desenhar_campo.py --autoteste

# O documento 11 cita registro e página à mão. Duas citações da primeira versão
# foram escritas por dedução de vizinhança, e estavam erradas — esta é a
# checagem que impede a terceira.
echo "== 15/15  conferir_hipoteses — o documento 11 x codebook"
python scripts/conferir_hipoteses.py

echo "== OK — ciclo completo sem falhas"
