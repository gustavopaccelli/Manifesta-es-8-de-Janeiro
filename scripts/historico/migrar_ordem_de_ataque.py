# -*- coding: utf-8 -*-
"""Migração de uso único — 15/10/2026: a 'Ordem de ataque' vira dado.

Lê a seção escrita à mão em `docs/PENDENCIAS-ANALITICAS.md` e a deposita em
`data/ordem_de_ataque.json`, que passa a ser a fonte da verdade da tabela.
Depois desta execução, quem gera a seção é `scripts/gerar_ordem_de_ataque.py`.

**Por que isto existe.** A tabela envelheceu três vezes em dezesseis dias — 18
duplicada, tarefas fechadas listadas como abertas, e uma cifra de 30/09 na
linha que declara os números como gerados. O conserto de 15/10 foi o terceiro
de contabilidade, e a peça já previa o próprio defeito: *"a contagem da 17 já é
gerada; o resto desta tabela não é, e é a próxima candidata a virar script"*.

**Não se reexecuta.** Como toda migração desta pasta, ela afirma por `assert` o
estado anterior — a seção escrita à mão, com 30 linhas fechadas e 5 abertas e
SEM os marcadores de bloco gerado. Depois de migrada, a seção tem marcadores e
esta varredura aborta.

**O que a migração NÃO faz:** não divide título e nota, não reordena, não
reescreve nenhuma célula. Cada linha entra como o texto que já era, para que a
primeira geração possa ser provada idêntica ao que estava no disco. Quem muda
texto é o pesquisador, no JSON, depois.
"""
import io
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

AGENDA = "docs/PENDENCIAS-ANALITICAS.md"
LEDGER = "data/ordem_de_ataque.json"
H = "## Ordem de ataque — revista em 15/10/2026"

t = io.open(AGENDA, encoding="utf-8").read()
assert t.count(H) == 1, "o cabeçalho de 15/10 não está no disco — já migrado?"
assert "ORDEM-DE-ATAQUE" not in t, "a seção já tem marcadores: migração já rodou"
assert not os.path.exists(LEDGER), "o ledger já existe: " + LEDGER

secao = t.split(H, 1)[1].split("\n> **As decisões suas que restam", 1)[0]


def celulas(linha):
    return [c.strip() for c in linha.strip().strip("|").split("|")]


def paragrafos(txt):
    return [p.strip() for p in txt.strip().split("\n\n") if p.strip()]


antes, resto = secao.split("### Fechadas", 1)
bruto_fechadas, resto = resto.split("### Abertas", 1)

linhas_abertas, depois = [], []
for p in paragrafos(resto):
    (linhas_abertas if p.startswith("|") else depois).append(p)
assert len(linhas_abertas) == 1, "a tabela de abertas não é um bloco único"

tarefas = []
for estado, bruto in (("fechada", bruto_fechadas), ("aberta", linhas_abertas[0])):
    corpo = [l for l in bruto.strip().splitlines() if l.startswith("|")]
    cab, sep, dados = corpo[0], corpo[1], corpo[2:]
    assert set(sep.replace("|", "").replace(":", "").replace("-", "").strip()) == set(), sep
    assert celulas(cab)[0] == "#", cab
    for l in dados:
        c = celulas(l)
        assert len(c) == 4, "linha com {} células: {}".format(len(c), l[:60])
        reg = {"n": c[0], "estado": estado, "texto": c[1], "itens": c[2]}
        if estado == "fechada":
            assert c[3].startswith("✅"), "linha fechada sem data: " + l[:60]
            reg["quando"] = c[3]
        else:
            reg["depende"] = c[3]
        tarefas.append(reg)

fech = [x for x in tarefas if x["estado"] == "fechada"]
abert = [x for x in tarefas if x["estado"] == "aberta"]
assert (len(fech), len(abert)) == (30, 5), (len(fech), len(abert))

# A natureza de cada aberta — é o que gera a frase de contagem, e é a única
# coisa que esta migração acrescenta, porque a frase antiga a dizia em prosa:
# "decisão sua (19), leitura ou entrega de arquivo (10, 17, 25) e a redação (16)".
NATUREZA = {"19": "decisão sua", "10": "leitura ou entrega de arquivo",
            "17": "leitura ou entrega de arquivo",
            "25": "leitura ou entrega de arquivo", "16": "a redação"}
for x in abert:
    assert x["n"] in NATUREZA, "aberta sem natureza declarada: " + x["n"]
    x["natureza"] = NATUREZA[x["n"]]

ledger = {
    "_leia_me": ("Fonte da verdade da seção 'Ordem de ataque' de "
                 "docs/PENDENCIAS-ANALITICAS.md. Edite AQUI; a seção é gerada por "
                 "scripts/gerar_ordem_de_ataque.py e sobrescrita a cada ciclo. "
                 "Em qualquer texto, {{chave}} é substituído por número medido — "
                 "`python scripts/gerar_ordem_de_ataque.py --chaves` lista as "
                 "disponíveis."),
    "revisada": "15/10/2026",
    "antes": paragrafos(antes),
    "tarefas": tarefas,
    "depois": depois,
    "medidos_a_mao": {},
}
io.open(LEDGER, "w", encoding="utf-8", newline="\n").write(
    json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")
print("ledger escrito: {} — {} fechadas, {} abertas, {} parágrafos de prosa".format(
    LEDGER, len(fech), len(abert), len(ledger["antes"]) + len(depois)))
