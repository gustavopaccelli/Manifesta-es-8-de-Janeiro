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

import gzip
import hashlib
import html
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
    # AS TRES EXCECOES DE PT-08 SAIRAM EM 25/10/2026, e e o melhor desfecho
    # possivel para uma excecao: **a correcao que ela pedia chegou.** Elas
    # entraram em 22/10 porque as transcricoes da materia do Estadao estao num
    # `.md` citado por localizador estrutural, e `localizar()` so abria PDF --
    # de modo que ele as procurava nas folhas de Castaneda, Chen e CPMI, onde
    # nao estao. O comentario delas dizia, com estas palavras: "A correcao
    # certa nao e esta excecao: e ensinar `localizar()` a ler ancora nao-PDF".
    #
    # Foi o que o item 87 fez. As tres conferem no proprio `.md`, e PT-08
    # passou de 8/8 com tres dispensas a **11/11 sem nenhuma**. Fica o registro
    # porque excecao que sai por conserto e dado sobre o conserto: ela media,
    # durante tres dias, exatamente o buraco que o leitor novo fechou.
    #
    # AS DUAS DE PT-38 entraram em 25/10/2026 (item 89) e sao o caso 4:
    # transcricao que esta em `fonte_trecho` DE PROPOSITO sem ser ancora do
    # registro. As cifras do dano vem de SINOPSE DE DOCUMENTARIO (ago/2023) e
    # de LEVANTAMENTO DIVULGADO PELA IMPRENSA (jan/2025).
    #
    # A RAZAO DELAS MUDOU EM 27/10/2026 (item 95), e as excecoes FICARAM.
    # Ate aqui elas invocavam uma afirmacao do proprio registro: a de que
    # NENHUM documento primario do corpus carregava a valoracao do dano. **Essa
    # afirmacao caiu**, e a frase nao esta grafada aqui de proposito, porque
    # quem cita o defeito reproduz o defeito. O que a derrubou: a varredura de
    # 16/08 buscou a CIFRA, e buscando NOME DE OBRA o Relatorio Final da CPMI
    # descreve o evento em quatro folhas e credita a valoracao do STF a oficio
    # do proprio tribunal -- as DUAS PARCELAS de ago/2023 estao na f. 676.
    #
    # ENTAO POR QUE AS EXCECOES FICAM? Porque a pergunta delas e outra: a
    # excecao dispensa uma ASPA de ser localizada, e as duas aspas continuam
    # nao estando em peca nenhuma do corpus. **O que a CPMI traz sao as
    # parcelas, nao a frase, e a soma e derivacao que ela nunca imprime.** O
    # registro deixou de ser o unico do codebook sem transcricao verificavel --
    # tem oito, conferidas por folha --, e e so isso que mudou aqui.
    ("PT-38", "somente no stf, o prejuizo financeiro chegou a r$ 11,4 milhoes"):
        "sinopse oficial do documentário Democracia Inabalada (ago/2023), "
        "fonte jornalística com atribuição ao STF. A CIFRA tem lastro primário "
        "desde 27/10/2026, nas duas parcelas da CPMI f. 676 (Ofício "
        "023/CDG/2023 – STF), mas a SOMA é derivada e a CPMI não a imprime: a "
        "aspa, que é o que esta exceção dispensa, continua fora do corpus",
    ("PT-38", "furtados, quebrados ou completamente destruidos"):
        "levantamento do STF divulgado pela imprensa (jan/2025), idem — e esta "
        "metade da série segue SEM lastro primário, porque é posterior ao "
        "relatório da CPMI. A série está no campo COM DATA porque a cifra de "
        "2023 foi superada, e é isso que o registro existe para mostrar",
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

# LINHA DE BASE DO CASAMENTO PARCIAL SEM CAUSA CLASSIFICADA: ZERO, desde
# 15/10/2026. Eram 45 em 09/10 e 17 em 10/10, quando se absorveram as tres
# classes que NAO sao divergencia de conteudo (pontuacao terminal, interpolacao
# entre colchetes, transcricao atravessando a quebra de pagina). A tarefa 26(b)
# classificou as duas que faltavam:
#
#   * ANCORA ATRIBUIDA A FOLHA ERRADA -- 4 casos, e CORRIGIDO em 15/10/2026 o
#     numero que esta linha trazia antes: eram 3 de DOCUMENTO errado e 1 de
#     PAGINA errada dentro do mesmo documento, nao 4 de documento errado.
#     Medido no item 53. `localizar()` devolvia a primeira folha com qualquer
#     janela de 40 caracteres, e as pecas do corpus se citam entre si.
#     Corrigido no localizador, nao na contagem.
#   * MARCADOR DE NOTA DE RODAPE -- 11 casos. A extracao cola o numero da nota
#     na prosa. Classe propria, "nota", contada e impressa em separado.
#
# Com o residuo inexplicado em ZERO, a guarda fica no seu ponto mais forte:
# QUALQUER fragmento que passe a casar so por janela faz o ciclo cair. E o
# contrario de afrouxar -- 45 ancoras legitimas continuam passando, cada uma
# por uma causa nomeada.
# Se um trecho novo for legitimamente parcial, suba o numero aqui E diga por que.
#
# Em escopo de MODULO desde 15/10/2026: `gerar_ordem_de_ataque.py` importa este
# numero para a linha da tarefa 26, em vez de redigita-lo. Quem garante que ele
# corresponde ao disco e o passo 7 do ciclo, que cai se a contagem mudar.
PARCIAIS_BASE = 0

# LINHA DE BASE DO EMPATE ENTRE DOCUMENTOS: ZERO, medida em 15/10/2026 ao
# responder o item 52.5. A pergunta era se a preferencia nova de `localizar()`
# escolhe por TEXTO ou por ORDEM de `fonte_pagina`: 234 fragmentos localizados,
# 217 com uma unica folha candidata, 17 com mais de uma, e nos 15 que tem
# candidata disputada a folha escolhida confere numa classe ESTRITAMENTE melhor
# que as rivais. Os 2 empates que existem sao entre paginas do MESMO documento
# citado -- PT-53 no Balanco do STF e PT-58 na Pet 14.129, formula repetida duas
# vezes na mesma peca --, e por isso nao contam: a ancora esta certa das duas
# maneiras. Empate entre DOCUMENTOS e outra coisa, e e a forma exata do defeito
# que passou dois meses invisivel. Com a base em zero, o primeiro que aparecer
# faz o ciclo cair.
EMPATES_BASE = 0

