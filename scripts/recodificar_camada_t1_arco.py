#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Segunda rodada da tarefa 14: o arco conjuntural 2013 -> 2015/16 -> 2018.

A primeira rodada (04/10/2026, scripts/recodificar_camada_t1.py) ancorou PT-01,
PT-02 e PT-03 em quatro artigos e deixou SEIS pontos como decisao do
pesquisador. O primeiro deles era o mais caro:

    "A descontinuidade de 2013 para 2015-2016 nao e consensual, e o codebook
    adota um lado sem dizer. [...] Se a leitura das autoras for adotada, o
    mecanismo vira difusao intraciclo, nao apropriacao entre ciclos."

O pesquisador decidiu, em 04/10/2026, pela CONTINUIDADE, e indicou a
literatura: Marcelo Kunrath Silva. Esta rodada executa a decisao e entra com
tres pecas novas, todas lidas na fonte:

  KUNRATH SILVA 2018 — "A apropriacao conservadora do ciclo de protestos de
  2013: rumo aos protestos anti-Dilma?", Lusotopie XVII(1):88-111. E a peca que
  NOMEIA o mecanismo. Tres achados que mudam campo:

    (a) o que foi apropriado nao foram recursos nem estruturas, foi um
        REPERTORIO (§ 15). Isso vindica o nome do mecanismo de PT-02 e responde
        a cobranca que Alonso (2012, p. 24) fazia na rodada anterior — "Tilly
        nao detalha o processo de apropriacao do repertorio pelos atores" —, que
        o relatorio da primeira rodada tratou como defeito do codebook. Nao era:
        a apropriacao de repertorio e um mecanismo DISTINTO da apropriacao
        social de McAdam, Tarrow e Tilly, e e por isso que a obra deles nao a
        detalha.

    (b) a oportunidade esta invertida em relacao ao canone (§ 14): nao foi
        realinhamento de elites que abriu a oportunidade, foi o confronto
        produzido pelos movimentos progressistas, lido como oportunidade pelos
        contramovimentos conservadores.

    (c) e a ressalva que nenhum dos dois lados do debate anterior fazia (§ 56):
        "e um equivoco afirmar que tais processos posteriores ja estavam
        predeterminados pelo que ocorreu em 2013". Continuidade NAO e
        determinacao. O codebook e uma cadeia causal; a cadeia precisa dizer
        isso, ou afirma mais do que a fonte sustenta.

  KUNRATH SILVA 2023 — "Ciclo de protestos de 2013: contribuicoes do campo de
  estudos de movimentos sociais e protesto para a analise de um objeto de
  disputa", Desigualdade & Diversidade 23:57-90. Traz a ponte que faltava para
  2018: o ciclo de 2013 como "laboratorio" de enquadramentos, simbologias,
  taticas e estruturas de mobilizacao empregadas depois na campanha do
  impeachment e nas mobilizacoes da extrema-direita "articulados em torno de
  Jair Bolsonaro e/ou do intervencionismo militar" (p. 86 impressa). E a
  PRIMEIRA peca do corpus que liga o ciclo de protestos a Bolsonaro e ao
  intervencionismo militar — e por isso PT-04 deixa de ser contextual.

  ALONSO 2023 — "Treze: a politica de rua de Lula a Dilma", Companhia das
  Letras. Da o ator: o "campo patriota", presente em junho de 2013 e ignorado,
  "o maior dos lados de 2013" (p. 223). O codebook punha a direita so em PT-02,
  a partir de 2015 — e era essa ausencia que fazia a leitura de spin-off
  parecer certa.

O QUE ESTA RODADA MUDA DE FATO, e nada mais:

  1. PT-02 perde "(spin-off)" do mecanismo_causal. Spin-off afirma ruptura
     entre ciclos; a decisao do pesquisador e as tres pecas afirmam o
     contrario. Os demais nomes de mecanismo seguem na tarefa 19.
  2. PT-01 e PT-02 passam a nomear o campo patriota entre os atores de 2013.
  3. PT-04 passa de Contextual a Confirmado quanto a genealogia do ator e ao
     mecanismo — e declara, no status, o que continua sem ancora (o repertorio
     digital da campanha, o enquadramento 'nova politica', a validacao do TSE).
  4. Ancoras novas com pagina em PT-01, PT-02, PT-03 e PT-04.
  5. PT-05, PT-06 e PT-08 seguem contextuais. PT-05 ganha a nota de que as
     pecas novas cobrem a genealogia do conflito, nao o periodo.

