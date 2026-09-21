#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Resolução de PT-12 e PT-17; esclarecimento (não substituição) de PT-52.

Rodada única, 16/08/2026, seguindo o mesmo método de recodificar_pt34.py: busca
exaustiva no corpus inteiro (não só a seção já checada) + imprensa; recodifica
quando há lastro, retira/qualifica quando não há.

PT-12 — "mais de 100 acampamentos": MESMO PADRÃO DO PT-34. Busca em todo o PDF
da CPMI (não só p. 524-540) e no Cappelli não encontrou a cifra. Ela provém da
retrospectiva da Agência Brasil (jan/2026), sem órgão nomeado — igual ao "4 mil"
de PT-34. RETIRADA e substituída pela caracterização geográfica que a CPMI
sustenta com página: "em todos os Estados" (p. 510).

PT-17 — saída de Bolsonaro para os EUA em 30/12/2022: ACHADO. A busca exaustiva
no corpus encontrou o que a rodada anterior não viu: CPMI p. 612, no corpo
analítico do próprio relatório ("principalmente após a partida de Bolsonaro para
os EUA no dia 30 de dezembro"). CONFIRMADO EM FONTE PRIMÁRIA.

PT-52 — números de detidos na desocupação: NÃO É O MESMO PADRÃO DO PT-34. Busca
na imprensa (Poder360, Terra, Exame, jan/2023, com atribuição ao então ministro
Flávio Dino) mostra que "~1.200 em 40 ônibus" é uma contagem PARCIAL e PROGRESSIVA
— pessoas levadas para triagem na Academia Nacional de Polícia ao longo da manhã,
que a própria imprensa da época registra subindo para ~2.000 à tarde. Já os 2.151
presos de CPMI p. 688 são o total de PRISÕES no fim da operação — universo
diferente (verificação/triagem vs. prisão efetiva), não a mesma medição em
unidades diferentes. NÃO SUBSTITUÍDO — as duas cifras entram lado a lado, com
os referentes explícitos, e a escolha de qual liderar no texto fica para o
pesquisador (ver PENDENCIAS-ANALITICAS.md).

Uso:  python scripts/recodificar_ressalvas_dado.py [--dry-run]
"""

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

PT12 = {
    "repertorio_acao":
        "Acampamentos permanentes em frente a quartéis, instalados em todos os Estados "
        "(CPMI, p. 510)",

    "fonte_trecho":
        "Relatório Final da CPMI, seção 5.5 'Acampamentos golpistas', p. 524 e seguintes. A "
        "seção abre com falas de lideranças que sustentavam a permanência: 'Vocês não percam "
        "a fé, é só o que eu posso falar para vocês agora' (gen. Walter Braga Netto, "
        "19/11/2022); 'Continuem na luta, o Bolsonaro não vai decepcionar ninguém' (Valdemar "
        "Costa Neto, 16/12/2022). Subseções: 'As primeiras mobilizações' (p. 524), 'Comboios' "
        "(p. 529), '15 de novembro' (p. 531). A p. 532 registra 95 ônibus na área do QG do "
        "Exército em 15/11 e pico de 4 mil pessoas acampadas (evento distinto de PT-34, mesma "
        "ressalva de proveniência já resolvida lá). ESCOPO GEOGRÁFICO, com página: CPMI, p. "
        "510, ao listar as quatro linhas de ação golpista: '(3) instalação de acampamentos em "
        "frente a organizações militares em todos os Estados'. "
        "LASTRO MATERIAL — Relatório Final da CPMI, p. 577, subseção 'Financiamento': 'O "
        "acampamento golpista em Brasília teve um custo de R$ 376.043,64 para a União. O "
        "total corresponde a quase R$ 5 mil por dia. O Comando Militar do Planalto precisou "
        "colocar 200 homens a mais em prontidão e realizar patrulhamentos na área durante os "
        "70 dias de ocupação ilegal.' "
        "RETIRADO EM 16/08/2026 — a cifra de 'mais de 100 acampamentos' provinha da "
        "cronologia da Agência Brasil (jan/2026), sem órgão nomeado, mesmo padrão do '4 mil' "
        "de PT-34. Busca exaustiva em todo o PDF da CPMI (não só p. 524-540) e no relatório "
        "Cappelli não localizou a cifra; a CPMI só sustenta, com página, o escopo geográfico "
        "'em todos os Estados' (p. 510), sem quantificar.",

    "fonte_pagina": "CPMI: 524, 529, 531, 532, 510, 577",

    "status_verificacao":
        "Confirmado em fonte primária quanto à existência, à escala nacional (em todos os "
        "Estados, CPMI p. 510) e ao incentivo por lideranças — CPMI, seção 5.5. RESOLVIDO EM "
        "16/08/2026: a cifra de 'mais de 100 acampamentos' foi retirada — sem lastro na CPMI "
        "nem no Cappelli, mesma proveniência frágil do '4 mil' de PT-34 (Agência Brasil, sem "
        "órgão nomeado). Lastro material do mecanismo confirmado em fonte primária — CPMI, p. "
        "577.",

    "nota_auditoria":
        "PT-12 RESOLVIDO em 16/08/2026, mesmo padrão do PT-34. Cifra de 'mais de 100 "
        "acampamentos' retirada — busca exaustiva em todo o PDF da CPMI e no Cappelli não a "
        "localizou; provinha de retrospectiva da Agência Brasil sem órgão nomeado. Substituída "
        "pela caracterização geográfica que a CPMI sustenta com página: 'em todos os Estados' "
        "(p. 510).",
}

PT17 = {
    "repertorio_acao":
        "Última live como presidente, em que admite ter passado dois meses buscando "
        "alternativas ao resultado eleitoral; partida para os EUA em 30 de dezembro de 2022, "
        "antes da posse (CPMI, p. 612)",

    "fonte_trecho":
        "Relatório Final da CPMI, p. 507. Em sua última live como presidente, em 30 de "
        "dezembro, Bolsonaro admitiu ter buscado alternativas ao resultado: 'São 30 de "
        "dezembro, está prevista a posse em 1º de janeiro. Eu busquei dentro das quatro "
        "linhas, dentro das leis, respeitando a Constituição, uma saída para isso aí, se tinha "
        "uma alternativa para isso.' E acrescentou: 'Como foi difícil ficar dois meses calado, "
        "trabalhando para buscar alternativas.' Informou não ter tido sucesso por falta de "
        "apoio. "
        "SAÍDA DO PAÍS, ACHADO DE 16/08/2026 — CPMI, p. 612, na análise da comissão sobre a "
        "'estratégia do caos': 'os atos de vandalismo do dia 12 de dezembro e o atentado a "
        "bomba do dia 24 de dezembro pareciam indicar a única via disponível de ação, "
        "principalmente após a partida de Bolsonaro para os EUA no dia 30 de dezembro'. Busca "
        "exaustiva no restante do corpus (CPMI inteira, PGR, Cappelli) não localizou órgão "
        "oficial (PF, Receita Federal) que registre horário de voo ou aeroporto — a CPMI "
        "confirma a data, não o detalhe logístico da viagem.",

    "fonte_pagina": "CPMI: 507, 612",

    "status_verificacao":
        "Confirmado em fonte primária — CPMI, p. 507 (live e admissão de busca de "
        "alternativas) e p. 612 (partida para os EUA em 30 de dezembro, no corpo analítico da "
        "própria comissão). RESOLVIDO EM 16/08/2026: busca exaustiva em todo o corpus "
        "encontrou a confirmação da data de saída, que a rodada anterior não havia localizado. "
        "Não há, no corpus, fonte primária para o detalhe logístico (voo, aeroporto) — apenas "
        "para a data.",

    "status_classe": "Confirmado em fonte primária",

    "nota_auditoria":
        "PT-17 RESOLVIDO em 16/08/2026. Busca exaustiva em todo o PDF da CPMI (985 páginas "
        "além da seção já checada) localizou a confirmação da data de saída de Bolsonaro para "
        "os EUA em p. 612, no texto analítico da comissão sobre a 'estratégia do caos'. "
        "Reclassificado de 'A verificar' para 'Confirmado em fonte primária'.",
}

PT52 = {
    "repertorio_acao":
        "Desmonte do acampamento do SMU; dois universos de contagem distintos e não "
        "somáveis — ~1.200 a 2.000 pessoas levadas para triagem na Academia Nacional de "
        "Polícia ao longo da manhã (contagem progressiva, imprensa) e 2.151 pessoas "
        "efetivamente presas ao fim da operação (CPMI, p. 688)",

    "fonte_trecho":
        "Relatório Final da CPMI, p. 576. E, em fonte primária direta, Relatório do "
        "Interventor Federal, conclusão A, p. 53: 'A permanência do acampamento na Praça dos "
        "Cristais no Setor Militar Urbano permitiu apoio logístico e local de concentração aos "
        "manifestantes que se deslocaram a Brasília para que as ações do dia 08 fossem "
        "desencadeadas, sendo verificada, desde o dia 07 de janeiro de 2023, a chegada de "
        "vários ônibus vindo de fora de Brasília.' "
        "TRIAGEM/TRANSPORTE (imprensa, atribuído) — CPMI, p. 687: 'Das cerca de 3.000 pessoas "
        "que estavam no local, 1.500 deixaram o espaço por conta própria; as restantes foram "
        "levadas para a triagem na Academia Nacional de Polícia.' Poder360 (09/01/2023), "
        "citando o então ministro da Justiça Flávio Dino: cerca de 1.200 pessoas levadas ao "
        "ginásio da ANP nas primeiras levas de ônibus da manhã, número que a própria "
        "reportagem registra subindo para ~2.000 à tarde, conforme mais ônibus deixavam o QG. "
        "O número de veículos varia entre 40 e 50 conforme a reportagem consultada. "
        "PRISÃO EFETIVA (fonte primária, achado distinto) — CPMI, p. 688: 'No ato de "
        "desocupação, foram presas 2.151 pessoas.' "
        "ESCLARECIDO EM 16/08/2026, SEM SUBSTITUIÇÃO — os dois números não medem a mesma "
        "coisa: um é contagem progressiva de pessoas levadas para verificação/triagem ao "
        "longo da manhã (jornalística, mas com atribuição ministerial); o outro é o total de "
        "prisões efetivadas ao fim da operação (primária, CPMI p. 688). Não há, no corpus, "
        "elemento que permita afirmar que 2.151 é a atualização de 1.200/40 ônibus, nem o "
        "contrário — podem ser o mesmo universo em momentos diferentes, ou universos "
        "parcialmente distintos (a própria CPMI, ao somar 1.500 que saíram por conta própria "
        "com o total de 3.000 no local, não fecha a conta com 2.151 presos, o que sugere que "
        "as prisões não se restringiram a quem ficou no acampamento).",

    "fonte_pagina": "CPMI: 576, 687, 688 | Cappelli: 53",

    "status_verificacao":
        "Confirmado em fonte primária direta quanto ao mecanismo — Relatório do Interventor "
        "Federal, conclusão A (p. 53), e CPMI, p. 576. ESCLARECIDO, NÃO RESOLVIDO, EM "
        "16/08/2026: os números de detidos não foram unificados porque medem coisas "
        "diferentes. '~1.200 em 40 ônibus' é contagem progressiva de pessoas levadas para "
        "triagem (imprensa, atribuída ao então ministro Flávio Dino); '2.151 presas' é o "
        "total de prisões ao fim da operação (CPMI, p. 688, primária). PENDÊNCIA PARA O "
        "PESQUISADOR: qual cifra liderar no texto, e como tratar a diferença — ver "
        "PENDENCIAS-ANALITICAS.md.",

    "nota_auditoria":
        "PT-52 — busca de 16/08/2026 não permitiu unificar as duas cifras de detidos: são "
        "medições de universos distintos (triagem progressiva x prisão final), não a mesma "
        "contagem em fontes diferentes. Mantidas as duas, lado a lado, com atribuição "
        "explícita. Decisão de qual liderar no texto NÃO foi tomada — fica como pendência "
        "explícita para o pesquisador, por exigir julgamento editorial além da verificação "
        "factual.",
}


def main():
    dry = "--dry-run" in sys.argv
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))

    for ev in dados["eventos"]:
        if ev["id"] == "PT-12":
            print("=== PT-12 — antes ===")
            print("  repert :", ev["repertorio_acao"])
            print("  pagina :", ev["fonte_pagina"])
            ev.update(PT12)
            print("=== PT-12 — depois ===")
            print("  repert :", ev["repertorio_acao"])
            print("  pagina :", ev["fonte_pagina"])
        elif ev["id"] == "PT-17":
            print("\n=== PT-17 — antes ===")
            print("  classe :", ev["status_classe"], "| pagina:", ev["fonte_pagina"])
            ev.update(PT17)
            print("=== PT-17 — depois ===")
            print("  classe :", ev["status_classe"], "| pagina:", ev["fonte_pagina"])
        elif ev["id"] == "PT-52":
            print("\n=== PT-52 — antes ===")
            print("  repert :", ev["repertorio_acao"][:90])
            ev.update(PT52)
            print("=== PT-52 — depois (esclarecido, não substituído) ===")
            print("  repert :", ev["repertorio_acao"][:90])

    dados["metadados"]["revisoes"] = [
        r for r in dados["metadados"]["revisoes"] if not r.startswith("2026-08-16 (ressalvas dado)")
    ]
    dados["metadados"]["revisoes"].append(
        "2026-08-16 (ressalvas dado) — três ressalvas de proveniência de dado tratadas por busca "
        "exaustiva no corpus (todo o PDF da CPMI, não só as seções já checadas) e na imprensa. "
        "PT-12: retirada a cifra de 'mais de 100 acampamentos' (mesmo padrão do PT-34 — sem "
        "lastro na CPMI nem no Cappelli, provinha da Agência Brasil sem órgão nomeado); "
        "substituída pela caracterização geográfica ancorada 'em todos os Estados' (CPMI, p. "
        "510). PT-17: RESOLVIDO — a busca exaustiva localizou a confirmação da partida de "
        "Bolsonaro para os EUA em 30/12/2022 na p. 612 da CPMI, texto analítico da própria "
        "comissão; reclassificado para 'Confirmado em fonte primária'. PT-52: ESCLARECIDO SEM "
        "SUBSTITUIÇÃO — as duas cifras de detidos ('~1.200 em 40 ônibus' e '2.151 presas') "
        "medem universos diferentes (triagem progressiva x prisão final ao fim da operação, "
        "CPMI p. 687-688) e foram mantidas lado a lado, com a escolha de qual liderar no texto "
        "explicitamente reservada ao pesquisador. Nenhum dado analítico alheio a estes três "
        "registros foi alterado."
    )

    if dry:
        print("\nDRY RUN — nada gravado")
    else:
        JSON_P.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("\nJSON reescrito.")


if __name__ == "__main__":
    main()
