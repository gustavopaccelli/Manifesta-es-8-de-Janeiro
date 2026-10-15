# -*- coding: utf-8 -*-
"""A seção 'Ordem de ataque' de docs/PENDENCIAS-ANALITICAS.md, GERADA.

Fonte da verdade: `data/ordem_de_ataque.json`. Esta peça não decide nada — não
abre, não fecha e não ordena tarefa. Ela faz três coisas que a mão fazia mal:

1. **A seção em que a tarefa aparece é consequência do campo `estado`**, não de
   alguém lembrar de mover a linha. A 15 ficou listada como aberta dois dias
   depois de executada.
2. **Toda contagem sai de medição.** As da camada A vêm de
   `localizar_camada_a.py` (mesma função `estado()` do script que já gerava
   aquela linha); as de corpus vêm de `Fontes/MANIFESTO-CORPUS.csv`. A linha da
   17 declarava "números gerados" e carregava uma cifra de 30/09.
3. **A frase que conta as abertas é derivada da tabela.** Ela já dissera "seis"
   com cinco linhas.

**O que NÃO é medido fica declarado como não medido.** Cifra apurada uma vez,
por tentativa de rede ou leitura — quantas peças estão barradas no cliente, por
exemplo — vive em `medidos_a_mao`, e o bloco gerado imprime a data de cada uma.
Número à mão não desaparece por decreto: ou se mede, ou se datilografa a data
ao lado dele.

Uso:
    python scripts/gerar_ordem_de_ataque.py              # gera e grava
    python scripts/gerar_ordem_de_ataque.py --chaves     # lista as chaves
    python scripts/gerar_ordem_de_ataque.py --autoteste  # provas, sem gravar
"""
import csv
import io
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))

AGENDA = RAIZ / "docs/PENDENCIAS-ANALITICAS.md"
LEDGER = RAIZ / "data/ordem_de_ataque.json"
MANIFESTO = RAIZ / "Fontes/MANIFESTO-CORPUS.csv"

ABRE = ("<!-- ORDEM-DE-ATAQUE: gerado por scripts/gerar_ordem_de_ataque.py a partir "
        "de data/ordem_de_ataque.json. Não editar à mão: o ciclo sobrescreve. -->")
FECHA = "<!-- /ORDEM-DE-ATAQUE -->"

CHAVE = re.compile(r"\{\{(\w+)\}\}")
PALAVRA = {0: "nenhuma", 1: "uma", 2: "duas", 3: "três", 4: "quatro", 5: "cinco",
           6: "seis", 7: "sete", 8: "oito", 9: "nove", 10: "dez", 11: "onze",
           12: "doze", 13: "treze", 14: "catorze", 15: "quinze", 16: "dezesseis",
           17: "dezessete", 18: "dezoito", 19: "dezenove", 20: "vinte"}


def mil(n):
    """1832 -> '1.832'. O separador do projeto é o ponto."""
    return "{:,}".format(int(n)).replace(",", ".")


def ledger():
    return json.loads(io.open(LEDGER, encoding="utf-8").read())


# --------------------------------------------------------------- medidas ---
def medir_camada_a():
    """Conta os 43 da camada A por estado de leitura, sem rede.

    Importa `localizar_camada_a` em vez de reimplementar: é o mesmo
    `estado()` que gera a planilha, e duas contagens do mesmo universo por
    dois códigos diferentes é como a cifra errada entra."""
    import localizar_camada_a as camada_a

    linhas = camada_a.carregar()
    por_estado = {}
    for r in linhas:
        por_estado[camada_a.estado(r["doi"])] = por_estado.get(camada_a.estado(r["doi"]), 0) + 1
    pend = [r for r in linhas if camada_a.estado(r["doi"]) == "PENDENTE"]
    return {
        "camada_a_total": len(linhas),
        "camada_a_lidos": por_estado.get("LIDO", 0),
        "camada_a_fichas": por_estado.get("FICHA", 0),
        "camada_a_impedidos": por_estado.get("IMPEDIDO", 0),
        "camada_a_pendentes": por_estado.get("PENDENTE", 0),
        "camada_a_mobilization": sum(1 for r in pend if "Mobilization" in r["veiculo"]),
    }


