#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Onde ler cada um dos 43 itens da camada A — o passo que antecede a leitura.

Passo 3 do encaminhamento do item 11.3 da agenda (tarefa 17 da "Ordem de
ataque") começa aqui. A triagem de `scripts/triar_dois.py` disse *quais* obras
sustentam os mecanismos que o codebook afirma. Ela não disse **onde elas estão**
— e sem isso "ler na fonte" não é uma tarefa, é uma intenção.

POR QUE ESTE SCRIPT EXISTE, E POR QUE ELE NÃO É A LEITURA. A camada A saiu de
metadado de agência: título, veículo, ano, autoria. O projeto já sabe quanto
disso não sobrevive à leitura — as dez fichas de
`docs/analise/08_BIBLIOGRAFIA-METODOLOGICA.md` nomeiam quatro modos de falha,
e a segunda leva de 29/09 nomeou um quinto. Este script não lê nenhuma obra. Ele
responde a pergunta anterior: **desta lista, o que eu consigo abrir?** A resposta
divide os 43 em rotas de acesso, e só a primeira delas permite ficha hoje.

O TERCEIRO REGISTRO, E O QUE ELE ACRESCENTA. A verificação de 29/09 usou dois
eixos — o DOI resolve (CrossRef, DataCite) e o título registrado casa com o
declarado na síntese. Aqui entra um terceiro informante, o **OpenAlex**, que
agrega CrossRef, PubMed, repositórios e o texto aberto quando existe. Ele serve
a duas coisas ao mesmo tempo: dá a rota de acesso e **confere o título uma
terceira vez**, num acervo que não é o que gerou o dado da triagem. Divergência
aqui não condena o item; marca-o para conferência na leitura.

POR QUE OpenAlex E NÃO Unpaywall. A rota de texto aberto do Unpaywall exigiria
`?email=`, isto é, mandar dado pessoal do pesquisador a um terceiro que ele não
pediu. O OpenAlex responde sem identificação — o `mailto` do "polite pool" é
opcional, e pela mesma razão está ausente aqui, como no verificador de DOIs.

AS QUATRO ROTAS, e o que cada uma autoriza:

    CORPUS   o arquivo está em Fontes/. Ficha possível hoje, sem rede.
    ABERTO   há texto integral livre, com licença declarada e URL de PDF.
    VITRINE  o registro diz "acesso aberto" mas só devolve página de destino:
             resumo e metadado do editor, não o texto. Não autoriza ficha.
    FECHADO  não há rota livre. Depende de acesso institucional — e é a maior
             parte, porque a camada A é feita de clássicos e de periódicos de
             movimentos sociais, que não publicam em ouro.

A distinção VITRINE/ABERTO é o ponto do script. "is_oa: true" no registro não
significa texto disponível: significa que alguém declarou abertura em algum
lugar. Sem URL de PDF não há o que ler, e tratar os dois como a mesma coisa
produziria uma lista de leitura que não se pode cumprir — o mesmo defeito de
sempre, a cifra correta no referente errado.

Uso:  python scripts/localizar_camada_a.py [--autoteste]
"""
import csv
import io
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parent.parent
TRIAGEM = RAIZ / "data/processed/triagem_dois.csv"
CACHE = RAIZ / "data/external/openalex_cache.jsonl"
SAIDA = RAIZ / "data/processed/camada_a_acesso.csv"

# Sem `mailto`: ver o cabeçalho. O OpenAlex atende sem identificação.
UA = "verificador-bibliografico-8jan/1.0 (pesquisa academica; python-urllib)"
API = "https://api.openalex.org/works/doi:"

# Os itens da camada A cujo arquivo está no corpus. A chave é o DOI porque é o
# que a planilha carrega; o valor é o caminho relativo, conferido na execução.
NO_CORPUS = {
    "10.1017/CBO9780511805431":
        "Fontes/05_Bibliografia-teorica/McADAM-TARROW-TILLY_Dynamics-of-Contention_Cambridge-2001.pdf",
    "10.1017/CBO9780511813245":
        "Fontes/05_Bibliografia-teorica/TARROW_O-poder-em-movimento_Vozes-2009.pdf",
    "10.1002/9780470674871.wbespm127":
        "Fontes/05_Bibliografia-teorica/SNOW-DELLA-PORTA-KLANDERMANS-McADAM_"
        "Wiley-Blackwell-Encyclopedia-of-Social-and-Political-Movements_2013.pdf",
    # Entrou no corpus em 13/10/2026. A rota que o REGISTRO declara para esta peca
    # e o PDF da Wiley, que devolve 403; a rota que serviu o arquivo foi o deposito
    # de Amsterdam, no campo `locations`. Declarar CORPUS aqui diz o que e verdade
    # hoje -- o arquivo esta em Fontes/ -- em vez de repetir a rota do registro.
    "10.1002/9781119168577.ch22":
        "Fontes/05_Bibliografia-teorica/SNOW-VLIEGENTHART-KETELAARS_"
        "The-framing-perspective-on-social-movements_Wiley-Blackwell-Companion-2ed_2019.pdf",
    # OS OITO DA MOBILIZATION, entregues pelo pesquisador em 28/10/2026
    # pelo pedido do dia anterior. A rota do REGISTRO e FECHADO nos oito --
    # medido na API do OpenAlex antes de pedir: `oa_status = closed` nos oito
    # e ZERO depositos abertos entre os treze que ele lista. CORPUS aqui diz
    # o que e verdade hoje: o arquivo esta em Fontes/.
    "10.17813/maiq.14.3.kx87723664558jm4":
        "Fontes/05_Bibliografia-teorica/"
        "BROER-DUYVENDAK_Discursive-opportunities-feeling-rules_Mobilization-14-3_2009.pdf",
    "10.17813/maiq.15.1.86260543m3110705":
        "Fontes/05_Bibliografia-teorica/"
        "JUNG_Disentangling-protest-cycles_Mobilization-15-1_2010.pdf",
    "10.17813/maiq.16.1.74v41g7nl3722775":
        "Fontes/05_Bibliografia-teorica/"
        "BEISSINGER_Mechanisms-of-Maidan_Mobilization-16-1_2011.pdf",
    "10.17813/maiq.17.1.u7rw348t8200174h":
        "Fontes/05_Bibliografia-teorica/"
        "ALIMI-BOSI-DEMETRIOU_Relational-dynamics-processes-of-radicalization_Mobilization-17-1_2012.pdf",
    "10.17813/maiq.19.1.x74278226830m69l":
        "Fontes/05_Bibliografia-teorica/"
        "SNOW-BENFORD-McCAMMON-HEWITT-FITZGERALD_Framing-perspective-25-anos_Mobilization-19-1_2014.pdf",
    "10.17813/1086-671x-24-3-251":
        "Fontes/05_Bibliografia-teorica/"
        "KRIESI-HUTTER-BOJAR_Contentious-episode-analysis_Mobilization-24-3_2019.pdf",
    "10.17813/1086-671x-26-1-87":
        "Fontes/05_Bibliografia-teorica/"
        "ELLEFSEN_Unintended-consequences-of-escalated-repression_Mobilization-26-1_2021.pdf",
    "10.17813/1086-671x-30-4-387":
        "Fontes/05_Bibliografia-teorica/"
        "CASTRO_Deterrence-or-defiance_Mobilization-30-4_2025.pdf",
}

# =============================================================================
# O ESTADO DE LEITURA — e por que ele é gerado, não digitado
# =============================================================================
# A regra de 25/09/2026: peça escrita à mão que reproduz número do codebook
# envelhece. A tarefa 17 da "Ordem de ataque" trazia "os 43 da camada A, 6
# lidos, ~26 atrás de muro" — três números à mão, e o terceiro não fechava a
# soma. Aqui eles passam a sair da execução.
#
# FICHA: item com ficha da PRIMEIRA leva (01/09/2026), em
# `docs/analise/08_BIBLIOGRAFIA-METODOLOGICA.md` §1. Ficha é o padrão do
# projeto para "verificado"; nem toda ficha é leitura integral.
FICHAS = {
    "10.3998/mpub.2556282": "ficha 1 — Beach & Pedersen, divergência de edição",
    "10.1086/392759": "ficha 2 — Machamer, Darden & Craver",
    "10.1177/0267323112441007": "ficha 3 — Cammaerts",
    "10.1086/378395": "ficha 4 — Almeida",
    "10.1080/14742837.2014.947253": "ficha 5 — Motta, Renata",
    "10.17813/maiq.10.1.t5767064661w2u34": "ficha 6 — Koopmans",
    "10.1080/09636412.2015.1036624": "ficha 9 — Waldner",
}

# LIDO NA FONTE: obra aberta e lida, com onde e quando. É o passo 3.
#
# TERCEIRO CAMPO ACRESCENTADO EM 08/10/2026, e fecha um buraco que enganou o
# próprio projeto: **`LIDO` não implicava arquivo no corpus.** A peça de Castañeda
# e Jenks constava aqui como "MDPI, integral" desde 30/09 e o PDF não estava em
# `Fontes/` — tinha sido lida on-line. Sem arquivo local, `conferir_paginas.py`
# não confere página nenhuma, de modo que o estado prometia âncora que não
# existia. O terceiro campo é o caminho no corpus, ou None quando a leitura foi
# on-line; `main()` conta e nomeia os lidos sem arquivo.
LIDOS = {
    # ARQUIVADAS EM 08/10/2026, por decisão do pesquisador. As três estavam lidas
    # desde 30/09 SEM arquivo no corpus, e por isso não podiam ancorar página.
    # Rotas, porque cada uma exigiu uma: Collier saiu da página do DEPARTAMENTO DO
    # AUTOR em Berkeley, porque a Cambridge Core devolve 429 a cliente que não é
    # navegador (o PDF é oferecido de graça, 0,13 MB, e o navegador real o alcança);
    # Mayntz saiu da API REST do MPG.PuRe, porque a página do item está atrás do
    # Anubis, o mesmo desafio de prova-de-trabalho da OpenEdition; González-Bailón
    # et al. saiu do PDF aberto da Nature, em uma chamada.
    "10.1017/s1049096511001429": (
        "30/09 on-line; 08/10 no corpus",
        "Berkeley (página do autor), integral, 8 p. — impressa = PDF + 822",
        "Fontes/05_Bibliografia-teorica/COLLIER_Understanding-process-tracing_PS-44-4_2011.pdf"),
    "10.1177/0048393103262552": (
        "30/09 on-line; 08/10 no corpus",
        "MPG.PuRe via API REST, integral, 23 p. — impressa = PDF + 236",
        "Fontes/05_Bibliografia-teorica/MAYNTZ_Mechanisms-in-the-analysis-of-social-macro-phenomena_PSS-34-2_2004.pdf"),
    "10.1038/srep00197": (
        "30/09 on-line; 08/10 no corpus",
        "PDF aberto da Nature, integral, 7 p. — SEM paginação impressa de fascículo; "
        "QUATRO autores, e o primeiro é González-Bailón",
        "Fontes/05_Bibliografia-teorica/GONZALEZ-BAILON-BORGE-HOLTHOEFER-RIVERO-MORENO_Dynamics-of-protest-recruitment-through-an-online-network_Scientific-Reports-1_2011.pdf"),
    "10.3390/socsci12040238": (
        "30/09 on-line; 08/10 no corpus",
        "MDPI, integral — entregue pelo pesquisador em 08/10 e arquivada; ancora PT-08",
        "Fontes/15_Comparado-6-de-janeiro/CASTANEDA-JENKS_January-6th-and-"
        "de-democratization_Social-Sciences-12-4_2023.pdf"),
    "10.1177/20563051231196879": (
        "08/10",
        "SAGE, integral — entregue pelo pesquisador; ancora PT-08. Três autores",
        "Fontes/15_Comparado-6-de-janeiro/CHEN-LUKITO-KOO_Comparing-the-StopTheSteal-"
        "movement-across-platforms_Social-Media-and-Society-9-3_2023.pdf"),
    "10.1017/CBO9780511805431": (
        "30/09", "corpus, trechos definidores + índice",
        "Fontes/05_Bibliografia-teorica/McADAM-TARROW-TILLY_Dynamics-of-Contention_"
        "Cambridge-2001.pdf"),
    "10.1002/9780470674871.wbespm127": (
        "30/09", "corpus, integral",
        "Fontes/05_Bibliografia-teorica/SNOW-DELLA-PORTA-KLANDERMANS-McADAM_"
        "Wiley-Blackwell-Encyclopedia-of-Social-and-Political-Movements_2013.pdf"),
    # ACHADA EM 13/10/2026 PELO CAMPO `locations` DA API DO OpenAlex, que lista
    # TODOS os depositos e nao so o melhor. Este script guardava do OpenAlex
    # apenas o best_oa_location, e por isso o deposito de Amsterdam nunca havia
    # aparecido: a rota do editor (Wiley, declarada OURO) devolve 403, e a rota
    # que serve o arquivo esta em outro campo. Foi assim que Mayntz apareceu no
    # MPG.PuRe em 08/10, e vale para os pendentes que ainda tenham deposito.
    # QUATRO divergencias que so a abertura do arquivo mostrou: sao TRES autores
    # e a planilha nomeava zero; o volume e a 2a edicao, de 2019, pp. 392-410, e
    # a triagem registrou 2018; o OpenAlex chama o deposito de submittedVersion e
    # a folha de capa diz FINAL PUBLISHED VERSION; e a licenca e a do art. 25fa
    # da lei holandesa (emenda Taverne), nao CC -- uso pessoal permitido,
    # redistribuicao vedada, de modo que a peca e RESERVADA no manifesto.
    "10.1002/9781119168577.ch22": (
        "13/10",
        "UvA-DARE (Pure) via campo `locations`, integral, 20 p. — impressa = "
        "PDF + 390; TRES autores (Snow, Vliegenthart e Ketelaars); 2a ed. de "
        "2019, pp. 392-410; licenca Taverne, nao CC",
        "Fontes/05_Bibliografia-teorica/SNOW-VLIEGENTHART-KETELAARS_"
        "The-framing-perspective-on-social-movements_Wiley-Blackwell-Companion-2ed_2019.pdf"),
    # OS OITO DA MOBILIZATION, lidos em 28/10/2026 no dia em que chegaram.
    # **O OFFSET DE CADA UM FOI CONFERIDO FOLHA A FOLHA**, procurando o
    # numero impresso na borda de CADA folha -- nao derivado da primeira
    # pagina, que e o atalho que deriva em sete faixas quando a peca tem
    # material editorial. Tres folhas do lote nao trazem o numero na borda,
    # e a causa de cada uma esta medida e escrita no campo do meio.
    "10.17813/maiq.14.3.kx87723664558jm4": (
        "28/10",
        "integral, 20 p. — impressa = PDF + 336",
        "Fontes/05_Bibliografia-teorica/"
        "BROER-DUYVENDAK_Discursive-opportunities-feeling-rules_Mobilization-14-3_2009.pdf"),
    "10.17813/maiq.15.1.86260543m3110705": (
        "28/10",
        "integral, 20 p. — impressa = PDF + 24",
        "Fontes/05_Bibliografia-teorica/"
        "JUNG_Disentangling-protest-cycles_Mobilization-15-1_2010.pdf"),
    "10.17813/maiq.16.1.74v41g7nl3722775": (
        "28/10",
        "integral, 19 p. — impressa = PDF + 24",
        "Fontes/05_Bibliografia-teorica/"
        "BEISSINGER_Mechanisms-of-Maidan_Mobilization-16-1_2011.pdf"),
    "10.17813/maiq.17.1.u7rw348t8200174h": (
        "28/10",
        "integral, 20 p. — impressa = PDF + 6",
        "Fontes/05_Bibliografia-teorica/"
        "ALIMI-BOSI-DEMETRIOU_Relational-dynamics-processes-of-radicalization_Mobilization-17-1_2012.pdf"),
    "10.17813/maiq.19.1.x74278226830m69l": (
        "28/10",
        "integral, 24 folhas e o ARTIGO tem 23 — impressa = PDF + 22; a linha de copyright diz 23-45 e a folha 24 e anuncio da editora",
        "Fontes/05_Bibliografia-teorica/"
        "SNOW-BENFORD-McCAMMON-HEWITT-FITZGERALD_Framing-perspective-25-anos_Mobilization-19-1_2014.pdf"),
    "10.17813/1086-671x-24-3-251": (
        "28/10",
        "integral, 23 p. — impressa = PDF + 250; a folha 17 e figura de pagina inteira e nao traz o numero na borda",
        "Fontes/05_Bibliografia-teorica/"
        "KRIESI-HUTTER-BOJAR_Contentious-episode-analysis_Mobilization-24-3_2019.pdf"),
    "10.17813/1086-671x-26-1-87": (
        "28/10",
        "integral, 22 p. — impressa = PDF + 86; o arquivo traz MARCA DE DOWNLOAD nas 22 folhas, que entra na camada de texto",
        "Fontes/05_Bibliografia-teorica/"
        "ELLEFSEN_Unintended-consequences-of-escalated-repression_Mobilization-26-1_2021.pdf"),
    "10.17813/1086-671x-30-4-387": (
        "28/10",
        "integral, 22 p. — impressa = PDF + 386; chegou em DUAS copias e entrou a sem marca de download",
        "Fontes/05_Bibliografia-teorica/"
        "CASTRO_Deterrence-or-defiance_Mobilization-30-4_2025.pdf"),
}

# Impedimento declarado, para a conta não sugerir que só falta querer.
IMPEDIDOS = {
    "10.1017/CBO9780511813245": "varredura sem camada de texto, 2 págs. por folha",
    "10.1086/226464": "referência sem arquivo coletado",
    "10.1002/9780470674871.wbespm127.pub2": "revisão de 2022; não está no volume de 2013",
}


def normalizar(t):
    """Título comparável entre acervos: sem acento, sem pontuação, sem caixa.

    Os acervos divergem em pontuação e em hífen (o CrossRef devolve U+2010 onde
    o OpenAlex devolve U+002D), em itálico marcado com tag, e em travessão de
    subtítulo. Comparar cadeia crua produziria divergência em quase todo item e
    a checagem perderia o sentido."""
    t = unicodedata.normalize("NFKD", t or "")
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"[^0-9a-zA-Z ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip().lower()


def cache_lido():
    if not CACHE.exists():
        return {}
    guardado = {}
    with io.open(CACHE, encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                reg = json.loads(linha)
                guardado[reg["doi_consultado"]] = reg
    return guardado


def consultar(doi):
    """Devolve o registro do OpenAlex, ou um dicionário de ausência."""
    req = urllib.request.Request(API + urllib.parse.quote(doi, safe="/:."),
                                 headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            w = json.load(r)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {"doi_consultado": doi, "achado": False}
        raise
    oa = w.get("open_access") or {}
    melhor = w.get("best_oa_location") or {}
    return {
        "doi_consultado": doi,
        "achado": True,
        "titulo": w.get("title") or "",
        "tipo": w.get("type") or "",
        "ano": w.get("publication_year"),
        "is_oa": bool(oa.get("is_oa")),
        "oa_status": oa.get("oa_status") or "",
        "pdf_url": melhor.get("pdf_url") or "",
        "landing": melhor.get("landing_page_url") or "",
        "licenca": melhor.get("license") or "",
        "versao": melhor.get("version") or "",
        "citado_por": w.get("cited_by_count"),
    }


def estado(doi):
    """Em que pé está a leitura deste item. Exclusivo e exaustivo, nesta ordem.

    LIDO vence FICHA porque leitura integral supera conferência de metadado;
    IMPEDIDO só se aplica a quem não foi lido nem tem ficha."""
    if doi in LIDOS:
        return "LIDO"
    if doi in FICHAS:
        return "FICHA"
    if doi in IMPEDIDOS:
        return "IMPEDIDO"
    return "PENDENTE"


def rota(linha, reg):
    """Classifica o item numa das quatro rotas. Ver o cabeçalho."""
    if linha["doi"] in NO_CORPUS:
        return "CORPUS"
    if not reg.get("achado"):
        return "FECHADO"
    if reg["pdf_url"]:
        return "ABERTO"
    if reg["is_oa"]:
        return "VITRINE"
    return "FECHADO"


def carregar():
    with io.open(TRIAGEM, encoding="utf-8-sig") as f:
        return [r for r in csv.DictReader(f) if r["camada"] == "A"]


def autoteste():
    assert normalizar("Opportunity Organizations and Threat‐Induced Contention") == \
        normalizar("Opportunity Organizations and Threat-Induced Contention"), \
        "o hifen tipografico tem de ser equiparado ao comum"
    assert normalizar("<i>Event</i> Catalogs, as Theories") == "event catalogs as theories"

    linhas = carregar()
    assert len(linhas) == 43, "a camada A tem 43 itens; achei {}".format(len(linhas))

    for doi, caminho in NO_CORPUS.items():
        assert (RAIZ / caminho).exists(), "arquivo declarado no corpus nao existe: " + caminho
        assert any(r["doi"] == doi for r in linhas), "DOI de corpus fora da camada A: " + doi

    # Rota depende de PDF, não de `is_oa`: é a distinção que o script existe para fazer.
    assert rota({"doi": "x"}, {"achado": True, "is_oa": True, "pdf_url": ""}) == "VITRINE"
    assert rota({"doi": "x"}, {"achado": True, "is_oa": True, "pdf_url": "u"}) == "ABERTO"
    assert rota({"doi": "x"}, {"achado": False}) == "FECHADO"

    # Todo DOI declarado em FICHAS, LIDOS ou IMPEDIDOS tem de estar na camada A;
    # senão a conta de estado divide um universo que não é o dela.
    dois = {r["doi"] for r in linhas}
    for nome, d in (("FICHAS", FICHAS), ("LIDOS", LIDOS), ("IMPEDIDOS", IMPEDIDOS)):
        for doi in d:
            assert doi in dois, "{} declara DOI fora da camada A: {}".format(nome, doi)

    # Os três conjuntos não se sobrepõem onde importa: nenhum item lido pode
    # estar declarado como impedido.
    assert not (set(LIDOS) & set(IMPEDIDOS)), "item lido nao pode estar impedido"
    assert estado(next(iter(LIDOS))) == "LIDO"
    assert estado("10.1017/CBO9780511813245") == "IMPEDIDO"
    print("autoteste OK — 43 itens, normalizador, as quatro rotas e os quatro estados")


def main():
    if "--autoteste" in sys.argv:
        autoteste()
        return 0

    linhas = carregar()
    if len(linhas) != 43:
        print("ABORTA: a camada A tem {} itens, nao 43".format(len(linhas)))
        return 1

    guardado = cache_lido()
    novos = []
    for r in linhas:
        doi = r["doi"]
        if doi.lower() in {k.lower() for k in guardado}:
            continue
        if doi in guardado:
            continue
        reg = consultar(doi)
        guardado[doi] = reg
        novos.append(reg)
        time.sleep(0.15)
    if novos:
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        with io.open(CACHE, "a", encoding="utf-8", newline="\n") as f:
            for reg in novos:
                f.write(json.dumps(reg, ensure_ascii=False) + "\n")
        print("consultei {} DOIs no OpenAlex; {} vieram do cache".format(
            len(novos), len(linhas) - len(novos)))
    else:
        print("todos os 43 vieram do cache de {}".format(CACHE.relative_to(RAIZ)))

    contagem = {"CORPUS": 0, "ABERTO": 0, "VITRINE": 0, "FECHADO": 0}
    leitura = {"LIDO": 0, "FICHA": 0, "IMPEDIDO": 0, "PENDENTE": 0}
    divergencias = []
    saida = []
    for r in linhas:
        reg = guardado.get(r["doi"], {"achado": False})
        rt = rota(r, reg)
        contagem[rt] += 1
        est = estado(r["doi"])
        leitura[est] += 1
        if reg.get("achado") and normalizar(reg["titulo"]) != normalizar(r["titulo"]):
            divergencias.append((r["doi"], r["titulo"], reg["titulo"]))
        saida.append({
            "rota": rt,
            "estado": est,
            "nota": LIDOS.get(r["doi"], ("", ""))[1] or FICHAS.get(r["doi"], "")
                    or IMPEDIDOS.get(r["doi"], ""),
            "doi": r["doi"],
            "ano": r["ano"],
            "titulo": r["titulo"],
            "veiculo": r["veiculo"],
            "uso": r["uso"],
            "onde": NO_CORPUS.get(r["doi"], reg.get("pdf_url") or reg.get("landing") or ""),
            "licenca": reg.get("licenca", ""),
            "versao": reg.get("versao", ""),
            "oa_status": reg.get("oa_status", ""),
            "tipo_openalex": reg.get("tipo", ""),
        })

    saida.sort(key=lambda d: (["CORPUS", "ABERTO", "VITRINE", "FECHADO"].index(d["rota"]),
                              d["veiculo"], d["ano"]))
    with io.open(SAIDA, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(saida[0].keys()))
        w.writeheader()
        w.writerows(saida)

    print()
    print("| Estado da leitura | Itens | O que significa |")
    print("|:--|--:|:--|")
    print("| LIDO na fonte | {} | obra aberta e lida — o passo 3 |".format(leitura["LIDO"]))
    print("| FICHA, sem leitura | {} | primeira leva, 01/09: metadado conferido |".format(leitura["FICHA"]))
    print("| IMPEDIDO | {} | sem camada de texto, sem arquivo, ou fora do volume |".format(leitura["IMPEDIDO"]))
    print("| PENDENTE | {} | **é o que falta da tarefa 17** |".format(leitura["PENDENTE"]))
    print("| **Total** | **{}** | |".format(sum(leitura.values())))

    # LIDO nao implica arquivo no corpus, e essa confusao enganou o projeto por
    # oito dias: ver o comentario de LIDOS. A conta abaixo e a correcao.
    sem_arquivo, inexistentes = [], []
    for doi, dados in LIDOS.items():
        caminho = dados[2] if len(dados) > 2 else None
        if not caminho:
            sem_arquivo.append(doi)
        elif not (RAIZ / caminho).exists():
            inexistentes.append((doi, caminho))
    print()
    print("**Dos {} lidos, {} tem arquivo no corpus e {} foram lidos so on-line.** "
          "Leitura on-line nao ancora pagina: `conferir_paginas.py` abre o PDF do "
          "corpus.".format(len(LIDOS), len(LIDOS) - len(sem_arquivo), len(sem_arquivo)))
    for doi in sem_arquivo:
        print("  - sem arquivo: {} — {}".format(doi, LIDOS[doi][1][:60]))
    for doi, caminho in inexistentes:
        print("  ! DECLARADO E AUSENTE: {} -> {}".format(doi, caminho))
    if inexistentes:
        raise SystemExit("caminho declarado em LIDOS nao existe em disco")
    print()
    print("| Rota | Itens | O que autoriza |")
    print("|:--|--:|:--|")
    print("| CORPUS | {} | ficha hoje, arquivo em `Fontes/` |".format(contagem["CORPUS"]))
    print("| ABERTO | {} | ficha hoje, texto integral livre |".format(contagem["ABERTO"]))
    print("| VITRINE | {} | só resumo e metadado do editor |".format(contagem["VITRINE"]))
    print("| FECHADO | {} | depende de acesso institucional |".format(contagem["FECHADO"]))
    print("| **Total** | **{}** | |".format(sum(contagem.values())))

    print()
    print("Legíveis hoje: **{}** dos 43.".format(contagem["CORPUS"] + contagem["ABERTO"]))
    print("Planilha: {}".format(SAIDA.relative_to(RAIZ)))

    if divergencias:
        print()
        print("Divergência de título no terceiro registro — conferir na leitura:")
        for doi, a, b in divergencias:
            print("  {}\n    triagem : {}\n    OpenAlex: {}".format(doi, a, b))

    print()
    for rt in ("CORPUS", "ABERTO", "VITRINE"):
        itens = [d for d in saida if d["rota"] == rt]
        if not itens:
            continue
        print("### {} ({})".format(rt, len(itens)))
        for d in itens:
            print("- {} ({}) — {} | {} | {}".format(
                d["titulo"][:70], d["ano"], d["veiculo"][:34],
                d["licenca"] or d["oa_status"] or "—", d["onde"][:88]))
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
