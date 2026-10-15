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

# Apóstrofo entre dois caracteres de palavra NÃO é aspa: é "Bolsonaro's". Ver o
# docstring de transcricoes(), que explica o buraco que isto fecha.
_INTRA_APOSTROFO = re.compile(r"(?<=\w)['’](?=\w)")

_cache = {}

# Transcrições que legitimamente NÃO estão no documento ancorado. Cada uma com
# o motivo, porque exceção sem motivo é buraco. A chave é o começo da citação
# normalizada; basta o suficiente para identificá-la.
EXCECOES = {
    ("PT-06A", "fachin anula condenacoes de lula"):
        "manchete do portal do STF (08/03/2021), citada como referência do fato; "
        "o que o registro ancora na denúncia da PGR é a correlação com a elegibilidade, "
        "e essa transcrição está na p. 8",
    # Tatagiba (2014) entrou no corpus em 04/10/2026 e é DIGITALIZAÇÃO SEM CAMADA
    # DE TEXTO: PyPDF2 devolve string vazia em todas as 28 páginas. As duas
    # transcrições abaixo foram lidas por renderização a 170 dpi — a mesma técnica
    # com que o projeto leu os gráficos vetoriais do balanço do STF em 16/08/2026 —
    # e estão nas páginas 2 e 6 do PDF (p. 36 e 40 da revista). Quem quiser
    # conferir, renderize: ausência de texto extraível não é ausência de conteúdo.
    ("PT-01", "foram nacionalizados a partir da forte repressao policial"):
        "Tatagiba (2014, p. 36) — PDF p. 2, peça sem camada de texto, lida por "
        "renderização a 170 dpi",
    ("PT-01", "nao houve a conformacao de um frame capaz de conferir unidade"):
        "Tatagiba (2014, p. 40) — PDF p. 6, peça sem camada de texto, lida por "
        "renderização a 170 dpi",
    # As duas exceções abaixo entraram em 09/10/2026 e são do MESMO tipo, que é o
    # caso 4 da lista impressa ao fim deste arquivo: transcrição que está em
    # `fonte_trecho` DE PROPÓSITO sem ser âncora do registro.
    ("PT-03C", "o plenario do stf negou, por maioria dos votos, o habeas corpus"):
        "nota do portal do STF (04/04/2018), que é a fonte_url do registro e não um "
        "PDF com página; entrou antes de o registro ter fonte_pagina. O que PT-03C "
        "ancora com página é a pressão militar sobre este julgamento, em Madeira et "
        "al. (2022), p. 256 e 267 do PDF",
    ("PT-19", "ostensibly inspired by the coups in sri lanka and thailand"):
        "DELIBERADAMENTE NÃO É ÂNCORA. A frase é de Bastos e Recuero (2023, p. 4) e "
        "está citada no registro para declarar que NÃO corrobora o Sri Lanka: os "
        "autores a atribuem a Keulenaar et al. (2023), relatório não publicado. A "
        "peça não está em fonte_local nem em fonte_pagina de PT-19, e é por isso que "
        "o conferidor não a acha — o que está certo. Citar uma citação é o que o "
        "projeto proibiu em 30/09, e a exceção existe para que a proibição fique "
        "legível em vez de virar falha silenciosa",
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

    ACRESCENTADO EM 04/10/2026, terceira rodada da tarefa 14: o hífen passou a
    engolir o espaço que vem depois dele, para **unir a hifenização de quebra de
    linha**. A versão anterior apagava o hífen e deixava o espaço, de modo que o
    PDF "mobiliza-\\ntion" normalizava para "mobiliza tion" enquanto o codebook
    trazia "mobilization": duas âncoras de von Bülow e Abers (2024) apareciam
    como não localizadas tendo a frase exatamente na página citada — o mesmo
    sintoma de PT-08A e PT-36, por outra causa. A simetria é o que torna isto
    seguro: a mesma normalização se aplica à citação e ao texto da página, e por
    isso juntar demais não cria casamento falso, só perde legibilidade da forma
    normalizada. As 66 âncoras anteriores continuam idênticas.
    """
    s = re.sub(r"[‐-―\-]\s*", "", norm(s))
    return re.sub(r"[\"“”‘’']+", "", s)


# Fontes cujo CMap vem defeituoso e precisam de conserto por span. Ver
# _mupdf() logo abaixo.
FONTES_DESLOCADAS = {"Gentium-Book-Basic"}

# LINHA DE BASE DO CASAMENTO PARCIAL, fixada em 10/10/2026 com 17.
# Enquanto eram 45 o numero nao servia de linha de base; com 17 serve, e isso
# converte o ponto cego em tripwire: uma transcricao editada na cauda tira um
# fragmento de "ok" e o poe em "parcial", o total vai a 18 e o ciclo cai.
# NAO se endurece o casamento nem se mexe nos 17 legitimos -- vigia-se a
# CONTAGEM, que e o mesmo padrao do inventario do corpus.
# Se um trecho novo e legitimamente parcial, suba o numero aqui E diga por que.
#
# Em escopo de MODULO desde 15/10/2026: `gerar_ordem_de_ataque.py` importa este
# numero para a linha da tarefa 26, em vez de redigita-lo. Quem garante que ele
# corresponde ao disco e o passo 7 do ciclo, que cai se a contagem mudar.
PARCIAIS_BASE = 17


def confere_integral(frag, caminho, pg):
    """O trecho confere POR INTEIRO, e não só por janela?

    Responde ignorando o que não é conteúdo da fonte, e cada exclusão tem razão:

      - **pontuação terminal**: a transcrição costuma fechar com ponto que a
        extração não traz naquele ponto; 6 dos 42 casos eram só isso;
      - **interpolação do analista entre COLCHETES**: `[três poderes]`,
        `[prisões]` são inserções declaradas pelo próprio uso do colchete e,
        por definição, NÃO estão na fonte — 3 casos;
      - **páginas vizinhas**: um trecho longo atravessa a quebra de página, e o
        conferidor localiza numa página só; 33 casos tinham prefixo casando 3 de
        406, 7 de 349, que é a assinatura disso.

    Devolve "ok", "pagina" (confere ao juntar a vizinha) ou "parcial".
    """
    alvo = _sem_apoio(frag)
    if not alvo:
        return "ok"
    if alvo in _sem_apoio(texto_pagina(caminho, pg) or ""):
        return "ok"
    for par in ((pg - 1, pg), (pg, pg + 1)):
        junto = "".join(_sem_apoio(texto_pagina(caminho, p) or "") for p in par)
        if alvo in junto:
            return "pagina"
    return "parcial"


COLCHETE = re.compile(r"\[[^\]]{0,120}\]")
_TERMINAL = " .,;:!?\u2026"


def _sem_apoio(s):
    """norm_busca sem espaço, sem interpolação em colchete e sem pontuação final."""
    return re.sub(r"\s+", "", norm_busca(COLCHETE.sub(" ", s or ""))).strip(_TERMINAL)


def sem_espaco(s):
    """norm_busca sem espaco algum — só para a pergunta do casamento INTEGRAL.

    Criada em 10/10/2026, depois de classificar a causa dos 45 fragmentos que
    casavam só por janela: **28 eram artefato de espaço na junção** — 18 casavam
    o trecho inteiro menos até 2 caracteres, e 10 tinham as duas metades
    presentes na página e só a junção falhando, que é quebra de linha e
    hifenização. Comparar sem espaço nenhum absorve esses 28 e deixa à vista os
    que divergem de verdade.

    **Não substitui `norm_busca` e não entra em `casa()`**: mexer ali mudaria o
    casamento de todas as âncoras do codebook. Esta função responde uma pergunta
    de diagnóstico, não de validação.
    """
    return re.sub(r"\s+", "", norm_busca(s))


def _desloca(t):
    """Desfaz o deslocamento de glifos de um subconjunto de fonte quebrado.

    O PDF da OpenEdition de Kunrath Silva (2018) traz camada de texto PRESENTE
    E ERRADA: o código de cada glifo é o ASCII menos 29 — espaço=0x03, 'A'=0x24,
    'a'=0x44, vírgula=0x0F, '0'=0x13 — e os acentuados saem deslocados de 62 na
    faixa 0xA2. PyPDF2 e PyMuPDF devolvem os dois a mesma sopa de letras.

    Isto é pior que a digitalização sem texto de Tatagiba (2014): lá a string
    vinha vazia e a ausência era visível; aqui a string vem cheia, e uma busca
    por qualquer frase "prova" com alta confiança que o artigo não a contém.
    O 0x20 fica de fora porque, dentro do mesmo span, ele é espaço de verdade:
    deslocá-lo trocava cada espaço de texto justificado por um '='.
    """
    out = []
    for c in t:
        o = ord(c)
        if o == 0x20:
            out.append(c)
        elif 0x03 <= o <= 0x5D:
            out.append(chr(o + 29))
        elif 0xA2 <= o <= 0xBF:
            out.append(chr(o + 62))
        else:
            out.append(c)
    return "".join(out)


def _mupdf(caminho, n, consertar):
    """Leitura por PyMuPDF; com consertar=True, aplica _desloca span por span.

    Por span, não pela página: no mesmo arquivo da OpenEdition as fontes Roboto
    saem corretas, e consertar a página inteira estragaria o que estava bom.
    """
    try:
        import pymupdf
    except ImportError:
        return ""
    d = _cache.get(("mu", caminho))
    if d is None:
        d = _cache[("mu", caminho)] = pymupdf.open(str(RAIZ / caminho))
    pag = d[n - 1]
    if not consertar:
        return pag.get_text()
    linhas = []
    for b in pag.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            linhas.append("".join(
                _desloca(s["text"]) if s["font"] in FONTES_DESLOCADAS else s["text"]
                for s in l["spans"]))
    return "\n".join(linhas)


def texto_pagina(caminho, n):
    """Todas as leituras fiéis da página, concatenadas, para busca de substring.

    São três — PyPDF2, PyMuPDF e PyMuPDF com conserto de glifo — porque nenhuma
    serve sozinha. PyPDF2 injeta espaço DENTRO das palavras em alguns PDFs
    ("destaca -se", "empac amentos"), e foi por isso que nenhuma das 26 âncoras
    que entraram em 04/10/2026 casava; PyMuPDF não faz isso, mas nem ele lê a
    fonte deslocada da OpenEdition.

    É acréscimo, não troca: as leituras são concatenadas, de modo que o que
    casava antes continua casando, e as 63 âncoras anteriores seguem idênticas.
    O separador \\x00 impede casamento que atravesse a junção — nenhuma citação
    normalizada contém byte nulo.
    """
    r = _cache.get(caminho)
    if r is None:
        r = _cache[caminho] = PdfReader(str(RAIZ / caminho))
    if n < 1 or n - 1 >= len(r.pages):
        return None
    chave = (caminho, n)
    txt = _cache.get(chave)
    if txt is None:
        leituras = [r.pages[n - 1].extract_text() or "",
                    _mupdf(caminho, n, False),
                    _mupdf(caminho, n, True)]
        txt = _cache[chave] = "\x00".join(norm_busca(t) for t in leituras)
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

    CORRIGIDO EM 04/10/2026, terceira rodada da tarefa 14 — e era um buraco aberto
    desde o começo. **Apóstrofo dentro de palavra também era tomado por
    delimitador:** ASPAS_FECHA contém U+2019, que é o apóstrofo tipográfico de
    todo texto em inglês ("Bolsonaro's"). A paridade invertia e a citação inteira
    era descartada **em silêncio** — zero candidatos, nenhum aviso, e o ciclo
    passava verde porque não havia o que conferir. Auditado o codebook no dia da
    descoberta: as 57 transcrições entre aspas curvas então existentes NÃO eram
    afetadas, por serem em português e sem aspa interna, de modo que nada
    retroativo mudou. Mas a primeira peça em inglês a ancorar registro cairia no
    buraco — e caiu: von Bülow e Abers (2024), em PT-06.

    O conserto mascara o apóstrofo INTRAPALAVRA antes de fatiar e o devolve
    depois. Aspa que de fato abre ou fecha nunca está entre dois caracteres de
    palavra, e por isso a máscara não a atinge. Continua valendo a limitação
    irmã, que NÃO tem conserto aqui: **aspa dupla aninhada** — uma citação que
    contenha outra citação aspada — ainda inverte a paridade, e a saída correta é
    escolher outro trecho da mesma página. Ver PT-06 e o item 34.5 da agenda.
    """
    masc = _INTRA_APOSTROFO.sub("\x01", trecho or "")
    partes = [p.replace("\x01", "'")
              for p in re.split("[{}]".format(
                  re.escape(ASPAS_ABRE + ASPAS_FECHA)), masc)]
    if len(partes) < 2:
        return []  # nenhuma aspa: é referência, não transcrição
    # Índices ímpares são o que está DENTRO de aspas; os pares são o aparato
    # entre elas. Sem essa distinção, um registro sem transcrição alguma teria
    # o próprio texto de referência tomado como citação a procurar no PDF.
    dentro = [p.strip() for i, p in enumerate(partes) if i % 2 == 1]
    return [p for p in dentro if len(p) >= 45 and not APARATO.search(p[:60])]


PAR_CURVO = re.compile("“([^“”]{45,}?)”")


def aninhamento(trecho):
    """Quantas citações o pareamento acha que transcricoes() NÃO vê?

    ACRESCENTADO EM 08/10/2026, depois de a armadilha morder três vezes no mesmo
    dia. transcricoes() fatia em TODO caractere de aspa e fica com os índices
    ímpares; qualquer aspa ANINHADA inverte a paridade dali para frente. As duas
    consequências são simétricas e as duas são silenciosas:

      - uma transcrição real deixa de ser extraída, e **ninguém a confere** — o
        ciclo passa verde porque não havia o que conferir (foi o caso do kit
        Covid em PT-06, em 04/10);
      - e um pedaço de APARATO — prosa do analista entre duas citações — é
        promovido a transcrição e procurado no PDF, onde naturalmente não está
        (foi o caso de PT-08, em 08/10: a frase 'não foi o Capitólio, e sim a
        revolta do Sri Lanka' é minha, não da fonte).

    A detecção é barata: um pareamento simples de aspas curvas acha as citações
    bem formadas; se transcricoes() não devolve todas elas, há aninhamento. Devolve
    a lista das perdidas, e main() trata como FALHA — porque transcrição não
    conferida é pior que transcrição errada: a errada aparece.
    """
    vistas = [norm_busca(t) for t in transcricoes(trecho)]
    perdidas = []
    for m in PAR_CURVO.finditer(trecho or ""):
        cit = m.group(1).strip()
        alvo = norm_busca(cit)
        if not any(alvo in v or v in alvo for v in vistas):
            perdidas.append(cit)
    return perdidas


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
    ok = falha = indet = parciais_total = atravessa_total = 0
    falhas, ociosas_total, excecoes_usadas = [], 0, 0

    aninhadas = {}
    for e in alvos_reg:
        perdidas = aninhamento(e.get("fonte_trecho"))
        if perdidas:
            aninhadas[e["id"]] = perdidas

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

        achados, perdidas, usadas, fracas, parciais = [], [], set(), 0, 0
        atravessa = 0
        for cit in cits:
            for frag in fragmentos(cit):
                onde = localizar(frag, pp, docs)
                if onde:
                    achados.append((frag, onde))
                    usadas.add((onde[0], onde[1]))
                    if onde[2] <= 40:
                        fracas += 1
                    # CASOU POR JANELA, MAS NAO POR TEXTO INTEGRAL — e isso precisa
                    # aparecer. `casa()` devolve sucesso assim que UMA janela de 90
                    # (ou 60, ou 40) caracteres confere, de proposito, porque
                    # hifenizacao e ligadura quebram o casamento literal. O preco,
                    # descoberto por prova negativa em 09/10/2026: **editar a cauda
                    # de uma transcricao longa PASSA sem ser notado** — duas
                    # injecoes de uma palavra trocada no fim (menor->maior,
                    # tres->dois) nao foram pegas, enquanto as duas injecoes de
                    # pagina errada foram. A garantia real e "existe uma janela
                    # desta transcricao nesta pagina", nao "a transcricao e fiel".
                    # Medido no mesmo dia: 176 fragmentos casam integral e 45 so
                    # por janela, de modo que EXIGIR integral quebraria 45 ancoras
                    # legitimas. Entao nao se endurece: torna-se visivel.
                    _est = confere_integral(frag, docs[onde[0]], onde[1])
                    if _est == "pagina":
                        atravessa += 1
                    elif _est == "parcial":
                        parciais += 1
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
            print("  {:<7} {} {}/{} localizadas · {}{}{}".format(
                e["id"], marca, len(achados), total, onde_txt,
                "  ({} por janela curta)".format(fracas) if fracas else "",
                "  ({} só por janela, texto integral não confere)".format(parciais)
                if parciais else ""))
            ok += 1
        parciais_total += parciais
        atravessa_total += atravessa

        if verboso:
            for frag, (c, p, j) in achados:
                print("          · {} p.{} (janela {}) «{}…»".format(
                    c, p, j, norm(frag)[:52]))
        if ociosas:
            print("          · página(s) que nenhuma transcrição alcança: {}".format(
                ", ".join("{} p.{}".format(c, p) for c, p in ociosas)))

    print("=" * 78)
    print("confirmados {} | falhas {} | indeterminados {}".format(ok, falha, indet))
    if atravessa_total:
        print("{} fragmento(s) conferem POR INTEIRO ao juntar a página vizinha: a "
              "transcrição atravessa a quebra de página.".format(atravessa_total))
    if parciais_total:
        print("{} fragmento(s) localizado(s) SO POR JANELA: a janela confere e o "
              "texto integral nao.".format(parciais_total))
        print("Eram 45 em 09/10/2026 e são {} desde 10/10. A queda não veio de"
              .format(parciais_total))
        print("afrouxar o critério: veio de classificar a causa de cada um e absorver")
        print("as três que NÃO são divergência de conteúdo: pontuação terminal,")
        print("interpolação do analista entre colchetes (que por definição não está")
        print("na fonte) e transcrição que atravessa a quebra de página. A conta por")
        print("classe está em docs/PENDENCIAS-ANALITICAS.md, item 45; aqui só se")
        print("imprime o que o próprio conferidor mede.")
        print("O que sobra é o PONTO CEGO real: editar a cauda de uma transcrição")
        print("longa passa sem ser notado. Prova negativa de 09/10: 2 de 4 injeções")
        print("escaparam, e as duas eram troca de palavra no fim do trecho.")
        print("Para ver quais, rode com -v e compare casa/total.".format())
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
    if aninhadas:
        print()
        print("ASPA ANINHADA — transcrição que NINGUÉM confere: {}".format(
            ", ".join(sorted(aninhadas))))
        print("Uma aspa dentro de outra inverte a paridade de transcricoes(), e a")
        print("consequência é silenciosa nas duas direções: a citação real deixa de ser")
        print("extraída, ou um pedaço de aparato é promovido a citação e procurado no PDF.")
        print("A saída é no TEXTO, não no script: reescrever o trecho sem aspa interna.")
        for rid, perdidas in sorted(aninhadas.items()):
            for cit in perdidas:
                print("  {:<7} não extraída: “{}...”".format(rid, cit[:72]))
    # SO em --todos: num subconjunto a contagem mede outra coisa, e guarda que
    # dispara no recorte errado e ruido -- e ruido treina a ignorar guarda.
    if todos and parciais_total != PARCIAIS_BASE:
        print("")
        print("X CONTAGEM DE CASAMENTO PARCIAL MUDOU: {} agora, {} na linha de base "
              "de 10/10/2026.".format(parciais_total, PARCIAIS_BASE))
        if parciais_total > PARCIAIS_BASE:
            print("  Subiu. Uma transcrição que casava por inteiro deixou de casar —")
            print("  é exatamente a edição de cauda que a prova negativa de 09/10 viu")
            print("  escapar. Rode com -v, compare casa/total e ache a que mudou.")
        else:
            print("  Caiu, o que é bom, e ainda assim precisa de decisão: ajuste")
            print("  PARCIAIS_BASE neste arquivo e diga no commit por que caiu.")
        return 1
    return 1 if (falhas or aninhadas) else 0


if __name__ == "__main__":
    sys.exit(main())
