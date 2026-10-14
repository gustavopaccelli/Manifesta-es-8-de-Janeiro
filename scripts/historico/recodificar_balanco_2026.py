#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Incorporação do balanço "Democracia Inabalada" (29/04/2026) ao codebook.

O documento primário que faltava desde 16/08/2026 chegou: o Relatório do
Gabinete do Ministro Alexandre de Moraes sobre o 8 de Janeiro, 15 p., datado de
29/04/2026, obtido do bucket oficial do STF em S3 (noticias-stf-wp-prd).

Fecha PT-53 e PT-61, que estavam rebaixados a 'A verificar' e depois
reclassificados a 'Confirmado' com base apenas em cobertura jornalística.

CUIDADO DE LEITURA — o relatório é peça gráfica. Números em gráficos vetoriais
não saem na camada de texto: o gráfico "AÇÕES PENAIS" (p. 6 do PDF) e o
infográfico da p. 5 têm rótulos legíveis mas valores que NÃO extraem. Tudo o que
este script grava foi lido na camada de texto e conferido; nada foi inferido de
gráfico.

Uso:  python scripts/recodificar_balanco_2026.py [--dry-run]
"""

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

BAL = "Fontes/10_Democracia-Inabalada/STF_Gabinete-Moraes_Balanco-8-de-Janeiro_2026-04-29.pdf"

PT53 = {
    "repertorio_acao":
        "Inquéritos 4921 (crimes menos graves) e 4922 (crimes graves), Operação Lesa Pátria e "
        "ações penais decorrentes; 1.878 investigações instauradas",

    "fonte_trecho":
        "Relatório do Gabinete do Min. Alexandre de Moraes, 29/04/2026, p. 4, seções 'DADOS "
        "GERAIS - 8 DE JANEIRO' e 'INVESTIGAÇÕES INSTAURADAS'. Enquadramento legal, literal: "
        "'INQUÉRITO 4921 – CRIMES MENOS GRAVES: ARTIGOS 286, § ÚNICO E 288, CAPUT, AMBOS DO "
        "CÓDIGO PENAL'; o INQ 4922, de crimes graves, cobre os arts. 359-L, 359-M, 163 § único "
        "I-IV e 288 § único do CP, e o art. 62, I, da Lei 9.605/1998. Valores do gráfico de "
        "investigações instauradas: 1.878 (total); denúncias recebidas no Inquérito 4922 "
        "(Executores) 628; no Inquérito 4921 (Incitadores) 1.160; Núcleos Principais 31; "
        "investigação em andamento 177; denúncias em fase de recebimento 67; arquivamentos por "
        "ausência de justa causa 144. "
        "RESSALVA ARITMÉTICA, declarada e não resolvida: 628 + 1.160 + 31 = 1.819, e não "
        "1.878 — a diferença de 59 não é explicada na peça, e o rótulo do total é "
        "'investigações instauradas', não 'denúncias'. Não force a soma ao citar. "
        "RESSALVA DE LEITURA: o total de AÇÕES PENAIS está em gráfico vetorial na p. 6 do PDF "
        "(p. 10-11 do layout), cujos valores NÃO saem na camada de texto — a afirmação "
        "anterior de 'mais de 1.600 ações penais' precisa de leitura visual dessa página para "
        "ser confirmada ou corrigida.",

    "fonte_url":
        "https://noticias-stf-wp-prd.s3.sa-east-1.amazonaws.com/wp-content/uploads/wpallimport/"
        "uploads/2026/04/29155000/Relatorio_do_Gabinete_Alexandre_de_Moraes_08_de_janeiro____"
        "29-4-26-15h34.pdf",

    "fonte_local": BAL,
    "fonte_pagina": "Balanço 2026: 4",

    "status_verificacao":
        "Confirmado em fonte primária — Relatório do Gabinete do Min. Alexandre de Moraes "
        "(29/04/2026), p. 4, com os números de investigações instauradas e o enquadramento "
        "legal dos dois inquéritos. DUAS RESSALVAS DECLARADAS: (a) a soma das denúncias por "
        "inquérito não fecha com o total (1.819 x 1.878); (b) o total de ações penais está em "
        "gráfico vetorial não extraível e a cifra de 'mais de 1.600' segue sem confirmação — "
        "exige leitura visual da p. 6.",

    "status_classe": "Confirmado em fonte primária",

    "nota_auditoria":
        "PT-53 RESOLVIDO em 16/08/2026 com a chegada do documento primário. Corrigida também a "
        "fonte_url, que apontava para um balanço DIFERENTE (o de dois anos, 898 pessoas) do "
        "que o registro descrevia — inconsistência apontada na rodada anterior e agora sanada. "
        "Reclassificado de 'A verificar' para 'Confirmado em fonte primária'. Persiste a "
        "necessidade de leitura visual da p. 6 para o total de ações penais.",
}

PT61 = {
    "repertorio_acao":
        "Divulgação do balanço: 1.402 réus responsabilizados — 29 nos núcleos principais da "
        "organização criminosa, 402 por crimes graves, 419 por crimes menos graves e 552 "
        "ANPPs; 190 presos (10,12%)",

    "fonte_trecho":
        "Relatório do Gabinete do Min. Alexandre de Moraes, 29/04/2026. "
        "RÉUS RESPONSABILIZADOS (p. 6): '1.402' — 'NÚCLEOS PRINCIPAIS DA ORGANIZAÇÃO "
        "CRIMINOSA' 29; 'CRIMES GRAVES' 402; 'CRIMES MENOS GRAVES' 419; 'ANPPS (ACORDOS DE NÃO "
        "PERSECUÇÃO PENAL), COM CONFISSÃO DE CULPA' 552. A soma fecha: 29+402+419+552 = 1.402. "
        "SANÇÕES IMPOSTAS (p. 7): '431 PENAS PRIVATIVAS DE LIBERDADE, MULTA E DANOS MORAIS "
        "COLETIVOS NO VALOR DE R$ 30 MILHÕES' (30,7%); '419 PENAS PRIVATIVAS DE LIBERDADE "
        "CONVERTIDAS EM PRESTAÇÃO DE SERVIÇO À COMUNIDADE, RESTRITIVAS DE DIREITO E 20 DIAS "
        "MULTA NO VALOR DE ½ DO SALÁRIO MÍNIMO E DANOS MORAIS COLETIVOS NO VALOR DE R$ 5 "
        "MILHÕES' (29,9%); '552 ANPPS' (39,4%). "
        "PRISÕES ATUAIS (p. 10-11): '190 presos – 10,12% do total de réus', sendo 169 prisões "
        "definitivas (9%) e 21 processuais (1,12%). "
        "PENAS (p. 8, tabela demonstrativa): a mais alta é '27 ANOS E 3 MESES', aplicada a 1 "
        "réu (0,07%); 404 réus (28,82%) receberam 1 ano; 213 (15,19%) receberam 14 anos. "
        "NÚCLEOS (p. 13-14): 29 condenações penais nas APs 2668, 2693, 2694 e 2696; 21 sessões "
        "de julgamento entre setembro e dezembro; 31 réus julgados, com 25 condenações "
        "integrais, 2 parciais, 2 desclassificações e 2 absolvições; 127 advogadas e "
        "advogados; 154 testemunhas, sendo 8 de acusação e 146 de defesa. Núcleos nomeados: "
        "1-Crucial, 2-Estratégico, 3-Executores, 4-Desinformação.",

    "fonte_url":
        "https://noticias-stf-wp-prd.s3.sa-east-1.amazonaws.com/wp-content/uploads/wpallimport/"
        "uploads/2026/04/29155000/Relatorio_do_Gabinete_Alexandre_de_Moraes_08_de_janeiro____"
        "29-4-26-15h34.pdf",

    "fonte_local": BAL,
    "fonte_pagina": "Balanço 2026: 6, 7, 8, 10, 11, 13, 14",

    "status_verificacao":
        "Confirmado em fonte primária — Relatório do Gabinete do Min. Alexandre de Moraes "
        "(29/04/2026), documento obtido em 16/08/2026 do bucket oficial do STF. Os 1.402 "
        "réus, a composição por classe de crime, as sanções e os 190 presos estão todos na "
        "camada de texto do PDF e foram conferidos. RESSALVA: há divergência entre a tabela "
        "geral (p. 8, '27 ANOS E 3 MESES' para 1 réu) e a tabela dos núcleos (p. 13, '27 "
        "ANOS'), provavelmente arredondamento na peça gráfica — citar a p. 8, que é a tabela "
        "demonstrativa completa.",

    "status_classe": "Confirmado em fonte primária",

    "nota_auditoria":
        "PT-61 RESOLVIDO em 16/08/2026 com a chegada do documento primário, fornecido pelo "
        "pesquisador. Percorreu três estados no mesmo dia: 'Confirmado' (jornalístico) → "
        "rebaixado a 'A verificar' pela auditoria → 'Confirmado' por corroboração jornalística "
        "dupla → agora 'Confirmado em fonte primária'. A cifra de 1.402 pode ser citada como "
        "dado oficial, com página.",
}


def main():
    dry = "--dry-run" in sys.argv
    if not (RAIZ / BAL).exists():
        raise SystemExit("ERRO: balanço não encontrado em " + BAL)

    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    for ev in dados["eventos"]:
        if ev["id"] == "PT-53":
            print("=== PT-53 — antes ===")
            print("  classe :", ev["status_classe"], "| local:", ev.get("fonte_local"))
            ev.update(PT53)
            print("=== PT-53 — depois ===")
            print("  classe :", ev["status_classe"], "| pagina:", ev["fonte_pagina"])
        elif ev["id"] == "PT-61":
            print("\n=== PT-61 — antes ===")
            print("  classe :", ev["status_classe"], "| local:", ev.get("fonte_local"))
            ev.update(PT61)
            print("=== PT-61 — depois ===")
            print("  classe :", ev["status_classe"], "| pagina:", ev["fonte_pagina"])

    reg = dados["metadados"].setdefault("registro_documentos", {})
    reg["Balanço 2026"] = BAL

    dados["metadados"]["revisoes"] = [
        r for r in dados["metadados"]["revisoes"] if not r.startswith("2026-08-16 (balanço 2026)")
    ]
    dados["metadados"]["revisoes"].append(
        "2026-08-16 (balanço 2026) — incorporado o Relatório do Gabinete do Min. Alexandre de "
        "Moraes sobre o 8 de Janeiro (29/04/2026, 15 p.), obtido do bucket oficial do STF e "
        "fornecido pelo pesquisador. É o documento primário que faltava desde a auditoria: "
        "PT-53 e PT-61 passam a 'Confirmado em fonte primária', e a cifra de 1.402 réus "
        "responsabilizados pode ser citada como dado oficial, com página. Corrigida a "
        "fonte_url de PT-53, que apontava para um balanço diferente. DUAS RESSALVAS FICAM "
        "DECLARADAS, porque a peça é gráfica: (a) em PT-53, a soma das denúncias por inquérito "
        "(1.819) não fecha com o total de investigações instauradas (1.878); (b) o total de "
        "AÇÕES PENAIS está em gráfico vetorial cujos valores não saem na camada de texto, de "
        "modo que a afirmação de 'mais de 1.600 ações penais' segue pendente de leitura visual "
        "da p. 6."
    )

    if dry:
        print("\nDRY RUN — nada gravado")
    else:
        JSON_P.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("\nJSON reescrito.")


if __name__ == "__main__":
    main()
