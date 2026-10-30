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
    # INCLUSAO POR AUTORIZACAO TEM UM PRECO, e ele apareceu em 30/10/2026:
    # ela exclui o que ninguem autorizou, e a autorizacao aqui e por SUFIXO.
    # `LICENSE` nao tem extensao, de modo que a arvore publicavel sairia SEM
    # a licenca da obra -- no dia em que a licenca foi decidida. Por NOME, e
    # nao por sufixo novo, porque `endswith("license")` casaria qualquer
    # caminho terminado nessa palavra. **E note a assimetria da guarda deste
    # script: ela apaga o destino se peca RESERVADA VAZAR, e nada nela
    # acusaria a AUSENCIA de um arquivo que devia viajar.**
    POR_NOME = ("LICENSE",)
    aparato = [p for p in todos
               if p.lower().endswith(TEXTO)
               or os.path.basename(p).startswith(".git")
               or os.path.basename(p) in POR_NOME]
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
    # A CIFRA PARTIDA PELO MANIFESTO, que e quem define peca do corpus. Ate
    # 30/10/2026 esta linha somava todo PDF excluido e os chamava de "PDFs do
    # corpus" -- e o unico PDF versionado e um backup em `.backup_pre_lula/`.
    # Era a cifra certa no referente errado, a assinatura desta casa, dentro
    # do proprio relatorio. E a frase dizia "os 1 PDFs": **releia a frase com
    # o valor novo, e com zero.**
    pdfs_ex = [p for p in excluidos if p.lower().endswith(".pdf")]
    n_corpus = sum(1 for p in pdfs_ex if p in man)
    # A frase e VERBLESS de proposito: "%d nao sao" lia "1 nao sao".
    print("  EXCLUÍDOS %d arquivo(s) binário(s), %.0f MB — entre eles %d PDF(s) "
          "de peça do corpus e %d PDF(s) fora do corpus"
          % (len(excluidos), bytes_ex / 1e6, n_corpus,
             len(pdfs_ex) - n_corpus))
    print("  a verificabilidade do corpus não depende desta exportação: o "
          "manifesto viaja, com rota e SHA-256 de cada peça")
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