def medir_corpus(lidas_por_eixo):
    """Peças e páginas por eixo, do manifesto — que é o que a checagem 8 confere.

    Onde o ledger nomeia as peças já lidas, mede também o que falta: contar
    "faltam quinze" à mão é como a linha da 17 envelheceu."""
    with io.open(MANIFESTO, encoding="utf-8-sig") as f:
        linhas = list(csv.DictReader(f))
    assert linhas, "manifesto vazio: rode gerar_manifesto_corpus.py"

    def paginas(itens):
        return sum(int(x["paginas"]) for x in itens)

    out = {}
    for chave, eixo in (("eixo13", "13_Bolsonarismo-mobilizacao"),
                        ("eixo14", "14_Livros-brasileiros")):
        peças = [x for x in linhas if x["eixo"] == eixo]
        assert peças, "eixo sem peça no manifesto: " + eixo
        out[chave + "_arquivos"] = len(peças)
        out[chave + "_paginas"] = mil(paginas(peças))

        # Cada fragmento declarado tem de casar com UMA peça. Fragmento que não
        # casa é peça renomeada — e aí a conta do que falta estaria errada em
        # silêncio, que é o defeito que este script existe para matar.
        lidas = []
        for frag in lidas_por_eixo.get(eixo, []):
            casa = [x for x in peças if frag in x["caminho"]]
            assert len(casa) == 1, \
                "o fragmento {!r} casa com {} peças do eixo {}".format(
                    frag, len(casa), eixo)
            lidas.append(casa[0])
        if lidas_por_eixo.get(eixo) is not None:
            restam = [x for x in peças if x not in lidas]
            out[chave + "_lidas"] = len(lidas)
            out[chave + "_lidas_palavra"] = PALAVRA.get(len(lidas), str(len(lidas)))
            out[chave + "_faltam"] = len(restam)
            out[chave + "_faltam_palavra"] = PALAVRA.get(len(restam), str(len(restam)))
            out[chave + "_faltam_paginas"] = mil(paginas(restam))
    return out


def medir(d):
    """Todas as chaves disponíveis para `{{...}}`, com a procedência de cada uma."""
    abertas = [x for x in d["tarefas"] if x["estado"] == "aberta"]
    fechadas = [x for x in d["tarefas"] if x["estado"] == "fechada"]

    # A frase de natureza, derivada da tabela: agrupa na ordem em que a
    # natureza aparece, nunca na ordem alfabética, para que o texto não se
    # reembaralhe a cada geração.
    grupos = []
    for x in abertas:
        for g in grupos:
            if g[0] == x["natureza"]:
                g[1].append(x["n"])
                break
        else:
            grupos.append([x["natureza"], [x["n"]]])
    partes = ["{} (**{}**)".format(nat, ", ".join(ns)) for nat, ns in grupos]
    frase = partes[0] if len(partes) == 1 else \
        ", ".join(partes[:-1]) + " e " + partes[-1]

    chaves = {
        "abertas": str(len(abertas)),
        "abertas_palavra": PALAVRA[len(abertas)],
        "fechadas": str(len(fechadas)),
        "fechadas_palavra": PALAVRA.get(len(fechadas), str(len(fechadas))),
        "abertas_natureza": frase,
    }
    chaves.update(medir_camada_a())
    chaves.update(medir_corpus(d.get("lidas", {})))
    for k, v in d.get("medidos_a_mao", {}).items():
        chaves[k] = str(v["valor"])
    return {k: str(v) for k, v in chaves.items()}


def preencher(texto, chaves, usadas=None):
    """Troca {{chave}} pelo valor medido.

    `{{Chave}}` com maiúscula inicial devolve o valor capitalizado — é o que
    permite começar frase com número escrito ("**Três foram lidas**") sem
    guardar a palavra duas vezes no ledger."""
    def troca(m):
        k = m.group(1)
        baixa = k[0].lower() + k[1:]
        if k in chaves:
            achada, valor = k, chaves[k]
        elif k[0].isupper() and baixa in chaves:
            achada, valor = baixa, chaves[baixa][:1].upper() + chaves[baixa][1:]
        else:
            raise KeyError("chave desconhecida em texto do ledger: {{" + k + "}}")
        if usadas is not None:
            usadas.add(achada)
        return valor
    return CHAVE.sub(troca, texto)


# ----------------------------------------------------------------- bloco ---
def linha(x, coluna_final):
    return "| {} | {} | {} | {} |".format(x["n"], x["texto"], x["itens"],
                                          x[coluna_final])


def montar(d):
    chaves, usadas = medir(d), set()

    def p(txt):
        return preencher(txt, chaves, usadas)

    out = ["## Ordem de ataque — revista em " + d["revisada"], ""]
    for par in d["antes"]:
        out += [p(par), ""]

    for titulo, estado, cab, col in (("### Fechadas", "fechada", "Quando", "quando"),
                                     ("### Abertas", "aberta", "Depende de", "depende")):
        out += [titulo, "",
                "| # | Tarefa | Item desta agenda | {} |".format(cab),
                "|:--|:--|:--|:--|"]
        out += [p(linha(x, col)) for x in d["tarefas"] if x["estado"] == estado]
        out += [""]

    for par in d["depois"]:
        out += [p(par), ""]

    # As cifras que não se medem entram com a data em que foram medidas. É o
    # contrário de esconder: a linha existe para que a próxima rodada veja a
    # idade do número sem precisar escavar o item que o produziu.
    mao = d.get("medidos_a_mao", {})
    citadas = {k: v for k, v in mao.items() if k in usadas}
    if citadas:
        itens = ["**{}** — {} (medido em {}, {})".format(
            v["valor"], v["o_que"], v["medido_em"], v["fonte"])
            for k, v in sorted(citadas.items())]
        out += ["> **Cifras desta seção que não são medidas a cada ciclo:** "
                + "; ".join(itens) + ". Todo o resto sai de medição na geração.", ""]

    return "\n".join(out).rstrip("\n")


