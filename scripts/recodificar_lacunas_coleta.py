#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Busca de melhor esforço nas cinco lacunas de coleta (Tier 2), 16/08/2026.

Nenhum arquivo foi baixado para Fontes/ nesta rodada — as duas peças
potencialmente relevantes que a busca encontrou (voto do min. Barroso no HC
126.292; comentário de 6 p. sobre a sentença de Moro) foram lidas em memória
para verificação e NÃO gravadas em disco, por não resolverem integralmente a
lacuna e por a política do projeto exigir confirmação antes de qualquer
download. Ver a lista de pendências ao final da rodada.

Resultado, por registro:
  PT-58        ACHADO — Agência Brasil, duas matérias independentes e datadas,
               confirmam a prisão preventiva (22/11) e a transferência para
               cumprimento de pena (25/11). Reclassificado para 'Confirmado'
               (jornalístico, não fonte primária — mesmo padrão de PT-59/60).
  PT-61        ACHADO — ohoje.com (30/04/2026) nomeia o relatório 'Democracia
               Inabalada' (divulgado 29/04) com detalhamento que soma
               exatamente 1.402 (431+419+552). Reclassificado para 'Confirmado'.
  PT-53        NÃO RESOLVIDO. Achado tangencial (~1.628 ações penais, contexto
               de decisão diversa) não verificado contra documento primário;
               além disso a fonte_url atual aponta para um balanço DIFERENTE
               (898 pessoas, "em dois anos") do que o texto do registro
               descreve. Mantido 'A verificar'; a inconsistência de URL some
               fica registrada para decisão do pesquisador.
  PT-38        SEM MUDANÇA DE STATUS. Busca confirma que a perícia segue em
               andamento sem prazo definido (Agência Brasil, 2023) — a
               restrição de acesso descrita já era a hipótese correta.
  PT-03A       SEM MUDANÇA DE STATUS. Busca exaustiva não localizou o inteiro
               teor; achou apenas um comentário de 6 p. sobre a sentença, não
               a peça. Permanece baixa prioridade, já suprida pela transcrição
               no TRF-4.
  PT-02A       SEM MUDANÇA DE STATUS. Busca localizou um mirror parcial — só o
               voto do min. Barroso (28 p.), não o acórdão completo com todos
               os votos. Não resolve a lacuna; fica como pendência de decisão.

