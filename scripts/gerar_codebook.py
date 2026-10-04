#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gerador do codebook do process tracing do 8 de Janeiro.

O JSON é a ÚNICA fonte da verdade. Este script lê
`process_tracing_8jan_eventos.json` e emite os outros dois formatos:

  - data/processed/process_tracing_8jan_eventos.csv     (UTF-8 com BOM, para Excel pt-BR)
  - data/processed/process_tracing_8jan_codebook.xlsx   (quatro abas)

Nunca edite o CSV ou o XLSX à mão: a próxima execução sobrescreve. Edite o JSON
e rode este script. Foi assim que a divergência entre formatos foi eliminada em
16/08/2026 — antes disso, CSV e JSON tinham esquemas diferentes.

Uso:  python scripts/gerar_codebook.py
"""

import csv
import json
import os
from collections import OrderedDict, defaultdict
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

RAIZ = Path(__file__).resolve().parent.parent
JSON_IN = RAIZ / "process_tracing_8jan_eventos.json"
CSV_OUT = RAIZ / "data/processed/process_tracing_8jan_eventos.csv"
XLSX_OUT = RAIZ / "data/processed/process_tracing_8jan_codebook.xlsx"

CABECALHOS = OrderedDict([
    ("id", "ID"), ("data_hora", "Data_Hora"), ("fase", "Fase"),
    ("ator_grupo", "Ator_Grupo"), ("repertorio_acao", "Repertorio_Acao"),
    ("target_alvo", "Target_Alvo"), ("framing_narrativa", "Framing_Narrativa"),
    ("resposta_estatal", "Resposta_Estatal"), ("mecanismo_causal", "Mecanismo_Causal"),
    ("fonte_trecho", "Fonte_Trecho"), ("fonte_url", "Fonte_URL"),
    ("fonte_local", "Fonte_Local"), ("fonte_pagina", "Fonte_Pagina"),
    ("status_verificacao", "Status_Verificacao"), ("status_classe", "Status_Classe"),
    ("nota_auditoria", "Nota_Auditoria"),
])

# Definições do dicionário de variáveis. Sai na aba `Dicionario` do XLSX e é o
# que um parecerista lê para entender o que cada campo significa.
DICIONARIO = [
    ("id", "Identificador do sub-evento. Sufixo alfabético (PT-03A) indica registro inserido em revisão posterior, mantendo a ordem cronológica.", "texto", "PT-01 … PT-62 com sufixos", "atribuído pelo pesquisador"),
    ("data_hora", "Data e, quando aplicável, hora do sub-evento. Granularidade variável: de 'jun/2013' a '08/01/2023 15h16'.", "texto", "livre", "fonte"),
    ("fase", "Fase do process tracing.", "categórico", "T-1 Conjuntural · T-1 Operacional · T0 Mobilização · T0 Execução · T0 Resposta tática/política · T+1 (várias)", "atribuído pelo pesquisador"),
    ("ator_grupo", "Quem age. Indivíduo, órgão, corporação ou coletivo.", "texto", "livre", "fonte"),
    ("repertorio_acao", "O que foi feito, no vocabulário de repertórios de Tilly.", "texto", "livre", "fonte + leitura do pesquisador"),
    ("target_alvo", "Contra quem ou o quê a ação se dirige.", "texto", "livre", "fonte + leitura do pesquisador"),
    ("framing_narrativa", "Enquadramento invocado pelos atores, preferencialmente em suas próprias palavras.", "texto", "livre", "fonte"),
    ("resposta_estatal", "Reação do Estado ao sub-evento, inclusive a omissão.", "texto", "livre", "fonte"),
    ("mecanismo_causal", "ATRIBUIÇÃO ANALÍTICA do pesquisador, derivada de Dynamics of Contention. NÃO é citação da fonte e não deve ser lido como achado estabelecido.", "texto", "livre", "pesquisador"),
    ("fonte_trecho", "Referência e, quando há, transcrição literal do trecho que sustenta o registro.", "texto", "livre", "fonte"),
    ("fonte_url", "URL da fonte, quando pública.", "url", "livre", "fonte"),
    ("fonte_local", "Caminho do arquivo em Fontes/, relativo à raiz do projeto. Vários documentos separados por '; '.", "caminho", "ver aba Inventario_Fontes", "auditoria de 16/08/2026"),
    ("fonte_pagina", "Página citada, prefixada pelo código curto do documento — 'CPMI: 646, 711 | Cappelli: 55, 57'. O prefixo existe para que a página nunca fique atribuída ao documento errado.", "texto estruturado", "COD: n[, n] [| COD: n]", "extraído de fonte_trecho, conferido manualmente"),
    ("status_verificacao", "Status em texto livre, com a nuance de cada caso. Preservado integralmente.", "texto", "livre", "pesquisador"),
    ("status_classe", "Redução do status a vocabulário controlado, para contagem e filtro.", "categórico", "Confirmado em fonte primária · Confirmado · Contextual · A verificar · Inferência do analista", "derivado de status_verificacao"),
    ("nota_auditoria", "O que a auditoria de fontes alterou neste registro e por quê. Vazio = registro não tocado.", "texto", "livre", "auditoria de 16/08/2026"),
]

# Procedência de cada arquivo do corpus. 'espelho' significa que o documento traz
# identificação oficial mas não foi localizado em domínio oficial — distinção que
# precisa ficar declarada em pesquisa científica.
PROCEDENCIA = {
    "Fontes/04_T+1_Resposta-institucional/CPMI-8-de-Janeiro_Relatorio-Final_2023-10-17.pdf":
        ("Senado Federal — senado.leg.br", "oficial", "Espinha dorsal de T0. Numeração impressa coincide com a do PDF."),
    "Fontes/04_T+1_Resposta-institucional/STF_AP-2668_Acordao_Condenacao_2025-09-11.pdf":
        ("STF — redir.stf.jus.br", "oficial", "Inteiro teor com todos os votos."),
    "Fontes/04_T+1_Resposta-institucional/STF_Pet-14129_Decisao-Prisao-Preventiva_2025-11-22.pdf":
        ("STF — PDF hospedado pela Agência Brasil (EBC)", "oficial",
         "Decisão do min. Alexandre de Moraes na Pet 14.129/DF, 22/11/2025, 17 p. Decreta a "
         "prisão preventiva. Ancora PT-58. ATENÇÃO: processo DISTINTO da AP 2668 — trata de "
         "coação no curso do processo, obstrução e art. 359-L."),
    "Fontes/04_T+1_Resposta-institucional/STF_EP-169_Decisao-Transferencia-Papuda_2026-01-15.pdf":
        ("STF — bucket noticias-stf-wp-prd (S3)", "oficial",
         "Decisão do min. Alexandre de Moraes na EP 169/DF, 15/01/2026, 36 p. Transferência para "
         "Sala de Estado Maior no 19º BPM, na Papuda. Ancora PT-59."),
    "Fontes/04_T+1_Resposta-institucional/STF_EP-169_Decisao-Prisao-Domiciliar_2026-03-24.pdf":
        ("STF — portal.stf.jus.br/processos/downloadPeca.asp", "oficial",
         "Decisão do min. Alexandre de Moraes na EP 169/DF, 24/03/2026, 40 p. Autoriza prisão "
         "domiciliar humanitária por 90 dias da alta médica. Ancora PT-60."),
    "Fontes/09_Arquivamento-web/AgenciaBrasil_2017-07-12_Condenacao-Lula_PT-03A.html":
        ("Agência Brasil (EBC) — arquivamento local", "arquivamento web",
         "Cópia de matéria que ancora registro só por URL. Preserva a evidência contra link rot. "
         "NÃO é fonte primária."),
    "Fontes/04_T+1_Resposta-institucional/STF_AP-2668-QO_Acordao_2025-05-14.pdf":
        ("STF — redir.stf.jus.br", "oficial", "Questão de ordem preliminar."),
    "Fontes/03_T0_8-de-janeiro/GDF-SSP_Relatorio-Interventor-Federal_Cappelli_2023-01-27.pdf":
        ("Espelho jornalístico — Poder360", "espelho", "Traz cabeçalho e identificação oficiais, mas NÃO foi localizado em domínio oficial. Conclusões A-H, p. 53-60."),
    "Fontes/02_T-1_Articulacao/PGR_Denuncia_PET-12100_Nucleo-1_2025-02-18.pdf":
        ("Agência Brasil (EBC), assinada por Paulo Gustavo Gonet Branco", "oficial", "Chave de validação verificável em transparencia.mpf.mp.br/validacaodocumento."),
    "Fontes/01_Arco-judicial_2017-2021/TRF4_Revista-97_Acordao-ACr-5046512-94_2018-01-24.pdf":
        ("TRF-4 — trf4.jus.br/trf4/revistatrf4", "oficial", "Revista nº 97. Traz o dispositivo da sentença de Moro transcrito, p. 395."),
    "Fontes/01_Arco-judicial_2017-2021/TSE_RCand-0600903-50_Acordao_2018-09-01.html":
        ("TSE — Consulta Unificada PJe, consultaunificadapje.tse.jus.br", "oficial",
         "Inteiro teor do acórdão que indeferiu o registro de candidatura de Lula "
         "(RCand 0600903-50.2018.6.00.0000, rel. min. Barroso, 1º/09/2018). Ancora PT-03E. "
         "SERVIDO EM HTML, não em PDF: o parâmetro extensaoArquivo do endpoint só muda o "
         "Content-Type. Citar por estrutura interna (item da ementa, dispositivo), não por "
         "página. Obtido SEM captcha — o buscador de jurisprudência exige hCaptcha, este "
         "endpoint não."),
    "Fontes/01_Arco-judicial_2017-2021/STF_ADC-43-44-54_Acordao_2019-11-07.pdf":
        ("STF — redir.stf.jus.br", "oficial", "Constitucionalidade do art. 283 do CPP."),
    "Fontes/01_Arco-judicial_2017-2021/STF_ADC-43-MC_Acordao_2016-10-05.pdf":
        ("STF — redir.stf.jus.br", "oficial", "Medida cautelar de 2016, precedente da execução provisória."),
    "Fontes/01_Arco-judicial_2017-2021/STF_HC-152752_Acordao_2018-04-04.pdf":
        ("STF — redir.stf.jus.br", "oficial", "Denegação por 6x5."),
    "Fontes/01_Arco-judicial_2017-2021/STF_HC-164493_Acordao_Suspeicao-Moro_2021-03-23.pdf":
        ("STF — redir.stf.jus.br", "oficial", "2ª Turma reconhece a suspeição."),
    "Fontes/01_Arco-judicial_2017-2021/STF_HC-193726-AgR_Acordao_2021-04-15.pdf":
        ("STF — redir.stf.jus.br", "oficial", "Plenário confirma a anulação (8x3)."),
    "Fontes/01_Arco-judicial_2017-2021/STF_HC-193726-AgR-segundo_Acordao_2021-06-23.pdf":
        ("STF — redir.stf.jus.br", "oficial", "Plenário mantém o entendimento (7x4)."),
    "Fontes/07_NetLab-UFRJ/NetLab-UFRJ_Anuncios-golpistas-Meta-Ads_2023-02-07.md":
        ("NetLab UFRJ — transcrição de publicação web", "transcrição", "Relatório de laboratório universitário, NÃO revisado por pares."),
    "Fontes/07_NetLab-UFRJ/Doxa-IESP-UERJ_Manchetometro_Atos-golpistas-8-jan_2023-03.pdf":
        ("Doxa/IESP-UERJ — Manchetômetro", "laboratório",
         "Relatório temático mar/2023, 16 p. ANCORA PT-50A desde 16/08/2026, quando deixou de "
         "ser órfão. NÃO revisado por pares. Coleta via CrowdTangle, descontinuado pela Meta em "
         "14/08/2024 — dados não reproduzíveis. URL de origem não registrada: pendência."),
    "Fontes/05_Bibliografia-teorica/Livro_Process tracing.pdf":
        ("Bibliografia metodológica", "bibliografia", "Referencial de método, não corpus empírico."),
    "Fontes/05_Bibliografia-teorica/process-tracing-research-designs-a-practical-guide.pdf":
        ("Bibliografia metodológica", "bibliografia", "Referencial de método, não corpus empírico."),
    "Fontes/06_Lava-Jato-judicializacao-lawfare/bibliografia_eixo_lava-jato.csv":
        ("Levantamento próprio, verificado no CrossRef", "bibliografia",
         "20 referências, 18 com DOI confirmado. Instrumento de busca, não fonte de evento."),
    "Fontes/06_Lava-Jato-judicializacao-lawfare/bibliografia_comentada.md":
        ("Levantamento próprio", "bibliografia",
         "Comentário das 20 referências do eixo. Não é fonte de evento."),
    "Fontes/10_Democracia-Inabalada/STF_Gabinete-Moraes_Balanco-8-de-Janeiro_2026-04-29.pdf":
        ("STF — bucket oficial noticias-stf-wp-prd (S3)", "oficial",
         "Relatório do Gabinete do Min. Alexandre de Moraes, 29/04/2026, 15 p. Ancora PT-53 e "
         "PT-61. PEÇA GRÁFICA: números em gráficos vetoriais (AÇÕES PENAIS na p. 6; "
         "infográfico da p. 5) NÃO saem na camada de texto — exigem leitura visual."),
    "Fontes/10_Democracia-Inabalada/STF_Democracia-Inabalada_Ebook_28x28cm.pdf":
        ("STF — publicação oficial, ISBN 978-85-54223-50-2", "oficial",
         "Livro '8.1.2023: Democracia Inabalada', ago/2023, 210 p. Ancora PT-38. CÓPIA "
         "CONSOLIDADA em 16/08/2026: era duplicata byte-idêntica da que estava em "
         "03_T0_8-de-janeiro/, removida na mesma data (SHA-256 conferido). NÃO confundir com o "
         "balanço de abr/2026, que é documento distinto, nesta mesma pasta."),
    "Fontes/10_Democracia-Inabalada/PAGINA-CAMPANHA-catalogacao.md":
        ("Catalogação própria da página oficial da campanha", "catalogação",
         "Inventário das peças da campanha #DemocraciaInabalada (livro, documentário, 15 "
         "vídeos, 13 cards, folder) com URLs e termos de uso. Objeto de enquadramento, não "
         "fonte de evento."),
    "Fontes/10_Democracia-Inabalada/DOCUMENTARIO-catalogacao.md":
        ("Catalogação própria, a partir de metadados oficiais", "catalogação",
         "Ficha do documentário (57min01s, Rádio e TV Justiça, 30/08/2023) e sinopse oficial. "
         "NÃO é resumo de quem assistiu — a transcrição não foi obtida."),
    "Fontes/10_Democracia-Inabalada/STF_Democracia-Inabalada_Folder.pdf":
        ("STF — campanha #DemocraciaInabalada", "peça de divulgação",
         "Folder institucional, 6 p., SEM camada de texto (peça gráfica). Conteúdo lido por "
         "extração de imagem: capa com hashtag, citação da min. Rosa Weber, tríptico do "
         "Plenário (dez/2022 → jan/2023 destruído → fev/2023 restaurado) e assinatura do STF. "
         "Material de comunicação, não fonte de evento."),
    "Fontes/08_Imprensa-enquadramento/SciELO-Preprints_Drummond-Manginelli_Editoriais-8-jan_2023-10-09.pdf":
        ("SciELO Preprints — DOI 10.1590/SciELOPreprints.7040, CC-BY 4.0", "preprint",
         "Drummond (IESP-UERJ) e Manginelli (UFPR), postado em 09/10/2023. Análise temática e de "
         "enquadramento de 105 editoriais (Folha 34, Estadão 36, O Globo 35), 1 a 18/01/2023. "
         "NÃO revisado por pares — verificar publicação definitiva antes de citar. NÃO traz "
         "números de manifestantes: sustenta a frente de disputa discursiva, não o codebook."),
}

# Arquivamento web: cópias de matérias que ancoram registros só por URL.
# Preservam a evidência contra link rot; NÃO são fonte primária.
for _arq in ["AgenciaBrasil_2018-04-07_Prisao-Curitiba_PT-03D.html",
             "AgenciaBrasil_2024-09_Obras-recuperadas_PT-38.html",
             "AgenciaBrasil_2025-11-22_Prisao-preventiva_PT-58.html",
             "AgenciaBrasil_2025-11-25_Cumprimento-pena_PT-58.html",
             "STF-noticias_Transferencia-Papuda_PT-59.html",
             "STF-noticias_Prisao-domiciliar_PT-60.html"]:
    PROCEDENCIA["Fontes/09_Arquivamento-web/" + _arq] = (
        "Arquivamento local da matéria original", "arquivamento web",
        "Cópia preservada contra link rot. NÃO é fonte primária: serve como evidência de que a "
        "notícia existiu e do que dizia.")

# Sínteses geradas por sistema automatizado. Não são citáveis e não ancoram
# registro nenhum — servem como mapa de leitura e lista de DOIs a verificar.
# As contagens abaixo são DOIs distintos por arquivo, no critério de
# scripts/verificar_dois_sinteses.py, que as imprime a cada execução.
# Conferidas em 29/09/2026; a de Causal_mechanisms é 90, e o inventário de
# fontes trazia 89 por recontagem errada de 01/09.
for _nome, _dois in [("Process_tracing", 77), ("Causal_mechanisms_in_social_science", 90),
                     ("Political_Process_by_Charles_Tilly", 82),
                     ("Mobilization_structures", 76), ("Protest_cycle", 24),
                     ("Political_and_discursive_opportunities", 46),
                     ("Framing_process_and_alignment", 44)]:
    PROCEDENCIA["Fontes/05_Bibliografia-teorica/{}_LeapSpace.docx".format(_nome)] = (
        "LeapSpace — síntese gerada automaticamente", "não citável",
        "NÃO revisada por pares, sem autoria identificável. {} DOIs, verificados em "
        "29/09/2026 no CrossRef e na DataCite por scripts/verificar_dois_sinteses.py — ver "
        "data/processed/dois_sinteses_leapspace.csv, que registra também se o título declarado "
        "casa com o do DOI. Mapa de leitura, nunca citação.".format(_dois),
    )

# Diário Oficial do DF, coletado em 30/09/2026 pela tarefa 24: são a fonte dos
# atos que o anexo 14 do Relatório do Interventor apenas compila, e entraram
# porque a varredura do DODF contrariou a descrição do interventor.
PROCEDENCIA["Fontes/02_T-1_Articulacao/DODF-001_Decreto-01-01-2023_Nomeacao-Torres-SSPDF_2023-01-02.pdf"] = (
    "Diário Oficial do Distrito Federal — portal oficial dodf.df.gov.br", "oficial",
    "DODF nº 001, de 02/01/2023, 66 p. Seção II, p. 16: decreto de 1º/01/2023 que exonera "
    "Julio Danilo Souza Ferreira e nomeia Anderson Gustavo Torres secretário de Segurança "
    "Pública do DF, assinado por Ibaneis Rocha. Ancora PT-18A.",
)
PROCEDENCIA["Fontes/02_T-1_Articulacao/DODF-003_Decreto-03-01-2023_Ajudancia-de-Ordens-SSPDF_2023-01-04.pdf"] = (
    "Diário Oficial do Distrito Federal — portal oficial dodf.df.gov.br", "oficial",
    "DODF nº 003, de 04/01/2023, 66 p. Seção II, p. 35: decreto de 03/01/2023, ÚNICO ato de "
    "pessoal da SSP-DF publicado naquele dia — troca do Chefe da Ajudância de Ordens do "
    "Gabinete, que é apoio pessoal do secretário e não a estrutura de planejamento. Ancora a "
    "divergência registrada em PT-18A.",
)

# Cânone de mecanismos, acrescentado à mão em 29/09/2026: a triagem dos DOIs das
# sínteses (item 23 da agenda) mostrou que as obras de que o codebook toma o
# vocabulário — certificação, difusão, repertório, limiar — não estavam no corpus.
PROCEDENCIA["Fontes/05_Bibliografia-teorica/McADAM-TARROW-TILLY_Dynamics-of-Contention_Cambridge-2001.pdf"] = (
    "McAdam, Tarrow e Tilly — Cambridge University Press", "bibliografia",
    "McADAM, D.; TARROW, S.; TILLY, C. 'Dynamics of Contention'. Cambridge: CUP, 2001. "
    "ISBN 0-521-80588-0. DOI 10.1017/CBO9780511805431. 411 p. no PDF, com camada de texto. "
    "É a obra do vocabulário causal que o codebook usa; não ancora registro nenhum.",
)
PROCEDENCIA["Fontes/05_Bibliografia-teorica/TARROW_O-poder-em-movimento_Vozes-2009.pdf"] = (
    "Sidney Tarrow — tradução brasileira, Editora Vozes", "bibliografia",
    "TARROW, S. 'O poder em movimento: movimentos sociais e confronto político'. Trad. Ana "
    "Maria Sallum. Petrópolis: Vozes, 2009. ISBN 978-85-326-3828-1. Original: 'Power in "
    "movement'. 162 p. no PDF, digitalização em duas páginas por folha e SEM camada de "
    "texto — conferir_paginas.py não o lê. Não ancora registro nenhum.",
)
# Acrescentada em 30/09/2026 pelo pesquisador. É a obra-contêiner de boa parte dos
# 411 DOIs das sínteses: 434 verbetes com DOI próprio, o que a torna a fonte que
# permite ler na fonte os verbetes da camada A sem passar por muro de editor.
PROCEDENCIA["Fontes/05_Bibliografia-teorica/SNOW-DELLA-PORTA-KLANDERMANS-McADAM_Wiley-Blackwell-Encyclopedia-of-Social-and-Political-Movements_2013.pdf"] = (
    "Snow, della Porta, Klandermans e McAdam (orgs.) — Wiley-Blackwell", "bibliografia",
    "SNOW, D. A.; DELLA PORTA, D.; KLANDERMANS, B.; McADAM, D. (Orgs.). 'The "
    "Wiley-Blackwell Encyclopedia of Social and Political Movements'. Oxford: Blackwell, "
    "2013. 1.638 p. no PDF, com camada de texto; 434 verbetes com DOI impresso no rodapé. "
    "ATENÇÃO AO IDENTIFICADOR: o rodapé imprime o prefixo do ISBN impresso "
    "(10.1002/9781405198431.wbespmNNN), que retorna 404 no CrossRef; o registrado é o do "
    "ISBN eletrônico (10.1002/9780470674871.wbespmNNN). Não ancora registro nenhum.",
)

# Antecedente teórico do projeto. Não ancora registro nenhum e não é fonte de
# evento: é a obra de que a pesquisa parte, incorporada em 19/08/2026.
PROCEDENCIA["Fontes/11_Tese-doutorado/PACCELLI_Tese-doutorado_UFJF_2024.docx"] = (
    "Tese de doutorado do pesquisador — UFJF/PPGCSO", "bibliografia",
    "PACCELLI, Gustavo. 'Estruturas de mobilização e Oportunidades Políticas: análise dos "
    "ciclos de protestos no Brasil contemporâneo'. UFJF, Programa de Pós-Graduação em "
    "Ciências Sociais, 2024. Orientação: Christiane Jalles de Paula. Analisa três ciclos "
    "(1992, 2013, 2015) pela interação entre estruturas de mobilização e oportunidades "
    "políticas e discursivas; a última seção substantiva trata da entrada dos movimentos de "
    "direita. É o antecedente teórico do projeto e a origem do par analítico adotado — "
    "inclusive de Koopmans & Olzak (2004) sobre oportunidades discursivas e violência de "
    "extrema-direita. NÃO é fonte de evento e não deve ancorar registro do codebook.",
)

# Literatura da camada T-1 conjuntural, incorporada em 04/10/2026 pela tarefa 14.
# São o PRIMEIRO caso no corpus de peça que é literatura secundária E ancora
# registro: até aqui, quem ancorava era documento oficial, e teoria não ancorava
# nada. Por isso o eixo 12 fica FORA da contagem documental em
# verificar_integridade.py, ao lado do eixo 05 — o número de "documentos oficiais"
# não pode crescer porque entrou artigo de revista.
#
# A NUMERAÇÃO DA REVISTA NÃO COINCIDE COM A DO PDF em nenhum dos quatro, e
# `fonte_pagina` guarda a do PDF, que é a que conferir_paginas.py abre. O
# deslocamento vai declarado aqui, item por item, porque é o que permite
# converter a âncora em citação publicável.
# A ORIGEM entrou como quinto campo em 04/10/2026, na segunda rodada da tarefa 14:
# as quatro primeiras peças vieram todas da mesma pasta do pesquisador, e a origem
# estava fixa no código. As três que entraram depois vêm de três lugares distintos,
# e de onde veio a peça é parte da proveniência, não detalhe de coleta.
_PASTA = "Pasta de textos de ação coletiva do pesquisador — artigo revisado por pares"
for _arq, _ref, _desloc, _nota, _orig in [
    ("TATAGIBA_Ciclos-de-protestos-e-democracia_Politica-e-Sociedade-28_2014.pdf",
     "TATAGIBA, Luciana. '1984, 1992 e 2013. Sobre ciclos de protestos e democracia no "
     "Brasil'. Política & Sociedade, Florianópolis, v. 13, n. 28, p. 35-62, set./dez. 2014. "
     "DOI 10.5007/2175-7984.2014v13n28p35",
     "p. da revista = p. do PDF + 34",
     "SEM CAMADA DE TEXTO — é digitalização. Lido por renderização a 170 dpi, a mesma "
     "técnica usada nos dois gráficos vetoriais do balanço do STF. As transcrições deste "
     "documento estão em EXCECOES de conferir_paginas.py, com o motivo. Ancora PT-01.",
     _PASTA),
    ("TATAGIBA-GALVAO_Protestos-no-Brasil-em-tempos-de-crise_Opiniao-Publica-25-1_2019.pdf",
     "TATAGIBA, Luciana; GALVÃO, Andreia. 'Os protestos no Brasil em tempos de crise "
     "(2011-2016)'. Opinião Pública, Campinas, v. 25, n. 1, p. 63-96, jan./abr. 2019. "
     "DOI 10.1590/1807-0191201925163",
     "p. da revista = p. do PDF + 62",
     "Análise de eventos de protesto sobre a Folha de S.Paulo: 1.285 eventos entre "
     "1/1/2011 e 31/8/2016. Ancora PT-01, PT-02 e PT-03.",
     _PASTA),
    ("PINTO_Trajetoria-discursiva-das-manifestacoes-de-rua_Lua-Nova-100_2017.pdf",
     "PINTO, Céli Regina Jardim. 'A trajetória discursiva das manifestações de rua no "
     "Brasil (2013-2015)'. Lua Nova, São Paulo, n. 100, p. 119-153, 2017. "
     "DOI 10.1590/0102-119153/100",
     "p. da revista = p. do PDF + 118",
     "Ancora PT-01 e PT-02. É a peça que documenta, na p. 150, faixas por intervenção "
     "militar e o movimento 'SOS Forças Armadas' já em março de 2015.",
     _PASTA),
    ("ALONSO_Repertorio-segundo-Charles-Tilly_Sociologia-e-Antropologia-2-3_2012.pdf",
     "ALONSO, Angela. 'Repertório, segundo Charles Tilly: história de um conceito'. "
     "Sociologia & Antropologia, Rio de Janeiro, v. 2, n. 3, p. 21-41, 2012",
     "p. da revista = p. do PDF + 20",
     "ATENÇÃO: NÃO é a 'Alonso (2017)' que PT-01 e PT-02 citavam — essa nunca esteve no "
     "corpus. Ancora PT-02 pela história do conceito de repertório.",
     _PASTA),
    # As três abaixo entraram em 04/10/2026, na SEGUNDA rodada da tarefa 14, e são
    # as que sustentam a leitura de continuidade entre 2013 e 2015-2016.
    ("KUNRATH-SILVA_Apropriacao-conservadora-do-ciclo-de-protestos_Lusotopie-17-1_2018.pdf",
     "SILVA, Marcelo Kunrath. 'A apropriação conservadora do ciclo de protestos de 2013: "
     "rumo aos protestos anti-Dilma?'. Lusotopie, v. 17, n. 1, p. 88-111, 2018. "
     "DOI 10.1163/17683084-12341713",
     "NÃO HÁ OFFSET: a edição eletrônica da OpenEdition não reproduz a paginação impressa "
     "88-111. A unidade citável é o PARÁGRAFO (§), numerado pela própria OpenEdition; "
     "`fonte_pagina` guarda, como sempre, a página do PDF",
     "CAMADA DE TEXTO PRESENTE E ERRADA — a fonte Gentium-Book-Basic vem com CMap "
     "defeituoso: o código de cada glifo é o ASCII menos 29. PyPDF2 e PyMuPDF devolvem "
     "sopa de letras, e uma busca ingênua 'prova' que o artigo não diz nada. "
     "conferir_paginas.py desfaz o deslocamento span por span (_desloca), porque as outras "
     "fontes do mesmo arquivo saem corretas. É a peça que NOMEIA o mecanismo de PT-02: a "
     "apropriação em causa não é de recursos nem de estruturas, é de um repertório (§ 15). "
     "Ancora PT-01 e PT-02.",
     "OpenEdition (journals.openedition.org/lusotopie/2568) — acesso aberto, "
     "artigo revisado por pares"),
    ("KUNRATH-SILVA_Ciclo-de-protestos-de-2013-objeto-de-disputa_Desigualdade-e-Diversidade-23_2023.pdf",
     "SILVA, Marcelo Kunrath. 'Ciclo de protestos de 2013: contribuições do campo de estudos "
     "de movimentos sociais e protesto para a análise de um objeto de disputa'. Desigualdade "
     "& Diversidade, n. 23, p. 57-90, 2023. DOI 10.17771/PUCRio.DDCIS.64184",
     "p. da revista = p. do PDF + 56",
     "É a PRIMEIRA peça do corpus que liga o ciclo de protestos a Bolsonaro e ao "
     "intervencionismo militar, na p. 86 impressa — e é por isso que PT-04 deixou de ser "
     "contextual. Ancora PT-01, PT-03 e PT-04.",
     "Maxwell PUC-Rio (maxwell.vrac.puc-rio.br/64184) — acesso aberto, "
     "artigo revisado por pares"),
    ("ALONSO_Treze-a-politica-de-rua-de-Lula-a-Dilma_Companhia-das-Letras_2023.pdf",
     "ALONSO, Angela. Treze: a política de rua de Lula a Dilma. São Paulo: Companhia das "
     "Letras, 2023. ISBN 978-85-3593-492-2",
     "NÃO HÁ OFFSET A DECLARAR PORQUE NÃO HÁ PAGINAÇÃO IMPRESSA: é edição digital, sem "
     "número de página de papel e sem rótulos de página no PDF. 'p. 219' é a página do PDF, "
     "e quem conferir na edição em papel não encontrará o mesmo número. Esta é a terceira "
     "variante de armadilha de numeração do eixo 12",
     "Livro acadêmico, não artigo: tem capítulo de método ('História de uma pesquisa') e "
     "lista de fontes primárias. Entra como literatura secundária, como os demais do eixo. "
     "É a peça que dá o ATOR — o 'campo patriota', presente em junho de 2013 e então não "
     "reconhecido como ator político. Ancora PT-01, PT-02, PT-03 e PT-04.",
     "Exemplar fornecido pelo pesquisador em 04/10/2026 — livro de editora comercial"),
]:
    PROCEDENCIA["Fontes/12_Camada-T-1_Literatura/" + _arq] = (
        _orig, "literatura", "{} | {} | {}".format(_ref, _desloc, _nota))

# Eixo 13 — a literatura do bolsonarismo como fenômeno de mobilização. DEZOITO
# peças, em três procedências distintas, e a distinção é o que este bloco existe
# para registrar:
#
#   (a) DOZE coletadas em 04/10/2026 pela tarefa 25 via OpenAlex, com DOI resolvido
#       e título conferido contra o que o OpenAlex devolve (os DOIS eixos da regra
#       de 29/09: existir não é estar bem atribuído). **Nenhuma lida, nenhuma
#       ancorando registro.** Isto está escrito aqui, e não só no documento 13,
#       porque é a declaração que impede o acidente: um arquivo em Fontes/ parece
#       lastro, e estas doze são fila de leitura.
#
#   (b) DUAS lidas na fonte na terceira rodada do mesmo dia, por encaminhamento do
#       pesquisador, e que ANCORAM registro com página — Araujo e Sales (2022) e
#       Fernandes e Silva (2021). Entram no mesmo padrão do eixo 12: offset de
#       paginação declarado e transcrição conferida por conferir_paginas.py.
#
#   (c) QUATRO entregues pelo pesquisador em 04/10/2026, as mesmas que a coleta
#       automatizada não alcançara (Cambridge, SAGE, Oxford e um OJS equatoriano).
#       **Coletadas, não lidas.** O bloqueio era do acesso automatizado, não da
#       obra: é o resultado que o documento 13 registra, e a entrega o confirma.
#       Duas trazem correção de atribuição — ver o campo de nota de cada uma.
_COLETA25 = ("Coleta da tarefa 25 (04/10/2026) via OpenAlex — acesso aberto, "
             "artigo revisado por pares. COLETADA, NÃO LIDA: não ancora registro")
for _arq, _ref, _serve in [
    ("MESSENBERG_A-direita-que-saiu-do-armario_Sociedade-e-Estado-32-3_2017.pdf",
     "MESSENBERG, Débora. 'A direita que saiu do armário: a cosmovisão dos formadores de "
     "opinião dos manifestantes de direita'. Sociedade e Estado, v. 32, n. 3, 2017. "
     "DOI 10.1590/s0102-69922017.3203004",
     "PT-02 — cosmovisão dos manifestantes de direita de 2015-2016"),
    ("ROCHA_Imposto-e-roubo-contrapublico-ultraliberal_Dados-62-3_2019.pdf",
     "ROCHA, Camila. \"'Imposto é Roubo!' A Formação de um Contrapúblico Ultraliberal e os "
     "Protestos Pró-Impeachment de Dilma Rousseff\". Dados, v. 62, n. 3, 2019. "
     "DOI 10.1590/001152582019189",
     "PT-02 e PT-03 — formação do contrapúblico ultraliberal e os protestos pró-impeachment"),
    ("CESARINO_Identidade-e-representacao-no-bolsonarismo_Revista-de-Antropologia-62-3_2019.pdf",
     "CESARINO, Letícia. 'Identidade e representação no bolsonarismo'. Revista de "
     "Antropologia, v. 62, n. 3, 2019. DOI 10.11606/2179-0892.ra.2019.165232",
     "PT-04 — a obra que PT-04 citava sem ter; entra no corpus pela primeira vez"),
    ("CESARINO_Bolsonarismo-sem-Bolsonaro-publicos-antiestruturais_Revista-do-IEB-82_2022.pdf",
     "CESARINO, Letícia. 'Bolsonarismo sem Bolsonaro? Públicos antiestruturais na nova "
     "fronteira cibernética'. Revista do Instituto de Estudos Brasileiros, n. 82, 2022. "
     "DOI 10.11606/issn.2316-901x.v1i82p162-188",
     "PT-06 — públicos antiestruturais e o ecossistema informacional, que é a junta da cadeia"),
    ("TATAGIBA_Entre-as-ruas-e-as-instituicoes-impeachment_Lusotopie-17-1_2018.pdf",
     "TATAGIBA, Luciana. 'Entre as ruas e as instituições: os protestos e o impeachment de "
     "Dilma Rousseff'. Lusotopie, v. 17, n. 1, p. 112-135, 2018. DOI 10.1163/17683084-12341714",
     "PT-02 e PT-03 — mesmo número da Lusotopie em que está Kunrath Silva (2018)"),
    ("SANTOS-TANSCHEIT_Quando-velhos-atores-saem-de-cena-nova-direita_Colombia-Internacional-99_2019.pdf",
     "SANTOS, Fabiano; TANSCHEIT, Talita. 'Quando velhos atores saem de cena: a ascensão da "
     "nova direita política no Brasil'. Colombia Internacional, n. 99, 2019. "
     "DOI 10.7440/colombiaint99.2019.06",
     "PT-04 — ascensão da nova direita política"),
    ("CARVALHO-TATAGIBA_Quando-o-conflito-eleitoral-extravasa-para-as-ruas_Lua-Nova-124_2025.pdf",
     "CARVALHO, Priscila Delgado de; TATAGIBA, Luciana. 'Quando o conflito eleitoral "
     "extravasa para as ruas: protestos e eleições presidenciais no Brasil'. Lua Nova, "
     "n. 124, 2025. DOI 10.1590/0102-124046pd/124",
     "PT-04 e T-1 operacional — conflito eleitoral que extravasa para as ruas"),
    ("KAYSEL-BIANCHI_Bolsonarismo-como-coalizao-discursiva-de-extrema-direita_Caderno-CRH-38_2025.pdf",
     "KAYSEL, André; BIANCHI, Álvaro. 'Bolsonarismo como coalizão discursiva de "
     "extrema-direita'. Caderno CRH, v. 38, 2025. DOI 10.9771/ccrh.v38i0.66145",
     "PT-04 — o bolsonarismo como coalizão, não como partido nem como movimento único"),
    ("NUNES_A-palavra-e-a-coisa-bolsonarismo-como-infraestrutura_Lua-Nova-122_2024.pdf",
     "NUNES, Rodrigo. 'A palavra e a coisa: bolsonarismo como convergência, horizonte, "
     "infraestrutura, ecologia'. Lua Nova, n. 122, 2024. DOI 10.1590/0102-001020rn/122",
     "PT-06 — bolsonarismo como infraestrutura e ecologia, vocabulário próximo do mecanismo "
     "que PT-06 afirma"),
    ("MENDONCA-FREITAS_Fake-news-e-o-repertorio-contemporaneo-de-acao-politica_Dados-66-2_2022.pdf",
     "MENDONÇA, Ricardo Fabrino; FREITAS, Viviane Gonçalves. 'Fake News e o Repertório "
     "Contemporâneo de Ação Política'. Dados, v. 66, n. 2, 2022. "
     "DOI 10.1590/dados.2023.66.2.301",
     "PT-06 — desinformação tratada como repertório, que é o vocabulário do codebook"),
    ("MENDONCA-DOMINGUES_Protestos-contemporaneos-e-a-crise-da-democracia_RBCP-37_2021.pdf",
     "MENDONÇA, Ricardo Fabrino; DOMINGUES, Letícia Birchal. 'Protestos contemporâneos e a "
     "crise da democracia'. Revista Brasileira de Ciência Política, n. 37, 2021. "
     "DOI 10.1590/0103-3352.2022.37.246424",
     "PT-05 — protesto e erosão democrática"),
    ("CHAGAS-CARREIRO_Far-right-digital-activism-in-polarized-contexts_Media-and-Communication-10-4_2022.pdf",
     "CHAGAS, Viktor; CARREIRO, Rodrigo. 'Far-Right Digital Activism in Polarized Contexts'. "
     "Media and Communication, v. 10, n. 4, 2022. DOI 10.17645/mac.v10i4.5622",
     "PT-06 — ativismo digital de extrema-direita"),
]:
    PROCEDENCIA["Fontes/13_Bolsonarismo-mobilizacao/" + _arq] = (
        _COLETA25, "literatura", "{} | SERVE A: {}".format(_ref, _serve))

# (b) As duas LIDAS na terceira rodada de 04/10/2026, por encaminhamento do
# pesquisador. Ancoram registro com página, e por isso declaram offset — a regra
# do eixo 12 vale igual aqui.
_LIDAS25 = ("Coleta da tarefa 25 (04/10/2026) via OpenAlex, LIDA NA FONTE na "
            "terceira rodada do mesmo dia — acesso aberto, artigo revisado por "
            "pares. ANCORA REGISTRO com página")
for _arq, _ref, _desloc, _serve in [
    ("ARAUJO-SALES_Atuacao-politica-das-Forcas-Armadas-e-bolsonarismo_Cadernos-do-Tempo-Presente-13-1_2022.pdf",
     "ARAUJO, Rafael; SALES, Jean Rodrigues. 'Atuação política das Forças Armadas e o "
     "fenômeno bolsonarista no Brasil (2013-2022)'. Cadernos do Tempo Presente, v. 13, n. 1, "
     "p. 26-42, 2022. DOI 10.33662/ctp.v13i01.17763",
     "PÁGINA IMPRESSA = PDF + 25, e o offset é DERIVADO, não lido: as páginas deste PDF não "
     "imprimem número algum. O que se lê, no cabeçalho corrente de toda página, é o "
     "intervalo do artigo — 'p. 26-42' — e o PDF tem exatamente 17 páginas, 42-26+1. A "
     "derivação é aritmética e verificável; não é leitura de rótulo",
     "PT-02, PT-04, PT-05 e PT-12 — a genealogia do apelo de intervenção militar depois de "
     "junho de 2013 (PDF p. 4), a assertividade da caserna (p. 5), a instrumentalização "
     "autoritária das manifestações (p. 6), motociatas, artigo 142 e 'kit Covid' (p. 8) e a "
     "superação parcial da atomização das direitas depois de 2013 (p. 11)"),
    ("FERNANDES-SILVA_Dinamicas-do-controle-a-acao-coletiva-policiamento_Mediacoes-26-3_2021.pdf",
     "FERNANDES, Eduardo Georjão; SILVA, Camila Farias da. 'Dinâmicas do controle à ação "
     "coletiva: o policiamento a protestos no Rio Grande do Sul'. Mediações, v. 26, n. 3, "
     "p. 485-502, 2021. DOI 10.5433/2176-6665.2021v26n3p485",
     "PÁGINA IMPRESSA = PDF + 484, e este offset É LIDO: a p. 1 do PDF imprime '485'",
     "PT-02 — e resolve o conflito, em vez de declará-lo. O que PT-02 chamava de 'tolerância "
     "policial' não se sustenta: as autoras documentam 'o uso prevalente de táticas de "
     "repressão física, pouco tolerantes' (PDF p. 8) e seletividade pelo grau de contestação "
     "à ordem (p. 10). DOIS LIMITES DECLARADOS: um só estado (RS) e série que termina em "
     "2015, de modo que a peça não cobre 2015-2016 inteiro nem 2018-2022"),
]:
    PROCEDENCIA["Fontes/13_Bolsonarismo-mobilizacao/" + _arq] = (
        _LIDAS25, "literatura", "{} | {} | SERVE A: {}".format(_ref, _desloc, _serve))

# (c) As QUATRO que a coleta automatizada não alcançou, entregues pelo pesquisador
# em 04/10/2026 depois que o encaminhamento 4 pediu os links. A entrega confirma o
# achado de acesso do documento 13: o bloqueio era do acesso automatizado, não da
# obra. COLETADAS, NÃO LIDAS — valem exatamente como as doze do bloco (a).
#
# E duas trazem CORREÇÃO DE ATRIBUIÇÃO, apurada ao abrir o arquivo. A lista que o
# projeto vinha carregando dizia 'Gohn 2020' e 'Farias e Casarões 2022'. Nenhuma
# das duas estava certa, e o padrão é o de sempre nesta pesquisa: o identificador
# certo no referente errado.
_ENTREGA25 = ("Entregue pelo pesquisador em 04/10/2026 (encaminhamento 4 da "
              "terceira rodada) — peça que a coleta automatizada da tarefa 25 não "
              "alcançou. COLETADA, NÃO LIDA: não ancora registro")
for _arq, _ref, _desloc, _serve in [
    ("GOHN_Ciclos-de-protestos-no-Brasil-1970-2019_Mundos-Plurales-6-1_2019.pdf",
     "GOHN, Maria da Glória. 'Ciclos de protestos no Brasil: 1970-2019'. mundosplurales — "
     "Revista Latinoamericana de Políticas y Acción Pública, FLACSO Sede Ecuador, v. 6, "
     "n. 1, p. 93-119, 2019. DOI 10.17141/mundosplurales.1.2019.3925",
     "PÁGINA IMPRESSA = PDF + 92, offset LIDO: a p. 1 do PDF imprime '93'. CORREÇÃO DE ANO: "
     "o projeto vinha listando esta peça como 'Gohn 2020'. É de 2019 — o próprio DOI traz "
     "'.1.2019.' e o rodapé registra 'Recibido: 3/4/2019 - Aceptado: 17/11/2019'",
     "PT-01 a PT-04, e também a tarefa 10 — é levantamento de cinco décadas de estudos "
     "brasileiros de protesto, com o quinto ciclo definido como 'pós junho de 2013'. É a "
     "única peça do corpus que faz o balanço da própria literatura brasileira"),
    ("VON-BULOW-ABERS_Denialism-and-populism-two-sides-of-a-coin_Government-and-Opposition-59_2024.pdf",
     "VON BÜLOW, Marisa; ABERS, Rebecca Neaera. 'Denialism and Populism: Two Sides of a Coin "
     "in Jair Bolsonaro’s Brazil'. Government and Opposition, v. 59, p. 998-1016, 2024. "
     "DOI 10.1017/gov.2022.14",
     "PÁGINA IMPRESSA = PDF + 997 (p. 998-1016 em 19 páginas de PDF). CORREÇÃO DE ANO, e é "
     "uma armadilha de citação: o slug do DOI é 'gov.2022.14' e a primeira publicação "
     "on-line é de 10/05/2022, mas o FASCÍCULO é de 2024, v. 59. O projeto vinha listando "
     "'von Bülow e Abers 2022'. O ano do DOI não é o ano de publicação",
     "PT-05 e PT-06 — é a peça que sustenta, com pesquisa, o que PT-06 afirma sem âncora: "
     "as autoras argumentam que o bolsonarismo precisa ser entendido como MOVIMENTO SOCIAL, "
     "não só como ideologia, e analisam o negacionismo pandêmico de março/2020 a "
     "outubro/2021 — exatamente o período de PT-06"),
    ("BASTOS-RECUERO_The-insurrectionist-playbook_Social-Media-and-Society-out-dez_2023.pdf",
     "BASTOS, Marco; RECUERO, Raquel. 'The Insurrectionist Playbook: Jair Bolsonaro and the "
     "National Congress of Brazil'. Social Media + Society, out.-dez. 2023, p. 1-16. "
     "DOI 10.1177/20563051231211881",
     "SEM OFFSET: a paginação impressa do artigo é 1-16 e o PDF tem 16 páginas. O fascículo "
     "não traz volume nem número impressos na peça — só 'October-December 2023' —, e por "
     "isso o nome do arquivo não os inventa",
     "PT-06 e T-1 operacional — trata o repertório insurrecional do 8 de janeiro nas redes, "
     "e é a peça mais próxima do objeto central desta pesquisa entre as dezoito"),
    ("FARIAS-CASAROES-MAGALHAES_Radical-right-populism-and-the-politics-of-cruelty_Global-Studies-Quarterly-2_2022.pdf",
     "FARIAS, Deborah Barros Leal; CASARÕES, Guilherme; MAGALHÃES, David. 'Radical Right "
     "Populism and the Politics of Cruelty: The Case of COVID-19 in Brazil Under President "
     "Bolsonaro'. Global Studies Quarterly, v. 2, p. 1-13, 2022. DOI 10.1093/isagsq/ksab048",
     "SEM OFFSET: 'Global Studies Quarterly (2022) 2, 1-13' e 13 páginas de PDF. CORREÇÃO DE "
     "AUTORIA: o projeto vinha listando 'Farias e Casarões'. São TRÊS autores — David "
     "Magalhães (PUC-SP e FAAP) faltava. ARMADILHA DE BUSCA JÁ CONHECIDA: o texto usa "
     "ligadura ﬁ ('deﬁned'), de modo que buscar 'defined' sem normalizar NFKC não acha",
     "PT-05 e PT-06 — crueldade como estratégia política sob populismo de direita radical, "
     "no caso da COVID-19. Toca o enquadramento de PT-06, não o ecossistema informacional"),
]:
    PROCEDENCIA["Fontes/13_Bolsonarismo-mobilizacao/" + _arq] = (
        _ENTREGA25, "literatura", "{} | {} | SERVE A: {}".format(_ref, _desloc, _serve))

# O que falta coletar. Alimenta a aba Pendencias_Coleta e o script baixar_fontes.sh.
PENDENCIAS = [
    ("Decisão de transferência para a Papuda (15/01/2026)", "PT-59",
     "STF", "AWS WAF (cookie aws-waf-token)", "Média", "Hoje apoiado em notícia do portal do STF."),
    ("Decisão da prisão preventiva (22-25/11/2025)", "PT-58",
     "STF — busca de jurisprudência", "AWS WAF (cookie aws-waf-token)",
     "Alta", "Único registro de T+1 sem ancoragem. É o de melhor retorno: fato recente e verificável."),
    ('Balanço "Democracia Inabalada" (29/04/2026)', "PT-53; PT-61",
     "Assessoria de imprensa do STF", "Não indexado como PDF",
     "Alta", "Os dois registros foram rebaixados a 'A verificar' em 16/08/2026 por falta desta peça."),
    ("Decisão de transferência para a Papuda (15/01/2026)", "PT-59",
     "STF", "AWS WAF (cookie aws-waf-token)", "Média", "Hoje apoiado em notícia do portal do STF."),
    ("Prisão domiciliar humanitária — Execução Penal 169", "PT-60",
     "STF", "AWS WAF (cookie aws-waf-token)", "Média", "Hoje apoiado em notícia do portal do STF."),
    ("Laudos periciais do Instituto de Criminalística/PF", "PT-38",
     "Polícia Federal", "Provável restrição de acesso",
     "Baixa", "O livro oficial do STF cobre o essencial; o laudo daria o detalhamento por peça."),
    ("Sentença de 1ª instância de Moro (12/07/2017), inteiro teor", "PT-03A",
     "JFPR / e-proc", "Consulta processual",
     "Baixa", "O dispositivo já está transcrito no acórdão do TRF-4, p. 395. Não bloqueia nada."),
    ("Arquivamento em PDF das matérias da Agência Brasil", "PT-03D; PT-38; PT-12",
     "agenciabrasil.ebc.com.br", "Nenhum",
     "Média", "Registros ancorados só em URL. Arquivar preserva a evidência contra link rot."),
    ("Decisão sobre o Manchetômetro (Doxa/IESP-UERJ)", "—",
     "—", "Decisão do pesquisador",
     "Média", "Arquivo no corpus sem registro que o cite: ou vira registro de cobertura midiática, ou fica declarado como contexto."),
]

FILL_CAB = PatternFill("solid", fgColor="1F3864")
FONT_CAB = Font(bold=True, color="FFFFFF", size=10)
BORDA = Border(*[Side(style="thin", color="BFBFBF")] * 4)


def escrever_aba(ws, cabecalhos, linhas, larguras, congelar="A2"):
    ws.append(cabecalhos)
    for c in range(1, len(cabecalhos) + 1):
        cel = ws.cell(row=1, column=c)
        cel.fill, cel.font = FILL_CAB, FONT_CAB
        cel.alignment = Alignment(vertical="center", horizontal="left", wrap_text=True)
    for linha in linhas:
        ws.append(linha)
    for r in range(2, ws.max_row + 1):
        for c in range(1, len(cabecalhos) + 1):
            cel = ws.cell(row=r, column=c)
            cel.alignment = Alignment(vertical="top", wrap_text=True)
            cel.border = BORDA
    for i, larg in enumerate(larguras, start=1):
        ws.column_dimensions[get_column_letter(i)].width = larg
    ws.row_dimensions[1].height = 30
    ws.freeze_panes = congelar
    ws.auto_filter.ref = "A1:{}{}".format(get_column_letter(len(cabecalhos)), ws.max_row)


def main():
    dados = json.loads(JSON_IN.read_text(encoding="utf-8"))
    eventos = dados["eventos"]
    campos = list(CABECALHOS.keys())

    # ---------------------------------------------------------------- CSV ----
    # utf-8-sig: o Excel pt-BR abre com acentuação correta sem assistente.
    with CSV_OUT.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh, quoting=csv.QUOTE_ALL, lineterminator="\n")
        w.writerow(CABECALHOS.values())
        for ev in eventos:
            w.writerow([ev.get(c) or "" for c in campos])
    print("CSV  : {} linhas x {} colunas".format(len(eventos), len(campos)))

    # --------------------------------------------------------------- XLSX ----
    wb = Workbook()

    ws = wb.active
    ws.title = "Codebook"
    escrever_aba(
        ws, list(CABECALHOS.values()),
        [[ev.get(c) or "" for c in campos] for ev in eventos],
        [9, 16, 17, 26, 34, 26, 32, 28, 40, 60, 34, 40, 22, 34, 20, 40],
        congelar="B2",
    )

    escrever_aba(
        wb.create_sheet("Dicionario"),
        ["Campo", "Definição", "Tipo", "Vocabulário admitido", "Origem do dado"],
        [list(d) for d in DICIONARIO],
        [20, 66, 16, 46, 30],
    )

    # Inventário: um arquivo por linha, com os registros que o citam.
    cita = defaultdict(list)
    for ev in eventos:
        for p in (ev.get("fonte_local") or "").split("; "):
            if p.strip():
                cita[p.strip()].append(ev["id"])

    try:
        from PyPDF2 import PdfReader
    except ImportError:
        PdfReader = None

    inventario = []
    for raiz, _, arquivos in os.walk(RAIZ / "Fontes"):
        for nome in sorted(arquivos):
            abs_p = Path(raiz) / nome
            rel = abs_p.relative_to(RAIZ).as_posix()
            if nome.upper().startswith("LEIA-ME"):
                continue
            paginas = ""
            if nome.lower().endswith(".pdf") and PdfReader:
                try:
                    paginas = len(PdfReader(str(abs_p)).pages)
                except Exception:
                    paginas = "erro"
            origem, tipo, obs = PROCEDENCIA.get(rel, ("—", "não declarado", ""))
            regs = cita.get(rel, [])
            inventario.append([
                rel, paginas, tipo, origem,
                ", ".join(regs) if regs else "— sem registro vinculado —",
                len(regs), obs,
            ])
    inventario.sort(key=lambda r: (-r[5], r[0]))
    escrever_aba(
        wb.create_sheet("Inventario_Fontes"),
        ["Arquivo", "Páginas", "Natureza", "Procedência", "Registros que citam", "Nº registros", "Observação"],
        inventario, [62, 10, 16, 44, 40, 12, 58],
    )

    escrever_aba(
        wb.create_sheet("Pendencias_Coleta"),
        ["Peça faltante", "Registro(s)", "Via", "Bloqueio", "Prioridade", "Observação"],
        [list(p) for p in PENDENCIAS], [48, 18, 30, 40, 12, 62],
    )

    wb.save(XLSX_OUT)
    print("XLSX : {} abas — {}".format(len(wb.sheetnames), ", ".join(wb.sheetnames)))
    print("       Inventario_Fontes: {} arquivos".format(len(inventario)))
    naodecl = [r[0] for r in inventario if r[2] == "não declarado"]
    if naodecl:
        print("       AVISO — procedência não declarada: {}".format(len(naodecl)))
        for n in naodecl:
            print("         ! " + n)
    # 'preprint' entra aqui porque literatura sobre a cobertura é objeto de
    # análise, não fonte de evento: não deve ancorar registro nenhum.
    orfaos = [r[0] for r in inventario
              if r[5] == 0 and r[2] not in ("bibliografia", "não citável", "preprint",
                                            "duplicata", "peça de divulgação",
                                            "catalogação", "arquivamento web")]
    print("       sem registro vinculado (fora bibliografia): {}".format(len(orfaos)))
    for o in orfaos:
        print("         - " + o)


if __name__ == "__main__":
    main()
