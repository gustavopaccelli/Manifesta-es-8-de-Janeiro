# -*- coding: utf-8 -*-
"""TAREFA 15 — auditoria de licenca do corpus, peca por peca.

Pergunta: o que CADA ARQUIVO declara sobre a propria redistribuicao?

Nao se infere licenca do editor nem do registro de acesso aberto: le-se o que
esta impresso no arquivo. A razao e o caso Rich (2021), de 08/10/2026 -- o
OpenAlex a declarava OURO e ela esta a venda em livraria. **Registro de acesso
aberto pode estar errado sobre a licenca**; o arquivo e o que vale.

Classes devolvidas:
  CC          licenca Creative Commons declarada NO arquivo, com a variante
  ABERTA      declaracao de acesso aberto sem nome de licenca
  RESERVADA   todos os direitos reservados, declarado
  SEM         nenhuma declaracao encontrada -- e **SEM nao e livre**: e
              desconhecido, e desconhecido conta como reservado por omissao
"""
import collections
import glob
import hashlib
import io
import os
import re
import sys
import unicodedata
import warnings

import pypdf

warnings.filterwarnings("ignore")
RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
os.chdir(RAIZ)

# Padroes procurados no texto normalizado (sem acento, minusculo).
CC = re.compile(r"creative commons|creativecommons\.org|\bcc[ -]?by\b|\bcc[ -]?by[ -]?"
                r"(nc|sa|nd)\b")
VARIANTE = re.compile(r"cc[ -]?by(?:[ -]?(?:nc|sa|nd))*", re.I)
ABERTA = re.compile(r"open access|acesso aberto|acceso abierto|openaccess")

# MENCAO NAO E DECLARACAO — acrescentado em 13/10/2026, e o caso que forcou isto e
# do proprio projeto: o deposito de Amsterdam de Snow, Vliegenthart e Ketelaars
# (2019) diz "other than for strictly personal, individual use, UNLESS the work is
# under an open content license (like creative commons)". A frase afirma que a obra
# NAO esta sob CC, e o classificador a leu como declaracao de CC. E a cifra certa no
# referente errado aplicada a licenca.
#
# A regra e estreita de proposito: so desqualifica o casamento que esta DENTRO de
# uma hipotese. Nao usa "except", porque "except where otherwise noted, is licensed
# under a creative commons..." -- que e a formula das tres obras da EdUERJ e da
# Editora UnB no corpus -- e limitacao de ESCOPO de uma licenca real, nao negacao
# dela. Reauditadas as 15 pecas classificadas CC em 13/10/2026, uma a uma, com o
# contexto de cada casamento: 14 eram declaracao e 1 era esta hipotese.
CONTRAFACTUAL = re.compile(r"(?:unless|a menos que|salvo se|caso a obra)"
                           r"[^.]{0,90}$")

# "Todos os direitos reservados" NAO e a unica forma de reservar direitos, e supor
# que fosse deixaria a peca de 13/10 cair em ABERTA -- porque a folha de capa do
# deposito cita openaccess.nl. Duas formas novas, as duas lidas no arquivo:
# a PROIBICAO EXPLICITA de redistribuir, e o art. 25fa da lei holandesa (emenda
# Taverne), que autoriza o deposito para uso pessoal e veda a redistribuicao.
RESERVADA = re.compile(r"todos os direitos reservados|all rights reserved|"
                       r"tous droits reserves|todos los derechos reservados|"
                       r"not permitted to download|not permitted to forward|"
                       r"nao e permitido .{0,40}distribuir|"
                       r"article 25fa|artikel 25fa")


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").lower()
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s)


