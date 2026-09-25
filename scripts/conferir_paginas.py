#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Conferência: TODA transcrição literal está mesmo em ALGUMA página citada?

Esta é a única checagem que abre o PDF e compara o texto. As demais verificam
estrutura — que o caminho existe, que a página pertence ao documento vinculado —
e por isso **não pegam um vínculo errado**: elas derivam o código do documento a
partir do próprio vínculo, e validam como coerente um vínculo que aponta para a
peça errada.

Foi assim que se descobriu, em 16/08/2026, que PT-28 citava "CPMI, p. 657" no
texto e apontava para o acórdão da AP 2668 no vínculo. Rode isto a cada rodada.

ENDURECIDO EM 25/09/2026. A versão anterior aprovava o registro assim que UMA
transcrição casasse com UMA página listada, e parava ali. Quatro consequências:

  - só o PRIMEIRO documento de `fonte_pagina` era aberto, de modo que as demais
    peças de um registro com corroboração dupla nunca eram conferidas — as
    âncoras novas de PT-28 (Cappelli e AP 2668) seriam invisíveis;
  - intervalos como "CPMI: 880-884" viravam duas páginas, 880 e 884, e o miolo
    nunca era aberto — era ali que estavam duas transcrições de PT-12A;
  - a elisão "(...)" no meio de uma transcrição impedia qualquer casamento,
    porque a janela literal atravessava o buraco (PT-34);
  - e bastava uma transcrição de várias.

Agora: cada transcrição precisa ser localizada em alguma página listada de
algum documento listado; intervalos são expandidos; a elisão parte a citação em
fragmentos, cada um conferido por si. Duas transcrições que apareciam como não
localizadas — PT-08A e PT-36 — eram artefato de casamento, não erro: o PDF
escreve «o painel "as mulatas", de di cavalcanti» e o codebook transcreve sem as
aspas internas. A normalização de busca passou a apagá-las.

Na estreia sob a regra nova, dois erros de página reais: PT-02A citava a p. 3
do acórdão das ADC, que é a autuação, com o trecho na p. 6; e PT-03A ancorava
só a p. 395, com a segunda transcrição na p. 348.

O QUE ELE NÃO PEGA, e o caso é instrutivo. **PT-59 continua passando com o
vínculo errado de antes de 11/09/2026.** A leitura que este projeto vinha
repetindo — "casou pela citação errada, um trecho de fórmula repetida" — está
imprecisa, e a verificação feita ao endurecer a ferramenta a corrigiu: a
decisão da EP 169 tem o dispositivo COMEÇANDO na p. 33 e SEGUINDO até a p. 36,
e a janela que casava na p. 36, com o endereço do 19º BPM, é parte legítima da
mesma transcrição — só que 300 caracteres adiante. O vínculo antigo não era
falso, era INCOMPLETO: confirmava a página final sem nunca abrir a inicial.

Exigir que toda transcrição seja localizada não resolve esse caso, porque as
duas transcrições de PT-59 realmente têm pedaço na p. 36. O que aponta para ele
é a outra saída desta ferramenta: a lista de **páginas listadas que nenhuma
transcrição alcança**. Com o vínculo antigo, a p. 1 aparecia ali. É sinal, não
falha — a página pode sustentar um fato que o registro não transcreve entre
aspas —, e é onde olhar primeiro quando uma âncora estiver sob suspeita.

O QUE TAMBÉM NÃO FAZ. Não decide se a página **sustenta** a afirmação do
registro: confere que o texto transcrito está lá, o que é outra coisa. E não
sabe a qual documento cada transcrição pertence quando o registro ancora vários
— exige que ela esteja em algum deles, não no certo.

Uso:
    python scripts/conferir_paginas.py              # amostra de 12
    python scripts/conferir_paginas.py --todos      # todos os que têm página
    python scripts/conferir_paginas.py PT-28 PT-31  # registros específicos
    python scripts/conferir_paginas.py --todos -v   # mostra cada transcrição
