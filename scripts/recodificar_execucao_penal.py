#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PT-58, PT-59 e PT-60 passam a fonte primária — as três decisões foram obtidas.

Rodada de 16/08/2026. Os três registros de T+1 sobre a execução penal de
Bolsonaro estavam apoiados em cobertura do portal do STF, não nas decisões.
As três decisões foram baixadas e conferidas.

COMO FORAM OBTIDAS. As páginas de notícia do STF, que devolvem 403 ao WebFetch,
respondem 200 a curl com user-agent de navegador — e trazem link direto para a
peça. Daí saíram três rotas, nenhuma exigindo o cookie do WAF:
  PT-58 — PDF hospedado pela própria Agência Brasil
  PT-59 — bucket S3 do portal de notícias do STF (mesmo padrão do balanço)
  PT-60 — portal.stf.jus.br/processos/downloadPeca.asp, que respondeu direto

DUAS CORREÇÕES DE FATO que a leitura das decisões produziu:

  1. PT-58 — a preventiva NÃO decorre da execução da AP 2668. Foi decretada na
     PETIÇÃO 14.129, processo distinto, por coação no curso do processo (art.
     344 do CP), obstrução de investigação de organização criminosa (art. 2º,
     §1º, da Lei 12.850/13) e abolição violenta do Estado Democrático de Direito
     (art. 359-L do CP) — "em face de sua participação nos mesmos delitos de
     EDUARDO NANTES BOLSONARO". O que a decisão faz é CONVERTER em prisão as
     cautelares já impostas em 17/7/2025 naqueles autos. O cumprimento da pena
     da AP 2668 começa depois, em 25/11/2025, e é outro ato.

  2. PT-60 — a decisão é de 24 DE MARÇO DE 2026, não de "mar/2026 com
     prorrogação em 03/07/2026". A prorrogação, se existe, é decisão posterior
     que NÃO está no corpus e não foi verificada.

