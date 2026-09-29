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
