#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
`11_HIPOTESES-RIVAIS-PT-28.md` contra o codebook — registros e páginas.

O documento 11 é peça escrita à mão que cita registros do codebook e páginas de
fonte primária. Pela regra de 25/09/2026 — "toda peça escrita à mão que
reproduz números do codebook precisa ou virar gerada, ou ganhar uma checagem no
ciclo" —, esta é a checagem dele.

POR QUE ELA EXISTE, e o caso é da própria redação do documento. Na primeira
versão, duas citações foram escritas por dedução em vez de leitura: PT-20 saiu
como "CPMI: 631" quando o registro ancora **576**, e PT-21 como "CPMI: 640"
quando ancora **576, 374, 637, 643**. As duas páginas eram plausíveis — vizinhas
das corretas, na seção certa do relatório — e é exatamente por isso que
passariam. É o modo de falha do projeto na sua forma mais banal: **a cifra
correta no referente errado, produzida por inferência de vizinhança.**

O QUE ELA CONFERE. Cada linha de tabela do documento no formato

    | PT-xx | qualquer texto | CPMI: 646 |

é lida como uma asserção de que aquele registro existe e que **cada página
citada consta do `fonte_pagina` daquele registro**. O rótulo antes dos dois
pontos identifica o documento-fonte, e tem de bater com o do registro:
`fonte_pagina` guarda "CPMI: 646, 711 | Cappelli: 55, 57", e citar
"Cappelli: 646" seria pegar a página certa no documento errado.

O QUE ELA NÃO CONFERE. Não abre PDF — quem faz isso é `conferir_paginas.py`, e
é ele que garante que a página contenha o texto. Aqui a pergunta é anterior: se
a página citada no documento é a que o codebook ancora.

Uso:  python scripts/conferir_hipoteses.py
"""
import io
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parent.parent
JSON_IN = RAIZ / "process_tracing_8jan_eventos.json"

# Um documento por peça escrita à mão que cita registro e página em tabela. O 12
# entrou em 04/10/2026 com a tarefa 14, e a checagem valeu de imediato: a mesma
# ferramenta, o mesmo formato de tabela, zero código novo.
DOCS = [
    RAIZ / "projeto-pos-doc/11_HIPOTESES-RIVAIS-PT-28.md",
    RAIZ / "projeto-pos-doc/12_CAMADA-T-1-CONJUNTURAL.md",
]

# | PT-xx | ... | Rotulo: 123, 456 |  — a última célula é a das páginas
LINHA = re.compile(r"^\|\s*(PT-[0-9]+[A-Z]?)\s*\|.*\|\s*([^|]*?)\s*\|\s*$")
CITACAO = re.compile(r"([A-Za-zÀ-ÿ' 0-9.]+?):\s*([0-9,\s-]+)")


def paginas_do_registro(fonte_pagina):
    """"CPMI: 646, 711 | Cappelli: 55, 57" -> {"cpmi": {646, 711}, ...}

    Intervalo "495-496" entra como os dois extremos e como a cadeia crua, para
    que tanto "495" quanto "495-496" sejam aceitos."""
    fora = {}
    for bloco in (fonte_pagina or "").split("|"):
        m = CITACAO.search(bloco)
        if not m:
            continue
        rotulo = m.group(1).strip().lower()
        paginas = set()
        for p in m.group(2).split(","):
            p = p.strip()
            if not p:
                continue
            paginas.add(p)
            if "-" in p:
                a, _, b = p.partition("-")
                paginas.update({a.strip(), b.strip()})
        fora.setdefault(rotulo, set()).update(paginas)
    return fora


def main():
    with io.open(JSON_IN, encoding="utf-8") as f:
        por_id = {r["id"]: r for r in json.load(f)["eventos"]}

    falhas, conferidas = [], 0
    for doc in DOCS:
        if not doc.exists():
            print("ABORTA: {} nao existe".format(doc.relative_to(RAIZ)))
            return 1
        for n, linha in enumerate(io.open(doc, encoding="utf-8"), 1):
            m = LINHA.match(linha.rstrip("\n"))
            if not m:
                continue
            rid, celula = m.group(1), m.group(2)
            onde = "{} l.{}".format(doc.name, n)
            reg = por_id.get(rid)
            if reg is None:
                falhas.append("{}: registro {} nao existe no codebook".format(onde, rid))
                continue
            ancorado = paginas_do_registro(reg.get("fonte_pagina"))
            citou = False
            for cm in CITACAO.finditer(celula):
                rotulo = cm.group(1).strip().lower()
                if rotulo not in ancorado:
                    falhas.append("{}: {} cita '{}', e o registro ancora {}".format(
                        onde, rid, cm.group(1).strip(), sorted(ancorado) or "nada"))
                    citou = True
                    continue
                for p in cm.group(2).split(","):
                    p = p.strip()
                    if not p:
                        continue
                    citou = True
                    conferidas += 1
                    if p not in ancorado[rotulo]:
                        falhas.append("{}: {} cita {} p. {}, e o registro ancora {}".format(
                            onde, rid, cm.group(1).strip(), p,
                            ", ".join(sorted(ancorado[rotulo]))))
            if not citou:
                falhas.append("{}: {} aparece em tabela sem citar pagina".format(onde, rid))

    print("=" * 74)
    print("{} x codebook — {} citações de página".format(
        " + ".join(d.name for d in DOCS), conferidas))
    print("=" * 74)
    if falhas:
        for f in falhas:
            print("  FALHA  " + f)
        print()
        print("{} divergência(s). O documento cita página que o registro não ancora.".format(
            len(falhas)))
        return 1
    if conferidas == 0:
        print("  FALHA  nenhuma citação encontrada — o parser ou o documento mudou")
        return 1
    print("  OK — toda página citada no documento é ancorada pelo registro")
    return 0


if __name__ == "__main__":
    sys.exit(main())
