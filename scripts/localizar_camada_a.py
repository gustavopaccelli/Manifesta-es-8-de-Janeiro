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
`projeto-pos-doc/08_BIBLIOGRAFIA-METODOLOGICA.md` nomeiam quatro modos de falha,
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
    print("autoteste OK — 43 itens, normalizador e as quatro rotas")


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
    divergencias = []
    saida = []
    for r in linhas:
        reg = guardado.get(r["doi"], {"achado": False})
        rt = rota(r, reg)
        contagem[rt] += 1
        if reg.get("achado") and normalizar(reg["titulo"]) != normalizar(r["titulo"]):
            divergencias.append((r["doi"], r["titulo"], reg["titulo"]))
        saida.append({
            "rota": rt,
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
