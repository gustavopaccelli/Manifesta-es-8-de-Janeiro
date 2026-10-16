# -*- coding: utf-8 -*-
"""TAREFA 15 — o manifesto do corpus: reprodutivel sem ser redistribuivel.

O problema que este arquivo resolve. A auditoria de licenca mostrou que **27 das
40 pecas de literatura do corpus nao podem ser redistribuidas** -- duas declaram
todos os direitos reservados no proprio arquivo, e entre as 25 sem declaracao
estao livros da Cambridge, da Wiley-Blackwell, da Vozes e da Companhia das
Letras. Logo o corpus nao vai a remoto publico, e a pergunta passa a ser: **como
alguem verifica esta pesquisa sem receber os arquivos?**

Com o manifesto. Para cada peca: caminho, SHA-256, paginas, bytes, classe de
licenca lida NO arquivo, e a rota de obtencao declarada em PROCEDENCIA. Quem
quiser conferir uma ancora obtem a peca pela rota, compara o SHA-256 e abre a
pagina. **A verificabilidade nao depende da redistribuicao.**

E o manifesto serve a um segundo proposito, que vale por si: **detectar
corrupcao silenciosa do corpus**. Um PDF que muda de bytes sem mudar de nome
quebraria toda ancora que depende dele, e hoje nada acusaria. A checagem 8 de
verificar_integridade.py compara o corpus com este manifesto.

Regera com:  python scripts/gerar_manifesto_corpus.py
"""
import csv
import glob
import hashlib
import io
import json
import os
import sys
import warnings

import pypdf

warnings.filterwarnings("ignore")
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
os.chdir(RAIZ)
sys.path.insert(0, "scripts")

from auditar_licencas import FORA_DA_DOCUMENTAL, classifica  # noqa: E402
from gerar_codebook import PROCEDENCIA                       # noqa: E402

SAIDA = "Fontes/MANIFESTO-CORPUS.csv"
CODEBOOK = "process_tracing_8jan_eventos.json"
CAMPOS = ["caminho", "sha256", "paginas", "bytes", "licenca_declarada",
          "variante", "eixo", "documental", "procedencia"]


