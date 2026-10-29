# -*- coding: utf-8 -*-
"""A TABELA DAS DIADES -- pares de registros que se opoem no mesmo processo.

POR QUE ISTO NAO E UM CAMPO NOVO, e a medicao decidiu: em 29/10/2026, **58 dos
87 registros ja remetiam a outro registro**, com 226 remissoes em quatro
campos. **A relacao ja esta no codebook.** O que faltava nao era um campo --
era TIPO e RECIPROCIDADE. Um 18o campo seria a quinta copia de uma relacao que
a prosa ja carrega, e abriria uma segunda decisao de esquema enquanto a
primeira, a grade funcional como 18o campo, segue aberta.

O MARCADOR: `DIADE: PT-XX` ou `DIADE: PT-XX, PT-YY` em `mecanismo_causal`.
Medido antes de escolher: `diade` tinha ZERO ocorrencias no codebook, e so um
marcador tipado existia (`REMISSAO`, em PT-62) -- o vocabulario estava livre.

O QUE A GUARDA PERGUNTA, e a segunda e a que importa:
  1. o id apontado existe? (a checagem 6 ja faz isso para remissao solta)
  2. **a declaracao e RECIPROCA?** Se A declara diade com B, B tem de declarar
     com A. Ponteiro so confere existencia; **reciprocidade confere que a
     relacao foi pensada dos dois lados** -- e e isso que separa `vide tambem`
     de uma afirmacao sobre a estrutura do conflito.

DOIS SENTIDOS DE `DIADE` NO MESMO APARATO, e a distincao fica escrita porque
confundi-los seria facil:
  - A diade DESTE arquivo e INTER-REGISTRO: dois registros, dois campos, um
    processo.
  - A diade da GRADE FUNCIONAL e INTRA-REGISTRO: um registro cujo
    `framing_narrativa` carrega dois quadros em disputa, como PT-03D --
    `'Ninguem esta acima da lei' x 'preso politico'`. O conjunto MISTO daquele
    script se chama `campos opostos` e tem UM registro.
  **PT-03D nao recebe marcador, e nao e omissao: e outra coisa.**

A TEORIA que autoriza a tabela e o verbete `Movement/countermovement dynamics`
(Dillard, Wiley-Blackwell Encyclopedia 2013, f. 391-393), lido em 29/10/2026:
`Movement/countermovement dynamics refers to the patterns of interaction
between the originating social movement and the responding countermovement`.

Emite:  reports/TABELA-DIADES.md

Uso:  python scripts/gerar_diades.py [--autoteste]
"""

import copy
import io
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"
SAIDA = RAIZ / "reports/TABELA-DIADES.md"

# `DIADE:` com ou sem acento, seguido de um ou mais ids separados por virgula.
MARCA = re.compile(r"D[IÍ]ADE\s*:\s*((?:PT-\d{1,2}[A-E]?(?:\s*,\s*)?)+)",
                   re.IGNORECASE)
ID = re.compile(r"PT-\d{1,2}[A-E]?")


def declaradas(dados):
    """{id: [ids declarados]} a partir de `mecanismo_causal`.

    UM CAMPO SO, de proposito. Espalhar o marcador por quatro campos daria a
    mesma ambiguidade que a remissao solta tem hoje -- e o campo analitico e
    onde a afirmacao sobre o mecanismo vive.
    """
    out = {}
    for ev in dados["eventos"]:
        achados = []
        for m in MARCA.finditer(ev.get("mecanismo_causal") or ""):
            achados.extend(ID.findall(m.group(1)))
        if achados:
            # dedup preservando a ordem de escrita
            vistos, lim = set(), []
            for x in achados:
                if x not in vistos:
                    vistos.add(x)
                    lim.append(x)
            out[ev["id"]] = lim
    return out


def guarda(dados, falar=True):
    """Devolve (pares, falhas). Pares sao tuplas ordenadas, sem repeticao."""
    ids = {ev["id"] for ev in dados["eventos"]}
    decl = declaradas(dados)
    falhas = []

    for a, alvos in sorted(decl.items()):
        for b in alvos:
            if b not in ids:
                falhas.append("%s declara díade com %s, que não existe" % (a, b))
                continue
            if b == a:
                falhas.append("%s declara díade consigo mesmo" % a)
                continue
            # RECIPROCIDADE
            if a not in decl.get(b, []):
                falhas.append(
                    "díade não recíproca: %s declara %s, e %s não declara %s"
                    % (a, b, b, a))

    pares = sorted({tuple(sorted((a, b))) for a, alvos in decl.items()
                    for b in alvos if b in ids and b != a})
    if falar:
        print("  registros com díade declarada : %d" % len(decl))
        print("  pares                         : %d" % len(pares))
        for f in falhas:
            print("    X " + f)
        if not falhas:
            print("  OK — todo id existe e toda díade é recíproca")
    return pares, falhas


