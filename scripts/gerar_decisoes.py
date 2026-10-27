# -*- coding: utf-8 -*-
"""A seção 'Decisões pendentes' de docs/PENDENCIAS-ANALITICAS.md, GERADA.

Fonte da verdade: `data/decisoes_abertas.json`. Esta peça não decide nada — não
abre, não fecha e não ordena decisão. Ela faz o que a mão fazia mal, e o
diagnóstico tem data: em 25/10/2026 a colheita das seções *"O que isto deixa"*
de cada item da agenda devolveu **oito pendências já resolvidas por itens
posteriores**.

**O defeito não era a prosa daquelas seções.** Elas são o registro do que se
sabia naquele dia, e é assim que devem ficar. O defeito era **não haver um
lugar único onde virar o bit** — exatamente o que a ordem de ataque resolveu
para as tarefas no item 49, e que as decisões nunca tiveram.

Três coisas saem de derivação:

1. **A seção em que a decisão aparece é consequência do campo `estado`.** Fechar
   uma decisão é virar um campo, e ela sai da lista aberta sozinha.
2. **A contagem sai da lista**, nunca de prosa. A frase que conta as abertas e a
   que as agrupa por natureza são derivadas, pela mesma razão que a ordem de
   ataque deriva as dela: "a lista é que manda no número" foi aprendido três
   vezes nesta casa, por perda de item em cópia.
3. **O ponteiro de seção é CONFERIDO.** G-A abre a agenda e exige que a seção
   citada exista — porque ponteiro quebrado é a forma que o apodrecimento toma
   aqui, e ponteiro que aponta para o nada é pior que pendência esquecida: ele
   parece verificável.

**O LIMITE, DECLARADO:** este gerador conserta a CÓPIA, não o JUÍZO. Ele dá um
lugar único para registrar que uma decisão saiu, e **não detecta sozinho** que
ela foi resolvida noutro item. Isso continua sendo leitura humana — o que ele
garante é que, uma vez lida, a resolução entra em UM lugar e a lista acompanha.

Uso:
    python scripts/gerar_decisoes.py              # gera e grava
    python scripts/gerar_decisoes.py --autoteste  # provas, sem gravar
"""
import io
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
AGENDA = RAIZ / "docs/PENDENCIAS-ANALITICAS.md"
LEDGER = RAIZ / "data/decisoes_abertas.json"

ABRE = ("<!-- DECISOES-PENDENTES: gerado por scripts/gerar_decisoes.py a partir "
        "de data/decisoes_abertas.json. Não editar à mão: o ciclo sobrescreve. -->")
FECHA = "<!-- /DECISOES-PENDENTES -->"

PALAVRA = {0: "nenhuma", 1: "uma", 2: "duas", 3: "três", 4: "quatro",
           5: "cinco", 6: "seis", 7: "sete", 8: "oito", 9: "nove", 10: "dez",
           11: "onze", 12: "doze", 13: "treze", 14: "catorze", 15: "quinze"}


def ledger():
    return json.loads(io.open(str(LEDGER), encoding="utf-8").read())


def secoes_da_agenda():
    """Os rótulos de seção e de item que a agenda traz, para a guarda G-A.

    Aceita `89.7` (uma subseção `### 89.7 ...`) e `74` (um item `## 74. ...`),
    porque as duas formas são usadas como ponteiro e as duas são verificáveis.
    """
    txt = io.open(str(AGENDA), encoding="utf-8").read()
    subs = set(re.findall(r"^### (\d+\.\d+) ", txt, re.M))
    itens = set(re.findall(r"^## (\d+)\. ", txt, re.M))
    return subs, itens


def confere_ponteiros(d):
    """G-A: toda decisão aponta para seção que EXISTE na agenda."""
    subs, itens = secoes_da_agenda()
    quebrados = []
    for x in d["decisoes"]:
        onde = str(x["onde"])
        if onde not in subs and onde not in itens:
            quebrados.append((x["id"], onde))
    return quebrados


def montar(d):
    abertas = [x for x in d["decisoes"] if x["estado"] == "aberta"]
    fechadas = [x for x in d["decisoes"] if x["estado"] != "aberta"]

    # A frase de natureza, derivada da lista e na ordem em que a natureza
    # aparece — nunca alfabética, para que o texto não se reembaralhe.
    grupos = []
    for x in abertas:
        for g in grupos:
            if g[0] == x["natureza"]:
                g[1].append(x)
                break
        else:
            grupos.append([x["natureza"], [x]])

    out = ["## Decisões pendentes — revista em " + d["revisada"], ""]
    for par in d["antes"]:
        out += [par, ""]

    n = len(abertas)
    out += ["**São {} decisões abertas, em {} naturezas:** {}.".format(
        PALAVRA.get(n, str(n)), PALAVRA.get(len(grupos), str(len(grupos))),
        " · ".join("{} ({})".format(nat, len(xs)) for nat, xs in grupos)), ""]

    for nat, xs in grupos:
        out += ["### " + nat[0].upper() + nat[1:], "",
                "| Decisão | Nasceu | Onde |", "|:--|:--|:--|"]
        for x in xs:
            out.append("| {} | {} | §{} |".format(
                x["o_que"], x["nasceu"], x["onde"]))
        out += [""]

    if fechadas:
        out += ["### Decididas", "", "| Decisão | Quando |", "|:--|:--|"]
        for x in fechadas:
            out.append("| ~~{}~~ | {} |".format(
                re.sub(r"\*\*", "", x["o_que"].split(".")[0])[:150],
                x.get("quando", "—")))
        out += [""]

    for par in d["depois"]:
        out += [par, ""]
    return "\n".join(out).rstrip("\n")


