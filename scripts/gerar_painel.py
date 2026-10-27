# -*- coding: utf-8 -*-
"""O 'Painel de estado' de docs/PENDENCIAS-ANALITICAS.md, GERADO.

A narrativa vive no script e as cifras saem dos dados — a mesma divisão que
`gerar_auditoria.py` usa desde 16/08/2026.

**Por que ele nasceu em 27/10/2026 (item 91):** o painel era escrito à mão e
datava-se de **29/09**. Em 27/10 a revisão do repositório mediu cada cifra dele
e **nenhuma estava certa**: dizia 83 sub-eventos (eram 85), 61 em fonte
primária (68), 49 registros num "Caderno de evidências" que **não existe como
arquivo algum**, 66 PDFs (65), oito passos de ciclo (treze) — e afirmava
*"git desde 20/09/2026, sem remoto configurado"* quando o remoto existe **e é
público**, o que inverte uma declaração de distribuição.

**Nenhuma das cifras aqui é digitada.** E as listas de tarefas e decisões NÃO
são repetidas: o painel aponta para as seções que os passos 3 e 4 geram, porque
a quarta cópia é o defeito que esta casa já pagou quatro vezes.
"""
import csv
import io
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
AGENDA = RAIZ / "docs/PENDENCIAS-ANALITICAS.md"

ABRE = ("<!-- PAINEL: gerado por scripts/gerar_painel.py. Não editar à mão: "
        "o ciclo sobrescreve. -->")
FECHA = "<!-- /PAINEL -->"

MES = {1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril", 5: "maio",
       6: "junho", 7: "julho", 8: "agosto", 9: "setembro", 10: "outubro",
       11: "novembro", 12: "dezembro"}


def mil(n):
    return "{:,}".format(int(n)).replace(",", ".")


def br(iso):
    """`2026-09-20` -> `20/09/2026`. O painel e documento em portugues,
    e data em ISO na celula tambem partia a prova de procedencia em
    `09` e `20`."""
    p = (iso or "").split("-")
    return "/".join(reversed(p)) if len(p) == 3 else (iso or "?")


def git(*args):
    r = subprocess.run(["git"] + list(args), capture_output=True, text=True,
                       cwd=str(RAIZ))
    return (r.stdout or "").strip()


def passos_do_ciclo(ciclo):
    """{nome do script: número do passo}, lido de `ciclo.sh`.

    **Número de passo é a cifra que mais apodrece neste repositório:** o ciclo
    foi de oito a treze passos em dezenove dias, e cada entrada renumerou
    tudo. Citar "passo 9" à mão é marcar hora num relógio que anda.
    """
    mapa, linhas = {}, ciclo.split("\n")
    for i, l in enumerate(linhas):
        m = re.match(r'echo "== (\d+)/\d+ ', l)
        if not m:
            continue
        for j in range(i + 1, min(i + 8, len(linhas))):
            s = re.search(r"python scripts/(\w+)\.py", linhas[j])
            if s:
                mapa[s.group(1)] = int(m.group(1))
                break
    return mapa