def montar(dados, pares):
    reg = {ev["id"]: ev for ev in dados["eventos"]}

    def cel(s, n=78):
        s = " ".join((s or "—").split())
        return (s[:n] + "…") if len(s) > n else s

    w = []
    w.append("<!-- GERADO por scripts/gerar_diades.py. Não editar à mão: "
             "o ciclo sobrescreve. -->")
    w.append("")
    w.append("# As díades do processo — pares de registros que se opõem")
    w.append("")
    w.append("**O que esta tabela é.** Cada linha é um **par de registros que "
             "o codebook declara em díade** — dois campos interagindo dentro "
             "do mesmo processo. A declaração vive no marcador `DÍADE: PT-XX` "
             "do campo `mecanismo_causal`, e **é recíproca por guarda**: se um "
             "declara, o outro tem de declarar.")
    w.append("")
    w.append("**Por que não é um campo do esquema.** Em 29/10/2026, **58 dos "
             "87 registros já remetiam a outro registro**, com 226 remissões "
             "em quatro campos — a relação já estava no codebook, e o que "
             "faltava era **tipo e reciprocidade**, não um campo.")
    w.append("")
    w.append("**A teoria.** O verbete *Movement/countermovement dynamics* "
             "(Dillard, *Wiley-Blackwell Encyclopedia*, 2013, f. 391-393), "
             "lido em 29/10/2026: a dinâmica é o padrão de interação entre o "
             "movimento que origina e o contramovimento que responde, e as "
             "**cinco dimensões de distinção** são objetivos, ideologia, "
             "táticas, composição e **posição na estrutura social**.")
    w.append("")
    w.append("> **Dois sentidos de `díade` no mesmo aparato, e eles não se "
             "confundem.** A díade **desta tabela é INTER-REGISTRO**: dois "
             "registros, dois campos. A díade da **grade funcional é "
             "INTRA-REGISTRO**: um registro cujo `framing_narrativa` carrega "
             "dois quadros em disputa — é o caso de **PT-03D**, e é por isso "
             "que ele **não** aparece aqui.")
    w.append("")
    w.append("**%d par(es) declarado(s).**" % len(pares))
    w.append("")
    for a, b in pares:
        ea, eb = reg[a], reg[b]
        w.append("## %s ↔ %s" % (a, b))
        w.append("")
        w.append("| | `%s` | `%s` |" % (a, b))
        w.append("|:--|:--|:--|")
        w.append("| **data** | %s | %s |" % (cel(ea["data_hora"], 44),
                                             cel(eb["data_hora"], 44)))
        w.append("| **fase** | %s | %s |" % (cel(ea["fase"], 44),
                                             cel(eb["fase"], 44)))
        w.append("| **ator** | %s | %s |" % (cel(ea["ator_grupo"]),
                                             cel(eb["ator_grupo"])))
        w.append("| **repertório** | %s | %s |" % (cel(ea["repertorio_acao"]),
                                                   cel(eb["repertorio_acao"])))
        w.append("| **enquadramento** | %s | %s |"
                 % (cel(ea["framing_narrativa"]), cel(eb["framing_narrativa"])))
        w.append("")
    w.append("> **A divergência não é declarada: ela é lida.** As linhas de "
             "ator, repertório e enquadramento vêm do codebook sem "
             "intermediação, e é nelas que as dimensões de Dillard aparecem. "
             "**A única afirmação nova desta tabela é o PAR** — e é por isso "
             "que o marcador carrega só os ids.")
    return "\n".join(w) + "\n"


def autoteste():
    dados = json.load(io.open(str(JSON_P), encoding="utf-8"))
    pares, falhas = guarda(dados, falar=False)
    assert not falhas, falhas
    assert pares, "nenhuma díade declarada — a tabela não tem o que dizer"

    # PROVA 1 — id que nao existe
    c = copy.deepcopy(dados)
    alvo = next(e for e in c["eventos"] if MARCA.search(e["mecanismo_causal"] or ""))
    alvo["mecanismo_causal"] = MARCA.sub("DÍADE: PT-99Z", alvo["mecanismo_causal"])
    _, f1 = guarda(c, falar=False)
    assert any("não existe" in x for x in f1), f1

    # PROVA 2 — declaracao nao reciproca: tira o marcador de UM lado do par
    c = copy.deepcopy(dados)
    a, b = pares[0]
    outro = next(e for e in c["eventos"] if e["id"] == b)
    outro["mecanismo_causal"] = MARCA.sub("", outro["mecanismo_causal"])
    _, f2 = guarda(c, falar=False)
    assert any("não recíproca" in x for x in f2), f2

    # PROVA 3 — diade consigo mesmo
    c = copy.deepcopy(dados)
    um = next(e for e in c["eventos"] if e["id"] == a)
    um["mecanismo_causal"] = MARCA.sub("DÍADE: %s" % a, um["mecanismo_causal"])
    _, f3 = guarda(c, falar=False)
    assert any("consigo mesmo" in x for x in f3), f3

    print("autoteste OK — %d par(es), reciprocidade conferida, três provas "
          "negativas" % len(pares))


def main():
    if "--autoteste" in sys.argv:
        autoteste()
        return 0
    dados = json.load(io.open(str(JSON_P), encoding="utf-8"))
    print("DÍADES DO PROCESSO")
    pares, falhas = guarda(dados)
    if falhas:
        print("  ! a tabela não foi gravada — conserte a declaração")
        return 1
    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    io.open(str(SAIDA), "w", encoding="utf-8", newline="\n").write(
        montar(dados, pares))
    print("  -> %s" % SAIDA.relative_to(RAIZ).as_posix())
    return 0


if __name__ == "__main__":
    sys.exit(main())