def sha256(cam):
    h = hashlib.sha256()
    with io.open(cam, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def ancoras_nao_pdf():
    """Os arquivos NAO-PDF que ancoram registro, lidos do `fonte_local`.

    ACRESCENTADO EM 16/10/2026, item 62, e o buraco que ele fecha foi achado
    dentro da propria nota que se apoiava nele. A `nota_auditoria` de PT-19A
    declarava, desde 15/10, que "a ancora e o arquivo inteiro, cujo SHA-256 a
    checagem 8 do ciclo vigia" -- e este gerador varria `Fontes/**/*.pdf`. O
    manifesto tinha 63 pecas, TODAS PDF: os dois arquivos nao-PDF que ancoram
    registro (o `.md` do NetLab em PT-19A e o `.html` do acordao do TSE em
    PT-03E) nao eram vigiados por nada. **Garantia declarada que ninguem
    confere e o modo de falha batizado deste projeto.**

    O conjunto sai do codebook, nao de lista a mao: anexo nao-PDF novo entra no
    manifesto no primeiro ciclo, ou a checagem 8 acusa "em disco e fora do
    manifesto". E o recorte e `fonte_local` porque e o que define ancora --
    LEIA-ME, bibliografia e .docx de teoria nao ancoram registro nenhum, e
    vigiar byte deles seria ruido.
    """
    dados = json.loads(io.open(CODEBOOK, encoding="utf-8").read())
    caminhos = set()
    for ev in dados["eventos"]:
        for p in (ev.get("fonte_local") or "").split(";"):
            p = p.strip().replace("\\", "/")
            if p and not p.lower().endswith(".pdf") and os.path.exists(p):
                caminhos.add(p)
    return sorted(caminhos)


def main():
    pdfs = sorted(p.replace("\\", "/") for p in
                  glob.glob("Fontes/**/*.pdf", recursive=True))
    linhas = []
    for cam in pdfs:
        eixo = cam.split("/")[1]
        doc = eixo not in FORA_DA_DOCUMENTAL
        cls, var, n = classifica(cam)
        if doc and cls in ("SEM", "ABERTA"):
            cls = "ATO OFICIAL"
        proc = PROCEDENCIA.get(cam)
        # A procedencia e a ROTA: e o que permite a outra pessoa obter a peca.
        rota = (proc[0] if proc else "NAO DECLARADA").replace("\n", " ")
        linhas.append({
            "caminho": cam,
            "sha256": sha256(cam),
            "paginas": n,
            "bytes": os.path.getsize(cam),
            "licenca_declarada": cls,
            "variante": var,
            "eixo": eixo,
            "documental": "sim" if doc else "nao",
            "procedencia": rota,
        })

    nao_pdf = ancoras_nao_pdf()
    for cam in nao_pdf:
        eixo = cam.split("/")[1]
        doc = eixo not in FORA_DA_DOCUMENTAL
        proc = PROCEDENCIA.get(cam)
        rota = (proc[0] if proc else "NAO DECLARADA").replace("\n", " ")
        linhas.append({
            "caminho": cam,
            "sha256": sha256(cam),
            # paginas = 0 nao e "zero paginas": e NAO PAGINADO. Fica 0 e nao
            # vazio porque `medir_corpus` soma esta coluna com int().
            "paginas": 0,
            "bytes": os.path.getsize(cam),
            # NAO herda o "ATO OFICIAL" que o laco dos PDFs aplica por padrao a
            # peca documental: `classifica` abre PDF, de modo que aqui a licenca
            # nao foi lida no arquivo -- e o post do NetLab nao e ato oficial
            # nenhum. Declarar o que nao se conferiu era o erro a evitar.
            "licenca_declarada": "NAO CONFERIDA (nao-PDF)",
            "variante": "",
            "eixo": eixo,
            "documental": "sim" if doc else "nao",
            "procedencia": rota,
        })
    linhas.sort(key=lambda l: l["caminho"])

    with io.open(SAIDA, "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=CAMPOS)
        w.writeheader()
        w.writerows(linhas)

    sem_rota = [l for l in linhas if l["procedencia"] == "NAO DECLARADA"]
    print("%s: %d peças" % (SAIDA, len(linhas)))
    print("  %d PDFs + %d âncora(s) não-PDF (%s)"
          % (len(pdfs), len(nao_pdf),
             ", ".join(c.rsplit("/", 1)[-1] for c in nao_pdf) or "nenhuma"))
    # A cifra documental DESTE arquivo nao e a linha de base da checagem 6 e, a
    # partir de 16/10/2026, as duas nao coincidem mais: a checagem 6 mede 22
    # PDFs / 6.951 p. varrendo o DISCO so por PDF, e aqui entram tambem as
    # ancoras nao-PDF. Duas medidas de nomes parecidos e recortes diferentes e o
    # modo de falha batizado deste projeto -- por isso a linha diz o recorte.
    print("  %d documentais (dos quais %d não-PDF — a linha de base da checagem 6"
          " é de PDF: 22 / 6.951 p.), %d de literatura"
          % (sum(1 for l in linhas if l["documental"] == "sim"),
             sum(1 for l in linhas if l["documental"] == "sim" and not l["paginas"]),
             sum(1 for l in linhas if l["documental"] == "nao")))
    print("  %.0f MB no total" % (sum(l["bytes"] for l in linhas) / 1e6))
    if sem_rota:
        # O %d nasceu sem argumento em 13/10/2026 e imprimia o proprio marcador:
        # o aviso funcionava, a cifra nao existia. Corrigido na rodada seguinte.
        print("  ! %d peça(s) SEM rota declarada em PROCEDENCIA — quem for conferir"
              % len(sem_rota))
        print("    esta pesquisa não teria como obtê-las:")
        for l in sem_rota:
            print("      %s" % l["caminho"])
    else:
        print("  OK — toda peça tem rota de obtenção declarada")
    return 0


if __name__ == "__main__":
    sys.exit(main())