"""

import json
import random
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

try:
    from PyPDF2 import PdfReader
except ImportError:
    raise SystemExit("PyPDF2 ausente:  pip install PyPDF2")

ASPAS_ABRE = "\"“‘'"
ASPAS_FECHA = "\"”’'"
_cache = {}

# Transcrições que legitimamente NÃO estão no documento ancorado. Cada uma com
# o motivo, porque exceção sem motivo é buraco. A chave é o começo da citação
# normalizada; basta o suficiente para identificá-la.
EXCECOES = {
    ("PT-06A", "fachin anula condenacoes de lula"):
        "manchete do portal do STF (08/03/2021), citada como referência do fato; "
        "o que o registro ancora na denúncia da PGR é a correlação com a elegibilidade, "
        "e essa transcrição está na p. 8",
}


def norm(s):
    """Normalização para exibição: sem acento, minúscula, espaço colapsado."""
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", s).lower()


def norm_busca(s):
    """Normalização para CASAMENTO: também apaga aspas e travessões.

    O PDF escreve «havia falado em “policiamento direcionado” durante o segundo
    turno» e o codebook transcreve sem as aspas internas. Comparar literalmente
    falhava por causa de dois caracteres, e era assim que PT-08A e PT-36
    apareciam como não localizados tendo a frase exatamente na página citada.
    """
    return re.sub(r"[\"“”‘’'‐-―\-]+", "", norm(s))


def texto_pagina(caminho, n):
    r = _cache.get(caminho)
    if r is None:
        r = _cache[caminho] = PdfReader(str(RAIZ / caminho))
    if n < 1 or n - 1 >= len(r.pages):
        return None
    chave = (caminho, n)
    txt = _cache.get(chave)
    if txt is None:
        txt = _cache[chave] = norm_busca(r.pages[n - 1].extract_text() or "")
    return txt


INTERVALO = re.compile(r"\b(\d{1,4})\s*[-–—]\s*(\d{1,4})\b")


def pares(fonte_pagina):
    """'CPMI: 646, 711 | Cappelli: 55, 57' -> [('CPMI',[646,711]),('Cappelli',[55,57])]

    Intervalos são EXPANDIDOS: 'CPMI: 880-884' vira 880, 881, 882, 883, 884. A
    versão anterior guardava só as pontas, e duas transcrições de PT-12A, que
    estão nas p. 881 e 882, ficavam inalcançáveis. O teto de 30 páginas evita
    que um intervalo largo demais mande abrir meio PDF.
    """
    saida = []
    for seg in (fonte_pagina or "").split("|"):
        if ":" not in seg:
            continue
        cod, resto = seg.split(":", 1)
        nums = set()
        for a, b in INTERVALO.findall(resto):
            a, b = int(a), int(b)
            if 0 < b - a <= 30:
                nums.update(range(a, b + 1))
        for x in re.findall(r"\b(\d{1,4})\b", INTERVALO.sub(" ", resto)):
            nums.add(int(x))
        if nums:
            saida.append((cod.strip(), sorted(nums)))
    return saida


APARATO = re.compile(r"^\s*[,;.)\]]|p\.\s*\d+\s*[;)]|oitiva de|apêndice", re.I)
ELISAO = re.compile(r"\(\s*(?:\.\.\.|…)\s*\)|\[\s*(?:\.\.\.|…)\s*\]")


def transcricoes(trecho):
    """Candidatos a transcrição literal dentro do texto de fonte_trecho.

    Não usar regex de par aberto-fecha: a aspa de fechamento de uma citação é
    consumida como delimitador e a citação SEGUINTE se perde. Foi o que produziu
    o falso positivo de PT-16, cujo fonte_trecho usa aspas simples para *títulos
    de seção* ('A radicalização do movimento') e não só para transcrições — o
    casamento pegou o intervalo entre dois títulos, que é aparato de referência.

    A abordagem aqui é grosseira de propósito: fatia em todo caractere de aspa,
    fica com os pedaços longos e descarta os que parecem aparato. Gerar
    candidato demais é barato; perder o candidato certo custa um falso alarme.
    """
    partes = re.split("[{}]".format(re.escape(ASPAS_ABRE + ASPAS_FECHA)), trecho or "")
    if len(partes) < 2:
        return []  # nenhuma aspa: é referência, não transcrição
    # Índices ímpares são o que está DENTRO de aspas; os pares são o aparato
    # entre elas. Sem essa distinção, um registro sem transcrição alguma teria
    # o próprio texto de referência tomado como citação a procurar no PDF.
    dentro = [p.strip() for i, p in enumerate(partes) if i % 2 == 1]
    return [p for p in dentro if len(p) >= 45 and not APARATO.search(p[:60])]


def fragmentos(citacao):
    """Parte a citação nas elisões: '(...)' não existe no PDF, e a janela
    literal que a atravessa nunca casa. Cada pedaço longo vale por si."""
    pedacos = [f.strip() for f in ELISAO.split(citacao) if len(f.strip()) >= 45]
    return pedacos or [citacao]


def casa(alvo, texto):
    """Procura janelas ao longo da citação, não só o início.

    Ancorar no começo produz falso negativo: hifenização e quebra de linha no
    PDF costumam atingir justamente as primeiras palavras. PT-31 foi um desses.
    """
    a = norm_busca(alvo)
    for tam in (90, 60, 40):
        if len(a) < tam:
            continue
        for ini in range(0, max(1, len(a) - tam), max(1, tam // 2)):
            if a[ini:ini + tam] in texto:
                return tam, ini
    if len(a) < 40 and a and a in texto:
        return len(a), 0
    return None


def localizar(fragmento, alvos, docs):
    """Onde, entre as páginas listadas, este fragmento aparece? (cod, pg, janela)"""
    for cod, nums in alvos:
        caminho = docs.get(cod)
        if not caminho or not caminho.lower().endswith(".pdf"):
            continue
        for pg in nums:
            txt = texto_pagina(caminho, pg)
            if txt is None:
                continue
            r = casa(fragmento, txt)
            if r:
                return cod, pg, r[0]
    return None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    todos = "--todos" in sys.argv
    verboso = "-v" in sys.argv or "--verboso" in sys.argv

    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    docs = dados["metadados"]["registro_documentos"]
    eventos = {e["id"]: e for e in dados["eventos"]}

    cands = [e for e in dados["eventos"] if pares(e.get("fonte_pagina"))]
    if args:
        alvos_reg = [eventos[a] for a in args if a in eventos]
    elif todos:
        alvos_reg = cands
    else:
        random.seed(81)
        alvos_reg = sorted(random.sample(cands, min(12, len(cands))), key=lambda e: e["id"])

    print("CONFERÊNCIA PÁGINA x TRANSCRIÇÃO — {} registro(s), modo estrito".format(
        len(alvos_reg)))
    print("=" * 78)
    ok = falha = indet = 0
    falhas, ociosas_total, excecoes_usadas = [], 0, 0

    for e in alvos_reg:
        pp = pares(e.get("fonte_pagina"))
        if not pp:
            print("  {:<7} ~  sem página estruturada".format(e["id"]))
            indet += 1
            continue
        if not any((docs.get(c) or "").lower().endswith(".pdf") for c, _ in pp):
            print("  {:<7} ~  {} fora do alcance (não é PDF)".format(
                e["id"], ", ".join(c for c, _ in pp)))
            indet += 1
            continue
        cits = transcricoes(e.get("fonte_trecho"))
        if not cits:
            print("  {:<7} ~  {} — referência sem transcrição literal".format(
                e["id"], e["fonte_pagina"]))
            indet += 1
            continue

        achados, perdidas, usadas, fracas = [], [], set(), 0
        for cit in cits:
            for frag in fragmentos(cit):
                onde = localizar(frag, pp, docs)
                if onde:
                    achados.append((frag, onde))
                    usadas.add((onde[0], onde[1]))
                    if onde[2] <= 40:
                        fracas += 1
                    continue
                chave = next((k for k in EXCECOES
                              if k[0] == e["id"] and norm(frag).startswith(k[1])), None)
                if chave:
                    excecoes_usadas += 1
                    continue
                perdidas.append(frag)

        todas = {(c, p) for c, nums in pp for p in nums
                 if (docs.get(c) or "").lower().endswith(".pdf")}
        ociosas = sorted(todas - usadas)
        ociosas_total += len(ociosas)

        total = len(achados) + len(perdidas)
        onde_txt = ", ".join("{} p.{}".format(c, p) for c, p in sorted(usadas)[:4])
        if len(usadas) > 4:
            onde_txt += ", +{}".format(len(usadas) - 4)

        if perdidas:
            print("  {:<7} X  {}/{} localizadas · {}".format(
                e["id"], len(achados), total, onde_txt or "nenhuma"))
            for frag in perdidas:
                print("          não localizada: «{}…»".format(norm(frag)[:64]))
            falhas.append(e["id"])
            falha += 1
        else:
            marca = "OK" if not fracas else "OK"
            print("  {:<7} {} {}/{} localizadas · {}{}".format(
                e["id"], marca, len(achados), total, onde_txt,
                "  ({} por janela curta)".format(fracas) if fracas else ""))
            ok += 1

        if verboso:
            for frag, (c, p, j) in achados:
                print("          · {} p.{} (janela {}) «{}…»".format(
                    c, p, j, norm(frag)[:52]))
        if ociosas:
            print("          · página(s) que nenhuma transcrição alcança: {}".format(
                ", ".join("{} p.{}".format(c, p) for c, p in ociosas)))

    print("=" * 78)
    print("confirmados {} | falhas {} | indeterminados {}".format(ok, falha, indet))
    if ociosas_total:
        print("{} página(s) listada(s) que nenhuma transcrição alcança. Não é falha: a "
              "página pode\nsustentar um fato que o registro não transcreve entre aspas. "
              "É onde olhar primeiro\nquando uma âncora estiver sob suspeita.".format(
                  ociosas_total))
    if excecoes_usadas:
        print("{} transcrição(ões) dispensada(s) por exceção registrada em EXCECOES."
              .format(excecoes_usadas))
    if falhas:
        print("\nFALHAS — investigar antes de citar: {}".format(", ".join(falhas)))
        print("Uma falha significa uma de quatro coisas, nesta ordem de probabilidade:")
        print("  1. a página está errada (foi o caso de PT-02A: p. 3, e o trecho na p. 6)")
        print("  2. o vínculo aponta para o documento errado (foi o caso de PT-28)")
        print("  3. a transcrição foi editada e não confere mais com o original")
        print("  4. a transcrição é de outra fonte que o registro cita de passagem —")
        print("     manchete, paráfrase —, e não do documento ancorado. Se for o caso,")
        print("     registre em EXCECOES, no alto deste arquivo, com o motivo.")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