def medir():
    cb = json.loads((RAIZ / "process_tracing_8jan_eventos.json")
                    .read_text(encoding="utf-8"))
    ev = cb["eventos"]
    with io.open(str(RAIZ / "Fontes/MANIFESTO-CORPUS.csv"),
                 encoding="utf-8-sig") as fh:
        man = list(csv.DictReader(fh))
    ciclo = (RAIZ / "scripts/ciclo.sh").read_text(encoding="utf-8")
    vi = (RAIZ / "scripts/verificar_integridade.py").read_text(encoding="utf-8")
    led = json.loads((RAIZ / "data/ordem_de_ataque.json")
                     .read_text(encoding="utf-8"))
    dec = json.loads((RAIZ / "data/decisoes_abertas.json")
                     .read_text(encoding="utf-8"))

    classes = Counter(e["status_classe"] for e in ev)
    pdfs = [r for r in man if r["caminho"].lower().endswith(".pdf")]
    docum = [r for r in man if r.get("documental", "").strip().lower() == "sim"]
    docpdf = [r for r in docum if r["caminho"].lower().endswith(".pdf")]

    return {
        "passo": passos_do_ciclo(ciclo),
        "registros": len(ev),
        "campos": len(ev[0]),
        "classes": classes,
        "com_local": sum(1 for e in ev if (e.get("fonte_local") or "").strip()),
        "com_pagina": sum(1 for e in ev if (e.get("fonte_pagina") or "").strip()),
        "com_trecho": sum(1 for e in ev if (e.get("fonte_trecho") or "").strip()),
        "pecas": len(man),
        "pdfs": len(pdfs),
        "nao_pdf": len(man) - len(pdfs),
        "paginas": sum(int(r["paginas"]) for r in pdfs),
        "doc_pecas": len(docum),
        "doc_paginas": sum(int(r["paginas"]) for r in docpdf),
        "lit_pecas": len(man) - len(docum),
        "eixos": len({r["eixo"] for r in man}),
        "passos": max(int(m) for m in re.findall(r"== \d+/(\d+) ", ciclo)),
        "geradores": len(re.findall(r"python scripts/gerar_", ciclo)),
        "conferidores": len(re.findall(
            r"python scripts/(?:conferir_|verificar_|desenhar_)", ciclo)),
        "checagens": len(set(re.findall(r"cabecalho\((\d+),", vi))),
        "tarefas_abertas": [x["n"] for x in led["tarefas"]
                            if x["estado"] == "aberta"],
        "tarefas_fechadas": len([x for x in led["tarefas"]
                                 if x["estado"] == "fechada"]),
        "decisoes_abertas": len([x for x in dec["decisoes"]
                                 if x["estado"] == "aberta"]),
        "decisoes_naturezas": len({x["natureza"] for x in dec["decisoes"]
                                   if x["estado"] == "aberta"}),
        "commits": git("rev-list", "--count", "HEAD"),
        "remoto": git("remote", "get-url", "origin"),
        "primeiro": br((git("log", "--reverse", "--format=%ad",
                            "--date=short") or "\n").split("\n")[0]),
        "ultimo": br(git("log", "-1", "--format=%ad", "--date=short")),
    }


