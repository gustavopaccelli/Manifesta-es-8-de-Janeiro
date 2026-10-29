#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Verificação de integridade do aparato do process tracing.

Roda dez checagens e devolve código de saída != 0 se qualquer uma falhar.
Pensada para ser executada depois de toda alteração no codebook — é o que
garante que JSON, CSV e XLSX não voltem a divergir.

  1. Sincronia dos três formatos, célula a célula — e o esquema declarado em
     `metadados.colunas_codebook` conferido contra os cabeçalhos do gerador
  2. Integridade referencial: todo fonte_local existe em disco
  3. Cobertura do inventário: todo arquivo de Fontes/ está declarado
  4. Vocabulário controlado de status_classe e de autonomia_movimento
  5. Coerência entre fonte_pagina e fonte_local (documento citado x documento vinculado)
  6. Paginação real dos PDFs via PyPDF2 (nunca pdfinfo, que subconta)

Uso:  python scripts/verificar_integridade.py
"""

import csv
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))

from gerar_codebook import CABECALHOS, PROCEDENCIA  # noqa: E402

JSON_P = RAIZ / "process_tracing_8jan_eventos.json"
CSV_P = RAIZ / "data/processed/process_tracing_8jan_eventos.csv"
XLSX_P = RAIZ / "data/processed/process_tracing_8jan_codebook.xlsx"

# "Contextual" SAIU em 08/10/2026, por decisão do pesquisador: era isenção da
# cobrança de âncora, e com zero registros na classe o que a sua permanência
# garantia era apenas que um registro futuro pudesse nascer dispensado.
CLASSES = {"Confirmado em fonte primária", "Confirmado",
           "A verificar", "Inferência do analista"}

# `autonomia_movimento` entrou em 16/10/2026 como campo 17, por decisão do
# pesquisador (decisão 3 da tarefa 26(c), aberta no item 35.4). O VAZIO não
# está aqui de propósito: ele não é valor, é a declaração de que o registro
# ainda não foi lido sob esta pergunta -- 82 dos 83 hoje.
AUTONOMIA = {"Autonomia relativa", "Autonomia com encorajamento de cima",
             "Conduzido por patrocínio de setor organizado", "Não se aplica",
             "Lido, não documentado"}

# Eixos que NÃO entram na contagem de fonte documental. O eixo 05 está fora desde
# sempre: livro de método não é documento oficial. O eixo 12 entrou em 04/10/2026,
# pela tarefa 14, e é um caso novo — literatura revisada por pares que **ancora
# registro**, coisa que a teoria do eixo 05 nunca fez. A regra que a separação
# protege continua a mesma: a contagem documental mede documento oficial, e não
# pode crescer porque entrou artigo de revista.
FORA_DA_DOCUMENTAL = {"05_Bibliografia-teorica", "12_Camada-T-1_Literatura",
                      "13_Bolsonarismo-mobilizacao", "14_Livros-brasileiros",
                      "15_Comparado-6-de-janeiro"}

falhas = []
avisos = []


def cabecalho(n, titulo):
    print("\n" + "=" * 72)
    print("{}. {}".format(n, titulo))
    print("=" * 72)


def main():
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    eventos = dados["eventos"]
    campos = list(CABECALHOS.keys())

    # ------------------------------------------------------------------ 1 ---
    cabecalho(1, "SINCRONIA DOS TRÊS FORMATOS")
    with CSV_P.open(encoding="utf-8-sig", newline="") as fh:
        csv_rows = {r["ID"]: r for r in csv.DictReader(fh)}

    from openpyxl import load_workbook
    ws = load_workbook(XLSX_P, read_only=True)["Codebook"]
    it = ws.iter_rows(values_only=True)
    cab_x = list(next(it))
    xlsx_rows = {}
    for linha in it:
        if linha and linha[0]:
            xlsx_rows[linha[0]] = dict(zip(cab_x, linha))

    div = 0
    for ev in eventos:
        pid = ev["id"]
        for jk in campos:
            ck = CABECALHOS[jk]
            v_json = (ev.get(jk) or "").strip()
            v_csv = (csv_rows.get(pid, {}).get(ck) or "").strip()
            v_xls = str(xlsx_rows.get(pid, {}).get(ck) or "").strip()
            if not (v_json == v_csv == v_xls):
                div += 1
                if div <= 5:
                    print("  DIVERGÊNCIA {}.{}".format(pid, jk))
                    print("    JSON: {!r}".format(v_json[:80]))
                    print("    CSV : {!r}".format(v_csv[:80]))
                    print("    XLSX: {!r}".format(v_xls[:80]))
    print("  registros: JSON {} | CSV {} | XLSX {}".format(
        len(eventos), len(csv_rows), len(xlsx_rows)))
    print("  células divergentes: {}".format(div))
    if div or not (len(eventos) == len(csv_rows) == len(xlsx_rows)):
        falhas.append("sincronia entre formatos ({} células)".format(div))
    else:
        print("  OK — os três formatos são idênticos nos {} x {}".format(
            len(eventos), len(campos)))

    # O esquema que os metadados DECLARAM é o que o gerador usa? A pergunta
    # existe porque `colunas_codebook` foi escrito pela migração de 16/08 e
    # ninguém o conferia desde então: declaração de esquema que nenhuma
    # checagem lê é da mesma família do `sha1` que declarava identidade já
    # desfeita (item 48). Entrou em 16/10/2026, com o campo 17.
    declarado = dados["metadados"].get("colunas_codebook") or []
    if list(declarado) != campos:
        print("  ! metadados.colunas_codebook divergem dos cabeçalhos do gerador")
        print("    declarado: {}".format(declarado))
        print("    gerador  : {}".format(campos))
        falhas.append("colunas_codebook x CABECALHOS")
    else:
        print("  OK — metadados.colunas_codebook declara os mesmos {} campos".format(
            len(campos)))

    # ------------------------------------------------------------------ 2 ---
    cabecalho(2, "INTEGRIDADE REFERENCIAL DOS CAMINHOS")
    quebrados = []
    com_local = 0
    for ev in eventos:
        local = (ev.get("fonte_local") or "").strip()
        if not local:
            continue
        com_local += 1
        for p in [x.strip() for x in local.split(";") if x.strip()]:
            if not (RAIZ / p).exists():
                quebrados.append((ev["id"], p))
    print("  registros com fonte_local: {}/{}".format(com_local, len(eventos)))
    print("  referências quebradas    : {}".format(len(quebrados)))
    for i, p in quebrados:
        print("    ! {} -> {}".format(i, p))
    if quebrados:
        falhas.append("{} referência(s) quebrada(s)".format(len(quebrados)))
    else:
        print("  OK — todo caminho declarado existe em disco")

    # ------------------------------------------------------------------ 3 ---
    cabecalho(3, "COBERTURA DO INVENTÁRIO")
    citados = set()
    for ev in eventos:
        for p in (ev.get("fonte_local") or "").split(";"):
            if p.strip():
                citados.add(p.strip())
    naodecl = []
    for arq in sorted((RAIZ / "Fontes").rglob("*")):
        if arq.is_dir() or arq.name.upper().startswith("LEIA-ME"):
            continue
        rel = arq.relative_to(RAIZ).as_posix()
        if rel not in citados and rel not in PROCEDENCIA:
            naodecl.append(rel)
    print("  arquivos citados por registro : {}".format(len(citados)))
    print("  arquivos sem declaração       : {}".format(len(naodecl)))
    for n in naodecl:
        print("    ! " + n)
    if naodecl:
        falhas.append("{} arquivo(s) sem procedência declarada".format(len(naodecl)))
    else:
        print("  OK — todo arquivo ou ancora um registro ou tem procedência declarada")

    # ------------------------------------------------------------------ 4 ---
    cabecalho(4, "VOCABULÁRIO CONTROLADO — status_classe e autonomia_movimento")
    from collections import Counter
    cont = Counter(ev.get("status_classe") for ev in eventos)
    fora = [k for k in cont if k not in CLASSES]
    for k, v in cont.most_common():
        print("  {:3d}  {}".format(v, k))
    if fora:
        print("  ! valores fora do vocabulário: {}".format(fora))
        falhas.append("status_classe fora do vocabulário: {}".format(fora))
    else:
        print("  OK — só os {} valores previstos".format(len(CLASSES)))

    # autonomia_movimento, desde 16/10/2026 (campo 17, decisão 3 da tarefa
    # 26(c)). Duas guardas e uma contagem:
    #   - valor fora do vocabulário derruba, como em status_classe;
    #   - valor que AFIRMA autonomia ou condução exige `fonte_pagina`, porque
    #     a pergunta que este campo responde é a central da pesquisa e
    #     codificação sem folha é exatamente a âncora-que-parece-âncora;
    #     só "Não se aplica" fica de fora da cobrança -- negar pertinência
    #     não precisa de folha, e cobrá-la seria ruído. "Lido, não
    #     documentado", que entrou em 16/10/2026, PRECISA: dizer que se leu
    #     e a fonte não documenta é afirmação sobre uma folha determinada,
    #     e sem folha citada a afirmação não tem objeto;
    #   - o vazio é CONTADO e impresso, nunca somado aos valores: vazio é
    #     "ninguém leu ainda sob esta pergunta", e zero suposto é silêncio.
    print("")
    cont_a = Counter(ev.get("autonomia_movimento") for ev in eventos)
    fora_a = [k for k in cont_a if k and k not in AUTONOMIA]
    sem_folha = [ev["id"] for ev in eventos
                 if (ev.get("autonomia_movimento") or "") not in ("", "Não se aplica")
                 and not (ev.get("fonte_pagina") or "").strip()]
    for k, v in cont_a.most_common():
        print("  {:3d}  autonomia_movimento: {}".format(v, k or "(vazio) — NÃO CODIFICADO"))
    if fora_a:
        print("  ! valores fora do vocabulário: {}".format(fora_a))
        falhas.append("autonomia_movimento fora do vocabulário: {}".format(fora_a))
    if sem_folha:
        print("  ! codificado sem fonte_pagina: {}".format(sem_folha))
        falhas.append("autonomia_movimento sem folha: {}".format(sem_folha))
    if not fora_a and not sem_folha:
        print("  OK — vocabulário respeitado e todo valor afirmativo tem folha")

    # ------------------------------------------------------------------ 5 ---
    cabecalho(5, "COERÊNCIA fonte_pagina x fonte_local")
    from gerar_codebook import RAIZ as _R  # noqa: F401
    reg_docs = dados["metadados"].get("registro_documentos", {})
    path_to_cod = {v: k for k, v in reg_docs.items()}
    incoerentes = []
    for ev in eventos:
        pag = (ev.get("fonte_pagina") or "").strip()
        local = (ev.get("fonte_local") or "").strip()
        if not pag:
            continue
        cods_pag = {m.strip() for m in re.findall(r"(?:^|\|)\s*([^:|]+):", pag)}
        cods_loc = {path_to_cod[p.strip()] for p in local.split(";")
                    if p.strip() in path_to_cod}
        if not cods_pag <= cods_loc:
            incoerentes.append((ev["id"], sorted(cods_pag - cods_loc), sorted(cods_loc)))
    print("  registros com fonte_pagina: {}".format(
        sum(1 for e in eventos if (e.get("fonte_pagina") or "").strip())))
    print("  incoerências              : {}".format(len(incoerentes)))
    for i, falta, tem in incoerentes:
        print("    ! {} cita {} mas só vincula {}".format(i, falta, tem))
    if incoerentes:
        falhas.append("{} incoerência(s) página x documento".format(len(incoerentes)))
    else:
        print("  OK — toda página citada pertence a um documento vinculado")

    # A PERGUNTA INVERSA, acrescentada em 15/10/2026 (item 51). O laço acima
    # começa com `if not pag: continue` — ele confere quem cita página, e quem
    # não cita passava. Foi assim que PT-03B, PT-05A, PT-06C e PT-57 ficaram
    # dois meses vinculando PDF do corpus sem apontar folha, com transcrição de
    # imprensa no lugar da transcrição da fonte. Registro que vincula PDF tem de
    # citar página: é o que separa âncora de referência.
    sem_folha = []
    for ev in eventos:
        if (ev.get("fonte_pagina") or "").strip():
            continue
        pdfs = [p.strip() for p in (ev.get("fonte_local") or "").split(";")
                if p.strip().lower().endswith(".pdf")]
        if any((_R / p).exists() for p in pdfs):
            sem_folha.append(ev["id"])
    print("  PDF vinculado sem página citada: {}".format(len(sem_folha) or "nenhum"))
    if sem_folha:
        for i in sem_folha:
            print("    ! {} vincula PDF do corpus e não aponta folha".format(i))
        falhas.append("{} registro(s) com PDF vinculado e sem página".format(
            len(sem_folha)))

    # LOCALIZADOR ESTRUTURAL RESOLVIDO — acrescentado em 16/10/2026 (item 62),
    # ao resolver a guarda de PT-19A. Fonte nao paginada se cita por estrutura
    # interna, e isso nao e desenho novo: a rota do acordao do TSE declara em
    # PROCEDENCIA, desde 15/10, "citar por estrutura interna (item da ementa,
    # dispositivo), nao por pagina", e PT-03E pratica desde entao.
    #
    # O QUE FALTAVA ERA A RESOLUCAO. `conferir_paginas.py` abre PDF, de modo que
    # um titulo de secao citado com nome errado -- ou uma secao renomeada no
    # arquivo depois da citacao -- passaria para sempre. A folha de um PDF e
    # conferida contra o texto; a secao nao era conferida contra nada. Aqui ela
    # e: todo `§Titulo` em `fonte_pagina` tem de existir como CABECALHO em algum
    # dos arquivos nao-PDF vinculados ao registro.
    #
    # So o `§` entra. O localizador de PT-03E ("ementa itens 2-4 e 12;
    # dispositivo") fica de fora de proposito: "itens" nao sao cabecalhos, e
    # guarda que reprova registro legitimo treina a ignorar guarda.
    SECAO = re.compile(r"§\s*([^;,|()]+)")
    nao_resolvidos = []
    com_secao = 0
    for ev in eventos:
        titulos = [t.strip() for t in SECAO.findall(ev.get("fonte_pagina") or "")]
        if not titulos:
            continue
        com_secao += 1
        textos = []
        for p in (ev.get("fonte_local") or "").split(";"):
            p = p.strip()
            if p and not p.lower().endswith(".pdf") and (RAIZ / p).exists():
                textos.append((RAIZ / p).read_text(encoding="utf-8"))
        for t in titulos:
            md = r"(^|\n)[ \t]*#{1,6}[ \t]*" + re.escape(t) + r"[ \t]*(\n|$)"
            ht = r"<h[1-6][^>]*>\s*" + re.escape(t) + r"\s*</h[1-6]>"
            if not any(re.search(md, x) or re.search(ht, x, re.I) for x in textos):
                nao_resolvidos.append((ev["id"], t))
    print("  registros com localizador estrutural (§): {}".format(com_secao))
    for i, t in nao_resolvidos:
        print("    ! {} cita §{} e esse cabeçalho não existe no arquivo vinculado"
              .format(i, t))
    if nao_resolvidos:
        falhas.append("{} localizador(es) estrutural(is) não resolvido(s)".format(
            len(nao_resolvidos)))
    elif com_secao:
        print("  OK — todo §seção citado existe como cabeçalho na fonte vinculada")

    # ------------------------------------------------------------------ 6 ---
    cabecalho(6, "PAGINAÇÃO REAL DOS PDFs (PyPDF2)")
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        avisos.append("PyPDF2 ausente — paginação não conferida")
        print("  ! PyPDF2 não instalado")
    else:
        total = n = 0
        doc_total = doc_n = 0          # só fonte documental: fora do eixo 05
        for arq in sorted((RAIZ / "Fontes").rglob("*.pdf")):
            try:
                p = len(PdfReader(str(arq)).pages)
                total += p
                n += 1
                if arq.parent.name not in FORA_DA_DOCUMENTAL:
                    doc_total += p
                    doc_n += 1
            except Exception as exc:
                falhas.append("PDF ilegível: {}".format(arq.name))
                print("    ! {}: {}".format(arq.name, str(exc)[:60]))
        print("  {} PDFs, {} páginas no total — dos quais {} PDFs / {} p. são fonte documental"
              .format(n, total, doc_n, doc_total))
        # Linha de base: 30/09/2026, quando a Wiley-Blackwell Encyclopedia entrou no
        # eixo 05, somando-se ao cânone de 29/09 (Dynamics of Contention e O poder em
        # movimento). Atualize junto com o inventário sempre que uma peça entrar.
        #
        # As DUAS contagens existem porque a de cima conflaciona. O dossiê de
        # candidatura dizia "22 documentos oficiais que somam 6.928 páginas", e dois
        # daqueles 22 eram livros de método do eixo 05. Documento oficial é o que
        # ancora registro; livro de teoria não ancora nenhum. **A documental não muda
        # quando entra teoria** — é o que esta separação garante.
        # Linha de base atualizada em 04/10/2026, em TRÊS passos do mesmo dia: entram
        # Kunrath Silva (2018 e 2023) e Alonso (2023) no eixo 12; as 14 peças da
        # coleta da tarefa 25 no eixo 13; e, na terceira rodada, as 4 peças que a
        # coleta automatizada não alcançara (Gohn 2019, von Bülow e Abers 2024,
        # Bastos e Recuero 2023, Farias, Casarões e Magalhães 2022), entregues pelo
        # pesquisador. A documental continua em 22 / 6.951, e é exatamente o que a
        # separação serve para mostrar: o corpus cresceu 816 páginas sem que um
        # único documento oficial entrasse.
        # Linha de base atualizada em 08/10/2026 pela tarefa 10: entra o eixo 14,
        # com sete peças de literatura brasileira em livro — o volume Giros à
        # direita (SertãoCult, 2020, seis capítulos — retirados no terceiro passo,
        # ver abaixo) e O Brasil no inferno global
        # (FFLCH/USP, 2022). A documental continua em 22 / 6.951: é a quarta vez
        # que o corpus cresce sem que um único documento oficial entre.
        # Linha de base atualizada em 08/10/2026, SEGUNDO passo do mesmo dia: o
        # pesquisador entregou cinco peças que a coleta não alcançara (três livros
        # do SciELO Livros e os dois artigos comparados sobre o 6 de janeiro) e
        # mandou coletar dois capítulos a mais de Giros à direita. O eixo 14 vai a
        # 12 peças e nasce o eixo 15. A documental continua em 22 / 6.951: quinta
        # vez que o corpus cresce sem que um documento oficial entre.
        # Linha de base atualizada em 08/10/2026, TERCEIRO passo do mesmo dia, e é a
        # PRIMEIRA VEZ QUE O CORPUS DIMINUI DE ARQUIVOS E ISSO É GANHO: os oito
        # offprints de Giros à direita saíram e entrou o volume inteiro, com onze
        # capítulos, offset zero e SHA-256 conferido contra a cópia que eu mesmo
        # baixei do IBICT. São 8 arquivos a menos e 1 a mais — 59 PDFs —, 22 páginas
        # a menos no total, e TRÊS capítulos a mais de conteúdo (Torres, Costa Filho
        # e Marques), que o corpus não tinha. A documental continua em 22 / 6.951.
        # Linha de base atualizada em 08/10/2026, QUARTO passo: entram as três peças
        # da camada A que estavam lidas só on-line (Collier 2011, Mayntz 2004 e
        # González-Bailón et al. 2011), por decisão do pesquisador. Com elas, as 7
        # peças lidas da camada A passam a ter arquivo — e `lida` deixa de divergir
        # de `lida-e-arquivada`. A documental continua em 22 / 6.951.
        # Linha de base atualizada em 20/10/2026, e e a PRIMEIRA VEZ QUE A
        # DOCUMENTAL SE MOVE desde 29/09: entra o eixo 16, criado por
        # encaminhamento do pesquisador para os dois antecedentes do impeachment,
        # com o documento `Uma Ponte para o Futuro` (19 folhas). As seis
        # atualizacoes anteriores desta linha diziam, uma a uma, que a documental
        # NAO mudava quando entrava literatura -- e e isso que a separacao serve
        # para mostrar. Agora ela muda, porque entrou documento que ancora
        # registro: 22 -> 23 PDFs documentais, 6.951 -> 6.970 paginas.
        # 21/10/2026: entra BEACH-PEDERSEN, 'Process-Tracing Methods' (Michigan,
        # 2013), 208 folhas, fornecida pelo pesquisador. 64 -> 65 PDFs e 12.144 ->
        # 12.352 paginas; a DOCUMENTAL nao se move, porque e literatura, e e isso
        # que a separacao desta linha serve para mostrar. Licenca lida no arquivo:
        # RESERVADA -- nao redistribuivel, e por isso o manifesto existe.
        if (n, total, doc_n, doc_total) != (65, 12352, 23, 6970):
            avisos.append("corpus mudou: {} PDFs / {} páginas, {} documentais / {} p. "
                          "(era 65 / 12352, 23 / 6970)".format(n, total, doc_n, doc_total))
            print("  ~ corpus difere da linha de base de 21/10/2026 (65 PDFs / 12352 p., "
                  "23 documentais / 6970 p.)")
        else:
            print("  OK — bate com o inventário")

    # ------------------------------------------------------------------ 7 ---
    # Checagem criada em 10/10/2026, e a prova negativa que a motivou vale ser
    # lida: ao renomear os quatro mecanismos da tarefa 19, reinjetei o nome VELHO
    # numa figura e no relatório e rodei `conferir_figuras` e `conferir_relatorio`.
    # **Zero de duas pegaram.** O ciclo não compara o texto do mecanismo entre o
    # JSON e os artefatos mantidos à mão, de modo que uma renomeação podia deixar
    # nome morto em qualquer um deles sem um aviso. Não se tenta diferenciar prosa
    # livre: basta exigir que NENHUM nome retirado reapareça.
    cabecalho(7, "NOMES E ATRIBUIÇÕES RETIRADOS NÃO REAPARECEM")
    # 14/10/2026: saiu `projeto-pos-doc/figuras/cronologia-interativa.html`, e a
    # razao e o que a reorganizacao achou. Aquela pasta guardava COPIAS que a
    # LEIA-ME do dossie declarava "byte-identicas" aos artefatos da raiz, com
    # sha1 registrado -- e nao eram: o SVG ainda casava com o sha1 DECLARADO e o
    # original ja tinha mudado (seis semanas de atraso), e no HTML nenhum dos
    # dois casava com o sha1 declarado, porque os dois andaram por conta propria.
    # Identidade declarada que ninguem conferia e duplicata, nao redundancia:
    # `conferir_figuras.py` so olha reports/figures/, e por isso nada avisou. As
    # copias sairam e os documentos do edital passaram a apontar para a raiz.
    # 18/10/2026: ENTRA O SVG, e a lacuna estava na propria contagem da checagem.
    # O item 42.3 dizia que quatro artefatos sao mantidos a mao -- "as duas
    # figuras interativas, o relatorio de pesquisa e o caderno de evidencias" --
    # e esta lista tinha TRES: o SVG da cadeia causal nunca entrou. Ele carrega
    # texto de mecanismo (`>mecanismo: ... + alinhamento de quadros previo`) e
    # `conferir_figuras.py` nao compara esse texto com o JSON, de modo que um
    # nome retirado podia viver ali indefinidamente. Medido em 18/10 antes de
    # acrescentar: o SVG nao continha nenhum dos nomes ja retirados -- a lacuna
    # existia e ainda nao havia mordido.
    ARTEFATOS = [
        "reports/figures/cronologia_8jan_interativa.html",
        "reports/figures/figura_cronologia_8jan.svg",
        "reports/process_tracing_8jan_relatorio.md",
        "Caderno-de-evidencias/caderno_CPMI_verbatim.md",
    ]
    # nome retirado -> (data, registro, nome que passou a valer)
    RETIRADOS = {
        "Transposição do limiar": ("10/10/2026", "PT-29", "Demonstração de viabilidade"),
        "Massa crítica atingida": ("10/10/2026", "PT-34",
                                   "Concentração simultânea no conjunto simbólico"),
        "rede distribuída com nós centralizadores":
            ("10/10/2026", "PT-12A", "Agregação na base e intermediação concentrada"),
        # DUAS ENTRADAS PARA PT-62, e a segunda nasceu da primeira. Em
        # 27/10/2026 (item 96) o pesquisador adotou o nome da tipologia, e o
        # nome que ESTA entrada apontava como vigente desde 10/10 passou a ser
        # ele proprio um nome retirado. **Entrada de registro de nome morto
        # tambem envelhece**: ela aponta para o que vale hoje, e se o que vale
        # hoje sair sem que ela mude, a guarda passa a ensinar nome morto.
        "Desarticulação do repertório de rua":
            ("10/10/2026", "PT-62",
             "Desmobilização heterônoma por custo penal"),
        "Desmobilização por repressão seletiva":
            ("27/10/2026", "PT-62",
             "Desmobilização heterônoma por custo penal"),
        "Certificação de eficácia": ("04/10/2026", "PT-03", "Ressignificação do protesto"),
        # Nao e nome de mecanismo, e a vigilancia e a mesma: atribuicao retirada.
        # Os quatro testes sao de Van Evera (1997), na formulacao de Bennett
        # (2010) e na apresentacao de Collier (2011) -- corrigido em 10/10/2026
        # pela quinta cobranca da tarefa 19, em seis lugares.
        "testes de Beach e Pedersen": ("10/10/2026", "os quatro testes",
                                       "Van Evera 1997 / Bennett 2010 / Collier 2011"),
        "testes de Beach & Pedersen": ("10/10/2026", "os quatro testes",
                                       "Van Evera 1997 / Bennett 2010 / Collier 2011"),
        # 18/10/2026, decisao 1 do item 47.5: o nome de PT-07. TRES variantes,
        # porque os artefatos a mao o escreviam de tres formas -- o SVG em
        # minuscula dentro de uma cadeia, o HTML capitalizado, e o relatorio com
        # o termo ingles no meio. Guarda de substring exige a forma exata, e uma
        # so entrada teria deixado duas passar.
        "Alinhamento de quadros prévio": ("18/10/2026", "PT-07",
                                          "Deliberação de ruptura e articulação "
                                          "do quadro de fraude"),
        "Alinhamento de quadros (frame alignment) prévio":
            ("18/10/2026", "PT-07",
             "Deliberação de ruptura e articulação do quadro de fraude"),
        # 18/10/2026, decisao 2 do item 57.4: o valor de autonomia de PT-10A.
        # Nao e nome de mecanismo, e a vigilancia e a mesma -- valor de
        # vocabulario retirado.
        "Conduzido de cima": ("18/10/2026", "PT-10A (autonomia_movimento)",
                              "Conduzido por patrocínio de setor organizado"),
        # 18/10/2026, frente F5 (item 66): PT-21. E AQUI A ENTRADA NAO E O NOME,
        # E O CONCEITO -- e essa e a licao da rodada.
        #
        # A tarefa 19 retirou "massa critica" de PT-34 em 10/10 e registrou aqui
        # a STRING retirada ("Massa critica atingida no ponto de maxima densidade
        # simbolica"). O conceito continuou vivo em PT-21, que afirmava "a massa
        # critica NECESSARIA para romper barreiras", e em CINCO ocorrencias em
        # tres dos quatro artefatos -- nenhuma acusada, porque a guarda vigiava a
        # frase de um registro e nao o termo. **Nome retirado de um registro nao
        # retira o conceito do codebook.** Com estas duas entradas, retira.
        #
        # Medido em 18/10, depois da limpeza: zero ocorrencias nos quatro
        # artefatos. Discussao legitima do conceito -- o verbete de Oliver, por
        # exemplo -- vive em docs/analise/, que nao e artefato vigiado.
        "massa crítica": ("18/10/2026", "PT-21 e PT-34",
                          "o que a folha mede: 300 → 5.500 pessoas"),
        "Concentração de recursos": ("18/10/2026", "PT-21",
                                     "Concentração de contingente no acampamento"),
        # 21/10/2026, frente F10 (item 70): as TRES formulacoes que a tabela-
        # espelho achou vivas nas figuras. Nao eram "nomes retirados" no sentido
        # do registro acima -- eram REFORMULACOES de campo, de 04/10/2026, e e
        # por isso que nunca entraram aqui e a figura envelheceu dezessete dias
        # em silencio. **Esta e a licao da rodada: reformulacao de campo tambem
        # retira enunciado, e enunciado retirado tambem volta.**
        "Abertura de estrutura de oportunidade": (
            "04/10/2026", "PT-01",
            "Janela de oportunidades políticas aberta no ciclo de 2013"),
        # LIMITE DECLARADO, e e de recorte: o termo NU -- spin-off -- fica livre,
        # porque o codebook o usa em NEGACAO ("nao e ciclo novo nem spin-off") e
        # o relatorio o discute. O que se vigia e a glosa entre parenteses, que
        # so aparece quando o termo e usado como NOME de mecanismo. Guarda que
        # disparasse na negacao treinaria a ignorar a guarda.
        "(spin-off)": ("04/10/2026", "PT-02",
                       "Apropriação parcial do repertório de protesto por "
                       "contramovimentos conservadores"),
        # TRES strings para a mesma retificacao, e cada uma foi medida num lugar
        # diferente: a figura dizia "ecossistema informacional paralelo", a
        # cadeia ASCII do relatorio dizia "ecossistema digital paralelo", e o
        # campo de mecanismo do relatorio dizia "infraestrutura comunicacional
        # autonoma". Uma entrada so teria deixado duas passar -- a mesma forma
        # da licao das tres variantes de PT-07.
        "ecossistema informacional paralelo": (
            "04/10/2026", "PT-06",
            "Mobilização permanente da base por circulação de enquadramentos "
            "negacionistas"),
        "ecossistema digital paralelo": (
            "04/10/2026", "PT-06",
            "Mobilização permanente da base por circulação de enquadramentos "
            "negacionistas"),
        "infraestrutura comunicacional autônoma": (
            "04/10/2026", "PT-06",
            "Mobilização permanente da base por circulação de enquadramentos "
            "negacionistas"),
    }
    achou_morto = 0
    for rel in ARTEFATOS:
        cam = RAIZ / rel
        if not cam.exists():
            avisos.append("artefato ausente na checagem 7: {}".format(rel))
            continue
        # CAIXA IGNORADA desde 21/10/2026, frente F10 — e a medição que motivou
        # a mudança achou DOIS USOS VIVOS de nome retirado que esta guarda havia
        # deixado passar por onze dias:
        #   `certificação de eficácia` (minúscula) no mecanismo do bloco
        #      2013–2016 do relatório e no elo da cadeia ASCII, enquanto a
        #      entrada vigiada era `Certificação de eficácia`;
        #   `Rede distribuída com nós centralizadores` (maiúscula) na linha de
        #      PT-12A da tabela de síntese, enquanto a entrada era minúscula.
        # A lição de 18/10 — três variantes para o nome de PT-07, porque a
        # guarda casa substring exata — foi escrita e NÃO foi retroaplicada às
        # cinco entradas anteriores. Ignorar a caixa resolve a classe inteira e
        # dispensa a lista de variantes: as duas entradas que existiam só por
        # diferença de caixa saíram na mesma rodada.
        #
        # O PREÇO, e ele foi pago no texto, não na guarda: a comparação não
        # distingue MENÇÃO de USO, então os artefatos deixaram de GRAFAR o nome
        # morto ao narrar a troca — passaram a nomear a afirmação que saiu ("em
        # substituição ao nome anterior, que era o do modelo de limiar"). É o
        # padrão que a própria guarda impôs em 18/10, quando reprovou um texto
        # novo que escrevia o nome morto para dizer que ele saíra. O registro do
        # nome antigo vive em `metadados.revisoes` e em `docs/analise/`, que não
        # são artefatos vigiados.
        txt = cam.read_text(encoding="utf-8").lower()
        for morto, (quando, pid, vivo) in RETIRADOS.items():
            if morto.lower() in txt:
                achou_morto += 1
                falhas.append("nome retirado em {}: '{}' ({}, {} -> {})"
                              .format(rel, morto, pid, quando, vivo))
                print("    X {} traz '{}' — retirado em {} de {}, hoje é '{}'"
                      .format(rel, morto, quando, pid, vivo))
    print("  {} nome(s)/atribuição(ões) retirado(s) vigiado(s) em {} artefato(s) à mão"
          .format(len(RETIRADOS), len(ARTEFATOS)))
    if not achou_morto:
        print("  OK — nenhum nome retirado reapareceu")

    # O MESMO VIGIA, APONTADO PARA DENTRO — acrescentado em 13/10/2026, tarefa 17.
    # A vigilancia acima olha quatro artefatos A MAO e nao olhava o proprio JSON,
    # por ele ser a fonte de verdade. E a nota metodologica do JSON continuava
    # ENSINANDO 'Contextual' como valor vigente cinco dias depois de a classe sair
    # do vocabulario — e omitindo 'Confirmado em fonte primaria', que existe. Fonte
    # de verdade nao e sinonimo de coerente consigo mesma.
    #
    # A regra e de DUAS VIAS, e por isso nao depende de manter lista de nome morto:
    # toda classe do vocabulario tem de ser citada na nota, e a nota nao pode citar
    # classe que nao esta no vocabulario. Escopo deliberadamente estreito: so
    # `aviso_metodologico`. As ocorrencias de 'Contextual' em `revisoes` e nos campos
    # de prosa dos registros sao narracao DATADA de recodificacao e tem de ficar —
    # guarda que dispara em narracao historica e ruido, e ruido treina a ignorar guarda.
    # UMA SEMANTICA SO, e a primeira versao desta guarda tinha duas: a via de ida
    # testava substring ("a classe e mencionada?") e a de volta testava aspa ("a
    # classe e ENSINADA como vigente?"). A prova negativa pegou a incoerencia --
    # tirar as aspas de uma classe vigente nao disparava nada, porque o nome
    # continuava no texto. Aqui as duas vias leem a MESMA marca: aspa simples no
    # aviso significa valor vigente. Mencao historica, sem aspas, fica livre -- e e
    # assim que a nota pode contar que Contextual saiu sem a guarda disparar.
    import re as _re0
    aviso = str(dados["metadados"].get("aviso_metodologico") or "")
    # CHAVE COM `_` E METADADO SOBRE O VOCABULARIO, nao valor do campo.
    # `vocabulario_status_classe` passou de lista para dicionario com
    # definicoes em 25/10/2026 (item 83), porque o critério de
    # `Confirmado em fonte primaria` vivia em prosa dentro de PT-01A e
    # nunca tinha sido escrito aqui. `set(dict)` devolve as chaves, o que
    # serve -- menos para `_nota`, que explica a mudanca. O prefixo `_` ja
    # e a convencao da casa para metadado-sobre-metadado, e a guarda a
    # respeita em vez de exigir que a nota metodologica "cite a classe
    # vigente `_nota`".
    vocab = {c for c in (dados["metadados"].get(
        "vocabulario_status_classe") or []) if not c.startswith("_")}
    citadas = set(_re0.findall(r"'([^']{4,40})'", aviso))
    nao_citadas = sorted(c for c in vocab if c not in citadas)
    # Nome de classe conhecido, entre aspas, e fora do vocabulario: o residuo de
    # 13/10 era exatamente este — Contextual ensinada como valor vigente.
    CONHECIDAS = CLASSES | {"Contextual"}
    intrusas = sorted(c for c in citadas if c in CONHECIDAS and c not in vocab)
    for c in nao_citadas:
        falhas.append("aviso_metodologico não cita a classe vigente: {}".format(c))
        print("    X aviso_metodologico nao cita a classe vigente '{}'".format(c))
    for c in intrusas:
        falhas.append("aviso_metodologico cita classe fora do vocabulário: {}".format(c))
        print("    X aviso_metodologico cita '{}', que nao esta no vocabulario"
              .format(c))
    if not nao_citadas and not intrusas:
        print("  OK — a nota metodológica e o vocabulário controlado dizem o mesmo "
              "({} classes)".format(len(vocab)))

    # Remissao entre registros: quando um campo diz "ver PT-52", esse registro tem
    # de existir. Guarda criada em 10/10/2026, quando PT-62 passou a REMETER a
    # PT-49, PT-52, PT-53 e PT-61 em vez de reafirmar o que eles provam. O projeto
    # ja inseriu identificadores com sufixo em revisao posterior (PT-03A a PT-06C),
    # de modo que remissao quebrada e risco real, e hoje nada a acusava.
    import re as _re
    import sys as _sys6
    _sys6.path.insert(0, str(RAIZ / "scripts"))
    from conferir_paginas import (CAMPOS_DE_PROSA as _PROSA6,
                                  CAMPO_BASE as _BASE6,
                                  confere_esquema as _esq6)
    # O ASSERT DO ESQUEMA RODA AQUI, no primeiro passo que importa a
    # classificacao. Se o codebook ganhar campo, ele derruba o ciclo no
    # passo 9 e exige a classificacao -- de modo que a guarda seguinte
    # nao pode nascer cega. **Funcao de guarda que ninguem chama nao e
    # guarda**, e esta casa ja pagou por isso uma vez, quando um
    # backspace de controle deixou o regex desta mesma checagem inerte.
    for _ev6 in eventos:
        _esq6(_ev6)
    ids = {ev["id"] for ev in eventos}
    pendura = 0
    for ev in eventos:
        # A LISTA DE CAMPOS DESTA CHECAGEM DEIXOU DE EXISTIR EM
        # 29/10/2026 (item 106), e e o conserto do padrao que a mordeu.
        # Em 28/10 ela lia tres campos e nao `status_verificacao`, que
        # tinha 33 remissoes; em 29/10 a varredura achou que ela tambem
        # nao lia `target_alvo` nem `resposta_estatal`, com 4 remissoes
        # e zero quebradas. **Em vez de acrescentar os dois, a lista
        # saiu:** ela passou a ser a classificacao derivada de
        # `conferir_paginas`, que o `assert` do esquema protege. Se o
        # codebook ganhar campo de prosa, esta checagem o le sozinha.
        #
        # Remissao pode morar em QUALQUER prosa, inclusive na
        # transcrita, e por isso o campo base entra aqui -- diferente
        # da guarda das meias-ancoras, onde ele e a contencao.
        for campo in _PROSA6 + (_BASE6,):
            # Fronteira de palavra dos dois lados. ATENCAO: esta linha ja foi
            # escrita uma vez por heredoc, que converteu a sequencia barra-b em
            # BACKSPACE de controle (\x08). O regex ficou inerte e a checagem
            # imprimia OK testando zero strings. Se editar isto, nao use heredoc.
            for ref in set(_re.findall(r"\bPT-\d{2}[A-Z]?\b",
                                       str(ev.get(campo) or ""))):
                if ref not in ids:
                    pendura += 1
                    falhas.append("remissão quebrada: {} cita {} em {}, e {} não existe"
                                  .format(ev["id"], ref, campo, ref))
                    print("    X {} cita {} em {} — e {} nao existe"
                          .format(ev["id"], ref, campo, ref))
    if not pendura:
        print("  OK — toda remissão PT-XX entre registros aponta para registro existente")

    # ------------------------------------------------------------------ 8 ---
    # Criada pela tarefa 15, em 13/10/2026. O manifesto existe porque 27 das 40
    # pecas de literatura do corpus NAO podem ser redistribuidas -- duas declaram
    # todos os direitos reservados no proprio arquivo, e entre as 25 sem
    # declaracao estao livros da Cambridge, da Wiley-Blackwell, da Vozes e da
    # Companhia das Letras. O corpus nao vai a remoto publico, e o manifesto e o
    # que mantem a pesquisa VERIFICAVEL sem ser redistribuivel: rota + SHA-256.
    #
    # E a checagem serve a um segundo proposito que vale por si: um PDF que mude
    # de bytes sem mudar de nome quebraria toda ancora que dependa dele, e ate
    # aqui NADA acusava. Agora acusa.
    cabecalho(8, "CORPUS x MANIFESTO (presença e SHA-256)")
    import csv as _csv
    import hashlib as _hl
    import io as _io
    MAN = RAIZ / "Fontes/MANIFESTO-CORPUS.csv"
    if not MAN.exists():
        falhas.append("manifesto do corpus ausente: Fontes/MANIFESTO-CORPUS.csv")
        print("  X manifesto ausente — regere com "
              "python scripts/gerar_manifesto_corpus.py")
    else:
        with _io.open(str(MAN), encoding="utf-8-sig", newline="") as _fh:
            man = {r["caminho"]: r for r in _csv.DictReader(_fh)}
        em_disco = {p.relative_to(RAIZ).as_posix()
                    for p in (RAIZ / "Fontes").rglob("*.pdf")}
        # OS ANEXOS NAO-PDF QUE ANCORAM REGISTRO, desde 16/10/2026 (item 62). A
        # regra vem IMPORTADA do gerador, nao reimplementada aqui: se as duas
        # divergissem, uma diria "falta no manifesto" e a outra "sobra em
        # disco", para sempre. Ate 16/10 este conjunto era vazio por construcao
        # -- a varredura era so de PDF -- e dois arquivos ancoravam registro sem
        # vigilancia de bytes, um deles declarando na propria nota que a tinha.
        from gerar_manifesto_corpus import ancoras_nao_pdf
        em_disco |= set(ancoras_nao_pdf())
        faltam = sorted(set(man) - em_disco)
        sobram = sorted(em_disco - set(man))
        mudou = []
        for rel in sorted(set(man) & em_disco):
            h = _hl.sha256()
            with _io.open(str(RAIZ / rel), "rb") as _f:
                for bl in iter(lambda: _f.read(1 << 20), b""):
                    h.update(bl)
            if h.hexdigest() != man[rel]["sha256"]:
                mudou.append(rel)
        print("  %d peça(s) no manifesto, %d em disco" % (len(man), len(em_disco)))
        for rel in faltam:
            falhas.append("no manifesto e ausente do disco: {}".format(rel))
            print("    X no manifesto e ausente do disco: {}".format(rel))
        for rel in sobram:
            falhas.append("em disco e fora do manifesto: {}".format(rel))
            print("    X em disco e fora do manifesto: {} — regere o manifesto"
                  .format(rel))
        for rel in mudou:
            falhas.append("SHA-256 divergente: {}".format(rel))
            print("    X SHA-256 DIVERGENTE: {} — os bytes mudaram, e toda âncora "
                  "que dependa desta peça está sob suspeita".format(rel))
        if not (faltam or sobram or mudou):
            print("  OK — presença e SHA-256 batem peça por peça")


    # ---------------------------------------------------------------------- 9
    # CLASSE INFERIOR COM ANCORA DOCUMENTAL APONTADA TEM DE DIZER POR QUE.
    #
    # Nasceu em 25/10/2026 (item 86) do que o item 83 revelou: o criterio de
    # `Confirmado em fonte primaria` vivia em PROSA dentro de PT-01A e nunca
    # tinha sido escrito em `vocabulario_status_classe`. Escrito, ele promoveu
    # SEIS registros -- o dobro do que a pendencia nomeava -- porque ninguem
    # podia ler o criterio para aplica-lo aos treze candidatos.
    #
    # A GUARDA NAO DECIDE A CLASSE, e nao poderia: duas das tres condicoes do
    # vocabulario nao sao decidiveis por maquina. "A peca do proprio ato" e
    # semantico -- PT-27 ancora a CPMI, documental, que CITA outra peca; PT-02A
    # ancora o acordao de OUTRO processo. E "insuficiencia pendente" e juizo de
    # prosa. O que ela exige e que o DESVIO SEJA EXPLICADO: registro em
    # `Confirmado` que ancore peca documental COM localizador que a aponte tem
    # de trazer a marca canonica no `status_verificacao`. E a forma de
    # PARCIAIS_BASE -- a excecao e legitima e tem de estar escrita.
    #
    # UMA MARCA, NAO UMA LISTA. Lista de marcas e a fragilidade que esta casa
    # pagou duas vezes: a checagem 7 era cega a caixa e passou nome morto por
    # onze dias, e a G2 nao tinha a forma coletiva da negacao e nao EXAMINOU a
    # linha falsa. Aqui a guarda confere uma cadeia so.
    #
    # LIMITE DECLARADO: ela nao alcanca quem cita por LOCALIZADOR ESTRUTURAL,
    # porque `pares()` nao cede numeral para `inteiro teor` nem para `§secao`.
    # Medido em 25/10/2026: PT-01A, PT-19A e PT-38 caiam fora por isso, e os
    # tres declaravam a razao de todo modo. Alcance entao: SEIS registros.
    #
    # ATUALIZADO EM 27/10/2026 (item 95): **PT-38 ENTROU no alcance** ao
    # ganhar `CPMI: 668, 671-672, 676`, e a guarda o pegou mudo na mesma
    # rodada em que a ancora entrou. A licao e de desenho e vale para as
    # outras guardas deste arquivo: **o alcance de uma guarda que depende
    # de FORMA DE CITACAO cresce sozinho quando um registro muda de
    # forma.**
    #
    # E EM 28/10/2026 ELE ENCOLHEU: PT-38 foi promovido a `Confirmado em
    # fonte primaria` e SAIU do alcance, um dia depois de entrar. O
    # comentario trazia a cifra do alcance com a advertencia de que ela
    # nao era fixa -- e envelheceu em UM DIA de todo modo. **A advertencia
    # nao conserta a cifra: so a cifra conserta a cifra.** Por isso o
    # numero saiu daqui: a guarda IMPRIME o alcance a cada rodada, na
    # linha `registro(s) em Confirmado com ancora documental apontada`, e
    # essa e a cifra medida. Nao escreva outra em prosa, aqui ou fora.
    cabecalho(9, "CLASSE INFERIOR COM ÂNCORA DOCUMENTAL DIZ POR QUÊ")
    import sys as _sys9
    _sys9.path.insert(0, str(RAIZ / "scripts"))
    from conferir_paginas import pares as _pares9
    MARCA_CLASSE = "CLASSE NÃO PRIMÁRIA:"
    LIT_EIXOS = {"05", "12", "13", "14", "15"}
    _rd = dados["metadados"]["registro_documentos"]
    _mudos, _alcance = [], 0
    for ev in dados["eventos"]:
        if ev.get("status_classe") != "Confirmado":
            continue
        _docum = set()
        for _p in (ev.get("fonte_local") or "").split(";"):
            _p = _p.strip().replace("\\", "/")
            _m = re.match(r"Fontes/(\d{2})_", _p)
            if _m and _m.group(1) not in LIT_EIXOS:
                _docum.add(_p)
        _aponta = None
        for _cod, _ in _pares9(ev.get("fonte_pagina")):
            if (_rd.get(_cod) or "").replace("\\", "/") in _docum:
                _aponta = _cod
                break
        if not _aponta:
            continue
        _alcance += 1
        if MARCA_CLASSE not in (ev.get("status_verificacao") or ""):
            _mudos.append((ev["id"], _aponta))
    print("  %d registro(s) em `Confirmado` com âncora documental apontada"
          % _alcance)
    for _rid, _cod in _mudos:
        falhas.append("classe sem razão declarada: {} ancora {} e não traz "
                      "a marca".format(_rid, _cod))
        print("    X {} ancora {} com localizador e NAO declara por que a "
              "classe nao e primaria".format(_rid, _cod))
    if _mudos:
        print("    escreva `" + MARCA_CLASSE + " <razao>` no "
              "status_verificacao, ou promova a classe")
    else:
        print("  OK — todos declaram a razão da classe")


    # --------------------------------------------------------------------- 10
    # AS CIFRAS DE ESTADO DO README CONTRA O MEDIDO.
    #
    # Nasceu em 27/10/2026 (item 91), da revisao do repositorio. O README e o
    # painel da agenda eram DOIS PAINEIS ESCRITOS A MAO, e os dois estavam
    # errados: o painel datava-se de 29/09 e nenhuma cifra dele batia; o README
    # dizia "nove passos" quando eram catorze, "oito checagens" quando eram
    # nove, "64 PDFs / 12.144 p." quando eram 65 / 12.352 e "25 migracoes"
    # quando eram 26. O painel passou a ser GERADO; o README continua escrito a
    # mao, porque e porta de entrada e nao painel -- e por isso ganha guarda.
    #
    # **A GUARDA FALHA SE A ANCORA DESAPARECER**, e isso e deliberado: guarda
    # que nao acha o que vigia e passa em silencio ja morreu duas vezes nesta
    # casa -- a vigilancia de SHA-256 que nao cobria arquivo nao-PDF, e a
    # exclusao de caminho inerte por separador de plataforma. Reescrever a
    # frase do README obriga a reescrever a ancora aqui.
    cabecalho(10, "AS CIFRAS DO README CONTRA O MEDIDO")
    import csv as _csv10
    import glob as _gl10
    import io as _io10
    _rd = (RAIZ / "README.md").read_text(encoding="utf-8")
    _ci = (RAIZ / "scripts/ciclo.sh").read_text(encoding="utf-8")
    _vi = (RAIZ / "scripts/verificar_integridade.py").read_text(encoding="utf-8")
    with _io10.open(str(RAIZ / "Fontes/MANIFESTO-CORPUS.csv"),
                    encoding="utf-8-sig") as _fh10:
        _man = list(_csv10.DictReader(_fh10))
    _pdf = [r for r in _man if r["caminho"].lower().endswith(".pdf")]
    _docpdf = [r for r in _pdf
               if r.get("documental", "").strip().lower() == "sim"]

    def _mil10(n):
        return "{:,}".format(int(n)).replace(",", ".")

    ESPERADO = [
        ("passos do ciclo", r"\*\*(\d+) passos\*\*",
         max(int(x) for x in re.findall(r"== \d+/(\d+) ", _ci))),
        ("geradores", r"\*\*(\d+) geram\*\*",
         len(re.findall(r"python scripts/gerar_", _ci))),
        ("conferidores", r"\*\*(\d+)\s*\n?\s*conferem\*\*",
         len(re.findall(r"python scripts/(?:conferir_|verificar_|desenhar_)",
                        _ci))),
        ("checagens estruturais", r"\*\*(\d+) checagens estruturais\*\*",
         len(set(re.findall(r"cabecalho\((\d+),", _vi)))),
        ("PDFs do corpus", r"\*\*(\d+) PDFs,", len(_pdf)),
        ("páginas dos PDFs", r"\*\*\d+ PDFs, ([\d.]+) p\.\*\*",
         _mil10(sum(int(r["paginas"]) for r in _pdf))),
        ("âncoras não-PDF", r"\*\*(\d+) âncoras não-PDF\*\*",
         len(_man) - len(_pdf)),
        ("PDFs documentais", r"\*\*(\d+) PDFs / [\d.]+ p\. são fonte",
         len(_docpdf)),
        # ACRESCENTADA EM 28/10/2026 (item 97). A entrada acima capturava a
        # CONTAGEM e pulava a cifra de PAGINAS da mesma frase, com
        # `[\d.]+`. Em 28/10 a guarda acusou tres cifras do README e
        # deixou passar a quarta, a seis caracteres da terceira: eu a
        # corrigi a mao e ninguem me cobraria o erro. **Presenca da cifra
        # certa nao prova ausencia da errada no mesmo paragrafo** -- e o
        # proprio padrao da guarda declarava esta como irrelevante.
        ("páginas dos PDFs documentais",
         r"\*\*\d+ PDFs / ([\d.]+) p\. são fonte",
         _mil10(sum(int(r["paginas"]) for r in _docpdf))),
        ("migrações históricas", r"\*\*(\d+) migrações de uso único\*\*",
         len(_gl10.glob(str(RAIZ / "scripts/historico/*.py")))),
    ]
    _erradas = _ausentes = 0
    for rotulo, padrao, verdade in ESPERADO:
        m = re.search(padrao, _rd)
        if not m:
            _ausentes += 1
            falhas.append("README: a âncora de '{}' desapareceu".format(rotulo))
            print("    X a ancora de '{}' nao esta mais no README -- "
                  "reescreva o padrao aqui".format(rotulo))
            continue
        if m.group(1) != str(verdade):
            _erradas += 1
            falhas.append("README diz {} em '{}', e são {}".format(
                m.group(1), rotulo, verdade))
            print("    X README diz {} em '{}', e sao {}".format(
                m.group(1), rotulo, verdade))
    if not (_erradas or _ausentes):
        print("  OK — as %d cifras de estado do README batem com o medido"
              % len(ESPERADO))

    # --------------------------------------------------------------------- --
    print("\n" + "=" * 72)
    if falhas:
        print("RESULTADO: {} FALHA(S)".format(len(falhas)))
        for f in falhas:
            print("  X " + f)
    else:
        print("RESULTADO: APROVADO — as dez checagens passaram")
    for a in avisos:
        print("  ~ aviso: " + a)
    print("=" * 72)
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