# LINHA DE BASE DOS REGISTROS COM `fonte_pagina` E SEM PAGINA EXTRAIVEL: CINCO,
# medida em 18/10/2026. Sao os que citam a fonte por LOCALIZADOR ESTRUTURAL e nao
# por folha -- `inteiro teor`, `peca integral`, secao -- e por isso ficam fora do
# alcance deste conferidor, que abre PDF numa pagina.
#
# ELES ERAM INVISIVEIS ATE AQUI, e e isso que a base conserta. `pares()` nao
# devolvia par nenhum para eles, de modo que nao entravam em `cands` e nao
# apareciam em lugar algum da saida: nem como conferidos, nem como
# indeterminados. Quatro registros sumiam em silencio da unica checagem que le a
# fonte. Com a base, o sexto que aparecer faz o ciclo cair -- porque registro que
# deixa de ser conferivel tem de ser uma decisao, nao um efeito colateral.
#
# 20/10/2026: passa de CINCO para SEIS, e a razao e entrada de registro, nao
# afrouxamento. PT-01A ancora nas duas transcricoes das noticias institucionais
# do TSE sobre a auditoria do PSDB de 2014 -- peca sem paginacao, citada por
# `§secao`, e e o segundo uso da convencao criada em 16/10. A checagem 5 resolve
# os cinco localizadores dele contra os cabecalhos dos arquivos vinculados.
# 25/10/2026: passa de SEIS para TRES, e e reducao de alcance cego, nao
# afrouxamento. PT-01A, PT-03E e PT-19A citam por localizador estrutural
# num `.md` ou `.html`, e o conferidor passou a ler ancora nao-PDF (item
# 87): as treze transcricoes deles, nunca examinadas, passaram a conferir
# no arquivo inteiro. Permanecem TRES, e por outra razao -- PT-06B, PT-38
# e PT-56 citam PDF por `inteiro teor`: o conferidor sabe abrir a peca e
# nao sabe ONDE olhar, e varrer PDF inteiro custa 205 s para 16 aspas.
SEM_PAGINA_EXTRAIVEL_BASE = 0

# LINHA DE BASE DA TRANSCRICAO QUE NAO ESTA NA PECA CITADA: CINCO, medida
# em 25/10/2026 (item 88) e e categoria NOVA, nao afrouxamento.
#
# Ate aqui PT-06B, PT-38 e PT-56 eram "fora do alcance": citam PDF por
# `inteiro teor`, e o conferidor sabia abrir a peca e nao sabia ONDE
# olhar. Com o cache de folha ele varreu as 2.874 folhas das cinco pecas
# -- 151 s na construcao, 0,27 s depois -- e provou coisa MAIS FORTE que
# falta de alcance: **as cinco transcricoes nao estao nas pecas citadas.**
#
# A CAUSA E UNICA e esta medida: as cinco sao manchete ou texto da pagina
# de `fonte_url` -- notas do portal do STF e materias da Agencia Brasil --
# e `fonte_pagina` cita um PDF por `inteiro teor`. PT-38 e a prova mais
# limpa: `11,4 milhoes`, `prejuizo financeiro` e `furtados` tem ZERO
# ocorrencias nas 210 folhas do livro, que TEM camada de texto (68 mil
# caracteres nas 30 primeiras folhas) -- e a `fonte_url` dele e uma
# materia de setembro de 2024.
#
# O CONSERTO EXISTE E JA FOI FEITO UMA VEZ: arquivar a pagina em
# `Fontes/09_Arquivamento-web/` como `.md` e cita-la por localizador
# estrutural, que foi a rota (b) do item 76 para PT-08 em 22/10 e que o
# leitor de ancora nao-PDF (item 87) confere. **E coleta na web, e coleta
# e decisao do pesquisador** -- fica listado no item 88.
#
# Com a base, a sexta que aparecer faz o ciclo cair. E a base REPROVA --
# nao avisa --, pela licao de 25/10: a de alcance so avisava, com codigo
# de saida zero, enquanto o comentario dela dizia o contrario.
# 25/10/2026: passa de CINCO para ZERO no mesmo dia em que nasceu, e a
# queda nao veio de afrouxar nada. As cinco tinham DUAS causas: tres eram
# manchete de pagina web COLETAVEL -- duas de PT-06B e uma de PT-56 --, e
# as paginas foram coletadas, arquivadas no eixo 09 e ancoradas por
# localizador estrutural (item 89); as duas de PT-38 vem de sinopse de
# documentario e de levantamento de imprensa, o proprio campo declara
# isso desde 16/08/2026, e entraram em EXCECOES com essa razao. **A base
# em zero e mais forte que a base em cinco:** a primeira transcricao que
# aparecer fora da peca citada, sem razao escrita, faz o ciclo cair.
INTEIRO_TEOR_SEM_ACHADO_BASE = 0

# LINHA DE BASE DA EXCECAO OCIOSA: ZERO, medida em 27/10/2026 (item 92).
#
# Listada desde 87.5: nada avisava quando uma entrada de `EXCECOES`
# deixava de ser usada. As tres de PT-08 sairam em 25/10 **porque eu fui
# olhar**, e a quarta teria ficado.
#
# E EXCECAO OBSOLETA E PIOR QUE PENDENCIA ESQUECIDA, porque ela CONTINUA
# DISPENSANDO: a chave e (registro, prefixo normalizado), e se a
# transcricao que ela cobria for reescrita mantendo o comeco, a NOVA
# passa pela dispensa velha sem ninguem conferir. Dispensa e licenca, e
# licenca que ninguem revisita e o defeito que esta casa nomeou ao
# recusar lista de excecao no `.gitignore` em 22/10.
#
# Medido em 27/10/2026, antes de construir: as SETE registradas estao
# todas em uso. A base e genuinamente zero, e nao um numero herdado.
OCIOSAS_BASE = 0

# LINHA DE BASE DAS MEIAS-ANCORAS: ZERO, medida em 22/10/2026 (itens 80 e
# 81) e zerada no mesmo dia.
#
# A MEIA-ANCORA: a aspa que sustenta uma afirmacao do registro vive em
# `nota_auditoria` ou `status_verificacao` -- campos que autorizam a prosa e
# que NENHUMA guarda confere contra a folha, porque este conferidor localiza
# transcricao de `fonte_trecho`. Resultado: **o ponteiro no campo certo e a
# verificacao fora do laco.**
#
# Descoberta ao decidir `data_hora` de PT-02: acrescentei a folha a
# `fonte_pagina`, declarei a data ancorada, e o ciclo listou aquela folha
# entre as "paginas que nenhuma transcricao alcanca". **Por a folha no campo
# certo nao poe a verificacao no laco -- ancora e folha MAIS transcricao
# localizavel.**
#
# Medido no codebook inteiro: 78 aspas em campo de nota, 47 ja em
# `fonte_trecho` e 31 nao. Das 31, DEZ eram meias-ancoras reais -- sete com a
# folha ja em `fonte_pagina` e tres sem ponteiro algum, que exigiram folha
# nova (PT-05A f.31, PT-18A f.61, PT-57 f.888). Das outras 21: 4 valores de
# campo citados na nota, 3 nomes retirados que a checagem 7 vigia, 13 que a
# varredura integral (7.677 folhas) nao achou em folha alguma, e 1 que DEVE
# ficar na nota -- a citacao intermediaria mutilada que o item 77 desmentiu,
# que esta la para ser contrastada e nao para ancorar.
#
# ESTA GUARDA E A PARTE BARATA DA VARREDURA, e so ela: testa a aspa de nota
# contra as folhas que o registro JA ancora -- as mesmas que este passo abre,
# em cache. Pega sete dos dez casos de hoje. A parte CARA -- varrer o PDF
# inteiro -- levou 205 s para 16 aspas e nao cabe no ciclo; quem quiser roda
# a mao, e o item 81 diz como.
#
# NAO HA LISTA DE DISPENSA, de proposito: a licao de 22/10 e que lista de
# excecao e divida que ninguem revisita. Aspa de nota que passe a conferir
# numa folha ancorada faz o ciclo cair, e as saidas sao duas -- promove-la a
# `fonte_trecho`, ou subir este numero E dizer no commit por que.
MEIAS_ANCORAS_BASE = 0