Uso:  python scripts/recodificar_lacunas_coleta.py [--dry-run]
"""

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

PT58 = {
    "fonte_trecho":
        "Cobertura jornalística (nov/2025). ACHADO DE 16/08/2026 — duas matérias da Agência "
        "Brasil, independentes e datadas, confirmam a sequência: 'Bolsonaro é preso "
        "preventivamente em Brasília' (22/11/2025, 07h52): 'a reunião poderia causar tumulto e "
        "até mesmo facilitar \"eventual tentativa de fuga do réu\"'; 'foi ainda verificada "
        "tentativa de violar a tornozeleira eletrônica'. A prisão preventiva, decretada pelo "
        "min. Alexandre de Moraes, substituiu a prisão domiciliar em vigor desde 04/08/2025. "
        "'Moraes decide que Bolsonaro continuará preso na Superintendência da PF' "
        "(25/11/2025, 15h33) confirma o início do cumprimento da pena de 27 anos e 3 meses na "
        "mesma data. Busca por espelho do inteiro teor da decisão (noticias.stf.jus.br, "
        "conjur.com.br) retornou bloqueio de acesso (403) — permanece atrás do WAF do STF, "
        "coleta possível apenas pela via de cookie descrita em scripts/baixar_fontes.sh "
        "stf-busca/stf-doc.",

    "fonte_url":
        "https://agenciabrasil.ebc.com.br/justica/noticia/2025-11/bolsonaro-e-preso-preventivamente-em-brasilia",

    "status_verificacao":
        "Confirmado — duas matérias independentes e datadas da Agência Brasil (22 e "
        "25/11/2025), com citação literal da motivação (risco de fuga; tentativa de violar a "
        "tornozeleira). Não é fonte primária: o inteiro teor da decisão segue atrás do WAF do "
        "STF, não obtido nesta rodada.",

    "status_classe": "Confirmado",

    "nota_auditoria":
        "PT-58 — busca de melhor esforço em 16/08/2026 (Tier 2). Duas matérias da Agência "
        "Brasil confirmam data, motivação e desfecho. Reclassificado de 'A verificar' para "
        "'Confirmado' — mesmo padrão de PT-59/PT-60, que também se apoiam em cobertura do "
        "portal do STF replicada pela imprensa, não no documento judicial em si.",
}

PT61 = {
    "fonte_trecho":
        "Correio Braziliense / STF: 'STF conclui julgamentos do 8 de janeiro com 1.402 "
        "condenações'. ACHADO DE 16/08/2026 — ohoje.com (30/04/2026) nomeia e data o "
        "documento: 'relatório \"Democracia Inabalada\", divulgado nesta quarta-feira (29)' "
        "[29/04/2026], com detalhamento que soma exatamente 1.402: 431 condenados a penas "
        "privativas de liberdade (indenizações e multas de R$ 30 milhões), 419 com penas "
        "convertidas em restrição de direitos (R$ 5 milhões) e 552 acordos de não persecução "
        "penal (39,4% dos casos). Busca por PDF do relatório em portal.stf.jus.br/"
        "democraciainabalada e em noticias.stf.jus.br retornou bloqueio de acesso (403) — "
        "atrás do WAF do STF, não indexado por mecanismo de busca comum.",

    "fonte_url":
        "https://www.correiobraziliense.com.br/politica/2026/04/7409048-stf-conclui-julgamentos-do-8-de-janeiro-com-1-402-condenacoes.html",

    "status_verificacao":
        "Confirmado — duas fontes jornalísticas independentes e datadas (Correio Braziliense; "
        "ohoje.com, 30/04/2026) nomeiam o relatório 'Democracia Inabalada' (STF, 29/04/2026) "
        "com detalhamento internamente consistente (431+419+552=1.402). Não é fonte primária: "
        "o documento do STF em si segue atrás do WAF, não obtido nesta rodada.",

    "status_classe": "Confirmado",

    "nota_auditoria":
        "PT-61 — busca de melhor esforço em 16/08/2026 (Tier 2). ohoje.com nomeia e data o "
        "relatório com detalhamento que soma exatamente 1.402, elevando a confiança de "
        "'fonte jornalística única' para 'duas fontes jornalísticas independentes e "
        "consistentes'. Reclassificado de 'A verificar' para 'Confirmado'. O PDF do STF "
        "permanece não obtido — ver PT-53 para a inconsistência de URL correlata.",
}

PT38_NOTA = (
    "PT-38 — busca de melhor esforço em 16/08/2026 (Tier 2), sem mudança de status. Agência "
    "Brasil (setembro/2023) confirma que a perícia do Instituto Nacional de Criminalística "
    "segue sem prazo definido ('o diretor do INC (…) afirma não haver prazo, pois seguem "
    "chegando materiais'). A hipótese de acesso restrito era a correta; nenhum laudo público "
    "foi localizado."
)

PT03A_NOTA = (
    "PT-03A — busca de melhor esforço em 16/08/2026 (Tier 2), sem mudança de status. "
    "Localizados apenas comentários sobre a sentença (ex.: artigo de 6 p. de Mário Montanha "
    "Teixeira Filho), não o inteiro teor. O e-proc da JFPR não foi consultado diretamente — "
    "provavelmente exige login. Permanece baixa prioridade: o dispositivo já está transcrito "
    "no acórdão do TRF-4, p. 395."
)

PT02A_NOTA = (
    "PT-02A — busca de melhor esforço em 16/08/2026 (Tier 2), sem mudança de status. "
    "Localizado um mirror em luisrobertobarroso.com.br — mas é APENAS o voto do min. Barroso "
    "(28 p.), não o acórdão completo do HC 126.292 com todos os votos. Não resolve a lacuna "
    "declarada ('o acórdão do próprio HC 126.292 não foi baixado'). Arquivo NÃO baixado para "
    "Fontes/ — decisão sobre incorporá-lo como material suplementar fica pendente para o "
    "pesquisador (ver lista de pendências)."
)


def main():
    dry = "--dry-run" in sys.argv
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))

    for ev in dados["eventos"]:
        if ev["id"] == "PT-58":
            print("=== PT-58 — antes ===")
            print("  classe :", ev["status_classe"])
            ev.update(PT58)
            print("=== PT-58 — depois ===")
            print("  classe :", ev["status_classe"])
        elif ev["id"] == "PT-61":
            print("\n=== PT-61 — antes ===")
            print("  classe :", ev["status_classe"])
            ev.update(PT61)
            print("=== PT-61 — depois ===")
            print("  classe :", ev["status_classe"])
        elif ev["id"] == "PT-38":
            ev["nota_auditoria"] = PT38_NOTA
            print("\n=== PT-38 — nota de busca registrada, status mantido ===")
        elif ev["id"] == "PT-03A":
            ev["nota_auditoria"] = PT03A_NOTA
            print("=== PT-03A — nota de busca registrada, status mantido ===")
        elif ev["id"] == "PT-02A":
            ev["nota_auditoria"] = PT02A_NOTA
            print("=== PT-02A — nota de busca registrada, status mantido ===")

    dados["metadados"]["revisoes"] = [
        r for r in dados["metadados"]["revisoes"] if not r.startswith("2026-08-16 (lacunas coleta)")
    ]
    dados["metadados"]["revisoes"].append(
        "2026-08-16 (lacunas coleta) — busca de melhor esforço (Tier 2) nas cinco lacunas de "
        "coleta. PT-58 e PT-61 RECLASSIFICADOS de 'A verificar' para 'Confirmado', com fontes "
        "jornalísticas datadas e independentes (Agência Brasil para PT-58; Correio Braziliense "
        "+ ohoje.com para PT-61) — em nenhum dos dois casos o documento primário do STF foi "
        "obtido, porque portal.stf.jus.br e noticias.stf.jus.br bloqueiam requisição "
        "automatizada (403), atrás do mesmo WAF já documentado em Fontes/LEIA-ME_fontes.md. "
        "PT-53 permanece 'A verificar' — achado tangencial não verificado, mais uma "
        "inconsistência encontrada entre a fonte_url do registro e o balanço que ele descreve, "
        "ambas deixadas como pendência explícita. PT-38, PT-03A e PT-02A sem mudança de "
        "status: buscas documentadas em nota_auditoria, nenhum documento primário novo "
        "localizado — no caso de PT-02A, um mirror PARCIAL (voto de um só ministro) foi achado "
        "mas não baixado, por não resolver a lacuna e por exigir confirmação antes de gravar "
        "em Fontes/."
    )

    if dry:
        print("\nDRY RUN — nada gravado")
    else:
        JSON_P.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("\nJSON reescrito.")


if __name__ == "__main__":
    main()
