# -*- coding: utf-8 -*-
"""AUDITORIA DE USO UNICO -- as razoes impressas do corpus documental.

29/10/2026, item 105. Encaminhamento: *"A varredura das razoes impressas no
corpus [...] Resolva isso."*

O QUE ELA PERGUNTA. Para cada percentual impresso numa folha, existe um inteiro
na peca cuja divisao o reproduz? E, quando o percentual traz ROTULO DE BASE, a
base que o reproduz e a que o rotulo nomeia? A segunda pergunta e a que pegou o
defeito do balanco do Gabinete: a folha 9 fixa `total de reus 1402` e as quatro
porcentagens de sancao casam ao centesimo; as folhas 10-11 imprimem `10,12% do
total de reus` para 190 presos, e 190/1402 = 13,55% -- a conta so fecha com
1.878, que e o numero de INVESTIGACOES INSTAURADAS da folha 4.

POR QUE ELA NAO VIROU GUARDA DO CICLO, e as tres razoes sao medidas:

  (1) A BUSCA BRUTA E MA GUARDA. No balanco, 477 percentuais impressos contra
      125 inteiros candidatos: 454 "resolvem" -- quase todo percentual acha um
      divisor por acidente. Os denominadores mais frequentes que a busca
      devolve sao 9605 e 500, noventa vezes cada, e a lista traz 4828, 4781 e
      4918, que sao NUMEROS DE INQUERITO. **Identificador nao e cifra.**

  (2) O SUBCONJUNTO ROTULADO E DOMINADO POR CITACAO EXTERNA. Dos 1.056
      percentuais do corpus documental, 236 trazem rotulo de base -- e os
      rotulos mais frequentes sao `dos casos`, `dos votos`, `do PIB`, `das
      acoes da Positivo`. Nos acordaos, o percentual cita ESTUDO DE TERCEIRO,
      e nao ha contagem da propria peca para recalcular.

  (3) A CLASSE DE PECA ONDE A PERGUNTA SE APLICA TEM UM MEMBRO. Densidade de
      percentual por folha-com-percentual: balanco do Gabinete **22,7**; a
      peca seguinte, o acordao da ADC 43/44/54, **7,0** -- e os 182 dela sao
      citacao criminologica. **O corpus tem uma peca que e relatorio
      estatistico das PROPRIAS contagens, e o defeito dela ja esta declarado**
      em PT-61 e no item 101.

  Guarda cuja unica ocorrencia viva ja esta declarada e dispensa que ninguem
  revisita -- a licao do item 92. Por isso esta peca e AUDITORIA DATADA, roda
  sob demanda, e vive em `scripts/historico/`.

O GATILHO PARA RODA-LA DE NOVO, declarado: quando entrar no corpus uma peca com
**densidade alta de percentual** -- muitos percentuais em poucas folhas, a
assinatura de relatorio estatistico -- rode isto nela. A densidade sai do
primeiro passo e nao precisa de julgamento.

Uso:  python scripts/historico/auditar_razoes_2026-10-29.py [peca.pdf ...]
      sem argumento, varre os PDFs documentais do manifesto.
"""

import csv
import io
import re
import sys
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
MANIFESTO = RAIZ / "Fontes/MANIFESTO-CORPUS.csv"

PCT = re.compile(r"\b(\d{1,3}(?:[.,]\d{1,2})?)\s?%")
ROT = re.compile(r"(\d{1,3}(?:[.,]\d{1,2})?)\s?%\s*(?:do|da|dos|das)\s+"
                 r"([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ ]{2,38})")
INT = re.compile(r"\b(\d{1,3}(?:\.\d{3})+|\d{2,4})\b")


def pecas():
    with io.open(str(MANIFESTO), encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            if (r["caminho"].lower().endswith(".pdf")
                    and r["documental"].strip().lower() == "sim"):
                yield RAIZ / r["caminho"]


def audita(caminho):
    import pymupdf
    d = pymupdf.open(str(caminho))
    folhas, inteiros = {}, set()
    for i in range(d.page_count):
        t = d[i].get_text()
        if PCT.search(t):
            folhas[i + 1] = " ".join(t.split())
        for m in INT.findall(t):
            inteiros.add(int(m.replace(".", "")))
    pcts = [(n, p) for n, t in folhas.items() for p in PCT.findall(t)]
    rots = [(n, p, " ".join(r.split()[:4]))
            for n, t in folhas.items() for p, r in ROT.findall(t)]
    denoms = Counter()
    orfaos = []
    for n, p in pcts:
        alvo = float(p.replace(",", "."))
        achou = False
        for num in inteiros:
            for base in inteiros:
                if base <= num or base < 10:
                    continue
                if abs(num / base * 100 - alvo) < 0.005:
                    denoms[base] += 1
                    achou = True
                    break
            if achou:
                break
        if not achou:
            orfaos.append((n, p))
    dens = len(pcts) / max(len(folhas), 1)
    return {"folhas_com_pct": len(folhas), "pcts": len(pcts),
            "densidade": dens, "rotulados": len(rots),
            "inteiros": len(inteiros), "orfaos": orfaos, "denoms": denoms}


def main():
    alvos = [Path(a) for a in sys.argv[1:]] or list(pecas())
    print("AUDITORIA DAS RAZOES IMPRESSAS -- %d peca(s)" % len(alvos))
    print("=" * 78)
    print("%-46s %6s %6s %7s %6s" % ("peca", "f./%", "n. %", "dens.", "rot."))
    altas = []
    for cam in alvos:
        r = audita(cam)
        if not r["pcts"]:
            continue
        print("%-46s %6d %6d %7.1f %6d"
              % (cam.name[:46], r["folhas_com_pct"], r["pcts"],
                 r["densidade"], r["rotulados"]))
        if r["densidade"] >= 10:
            altas.append((cam, r))
    print()
    if not altas:
        print("Nenhuma peca com densidade >= 10 por folha: nenhuma e relatorio")
        print("estatistico das proprias contagens, e nao ha razao a recalcular.")
        return 0
    for cam, r in altas:
        print("=" * 78)
        print("DENSIDADE ALTA: %s" % cam.name)
        print("  %d inteiros candidatos na peca -- com tantos, a busca bruta"
              % r["inteiros"])
        print("  resolve por acidente; o que vale e o HISTOGRAMA de denominador:")
        for b, n in r["denoms"].most_common(8):
            print("     %8d  %3d vezes" % (b, n))
        print("  orfaos: %d" % len(r["orfaos"]))
        print()
        print("  LEIA ASSIM: dois denominadores frequentes com o MESMO rotulo")
        print("  na peca sao o defeito. Confira o rotulo folha a folha.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