# --------------------------------------- A CLASSIFICACAO DOS CAMPOS ---
# ACRESCENTADA EM 29/10/2026 (item 106), e ela e o conserto de um padrao que
# mordeu DUAS VEZES EM TRES DIAS:
#
#   - a guarda das meias-ancoras nasceu em 22/10 lendo dois campos de nota, e
#     nao lia `mecanismo_causal`, que e onde a prosa deste projeto mais cita
#     fonte. Em 28/10 eu escrevi seis aspas la e o conferidor nao as leu: **o
#     ponto cego mordeu quem o construiu** (item 100);
#   - a checagem 6 validava remissao `PT-XX` em tres campos e nao em
#     `status_verificacao`, que tinha 33 remissoes (item 104).
#
# A CAUSA NAO E DESCUIDO: nao existia aqui uma classificacao dos campos do
# esquema, de modo que **cada guarda enumerava a lista do dia** e ficava a um
# campo de distancia de cegar. Varrido o repositorio em 29/10: TRES guardas
# enumeravam campo -- as duas acima e o marcador de diade, que le um campo so.
#
# A DISTINCAO QUE O CENSO OBRIGA A FAZER: **gerador que nomeia campo esta
# certo** -- nomear e o trabalho dele, e `gerar_codebook` nomeia quinze. O que
# envelhece e **guarda que VARRE PROSA e nomeia campo**.
#
# `NAO_PROSA` traz a razao de cada exclusao, porque exclusao sem razao e a
# dividida que esta casa persegue. `CAMPO_BASE` nao e exclusao: e o campo
# CONFERIDO, e ele entra nas guardas como contencao, nao como alvo.
NAO_PROSA = {
    "id": "identificador",
    "data_hora": "data, nao prosa — e `identificador nao e cifra` vale aqui",
    "fase": "vocabulario de quatro camadas",
    "autonomia_movimento": "vocabulario controlado de cinco valores",
    "status_classe": "vocabulario controlado de quatro classes",
    "fonte_url": "URL",
    "fonte_local": "caminhos, separados por ponto e virgula",
    "fonte_pagina": "localizadores — folha de PDF ou §secao",
}
CAMPO_BASE = "fonte_trecho"

# O ESQUEMA DECLARADO. Ele existe para o `assert` abaixo poder falar, e e
# conferido contra as chaves do proprio registro -- nao contra `CABECALHOS` de
# `gerar_codebook`, que arrastaria `openpyxl` para dentro de um conferidor.
ESQUEMA = ("id", "data_hora", "fase", "ator_grupo", "repertorio_acao",
           "target_alvo", "framing_narrativa", "resposta_estatal",
           "mecanismo_causal", "autonomia_movimento", "fonte_trecho",
           "fonte_url", "fonte_local", "fonte_pagina", "status_verificacao",
           "status_classe", "nota_auditoria")

CAMPOS_DE_PROSA = tuple(c for c in ESQUEMA
                        if c not in NAO_PROSA and c != CAMPO_BASE)
assert set(NAO_PROSA) | {CAMPO_BASE} | set(CAMPOS_DE_PROSA) == set(ESQUEMA)


def confere_esquema(evento):
    """O registro tem exatamente os campos que a classificacao conhece?

    **E AQUI QUE O PADRAO SE FECHA.** Se o esquema crescer, este assert
    derruba o ciclo e exige que o campo novo seja classificado em prosa ou
    nao-prosa -- de modo que a guarda seguinte **nao pode nascer cega**. A
    comparacao e contra as chaves do registro, que e a fonte da verdade.
    """
    vistos = set(evento)
    assert vistos == set(ESQUEMA), (
        "o esquema mudou e a classificacao de campos nao sabe: "
        "sobrando %s, faltando %s — classifique em NAO_PROSA ou deixe cair em "
        "CAMPOS_DE_PROSA, e diga a razao"
        % (sorted(vistos - set(ESQUEMA)) or "nada",
           sorted(set(ESQUEMA) - vistos) or "nada"))


# O nome antigo fica como apelido, porque a saida do ciclo o imprime e tres
# guardas o consomem. **O constante deixou de ser lista:** ele e derivado.
CAMPOS_DE_NOTA = CAMPOS_DE_PROSA


def _prefixo_maximo(alvo, folha):
    """Maior prefixo de `alvo` presente em `folha`, por busca binária."""
    lo, hi = 0, len(alvo)
    while lo < hi:
        meio = (lo + hi + 1) // 2
        if alvo[:meio] in folha:
            lo = meio
        else:
            hi = meio - 1
    return lo


def casa_ignorando_nota(alvo, folha, max_saltos=6, max_digitos=4):
    """`alvo` está em `folha` se ignorarmos marcadores de nota de rodapé?

    A extração de PDF cola o número da nota na prosa: a folha traz
    "…prontidão798. De acordo" onde a transcrição traz "…prontidão. De acordo".

    Esta função pula SÓ dígitos que existem na folha e NÃO na transcrição —
    nunca o contrário —, até 4 por salto e 6 saltos. Cifra trocada continua
    reprovando, porque aí o dígito divergente está na transcrição, e o
    alinhamento para no primeiro caractere que não é dígito da folha.
    """
    if len(alvo) < 20:
        return False
    ancora, desde = alvo[:20], 0
    for _ in range(5):
        i = folha.find(ancora, desde)
        if i < 0:
            return False
        desde = i + 1
        resto, j, saltos = folha[i:], 0, 0
        while j < len(alvo):
            if j < len(resto) and resto[j] == alvo[j]:
                j += 1
                continue
            k = 0
            while k < max_digitos and j + k < len(resto) and resto[j + k].isdigit():
                k += 1
            if k == 0 or saltos >= max_saltos:
                break
            resto = resto[:j] + resto[j + k:]
            saltos += 1
        if j >= len(alvo):
            return True
    return False


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
    # QUARTA CLASSE DE NAO-DIVERGENCIA, 15/10/2026: o marcador de nota de rodape
    # que a extracao cola na prosa. Onze dos treze residuos eram isto. Ver
    # casa_ignorando_nota -- pula digito que esta na FOLHA e nao na transcricao,
    # nunca o contrario, de modo que cifra trocada continua reprovando.
    if casa_ignorando_nota(alvo, _sem_apoio(texto_pagina(caminho, pg) or "")):
        return "nota"
    # A TRANSCRIÇÃO ATRAVESSA A QUEBRA E O APARATO DA PÁGINA FICA NO MEIO: bloco
    # de notas no pé da folha, número ou cabeçalho no alto da seguinte. O teste de
    # par de páginas acima falha justamente por isso — ele concatena as duas
    # folhas inteiras, e o aparato entra entre as duas metades da citação. Aqui
    # exige-se que o resto COMECE a página seguinte (primeiros 120 caracteres),
    # o que não mascara edição de cauda: o resto tem de aparecer literalmente.
    ta = _sem_apoio(texto_pagina(caminho, pg) or "")
    tb = _sem_apoio(texto_pagina(caminho, pg + 1) or "")
    if ta and tb:
        k = _prefixo_maximo(alvo, ta)
        if k >= 40 and len(alvo) - k >= 20 and 0 <= tb.find(alvo[k:]) <= 120:
            return "pagina"
    for par in ((pg - 1, pg), (pg, pg + 1)):
        junto = "".join(_sem_apoio(texto_pagina(caminho, p) or "") for p in par)
        if casa_ignorando_nota(alvo, junto):
            return "nota"
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