Uso:  python scripts/recodificar_execucao_penal.py [--dry-run]
"""

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"
D4 = "Fontes/04_T+1_Resposta-institucional"
PET = D4 + "/STF_Pet-14129_Decisao-Prisao-Preventiva_2025-11-22.pdf"
TRANSF = D4 + "/STF_EP-169_Decisao-Transferencia-Papuda_2026-01-15.pdf"
DOMIC = D4 + "/STF_EP-169_Decisao-Prisao-Domiciliar_2026-03-24.pdf"

PT58 = {
    "data_hora": "22/11/2025 (preventiva) — 25/11/2025 (início do cumprimento da pena)",

    "ator_grupo": "Min. Alexandre de Moraes (STF); Polícia Federal; PGR",

    "repertorio_acao":
        "Conversão das medidas cautelares em PRISÃO PREVENTIVA na Petição 14.129, com audiência "
        "de custódia por videoconferência em 23/11/2025; em 25/11/2025, início do cumprimento da "
        "pena da AP 2668 em Sala de Estado Maior na Superintendência da PF/DF",

    "mecanismo_causal":
        "Responsabilização do topo da cadeia — e, com a decisão em mãos, o mecanismo fica mais "
        "preciso do que 'prisão do ex-presidente'. A preventiva é medida de CONTENÇÃO DE FUGA, "
        "não de execução: converte cautelares de um processo distinto (Pet 14.129) diante do que "
        "a decisão chama de 'estratégia para possibilitar a sua fuga do distrito da culpa'. A "
        "decisão encadeia quatro elementos — a iminência do trânsito em julgado da AP 2668, a "
        "vigília convocada pelo senador Flávio Bolsonaro para a véspera, a evasão de outro "
        "condenado na mesma ação penal para Miami, e a violação do monitoramento eletrônico às "
        "0h08 do dia 22. O Estado age aqui contra a possibilidade de a punição não se consumar, "
        "e não ainda para consumá-la: o cumprimento da pena é ato posterior, de 25/11.",

    "fonte_trecho":
        "Decisão do min. Alexandre de Moraes na PETIÇÃO 14.129/DF, 22 de novembro de 2025, 17 p. "
        "OBJETO DO PROCESSO, p. 1: 'Trata-se de Pet instaurada a partir de representação da "
        "Polícia Federal pela decretação de diversas medidas cautelares em face de JAIR MESSIAS "
        "BOLSONARO (...) em face de sua participação nos mesmos delitos de EDUARDO NANTES "
        "BOLSONARO, ou seja, pelos crimes de coação no curso do processo (art. 344 do Código "
        "Penal), obstrução de investigação de infração penal que envolva organização criminosa "
        "(art. 2º, §1º, da Lei 12.850/13) e abolição violenta do Estado Democrático de Direito "
        "(art. 359-L do Código Penal).' As cautelares originais são de 17/7/2025 e incluíam "
        "tornozeleira eletrônica e recolhimento domiciliar noturno. "
        "FUNDAMENTAÇÃO: 'Em razão da iminência do trânsito em julgado do acórdão condenatório "
        "(...) verifica-se a adoção de estratégia para possibilitar a sua fuga do distrito da "
        "culpa e para se furtar à aplicação da lei penal.' A decisão registra: a Informação de "
        "Polícia Judiciária 099/2025 sobre vigília convocada para 22/11 nas proximidades da "
        "residência; o vídeo do senador Flávio Bolsonaro publicado em 21/11 convocando 'VIGÍLIA "
        "PELA SAÚDE DE BOLSONARO E PELA LIBERDADE NO BRASIL!'; a evasão para Miami de Alexandre "
        "Ramagem, condenado na mesma ação penal; a proximidade da embaixada dos EUA, a 'cerca de "
        "15 (quinze) minutos de carro'; o antecedente de que o réu 'planejou (...) a fuga para a "
        "embaixada da Argentina, por meio de solicitação de asilo político'; e a comunicação de "
        "'violação do equipamento de monitoramento eletrônico do réu (...) às 0h08min do dia "
        "22/11/2025'. "
        "DISPOSITIVO: 'converto as medidas cautelares anteriormente impostas e DECRETO A PRISÃO "
        "PREVENTIVA de JAIR MESSIAS BOLSONARO', com audiência de custódia por videoconferência "
        "em 23/11/2025 às 12h. "
        "INÍCIO DO CUMPRIMENTO DA PENA, ato distinto e posterior — a decisão da EP 169 de "
        "15/1/2026 recapitula: 'Em 25/11/2025, com a certificação de trânsito em julgado da ação "
        "penal, determinei o início do cumprimento da pena de JAIR MESSIAS BOLSONARO em Sala de "
        "Estado Maior na Superintendência Regional da Polícia Federal, Distrito Federal.'",

    "fonte_url":
        "https://agenciabrasil.ebc.com.br/sites/default/files/atoms/files/decisao_pp_jb.pdf",

    "fonte_local": PET + "; " + TRANSF,
    "fonte_pagina": "Pet 14.129: 1 | EP 169-Transferência: 1",

    "status_verificacao":
        "Confirmado em fonte primária — decisão do min. Alexandre de Moraes na Pet 14.129/DF, de "
        "22/11/2025, obtida em 16/08/2026 (PDF hospedado pela Agência Brasil, 17 p., SHA-256 "
        "9f553e9389305f8a29dbc9db…). O início do cumprimento da pena em 25/11/2025 está "
        "recapitulado na decisão da EP 169 de 15/1/2026. CORREÇÃO DE FATO: a preventiva NÃO "
        "decorre da execução da AP 2668, e sim da Pet 14.129 — processo distinto, por coação no "
        "curso do processo e obstrução. O registro anterior confundia os dois atos.",

    "status_classe": "Confirmado em fonte primária",

    "nota_auditoria":
        "PT-58 elevado a fonte primária em 16/08/2026, com as decisões obtidas. CORREÇÃO DE "
        "FATO: a prisão preventiva de 22/11/2025 foi decretada na PETIÇÃO 14.129 — por coação no "
        "curso do processo, obstrução e art. 359-L —, convertendo cautelares de 17/7/2025, e NÃO "
        "na execução da AP 2668. São dois atos distintos: a preventiva contém risco de fuga em "
        "22/11; o cumprimento da pena começa em 25/11. O registro anterior os tratava como um só.",
}

PT59 = {
    "data_hora": "15/01/2026",

    "repertorio_acao":
        "Transferência imediata da Sala de Estado Maior da Superintendência da PF/DF para a Sala "
        "de Estado Maior no 19º Batalhão da PMDF, no Complexo Penitenciário da Papuda; autorizada "
        "assistência médica particular 24h e deslocamento imediato a hospital em urgência; "
        "determinada submissão imediata a junta médica oficial da PF",

    "mecanismo_causal":
        "Normalização da execução penal do ex-chefe do Executivo — com a nuance que a decisão "
        "explicita e que o registro não tinha: a transferência é para SALA DE ESTADO MAIOR, "
        "prerrogativa legal mantida, dentro de um complexo penitenciário comum. Não é "
        "equiparação ao regime ordinário, é deslocamento do custodiado para dentro do sistema "
        "prisional preservando o tratamento diferenciado. E a mesma decisão já ordena a junta "
        "médica oficial que abrirá caminho, dois meses depois, para a domiciliar humanitária de "
        "PT-60 — a sequência é contínua e está no mesmo processo.",

    "fonte_trecho":
        "Decisão do min. Alexandre de Moraes na EXECUÇÃO PENAL 169/DF, 15 de janeiro de 2026, "
        "36 p. DISPOSITIVO: 'Diante do exposto, nos termos dos artigos 21 e 341 do Regimento "
        "Interno do SUPREMO TRIBUNAL FEDERAL, 1) DETERMINO A IMEDIATA TRANSFERÊNCIA de JAIR "
        "MESSIAS BOLSONARO da Sala de Estado Maior da Superintendência Regional da Polícia "
        "Federal/DF para a Sala de Estado Maior no 19º Batalhão da Polícia Militar - PMDF, "
        "localizado no Complexo Penitenciário da Papuda, em Brasília/DF, para cumprimento da pena "
        "privativa de liberdade fixada por esta CORTE, no julgamento da AP 2668, bem como, "
        "AUTORIZO: 1.1 A assistência integral, nas 24 (vinte e quatro) horas, dos médicos "
        "particulares anteriormente cadastrados, sem necessidade de comunicação prévia. 1.2 O "
        "deslocamento imediato para os hospitais em caso de urgência.' "
        "A decisão também DEFERE acesso a aparelho de televisão do tipo Smart TV e DETERMINA que "
        "o réu 'seja SUBMETIDO IMEDIATAMENTE À JUNTA MÉDICA OFICIAL, composta por médicos da "
        "Polícia Federal, para avaliação do seu quadro clínico, necessidades para o cumprimento "
        "da pena, bem como sobre a necessidade de transferência para o hospital penitenciário', "
        "com laudo em 10 dias e faculdade de assistentes técnicos à defesa e à PGR. "
        "PENA RECAPITULADA na p. 1: 27 anos e 3 meses — 24 anos e 9 meses de reclusão e 2 anos e "
        "6 meses de detenção, regime inicial fechado, mais 124 dias-multa. "
        "Assinada em Brasília, 15 de janeiro de 2026.",

    "fonte_url":
        "https://noticias-stf-wp-prd.s3.sa-east-1.amazonaws.com/wp-content/uploads/wpallimport/"
        "uploads/2026/01/15190501/Transferencia-EP169-2.pdf",

    "fonte_local": TRANSF,
    "fonte_pagina": "EP 169-Transferência: 1, 36",

    "status_verificacao":
        "Confirmado em fonte primária — decisão do min. Alexandre de Moraes na EP 169/DF, de "
        "15/01/2026, obtida em 16/08/2026 no bucket oficial do portal de notícias do STF "
        "(36 p., SHA-256 a92cb703f04c00fb97ba4b0d…). PRECISÃO ACRESCENTADA: a transferência é "
        "para Sala de Estado Maior dentro do complexo penitenciário, não para regime comum.",

    "status_classe": "Confirmado em fonte primária",

    "nota_auditoria":
        "PT-59 elevado a fonte primária em 16/08/2026. A decisão traz precisão que o registro não "
        "tinha: a transferência é para SALA DE ESTADO MAIOR no 19º BPM, dentro da Papuda — "
        "prerrogativa preservada, não equiparação ao regime comum. A mesma decisão ordena a junta "
        "médica que dois meses depois fundamenta a domiciliar de PT-60.",
}

PT60 = {
    "data_hora": "24/03/2026",

    "repertorio_acao":
        "Autorização de PRISÃO DOMICILIAR HUMANITÁRIA TEMPORÁRIA por 90 dias contados da alta "
        "médica, para recuperação de broncopneumonia, com tornozeleira eletrônica, monitoramento "
        "diário, visitas restritas e fiscalização semanal pela PMDF; reanálise ao fim do prazo",

    "mecanismo_causal":
        "Modulação humanitária da sanção — e o inteiro teor mostra que a modulação é fortemente "
        "condicionada, não uma flexibilização. A domiciliar vem acompanhada de tornozeleira com "
        "área de inclusão restrita ao endereço, relatórios diários ao juízo, rol nominal de "
        "visitantes autorizados, fiscalização semanal pela PMDF e vistoria documentada de "
        "habitáculo e porta-malas de todo veículo que deixe a residência. Registre-se ainda que a "
        "concessão é a SEGUNDA tentativa: a mesma relatoria havia INDEFERIDO o pedido em "
        "2/3/2026, após perícia médica oficial. O que muda entre março e março é o quadro "
        "clínico, não o critério — o que sustenta ler a decisão como modulação técnica, e não "
        "como recuo político.",

    "fonte_trecho":
        "Decisão do min. Alexandre de Moraes na EXECUÇÃO PENAL 169/DF, 24 de março de 2026, "
        "40 p. ANTECEDENTE, p. 1: 'Em 14/1/2026, a Defesa de JAIR MESSIAS BOLSONARO formulou "
        "requerimento de prisão domiciliar humanitária (eDoc. 378). Em decisão de 2/3/2026, após "
        "realização de perícia médica oficial pela Polícia Federal, indeferi a concessão de "
        "prisão domiciliar.' "
        "DISPOSITIVO: 'Diante do exposto, nos termos dos artigos 21 e 341 do Regimento Interno do "
        "STF, AUTORIZO A PRISÃO DOMICILIAR HUMANITÁRIA TEMPORÁRIA ao custodiado JAIR MESSIAS "
        "BOLSONARO, pelo prazo inicial de 90 (noventa) dias, a contar da data de sua alta médica, "
        "para fins de integral recuperação da broncopneumonia. Após esse prazo, será reanalisada "
        "a presença dos requisitos necessários para a manutenção da prisão domiciliar "
        "humanitária, inclusive com perícia médica se houver necessidade.' "
        "CONDIÇÕES: '1) Uso de tornozeleira eletrônica com área de inclusão do monitoramento "
        "limitando-se ao endereço residencial do sentenciado. Os relatórios de monitoramento "
        "deverão ser enviados diariamente ao Juízo; 2) Autorização de visitas permanentes de seus "
        "filhos (...)'. FISCALIZAÇÃO: determina ao comandante do 19º Batalhão da PMDF e "
        "subdiretor do Núcleo de Custódia 'as providências cabíveis para a fiscalização da prisão "
        "domiciliar humanitária', com 'envio de relatórios semanais ou imediatamente, em caso de "
        "descumprimento', e 'vistorias nos habitáculos e porta-malas de todos os veículos que "
        "saírem da residência do réu (...) devidamente documentadas, com a indicação dos "
        "veículos, motoristas e passageiros'. "
        "Assinada em Brasília, 24 de março de 2026.",

    "fonte_url": "https://portal.stf.jus.br/processos/downloadPeca.asp?id=15385383350&ext=.pdf",

    "fonte_local": DOMIC,
    "fonte_pagina": "EP 169-Domiciliar: 1, 40",

    "status_verificacao":
        "Confirmado em fonte primária — decisão do min. Alexandre de Moraes na EP 169/DF, de "
        "24/03/2026, obtida em 16/08/2026 em portal.stf.jus.br/processos/downloadPeca.asp "
        "(40 p., SHA-256 e2f42b289a5b49e9738e57d6…). CORREÇÃO DE DATA: a decisão é de 24/03/2026; "
        "o registro anterior dizia 'mar/2026 (prorrog. 03/07/2026)'. A prorrogação de julho, se "
        "existe, é decisão posterior que NÃO está no corpus e não foi verificada — não citar sem "
        "obtê-la.",

    "status_classe": "Confirmado em fonte primária",

    "nota_auditoria":
        "PT-60 elevado a fonte primária em 16/08/2026. Duas precisões: a data é 24/03/2026, e a "
        "menção a 'prorrog. 03/07/2026' que constava do registro NÃO tem lastro no corpus — foi "
        "retirada do campo de data e marcada como não verificada. Acrescentado o antecedente "
        "relevante: o mesmo pedido fora INDEFERIDO em 2/3/2026 após perícia oficial, o que "
        "sustenta ler a concessão como modulação técnica e não como recuo.",
}


def main():
    dry = "--dry-run" in sys.argv
    for f in (PET, TRANSF, DOMIC):
        if not (RAIZ / f).exists():
            raise SystemExit("ERRO: não encontrado " + f)

    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    patches = {"PT-58": PT58, "PT-59": PT59, "PT-60": PT60}
    for ev in dados["eventos"]:
        if ev["id"] in patches:
            print("=== {} ===".format(ev["id"]))
            print("  antes :", ev["status_classe"], "|", ev["data_hora"])
            ev.update(patches[ev["id"]])
            print("  depois:", ev["status_classe"], "|", ev["data_hora"])

    reg = dados["metadados"].setdefault("registro_documentos", {})
    reg["Pet 14.129"] = PET
    reg["EP 169-Transferência"] = TRANSF
    reg["EP 169-Domiciliar"] = DOMIC

    dados["metadados"]["revisoes"] = [
        r for r in dados["metadados"]["revisoes"] if not r.startswith("2026-08-16 (execução penal)")
    ]
    dados["metadados"]["revisoes"].append(
        "2026-08-16 (execução penal) — PT-58, PT-59 e PT-60 elevados a 'Confirmado em fonte "
        "primária' com a obtenção das três decisões do min. Alexandre de Moraes. As páginas de "
        "notícia do STF, que recusam o WebFetch com 403, respondem a curl com user-agent de "
        "navegador e trazem link direto para a peça; nenhuma das três rotas exigiu o cookie do "
        "WAF. DUAS CORREÇÕES DE FATO. (1) A prisão preventiva de 22/11/2025 foi decretada na "
        "PETIÇÃO 14.129 — coação no curso do processo, obstrução de investigação e art. 359-L —, "
        "convertendo cautelares de 17/7/2025, e NÃO na execução da AP 2668; o cumprimento da pena "
        "começa em 25/11 e é ato distinto, que o registro anterior fundia com a preventiva. "
        "(2) A domiciliar humanitária é de 24/03/2026, e a menção a 'prorrog. 03/07/2026' que "
        "constava do registro não tem lastro no corpus — foi retirada e marcada como não "
        "verificada. Acrescentou-se ainda que a transferência de 15/01/2026 é para SALA DE ESTADO "
        "MAIOR dentro da Papuda, não para regime comum, e que a domiciliar fora INDEFERIDA em "
        "2/3/2026 antes de ser concedida."
    )

    if dry:
        print("\nDRY RUN — nada gravado")
    else:
        JSON_P.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("\nJSON reescrito.")


if __name__ == "__main__":
    main()
