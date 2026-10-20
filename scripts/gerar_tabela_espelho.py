#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A TABELA-ESPELHO: o que as figuras exibem, ao lado do que o codebook diz.

POR QUE ISTO EXISTE, e foi o pesquisador que pediu em 20/10/2026. A cronologia
interativa é a peça que vai para o artigo, e ela **não é gerada**: carrega uma
cópia manual de cada registro dentro do `<script>`. `conferir_figuras.py` confere
cobertura, selo de status, procedência e cifras retiradas — e **não compara o
texto do mecanismo**. O item 42.3 registrou essa lacuna em 10/10/2026 e ela ficou
aberta; esta tabela é o instrumento que a torna visível.

E ela achou, na primeira execução, três registros em que **a figura afirma o que
o codebook corrigiu**: PT-02 diz "spin-off" onde o campo diz "não é spin-off";
PT-01 usa a formulação que o campo declara substituída em 04/10/2026; e PT-06
carrega a tese que a leitura de von Bülow e Abers retificou na mesma data.

O QUE NÃO SE PODE COBRAR, e a medição é a razão. Comparados os seis campos de
prosa da figura com os do codebook, `mec` difere em 100% das entradas -- e isso
é DESENHO: a figura precisa de uma frase legível, e `mecanismo_causal` carrega a
prosa de auditoria (a razão de cada troca de nome, os limites, as remissões).
Exigir igualdade reprovaria tudo e ensinaria a ignorar a guarda. **O que é
conferível é o NOME do mecanismo** — a frase até o primeiro `:` ou travessão.

GERADA, NUNCA ESCRITA À MÃO. Uma tabela-espelho mantida à mão seria a quinta
cópia dos mesmos dados, e este repositório tem o histórico de quatro cópias
envelhecendo em silêncio.

Emite:  reports/TABELA-ESPELHO-EVENTOS.md       (scanável, para leitura)
        data/processed/tabela_espelho_eventos.csv  (completa, para o artigo)

