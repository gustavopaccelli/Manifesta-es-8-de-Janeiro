#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Migração do codebook do process tracing para o esquema de 16 campos.

Rodada única, executada em 16/08/2026. Lê o JSON e o CSV vigentes, funde o campo
`fonte_local` que só existia no CSV, deriva `fonte_pagina` e `status_classe`, e
aplica as correções de vínculo apuradas na auditoria de fontes.

O JSON resultante passa a ser a ÚNICA fonte da verdade. CSV e XLSX são gerados a
partir dele por `gerar_codebook.py` — nunca editados à mão.

Uso:  python scripts/migrar_esquema16.py [--dry-run]
"""

import csv
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_IN = RAIZ / "process_tracing_8jan_eventos.json"
CSV_IN = RAIZ / "process_tracing_8jan_eventos.csv"

# ---------------------------------------------------------------------------
# Registro de documentos: código curto -> caminho relativo à raiz do projeto.
# O código curto é o que aparece em `fonte_pagina`, para que a página fique
# inequivocamente atribuída ao documento certo quando o registro cita mais de um.
# ---------------------------------------------------------------------------
DOCS = OrderedDict([
    ("CPMI",           "Fontes/04_T+1_Resposta-institucional/CPMI-8-de-Janeiro_Relatorio-Final_2023-10-17.pdf"),
    ("AP 2668",        "Fontes/04_T+1_Resposta-institucional/STF_AP-2668_Acordao_Condenacao_2025-09-11.pdf"),
    ("AP 2668-QO",     "Fontes/04_T+1_Resposta-institucional/STF_AP-2668-QO_Acordao_2025-05-14.pdf"),
    ("Cappelli",       "Fontes/03_T0_8-de-janeiro/GDF-SSP_Relatorio-Interventor-Federal_Cappelli_2023-01-27.pdf"),
    ("STF Livro 2023", "Fontes/03_T0_8-de-janeiro/STF_Livro-8-1-2023-democraciainabalada_2023_vandalismo-e-restauracao.pdf"),
    ("PGR",            "Fontes/02_T-1_Articulacao/PGR_Denuncia_PET-12100_Nucleo-1_2025-02-18.pdf"),
    ("TRF-4",          "Fontes/01_Arco-judicial_2017-2021/TRF4_Revista-97_Acordao-ACr-5046512-94_2018-01-24.pdf"),
    ("ADC 43/44/54",   "Fontes/01_Arco-judicial_2017-2021/STF_ADC-43-44-54_Acordao_2019-11-07.pdf"),
    ("ADC 43-MC",      "Fontes/01_Arco-judicial_2017-2021/STF_ADC-43-MC_Acordao_2016-10-05.pdf"),
    ("HC 152.752",     "Fontes/01_Arco-judicial_2017-2021/STF_HC-152752_Acordao_2018-04-04.pdf"),
    ("HC 164.493",     "Fontes/01_Arco-judicial_2017-2021/STF_HC-164493_Acordao_Suspeicao-Moro_2021-03-23.pdf"),
    ("HC 193.726",     "Fontes/01_Arco-judicial_2017-2021/STF_HC-193726-AgR_Acordao_2021-04-15.pdf"),
    ("HC 193.726-2",   "Fontes/01_Arco-judicial_2017-2021/STF_HC-193726-AgR-segundo_Acordao_2021-06-23.pdf"),
    ("NetLab",         "Fontes/07_NetLab-UFRJ/NetLab-UFRJ_Anuncios-golpistas-Meta-Ads_2023-02-07.md"),
    ("Doxa",           "Fontes/07_NetLab-UFRJ/Doxa-IESP-UERJ_Manchetometro_Atos-golpistas-8-jan_2023-03.pdf"),
])
PATH_TO_COD = {v: k for k, v in DOCS.items()}

# ---------------------------------------------------------------------------
# Correções de vínculo apuradas na auditoria de 16/08/2026.
# Cada entrada substitui a lista de documentos do registro. A justificativa é
# reproduzida para que a decisão fique auditável no próprio código.
# ---------------------------------------------------------------------------
VINCULOS = {
    # --- arquivos órfãos em Fontes/ que o LEIA-ME já atribuía a registros ---
    "PT-38":  (["STF Livro 2023"],
               "Livro oficial do STF sobre vandalismo e restauração do acervo; "
               "LEIA-ME_fontes.md já o atribuía a PT-38, mas fonte_local estava vazio."),
    "PT-56":  (["AP 2668", "AP 2668-QO"],
               "A questão de ordem preliminar de 14/05/2025 integra o julgamento e estava órfã."),
    "PT-06B": (["HC 164.493", "HC 193.726-2"],
               "O Plenário confirmou a suspeição em 23/06/2021 no segundo AgR do HC 193.726 (7x4); "
               "o registro cita as duas decisões mas só apontava a primeira."),
    "PT-02A": (["ADC 43/44/54", "ADC 43-MC"],
               "A medida cautelar de 05/10/2016 é o segundo momento da precondição jurisprudencial "
               "que o próprio registro descreve."),

    # --- registro sem âncora local, apesar de status alegar fonte primária ---
    "PT-08":  (["CPMI"],
               "O achado do Sri Lanka como precedente invocado está na CPMI p. 614 e é citado na "
               "tabela do relatório, mas fonte_local estava vazio."),

    # --- vínculo apontava para o documento ERRADO --------------------------
    # Achado pela conferência amostral contra o texto dos PDFs, não pela
    # checagem de coerência: esta última deriva o código do próprio vínculo e
    # por isso valida um vínculo errado como se fosse consistente.
    "PT-28":  (["CPMI"],
               "fonte_trecho cita 'Relatório Final da CPMI, p. 657' e o texto foi localizado nessa "
               "página, mas fonte_local apontava para o acórdão da AP 2668. Erro anterior a esta "
               "rodada, corrigido em 16/08/2026."),

    # --- registros que citam dois documentos e declaravam apenas um ---
    "PT-13":  (["PGR", "CPMI"], "Denúncia da PGR como peça integral, corroborada pela CPMI p. 230 e 566."),
    "PT-18":  (["CPMI", "Cappelli"], "CPMI p. 646 e 711; corroboração e agravamento em Cappelli, conclusões D e H."),
    "PT-27":  (["CPMI", "Cappelli"], "CPMI p. 651 cita textualmente o relatório do interventor, hoje disponível em local."),
    "PT-39":  (["CPMI", "AP 2668"], "CPMI p. 677 mais o acréscimo da AP 2668 p. 496 sobre o silêncio no grupo Difusão."),
    "PT-52":  (["CPMI", "Cappelli"], "CPMI p. 576 e, em fonte primária direta, Cappelli conclusão A, p. 53."),
}

# Páginas atribuídas manualmente onde a extração automática não separa documentos.
# Conferidas uma a uma contra o texto de fonte_trecho em 16/08/2026.
PAGINAS_MANUAIS = {
    "PT-02A": "ADC 43/44/54: 3, 9",
    "PT-06B": "HC 164.493: inteiro teor",
    "PT-08":  "CPMI: 614",
    "PT-13":  "PGR: peça integral | CPMI: 230, 566",
    "PT-18":  "CPMI: 646, 711 | Cappelli: 55, 57",
    "PT-27":  "CPMI: 651",
    "PT-28":  "CPMI: 657",
    "PT-38":  "STF Livro 2023: inteiro teor",
    "PT-39":  "CPMI: 677 | AP 2668: 496",
    "PT-52":  "CPMI: 576 | Cappelli: 53",
    "PT-56":  "AP 2668: inteiro teor",
}

# Status rebaixados: a asserção excede o que a fonte obtida sustenta.
STATUS_REBAIXADO = {
    "PT-53": ("A verificar",
              'Apoiado no balanço "Democracia Inabalada", que não foi obtido. '
              "Rebaixado de Confirmado em 16/08/2026."),
    "PT-61": ("A verificar",
              'Mesmo balanço de 29/04/2026, não indexado como PDF; a cifra de 1.402 condenados '
              "está hoje só em fonte jornalística. Rebaixado de Confirmado em 16/08/2026."),
}

CLASSES = ["Confirmado em fonte primária", "Confirmado", "Contextual",
           "A verificar", "Inferência do analista"]

CAMPOS = ["id", "data_hora", "fase", "ator_grupo", "repertorio_acao", "target_alvo",
          "framing_narrativa", "resposta_estatal", "mecanismo_causal", "fonte_trecho",
          "fonte_url", "fonte_local", "fonte_pagina", "status_verificacao",
          "status_classe", "nota_auditoria"]


def classificar_status(texto):
    """Reduz o status em texto livre a uma das cinco classes controladas."""
    t = (texto or "").strip().lower()
    if t.startswith("inferência") or t.startswith("inferencia"):
        return "Inferência do analista"
    if t.startswith("contextual"):
        return "Contextual"
    if t.startswith("a verificar"):
        return "A verificar"
    if t.startswith("parcialmente"):
        return "A verificar"
    if "fonte primária" in t or "fontes primárias" in t:
        return "Confirmado em fonte primária"
    if t.startswith("confirmado"):
        return "Confirmado"
    return "A verificar"


def extrair_paginas(trecho, codigos):
    """Extrai as páginas citadas no texto livre, prefixadas pelo documento.

    Só é usada quando o registro cita um único documento. Casos com mais de um
    documento entram por PAGINAS_MANUAIS, porque a segmentação automática do
    texto não é confiável o bastante para pesquisa científica.
    """
    if not trecho or not codigos:
        return ""
    achados = []
    for m in re.finditer(r"p\.\s*(\d{1,4})(?:\s*[-–]\s*(\d{1,4}))?", trecho):
        tok = m.group(1) + ("-" + m.group(2) if m.group(2) else "")
        if tok not in achados:
            achados.append(tok)
    # "p. 3 e 9" / "p. 55 e 57": o segundo número vem sem o prefixo "p."
    for m in re.finditer(r"p\.\s*\d{1,4}\s+e\s+(\d{1,4})", trecho):
        if m.group(1) not in achados:
            achados.append(m.group(1))
    if not achados:
        return ""
    return "{}: {}".format(codigos[0], ", ".join(achados))


def main():
    dry = "--dry-run" in sys.argv

    dados = json.loads(JSON_IN.read_text(encoding="utf-8"))
    # utf-8-sig: tolera o BOM que gerar_codebook.py escreve para o Excel pt-BR,
    # e também o CSV original, que não tinha BOM.
    with CSV_IN.open(encoding="utf-8-sig", newline="") as fh:
        csv_rows = {r["ID"]: r for r in csv.DictReader(fh)}

    novos = []
    relatorio = []

    for ev in dados["eventos"]:
        pid = ev["id"]
        linha = csv_rows.get(pid, {})
        notas = []

        # --- fonte_local: migra do CSV e aplica as correções da auditoria ------
        if pid in VINCULOS:
            codigos, motivo = VINCULOS[pid]
            local = "; ".join(DOCS[c] for c in codigos)
            antes = (linha.get("Fonte_Local") or "").strip()
            notas.append("vínculo corrigido em 16/08/2026 — " + motivo)
            relatorio.append((pid, "VÍNCULO", antes or "(vazio)", local))
        else:
            local = (linha.get("Fonte_Local") or "").strip()
            codigos = [PATH_TO_COD[p] for p in local.split("; ") if p in PATH_TO_COD]

        # --- fonte_pagina -----------------------------------------------------
        if pid in PAGINAS_MANUAIS:
            pagina = PAGINAS_MANUAIS[pid]
        else:
            pagina = extrair_paginas(ev.get("fonte_trecho"), codigos)

        # --- status_classe ----------------------------------------------------
        status_txt = ev.get("status_verificacao") or ""
        if pid in STATUS_REBAIXADO:
            classe, motivo = STATUS_REBAIXADO[pid]
            notas.append("status rebaixado — " + motivo)
            relatorio.append((pid, "STATUS", classificar_status(status_txt), classe))
        else:
            classe = classificar_status(status_txt)

        novo = OrderedDict()
        for campo in CAMPOS:
            if campo == "fonte_local":
                novo[campo] = local or None
            elif campo == "fonte_pagina":
                novo[campo] = pagina or None
            elif campo == "status_classe":
                novo[campo] = classe
            elif campo == "nota_auditoria":
                novo[campo] = " | ".join(notas) if notas else None
            else:
                novo[campo] = ev.get(campo)
        novos.append(novo)

    dados["eventos"] = novos
    dados["metadados"]["colunas_codebook"] = CAMPOS
    dados["metadados"]["vocabulario_status_classe"] = CLASSES
    dados["metadados"]["registro_documentos"] = dict(DOCS)
    # Idempotência: reexecutar a migração não deve empilhar entradas de revisão.
    dados["metadados"]["revisoes"] = [
        r for r in dados["metadados"]["revisoes"]
        if not r.startswith("2026-08-16 (esquema 16 campos")
    ]
    dados["metadados"]["revisoes"].append(
        "2026-08-16 (esquema 16 campos + auditoria de fontes) — o JSON passa a ser a única fonte "
        "da verdade; CSV e XLSX são gerados por scripts/gerar_codebook.py. Acrescentados quatro "
        "campos: fonte_local (antes só no CSV, fechando a inconsistência com colunas_codebook), "
        "fonte_pagina (página atribuída ao documento, por código curto), status_classe (vocabulário "
        "controlado de cinco valores, com o texto livre preservado em status_verificacao) e "
        "nota_auditoria. A auditoria vinculou cinco arquivos que estavam órfãos em Fontes/ "
        "(PT-38, PT-56, PT-06B, PT-02A e PT-08) e explicitou a corroboração dupla em PT-13, PT-18, "
        "PT-27, PT-39 e PT-52. CORREÇÃO DE VÍNCULO ERRADO: PT-28 apontava para o acórdão da AP 2668 "
        "enquanto seu próprio fonte_trecho citava a CPMI, p. 657 — o texto foi localizado nessa "
        "página da CPMI e o vínculo foi corrigido. O erro é anterior a esta rodada e só apareceu na "
        "conferência amostral contra o texto dos PDFs; a checagem de coerência não o pega, porque "
        "deriva o código do próprio vínculo. PT-53 e PT-61 foram rebaixados a 'A verificar': ambos "
        'se apoiam no balanço "Democracia Inabalada", que não foi obtido. '
        "Nenhum dado analítico foi alterado."
    )

    if dry:
        print("DRY RUN — nada foi escrito\n")
    else:
        JSON_IN.write_text(
            json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("JSON reescrito: {} eventos x {} campos\n".format(len(novos), len(CAMPOS)))

    print("ALTERAÇÕES APLICADAS")
    for pid, tipo, antes, depois in relatorio:
        print("  {:<7} {:<8} {}".format(pid, tipo, antes[:70]))
        print("  {:<7} {:<8} -> {}".format("", "", depois[:70]))

    print("\nDISTRIBUIÇÃO DE status_classe")
    from collections import Counter
    for k, v in Counter(e["status_classe"] for e in novos).most_common():
        print("  {:3d}  {}".format(v, k))

    print("\nCOBERTURA")
    print("  com fonte_local  : {}/{}".format(sum(1 for e in novos if e["fonte_local"]), len(novos)))
    print("  com fonte_pagina : {}/{}".format(sum(1 for e in novos if e["fonte_pagina"]), len(novos)))


if __name__ == "__main__":
    main()
