#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Verificação dos DOIs das sínteses LeapSpace — existência e atribuição.

Completa o passo 1 do encaminhamento do item 11.3 da agenda (tarefa 9 da "Ordem
de ataque"). **Não é a primeira leva:** em 01/09/2026 dez itens foram conferidos
à mão, quatro divergentes, e as fichas estão em
`projeto-pos-doc/08_BIBLIOGRAFIA-METODOLOGICA.md` — leia-as antes de tratar
qualquer achado daqui como novo. Este script cobre os 411 de uma vez: extrai os
DOIs das sínteses de `Fontes/05_Bibliografia-teorica/`,
consulta cada um no CrossRef — e, se lá não estiver, na DataCite — e emite a
planilha que é o insumo da triagem por pertinência.

POR QUE ISSO EXISTE. As sínteses são geradas por sistema automatizado: não são
revisadas por pares, não têm autoria identificável e **não são citáveis**. O que
elas têm de valor é a lista de DOIs, que aponta para literatura real. Mas o
projeto já encontrou **um DOI fabricado** no levantamento original
(`10.1215/00382876-12345678`, corrigido em `LEIA-ME_metodologia_verificacao.md`).
Material gerado exige a mesma desconfiança: nada entra na bibliografia sem
resposta de uma agência de registro.

CALIBRAÇÃO DO EXTRATOR, e é o que dá confiança na contagem. A união dos DOIs das
**cinco** sínteses de 13/08/2026 — Process_tracing, Causal_mechanisms,
Political_Process, Mobilization_structures, Protest_cycle — dá exatamente
**325**, o número que o item 11.3 da agenda declara desde 14/08. A regex
reproduz o levantamento anterior, então não está inventando nem perdendo DOIs.
O `--autoteste` prende essa contagem.

RESSALVA DE CONTAGEM. A agenda fala em 325 porque foi escrita quando havia cinco
sínteses. Duas outras chegaram em 11/09/2026 —
`Political_and_discursive_opportunities` e `Framing_process_and_alignment` — e
acrescentam 86 DOIs distintos. O universo de hoje é **411**, não 325.

=============================================================================
O SEGUNDO EIXO, E A RAZÃO DE ELE EXISTIR — achado de 29/09/2026
=============================================================================

Confirmar que o DOI existe **não** confirma que a síntese o atribuiu à obra
certa. A síntese `Framing_process_and_alignment` lista, em sequência:

    Vaughan, E. (2010) How can teachers use a corpus for their own research?
        → https://doi.org/10.4324/9780203856949-40
    O'Halloran, K. (2010) How to use corpus linguistics in the study of media
        discourse  → https://doi.org/10.4324/9780203856949-48

O `-48` não existe. E o `-40`, que **existe e seria aprovado como
`CONFIRMADO`**, é justamente o capítulo de O'Halloran sobre discurso midiático —
não o de Vaughan. Os DOIs estão deslocados: um real, colado ao autor errado.

É o modo de falha que este projeto já nomeou — *a cifra correta no referente
errado* — agora dentro da bibliografia gerada. Daí o segundo eixo: para cada
menção, o título que o CrossRef devolve é procurado na janela de 300 caracteres
que antecede o DOI na síntese. Abaixo de 60% dos termos significativos
presentes, a menção vai para conferência **com o trecho impresso**, porque
checagem que só grita é checagem abandonada.

Isto é casamento de termos, não juízo bibliográfico: acento e maiúscula são
normalizados, palavras de até quatro letras e artigos são descartados. Título
traduzido pela síntese cai na lista de conferência com razão — e é rápido de
absolver lendo o trecho.

O QUE ESTE SCRIPT NÃO FAZ. Não tria por pertinência. A coluna `eixos` é uma
ordenação **mecânica** por termo no título e nos assuntos declarados pela
agência — não é juízo sobre o argumento. Decidir o que sustenta os mecanismos
afirmados no codebook é do pesquisador, e a leitura é na fonte, nunca na síntese.

Idempotente: as respostas ficam em cache (`data/external/crossref_cache.jsonl`),
então reexecutar só consulta o que falta.

Uso:  python scripts/verificar_dois_sinteses.py [--limite N] [--autoteste]
"""

import argparse
import csv
import html
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):          # cp1252 já abortou script deste
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # projeto no meio

RAIZ = Path(__file__).resolve().parent.parent
SINTESES = RAIZ / "Fontes/05_Bibliografia-teorica"
CACHE = RAIZ / "data/external/crossref_cache.jsonl"
CSV_OUT = RAIZ / "data/processed/dois_sinteses_leapspace.csv"

CROSSREF = "https://api.crossref.org/works/"
DATACITE = "https://api.datacite.org/dois/"
# Sem `mailto`: o "polite pool" do CrossRef pede um e-mail no User-Agent, e o
# e-mail do pesquisador não vai para serviço de terceiro sem ele pedir. O pool
# público atende igual, só sem prioridade.
UA = "verificador-bibliografico-8jan/1.0 (pesquisa academica; python-urllib)"

DOI = re.compile(r"10\.[0-9]{4,9}/[^\s\"<>]+")
LIXO_FINAL = ".,;:)]>"
JANELA = 300            # caracteres antes do DOI onde o título declarado mora
CORTE = 0.60            # fração dos termos do título que precisa aparecer ali

# Os três que nenhuma agência registra, com o que a leitura da própria síntese
# mostrou. Ficam aqui porque o diagnóstico custou consulta e vale como registro —
# o script não os trata de forma especial, só os explica na saída.
NAO_EXISTEM = {
    "10.1007/9781139858472":
        "Prefixo Springer (10.1007) colado a ISBN da Cambridge. A obra é real e é "
        "central para este projeto: BENNETT & CHECKEL (2014, org.), 'Process Tracing: "
        "From Metaphor to Analytic Tool'. DOI correto: 10.1017/CBO9781139858472. "
        "JÁ ERA CONHECIDO: a primeira leva de verificação, de 01/09/2026, achou e "
        "corrigiu este caso — ficha 8 de projeto-pos-doc/08_BIBLIOGRAFIA-METODOLOGICA.md.",
    "10.4324/9780203856949-48":
        "Este sufixo não existe. O capítulo de O'HALLORAN, 'How to use corpus "
        "linguistics in the study of media discourse', está depositado em "
        "10.4324/9780203856949-40 — que a síntese atribui a Vaughan. Ver o par em "
        "VIZINHOS_TROCADOS.",
    "10.4324/9781315731377-34":
        "Este sufixo não existe, mas o capítulo existe: CHENOWETH (2015), 'Political "
        "mobilization and institutions', está em 10.4324/9781315731377-28. Achado por "
        "busca de título em 29/09/2026 — testar só o DOI do livro levou, na primeira "
        "passada, à conclusão errada de que o capítulo não tinha sido depositado.",
}

# O par deslocado do Routledge Handbook of Corpus Linguistics, com os DOIs que
# o CrossRef confirma. Registro da correção; o script não reescreve a síntese,
# que é fonte imutável em Fontes/.
VIZINHOS_TROCADOS = {
    "10.4324/9780203856949-34": "VAUGHAN (2010), 'How can teachers use a corpus for "
                               "their own research?' — a síntese lhe deu o -40",
    "10.4324/9780203856949-40": "O'HALLORAN (2010), 'How to use corpus linguistics in "
                               "the study of media discourse' — a síntese lhe deu o -48",
}

# Ordenação mecânica por termo declarado. Não é triagem — ver o cabeçalho.
EIXOS = [
    ("brasil", ["brasil", "brazil", "latin america", "américa latina", "america latina"]),
    ("movimentos", ["social movement", "protest", "mobiliz", "contentious", "framing",
                    "political opportunit", "repertoire", "activis", "riot", "insurgen",
                    "revolution", "collective action"]),
    ("metodo", ["process tracing", "case study", "case-study", "causal inference",
                "methodolog", "qualitative research", "comparative method", "mixed method",
                "set-theoretic", "qca", "congruence", "bayesian", "causal mechanism"]),
]

VAZIAS = set("""the a an of in on for and or to with from as at by its their this that
how what when where which who de la le el does do sobre para como uma""".split())


def norm(s):
    """Minúscula, sem acento, só letras e números — para casar termo com termo."""
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9 ]", " ", s)


def termos(s):
    return [w for w in norm(s).split() if len(w) > 3 and w not in VAZIAS]


def texto_docx(caminho):
    """Todo o XML de texto do .docx, com as tags trocadas por espaço."""
    with zipfile.ZipFile(caminho) as z:
        partes = [z.read(n).decode("utf-8", "replace") for n in z.namelist()
                  if n.startswith("word/") and n.endswith(".xml")]
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", "".join(partes)))


def extrair():
    """({doi: [sínteses]}, [(doi, síntese, janela anterior)]) — menção por menção."""
    achados, mencoes = {}, []
    for arq in sorted(SINTESES.glob("*_LeapSpace.docx")):
        nome = arq.name.replace("_LeapSpace.docx", "")
        txt = texto_docx(arq)
        for m in DOI.finditer(txt):
            d = m.group(0).lower().rstrip(LIXO_FINAL)
            achados.setdefault(d, [])
            if nome not in achados[d]:
                achados[d].append(nome)
            mencoes.append((d, nome, txt[max(0, m.start() - JANELA):m.start()]))
    return achados, mencoes


def cache_lido():
    if not CACHE.exists():
        return {}
    with CACHE.open(encoding="utf-8", newline="") as fh:
        return {r["doi"]: r for r in (json.loads(l) for l in fh if l.strip())}


def pegar(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.load(r)


def limpar(t):
    """Sem tag e sem entidade: o CrossRef devolve <i> no titulo e &amp; no veiculo."""
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", t))).strip()


def consultar_datacite(doi):
    """Segunda via: há DOI legítimo que a DataCite registra e o CrossRef não."""
    try:
        a = pegar(DATACITE + urllib.parse.quote(doi, safe=""))["data"]["attributes"]
    except Exception:
        return None
    return {
        "doi": doi,
        "situacao": "CONFIRMADO (DataCite)",
        "detalhe": "registrado na DataCite, não no CrossRef",
        "tipo": (a.get("types") or {}).get("resourceTypeGeneral", ""),
        "ano": a.get("publicationYear") or "",
        "titulo": limpar(" ".join(t.get("title", "") for t in (a.get("titles") or []))),
        "veiculo": (a.get("container") or {}).get("title") or a.get("publisher", ""),
        "autores": "; ".join(c.get("name", "") for c in (a.get("creators") or [])[:3]),
        "assuntos": "; ".join(s.get("subject", "") for s in (a.get("subjects") or [])),
        "citado_por": "",
    }


def consultar(doi):
    """CrossRef; em 404, DataCite. Devolve o registro já reduzido ao que interessa."""
    try:
        msg = pegar(CROSSREF + urllib.parse.quote(doi, safe=""))["message"]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return consultar_datacite(doi) or {
                "doi": doi, "situacao": "NAO ENCONTRADO",
                "detalhe": "404 no CrossRef e na DataCite"}
        if e.code == 429:                      # devagar, e tenta uma vez só
            time.sleep(5)
            return None
        return {"doi": doi, "situacao": "ERRO", "detalhe": "HTTP {}".format(e.code)}
    except Exception as e:                     # rede, timeout, JSON malformado
        return {"doi": doi, "situacao": "ERRO", "detalhe": type(e).__name__}

    autores = "; ".join(
        "{}, {}".format(a.get("family", ""), a.get("given", "")).strip(", ")
        for a in msg.get("author", [])[:3]
    )
    if len(msg.get("author", [])) > 3:
        autores += " et al."
    datas = (msg.get("issued") or {}).get("date-parts") or [[None]]
    return {
        "doi": doi,
        "situacao": "CONFIRMADO",
        "detalhe": "",
        "tipo": msg.get("type", ""),
        "ano": datas[0][0] or "",
        "titulo": limpar(" ".join(msg.get("title") or [])),
        "veiculo": limpar(" ".join(msg.get("container-title") or [])) or msg.get("publisher", ""),
        "autores": autores,
        "assuntos": "; ".join(msg.get("subject") or []),
        "citado_por": msg.get("is-referenced-by-count", ""),
    }


def eixos(reg):
    """Rótulos mecânicos, por termo no título e nos assuntos da agência."""
    campo = "{} {}".format(reg.get("titulo", ""), reg.get("assuntos", "")).lower()
    return ";".join(nome for nome, ts in EIXOS if any(t in campo for t in ts))


def atribuicao(mencoes, cache):
    """Por menção: o título registrado aparece na janela que antecede o DOI?

    Devolve [(taxa, doi, síntese, janela)] só das menções abaixo do corte —
    as que pedem leitura. O caso O'Halloran/Vaughan cai aqui."""
    duvidas = []
    for doi, sintese, janela in mencoes:
        reg = cache.get(doi) or {}
        if not reg.get("situacao", "").startswith("CONFIRMADO") or not reg.get("titulo"):
            continue
        ts = termos(reg["titulo"])
        if not ts:
            continue
        jan = norm(janela)
        taxa = sum(1 for w in ts if w in jan) / len(ts)
        if taxa < CORTE:
            duvidas.append((round(taxa, 2), doi, sintese, janela))
    return sorted(duvidas)


def autoteste():
    """Prova que a regex pega o DOI fabricado, que a contagem de 13/08 se mantém,
    e — o que importa — que o segundo eixo pega o caso que o motivou."""
    amostra = ("ver 10.1177/0049124113500475. Também "
               "https://doi.org/10.1215/00382876-12345678, e (10.1086/210394) "
               "além de <10.1002/9780470674871.wbespm073>")
    achados = [m.group(0).lower().rstrip(LIXO_FINAL) for m in DOI.finditer(amostra)]
    assert achados == ["10.1177/0049124113500475", "10.1215/00382876-12345678",
                       "10.1086/210394", "10.1002/9780470674871.wbespm073"], achados

    todos, mencoes = extrair()
    cinco = {"Process_tracing", "Causal_mechanisms_in_social_science",
             "Political_Process_by_Charles_Tilly", "Mobilization_structures", "Protest_cycle"}
    u5 = {d for d, fs in todos.items() if cinco & set(fs)}
    assert len(u5) == 325, "as cinco sínteses de 13/08 tinham 325 DOIs, achei {}".format(len(u5))

    cache = cache_lido()
    if cache:
        alvo = "10.4324/9780203856949-40"
        assert cache.get(alvo, {}).get("situacao", "").startswith("CONFIRMADO"), \
            "o caso-prova precisa do cache preenchido: rode o script sem --autoteste"
        pegos = {d for _, d, _, _ in atribuicao(mencoes, cache)}
        assert alvo in pegos, ("o segundo eixo deixou passar o caso que o motivou: "
                              "{} atribuído a Vaughan".format(alvo))
        print("autoteste OK — regex fiel, 325 mantidos, e o caso O'Halloran/Vaughan é pego")
    else:
        print("autoteste OK — regex fiel e 325 mantidos (sem cache: eixo 2 não exercitado)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limite", type=int, help="consulta só os N primeiros (ensaio)")
    ap.add_argument("--autoteste", action="store_true")
    args = ap.parse_args()

    if args.autoteste:
        return autoteste()

    achados, mencoes = extrair()
    print("{} DOIs distintos em {} sínteses, {} menções".format(
        len(achados), len(list(SINTESES.glob("*_LeapSpace.docx"))), len(mencoes)))

    cache = cache_lido()
    faltam = [d for d in achados if d not in cache]
    if args.limite:
        faltam = faltam[:args.limite]
    print("{} em cache, {} a consultar".format(len(cache), len(faltam)))

    CACHE.parent.mkdir(parents=True, exist_ok=True)
    with CACHE.open("a", encoding="utf-8", newline="") as fh:
        for i, doi in enumerate(faltam, 1):
            reg = consultar(doi) or consultar(doi)          # 429: uma segunda chance
            if reg is None:
                reg = {"doi": doi, "situacao": "ERRO", "detalhe": "429 persistente"}
            fh.write(json.dumps(reg, ensure_ascii=False) + "\n")
            fh.flush()                                       # cache sobrevive a Ctrl-C
            cache[doi] = reg
            if i % 25 == 0 or i == len(faltam):
                print("  {}/{}".format(i, len(faltam)))
            time.sleep(0.06)

    duvidas = atribuicao(mencoes, cache)
    pior = {}
    for taxa, doi, _, _ in duvidas:
        pior[doi] = min(taxa, pior.get(doi, 1.0))

    COLS = ["doi", "situacao", "atribuicao", "eixos", "tipo", "ano", "titulo", "veiculo",
            "autores", "citado_por", "assuntos", "sinteses", "detalhe"]
    CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
    with CSV_OUT.open("w", encoding="utf-8-sig", newline="") as fh:   # Excel pt-BR
        w = csv.DictWriter(fh, fieldnames=COLS, extrasaction="ignore")
        w.writeheader()
        for doi in sorted(achados):
            reg = dict(cache.get(doi, {"doi": doi, "situacao": "NAO CONSULTADO"}))
            for campo in ("titulo", "veiculo"):        # limpa tambem o que ja estava em cache
                if reg.get(campo):
                    reg[campo] = limpar(str(reg[campo]))
            reg["sinteses"] = "; ".join(achados[doi])
            reg["eixos"] = eixos(reg)
            reg["atribuicao"] = ("CONFERIR ({:.2f})".format(pior[doi]) if doi in pior
                                 else "casa" if reg.get("situacao", "").startswith("CONFIRMADO")
                                 else "")
            if doi in NAO_EXISTEM:
                reg["detalhe"] = NAO_EXISTEM[doi]
            w.writerow(reg)

    conta = {}
    for doi in achados:
        s = cache.get(doi, {}).get("situacao", "NAO CONSULTADO")
        conta[s] = conta.get(s, 0) + 1
    print("\n--- eixo 1: o DOI existe? ---")
    for s, n in sorted(conta.items(), key=lambda kv: -kv[1]):
        print("  {:<22} {}".format(s, n))

    rot = {}
    for doi in achados:
        reg = cache.get(doi, {})
        if reg.get("situacao", "").startswith("CONFIRMADO"):
            k = eixos(reg) or "(sem termo)"
            rot[k] = rot.get(k, 0) + 1
    print("--- eixos temáticos (ordenação mecânica, não triagem) ---")
    for k, n in sorted(rot.items(), key=lambda kv: -kv[1]):
        print("  {:<24} {}".format(k, n))

    print("--- eixo 2: o título registrado casa com o que a síntese declara? ---")
    print("  {} menções casam · {} a conferir".format(len(mencoes) - len(duvidas), len(duvidas)))
    for taxa, doi, sintese, janela in duvidas:
        reg = cache[doi]
        print("\n  [{:.2f}] {}  ({})".format(taxa, doi, sintese))
        print("    registrado: {} — {}".format(reg["titulo"][:110], reg.get("ano", "")))
        print("    na síntese: ...{}".format(janela[-160:].strip()))

    ruins = [d for d in sorted(achados)
             if cache.get(d, {}).get("situacao") in ("NAO ENCONTRADO", "ERRO")]
    if ruins:
        print("\n--- recusados pelas duas agências ---")
        for d in ruins:
            reg = cache.get(d, {})
            print("  {}  [{}]  — em {}".format(d, reg.get("situacao", "?"), "; ".join(achados[d])))
            print("     {}".format(NAO_EXISTEM.get(d, reg.get("detalhe", ""))))

    print("\nplanilha: {}".format(CSV_OUT.relative_to(RAIZ)))
    return 1 if conta.get("ERRO") else 0


if __name__ == "__main__":
    sys.exit(main() or 0)
