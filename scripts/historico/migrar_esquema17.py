#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Migração do codebook para o esquema de 17 campos: entra `autonomia_movimento`.

Rodada única, executada em 16/10/2026, por decisão do pesquisador — a decisão 3
da tarefa 26(c), aberta desde 04/10 no item 35.4: *"o esquema ganha campo, ou
isso vive só na prosa?"*. Resposta dele: ganha o campo.

POR QUE UM CAMPO, E NÃO PROSA. Von Bülow e Abers (2024) sustentam que o
bolsonarismo é movimento social com autonomia relativa em relação ao líder — o
presidente "depends on a well-organized grassroots mobilization process that
pre-dates his emergence as a populist radical-right leader and which he does not
fully control" (p. 1000 impressa, PDF p. 3). Isso responde à pergunta central da
pesquisa — o 8 de janeiro foi conduzido de cima ou teve vida própria — e nenhum
dos 16 campos a codificava: o achado vivia em `fonte_trecho`, legível por quem
lesse o registro inteiro e invisível para qualquer contagem.

O QUE ESTA MIGRAÇÃO NÃO FAZ, E É DE PROPÓSITO. Ela não codifica os 83 registros.
Atribuir valor a cada um é CODIFICAÇÃO — exige ler a fonte de cada registro e
decidir —, e codificação não se executa por inferência neste projeto. Entra com
UM valor, o de PT-06, porque ele não é interpretação nova: as duas transcrições
que o sustentam já estão em `fonte_trecho`, já têm página em `fonte_pagina`
(VON BULOW E ABERS 2024: 3 e 12) e já são conferidas contra o PDF a cada ciclo.
Os outros 82 ficam VAZIOS, e vazio aqui tem significado declarado: **não
codificado**, não "não se aplica". A contagem sai impressa no ciclo para que o
vazio não possa se esconder — zero medido é guarda, zero suposto é silêncio.

O VOCABULÁRIO é controlado, como o de `status_classe`, e tem três valores mais o
vazio declarado. Nome do campo e valores são do pesquisador: trocar qualquer um
é um comando, e esta é a proposta, não a palavra final.