# LOCALIZADOR ESTRUTURAL, acrescentado em 18/10/2026 (item 64). Segmento que
# localiza por ESTRUTURA INTERNA nao cede numeral nenhum a `pares()`.
#
# O caso que motivou: `fonte_pagina` de PT-03E e
#   TSE RCand: ementa itens 2-4 e 12; dispositivo
# e `pares()` devolvia [('TSE RCand', [2, 3, 4, 12])] -- ITENS DE EMENTA LIDOS
# COMO PAGINAS. Nao produzia erro porque o teste seguinte, em main(), descarta o
# que nao aponta para PDF; mas **o que salvava era a extensao do arquivo, nao o
# localizador**, e a rota daquela peca em PROCEDENCIA declara que o endpoint do
# TSE serve o MESMO conteudo. No dia em que o acordao entrasse tambem em PDF, o
# registro passaria a ser conferido contra as FOLHAS 2, 3, 4 e 12 de uma peca
# cujas transcricoes estao noutro lugar -- e um casamento acidental ali seria a
# cifra certa no referente errado, com aprovacao do ciclo.
#
# Falha FECHADA: o registro deixa de ser candidato em vez de ser conferido
# errado, e passa a ser contado pela SEM_PAGINA_EXTRAIVEL_BASE. Medido em
# 18/10/2026: destes termos, so PT-03E casa em todo o codebook.
ESTRUTURAL = re.compile(r"\bitem\b|\bitens\b|ementa|disposit", re.I)


def meias_ancoras(e, pp, docs):
    """Aspa que vive so em campo de NOTA e confere numa folha JA ancorada.

    Devolve [(campo, cod, folha, aspa)].

    O DETECTOR E DELIBERADAMENTE MAIS FROUXO QUE O PROMOTOR: usa `casa()`, de
    janela, e nao `confere_integral()`. A razao e um caso real -- a aspa de
    PT-57 na folha 19 era COMPOSTA por juncao de dois recortes que a folha traz
    separados, e confere `parcial`. Com `confere_integral` ela escaparia da
    guarda; com `casa` ela e acusada, que e o que se quer. **Guarda detecta;
    quem promove confere por inteiro.**

    A contencao usa `fonte_trecho` inteiro e tambem as transcricoes extraidas
    dele, porque a nota pode citar um PEDACO do que o campo de transcricao traz
    completo -- e nesse caso nao ha meia-ancora: o passo ja confere o todo.
    """
    base = norm_busca(e.get("fonte_trecho") or "")
    ja = [norm_busca(x) for x in transcricoes(e.get("fonte_trecho"))]
    achados = []
    # DEDUPLICA POR ASPA, desde a prova negativa de 22/10/2026: a mesma frase
    # citada duas vezes no campo de nota rende duas ocorrencias em
    # `transcricoes()`, e a guarda acusava 2 onde ha 1. Relato inflado e o que
    # ensina a ignorar a guarda.
    vistas = set()
    for campo in CAMPOS_DE_NOTA:
        for aspa in transcricoes(e.get(campo)):
            n = norm_busca(aspa)
            if not n or n in base or any(n in x or x in n for x in ja):
                continue
            if n in vistas:
                continue
            vistas.add(n)
            for cod, nums in pp:
                caminho = docs.get(cod)
                if not caminho or not caminho.lower().endswith(".pdf"):
                    continue
                achou = None
                for pg in nums:
                    txt = texto_pagina(caminho, pg)
                    if txt is not None and casa(aspa, txt):
                        achou = pg
                        break
                if achou:
                    achados.append((campo, cod, achou, aspa))
                    break
    return achados


# ------------------------------------------------------- ANCORA NAO-PDF ---
# ACRESCENTADO EM 25/10/2026 (item 87). Tres registros citam a fonte por
# LOCALIZADOR ESTRUTURAL num arquivo `.md` ou `.html` -- PT-01A (noticias do
# TSE), PT-03E (acordao do TSE em HTML) e PT-19A (post do NetLab) -- e NUNCA
# FORAM CONFERIDOS: `pares()` nao cede numeral para `§secao`, entao eles nao
# entram em `cands` e contam na SEM_PAGINA_EXTRAIVEL_BASE. Treze transcricoes
# sem nenhuma guarda.
#
# A UNIDADE AQUI NAO E A FOLHA, E O ARQUIVO. Arquivo sem paginacao nao tem
# folha para abrir, e a convencao do projeto -- criada em 16/10 para PT-19A e
# praticada por PT-03E desde 15/10 -- cita `§secao`, que a checagem 5 resolve
# contra os cabecalhos. Aqui a pergunta e a mesma de sempre: a transcricao esta
# na peca?
#
# E MARCACAO E APARATO DO FORMATO, NAO CONTEUDO DA FONTE. Medido: 4 das 13
# transcricoes so passaram a conferir quando a marcacao inline do Markdown
# saiu, porque o arquivo traz `Encontramos **185 anuncios** com conteudo
# golpista` e a transcricao nao tem os asteriscos. E o mesmo que o leitor de
# HTML ja fazia com tags, um formato adiante.
MD_INLINE = re.compile(r"\*\*|\*|__|`|~~")
MD_CITACAO = re.compile(r"^\s{0,3}>\s?", re.M)
HTML_BLOCO = re.compile(r"<(script|style)\b[^>]*>.*?</\1>", re.S | re.I)
HTML_TAGS = re.compile(r"<[^>]+>")
NAO_PDF_LEGIVEL = (".md", ".markdown", ".html", ".htm", ".xml", ".txt")


def texto_integral(caminho):
    """Texto de peca NAO paginada, reduzido como `_sem_apoio` reduz folha.

    Devolve None quando a extensao nao e de texto legivel -- PDF cai fora de
    proposito, porque para ele a unidade e a folha e quem decide e `localizar`.
    """
    if not caminho.lower().endswith(NAO_PDF_LEGIVEL):
        return None
    chave = ("integral", caminho)
    pronto = _cache.get(chave)
    if pronto is None:
        with open(str(RAIZ / caminho), encoding="utf-8",
                  errors="replace") as fh:
            bruto = fh.read()
        baixo = caminho.lower()
        if baixo.endswith((".html", ".htm", ".xml")):
            bruto = HTML_BLOCO.sub(" ", bruto)
            bruto = HTML_TAGS.sub(" ", bruto)
            bruto = html.unescape(bruto)
        elif baixo.endswith((".md", ".markdown")):
            bruto = MD_CITACAO.sub("", bruto)
            bruto = MD_INLINE.sub("", bruto)
        pronto = _cache[chave] = _sem_apoio(bruto)
    return pronto


def anexos_legiveis(e):
    """Os anexos NAO-PDF de `fonte_local` que este conferidor sabe abrir."""
    out = []
    for p in (e.get("fonte_local") or "").split(";"):
        p = p.strip().replace("\\", "/")
        if p and p.lower().endswith(NAO_PDF_LEGIVEL) and (RAIZ / p).exists():
            out.append(p)
    return out


