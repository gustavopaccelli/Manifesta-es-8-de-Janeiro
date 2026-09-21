#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Resolução de PT-52 — qual número de detidos lidera o texto.

Rodada de 16/08/2026. A pendência estava aberta desde a rodada das ressalvas,
quando se constatou que "~1.200 em 40 ônibus" (imprensa) e "2.151 presas"
(CPMI p. 688) mediam coisas diferentes e não podiam ser unificadas à força.

DECISÃO: 2.151 LIDERA, com o escopo corrigido para "8 e 9 de janeiro".

Três razões:
  1. PROVENIÊNCIA — 2.151 é primária, aparece duas vezes na CPMI (p. 76 e 688).
     Os ~1.200 são de imprensa, atribuídos ao então ministro Flávio Dino.
  2. NATUREZA DA MEDIDA — 2.151 é contagem fechada. Os ~1.200 são recorte de
     meio de manhã de uma operação em curso, que a própria reportagem registra
     subindo para ~2.000 à tarde. Liderar com o parcial subestimaria em quase
     metade.
  3. PERTINÊNCIA AO MECANISMO — PT-52 afirma destruição da infraestrutura de
     mobilização. O que faz trabalho causal é quantas pessoas foram removidas
     do acampamento, não a logística de transporte até a triagem.

CORREÇÃO DE ESCOPO, que é o achado desta rodada. A CPMI se contradiz sobre o
que os 2.151 cobrem:
  - p. 76 (precisa):  "2.151 pessoas presas em flagrante, no próprio domingo OU
                       NO DIA SEGUINTE, durante a desocupação do acampamento"
  - p. 688 (comprime): "No ato de desocupação, foram presas 2.151 pessoas"
A p. 76 é a formulação boa: o número cobre 8/1 (prédios) E 9/1 (acampamento).
Citar 2.151 como "presos na desocupação" — o que a p. 688 sugere e o registro
fazia — SUPERESTIMA o dia 9. O texto passa a dizer "nas prisões em flagrante do
8 e 9 de janeiro, a maior parte na desocupação".

GANHO ANALÍTICO: o funil. Cruzando CPMI e balanço de 2026, ~35% dos flagrantes
não converteram em processo. Ver o campo mecanismo_causal.