Uso:  python scripts/historico/migrar_esquema17.py [--dry-run]
"""

import json
import sys
from collections import OrderedDict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

CAMPO = "autonomia_movimento"
DEPOIS_DE = "mecanismo_causal"

# ---------------------------------------------------------------------------
# O vocabulário. Três valores e um vazio que significa coisa distinta de todos
# os três -- e é por isso que "não codificado" NÃO é valor: valor é o que o
# pesquisador afirmou depois de ler; vazio é o que ninguém olhou ainda. Fundir
# os dois tornaria a pendência invisível, que é o defeito que este projeto
# persegue desde agosto.
# ---------------------------------------------------------------------------
VOCABULARIO = OrderedDict([
    ("Autonomia relativa",
     "A fonte documenta processo de mobilização com vida própria, anterior à "
     "liderança ou não inteiramente controlado por ela."),
    ("Conduzido de cima",
     "A fonte documenta ação dirigida, convocada ou coordenada por liderança, "
     "órgão ou comando."),
    ("Não se aplica",
     "O registro não codifica ação de movimento — ato de Estado, decisão "
     "judicial, medida administrativa."),
])
VAZIO = ("vazio = NÃO CODIFICADO. Não é 'não se aplica': é registro que ainda "
         "não foi lido sob esta pergunta. A contagem sai no passo 4 do ciclo.")

# ---------------------------------------------------------------------------
# A única codificação desta rodada, e ela não é interpretação nova: o achado
# está transcrito em fonte_trecho de PT-06 desde 04/10/2026, com as duas
# páginas em fonte_pagina, e o item 35.4 o nomeia com estas palavras.
# ---------------------------------------------------------------------------
CODIFICADOS = {
    "PT-06": ("Autonomia relativa",
              "codificado em 16/10/2026, decisão 3 da tarefa 26(c) — o campo "
              "`autonomia_movimento` nasce com este registro porque foi ele "
              "que o exigiu. Lastro já conferido pelo ciclo, em fonte_trecho: "
              "o presidente “depends on a well-organized grassroots "
              "mobilization process that pre-dates his emergence as a populist "
              "radical-right leader and which he does not fully control” "
              "(von Bülow e Abers, 2024, p. 1000 impressa — PDF p. 3) e "
              "“bolsonarismo is part of a process of right-wing "
              "mobilization that is larger than the leader himself, and "
              "precedes his rise to power” (p. 1009 impressa — PDF p. 12). "
              "NENHUM OUTRO REGISTRO FOI CODIFICADO: atribuir valor exige ler "
              "a fonte de cada um, e isso é codificação, não migração."),
}

REVISAO_PREFIXO = "2026-10-16 (esquema 17 campos"
REVISAO = (
    "2026-10-16 (esquema 17 campos — entra autonomia_movimento) — por decisão do "
    "pesquisador, a decisão 3 da tarefa 26(c), aberta desde 04/10/2026 no item 35.4. "
    "O esquema passa de 16 para 17 campos: `autonomia_movimento` codifica o grau de "
    "autonomia do movimento em relação à liderança, que é a pergunta central da "
    "pesquisa — o 8 de janeiro foi conduzido de cima ou teve vida própria — e que "
    "nenhum campo codificava. Vocabulário controlado de três valores (Autonomia "
    "relativa · Conduzido de cima · Não se aplica), com o VAZIO declarado como NÃO "
    "CODIFICADO e contado no passo 4 do ciclo. CODIFICADO UM registro, PT-06, cujo "
    "lastro já estava em fonte_trecho com página conferida; os outros 82 entram "
    "vazios de propósito, porque atribuir valor é codificação e exige leitura da "
    "fonte de cada registro. Guardas que entram junto: o valor tem de estar no "
    "vocabulário; valor diferente de 'Não se aplica' exige fonte_pagina, para que "
    "não nasça codificação sem folha; e `metadados.colunas_codebook` passa a ser "
    "conferido contra os cabeçalhos que o gerador usa, porque esquema declarado que "
    "ninguém confere é a mesma família do sha1 que declarava identidade já desfeita. "
    "Nenhum dado analítico anterior foi alterado."
)


def main():
    dry = "--dry-run" in sys.argv
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    eventos = dados["eventos"]

    if CAMPO in eventos[0]:
        print("JÁ MIGRADO — o campo {} existe no primeiro registro.".format(CAMPO))
        return 0

    novos = []
    for ev in eventos:
        novo = OrderedDict()
        for k, v in ev.items():
            novo[k] = v
            if k == DEPOIS_DE:
                novo[CAMPO] = None
        assert CAMPO in novo, "{} não tem {}".format(ev["id"], DEPOIS_DE)
        if ev["id"] in CODIFICADOS:
            valor, nota = CODIFICADOS[ev["id"]]
            novo[CAMPO] = valor
            antiga = novo.get("nota_auditoria") or ""
            novo["nota_auditoria"] = (antiga + " || " + nota) if antiga else nota
        novos.append(novo)

    campos = list(novos[0].keys())
    dados["eventos"] = novos
    dados["metadados"]["colunas_codebook"] = campos
    dados["metadados"]["vocabulario_autonomia_movimento"] = dict(VOCABULARIO)
    dados["metadados"]["vocabulario_autonomia_movimento"]["(vazio)"] = VAZIO
    dados["metadados"]["revisoes"] = [
        r for r in dados["metadados"]["revisoes"]
        if not r.startswith(REVISAO_PREFIXO)
    ]
    dados["metadados"]["revisoes"].append(REVISAO)

    if dry:
        print("DRY RUN — nada foi escrito\n")
    else:
        JSON_P.write_text(
            json.dumps(dados, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8")

    print("{} eventos x {} campos".format(len(novos), len(campos)))
    print("ordem: ... {} -> {} -> {} ...".format(
        DEPOIS_DE, CAMPO, campos[campos.index(CAMPO) + 1]))
    print("\n{}".format(CAMPO.upper()))
    for ev in novos:
        if ev[CAMPO]:
            print("  {:<7} {}".format(ev["id"], ev[CAMPO]))
    print("  {:3d}  (vazio) — NÃO CODIFICADO".format(
        sum(1 for e in novos if not e[CAMPO])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