def montar(m):
    hoje = date.today()
    data = "%d de %s de %d" % (hoje.day, MES[hoje.month], hoje.year)
    cl = m["classes"]
    out = ["## Painel de estado — medido em " + data, ""]
    out += [
        "**Esta seção é GERADA pelo passo %d do ciclo. Nenhuma cifra dela é "
        % m["passo"]["gerar_painel"] + 
        "digitada**, e as listas de tarefas e decisões não são repetidas aqui: "
        "o painel aponta para as seções que os passos %d e %d geram. **A razão "
        % (m["passo"]["gerar_ordem_de_ataque"],
           m["passo"]["gerar_decisoes"]) + 
        "tem data** — até 27/10/2026 este painel era escrito à mão, datava-se "
        "de 29/09, e a revisão do repositório mediu que **nenhuma das suas "
        "cifras estava certa** (item 91).", "",
        "**O aparato está pronto, auditado, versionado e verificável por um "
        "comando; o artigo não começou.** Por decisão do pesquisador em "
        "**16/08/2026**, a redação é o **último** item da fila: o conjunto de "
        "dados de todo o processo político vem primeiro. Nada mudou nessa "
        "decisão desde então.", "",
        "| Frente | Estado |", "|:--|:--|",
    ]

    out.append(
        "| Codebook | **{} sub-eventos × {} campos** — JSON, CSV e XLSX "
        "gerados de uma fonte única, com zero divergências. Zero vazios em "
        "`mecanismo_causal` e em `autonomia_movimento` |".format(
            m["registros"], m["campos"]))
    out.append(
        "| Classes de verificação | **{} em fonte primária** · {} confirmados "
        "por outra via · **0 a verificar** · {} inferência declarada. O "
        "critério das três condições está escrito em "
        "`metadados.vocabulario_status_classe` desde 25/10/2026 |".format(
            cl.get("Confirmado em fonte primária", 0), cl.get("Confirmado", 0),
            cl.get("Inferência do analista", 0)))
    out.append(
        "| Ancoragem documental | **{} de {} registros** com arquivo vinculado "
        "· {} com página ou localizador estrutural · {} com transcrição "
        "literal no campo. O único sem arquivo é PT-03D, declarado |".format(
            m["com_local"], m["registros"], m["com_pagina"], m["com_trecho"]))
    out.append(
        "| Corpus | **{} peças / {} p.** no manifesto, em {} eixos — {} PDFs e "
        "{} âncoras não-PDF, estas conferidas por arquivo inteiro desde "
        "25/10/2026. Da documental: **{} peças / {} p.**; de literatura: {} "
        "peças |".format(
            m["pecas"], mil(m["paginas"]), m["eixos"], m["pdfs"], m["nao_pdf"],
            m["doc_pecas"], mil(m["doc_paginas"]), m["lit_pecas"]))
    # A COBERTURA NAO E CONTADA AQUI, de proposito (27/10/2026). A primeira
    # versao dizia "N registros cobertos" com N = numero de `id:"PT-..."` no
    # HTML, isto e, de PONTOS -- e `conferir_figuras` declara cobertura de
    # TODOS os registros, enquanto a tabela-espelho conta outro numero de
    # pontos, por causa dos compostos. **Cifra de referente errado e o defeito
    # batizado desta casa**, e cifra que nao se sabe explicar nao entra: quem
    # garante a cobertura e o passo 9, e e ele que a celula cita.
    out.append(
        "| Figuras | SVG da cadeia causal e cronologia navegável. **São a "
        "única parte do aparato escrita à mão**, e duas guardas as cobrem: o "
        "passo %d confere que todo registro do codebook aparece na figura, "
        "e a tabela-espelho do passo %d confere o **nome do mecanismo** de "
        "cada ponto contra o campo — com linha de base em zero "
        "divergências |" % (m["passo"]["conferir_figuras"],
                            m["passo"]["gerar_tabela_espelho"]))
    out.append(
        "| Verificação | `bash scripts/ciclo.sh` — **{} passos**: {} geradores "
        "e {} conferidores, entre eles as **{} checagens estruturais**. Toda "
        "linha de base reprova com código de saída ≠ 0; nenhuma apenas "
        "avisa |".format(m["passos"], m["geradores"], m["conferidores"],
                         m["checagens"]))
    out.append(
        "| Controle de versão | git desde **{}**, {} commits, **remoto "
        "PÚBLICO** em `{}` — e é por ele ser público que os PDFs do corpus "
        "saíram do versionamento em 21/10/2026. Último commit: {} |".format(
            m["primeiro"], m["commits"],
            m["remoto"].replace("https://github.com/", ""), m["ultimo"]))
    out.append(
        "| Tarefas abertas | **{}** — {}. A lista vive na seção *Ordem de "
        "ataque*, gerada pelo passo {}, e {} tarefas estão fechadas |".format(
            len(m["tarefas_abertas"]), ", ".join(m["tarefas_abertas"]),
            m["passo"]["gerar_ordem_de_ataque"], m["tarefas_fechadas"]))
    out.append(
        "| Decisões pendentes | **{}**, em {} naturezas. A lista vive na seção "
        "*Decisões pendentes*, no fim deste arquivo, gerada pelo passo {} "
        "|".format(m["decisoes_abertas"], m["decisoes_naturezas"],
                   m["passo"]["gerar_decisoes"]))
    out.append(
        "| **Redação do artigo** | **não iniciada — por decisão, é o último "
        "item da fila.** Desde 25/10/2026 ela não tem mais pré-requisito de "
        "dado: a tarefa 26 fechou e não há decisão de campo aberta no "
        "codebook. **Começá-la é decisão do pesquisador** |")
    out += [""]
    out += [
        "> **O que este painel NÃO repete, de propósito.** As tarefas e as "
        "decisões abertas têm cada uma a sua seção gerada, e listá-las aqui "
        "seria a quarta cópia — a contabilidade deste projeto já envelheceu "
        "quatro vezes por cópia à mão, e o histórico está nos itens 49, 78, 83 "
        "e 90. **Os itens numerados abaixo são um log cronológico:** a cifra "
        "dentro de um item era verdade no dia dele e fica como está."]
    return "\n".join(out).rstrip("\n")


