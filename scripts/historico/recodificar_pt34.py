#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Resolução de PT-34 — a estimativa de multidão do 8 de Janeiro.

Rodada única, 16/08/2026. Substitui a cifra pontual de "cerca de 4 mil pessoas
na Praça dos Três Poderes às 15h26" por uma FAIXA construída sobre contagens
oficiais convergentes, cada uma com órgão emissor, momento e página.

Motivo da mudança, em uma frase: o número pontual não tem lastro em fonte
primária nem corroboração jornalística independente; a faixa tem as duas coisas.

Acrescenta também a PT-21 a contagem de transporte da ANTT difundida pela Abin
(105 ônibus, ~3.900 passageiros), que estava ausente do codebook e é uma das
duas medições independentes que sustentam a faixa.

Uso:  python scripts/recodificar_pt34.py [--dry-run]
"""

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

# ---------------------------------------------------------------------------
# PT-34 — ocupação da Praça dos Três Poderes, 15h26
# ---------------------------------------------------------------------------
PT34 = {
    "ator_grupo":
        "Multidão de manifestantes — ordem de grandeza de poucos milhares; sem "
        "estimativa oficial para este horário e local específicos",

    "mecanismo_causal":
        "Massa crítica atingida no ponto de máxima densidade simbólica. A magnitude não "
        "repousa em estimativa pontual para as 15h26 — que não existe em fonte primária —, "
        "e sim na convergência de duas medições oficiais independentes na manhã do mesmo dia "
        "(contagem de transporte e contagem policial de público) e na caracterização que a "
        "própria CPMI faz dos invasores. ACHADO ANALÍTICO: a SSP/DF dispunha de estimativa "
        "própria de público às 9h e ainda assim o Congresso estava guarnecido por 20 policiais "
        "às 14h45 (PT-28) — o número deixa de ser dado descritivo e passa a ser evidência "
        "sobre o conhecimento do Estado, reforçando o hoop test.",

    "fonte_trecho":
        "Relatório Final da CPMI, p. 674: 'Os insurgentes avançaram pela via S1, ultrapassaram "
        "as tropas sem serem importunados e, por volta das 15h26, chegaram à Praça dos Três "
        "Poderes em altura muito próxima ao prédio do STF.' O relatório NÃO atribui número de "
        "manifestantes a esta passagem. "
        "MAGNITUDE, por convergência de fontes oficiais: (a) contagem de transporte — 'Conforme "
        "a ANTT (...) há um total de 105 ônibus, com cerca de 3900 passageiros', alerta da Abin "
        "de 07/01 às 12h (p. 374 e 637); (b) contagem policial de público — 'Público estimado "
        "pela SSP/DF de 3.000 pessoas na área próxima do SMU', mensagem ao CIISP-DF de 08/01 às "
        "9h (p. 643); (c) caracterização da própria CPMI — 'um grupo de poucos milhares de "
        "manifestantes invadissem, depredassem e saqueassem prédios públicos' (p. 695). "
        "Pool mobilizado a montante: 300 acampados em 05/01 e 5.500 em 07/01 (p. 576). Piso a "
        "jusante: 2.151 presos na desocupação de 09/01 (p. 688). "
        "RETIRADA EM 16/08/2026 — a cifra de 'cerca de 4 mil pessoas na Praça às 15h26' provinha "
        "da cronologia retrospectiva da Agência Brasil (jan/2024), atribuída apenas a 'policiais', "
        "sem órgão nomeado. Não foi localizada em fonte primária; não aparece nas cronologias "
        "contemporâneas (Poder360, 15/01/2023) nem na própria cronologia posterior da Agência "
        "Brasil (jan/2026); e a Wikipédia lusófona aplica o mesmo número a referente DIVERSO — os "
        "que deixaram o QG. Na CPMI, '4 mil' aparece em p. 532 (pico do acampamento em 15/11/2022) "
        "e em p. 1324 (depoimento do gen. Augusto Heleno, que se recusou a dizer se houve golpe).",

    "fonte_pagina": "CPMI: 674, 695, 643, 637, 374, 576, 688",

    "status_verificacao":
        "Confirmado em fonte primária quanto ao horário, ao local e à ordem de grandeza — CPMI, "
        "p. 674 (chegada à Praça às 15h26) e p. 695 ('poucos milhares'). A MAGNITUDE é faixa "
        "construída, não medição: 3.000 a 5.500 no conjunto mobilizado, com duas contagens "
        "oficiais independentes convergindo em ~3.000-3.900 na manhã de 08/01. NÃO existe "
        "estimativa oficial para a Praça às 15h26, e nenhuma deve ser apresentada como tal. "
        "A cifra de 4 mil foi retirada em 16/08/2026.",

    "status_classe": "Confirmado em fonte primária",

    "nota_auditoria":
        "PT-34 RESOLVIDO em 16/08/2026, após busca em veículos de escala nacional. Retirada a "
        "cifra pontual de 'cerca de 4 mil pessoas na Praça às 15h26': sem lastro primário e sem "
        "corroboração independente — fonte única (Agência Brasil, jan/2024, 'policiais' sem órgão "
        "nomeado), ausente das cronologias contemporâneas, e aplicada a referente diverso pela "
        "Wikipédia. Substituída por faixa de 3.000 a 5.500 no conjunto mobilizado, ancorada em "
        "duas medições oficiais independentes (ANTT/Abin: 105 ônibus e ~3.900 passageiros; "
        "SSP/DF: 3.000 de público às 9h) mais a caracterização da CPMI ('poucos milhares'). "
        "Ver o dossiê em ESTIMATIVA-MULTIDAO-8JAN.md.",
}

# ---------------------------------------------------------------------------
# PT-21 — caravanas e fretamento, 06-07/01
# A contagem da ANTT difundida pela Abin não estava no codebook e é uma das duas
# medições que sustentam a faixa de PT-34.
# ---------------------------------------------------------------------------
PT21_ACRESCIMO = (
    " ACRÉSCIMO DE 16/08/2026 — contagem de transporte, independente da contagem policial de "
    "público: alerta da Abin de 07/01 às 12h, p. 374 e 637: 'Conforme a ANTT, houve aumento do "
    "número de fretamentos de ônibus com destino a Brasília para este final de semana. Há um "
    "total de 105 ônibus, com cerca de 3900 passageiros.' Na manhã de 08/01, até as 8h20, o "
    "total era de 101 veículos (p. 643). A cifra da ANTT mede capacidade de transporte fretado, "
    "não presença na Esplanada, e é usada em PT-34 como um dos dois limites da faixa."
)


def main():
    dry = "--dry-run" in sys.argv
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))

    for ev in dados["eventos"]:
        if ev["id"] == "PT-34":
            print("=== PT-34 — antes ===")
            print("  ator   :", ev["ator_grupo"])
            print("  pagina :", ev["fonte_pagina"])
            print("  classe :", ev["status_classe"])
            ev.update(PT34)
            print("=== PT-34 — depois ===")
            print("  ator   :", ev["ator_grupo"])
            print("  pagina :", ev["fonte_pagina"])
            print("  classe :", ev["status_classe"])
        elif ev["id"] == "PT-21":
            if "ACRÉSCIMO DE 16/08/2026" not in (ev.get("fonte_trecho") or ""):
                ev["fonte_trecho"] = (ev.get("fonte_trecho") or "") + PT21_ACRESCIMO
                ev["fonte_pagina"] = "CPMI: 576, 374, 637, 643"
                ev["nota_auditoria"] = (
                    "Acrescentada em 16/08/2026 a contagem de transporte da ANTT difundida pela "
                    "Abin (105 ônibus, ~3.900 passageiros), que estava ausente do codebook e "
                    "sustenta a faixa de magnitude de PT-34."
                )
                print("\n=== PT-21 — acrescentada a contagem ANTT/Abin (p. 374, 637) ===")

    dados["metadados"]["revisoes"] = [
        r for r in dados["metadados"]["revisoes"] if not r.startswith("2026-08-16 (PT-34)")
    ]
    dados["metadados"]["revisoes"].append(
        "2026-08-16 (PT-34) — resolvida a ressalva de proveniência mais antiga do projeto. A cifra "
        "de 'cerca de 4 mil pessoas na Praça dos Três Poderes às 15h26' foi RETIRADA: busca em "
        "veículos de escala nacional mostrou fonte única (Agência Brasil, jan/2024, atribuída a "
        "'policiais' sem órgão nomeado), ausência nas cronologias contemporâneas e aplicação a "
        "referente diverso na Wikipédia lusófona. Em seu lugar entra uma FAIXA de 3.000 a 5.500 no "
        "conjunto mobilizado, sustentada por duas medições oficiais independentes — a contagem de "
        "transporte da ANTT difundida pela Abin (105 ônibus, ~3.900 passageiros, p. 374 e 637) e a "
        "contagem policial de público da SSP/DF (3.000 às 9h, p. 643) — mais a caracterização da "
        "própria CPMI ('poucos milhares', p. 695). A contagem da ANTT foi acrescentada a PT-21. "
        "Dossiê metodológico em ESTIMATIVA-MULTIDAO-8JAN.md."
    )

    if dry:
        print("\nDRY RUN — nada gravado")
    else:
        JSON_P.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n",
                          encoding="utf-8")
        print("\nJSON reescrito.")


if __name__ == "__main__":
    main()
