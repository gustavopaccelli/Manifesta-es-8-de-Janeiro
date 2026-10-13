# -*- coding: utf-8 -*-
"""TAREFA 15 — exporta o APARATO para publicacao, sem o corpus.

POR QUE ISTO EXISTE, e nao e preferencia: a auditoria de licenca de 13/10/2026
mostrou que **27 das 40 pecas de literatura do corpus nao podem ser
redistribuidas**. Duas declaram todos os direitos reservados no proprio arquivo
-- Kunrath Silva (2018) e Tatagiba (2018), as duas pela Lusotopie -- e entre as
25 sem declaracao estao Tarrow pela Vozes, Dynamics of Contention pela
Cambridge, a enciclopedia da Wiley-Blackwell e Alonso pela Companhia das Letras.
**Logo o repositorio deste projeto nao vai a remoto publico.**

E NAO BASTA PARAR DE VERSIONAR O CORPUS AGORA: os PDFs estao no HISTORICO, e o
.git tem 250 MB por causa deles. Um remoto publico deste repositorio
distribuiria os arquivos mesmo que a arvore de trabalho ficasse limpa. A unica
publicacao segura e **um repositorio novo, sem historico**, com o aparato.

O QUE ESTE SCRIPT FAZ: monta essa arvore num diretorio a parte e **se recusa a
terminar** se qualquer peca nao redistribuivel tiver escapado. A seguranca e por
CONSTRUCAO, conferida contra o manifesto -- nao por cuidado de quem executa.

O QUE ELE NAO FAZ, de proposito: nao cria remoto, nao faz commit e nao publica
nada. Publicar e ato do pesquisador, e irreversivel.

uso:  python scripts/exportar_aparato.py [destino]
      (destino padrao: ../8-de-janeiro-aparato)
"""
import csv
import io
import os
import shutil
import subprocess
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
os.chdir(RAIZ)

MANIFESTO = "Fontes/MANIFESTO-CORPUS.csv"
# Classes que NAO podem sair daqui. "SEM" entra na lista porque desconhecido
# conta como reservado por omissao -- foi a regra fixada na auditoria.
BARRADAS = {"RESERVADA", "SEM", "ILEGIVEL"}


def versionados():
    r = subprocess.run(["git", "ls-files", "-z"], capture_output=True, check=True)
    return [p for p in r.stdout.decode("utf-8").split("\0") if p]


def main():
    destino = os.path.abspath(sys.argv[1] if len(sys.argv) > 1
                              else os.path.join(RAIZ, "..", "8-de-janeiro-aparato"))
    if not os.path.exists(MANIFESTO):
        print("X manifesto ausente — rode primeiro "
              "python scripts/gerar_manifesto_corpus.py")
        return 1
    with io.open(MANIFESTO, encoding="utf-8-sig", newline="") as fh:
        man = {r["caminho"]: r for r in csv.DictReader(fh)}

    todos = versionados()
    # INCLUSAO POR AUTORIZACAO, nao exclusao por caminho. A primeira versao deste
    # script excluia "Fontes/**/*.pdf" e VAZOU um PDF de 24,7 MB que estava em
    # .backup_pre_lula/ -- regra de caminho falha no caminho que ninguem lembrou.
    # Aqui o default e EXCLUIR: entra texto e codigo, e binario so por lista.
    TEXTO = (".md", ".py", ".json", ".csv", ".sh", ".html", ".svg", ".txt",
             ".jsonl", ".gitignore", ".gitattributes", ".yml", ".yaml", ".toml")
    aparato = [p for p in todos
               if p.lower().endswith(TEXTO) or os.path.basename(p).startswith(".git")]
    excluidos = [p for p in todos if p not in set(aparato)]

    if os.path.exists(destino):
        print("X o destino já existe: %s" % destino)
        print("  apague-o ou escolha outro — este script não sobrescreve.")
        return 1
    for rel in aparato:
        alvo = os.path.join(destino, rel)
        os.makedirs(os.path.dirname(alvo), exist_ok=True)
        shutil.copyfile(os.path.join(RAIZ, rel), alvo)

    # --------------------------------------------------- a guarda, por construcao
    vazou = []
    for raiz, _, arqs in os.walk(destino):
        for a in arqs:
            rel = os.path.relpath(os.path.join(raiz, a), destino).replace("\\", "/")
            cls = (man.get(rel) or {}).get("licenca_declarada")
            if cls in BARRADAS:
                vazou.append((rel, cls))
    if vazou:
        print("X A EXPORTAÇÃO VAZOU PEÇA NÃO REDISTRIBUÍVEL — nada foi publicado:")
        for rel, cls in vazou:
            print("    %-12s %s" % (cls, rel))
        shutil.rmtree(destino)
        print("  o destino foi apagado. Corrija o filtro antes de tentar de novo.")
        return 1

    # --------------------------------------------------- o que saiu e o que ficou
    bytes_ap = sum(os.path.getsize(os.path.join(RAIZ, p)) for p in aparato)
    bytes_ex = sum(os.path.getsize(os.path.join(RAIZ, p)) for p in excluidos)
    print("APARATO EXPORTADO para %s" % destino)
    print("  %d arquivo(s) de texto e código, %.1f MB" % (len(aparato), bytes_ap / 1e6))
    print("  EXCLUÍDOS %d arquivo(s) binário(s), %.0f MB — entre eles os %d PDFs do "
          "corpus, de que fica só o manifesto, com rota e SHA-256 de cada peça"
          % (len(excluidos), bytes_ex / 1e6,
             sum(1 for p in excluidos if p.lower().endswith(".pdf"))))
    print("  guarda: nenhuma peça RESERVADA/SEM/ILEGÍVEL no resultado, conferido "
          "contra o manifesto")
    print()
    print("  BINÁRIOS EXCLUÍDOS QUE PODEM SER SEUS — diga se quer algum na publicação:")
    for p in sorted(excluidos):
        if p.startswith("Fontes/") and p.lower().endswith(".pdf"):
            continue                 # o corpus e o caso obvio, ja contado acima
        print("      %7.1f MB  %s" % (os.path.getsize(os.path.join(RAIZ, p)) / 1e6, p))
    print("  Publicá-los é decisão sua, e é por isso que o script os LISTA em vez")
    print("  de decidir — e por isso que o default é EXCLUIR.")
    print()
    print("ESTE SCRIPT NÃO PUBLICOU NADA. Para publicar, de dentro do destino:")
    print("    git init && git add -A && git commit -m \"aparato\" && git remote add ...")
    print("Publicar é irreversível, e é ato do pesquisador.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
