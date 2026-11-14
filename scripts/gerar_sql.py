#!/usr/bin/env python3
"""JSON -> SQL: o codebook e os três ledgers em tabelas relacionais.

O JSON continua a fonte única da verdade. Este gerador produz dois derivados:

- data/processed/codebook.sql  -- texto determinístico (CREATE + INSERT),
  versionado, diffável. É o que o histórico do git mostra.
- data/processed/codebook.db   -- SQLite construído a partir do .sql,
  NÃO versionado (binário não tem diff). Regere com este script.

Tabelas: eventos, metadados, tarefas, decisoes, pecas_lidas. Todas têm `ordem`
(posição no JSON) para que a ordem original sobreviva à consulta.

A guarda final reabre o .db e confere, valor por valor, contra o JSON. Se
qualquer célula divergir, ou se a contagem de eventos não bater com
metadados.n_subeventos, o gerador sai com código != 0.
"""
import json
import re
import sqlite3
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FONTE = RAIZ / "process_tracing_8jan_eventos.json"
TAREFAS = RAIZ / "data" / "ordem_de_ataque.json"
DECISOES = RAIZ / "data" / "decisoes_abertas.json"
LEITURA = RAIZ / "data" / "estado_de_leitura.json"
SAIDA_SQL = RAIZ / "data" / "processed" / "codebook.sql"
SAIDA_DB = RAIZ / "data" / "processed" / "codebook.db"

IDENT = re.compile(r"^[a-z_][a-z0-9_]*$")


def ler(caminho):
    return json.loads(caminho.read_text(encoding="utf-8"))


def valor_sql(v):
    """Texto para a célula. Str passa como está; o resto vira JSON em texto."""
    if v is None:
        return None
    if isinstance(v, str):
        return v
    return json.dumps(v, ensure_ascii=False, sort_keys=True)


def literal(v):
    t = valor_sql(v)
    if t is None:
        return "NULL"
    if "\x00" in t:
        raise ValueError("NUL em valor: a instrução SQL seria truncada")
    return "'" + t.replace("'", "''") + "'"


def linhas_de(obj):
    """Lista de dicts segue como está; dict de dicts vira lista com a chave em `chave`."""
    if isinstance(obj, list):
        return obj
    return [dict(chave=k, **v) for k, v in obj.items()]


def colunas_de(linhas):
    """União das chaves na ordem em que aparecem; nomes têm de ser identificadores simples."""
    cols = []
    for r in linhas:
        for k in r:
            if k not in cols:
                cols.append(k)
    for c in cols:
        if not IDENT.match(c):
            raise ValueError("nome de coluna fora do padrão: %r" % c)
    return cols


def tabela(nome, linhas, pk=None):
    """Devolve (cabecalho SQL, lista de tuplas) para uma tabela."""
    cols = colunas_de(linhas)
    cab = ['"ordem" INTEGER NOT NULL']
    for c in cols:
        cab.append('"%s" TEXT%s' % (c, " PRIMARY KEY" if c == pk else ""))
    create = 'CREATE TABLE %s (%s);' % (nome, ", ".join(cab))
    inserts = []
    for i, r in enumerate(linhas, 1):
        vals = [str(i)] + [literal(r.get(c)) for c in cols]
        inserts.append("INSERT INTO %s VALUES (%s);" % (nome, ", ".join(vals)))
    return create, inserts, cols


def montar():
    ev = ler(FONTE)
    tarefas = ler(TAREFAS)["tarefas"]
    decisoes = ler(DECISOES)["decisoes"]
    pecas = linhas_de(ler(LEITURA)["pecas"])

    meta = ev["metadados"]
    meta_linhas = [{"chave": k, "valor_json": valor_sql(v)} for k, v in meta.items()]

    blocos = []
    specs = [
        ("eventos", linhas_de(ev["eventos"]), "id"),
        ("metadados", meta_linhas, "chave"),
        ("tarefas", tarefas, None),
        ("decisoes", decisoes, None),
        ("pecas_lidas", pecas, None),
    ]
    dados = {}
    for nome, linhas, pk in specs:
        create, inserts, cols = tabela(nome, linhas, pk)
        blocos.append((nome, create, inserts))
        dados[nome] = (linhas, cols)
    return blocos, dados


def escrever_sql(blocos):
    partes = [
        "-- Gerado por scripts/gerar_sql.py a partir do JSON e dos ledgers.",
        "-- NÃO EDITAR: a próxima execução sobrescreve. A fonte é o JSON.",
        "BEGIN;",
    ]
    for nome, create, inserts in blocos:
        partes.append("")
        partes.append("-- " + nome)
        partes.append(create)
        partes.extend(inserts)
    partes.append("COMMIT;")
    SAIDA_SQL.parent.mkdir(parents=True, exist_ok=True)
    with open(SAIDA_SQL, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(partes) + "\n")


def construir_db():
    if SAIDA_DB.exists():
        SAIDA_DB.unlink()
    con = sqlite3.connect(str(SAIDA_DB))
    try:
        con.executescript(SAIDA_SQL.read_text(encoding="utf-8"))
    finally:
        con.close()


def conferir(dados, meta_n_subeventos):
    """Reabre o .db e compara cada célula com o JSON. Devolve lista de falhas."""
    falhas = []
    con = sqlite3.connect(str(SAIDA_DB))
    try:
        integ = con.execute("PRAGMA integrity_check").fetchone()[0]
        if integ != "ok":
            falhas.append("integrity_check devolveu %r" % integ)
        for nome, (linhas, cols) in dados.items():
            n_db = con.execute("SELECT COUNT(*) FROM %s" % nome).fetchone()[0]
            if n_db != len(linhas):
                falhas.append("%s: %d linhas no banco, %d no JSON" % (nome, n_db, len(linhas)))
                continue
            sel = ", ".join('"%s"' % c for c in cols)
            rows = con.execute("SELECT %s FROM %s ORDER BY ordem" % (sel, nome)).fetchall()
            for i, (r, row) in enumerate(zip(linhas, rows), 1):
                for c, celula in zip(cols, row):
                    esperado = valor_sql(r.get(c))
                    if esperado != celula:
                        falhas.append("%s[%d].%s: banco %r, JSON %r"
                                      % (nome, i, c, celula, esperado))
        n_ev = con.execute("SELECT COUNT(*) FROM eventos").fetchone()[0]
        if n_ev != meta_n_subeventos:
            falhas.append("eventos: %d no banco, metadados.n_subeventos = %d"
                          % (n_ev, meta_n_subeventos))
    finally:
        con.close()
    return falhas


def main():
    blocos, dados = montar()
    escrever_sql(blocos)
    construir_db()
    n_sub = ler(FONTE)["metadados"]["n_subeventos"]
    falhas = conferir(dados, n_sub)
    if falhas:
        print("X gerar_sql: o banco diverge do JSON")
        for f in falhas[:30]:
            print("   -", f)
        if len(falhas) > 30:
            print("   ... e mais %d" % (len(falhas) - 30))
        return 1
    print("OK gerar_sql: %s e %s conferidos contra o JSON (%d eventos)"
          % (SAIDA_SQL.name, SAIDA_DB.name, len(dados["eventos"][0])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