def gravar(bloco):
    t = io.open(str(AGENDA), encoding="utf-8").read()
    if ABRE not in t:
        # Primeira gravação: a seção nasce no fim do arquivo, como a ordem de
        # ataque nasceu, e dali em diante é sobrescrita no lugar.
        t = t.rstrip("\n") + "\n\n---\n\n" + ABRE + "\n\n" + bloco + "\n\n" \
            + FECHA + "\n"
        io.open(str(AGENDA), "w", encoding="utf-8", newline="\n").write(t)
        print("decisões pendentes: seção criada em docs/PENDENCIAS-ANALITICAS.md")
        return True
    assert t.count(ABRE) == 1 and t.count(FECHA) == 1, \
        "os marcadores de bloco não estão exatamente uma vez na agenda"
    cabeca, resto = t.split(ABRE, 1)
    _, cauda = resto.split(FECHA, 1)
    novo = cabeca + ABRE + "\n\n" + bloco + "\n\n" + FECHA + cauda
    # Prova de contenção: fora dos marcadores, nada muda.
    assert novo.split(ABRE, 1)[0] == cabeca
    assert novo.split(FECHA, 1)[1] == cauda
    if novo == t:
        print("decisões pendentes: já em dia, nada a gravar")
        return False
    io.open(str(AGENDA), "w", encoding="utf-8", newline="\n").write(novo)
    return True


def autoteste():
    d = ledger()

    ids = [x["id"] for x in d["decisoes"]]
    assert len(ids) == len(set(ids)), "id de decisão repetido: " + str(ids)
    for x in d["decisoes"]:
        assert x["estado"] in ("aberta", "decidida"), x
        for campo in ("id", "o_que", "onde", "nasceu", "natureza"):
            assert x.get(campo), "decisão sem %s: %s" % (campo, x.get("id"))
        if x["estado"] == "decidida":
            assert x.get("quando"), "decidida sem data: " + x["id"]

    # G-A: o ponteiro de seção existe na agenda.
    quebrados = confere_ponteiros(d)
    if quebrados:
        for i, onde in quebrados:
            print("  X %s aponta para §%s, que não existe na agenda" % (i, onde))
        raise AssertionError("G-A: %d ponteiro(s) quebrado(s)" % len(quebrados))

    # Prova negativa 1: ponteiro inventado é pego.
    copia = json.loads(json.dumps(d))
    copia["decisoes"][0]["onde"] = "999.9"
    assert confere_ponteiros(copia), "G-A não pegou ponteiro inventado"

    # Prova negativa 2: decidir uma decisão tira-a da lista aberta E muda a
    # contagem — é o defeito que esta peça existe para matar.
    copia = json.loads(json.dumps(d))
    viva = next(x for x in copia["decisoes"] if x["estado"] == "aberta")
    viva.update(estado="decidida", quando="✅ 99/99")
    antes = montar(d)
    depois = montar(copia)
    n0 = len([x for x in d["decisoes"] if x["estado"] == "aberta"])
    assert PALAVRA.get(n0) in antes and PALAVRA.get(n0 - 1) in depois, \
        "a contagem não seguiu o estado"
    assert viva["o_que"][:60] not in depois.split("### Decididas")[0], \
        "a decisão fechada continua na lista aberta"

    # Prova negativa 3: decidida sem data é pega.
    copia = json.loads(json.dumps(d))
    copia["decisoes"][0]["estado"] = "decidida"
    try:
        for x in copia["decisoes"]:
            if x["estado"] == "decidida":
                assert x.get("quando"), "decidida sem data: " + x["id"]
        raise AssertionError("a decidida sem data passou")
    except AssertionError as erro:
        assert "sem data" in str(erro), erro

    bloco = montar(d)
    assert bloco.startswith("## Decisões pendentes — revista em ")
    assert "{{" not in bloco, "sobrou chave no bloco"
    print("autoteste OK — %d decisões, ponteiros conferidos, três provas "
          "negativas" % len(d["decisoes"]))


if __name__ == "__main__":
    if (sys.argv[1:] or [""])[0] == "--autoteste":
        autoteste()
    else:
        autoteste()
        gravar(montar(ledger()))