def localizar_nao_pdf(frag, anexos):
    """O fragmento esta em algum anexo nao-PDF? Devolve o caminho, ou None."""
    alvo = _sem_apoio(frag)
    if not alvo:
        return None
    for cam in anexos:
        txt = texto_integral(cam)
        if txt and alvo in txt:
            return cam
    return None


# --------------------------------------------------- CACHE DE FOLHA EM DISCO
# ACRESCENTADO EM 25/10/2026 (item 88). Tres registros citam PDF por `inteiro
# teor` e por isso ficavam fora do alcance: o conferidor sabe abrir a peca e
# nao sabe ONDE olhar. As 2.874 folhas deles custam 144 s medidos -- por rodada
# de ciclo e inviavel, e sem varredura a afirmacao deles fica INGUARDAVEL.
#
# A CHAVE TEM DUAS PARTES, e a segunda e a que importa:
#   - o SHA-256 do PDF, que a checagem 8 do ciclo ja vigia peca por peca;
#   - **a versao da receita de extracao.** `texto_pagina` concatena TRES
#     leituras -- PyPDF2, PyMuPDF e PyMuPDF com conserto de glifo -- e
#     normaliza. Se a receita mudar e o cache sobreviver, ele passa a responder
#     pela receita velha, e **cache que sobrevive a uma mudanca no extrator e
#     cache que mente**. Mexer em `texto_pagina`, em `_mupdf` ou em
#     `norm_busca` obriga a subir o numero abaixo.
#
# O cache e DERIVADO e fica fora do git: `data/cache/` esta no .gitignore. Ele
# nao e fonte de nada -- some sem perda, e a proxima rodada o reconstroi.
RECEITA_EXTRACAO = "v1"
CACHE_DIR = RAIZ / "data/cache/folhas"


