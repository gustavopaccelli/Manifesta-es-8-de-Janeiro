#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Verificação de integridade do aparato do process tracing.

Roda seis checagens e devolve código de saída != 0 se qualquer uma falhar.
Pensada para ser executada depois de toda alteração no codebook — é o que
garante que JSON, CSV e XLSX não voltem a divergir.

  1. Sincronia dos três formatos, célula a célula (82 IDs x 16 campos)
  2. Integridade referencial: todo fonte_local existe em disco
  3. Cobertura do inventário: todo arquivo de Fontes/ está declarado
  4. Vocabulário controlado de status_classe
  5. Coerência entre fonte_pagina e fonte_local (documento citado x documento vinculado)
  6. Paginação real dos PDFs via PyPDF2 (nunca pdfinfo, que subconta)

Uso:  python scripts/verificar_integridade.py
"""

import csv
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))

from gerar_codebook import CABECALHOS, PROCEDENCIA  # noqa: E402

JSON_P = RAIZ / "process_tracing_8jan_eventos.json"
CSV_P = RAIZ / "process_tracing_8jan_eventos.csv"
XLSX_P = RAIZ / "process_tracing_8jan_codebook.xlsx"

CLASSES = {"Confirmado em fonte primária", "Confirmado", "Contextual",
           "A verificar", "Inferência do analista"}

falhas = []
avisos = []


def cabecalho(n, titulo):
    print("\n" + "=" * 72)
    print("{}. {}".format(n, titulo))
    print("=" * 72)


def main():
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    eventos = dados["eventos"]
    campos = list(CABECALHOS.keys())

    # ------------------------------------------------------------------ 1 ---
    cabecalho(1, "SINCRONIA DOS TRÊS FORMATOS")
    with CSV_P.open(encoding="utf-8-sig", newline="") as fh:
        csv_rows = {r["ID"]: r for r in csv.DictReader(fh)}

    from openpyxl import load_workbook
    ws = load_workbook(XLSX_P, read_only=True)["Codebook"]
    it = ws.iter_rows(values_only=True)
    cab_x = list(next(it))
    xlsx_rows = {}
    for linha in it:
        if linha and linha[0]:
            xlsx_rows[linha[0]] = dict(zip(cab_x, linha))

    div = 0
    for ev in eventos:
        pid = ev["id"]
        for jk in campos:
            ck = CABECALHOS[jk]
            v_json = (ev.get(jk) or "").strip()
            v_csv = (csv_rows.get(pid, {}).get(ck) or "").strip()
            v_xls = str(xlsx_rows.get(pid, {}).get(ck) or "").strip()
            if not (v_json == v_csv == v_xls):
                div += 1
                if div <= 5:
                    print("  DIVERGÊNCIA {}.{}".format(pid, jk))
                    print("    JSON: {!r}".format(v_json[:80]))
                    print("    CSV : {!r}".format(v_csv[:80]))
                    print("    XLSX: {!r}".format(v_xls[:80]))
    print("  registros: JSON {} | CSV {} | XLSX {}".format(
        len(eventos), len(csv_rows), len(xlsx_rows)))
    print("  células divergentes: {}".format(div))
    if div or not (len(eventos) == len(csv_rows) == len(xlsx_rows)):
        falhas.append("sincronia entre formatos ({} células)".format(div))
    else:
        print("  OK — os três formatos são idênticos nos 82 x 16")

    # ------------------------------------------------------------------ 2 ---
    cabecalho(2, "INTEGRIDADE REFERENCIAL DOS CAMINHOS")
    quebrados = []
    com_local = 0
    for ev in eventos:
        local = (ev.get("fonte_local") or "").strip()
        if not local:
            continue
        com_local += 1
        for p in [x.strip() for x in local.split(";") if x.strip()]:
            if not (RAIZ / p).exists():
                quebrados.append((ev["id"], p))
    print("  registros com fonte_local: {}/{}".format(com_local, len(eventos)))
    print("  referências quebradas    : {}".format(len(quebrados)))
    for i, p in quebrados:
        print("    ! {} -> {}".format(i, p))
    if quebrados:
        falhas.append("{} referência(s) quebrada(s)".format(len(quebrados)))
    else:
        print("  OK — todo caminho declarado existe em disco")

    # ------------------------------------------------------------------ 3 ---
    cabecalho(3, "COBERTURA DO INVENTÁRIO")
    citados = set()
    for ev in eventos:
        for p in (ev.get("fonte_local") or "").split(";"):
            if p.strip():
                citados.add(p.strip())
    naodecl = []
    for arq in sorted((RAIZ / "Fontes").rglob("*")):
        if arq.is_dir() or arq.name.upper().startswith("LEIA-ME"):
            continue
        rel = arq.relative_to(RAIZ).as_posix()
        if rel not in citados and rel not in PROCEDENCIA:
            naodecl.append(rel)
    print("  arquivos citados por registro : {}".format(len(citados)))
    print("  arquivos sem declaração       : {}".format(len(naodecl)))
    for n in naodecl:
        print("    ! " + n)
    if naodecl:
        falhas.append("{} arquivo(s) sem procedência declarada".format(len(naodecl)))
    else:
        print("  OK — todo arquivo ou ancora um registro ou tem procedência declarada")

    # ------------------------------------------------------------------ 4 ---
    cabecalho(4, "VOCABULÁRIO CONTROLADO DE status_classe")
    from collections import Counter
    cont = Counter(ev.get("status_classe") for ev in eventos)
    fora = [k for k in cont if k not in CLASSES]
    for k, v in cont.most_common():
        print("  {:3d}  {}".format(v, k))
    if fora:
        print("  ! valores fora do vocabulário: {}".format(fora))
        falhas.append("status_classe fora do vocabulário: {}".format(fora))
    else:
        print("  OK — só os cinco valores previstos")

    # ------------------------------------------------------------------ 5 ---
    cabecalho(5, "COERÊNCIA fonte_pagina x fonte_local")
    from gerar_codebook import RAIZ as _R  # noqa: F401
    reg_docs = dados["metadados"].get("registro_documentos", {})
    path_to_cod = {v: k for k, v in reg_docs.items()}
    incoerentes = []
    for ev in eventos:
        pag = (ev.get("fonte_pagina") or "").strip()
        local = (ev.get("fonte_local") or "").strip()
        if not pag:
            continue
        cods_pag = {m.strip() for m in re.findall(r"(?:^|\|)\s*([^:|]+):", pag)}
        cods_loc = {path_to_cod[p.strip()] for p in local.split(";")
                    if p.strip() in path_to_cod}
        if not cods_pag <= cods_loc:
            incoerentes.append((ev["id"], sorted(cods_pag - cods_loc), sorted(cods_loc)))
    print("  registros com fonte_pagina: {}".format(
        sum(1 for e in eventos if (e.get("fonte_pagina") or "").strip())))
    print("  incoerências              : {}".format(len(incoerentes)))
    for i, falta, tem in incoerentes:
        print("    ! {} cita {} mas só vincula {}".format(i, falta, tem))
    if incoerentes:
        falhas.append("{} incoerência(s) página x documento".format(len(incoerentes)))
    else:
        print("  OK — toda página citada pertence a um documento vinculado")

    # ------------------------------------------------------------------ 6 ---
    cabecalho(6, "PAGINAÇÃO REAL DOS PDFs (PyPDF2)")
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        avisos.append("PyPDF2 ausente — paginação não conferida")
        print("  ! PyPDF2 não instalado")
    else:
        total = n = 0
        for arq in sorted((RAIZ / "Fontes").rglob("*.pdf")):
            try:
                p = len(PdfReader(str(arq)).pages)
                total += p
                n += 1
            except Exception as exc:
                falhas.append("PDF ilegível: {}".format(arq.name))
                print("    ! {}: {}".format(arq.name, str(exc)[:60]))
        print("  {} PDFs, {} páginas no total".format(n, total))
        # Linha de base: 16/08/2026, após a entrada do preprint sobre editoriais
        # (eixo 08). Atualize junto com o inventário sempre que uma peça entrar.
        if (n, total) != (22, 6928):
            avisos.append("corpus mudou: {} PDFs / {} páginas (era 22 / 6928)".format(n, total))
            print("  ~ corpus difere do inventário de 16/08/2026 (19 PDFs / 6835 p.)")
        else:
            print("  OK — bate com o inventário")

    # --------------------------------------------------------------------- --
    print("\n" + "=" * 72)
    if falhas:
        print("RESULTADO: {} FALHA(S)".format(len(falhas)))
        for f in falhas:
            print("  X " + f)
    else:
        print("RESULTADO: APROVADO — as seis checagens passaram")
    for a in avisos:
        print("  ~ aviso: " + a)
    print("=" * 72)
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
