#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Páginas de PT-58, PT-59 e PT-60 apontam para o dispositivo, não só para a capa.

Rodada de 11/09/2026. Na rodada de 16/08/2026, as três decisões da execução
penal entraram no corpus com `fonte_pagina` apontando para a p. 1 (relatório ou
recapitulação) e para a última página (assinatura). As transcrições do
`fonte_trecho` estão, na maior parte, em outras páginas — o dispositivo da
transferência na p. 33, o da domiciliar na p. 36, a fundamentação da preventiva
na p. 7, o dispositivo dela na p. 16.

`conferir_paginas.py` não pegou isso porque passa quando QUALQUER transcrição
está em QUALQUER página listada. Em PT-58 e PT-60, a primeira citação está de
fato na p. 1, e as demais nunca foram procuradas. Em PT-59 o registro foi
aprovado pela citação errada: a do dispositivo NÃO está em nenhuma das páginas
listadas (está na p. 33), mas uma janela de 60 caracteres com o endereço do
batalhão ("...PMDF, localizado no Complexo Penitenciário da Papuda..."), que se
repete ao longo da decisão, casou na p. 36. A segunda citação, a da junta
médica, está sim em parte na p. 36 — o registro não estava sem âncora, mas o
OK que o script deu não era o que parecia.

COMO AS PÁGINAS FORAM LOCALIZADAS. Cada transcrição do `fonte_trecho` foi
procurada em todas as páginas do documento, com a mesma normalização de
`conferir_paginas.py`, medindo a fração de janelas de 30 caracteres presente
em cada página. Fórmulas genéricas ("Diante do exposto, nos termos dos artigos
21 e 341...") casam em várias páginas por janela curta; valeu a página de maior
cobertura. Fatos sem aspas (Miami, IPJ 099/2025, "15 (quinze) minutos",
audiência de 23/11, parecer da PGR) foram localizados por busca literal.

  PT-58 · Pet 14.129: 1 objeto e cautelares de 17/7/2025 · 7 fundamentação e
          IPJ 099/2025 · 8 e 10 vigília (10: Miami) · 14 embaixada da
          Argentina, 0h08, "15 minutos" · 16 dispositivo e custódia em 23/11
          EP 169-Transferência: 1 início da pena em 25/11/2025
  PT-59 · EP 169-Transferência: 1 pena recapitulada · 33 dispositivo ·
          35-36 junta médica · 36 laudo em 10 dias e assinatura
  PT-60 · EP 169-Domiciliar: 1 indeferimento de 2/3/2026 · 35 parecer da PGR
          pelo deferimento · 36 dispositivo e condição 1 · 37 condições ·
          38 fiscalização · 40 assinatura

Também corrige `metadados.n_subeventos`, que ficou em 81 depois da entrada de
PT-50A em 16/08/2026. O valor passa a ser contado, não digitado.

Nenhum fato, mecanismo, status ou transcrição é alterado — só página e
contagem.

Uso:  python scripts/recodificar_paginas_execucao.py [--dry-run]

RESSALVA ACRESCENTADA EM 25/09/2026 — o texto acima diz que PT-59 foi "aprovado
pela citação errada". A verificação feita ao endurecer o conferir_paginas.py
mostrou que a leitura estava exagerada: o dispositivo COMEÇA na p. 33 e SEGUE até
a p. 36, e a janela que casava na p. 36 é parte legítima da mesma transcrição, 300
caracteres adiante. O vínculo antigo era INCOMPLETO, não falso — confirmava a
página final sem nunca abrir a inicial. A correção que este script aplicou continua
certa; o diagnóstico é que estava mais forte do que a evidência sustentava.
"""

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

PAGINAS = {
    "PT-58": "Pet 14.129: 1, 7, 8, 10, 14, 16 | EP 169-Transferência: 1",
    "PT-59": "EP 169-Transferência: 1, 33, 35, 36",
    "PT-60": "EP 169-Domiciliar: 1, 35, 36, 37, 38, 40",
}

NOTA = (" PÁGINAS CORRIGIDAS em 11/09/2026: o vínculo anterior ({antes}) apontava para a "
        "capa e a assinatura da peça; as transcrições foram localizadas página a página e o "
        "campo passou a {depois}.")

REVISAO = (
    "2026-09-11 (páginas da execução penal) — fonte_pagina de PT-58, PT-59 e PT-60 corrigido "
    "para as páginas onde as transcrições efetivamente estão (dispositivos na Pet 14.129, p. 16; "
    "EP 169-Transferência, p. 33; EP 169-Domiciliar, p. 36). O vínculo de 16/08/2026 apontava "
    "para capa e assinatura. conferir_paginas.py aprovava PT-58 e PT-60 porque a primeira "
    "citação de cada um está na p. 1, e PT-59 pela citação errada: um trecho do endereço do 19º "
    "BPM, repetido ao longo da decisão, casou na p. 36, onde o dispositivo não está (está na "
    "p. 33). Nenhum "
    "fato, status ou transcrição alterado. Corrigido também "
    "metadados.n_subeventos, que ficara em 81 após a entrada de PT-50A; passa a ser contado."
)


def aplicar(dados):
    """Aplica a correção sobre o dict carregado. Idempotente."""
    mudancas = []
    for ev in dados["eventos"]:
        novo = PAGINAS.get(ev["id"])
        if novo is None or ev.get("fonte_pagina") == novo:
            continue
        antes = ev.get("fonte_pagina")
        ev["fonte_pagina"] = novo
        if "PÁGINAS CORRIGIDAS em 11/09/2026" not in (ev.get("nota_auditoria") or ""):
            ev["nota_auditoria"] = (ev.get("nota_auditoria") or "") + NOTA.format(
                antes="'{}'".format(antes), depois="'{}'".format(novo))
        mudancas.append((ev["id"], antes, novo))

    meta = dados["metadados"]
    n = len(dados["eventos"])
    if meta.get("n_subeventos") != n:
        mudancas.append(("metadados.n_subeventos", meta.get("n_subeventos"), n))
        meta["n_subeventos"] = n

    if mudancas and REVISAO not in meta["revisoes"]:
        meta["revisoes"].append(REVISAO)
    return mudancas


def main():
    dry = "--dry-run" in sys.argv
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    mudancas = aplicar(dados)
    if not mudancas:
        print("Nada a fazer — correção já aplicada.")
        return
    for campo, antes, depois in mudancas:
        print("=== {} ===\n  antes : {}\n  depois: {}".format(campo, antes, depois))
    if dry:
        print("\nDRY RUN — nada gravado")
    else:
        JSON_P.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("\nJSON reescrito.")


if __name__ == "__main__":
    main()