Uso:  python scripts/gerar_tabela_espelho.py
"""

import csv
import io
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))

# Importadas, não reimplementadas: se as duas cópias divergissem, uma diria que
# o ponto é composto e a outra que falta registro, para sempre.
from conferir_figuras import BLOCO, CLASSE, COMPOSTOS, campo  # noqa: E402

JSON_P = RAIZ / "process_tracing_8jan_eventos.json"
HTML_P = RAIZ / "reports/figures/cronologia_8jan_interativa.html"
SVG_P = RAIZ / "reports/figures/figura_cronologia_8jan.svg"
MD_P = RAIZ / "reports/TABELA-ESPELHO-EVENTOS.md"
CSV_P = RAIZ / "data/processed/tabela_espelho_eventos.csv"

# campo na figura -> campo no codebook
MAPA = [("ator", "ator_grupo"), ("rep", "repertorio_acao"),
        ("tgt", "target_alvo"), ("frm", "framing_narrativa"),
        ("res", "resposta_estatal"), ("mec", "mecanismo_causal")]

# LINHA DE BASE DAS DIVERGENCIAS DE NOME DE MECANISMO: DEZESSETE, medida em
# 20/10/2026 por este gerador, antes de qualquer correcao.
#
# E O NUMERO CORRIGE UM QUE EU HAVIA ESTIMADO. Ao levantar o problema eu medi
# com uma regex propria e anunciei 23; este gerador usa `BLOCO` e `COMPOSTOS`
# importados do verificador -- que resolvem os pontos compostos e alcancam os 85
# registros, nao 79 -- e um recorte de nome que corta tambem no ponto final.
# Medido com o instrumento do projeto em vez de com regex de ocasiao: 17.
# **Cifra estimada a mao nao vale como linha de base**, e esta e a quarta vez
# que isso aparece neste repositorio.
#
# A base existe para CAIR. Enquanto nao for zero, esta tabela CONTA e NOMEIA, e
# `conferir_figuras.py` nao reprova: guarda que derruba o ciclo em 17 casos
# conhecidos no dia em que nasce ensina a ignorar guarda. Quando chegar a zero,
# a cobranca do nome entra la, com prova negativa.
DIVERGENCIAS_BASE = 17


def norma(s):
    """Normaliza para comparar: sem acento, sem aspa curva, sem travessão."""
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    # Toda aspa vira a MESMA aspa reta. A figura escreve "de cima" com aspa
    # dupla e o codebook com aspa simples, e sem esta linha PT-56 aparecia como
    # divergência de nome quando a diferença era o caractere -- ruído que
    # ensinaria a ignorar a coluna.
    for a, b in ((u"“", '"'), (u"”", '"'), (u"‘", '"'),
                 (u"’", '"'), (u"'", '"'),
                 (u"—", "-"), (u"–", "-"), (u"−", "-")):
        s = s.replace(a, b)
    return " ".join(s.lower().split())


def nome_mecanismo(txt):
    """O NOME do mecanismo: o que vem antes do primeiro ':', ' - ' ou '.'.

    É a parte que a figura e o codebook têm de dizer igual. O corpo que vem
    depois é paráfrase na figura e prosa de auditoria no codebook, e comparar os
    dois seria comparar coisas de natureza diferente.

    O '.' ENTROU NA PRIMEIRA EXECUÇÃO, e vale registrar por quê: sem ele, o
    recorte devolvia a frase inteira para todo registro cujo nome termina em
    ponto em vez de dois-pontos — e aí a comparação do NOME voltava a ser
    comparação da PROSA, que é justamente o que esta função existe para não
    fazer. Com os três separadores, 'Certificação judicial do frame
    anticorrupção. A acusação de...' recorta no nome e não na narrativa.
    """
    t = norma(txt)
    cortes = [t.find(s) for s in (":", " - ", ".")]
    cortes = [i for i in cortes if i > 0]
    if cortes:
        t = t[:min(cortes)]
    return t.strip(" .,")


def estado(fig, cod):
    """Como o texto da figura se relaciona com o do codebook."""
    a, b = norma(fig), norma(cod)
    if not a and not b:
        return "vazio nos dois"
    if not a:
        return "ausente na figura"
    if a == b:
        return "idêntico"
    if b.startswith(a) or a in b:
        return "contido"
    return "parafraseado"


def curto(s, n=78):
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[:n - 1] + "…"


def main():
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    eventos = dados["eventos"]
    J = {e["id"]: e for e in eventos}
    html = HTML_P.read_text(encoding="utf-8")
    svg = SVG_P.read_text(encoding="utf-8")

    # id do codebook -> (id na figura, bloco, selo)
    por_id = {}
    for b in BLOCO.finditer(html):
        bloco, hid, selo = b.group(0), b.group(1), b.group(2)
        for i in COMPOSTOS.get(hid, [hid]):
            por_id[i] = (hid, bloco, selo)

    linhas, divergentes, sem_figura = [], [], []
    contagem = {hk: {} for hk, _ in MAPA}

    for e in eventos:
        pid = e["id"]
        if pid not in por_id:
            sem_figura.append(pid)
            hid, bloco, selo = "", "", ""
        else:
            hid, bloco, selo = por_id[pid]

        esperado = CLASSE.get(e["status_classe"], "?")
        nome_cod = nome_mecanismo(e.get("mecanismo_causal"))
        nome_fig = nome_mecanismo(campo(bloco, "mec")) if bloco else ""
        if not bloco:
            espelho_nome = "sem figura"
        elif nome_fig == nome_cod or nome_fig.startswith(nome_cod) \
                or nome_cod.startswith(nome_fig):
            espelho_nome = "casa"
        else:
            espelho_nome = "DIVERGENTE"
            divergentes.append((pid, nome_fig, nome_cod))

        linha = {
            "id": pid,
            "data_hora": e["data_hora"],
            "evento": campo(bloco, "c") if bloco else "",
            "fase": e["fase"],
            "ponto_na_figura": hid if hid != pid else "",
            "no_svg": "sim" if pid in svg else "nao",
            "status_classe": e["status_classe"],
            "selo_na_figura": selo,
            "selo_esperado": esperado,
            "nome_mecanismo_codebook": nome_cod,
            "nome_mecanismo_figura": nome_fig,
            "espelho_nome_mecanismo": espelho_nome,
            "ancora": e.get("fonte_pagina") or "",
            "autonomia_movimento": e.get("autonomia_movimento") or "",
        }
        for hk, jk in MAPA:
            est = estado(campo(bloco, hk) if bloco else "", e.get(jk))
            linha["espelho_" + hk] = est
            contagem[hk][est] = contagem[hk].get(est, 0) + 1
            linha["codebook_" + jk] = " ".join((e.get(jk) or "").split())
            linha["figura_" + hk] = " ".join(
                (campo(bloco, hk) if bloco else "").split())
        linhas.append(linha)

    # ------------------------------------------------------------------- CSV
    campos = list(linhas[0].keys())
    with io.open(str(CSV_P), "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=campos)
        w.writeheader()
        w.writerows(linhas)

    # -------------------------------------------------------------------- MD
    out = []
    w = out.append
    w("# Tabela-espelho dos eventos — figuras × codebook")
    w("")
    w("> **Peça gerada por `scripts/gerar_tabela_espelho.py`. Não edite à mão.** "
      "Ela existe para responder uma pergunta que o ciclo não respondia: *as "
      "figuras ainda dizem o que o codebook diz?* `conferir_figuras.py` confere "
      "cobertura, selo, procedência e cifras retiradas — **não o texto do "
      "mecanismo** (item 42.3, lacuna aberta desde 10/10/2026).")
    w("")
    w("**{} registros no codebook · {} pontos na cronologia interativa · {} "
      "deles compostos.**".format(
          len(eventos),
          len(set(h for h, _, _ in por_id.values())),
          len(COMPOSTOS)))
    w("")
    w("## 1. O que a comparação mede, e o que ela não pode cobrar")
    w("")
    w("| campo da figura | " + " | ".join(
        ["idêntico", "contido", "parafraseado", "ausente na figura"]) + " |")
    w("|:--|--:|--:|--:|--:|")
    for hk, jk in MAPA:
        c = contagem[hk]
        w("| `{}` → `{}` | {} | {} | {} | {} |".format(
            hk, jk, c.get("idêntico", 0), c.get("contido", 0),
            c.get("parafraseado", 0), c.get("ausente na figura", 0)))
    w("")
    w("> **`mec` parafraseado em toda parte é desenho, não defeito.** A figura "
      "precisa de uma frase legível; `mecanismo_causal` carrega a prosa de "
      "auditoria. **O que é conferível é o NOME** — a frase até o primeiro `:` "
      "—, e é só isso que a coluna `espelho_nome_mecanismo` cobra.")
    w("")
    w("## 2. Nome do mecanismo: onde a figura e o codebook discordam")
    w("")
    w("**{} divergências**, contra a linha de base de **{}** medida em "
      "20/10/2026.".format(len(divergentes), DIVERGENCIAS_BASE))
    if len(divergentes) != DIVERGENCIAS_BASE:
        w("")
        w("> ⚠️ **A contagem mudou.** Se caiu, atualize `DIVERGENCIAS_BASE` no "
          "gerador dizendo no commit por que caiu. Se subiu, há figura "
          "envelhecendo.")
    w("")
    if divergentes:
        w("| Registro | A figura diz | O codebook diz |")
        w("|:--|:--|:--|")
        for pid, a, b in divergentes:
            w("| **{}** | {} | {} |".format(pid, curto(a), curto(b)))
    else:
        w("Nenhuma. A figura e o codebook nomeiam o mesmo mecanismo em todos "
          "os registros.")
    w("")
    if sem_figura:
        w("**Registros sem ponto na cronologia interativa:** {}.".format(
            ", ".join(sem_figura)))
        w("")
    w("## 3. A tabela, registro por registro")
    w("")
    w("A versão completa — com os seis campos da figura ao lado dos seis do "
      "codebook e o estado do espelho de cada um — está em "
      "`data/processed/tabela_espelho_eventos.csv`. Abaixo, a forma scanável.")
    w("")
    w("| id | data | evento na figura | fase | classe | nome do mecanismo | "
      "ponto | espelho |")
    w("|:--|:--|:--|:--|:--|:--|:--|:--|")
    for l in linhas:
        w("| `{}` | {} | {} | {} | {} | {} | {} | {} |".format(
            l["id"], l["data_hora"], curto(l["evento"], 40), l["fase"],
            l["status_classe"], curto(l["nome_mecanismo_codebook"], 60),
            l["ponto_na_figura"] or "—",
            "✅" if l["espelho_nome_mecanismo"] == "casa"
            else ("—" if l["espelho_nome_mecanismo"] == "sem figura" else "⚠️")))
    w("")
    MD_P.write_text("\n".join(out) + "\n", encoding="utf-8")

    print("{}: {} registros".format(MD_P.relative_to(RAIZ), len(linhas)))
    print("{}: {} colunas".format(CSV_P.relative_to(RAIZ), len(campos)))
    print("  pontos na cronologia      : {} ({} compostos)".format(
        len(set(h for h, _, _ in por_id.values())), len(COMPOSTOS)))
    print("  divergências de nome      : {} (base {})".format(
        len(divergentes), DIVERGENCIAS_BASE))
    for pid, a, b in divergentes:
        print("    ~ {:<8} figura: {}".format(pid, curto(a, 56)))
    if sem_figura:
        print("  sem ponto na interativa   : {}".format(", ".join(sem_figura)))
    if len(divergentes) != DIVERGENCIAS_BASE:
        print("  ! a contagem mudou — atualize DIVERGENCIAS_BASE e diga no commit")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