def gravar(bloco):
    t = io.open(AGENDA, encoding="utf-8").read()
    assert t.count(ABRE) == 1 and t.count(FECHA) == 1, \
        "os marcadores de bloco não estão exatamente uma vez em " + AGENDA.name
    cabeca, resto = t.split(ABRE, 1)
    _, cauda = resto.split(FECHA, 1)
    novo = cabeca + ABRE + "\n\n" + bloco + "\n\n" + FECHA + cauda

    # Prova de contenção: fora dos marcadores, nada muda. Um gerador que
    # escreve num arquivo de 2.300 linhas escritas à mão precisa provar isso.
    assert novo.split(ABRE, 1)[0] == cabeca
    assert novo.split(FECHA, 1)[1] == cauda
    if novo == t:
        print("ordem de ataque: já em dia, nada a gravar")
        return False
    io.open(AGENDA, "w", encoding="utf-8", newline="\n").write(novo)
    return True


# -------------------------------------------------------------- autoteste ---
def autoteste():
    d = ledger()

    numeradas = [x["n"] for x in d["tarefas"] if x["n"] != "—"]
    assert len(numeradas) == len(set(numeradas)), \
        "número de tarefa repetido no ledger: " + str(sorted(numeradas))
    for x in d["tarefas"]:
        assert x["estado"] in ("aberta", "fechada"), x
        if x["estado"] == "fechada":
            assert x["quando"].startswith("✅"), "fechada sem data: " + x["n"]
            assert "depende" not in x, "fechada com dependência: " + x["n"]
        else:
            assert x.get("natureza") and x.get("depende"), \
                "aberta sem natureza ou sem dependência: " + x["n"]
    for v in d.get("medidos_a_mao", {}).values():
        for campo in ("valor", "o_que", "medido_em", "fonte"):
            assert campo in v, "medido_a_mao sem " + campo

    chaves = medir(d)
    assert chaves["camada_a_total"] == "43", chaves["camada_a_total"]
    soma = sum(int(chaves["camada_a_" + k])
               for k in ("lidos", "fichas", "impedidos", "pendentes"))
    assert soma == 43, "os quatro estados da camada A não somam 43: " + str(soma)

    # Prova negativa 1: chave inexistente aborta, em vez de sair no texto.
    try:
        preencher("{{nao_existe}}", chaves)
        raise AssertionError("chave desconhecida passou sem erro")
    except KeyError:
        pass

    # Prova negativa 2: fechar uma tarefa muda a contagem e a frase de natureza
    # — é o defeito de 15/10, e ele agora não sobrevive à geração.
    copia = json.loads(json.dumps(d))
    viva = next(x for x in copia["tarefas"] if x["estado"] == "aberta")
    viva.update(estado="fechada", quando="✅ 99/99")
    del viva["depende"]
    depois = medir(copia)
    assert depois["abertas"] == str(int(chaves["abertas"]) - 1), "a contagem não seguiu o estado"
    assert viva["n"] not in depois["abertas_natureza"], \
        "a frase de natureza continua citando tarefa fechada"

    # Prova negativa 3: número repetido é pego — foi o defeito de 29/09, a
    # tarefa 18 listada duas vezes.
    ns = [x["n"] for x in d["tarefas"] if x["n"] != "—"] + [d["tarefas"][0]["n"]]
    assert len(ns) != len(set(ns)), "a duplicata plantada não foi detectada"

    bloco = montar(d)
    assert bloco.startswith("## Ordem de ataque — revista em ")
    assert "### Fechadas" in bloco and "### Abertas" in bloco
    assert "{{" not in bloco, "sobrou chave não substituída no bloco"
    assert bloco.count("\n| ") >= len(d["tarefas"]), "linha de tarefa perdida"
    print("autoteste OK — ledger íntegro, 43 na camada A, três provas negativas")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    if arg == "--autoteste":
        autoteste()
    elif arg == "--chaves":
        for k, v in sorted(medir(ledger()).items()):
            print("  {{%s}}  ->  %s" % (k, v))
    else:
        autoteste()
        if gravar(montar(ledger())):
            print("ordem de ataque: seção regravada em docs/PENDENCIAS-ANALITICAS.md")