def _sha_arquivo(caminho):
    h = hashlib.sha256()
    with open(str(RAIZ / caminho), "rb") as fh:
        for bloco in iter(lambda: fh.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def folhas_da_peca(caminho, verboso=False):
    """Texto reduzido de TODAS as folhas de um PDF, com cache em disco.

    Devolve [(n, texto_reduzido)]. O texto ja vem por `_sem_apoio`, que e a
    reducao com que as comparacoes integrais sao feitas -- guardar o bruto
    custaria o triplo e nenhuma pergunta deste arquivo o usa.
    """
    sha = _sha_arquivo(caminho)
    alvo = CACHE_DIR / ("%s-%s.json.gz" % (sha[:32], RECEITA_EXTRACAO))
    if alvo.exists():
        with gzip.open(str(alvo), "rt", encoding="utf-8") as fh:
            d = json.load(fh)
        # O arquivo so e aceito se as DUAS partes da chave baterem. O nome ja
        # as carrega; conferir o conteudo pega cache renomeado a mao.
        if d.get("sha256") == sha and d.get("receita") == RECEITA_EXTRACAO:
            return [(i + 1, s) for i, s in enumerate(d["folhas"])]
    folhas, n = [], 1
    while True:
        txt = texto_pagina(caminho, n)
        if txt is None:
            break
        folhas.append(_sem_apoio(txt))
        n += 1
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    with gzip.open(str(alvo), "wt", encoding="utf-8") as fh:
        json.dump({"sha256": sha, "receita": RECEITA_EXTRACAO,
                   "caminho": caminho, "folhas": folhas}, fh)
    if verboso:
        print("    cache gravado: %s (%d folhas, %d KB)"
              % (alvo.name, len(folhas), alvo.stat().st_size // 1024))
    return [(i + 1, s) for i, s in enumerate(folhas)]


def pdfs_integrais(e, docs):
    """Os PDFs que o registro cita SEM FOLHA -- `inteiro teor`, secao, item.

    **A busca integral vale SO aqui, e a restricao e o ponto.** Aplicada a todo
    fragmento nao localizado, ela resgataria ancora creditada a FOLHA ERRADA --
    o defeito que o item 52 mediu em quatro registros e que a folha existe para
    pegar. `inteiro teor` autoriza procurar em qualquer folha porque e o que o
    campo afirma; `fonte_pagina: 185` nao.
    """
    out = []
    for seg in (e.get("fonte_pagina") or "").split("|"):
        if ":" not in seg:
            continue
        cod, resto = seg.split(":", 1)
        cod = cod.strip()
        # o segmento cede folha? entao nao e integral, e `pares()` ja o trata
        if re.findall(r"\b\d{1,4}\b", INTERVALO.sub(" ", resto)) \
                and not ESTRUTURAL.search(resto):
            continue
        cam = (docs.get(cod) or "").replace("\\", "/")
        if cam.lower().endswith(".pdf") and (RAIZ / cam).exists() \
                and cam not in out:
            out.append(cam)
    return out


def localizar_inteiro_teor(frag, pdfs):
    """O fragmento esta em ALGUMA folha de algum dos PDFs? -> (caminho, folha)."""
    alvo = _sem_apoio(frag)
    if not alvo:
        return None
    for cam in pdfs:
        for n, red in folhas_da_peca(cam):
            if alvo in red:
                return (cam, n)
    return None


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
        if ESTRUTURAL.search(resto):
            continue
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
    """Onde aparece? (cod, pg, janela, documentos_empatados)

    PREFERE A FOLHA QUE CONFERE POR INTEIRO. Até 15/10/2026 devolvia a primeira
    folha em que qualquer janela de 40 caracteres casasse, na ordem em que os
    documentos aparecem em `fonte_pagina` — e as peças do corpus se citam entre
    si: o relatório da CPMI transcreve o do interventor, e ambos repetem a
    fórmula "Secretaria de Estado de Segurança Pública do Distrito Federal". O
    resultado era âncora creditada ao DOCUMENTO ERRADO e contada como
    localizada: uma transcrição do DODF caiu em Cappelli p.35, e a conclusão A
    de Cappelli caiu em CPMI p.576.

    O critério de localização NÃO mudou — o conjunto de fragmentos localizados é
    o mesmo. Mudou a ordem de preferência: integral, depois com a página
    vizinha, e só então janela.

    DEVOLVE TAMBÉM O EMPATE, desde 15/10/2026 (item 53): a lista de documentos
    distintos que conferem na MESMA classe da folha escolhida. Com mais de um, a
    preferência não decide nada e quem decide é a ordem de `fonte_pagina` — que
    é exatamente a fragilidade que produziu o defeito acima. Medido no codebook
    inteiro: 234 fragmentos localizados, 17 com mais de uma folha candidata, 15
    decididos pelo texto e **zero empate entre documentos**. É por isso que
    EMPATES_BASE é zero e vale como guarda.
    """
    candidatos = []
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
                candidatos.append((cod, pg, r[0], caminho))
    if not candidatos:
        return None
    # Preferencia entre folhas candidatas: integral, depois a que confere ao
    # juntar a vizinha, depois a que confere ignorando marcador de nota, e so
    # em ultimo caso a que casa por janela sem causa classificada.
    ordem = {"ok": 0, "pagina": 1, "nota": 2, "parcial": 3}
    classes = [confere_integral(fragmento, c[3], c[1]) for c in candidatos]
    melhor = min(ordem[k] for k in classes)
    cod, pg, janela, _ = candidatos[next(
        i for i, k in enumerate(classes) if ordem[k] == melhor)]
    # EMPATE: outros DOCUMENTOS conferem na mesma classe? Empate entre paginas
    # do mesmo documento nao entra -- as duas folhas pertencem a peca que o
    # registro cita, e o dano possivel e o da pagina ociosa, nao o da ancora
    # falsa. Sao duas hoje, PT-53 e PT-58, e estao no item 53.
    empatados = sorted({candidatos[i][0] for i, k in enumerate(classes)
                        if ordem[k] == melhor})
    return cod, pg, janela, tuple(empatados) if len(empatados) > 1 else ()


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    todos = "--todos" in sys.argv
    verboso = "-v" in sys.argv or "--verboso" in sys.argv

    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    docs = dados["metadados"]["registro_documentos"]
    eventos = {e["id"]: e for e in dados["eventos"]}

    # OS CANDIDATOS INCLUEM ANCORA NAO-PDF desde 25/10/2026 (item 87): ate aqui
    # a fila exigia par de `pares()`, e registro que cita por localizador
    # estrutural num `.md` ou `.html` nao entrava nela -- tres registros com
    # treze transcricoes nunca examinadas. Contar o que a fila exclui e licao
    # desta casa; aqui a fila deixa de excluir.
    cands = [e for e in dados["eventos"]
             if pares(e.get("fonte_pagina")) or anexos_legiveis(e)
             or pdfs_integrais(e, dados["metadados"]["registro_documentos"])]
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
    ok = falha = indet = parciais_total = atravessa_total = notas_total = 0
    falhas, ociosas_total = [], 0
    # CONJUNTO DE CHAVES, nao contador, desde 27/10/2026: so se pode
    # perguntar quais excecoes sobraram se se souber quais foram usadas.
    excecoes_usadas = set()
    empatados = []
    meias = []          # a guarda de 22/10/2026 — ver MEIAS_ANCORAS_BASE
    nao_pdf = []        # ancora nao-PDF localizada — ver item 87
    fora_da_peca = []   # varrida por inteiro e nao achada — ver item 88

    # O ASSERT DO ESQUEMA tambem aqui, porque este passo e o que imprime
    # a linha das meias-ancoras com os campos no escopo: se a
    # classificacao estiver desatualizada, a linha mentiria.
    for _ev in eventos.values():
        confere_esquema(_ev)

    aninhadas = {}
    for e in alvos_reg:
        # A PARIDADE VAI AOS DOIS CAMPOS desde 28/10/2026 (item 100): a
        # guarda das meias-ancoras passou a ler `mecanismo_causal`, e
        # aspa aninhada ali inverteria a paridade e esconderia aspa da
        # guarda nova -- o mesmo silencio que §34.5 documentou para
        # `fonte_trecho`. Medido ao ligar: zero perdidas nos dois.
        perdidas = (aninhamento(e.get("fonte_trecho"))
                    + aninhamento(e.get("mecanismo_causal")))
        if perdidas:
            aninhadas[e["id"]] = perdidas

        pp = pares(e.get("fonte_pagina"))
        # OS ANEXOS NAO-PDF ENTRAM NO PORTAO desde 25/10/2026 (item 87):
        # registro que cita por localizador estrutural num `.md` ou
        # `.html` tem onde ser conferido, e ate aqui saia por um destes
        # `continue` sem nunca ter transcricao examinada.
        anexos = anexos_legiveis(e)
        integrais = pdfs_integrais(e, docs)
        if not pp and not anexos and not integrais:
            print("  {:<7} ~  sem página estruturada".format(e["id"]))
            indet += 1
            continue
        tem_pdf = any((docs.get(c) or "").lower().endswith(".pdf")
                      for c, _ in pp)
        if not tem_pdf and not anexos and not integrais:
            print("  {:<7} ~  {} fora do alcance (não é PDF)".format(
                e["id"], ", ".join(c for c, _ in pp)))
            indet += 1
            # a guarda nao se aplica: sem folha de PDF nao ha onde conferir
            continue

        # A GUARDA DAS MEIAS-ANCORAS roda AQUI, e a posicao e deliberada:
        # ANTES do desvio de "referencia sem transcricao literal" logo
        # abaixo. Registro que nao tem transcricao em `fonte_trecho` e cuja
        # NOTA traz aspa que confere numa folha que ele ancora e a
        # meia-ancora mais pura que existe -- e sairia pelo `continue` sem
        # ser examinado se a guarda viesse depois.
        for _m in meias_ancoras(e, pp, docs):
            meias.append((e["id"],) + _m)

        cits = transcricoes(e.get("fonte_trecho"))
        if not cits:
            print("  {:<7} ~  {} — referência sem transcrição literal".format(
                e["id"], e["fonte_pagina"]))
            indet += 1
            continue

        achados, perdidas, usadas, fracas, parciais = [], [], set(), 0, 0
        em_anexo = []       # fragmentos achados em anexo nao-PDF
        atravessa = notas = 0
        for cit in cits:
            for frag in fragmentos(cit):
                onde = localizar(frag, pp, docs)
                if onde:
                    achados.append((frag, onde))
                    usadas.add((onde[0], onde[1]))
                    if onde[2] <= 40:
                        fracas += 1
                    if onde[3]:
                        empatados.append((e["id"], onde[3], frag))
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
                    elif _est == "nota":
                        notas += 1
                    elif _est == "parcial":
                        parciais += 1
                    continue
                # O RAMO NAO-PDF, antes da excecao: a peca sem paginacao
                # confere no ARQUIVO INTEIRO, porque nela a unidade nao e
                # a folha. Vem antes de EXCECOES de proposito -- tres das
                # oito excecoes existiam so porque este ramo nao existia,
                # e o comentario delas dizia isso.
                cam = localizar_nao_pdf(frag, anexos)
                if cam:
                    nao_pdf.append((e["id"], cam, frag))
                    em_anexo.append((frag, cam))
                    continue
                # A BUSCA INTEGRAL, com o cache de folha (item 88): vale
                # SO nos PDFs que o registro cita SEM FOLHA. 2.874 folhas
                # custam 151 s na primeira construcao e 0,27 s depois.
                achou_int = localizar_inteiro_teor(frag, integrais)
                if achou_int:
                    em_anexo.append((frag, "%s#f%d" % achou_int))
                    continue
                # EXCECAO VENCE CATEGORIA, e a ordem foi invertida em
                # 25/10/2026 (item 89): declaracao EXPLICITA do
                # pesquisador tem precedencia sobre a categoria generica
                # abaixo. Com a ordem anterior, registro que cita so por
                # localizador integral NUNCA chegava as excecoes -- a
                # categoria o engolia antes, e uma razao escrita a mao
                # ficava inerte.
                chave = next((k for k in EXCECOES
                              if k[0] == e["id"] and norm(frag).startswith(k[1])), None)
                if chave:
                    excecoes_usadas.add(chave)
                    continue
                # A PECA FOI VARRIDA POR INTEIRO E A TRANSCRICAO NAO ESTA
                # NELA. Vale so para quem cita EXCLUSIVAMENTE por
                # localizador integral: registro que declara folha e tem
                # fragmento perdido continua falhando, porque ali a folha
                # e a afirmacao. Ver INTEIRO_TEOR_SEM_ACHADO_BASE.
                if integrais and not pp:
                    fora_da_peca.append((e["id"], frag))
                    continue
                perdidas.append(frag)

        todas = {(c, p) for c, nums in pp for p in nums
                 if (docs.get(c) or "").lower().endswith(".pdf")}
        ociosas = sorted(todas - usadas)
        ociosas_total += len(ociosas)

        # O TOTAL CONTA O ANEXO NAO-PDF, desde 25/10/2026 (item 87). Sem
        # isso os registros de ancora nao paginada relatavam `OK 0/0
        # localizadas`, e **OK de total zero e pior que falha**: diz que
        # nada foi conferido com a cara de quem verificou tudo.
        total = len(achados) + len(em_anexo) + len(perdidas)
        onde_txt = ", ".join("{} p.{}".format(c, p) for c, p in sorted(usadas)[:4])
        if len(usadas) > 4:
            onde_txt += ", +{}".format(len(usadas) - 4)
        if em_anexo:
            _anx = sorted({c.split("/")[-1] for _, c in em_anexo})
            onde_txt = (onde_txt + " · " if onde_txt else "") + \
                "§{} em {}".format(len(em_anexo), ", ".join(_anx)[:58])

        # TOTAL ZERO NUNCA E OK, e a regra entra em 25/10/2026 (item 88)
        # porque o defeito apareceu TRES vezes neste arquivo: registro sem
        # nada conferido relatava `OK 0/0 localizadas`, com cara de
        # verificado. Se nada foi conferido, o registro e INDETERMINADO e diz
        # por que -- e os `confirmados` deixam de contar quem nao foi.
        if total == 0 and not perdidas:
            # A RAZAO NOMEIA A CAUSA, e desde 25/10/2026 (item 89) a excecao
            # entra na conta: PT-38 tem as duas transcricoes dispensadas por
            # EXCECOES e relatava "nada foi conferido", o que e verdade e nao
            # e a razao. Guarda que diz o que aconteceu sem dizer por que
            # obriga quem le a ir escavar.
            _nf = len([1 for r, _ in fora_da_peca if r == e["id"]])
            _nex = len([1 for k in EXCECOES if k[0] == e["id"]])
            if _nf:
                _razao = ("as {} transcrição(ões) não estão na peça citada"
                          .format(_nf))
            elif _nex:
                _razao = ("as {} transcrição(ões) estão dispensadas por "
                          "exceção registrada em EXCECOES".format(_nex))
            else:
                _razao = "nada foi conferido"
            print("  {:<7} ~  0 de 0 — {}".format(e["id"], _razao))
            indet += 1
            continue

        if perdidas:
            print("  {:<7} X  {}/{} localizadas · {}".format(
                e["id"], len(achados) + len(em_anexo), total,
                onde_txt or "nenhuma"))
            for frag in perdidas:
                print("          não localizada: «{}…»".format(norm(frag)[:64]))
            falhas.append(e["id"])
            falha += 1
        else:
            marca = "OK" if not fracas else "OK"
            print("  {:<7} {} {}/{} localizadas · {}{}{}".format(
                e["id"], marca, len(achados) + len(em_anexo), total,
                onde_txt,
                "  ({} por janela curta)".format(fracas) if fracas else "",
                "  ({} só por janela, texto integral não confere)".format(parciais)
                if parciais else ""))
            ok += 1
        parciais_total += parciais
        atravessa_total += atravessa
        notas_total += notas

        if verboso:
            for frag, (c, p, j, _) in achados:
                print("          · {} p.{} (janela {}) «{}…»".format(
                    c, p, j, norm(frag)[:52]))
        if ociosas:
            print("          · página(s) que nenhuma transcrição alcança: {}".format(
                ", ".join("{} p.{}".format(c, p) for c, p in ociosas)))

    print("=" * 78)
    print("confirmados {} | falhas {} | indeterminados {}".format(ok, falha, indet))

    # OS QUE ESTE CONFERIDOR NAO ALCANCA, nomeados desde 18/10/2026 (item 64).
    # Citam a fonte por localizador estrutural e nao por folha, de modo que
    # `pares()` nao devolve par e eles nunca entram em `cands`. Antes disto eles
    # simplesmente NAO APARECIAM -- e contagem que nao imprime o que exclui
    # ensina a confiar no total errado.
    # DEIXA DE CONTAR QUEM TEM ANEXO LEGIVEL, desde 25/10/2026 (item 87):
    # registro que cita por localizador estrutural num `.md` ou `.html`
    # passou a ser conferido no arquivo inteiro, e por isso sai desta
    # lista. Quem permanece sao os PDF citados por `inteiro teor`, para os
    # quais o conferidor sabe abrir a peca e nao sabe ONDE olhar -- e
    # varrer PDF inteiro custa 205 s para 16 aspas, medido em 22/10.
    sem_extraivel = sorted(e["id"] for e in dados["eventos"]
                           if (e.get("fonte_pagina") or "").strip()
                           and not pares(e.get("fonte_pagina"))
                           and not anexos_legiveis(e)
                           and not pdfs_integrais(
                               e, dados["metadados"]["registro_documentos"]))
    print("fora do alcance deste conferidor: {} registro(s) com `fonte_pagina` e "
          "sem página extraível — {}".format(len(sem_extraivel),
                                             ", ".join(sem_extraivel)))
    print("  citam por localizador estrutural (inteiro teor, peça integral, seção);")
    print("  a folha deles não existe, e por isso não há o que abrir.")
    if len(sem_extraivel) != SEM_PAGINA_EXTRAIVEL_BASE:
        # PASSA A REPROVAR EM 25/10/2026 (item 87), e e correcao de
        # garantia declarada: o comentario desta base diz, desde 18/10,
        # que "o sexto que aparecer FAZ O CICLO CAIR" -- e ela so
        # imprimia aviso, com codigo de saida zero. Achado pela prova
        # negativa do leitor de ancora nao-PDF, que testou o CODIGO DE
        # SAIDA em vez da mensagem. **Garantia que ninguem confere e a
        # que nao existe**, pela terceira vez nesta casa.
        falhas.append("alcance do conferidor mudou: {} registro(s) sem "
                      "página extraível, base {}"
                      .format(len(sem_extraivel),
                              SEM_PAGINA_EXTRAIVEL_BASE))
        print("  X A linha de base do alcance é {}, e agora são {}. Um "
              "registro deixou de ser".format(
                  SEM_PAGINA_EXTRAIVEL_BASE, len(sem_extraivel)))
        print("    conferível, ou voltou a ser: confira qual e por quê, "
              "e atualize")
        print("    SEM_PAGINA_EXTRAIVEL_BASE neste arquivo dizendo no "
              "commit a razão.")
    # A TRANSCRICAO QUE NAO ESTA NA PECA CITADA — ver
    # INTEIRO_TEOR_SEM_ACHADO_BASE (item 88).
    print("transcrição varrida na peça inteira e NÃO encontrada: {} "
          "(base {})".format(len(fora_da_peca),
                             INTEIRO_TEOR_SEM_ACHADO_BASE))
    for _rid, _frag in fora_da_peca:
        print("  ~ {:<7} «{}…»".format(_rid, norm(_frag)[:72]))
    if len(fora_da_peca) != INTEIRO_TEOR_SEM_ACHADO_BASE:
        falhas.append("transcrição fora da peça citada: {}, base {}"
                      .format(len(fora_da_peca),
                              INTEIRO_TEOR_SEM_ACHADO_BASE))
        print("    X a contagem mudou. Se uma transcrição nova não está "
              "na peça, a âncora está")
        print("      errada; se uma saiu, atualize "
              "INTEIRO_TEOR_SEM_ACHADO_BASE e diga por quê.")

    # A GUARDA DAS MEIAS-ANCORAS, de 22/10/2026 — ver MEIAS_ANCORAS_BASE.
    # A FRASE MUDOU EM 28/10/2026 (item 100), porque o escopo mudou: ela dizia
    # "campo de nota" e a guarda passou a ler tambem `mecanismo_causal`, que
    # NAO e nota. Prosa de guarda que descreve escopo menor do que o que ela
    # tem e a mesma falha que o item 97 pegou na checagem 9 -- e aqui ela
    # apareceria no proprio relatorio que o pesquisador le a cada ciclo.
    print("meias-âncoras: {} (base {}) — aspa que sustenta afirmação do "
          "registro e vive fora de `fonte_trecho`, nos campos {}"
          .format(len(meias), MEIAS_ANCORAS_BASE,
                  ", ".join("`%s`" % c for c in CAMPOS_DE_NOTA)))
    for rid, campo, cod, pg, aspa in meias:
        print("  X {:<7} [{}] confere em {} p.{} e NÃO está em "
              "`fonte_trecho`".format(rid, campo, cod, pg))
        print("      «{}…»".format(norm(aspa)[:92]))
    if len(meias) != MEIAS_ANCORAS_BASE:
        print("  ~ A aspa está num campo que autoriza a prosa e que NENHUMA "
              "guarda confere contra a folha.")
        print("    Duas saídas: promovê-la a `fonte_trecho` — conferindo-a "
              "com `confere_integral` antes,")
        print("    e em recortes separados se a folha os traz separados — ou "
              "subir MEIAS_ANCORAS_BASE")
        print("    neste arquivo E dizer no commit por quê. Não há lista de "
              "dispensa, de propósito.")
    if atravessa_total:
        print("{} fragmento(s) conferem POR INTEIRO ao juntar a página vizinha: a "
              "transcrição atravessa a quebra de página.".format(atravessa_total))
    if notas_total:
        print("{} fragmento(s) conferem AO IGNORAR MARCADOR DE NOTA DE RODAPÉ: a "
              "camada de texto do PDF cola o número da nota na prosa."
              .format(notas_total))
    if parciais_total:
        print("{} fragmento(s) localizado(s) SO POR JANELA, SEM CAUSA "
              "CLASSIFICADA: a janela confere e o texto integral nao."
              .format(parciais_total))
        print("ISTO É O PONTO CEGO REAL — editar a cauda de uma transcrição longa.")
        print("A linha de base é ZERO desde 15/10/2026: eram 45 em 09/10, 17 em")
        print("10/10 e 0 depois que a tarefa 26(b) classificou as duas últimas")
        print("causas — âncora atribuída à folha errada (4 casos: 3 de documento")
        print("errado e 1 de página errada no mesmo documento, corrigidos no")
        print("localizador) e marcador de nota de rodapé (11 casos, classe própria).")
        print("Rode com -v, compare casa/total e ache a que mudou.")
        print("Para ver quais, rode com -v e compare casa/total.".format())
    if ociosas_total:
        print("{} página(s) listada(s) que nenhuma transcrição alcança. Não é falha: a "
              "página pode\nsustentar um fato que o registro não transcreve entre aspas. "
              "É onde olhar primeiro\nquando uma âncora estiver sob suspeita.".format(
                  ociosas_total))
    if excecoes_usadas:
        print("{} de {} exceção(ões) de EXCECOES foram usadas."
              .format(len(excecoes_usadas), len(EXCECOES)))
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
    if empatados:
        print()
        print("EMPATE ENTRE DOCUMENTOS — a âncora foi escolhida pela ORDEM de")
        print("fonte_pagina, não pelo texto: mais de um documento confere na mesma")
        print("classe. É a forma exata do defeito que passou dois meses invisível —")
        print("as peças deste corpus se citam entre si, e janela de N caracteres mede")
        print("semelhança de texto, não procedência. Abra as duas folhas e decida.")
        for rid, codigos, frag in empatados:
            print("  {:<7} {}  «{}…»".format(
                rid, " = ".join(codigos), norm(frag)[:52]))

    # SO em --todos: num subconjunto a contagem mede outra coisa, e guarda que
    # dispara no recorte errado e ruido -- e ruido treina a ignorar guarda.
    if todos and len(empatados) != EMPATES_BASE:
        print("")
        print("X EMPATE ENTRE DOCUMENTOS: {} agora, {} na linha de base de "
              "15/10/2026.".format(len(empatados), EMPATES_BASE))
        print("  Ver o item 53: a medição que fixou esta base em zero.")
        return 1
    # A GUARDA DA EXCECAO OCIOSA, e ela roda SO em `--todos` pelo mesmo
    # motivo que as duas irmas abaixo: o modo amostral abre doze
    # registros e deixaria a maioria das excecoes sem exercicio, de modo
    # que acusa-las ali seria ruido -- e ruido treina a ignorar guarda.
    if todos:
        ociosas = [k for k in EXCECOES if k not in excecoes_usadas]
        if len(ociosas) != OCIOSAS_BASE:
            print("")
            print("X EXCECAO OCIOSA: {} agora, {} na linha de base de "
                  "27/10/2026.".format(len(ociosas), OCIOSAS_BASE))
            for _rid, _pref in ociosas:
                print("    ~ {:<7} «{}…»".format(_rid, _pref[:66]))
            print("  Excecao que deixou de ser usada CONTINUA "
                  "DISPENSANDO: se a transcricao que")
            print("  ela cobria for reescrita mantendo o comeco, a nova "
                  "passa pela dispensa velha.")
            print("  Duas saidas: retire a entrada de EXCECOES, ou "
                  "atualize OCIOSAS_BASE dizendo")
            print("  no commit por que uma dispensa sem uso deve ficar.")
            falhas.append("excecao ociosa: {} de {}".format(
                len(ociosas), len(EXCECOES)))
            return 1

    if todos and parciais_total != PARCIAIS_BASE:
        print("")
        print("X CASAMENTO PARCIAL SEM CAUSA CLASSIFICADA: {} agora, {} na linha "
              "de base de 15/10/2026.".format(parciais_total, PARCIAIS_BASE))
        if parciais_total > PARCIAIS_BASE:
            print("  Subiu. Uma transcrição que casava por inteiro deixou de casar —")
            print("  é exatamente a edição de cauda que a prova negativa de 09/10 viu")
            print("  escapar. Rode com -v, compare casa/total e ache a que mudou.")
        else:
            print("  Caiu, o que é bom, e ainda assim precisa de decisão: ajuste")
            print("  PARCIAIS_BASE neste arquivo e diga no commit por que caiu.")
        return 1
    return 1 if (falhas or aninhadas
                 or len(meias) != MEIAS_ANCORAS_BASE) else 0


if __name__ == "__main__":
    sys.exit(main())
