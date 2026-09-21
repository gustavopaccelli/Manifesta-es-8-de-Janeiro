#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Conferência amostral: a transcrição literal está mesmo na página citada?

Esta é a única checagem que abre o PDF e compara o texto. As demais verificam
estrutura — que o caminho existe, que a página pertence ao documento vinculado —
e por isso **não pegam um vínculo errado**: elas derivam o código do documento a
partir do próprio vínculo, e validam como coerente um vínculo que aponta para a
peça errada.

Foi assim que se descobriu, em 16/08/2026, que PT-28 citava "CPMI, p. 657" no
texto e apontava para o acórdão da AP 2668 no vínculo. Rode isto a cada rodada.

Uso:
    python scripts/conferir_paginas.py              # amostra de 12
    python scripts/conferir_paginas.py --todos      # os 61 com página
    python scripts/conferir_paginas.py PT-28 PT-31  # registros específicos
"""

import json
import random
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

try:
    from PyPDF2 import PdfReader
except ImportError:
    raise SystemExit("PyPDF2 ausente:  pip install PyPDF2")

ASPAS_ABRE = "\"“‘'"
ASPAS_FECHA = "\"”’'"
_cache = {}


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s).lower()


def texto_pagina(caminho, n):
    r = _cache.get(caminho)
    if r is None:
        r = _cache[caminho] = PdfReader(str(RAIZ / caminho))
    if n < 1 or n - 1 >= len(r.pages):
        return None
    return norm(r.pages[n - 1].extract_text() or "")


def pares(fonte_pagina):
    """'CPMI: 646, 711 | Cappelli: 55, 57' -> [('CPMI',[646,711]),('Cappelli',[55,57])]"""
    saida = []
    for seg in (fonte_pagina or "").split("|"):
        if ":" not in seg:
            continue
        cod, resto = seg.split(":", 1)
        nums = [int(x) for x in re.findall(r"\b(\d{1,4})\b", resto)]
        if nums:
            saida.append((cod.strip(), nums))
    return saida


APARATO = re.compile(r"^\s*[,;.)\]]|p\.\s*\d+\s*[;)]|oitiva de|apêndice", re.I)


def transcricoes(trecho):
    """Candidatos a transcrição literal dentro do texto de fonte_trecho.

    Não usar regex de par aberto-fecha: a aspa de fechamento de uma citação é
    consumida como delimitador e a citação SEGUINTE se perde. Foi o que produziu
    o falso positivo de PT-16, cujo fonte_trecho usa aspas simples para *títulos
    de seção* ('A radicalização do movimento') e não só para transcrições — o
    casamento pegou o intervalo entre dois títulos, que é aparato de referência.

    A abordagem aqui é grosseira de propósito: fatia em todo caractere de aspa,
    fica com os pedaços longos e descarta os que parecem aparato. Gerar
    candidato demais é barato; perder o candidato certo custa um falso alarme.
    """
    partes = re.split("[{}]".format(re.escape(ASPAS_ABRE + ASPAS_FECHA)), trecho or "")
    if len(partes) < 2:
        return []  # nenhuma aspa: é referência, não transcrição
    # Índices ímpares são o que está DENTRO de aspas; os pares são o aparato
    # entre elas. Sem essa distinção, um registro sem transcrição alguma teria
    # o próprio texto de referência tomado como citação a procurar no PDF.
    dentro = [p.strip() for i, p in enumerate(partes) if i % 2 == 1]
    return [p for p in dentro if len(p) >= 45 and not APARATO.search(p[:60])]


def casa(alvo, texto):
    """Procura janelas ao longo da citação, não só o início.

    Ancorar no começo produz falso negativo: hifenização e quebra de linha no
    PDF costumam atingir justamente as primeiras palavras. PT-31 foi um desses.
    """
    a = norm(alvo)
    for tam in (90, 60, 40):
        if len(a) < tam:
            continue
        for ini in range(0, max(1, len(a) - tam), max(1, tam // 2)):
            janela = a[ini:ini + tam]
            if janela in texto:
                return tam, ini
    return None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    todos = "--todos" in sys.argv

    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    docs = dados["metadados"]["registro_documentos"]
    eventos = {e["id"]: e for e in dados["eventos"]}

    cands = [e for e in dados["eventos"] if pares(e.get("fonte_pagina"))]
    if args:
        alvos = [eventos[a] for a in args if a in eventos]
    elif todos:
        alvos = cands
    else:
        random.seed(81)
        alvos = sorted(random.sample(cands, min(12, len(cands))), key=lambda e: e["id"])

    print("CONFERÊNCIA PÁGINA x TRANSCRIÇÃO — {} registro(s)".format(len(alvos)))
    print("=" * 78)
    ok = falha = indet = 0
    falhas = []

    for e in alvos:
        pp = pares(e.get("fonte_pagina"))
        if not pp:
            print("  {:<7} ~  sem página estruturada".format(e["id"]))
            indet += 1
            continue
        cod, nums = pp[0]
        caminho = docs.get(cod)
        if not caminho:
            print("  {:<7} ?  código de documento desconhecido: {}".format(e["id"], cod))
            indet += 1
            continue
        if not caminho.lower().endswith(".pdf"):
            print("  {:<7} ~  {} não é PDF, fora do alcance".format(e["id"], cod))
            indet += 1
            continue
        cits = transcricoes(e.get("fonte_trecho"))
        if not cits:
            print("  {:<7} ~  {} p.{} — referência sem transcrição literal".format(
                e["id"], cod, nums[0]))
            indet += 1
            continue

        achou = None
        for pg in nums:
            txt = texto_pagina(caminho, pg)
            if txt is None:
                continue
            for cit in cits:
                r = casa(cit, txt)
                if r:
                    achou = (pg, cit, r)
                    break
            if achou:
                break

        if achou:
            pg, cit, (tam, _) = achou
            print("  {:<7} OK {} p.{} «{}…»".format(e["id"], cod, pg, norm(cit)[:50]))
            ok += 1
        else:
            print("  {:<7} X  {} p.{} NÃO contém «{}…»".format(
                e["id"], cod, nums[0], norm(cits[0])[:50]))
            falhas.append(e["id"])
            falha += 1

    print("=" * 78)
    print("confirmados {} | falhas {} | indeterminados {}".format(ok, falha, indet))
    if falhas:
        print("\nFALHAS — investigar antes de citar: {}".format(", ".join(falhas)))
        print("Uma falha significa uma de três coisas, nesta ordem de probabilidade:")
        print("  1. o vínculo aponta para o documento errado (foi o caso de PT-28)")
        print("  2. a página está errada")
        print("  3. a transcrição foi editada e não confere mais com o original")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