TRES ARMADILHAS DE LOCALIZACAO, todas declaradas em PROCEDENCIA:

  - KUNRATH SILVA 2018 vem da edicao eletronica da OpenEdition, que NAO
    reproduz a paginacao impressa 88-111. A unidade citavel e o PARAGRAFO (§),
    numerado pela propria OpenEdition. fonte_pagina guarda a pagina do PDF,
    como sempre; fonte_trecho traz o §.
  - KUNRATH SILVA 2023: pagina impressa = PDF + 56.
  - ALONSO 2023 e edicao digital SEM paginacao impressa. Nao ha offset a
    declarar porque nao ha pagina impressa: "p. 219" e a pagina do PDF, e
    quem conferir na edicao em papel nao vai encontrar o mesmo numero.

E UMA ARMADILHA DE FERRAMENTA NOVA, que custou meia hora e vale a nota. O PDF
da OpenEdition tem camada de texto PRESENTE E ERRADA: a fonte Gentium-Book-Basic
vem subconjuntada com CMap defeituoso, e o codigo de cada glifo e o ASCII menos
29 — espaco=0x03, 'A'=0x24, 'a'=0x44, virgula=0x0F, '0'=0x13 — com os acentuados
deslocados de 62 na faixa 0xA2. PyPDF2 e PyMuPDF devolvem os dois a mesma
sopa de letras. Isto e PIOR que a digitalizacao sem texto de Tatagiba (2014):
ali a string vinha vazia e a ausencia era visivel; aqui a string vem cheia, e
uma busca por qualquer frase "prova" com alta confianca que o artigo nao a
contem. conferir_paginas.py passou a consertar isso por SPAN — as outras fontes
do mesmo arquivo saem corretas, de modo que consertar a pagina inteira estragaria
o que estava bom.

NO MESMO MOVIMENTO, um defeito que estava la desde o inicio e so apareceu agora:
PyPDF2 injeta espacos DENTRO das palavras em alguns PDFs ("destaca -se",
"empac amentos"), e por isso nenhuma das 26 ancoras novas casava. A conferencia
passou a tentar PyMuPDF quando PyPDF2 nao acha. E fallback, nao troca: so
acrescenta casamento, nunca remove, e as 63 ancoras antigas seguem iguais.

Uso:
    python scripts/recodificar_camada_t1_arco.py --dry-run
    python scripts/recodificar_camada_t1_arco.py
