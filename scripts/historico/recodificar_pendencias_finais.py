#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fecha as duas pendências abertas pela rodada do balanço, e consolida a duplicata.

Rodada de 16/08/2026.

PENDÊNCIA 1 — valoração do dano ao STF (PT-38).
  A cifra de R$ 11,4 mi vinha só da sinopse do documentário (ago/2023) e NÃO
  está no livro de 210 p., no balanço de 2026 nem na CPMI — os três foram
  varridos. A busca em imprensa mostrou que ela foi SUPERADA: o levantamento
  final do STF chega a ~R$ 12 mi (R$ 8.616.822,30 de prejuízo direto mais
  R$ 3.424.600,25 de reconstrução do Plenário). Entra como SÉRIE DATADA, com
  atribuição, nunca como número único — repetir "R$ 11,4 mi" seria o mesmo erro
  do "4 mil" de PT-34.

PENDÊNCIA 2 — gráfico de ações penais do balanço (PT-53).
  Resolvida por renderização da página (PyMuPDF), já que os valores são
  vetoriais e não saem na camada de texto. RESULTADO QUE CORRIGE O REGISTRO: o
  total de ações penais é 1.335, e não "mais de 1.600". O 1.618 que circulava é
  de AUDIÊNCIAS DE CUSTÓDIA (p. 5), não de ações penais. Mesmo padrão de PT-34,
  PT-12 e PT-28: número aplicado ao referente errado.

CONSOLIDAÇÃO — o ebook duplicado.
  Mantida a cópia recém-baixada do domínio oficial em 10_Democracia-Inabalada/;
  removida a de 03_T0_8-de-janeiro/. PT-38 é repontado. Os arquivos eram
  byte-idênticos, então nenhum conteúdo se perde.