def sha256(cam):
    h = hashlib.sha256()
    with io.open(cam, "rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def classifica(cam):
    """Le as 6 primeiras e as 3 ultimas paginas: e onde a licenca vive."""
    try:
        r = pypdf.PdfReader(cam)
    except Exception as exc:                     # noqa: BLE001
        return "ILEGIVEL", str(exc)[:40], 0
    n = len(r.pages)
    alvo = list(range(min(6, n))) + list(range(max(0, n - 3), n))
    txt = norm(" ".join((r.pages[i].extract_text() or "") for i in sorted(set(alvo))))
    # CC vale se HOUVER ao menos um casamento que nao esteja dentro de hipotese.
    # A varredura e por casamento, nao pelo texto todo: uma peca pode mencionar CC
    # numa hipotese E declarar CC em outro lugar, e nesse caso a declaracao vence.
    afirmativo = [m for m in CC.finditer(txt)
                  if not CONTRAFACTUAL.search(txt[max(0, m.start() - 90):m.start()])]
    if afirmativo:
        m = VARIANTE.search(txt)
        v = re.sub(r"[ ]+", "-", m.group(0).upper().replace("CC ", "CC-")) if m else "CC"
        return "CC", v, n
    if RESERVADA.search(txt):
        return "RESERVADA", "", n
    if ABERTA.search(txt):
        return "ABERTA", "", n
    return "SEM", "", n


# Mesma linha de corte de verificar_integridade.py: nao se inventa taxonomia nova.
FORA_DA_DOCUMENTAL = {"05_Bibliografia-teorica", "12_Camada-T-1_Literatura",
                      "13_Bolsonarismo-mobilizacao", "14_Livros-brasileiros",
                      "15_Comparado-6-de-janeiro"}


def main():
    pdfs = sorted(glob.glob("Fontes/**/*.pdf", recursive=True))
    cont = collections.Counter()
    linhas = []
    for cam in pdfs:
        rel = cam.replace("\\", "/")
        eixo = rel.split("/")[1] if "/" in rel else "?"
        tipo = "LITERATURA" if eixo in FORA_DA_DOCUMENTAL else "DOCUMENTAL"
        cls, extra, n = classifica(cam)
        if tipo == "DOCUMENTAL" and cls in ("SEM", "ABERTA"):
            # Ato oficial: a ausencia de declaracao nao e desconhecimento. A Lei
            # 9.610/98, art. 8o, IV, poe atos oficiais fora do direito autoral.
            cls = "ATO OFICIAL"
        cont[(tipo, cls)] += 1
        linhas.append((tipo, cls, extra, n, os.path.getsize(cam), rel))

    print("AUDITORIA DE LICENCA DO CORPUS — %d PDFs" % len(pdfs))
    print("=" * 78)
    for tipo in ("DOCUMENTAL", "LITERATURA"):
        tot = sum(v for (t, _), v in cont.items() if t == tipo)
        print("  %s — %d arquivo(s)" % (tipo, tot))
        for cls in ("ATO OFICIAL", "CC", "ABERTA", "RESERVADA", "SEM", "ILEGIVEL"):
            if cont[(tipo, cls)]:
                print("      %-12s %3d" % (cls, cont[(tipo, cls)]))
    print("=" * 78)
    for tipo, cls, extra, n, b, rel in sorted(linhas):
        if tipo != "LITERATURA":
            continue
        eixo = rel.split("/")[1] if "/" in rel else "?"
        print("  %-10s %-11s %4dp %7.1fMB  %-26s %s"
              % (cls, extra, n, b / 1e6, eixo[:26], os.path.basename(rel)[:50]))

    trava = [l for l in linhas
             if l[0] == "LITERATURA" and l[1] in ("RESERVADA", "SEM", "ILEGIVEL")]
    lit = [l for l in linhas if l[0] == "LITERATURA"]
    print()
    print("LITERATURA QUE NAO SE PODE REDISTRIBUIR: %d de %d (%.0f MB)"
          % (len(trava), len(lit), sum(l[4] for l in trava) / 1e6))
    print("'SEM' NAO SIGNIFICA LIVRE: significa desconhecido, e desconhecido conta")
    print("como reservado por omissao. Ja ATO OFICIAL e outra coisa: a ausencia de")
    print("declaracao num acordao ou num relatorio de CPMI nao e lacuna, porque a Lei")
    print("9.610/98, art. 8o, IV, poe atos oficiais fora do direito autoral.")
    print()
    print("MAIORES ARQUIVOS DO CORPUS, para a higiene de tamanho:")
    for tipo, cls, extra, n, b, rel in sorted(linhas, key=lambda x: -x[4])[:5]:
        print("   %7.1fMB  %4dp  %6.2f MB/pagina  %s"
              % (b / 1e6, n, b / 1e6 / max(n, 1), os.path.basename(rel)[:52]))
    return 0 if not cont.get(("DOCUMENTAL", "ILEGIVEL")) \
        and not cont.get(("LITERATURA", "ILEGIVEL")) else 1


if __name__ == "__main__":
    sys.exit(main())