Uso:  python scripts/recodificar_pt52.py [--dry-run]
"""

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

CPMI = "Fontes/04_T+1_Resposta-institucional/CPMI-8-de-Janeiro_Relatorio-Final_2023-10-17.pdf"
CAPP = "Fontes/03_T0_8-de-janeiro/GDF-SSP_Relatorio-Interventor-Federal_Cappelli_2023-01-27.pdf"
BAL = "Fontes/10_Democracia-Inabalada/STF_Gabinete-Moraes_Balanco-8-de-Janeiro_2026-04-29.pdf"

PT52 = {
    "repertorio_acao":
        "Desmonte do acampamento do SMU em cumprimento a decisão do STF; das cerca de 3.000 "
        "pessoas no local, 1.500 saíram por conta própria e as demais foram levadas à triagem "
        "na Academia Nacional de Polícia. O 8 e 9 de janeiro somam 2.151 prisões em flagrante, "
        "a maior parte delas nesta desocupação",

    "mecanismo_causal":
        "Destruição da infraestrutura de mobilização — mecanismo decisivo do desfecho: "
        "eliminada a base logística, o ciclo de rua se encerra materialmente, não por "
        "convencimento, mas por remoção da capacidade de agir. A fonte primária acrescenta dois "
        "elementos. O primeiro fecha a discussão sobre a omissão militar: a CPMI afirma que a "
        "decisão judicial 'nem sequer era necessária para a desocupação da área pelo Exército' "
        "— o que retira validade à alegação de que faltava ordem judicial para desmontar o "
        "acampamento. O segundo é a conclusão do próprio interventor federal, de que a "
        "permanência do acampamento 'permitiu apoio logístico e local de concentração' para as "
        "ações do dia 8: é certificação oficial, e não apenas do analista, da tese de que o "
        "acampamento era infraestrutura de mobilização. "
        "FUNIL DA RESPONSABILIZAÇÃO (acrescentado em 16/08/2026, ao cruzar a CPMI com o balanço "
        "de 2026): das 2.151 prisões em flagrante saíram 1.397 audiências de custódia em 2023 "
        "(Balanço, p. 5), 1.390 denúncias do MPF até out/2023 (CPMI, p. 76) e 1.402 réus "
        "responsabilizados até abr/2026 (Balanço, p. 6). Três medições independentes convergem "
        "na casa de 1.400, e cerca de 750 flagrantes — perto de 35% — não converteram em "
        "processo. A repressão de massa do dia 9 é, portanto, mais ampla que a "
        "responsabilização que dela resultou: prender no acampamento e responsabilizar "
        "judicialmente são operações de escalas distintas, e a diferença é o que separa a "
        "desmobilização do repertório da punição de seus agentes.",

    "fonte_trecho":
        "Relatório Final da CPMI, p. 576: 'O acampamento golpista em Brasília só seria desfeito "
        "no dia 9 de janeiro, e tão somente em cumprimento a uma decisão judicial que, como "
        "assinalado, nem sequer era necessária para a desocupação da área pelo Exército.' Em "
        "fonte primária direta, Relatório do Interventor Federal, conclusão A, p. 53: 'A "
        "permanência do acampamento na Praça dos Cristais no Setor Militar Urbano permitiu "
        "apoio logístico e local de concentração aos manifestantes que se deslocaram a Brasília "
        "para que as ações do dia 08 fossem desencadeadas, sendo verificada, desde o dia 07 de "
        "janeiro de 2023, a chegada de vários ônibus vindo de fora de Brasília.' "
        "OPERAÇÃO — CPMI, p. 687: 'Os policiais chegaram por volta das 8 horas e estabeleceram o "
        "prazo de uma hora para a desocupação voluntária do acampamento. Das cerca de 3.000 "
        "pessoas que estavam no local, 1.500 deixaram o espaço por conta própria; as restantes "
        "foram levadas para a triagem na Academia Nacional de Polícia.' "
        "PRISÕES — CPMI, p. 76, na formulação PRECISA: 'O Oito de Janeiro resultou em 2.151 "
        "pessoas presas em flagrante, no próprio domingo ou no dia seguinte, durante a "
        "desocupação do acampamento golpista em frente ao quartel-general do Exército em "
        "Brasília.' A p. 688 comprime a mesma cifra em 'No ato de desocupação, foram presas "
        "2.151 pessoas' — formulação que atribui ao dia 9 o que a p. 76 distribui entre os dias "
        "8 e 9. ADOTADA A P. 76. "
        "RESOLUÇÃO DE 16/08/2026 — a cifra de '~1.200 em 40 ônibus' foi RETIRADA da posição "
        "principal. Ela vem da imprensa (Poder360, 09/01/2023, atribuída ao então ministro "
        "Flávio Dino), mede pessoas levadas à triagem nas primeiras levas da manhã, e a própria "
        "reportagem registra o número subindo para cerca de 2.000 à tarde — é recorte de "
        "operação em curso, não contagem fechada. Fica registrada como documentação da "
        "logística do transporte, não como medida da repressão. O número de veículos varia "
        "entre 40 e 50 conforme a reportagem.",

    "fonte_local": "{}; {}; {}".format(CPMI, CAPP, BAL),
    "fonte_pagina": "CPMI: 576, 687, 688, 76 | Cappelli: 53 | Balanço 2026: 4, 5, 6",

    "status_verificacao":
        "Confirmado em fonte primária — CPMI, p. 576 (fato, data e desnecessidade da ordem "
        "judicial), p. 687 (operação) e p. 76 (2.151 prisões em flagrante); Relatório do "
        "Interventor Federal, conclusão A, p. 53. RESOLVIDO EM 16/08/2026: adotado o número "
        "2.151 como principal, com o escopo corrigido para 8 e 9 de janeiro conforme a p. 76 — "
        "a p. 688 atribui a mesma cifra apenas à desocupação, e essa formulação foi descartada "
        "por superestimar o dia 9. A cifra jornalística de ~1.200 saiu da posição principal. "
        "RESSALVA DECLARADA: a correspondência entre as 1.397 audiências de custódia de 2023 e "
        "os flagrantes de 8-9/1 é INFERÊNCIA — forte, porque a audiência de custódia segue o "
        "flagrante em 24h e as prisões de 2023 foram esmagadoramente de janeiro, mas o balanço "
        "não faz a atribuição explicitamente.",

    "status_classe": "Confirmado em fonte primária",

    "nota_auditoria":
        "PT-52 RESOLVIDO em 16/08/2026, encerrando a última pendência de proveniência. Adotado "
        "2.151 (CPMI, primária) como número principal, em lugar de '~1.200 em 40 ônibus' "
        "(imprensa, contagem parcial de meio de manhã). ACHADO NO PROCESSO: a CPMI se "
        "contradiz sobre o escopo — p. 76 diz 'no próprio domingo ou no dia seguinte' e p. 688 "
        "diz 'no ato de desocupação'. Adotada a p. 76, e o texto do registro passou a dizer '8 "
        "e 9 de janeiro', porque citar 2.151 como prisões da desocupação superestima o dia 9. "
        "Acrescentado o funil da responsabilização (2.151 flagrantes → ~1.400 no processo), "
        "cruzando CPMI e balanço de 2026.",
}


def main():
    dry = "--dry-run" in sys.argv
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))

    for ev in dados["eventos"]:
        if ev["id"] == "PT-52":
            print("=== PT-52 — antes ===")
            print("  repert:", (ev.get("repertorio_acao") or "")[:100])
            print("  pagina:", ev.get("fonte_pagina"))
            ev.update(PT52)
            print("\n=== PT-52 — depois ===")
            print("  repert:", ev["repertorio_acao"][:100])
            print("  pagina:", ev["fonte_pagina"])

    dados["metadados"]["revisoes"] = [
        r for r in dados["metadados"]["revisoes"] if not r.startswith("2026-08-16 (PT-52)")
    ]
    dados["metadados"]["revisoes"].append(
        "2026-08-16 (PT-52) — encerrada a última ressalva de proveniência do projeto. Adotado o "
        "número 2.151 (prisões em flagrante, CPMI p. 76 e 688) como principal, no lugar de "
        "'~1.200 em 40 ônibus', que vinha da imprensa e media pessoas levadas à triagem nas "
        "primeiras levas da manhã — recorte de operação em curso, que a própria reportagem "
        "registra subindo para ~2.000 à tarde. ACHADO: a CPMI se contradiz sobre o escopo dos "
        "2.151 — a p. 76 os distribui entre 'o próprio domingo ou o dia seguinte' e a p. 688 os "
        "atribui só ao 'ato de desocupação'. Adotada a p. 76, com o registro passando a falar "
        "em '8 e 9 de janeiro'. Acrescentado o funil da responsabilização: das 2.151 prisões em "
        "flagrante saíram 1.397 audiências de custódia, 1.390 denúncias do MPF em 2023 e 1.402 "
        "réus responsabilizados em 2026 — cerca de 35% dos flagrantes não converteram em "
        "processo. A convergência das três medições independentes na casa de 1.400 é o que "
        "sustenta a leitura."
    )

    if dry:
        print("\nDRY RUN — nada gravado")
    else:
        JSON_P.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("\nJSON reescrito.")


if __name__ == "__main__":
    main()