"""

import io
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

LIT = "Fontes/12_Camada-T-1_Literatura/"
K18 = LIT + "KUNRATH-SILVA_Apropriacao-conservadora-do-ciclo-de-protestos_Lusotopie-17-1_2018.pdf"
K23 = LIT + "KUNRATH-SILVA_Ciclo-de-protestos-de-2013-objeto-de-disputa_Desigualdade-e-Diversidade-23_2023.pdf"
A23 = LIT + "ALONSO_Treze-a-politica-de-rua-de-Lula-a-Dilma_Companhia-das-Letras_2023.pdf"

# Os codigos NAO levam hifen: a regex CITACAO de conferir_hipoteses.py e
# ([A-Za-zA-y' 0-9.]+?):  e um hifen no codigo quebra o casamento.
DOCS_NOVOS = {
    "KUNRATH SILVA 2018": K18,
    "KUNRATH SILVA 2023": K23,
    "ALONSO 2023": A23,
}

MUDANCAS = {
    "PT-01": {
        "ator_grupo": (
            "Redes difusas urbanas; MPL; e, na massificação de junho, movimentos "
            "do campo patriota, à época não reconhecidos como atores políticos"
        ),
        "+fonte_trecho": (
            " ACRÉSCIMO DE 04/10/2026, segunda rodada da tarefa 14 — três peças novas. "
            "Sobre a indeterminação que a massificação abriu, e que é a condição da "
            "apropriação: “havia uma zona de indefinição sobre quem promovia e qual a "
            "intencionalidade dos protestos” (Kunrath Silva, 2023, p. 79 impressa — PDF "
            "p. 23). Sobre quem leu essa abertura como oportunidade: “São atores destes "
            "contramovimentos que irão identificar na conflitualidade da primeira fase do "
            "ciclo de protestos de 2013 uma oportunidade para sua intervenção” (Kunrath "
            "Silva, 2018, § 13 — PDF p. 6). Sobre o que exatamente foi apropriado: “não há "
            "uma apropriação de recursos ou de estruturas organizativas, mas sim de um "
            "repertório: o protesto” (§ 15 — PDF p. 6). Sobre a virada do enquadramento "
            "midiático DENTRO de 2013, que é o que legitima o repertório: “Na segunda fase, "
            "no entanto, observa-se uma significativa e rápida reorientação do enquadramento "
            "midiático” (§ 41 — PDF p. 11). Sobre a condição que tornou a convivência "
            "possível: “a crítica ao PT ofereceu um alvo comum a uma parcela significativa "
            "dos atores heterogêneos que compartilhavam as ruas” (§ 50 — PDF p. 13). Sobre a "
            "direita já organizada antes do ciclo: “havia um intenso processo de organização "
            "e mobilização de forças sociais e políticas à direita do espectro político pelo "
            "menos desde a eleição de Lula em 2003” (Kunrath Silva, 2023, p. 77 impressa — "
            "PDF p. 21). E sobre a forma de junho: “Em junho, os campos ficaram lado a lado, "
            "sem serem aliados” (Alonso, 2023, p. 220 da edição digital)."
        ),
        "+fonte_local": "; " + K18 + "; " + K23 + "; " + A23,
        "+fonte_pagina": " | KUNRATH SILVA 2018: 6, 11, 13 | KUNRATH SILVA 2023: 21, 23 | ALONSO 2023: 220",
        "status_verificacao": (
            "Confirmado em literatura revisada por pares, lida na fonte com página. Não há "
            "fonte primária de 2013 no corpus, e o registro não a reivindica. RESSALVA DE "
            "04/10/2026: a expressão “abertura de estrutura de oportunidade política”, no "
            "mecanismo, é do cânone e Kunrath Silva (2018, § 14) a inverte para este caso — "
            "a oportunidade não vem de realinhamento de elites, vem do próprio confronto "
            "produzido pelos movimentos progressistas, lido como oportunidade pelos "
            "contramovimentos. O nome do mecanismo é decisão da tarefa 19; a divergência "
            "fica declarada aqui."
        ),
        "+nota_auditoria": (
            " SEGUNDA RODADA, 04/10/2026 — o campo ator_grupo passou a nomear o campo "
            "patriota. O codebook punha a direita apenas em PT-02, a partir de 2015, e era "
            "essa ausência que fazia a leitura de ruptura parecer correta: Alonso (2023, p. "
            "223) sustenta que o campo patriota era “o maior dos lados de 2013, tão grande "
            "quanto ignorado em junho”, e Kunrath Silva (2023, p. 77 impressa) data a "
            "organização da direita “pelo menos desde a eleição de Lula em 2003”."
        ),
    },
    "PT-02": {
        "ator_grupo": (
            "MBL, Vem Pra Rua, Revoltados Online; classe média urbana — movimentos do "
            "campo patriota, já presentes em 2013 e com origem anterior ao ciclo"
        ),
        "mecanismo_causal": (
            "Apropriação parcial do repertório de protesto por contramovimentos "
            "conservadores: o confronto da primeira fase é lido como oportunidade, e a "
            "direita insere nas ruas suas causas, símbolos e táticas. Não é ciclo novo "
            "nem spin-off: é continuidade dentro de um mesmo processo de confronto — e "
            "continuidade não é determinação, porque as fontes negam que o que veio "
            "depois estivesse predeterminado por 2013"
        ),
        "+fonte_trecho": (
            " ACRÉSCIMO DE 04/10/2026, segunda rodada da tarefa 14 — a descontinuidade sai "
            "do registro, por decisão do pesquisador e com a literatura que a sustenta. O "
            "mecanismo, na fonte que o nomeia: “conflitos produzidos por movimentos sociais "
            "foram interpretados por atores de contramovimentos conservadores como "
            "oportunidades para sua mobilização” (Kunrath Silva, 2018, § 14 — PDF p. 6). O "
            "desenho do processo: “um processo dinâmico, iniciado por atores identificados "
            "com causas progressistas, mas parcialmente apropriado e transformado por atores "
            "conservadores durante a segunda fase” (§ 54 — PDF p. 14). A RESSALVA QUE O "
            "REGISTRO PASSA A CARREGAR: “é um equívoco afirmar que tais processos posteriores "
            "já estavam predeterminados pelo que ocorreu” em 2013 (§ 56 — PDF p. 14); e, "
            "depois da convergência, “observa-se uma clara demarcação e confrontação dos "
            "campos progressista e conservador” (§ 58 — PDF p. 15). A continuidade do ciclo: "
            "“desde 2013, observam-se contínuos ciclos de protesto, que não chegam a ser "
            "plenamente substituídos por períodos mais ou menos longos de estabilização "
            "política” (Kunrath Silva, 2023, p. 86-87 impressas — PDF p. 30). O ator e sua "
            "escala, em Alonso (2023, edição digital): “No campo patriota, movimentos já "
            "ativos incharam em aderentes, financiamento e implantação espacial” (p. 223); "
            "“Começou em 2015 um ciclo de protestos patriota puro-sangue” (p. 224); “Em 15 de "
            "março de 2015, apenas em São Paulo, apareceu coisa de 1 milhão, mobilizados por "
            "apenas um campo” (p. 224); e, contra a tese da novidade, “Vários de seus "
            "movimentos tinham surgido nos anos Lula ou antes” (p. 224). O arco inteiro em "
            "uma frase: “O país caiu num furacão político desde então, com dois outros ciclos "
            "de protesto, em 2015 e 2016, um impeachment, em 2016” (p. 219)."
        ),
        "+fonte_local": "; " + K18 + "; " + K23 + "; " + A23,
        "+fonte_pagina": " | KUNRATH SILVA 2018: 6, 14, 15 | KUNRATH SILVA 2023: 30 | ALONSO 2023: 219, 223, 224",
        "status_verificacao": (
            "Confirmado em literatura revisada por pares, lida na fonte com página. O "
            "mecanismo deixou de afirmar ruptura entre ciclos: a leitura de continuidade "
            "foi decidida pelo pesquisador em 04/10/2026 e está ancorada em Kunrath Silva "
            "(2018, § 14, 54; 2023, p. 86-87 impressas) e Alonso (2023, p. 223-224), ao "
            "lado de Tatagiba e Galvão (2019, p. 71). A DIVERGÊNCIA PERMANECE VISÍVEL: "
            "Alonso e Mische (2016), citadas por Kunrath Silva (2018, nota 6), sustentam a "
            "leitura oposta, e o registro não a apaga. DUAS AFIRMAÇÕES SEGUEM SEM ÂNCORA: "
            "“tolerância policial” não foi localizada em nenhuma das sete obras lidas; e o "
            "enquadramento midiático favorável está documentado para 2013 (Kunrath Silva, "
            "2018, § 41-45; Pinto, 2017, p. 130, nota 11), NÃO para 2015-2016 — o registro "
            "não transfere a âncora de um período para o outro."
        ),
        "+nota_auditoria": (
            " SEGUNDA RODADA, 04/10/2026 — o mecanismo dizia “Apropriação de repertório "
            "(spin-off): a direita converte a rua em recurso próprio e forma identidade "
            "política negativa”. O parêntese afirmava ruptura entre ciclos, e foi retirado. "
            "Três coisas sustentam a troca. (1) A decisão do pesquisador, em 04/10/2026, "
            "pela continuidade. (2) A peça que nomeia o mecanismo: Kunrath Silva (2018, § "
            "15) mostra que o que se apropria não são recursos nem estruturas, mas um "
            "repertório — o que VINDICA o nome “apropriação de repertório” e corrige o "
            "diagnóstico da primeira rodada, que tratara a observação de Alonso (2012, p. "
            "24) sobre Tilly como defeito do codebook; a apropriação de repertório é "
            "mecanismo distinto da apropriação social de McAdam, Tarrow e Tilly, e é por "
            "isso que a obra deles não a detalha. (3) A ressalva de § 56, que proíbe a "
            "leitura determinista e agora está no próprio mecanismo. O que NÃO se fez: "
            "redatar o registro. A apropriação começa na segunda fase de junho de 2013; o "
            "evento que o registro codifica continua sendo o ciclo de 2015-2016, e mudar "
            "isso é decisão sua."
        ),
    },
    "PT-03": {
        "+fonte_trecho": (
            " ACRÉSCIMO DE 04/10/2026, segunda rodada da tarefa 14. Sobre o mecanismo de "
            "certificação que o registro nomeia, a evidência mais próxima que a literatura "
            "lida oferece: “destaca-se a incorporação do protesto ao repertório de ação de "
            "forças sociais e políticas identificadas à direita do espectro ideológico” "
            "(Kunrath Silva, 2023, p. 85 impressa — PDF p. 29). Sobre a rua em 2016, em "
            "Alonso (2023, edição digital): “O processo se abriu na Câmara dos Deputados, "
            "justificado como resposta ao clamor da rua” (p. 225); “no ciclo do impeachment, "
            "a rua se partiu no meio” (p. 225); e, na votação, “os que estiveram lado a lado "
            "nas ruas em 2013 tinham confluído para dois campos antagônicos” (p. 226). Sobre "
            "o saldo dos três ciclos: “Ao longo dos três ciclos, o protagonismo nas ruas "
            "pendera para o campo patriota” (p. 226)."
        ),
        "+fonte_local": "; " + K23 + "; " + A23,
        "+fonte_pagina": " | KUNRATH SILVA 2023: 29 | ALONSO 2023: 225, 226",
        "+status_verificacao": (
            " ACRÉSCIMO DE 04/10/2026: o encadeamento com a rua ganhou âncora em Alonso "
            "(2023, p. 225-226), que registra o processo aberto na Câmara “como resposta ao "
            "clamor da rua”. O nome do mecanismo — certificação — continua na fila da tarefa "
            "19: a definição de Dynamics of Contention exige validação por autoridade "
            "externa, e o que a literatura documenta aqui é validação pela imprensa e pela "
            "opinião pública, não por autoridade."
        ),
        "+nota_auditoria": (
            " SEGUNDA RODADA, 04/10/2026 — nenhum campo deste registro mudou de conteúdo. "
            "Entraram duas âncoras novas e a nota de que a certificação documentada é "
            "midiática, não de autoridade."
        ),
    },
    "PT-04": {
        "fonte_trecho": (
            "RECODIFICADO EM 04/10/2026, segunda rodada da tarefa 14 — o registro deixa de "
            "ser contextual. A ponte entre o ciclo de protestos e o bolsonarismo está, com "
            "página, em Kunrath Silva (2023): o ciclo de 2013 funcionou como laboratório de "
            "enquadramentos, simbologias, táticas e estruturas de mobilização empregadas nos "
            "anos seguintes na campanha do impeachment e “nas mobilizações de grupos "
            "políticos da extrema-direita crescentemente articulados em torno de Jair "
            "Bolsonaro e/ou do intervencionismo militar” (p. 86 impressa — PDF p. 30). E a "
            "genealogia do ator está em Alonso (2023, edição digital): “A ocupação da "
            "presidência da República pela facção mais extrema do campo patriota resultou do "
            "longo e lento processo político de conflito nas ruas, mas também nas "
            "instituições” (p. 227). A MESMA PÁGINA TRAZ O LIMITE: “junho não foi uma causa "
            "primeira, da qual decorreria inevitavelmente tudo o que veio depois” (p. 227), "
            "e “Longe de independentes entre si, os três campos foram partes de um mesmo "
            "processo político” (p. 227). As obras declaradas no registro original — Campos "
            "Mello (2020) e Cesarino (2022) — continuam fora do corpus e não foram lidas."
        ),
        "fonte_local": K23 + "; " + A23,
        "fonte_pagina": "KUNRATH SILVA 2023: 30 | ALONSO 2023: 227",
        "status_verificacao": (
            "Confirmado quanto ao MECANISMO e à GENEALOGIA DO ATOR, em literatura lida na "
            "fonte com página: Kunrath Silva (2023, p. 86 impressa) e Alonso (2023, p. 227). "
            "O QUE CONTINUA SEM ÂNCORA, e o registro não finge o contrário: o repertório da "
            "campanha de 2018 — a campanha digital massiva e o uso de WhatsApp —, o "
            "enquadramento “nova política” / “anti-sistema”, e a validação do resultado pelo "
            "TSE. Nenhuma das sete obras do eixo 12 trata da eleição de 2018, e a varredura "
            "de 04/10/2026 nos 145 arquivos da pasta de textos de ação coletiva não achou "
            "literatura do período. O registro passou a Confirmado porque a cadeia causal que "
            "ele afirma está ancorada, não porque o evento esteja documentado no corpus."
        ),
        "status_classe": "Confirmado",
        "nota_auditoria": (
            "recodificado em 04/10/2026, segunda rodada da tarefa 14 — passou de Contextual a "
            "Confirmado. A primeira rodada deste mesmo dia havia declarado que “a literatura "
            "sobre o bolsonarismo não está no alcance deste projeto”, com base na varredura "
            "dos 145 arquivos e nos 411 DOIs das sínteses. A declaração estava certa sobre as "
            "duas coleções varridas e ERRADA como conclusão geral: Kunrath Silva (2023) liga o "
            "ciclo de protestos a Bolsonaro e ao intervencionismo militar em uma frase com "
            "página, e é a primeira peça do corpus a fazê-lo. A lição não é sobre o bolsonarismo: "
            "é que varredura exaustiva de duas coleções prova a lacuna DELAS, não a lacuna da "
            "literatura. A tarefa 25 passa a ter um ponto de partida dentro do corpus."
        ),
    },
    "PT-05": {
        "+fonte_trecho": (
            " ACRÉSCIMO DE 04/10/2026, segunda rodada da tarefa 14: duas peças novas do eixo "
            "12 tocam a GENEALOGIA deste atrito sem documentar o período. Kunrath Silva "
            "(2023, p. 86 impressa) nomeia o intervencionismo militar como um dos eixos em "
            "torno dos quais a extrema-direita se articula depois de 2013, e Alonso (2023, p. "
            "226 da edição digital) registra que a zona de conflito em torno da violência "
            "legítima se alça ao primeiro plano na votação do impeachment, com a observação "
            "de que seu tamanho e sua força se expressariam nos anos seguintes. Nenhuma das "
            "duas cobre 2019-2022, e por isso o registro continua contextual: falta a "
            "literatura que interpreta o período, não a documentação do atrito, que PT-05A e "
            "PT-06A a PT-06C têm em fonte primária."
        ),
        "+status_verificacao": (
            " ACRÉSCIMO DE 04/10/2026: a lacuna ficou mais estreita e mais precisa. O que "
            "falta não é a genealogia — essa agora tem página — mas a análise do período "
            "2019-2022. Ver tarefa 25."
        ),
    },
    "PT-06": {
        "+status_verificacao": (
            " ACRÉSCIMO DE 04/10/2026: as três peças que entraram na segunda rodada da tarefa "
            "14 não dizem nada sobre a pandemia nem sobre o ecossistema informacional "
            "paralelo. A lacuna deste registro é a mais cara da camada, porque o mecanismo que "
            "ele afirma é a junta entre T-1 conjuntural e T-1 operacional."
        ),
    },
    "PT-08": {
        "+status_verificacao": (
            " ACRÉSCIMO DE 04/10/2026: as três peças que entraram na segunda rodada da tarefa "
            "14 não tratam de 6 de janeiro de 2021."
        ),
    },
}

NOTA_REVISAO = (
    "2026-10-04 (tarefa 14, segunda rodada) — o arco conjuntural passa a ser codificado "
    "como CONTINUIDADE, por decisão do pesquisador, com três peças novas lidas na fonte: "
    "Kunrath Silva (2018, Lusotopie), Kunrath Silva (2023, Desigualdade & Diversidade) e "
    "Alonso (2023, Treze, Companhia das Letras). PT-02 perde o '(spin-off)' do "
    "mecanismo_causal, que afirmava ruptura entre ciclos, e passa a nomear a apropriação "
    "parcial do repertório de protesto por contramovimentos conservadores — com a ressalva, "
    "que a própria fonte impõe, de que continuidade não é determinação (§ 56). PT-01 e PT-02 "
    "passam a nomear o campo patriota entre os atores de 2013. PT-04 passa de Contextual a "
    "Confirmado quanto ao mecanismo e à genealogia do ator, declarando o que segue sem "
    "âncora. Vindicação registrada: Kunrath Silva (2018, § 15) mostra que a apropriação em "
    "causa é de REPERTÓRIO, mecanismo distinto da apropriação social de McAdam, Tarrow e "
    "Tilly — o nome que PT-02 já usava estava certo, e a cobrança da primeira rodada estava "
    "errada. Contagem de contextuais: 4 -> 3. Corpus: 31 -> 34 PDFs, 9.391 -> 9.754 páginas; "
    "a contagem documental não muda (22 PDFs, 6.951 páginas), porque o eixo 12 é literatura."
)


def aplicar(dados, seco):
    tocados = 0
    for rid, campos in MUDANCAS.items():
        ev = next((e for e in dados["eventos"] if e["id"] == rid), None)
        if ev is None:
            raise SystemExit("registro ausente: " + rid)
        for campo, valor in campos.items():
            if campo.startswith("+"):
                nome = campo[1:]
                antes = ev.get(nome) or ""
                depois = antes + valor
            else:
                nome, antes, depois = campo, ev.get(campo), valor
            if antes == depois:
                continue
            print("  {:<7} {:<20} {} -> {} car.".format(
                rid, nome, len(antes or ""), len(depois)))
            if not seco:
                ev[nome] = depois
            tocados += 1
    reg = dados["metadados"]["registro_documentos"]
    for cod, caminho in DOCS_NOVOS.items():
        if reg.get(cod) == caminho:
            continue
        print("  metadados registro_documentos += {}".format(cod))
        if not seco:
            reg[cod] = caminho
        tocados += 1
    if NOTA_REVISAO not in dados["metadados"]["revisoes"]:
        print("  metadados revisoes += nota da segunda rodada")
        if not seco:
            dados["metadados"]["revisoes"].append(NOTA_REVISAO)
        tocados += 1
    return tocados


def main():
    seco = "--dry-run" in sys.argv
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    print("RECODIFICAÇÃO — camada T-1 conjuntural, arco de continuidade{}".format(
        "  (SECO)" if seco else ""))
    print("=" * 78)
    n = aplicar(dados, seco)
    print("-" * 78)
    print("{} alteração(ões)".format(n))
    if not seco and n:
        # newline="\n" é obrigatório: o .gitattributes do projeto traz `* -text`,
        # isto é, nenhuma conversão. Sem isso, o Python no Windows grava CRLF e o
        # git mostra as 1.600 linhas do codebook como alteradas — diferença
        # fantasma que esconde as poucas linhas que de fato mudaram.
        with io.open(JSON_P, "w", encoding="utf-8", newline="\n") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print("gravado: {}".format(JSON_P.name))
        classes = {}
        for e in dados["eventos"]:
            classes[e.get("status_classe")] = classes.get(e.get("status_classe"), 0) + 1
        print("classes: " + " | ".join(
            "{} {}".format(v, k) for k, v in sorted(classes.items(), key=lambda x: -x[1])))


if __name__ == "__main__":
    main()