Uso:  python scripts/recodificar_pendencias_finais.py [--dry-run]
"""

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

ANTIGO = "Fontes/03_T0_8-de-janeiro/STF_Livro-8-1-2023-democraciainabalada_2023_vandalismo-e-restauracao.pdf"
NOVO = "Fontes/10_Democracia-Inabalada/STF_Democracia-Inabalada_Ebook_28x28cm.pdf"
BAL = "Fontes/10_Democracia-Inabalada/STF_Gabinete-Moraes_Balanco-8-de-Janeiro_2026-04-29.pdf"

PT38 = {
    "resposta_estatal":
        "Sem proteção do acervo durante o ataque; restauração posterior conduzida pelo próprio "
        "STF, com 106 itens declarados de valor imensurável e irrecuperáveis",

    "fonte_trecho":
        "Livro oficial do STF '8.1.2023: Democracia Inabalada' (ago/2023, 210 p.), sobre o "
        "vandalismo e a restauração do acervo. Detalhamento por peça exige o laudo pericial do "
        "Instituto de Criminalística/PF, não obtido — a perícia seguia sem prazo definido em "
        "set/2023. "
        "VALORAÇÃO DO DANO, acrescentada em 16/08/2026 como SÉRIE DATADA e não como cifra "
        "única, porque o número foi revisto ao longo do tempo: (a) ago/2023 — a sinopse oficial "
        "do documentário 'Democracia Inabalada' declara que 'somente no STF, o prejuízo "
        "financeiro chegou a R$ 11,4 milhões'; (b) jan/2025 — levantamento do STF divulgado "
        "pela imprensa eleva o total a cerca de R$ 12 milhões, decompostos em R$ 8.616.822,30 "
        "de prejuízo direto e R$ 3.424.600,25 de reconstrução do Plenário, com 951 itens "
        "'furtados, quebrados ou completamente destruídos' e 106 itens históricos de valor "
        "imensurável. Para contexto, o mesmo levantamento aponta R$ 4,9 mi no Congresso "
        "(R$ 2,7 mi na Câmara e R$ 2,2 mi no Senado) e R$ 4,3 mi no Planalto. "
        "RESSALVA: NENHUM documento primário do corpus traz esses valores — nem o livro do STF "
        "(varrido), nem o balanço de 2026 (varrido), nem o Relatório Final da CPMI (varrido). "
        "A série está em fonte jornalística com atribuição ao STF. Citar sempre com a data, "
        "porque a cifra de 2023 foi superada.",

    "fonte_local": NOVO,
    "fonte_pagina": "Livro STF 2023: inteiro teor",

    "status_verificacao":
        "Confirmado em linha geral quanto ao vandalismo e à restauração — livro oficial do STF. "
        "Detalhamento por peça segue dependendo do laudo do Instituto de Criminalística/PF, não "
        "obtido. VALORAÇÃO DO DANO acrescentada em 16/08/2026 como série datada (R$ 11,4 mi em "
        "ago/2023 → ~R$ 12 mi em jan/2025), apoiada em imprensa com atribuição ao STF e SEM "
        "lastro em documento primário do corpus. Não citar valor único sem a data.",

    "nota_auditoria":
        "PT-38, 16/08/2026: (a) repontado para a cópia consolidada do livro em "
        "10_Democracia-Inabalada/, após a remoção da duplicata byte-idêntica que estava em "
        "03_T0_8-de-janeiro/; (b) acrescentada a valoração do dano como série datada. O valor "
        "de R$ 11,4 mi, que vinha da sinopse do documentário, NÃO foi adotado como cifra final "
        "— foi superado pelo levantamento de ~R$ 12 mi. Nenhum documento primário do corpus "
        "carrega esses números; a busca no livro, no balanço e na CPMI foi exaustiva e negativa.",
}

PT53_PATCH = {
    "repertorio_acao":
        "Inquéritos 4921 (crimes menos graves) e 4922 (crimes graves), Operação Lesa Pátria e "
        "1.335 ações penais decorrentes; 1.878 investigações instauradas",

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
        "AÇÕES PENAIS — gráfico da p. 6, lido por renderização da página em 16/08/2026 (os "
        "valores são vetoriais e não saem na camada de texto). Por situação, em Crimes Menos "
        "Graves / Crimes Graves e Núcleos Principais / Total: condenações 419 / 431 / 850; "
        "absolvições 8 / 8 / 16; instrução em andamento 192 / 267 / 459; extinções de "
        "punibilidade pelo art. 107, I, 5 / 5 / 10. TOTAL DE AÇÕES PENAIS: 1.335. "
        "ATOS PROCESSUAIS — gráfico da p. 5, por ano (2023/2024/2025/2026/total): audiências de "
        "custódia 1.397/137/51/33 = 1.618; audiências de instrução 232/860/187/50 = 1.329; "
        "oitivas de testemunhas de acusação 719/1.660/143/51 = 2.573; oitivas de testemunhas de "
        "defesa 386/980/287/90 = 1.743; interrogatórios judiciais dos réus 232/860/187/50 = "
        "1.329. "
        "COERÊNCIA INTERNA, conferida: 850 condenações em ações penais + 552 ANPPs = 1.402 réus "
        "responsabilizados; e 431 (crimes graves e núcleos) = 29 núcleos + 402 crimes graves. "
        "CORREÇÃO DE 16/08/2026 — a afirmação anterior de 'mais de 1.600 ações penais' está "
        "ERRADA e foi retirada: o total é 1.335. O número 1.618 que circulava refere-se a "
        "AUDIÊNCIAS DE CUSTÓDIA (p. 5), não a ações penais. Mesmo padrão de PT-34, PT-12 e "
        "PT-28: cifra correta aplicada ao referente errado. "
        "RESSALVA ARITMÉTICA remanescente, declarada e não resolvida: 628 + 1.160 + 31 = 1.819, "
        "e não 1.878 — a diferença de 59 não é explicada na peça, e o rótulo do total é "
        "'investigações instauradas', não 'denúncias'. Não force a soma ao citar.",

    "fonte_pagina": "Balanço 2026: 4, 5, 6",

    "status_verificacao":
        "Confirmado em fonte primária — Relatório do Gabinete do Min. Alexandre de Moraes "
        "(29/04/2026), p. 4, 5 e 6. Os gráficos vetoriais das p. 5 e 6 foram lidos por "
        "renderização em 16/08/2026, o que fechou a última pendência de leitura. RESSALVA "
        "ÚNICA remanescente: a soma das denúncias por inquérito não fecha com o total "
        "(1.819 × 1.878), divergência da própria peça.",

    "nota_auditoria":
        "PT-53 RESOLVIDO em 16/08/2026 com o documento primário, e CORRIGIDO no mesmo dia: a "
        "cifra de 'mais de 1.600 ações penais' foi retirada por estar errada — o total é 1.335. "
        "O 1.618 pertence a audiências de custódia. A leitura dos gráficos vetoriais exigiu "
        "renderização da página; a camada de texto não os entrega. Corrigida também a "
        "fonte_url, que apontava para um balanço diferente.",
}


def main():
    dry = "--dry-run" in sys.argv
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))

    for ev in dados["eventos"]:
        if ev["id"] == "PT-38":
            print("=== PT-38 ===")
            print("  local antes :", ev.get("fonte_local"))
            ev.update(PT38)
            print("  local depois:", ev["fonte_local"])
        elif ev["id"] == "PT-53":
            print("\n=== PT-53 ===")
            print("  antes : repertorio menciona 'mais de 1.600'?",
                  "mais de 1.600" in (ev.get("repertorio_acao") or ""))
            ev.update(PT53_PATCH)
            print("  depois: 1.335 ações penais | pagina:", ev["fonte_pagina"])

    reg = dados["metadados"].setdefault("registro_documentos", {})
    reg["Livro STF 2023"] = NOVO
    reg["Balanço 2026"] = BAL

    dados["metadados"]["revisoes"] = [
        r for r in dados["metadados"]["revisoes"]
        if not r.startswith("2026-08-16 (pendências finais)")
    ]
    dados["metadados"]["revisoes"].append(
        "2026-08-16 (pendências finais) — três movimentos. (1) PT-53 CORRIGIDO: os gráficos "
        "vetoriais do balanço foram lidos por renderização de página, e o total de ações penais "
        "é 1.335, não 'mais de 1.600'; o 1.618 que circulava é de audiências de custódia. É o "
        "quarto caso do projeto de cifra correta aplicada ao referente errado, depois de PT-34, "
        "PT-12 e PT-28. (2) PT-38 recebeu a valoração do dano ao STF como SÉRIE DATADA "
        "(R$ 11,4 mi em ago/2023 → ~R$ 12 mi em jan/2025, com 951 itens danificados e 106 "
        "imensuráveis), com a ressalva de que nenhum documento primário do corpus a carrega — "
        "livro, balanço e CPMI foram varridos sem resultado. (3) A duplicata byte-idêntica do "
        "livro do STF foi consolidada: mantida a cópia baixada do domínio oficial em "
        "10_Democracia-Inabalada/, removida a de 03_T0_8-de-janeiro/, e PT-38 repontado."
    )

    if dry:
        print("\nDRY RUN — nada gravado")
    else:
        JSON_P.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("\nJSON reescrito.")


if __name__ == "__main__":
    main()