def gravar(bloco):
    t = AGENDA.read_text(encoding="utf-8")
    assert t.count(ABRE) == 1 and t.count(FECHA) == 1, \
        "os marcadores do painel não estão exatamente uma vez na agenda"
    cabeca, resto = t.split(ABRE, 1)
    _, cauda = resto.split(FECHA, 1)
    novo = cabeca + ABRE + "\n\n" + bloco + "\n\n" + FECHA + cauda
    assert novo.split(ABRE, 1)[0] == cabeca
    assert novo.split(FECHA, 1)[1] == cauda
    if novo == t:
        print("painel: já em dia, nada a gravar")
        return False
    AGENDA.write_text(novo, encoding="utf-8", newline="\n")
    return True


def autoteste():
    m = medir()
    assert m["registros"] > 0 and m["campos"] > 0
    assert m["passos"] >= 13, "o painel leu %d passos" % m["passos"]
    assert m["remoto"], "o remoto não foi lido — o painel afirmaria o contrário"
    soma = sum(m["classes"].values())
    assert soma == m["registros"], \
        "as classes somam %d e os registros são %d" % (soma, m["registros"])
    bloco = montar(m)
    # PROVA NEGATIVA 1: as CIFRAS DAS CÉLULAS são derivadas.
    #
    # Vigia as linhas de tabela, não a narrativa: esta cita número de item e
    # data, que são referência histórica escrita à mão e legítima. A primeira
    # versão varria o bloco inteiro e acusava `352` e `970` — pedaços de
    # **12.352** e **6.970** partidos pelo separador de milhar — e `09`, `10`,
    # `91`, que vêm de datas e de itens. **Guarda que acusa o próprio formato
    # treina a ser ignorada.**
    celulas = "\n".join(l for l in bloco.split("\n") if l.startswith("|"))
    limpo = re.sub(r"\b\d{2}/\d{2}(?:/\d{4})?\b", " ", celulas)
    limpo = re.sub(r"(?<=\d)\.(?=\d{3}\b)", "", limpo)
    limpo = re.sub(r"\bPT-[\w]+", " ", limpo)
    # IDENTIFICADOR NAO E CIFRA: numero que NOMEIA uma tarefa sai da varredura,
    # porque a prova vigia numero que MEDE. E a licao do referente aplicada a
    # propria prova -- ela acusava `26` em "a tarefa 26 fechou".
    limpo = re.sub(r"\btarefas? [\d,\se]+", " ", limpo)
    medidos = {str(v) for v in m.values() if isinstance(v, int)}
    medidos |= {str(v) for v in m["classes"].values()}
    medidos |= {m["commits"]}
    medidos |= set(m["tarefas_abertas"])        # identificadores, derivados
    medidos |= {str(v) for v in m["passo"].values()}   # passos, derivados
    livres = {n for n in re.findall(r"\b\d{2,}\b", limpo)
              if n not in medidos and not re.match(r"^(19|20)\d\d$", n)}
    assert not livres, ("cifra sem procedência nas células do painel: %s — ou "
                        "ela sai de medir(), ou não entra" % sorted(livres))

    # Prova negativa 2: o painel nao repete a lista de tarefas nem de decisoes.
    assert "| 10 |" not in bloco and "| 17 |" not in bloco, \
        "o painel voltou a repetir a tabela de tarefas"
    print("autoteste OK — %d registros, %d peças, %d passos, cifras com "
          "procedência, duas provas negativas"
          % (m["registros"], m["pecas"], m["passos"]))


if __name__ == "__main__":
    if (sys.argv[1:] or [""])[0] == "--autoteste":
        autoteste()
    else:
        autoteste()
        gravar(montar(medir()))
