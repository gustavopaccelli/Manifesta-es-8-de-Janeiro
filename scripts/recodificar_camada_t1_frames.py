#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Terceira rodada da tarefa 14: os oito encaminhamentos do pesquisador.

A segunda rodada (scripts/recodificar_camada_t1_arco.py) tirou a descontinuidade
2013 -> 2015/16 do codebook e deixou oito pontos para o pesquisador. Ele
respondeu os oito em 04/10/2026, e esta rodada executa o que e executavel. A
ordem abaixo e a dele; o que cada um virou em campo esta ao lado.

  1. "Esse e o argumento central da mudanca apos a segunda parte de junho de
     2013 quando os grupos de direita comecam a fazer parte das mobilizacoes e
     disputar o campo de mobilizacoes a partir de entao."
     -> ja aplicado na segunda rodada (ator_grupo de PT-01 e PT-02 nomeiam o
        campo patriota). Esta rodada confirma e nao mexe.

  2. "No ciclo de 2013 ha uma janela de oportunidades politicas aberta na qual
     as direitas passariam a disputar e ocupar posteriormente."
     -> PT-01.mecanismo_causal passa a ser ISSO, com as palavras dele. Resolve a
        RESSALVA que a segunda rodada so declarava: a expressao canonica
        "abertura de estrutura de oportunidade politica" sai do campo, porque
        Kunrath Silva (2018, par. 14) a INVERTE para este caso -- a oportunidade
        nao vem de realinhamento de elites, vem do proprio confronto produzido
        pelos movimentos progressistas, lido como oportunidade pelos
        contramovimentos. O registro parava de reivindicar um mecanismo cuja
        definicao a fonte contradiz.

  3. 2013 como laboratorio (Kunrath Silva 2023, p. 86 impressa): "Esse argumento
     tambem deve compor nossa analise."
     -> declarado como analise ADOTADA em PT-04, nao como achado de leitura.

  4. "Forneca os links dessas obras para que eu possa acessa-las."
     -> respondido fora do codebook, e o pesquisador ENTREGOU as quatro no mesmo
        dia. Entraram no eixo 13 como coletadas-nao-lidas, com procedencia
        declarada em gerar_codebook.py. Duas trouxeram correcao de atribuicao:
        Gohn e de 2019, nao 2020; e von Bulow e Abers e do fasciculo de 2024,
        v. 59, nao de 2022 -- o slug do DOI (gov.2022.14) e o ano da publicacao
        on-line, nao o do fasciculo. Farias e Casaroes sao TRES autores, com
        David Magalhaes. Nada disso toca o codebook; toca a bibliografia.

  5. "Trate essa ressalva para que ela venha compor o artigo. coloque no evento
     PT-02 essa ressalva explicativa como nota. Redija essa diferenca."
     -> NOTA REDIGIDA em PT-02.nota_auditoria, delimitada por
        "RESSALVA DE DATACAO". A diferenca e: o registro data o EVENTO em
        2015-2016, e esta certo; o ATOR e anterior ao evento, e a literatura da
        duas datas para isso -- antipetistas na rua em 2011 (Tatagiba e Galvao,
        2019, p. 82) e organizacao das direitas desde 2003 (Kunrath Silva, 2023,
        p. 77 impressa). O que 2015-2016 tem de proprio e a ESCALA e a
        convocacao, nao o surgimento.

  6. "Atribua esse nome. Faca isso e explique em nota essa mudanca."
     -> PT-03.mecanismo_causal: "Certificacao de eficacia" -> "RESSIGNIFICACAO
        DO PROTESTO". A nota explica por que: a certificacao de Dynamics of
        Contention exige validacao por AUTORIDADE EXTERNA, e o que a literatura
        documenta aqui e validacao pela imprensa e pela opiniao publica. Isso
        tira uma cobranca da fila da tarefa 19.

  7. Sobre o apelo de intervencao militar em marco de 2015: "Isso e uma forma de
     desejo dos grupos envolvimentos. Um frame que eles articulam como forma de
     angariar mais manifestantes do campo da direita e extrema-direita que
     pensam ideologicamente como eles."
     -> entra em PT-02.framing_narrativa como FRAME DE RECRUTAMENTO, nao como
        demanda do ciclo nem como registro novo. PT-12 ja codifica o frame
        ("Intervencao militar", "SOS Forcas Armadas") em fonte primaria; o que
        faltava era a GENEALOGIA, e ela entra em PT-12 com pagina.

  8. "execute essa tarefa tambem e resolva os conflitos."
     -> as duas pecas foram lidas na ordem pedida, e o conflito que importava se
        RESOLVEU em vez de ficar declarado. PT-02 afirmava "Tolerancia policial"
        sem ancora desde sempre. Fernandes e Silva (2021) documentam o
        CONTRARIO: "o uso prevalente de taticas de repressao fisica, pouco
        tolerantes a demonstracao publica de demandas coletivas" (PDF p. 8), com
        seletividade pelo grau de contestacao a ordem (p. 10) e policiamento
        mais duro das taticas mais disruptivas (p. 14). O campo passa a dizer
        SELETIVIDADE, nao tolerancia. DOIS LIMITES FICAM DECLARADOS: a serie e
        de um estado (RS) e termina em 2015.

AS DUAS PECAS LIDAS, e o que cada uma ancora:

  ARAUJO E SALES 2022 -- "Atuacao politica das Forcas Armadas e o fenomeno
  bolsonarista no Brasil (2013-2022)", Cadernos do Tempo Presente 13(1):26-42.
  Pagina impressa = PDF + 25, offset DERIVADO (as paginas nao imprimem numero;
  o cabecalho corrente traz "p. 26-42" e o PDF tem 17 paginas). Ancora PT-02
  (genealogia do apelo militar), PT-04 (expressao antissistemica e superacao
  parcial da atomizacao das direitas), PT-05 (instrumentalizacao autoritaria,
  artigo 142, hostilidade aos outros poderes), PT-06 (motociatas e kit Covid) e
  PT-12 (genealogia do frame).

  FERNANDES E SILVA 2021 -- "Dinamicas do controle a acao coletiva: o
  policiamento a protestos no Rio Grande do Sul", Mediacoes 26(3):485-502.
  Pagina impressa = PDF + 484, offset LIDO (a p. 1 do PDF imprime "485").
  Ancora PT-02, e e a peca que resolve o conflito do encaminhamento 8.

UMA PROMOCAO DE CLASSE, E UMA QUE NAO SE FEZ -- e a razao e a mesma:

  PT-05 passa de Contextual a Confirmado. O critario e o que PT-04 fixou na
  rodada anterior, e esta escrito na nota dele: "passou a Confirmado porque a
  cadeia causal que ele afirma esta ancorada". PT-05 afirma erosao do consenso
  institucional por atrito deliberado com os outros poderes, e Araujo e Sales
  (PDF p. 8) documentam exatamente isso: "diversos atos e motociatas ocorreram
  com o intuito de legitimar as hostilidades do mandatario em relacao aos
  membros dos outros poderes constitucionais".

  PT-06 NAO passa, pelo MESMO critario. Repertorio e enquadramento ganharam
  pagina (motociatas, tratamento precoce, kit Covid -- PDF p. 8), mas o
  MECANISMO que o registro afirma -- a consolidacao do ecossistema informacional
  paralelo, que e a junta entre T-1 conjuntural e T-1 operacional -- continua
  sem leitura. Promover aqui seria aplicar ao repertorio o critério que PT-04
  aplicou a cadeia causal, e as duas coisas nao sao a mesma. A peca que fecharia
  PT-06 entrou no corpus hoje e NAO foi lida: von Bulow e Abers (2024)
  sustentam, com pesquisa, que o bolsonarismo e movimento social, e cobrem
  marco/2020 a outubro/2021 -- o periodo exato de PT-06. Fica como item de
  julgamento do pesquisador, e e reversivel em um comando.

DOIS ACHADOS DA PROVA NEGATIVA, e o primeiro e defeito meu:

  (i) ASPA DENTRO DE ASPA TORNA A TRANSCRICAO INCONFERIVEL. A primeira redacao de
      PT-06 transcrevia "A reivindicacao do tratamento precoce e do "kit Covid"",
      com aspas aninhadas porque na fonte a expressao ja vem aspada.
      transcricoes() fatia fonte_trecho em TODO caractere de aspa e fica com os
      indices impares; a aspa interna inverte a paridade e o pedaco restante, com
      43 caracteres, cai abaixo do minimo de 45 e e descartado em silencio. O
      registro entraria no ciclo com UMA transcricao conferida em vez de tres. O
      ciclo nao distingue conferida-e-OK de nunca-conferida, e e por isso que a
      prova negativa existe. Corrigido antes de gravar.

  (ii) A JANELA DE 40 CARACTERES MASCARA ERRO DE PAGINA QUANDO O AUTOR REPETE A
      PROPRIA FORMULA. Injetado o defeito de trocar a p. 8 pela p. 7 em
      FERNANDES E SILVA 2021, a conferencia continuou aprovando: casa() desce a
      janelas de 40 caracteres, e "antes a demonstracao publica de demandas"
      aparece tambem na p. 14, que o registro lista. A ancora esta CERTA -- a
      frase inteira so existe na p. 8, conferido por busca independente nas 17
      paginas --, mas a prova negativa para esta peca e INCONCLUSIVA. E a mesma
      limitacao que o docstring de conferir_paginas.py ja declara para PT-59, e
      esta e a segunda ocorrencia: a conferencia pega vinculo errado e pagina
      errada, nao pega pagina errada dentro de uma lista de paginas do mesmo
      documento quando o texto se repete.

CONTAGEM ESPERADA: 61 primaria | 19 Confirmado | 2 Contextual | 1 Inferencia.

Uso:
    python scripts/recodificar_camada_t1_frames.py --dry-run
    python scripts/recodificar_camada_t1_frames.py
"""

import io
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

BOLSO = "Fontes/13_Bolsonarismo-mobilizacao/"
AS22 = BOLSO + "ARAUJO-SALES_Atuacao-politica-das-Forcas-Armadas-e-bolsonarismo_Cadernos-do-Tempo-Presente-13-1_2022.pdf"
FS21 = BOLSO + "FERNANDES-SILVA_Dinamicas-do-controle-a-acao-coletiva-policiamento_Mediacoes-26-3_2021.pdf"

# Sem hifen nos codigos: a regex CITACAO de conferir_hipoteses.py e
# ([A-Za-zA-y' 0-9.]+?):\s*([0-9,\s-]+) e um hifen no codigo quebra o casamento.
DOCS_NOVOS = {
    "ARAUJO E SALES 2022": AS22,
    "FERNANDES E SILVA 2021": FS21,
}

MUDANCAS = {
    # ------------------------------------------------------------------ PT-01
    "PT-01": {
        "mecanismo_causal": (
            "Janela de oportunidades políticas aberta no ciclo de 2013, na qual as "
            "direitas passariam a disputar e ocupar posteriormente — formulação do "
            "pesquisador, adotada em 04/10/2026 no lugar de “abertura de estrutura de "
            "oportunidade política”. A massificação da segunda metade de junho produz uma "
            "zona de indefinição sobre quem promovia os protestos e com que "
            "intencionalidade, e é essa indefinição, não um realinhamento de elites, que "
            "os contramovimentos conservadores leem como oportunidade de intervenção. "
            "Difusão simultânea de um repertório de rua massivo, que é o que vem a ser "
            "apropriado. A janela não determina o que se fez dela: continuidade não é "
            "determinação"
        ),
        "+status_verificacao": (
            " TERCEIRA RODADA, 04/10/2026 — A RESSALVA ACIMA ESTÁ RESOLVIDA, e não por "
            "argumento do analista: o pesquisador decidiu a formulação, e ela entrou no "
            "campo mecanismo_causal com as palavras dele. A expressão canônica saiu do "
            "registro, de modo que ele não reivindica mais um mecanismo cuja definição a "
            "própria fonte inverte. O nome do mecanismo continua sendo matéria da tarefa "
            "19 para os outros registros, não para este."
        ),
        "+nota_auditoria": (
            " TERCEIRA RODADA, 04/10/2026 — mecanismo_causal reescrito com a formulação do "
            "pesquisador (encaminhamento 2). O campo dizia “Abertura de estrutura de "
            "oportunidade política e difusão de repertório de rua massivo, posteriormente "
            "apropriado pela direita”. Duas coisas estavam erradas ali e uma só foi "
            "corrigida antes: a segunda rodada declarou a divergência com Kunrath Silva "
            "(2018, § 14) e a deixou no status, remetendo o nome à tarefa 19. O "
            "encaminhamento 2 fecha isso — “no ciclo de 2013 há uma janela de "
            "oportunidades políticas aberta na qual as direitas passariam a disputar e "
            "ocupar posteriormente” —, e a zona de indefinição de Kunrath Silva (2023, "
            "p. 79 impressa), já ancorada no registro, é o que dá conteúdo empírico à "
            "janela. O campo também passa a carregar a proibição da leitura determinista, "
            "que antes só existia em PT-02."
        ),
    },
    # ------------------------------------------------------------------ PT-02
    "PT-02": {
        "framing_narrativa": (
            "Antipetismo, anticorrupção, 'Fora Dilma'; e, já em março de 2015, o apelo de "
            "intervenção militar ('SOS Forças Armadas') — FRAME DE RECRUTAMENTO, não "
            "demanda do ciclo: é articulado pelos grupos como forma de angariar "
            "manifestantes da direita e da extrema-direita que já pensam ideologicamente "
            "como eles (leitura do pesquisador, 04/10/2026). Pouco expressivo em número no "
            "ciclo de 2015-2016, e é justamente por isso que o registro o codifica como "
            "frame e não como repertório"
        ),
        "resposta_estatal": (
            "Policiamento seletivo pelo grau de contestação à ordem — não tolerância; "
            "enquadramento midiático favorável documentado para 2013, não para 2015-2016"
        ),
        "+fonte_trecho": (
            " ACRÉSCIMO DE 04/10/2026, TERCEIRA RODADA — duas peças do eixo 13, lidas na "
            "fonte por encaminhamento do pesquisador. SOBRE A RESPOSTA ESTATAL, e isto "
            "RESOLVE o que o registro vinha declarando como sem âncora: a série de 45 anos "
            "de policiamento a protestos no Rio Grande do Sul mostra “o uso prevalente de "
            "táticas de repressão física, pouco tolerantes à demonstração pública de "
            "demandas coletivas” (Fernandes e Silva, 2021, p. 492 impressa — PDF p. 8). A "
            "seletividade, que é o que substitui a tolerância: “Os dados tendem a confirmar "
            "a seletividade da ação policial sobre os grupos mais contestadores à ordem "
            "social” (p. 494 impressa — PDF p. 10), e “as táticas da ação coletiva mais "
            "disruptivas tendem a ser mais duramente policiadas” (p. 498 impressa — PDF "
            "p. 14). Os mesmos autores nomeiam, na introdução, “a mobilização de grupos de "
            "extrema direita favoráveis à intervenção militar” como marcador recente (p. 486 "
            "impressa — PDF p. 2) — e os grupos de direita NÃO aparecem entre os atores "
            "policiados da série, o que é observação de ausência, não de tolerância "
            "documentada. SOBRE A GENEALOGIA DO FRAME de intervenção militar: “Após junho "
            "de 2013, o pleito de uma intervenção militar constitucional foi bradada por "
            "setores conservadores da sociedade” (Araujo e Sales, 2022, p. 29 impressa — "
            "PDF p. 4)."
        ),
        "+fonte_local": "; " + AS22 + "; " + FS21,
        "+fonte_pagina": " | ARAUJO E SALES 2022: 4 | FERNANDES E SILVA 2021: 2, 8, 10, 14",
        "+status_verificacao": (
            " TERCEIRA RODADA, 04/10/2026 — DAS DUAS AFIRMAÇÕES SEM ÂNCORA, UMA SE "
            "RESOLVEU E A OUTRA CONTINUA DECLARADA. (1) “Tolerância policial” SAIU do "
            "campo: Fernandes e Silva (2021, p. 492, 494, 498 impressas) documentam "
            "predomínio de repressão física e seletividade pelo grau de contestação à "
            "ordem, o oposto de tolerância. DOIS LIMITES DESTA ÂNCORA, e o registro não os "
            "esconde: a série é de UM estado (Rio Grande do Sul) e TERMINA EM 2015, de modo "
            "que não cobre 2016 nem o período posterior; e a ausência dos grupos de direita "
            "entre os atores policiados é ausência na série, não tolerância medida. (2) O "
            "enquadramento midiático favorável continua documentado para 2013 e NÃO para "
            "2015-2016. O registro segue sem transferir a âncora de um período para o outro."
        ),
        "+nota_auditoria": (
            " TERCEIRA RODADA, 04/10/2026 — três mudanças, as três por encaminhamento do "
            "pesquisador. (a) resposta_estatal deixou de dizer “Tolerância policial” "
            "(encaminhamento 8). A expressão estava no codebook desde a versão inicial e "
            "nunca tinha fonte; a leitura das duas peças não a confirmou, CONTRADISSE. É a "
            "segunda vez na tarefa 14 que uma expressão sem lastro se revela não apenas "
            "infundada, mas invertida — a primeira foi o enquadramento do adversário na boca "
            "do ator, em PT-01. (b) framing_narrativa ganhou o apelo de intervenção militar "
            "como FRAME DE RECRUTAMENTO (encaminhamento 7). O achado das faixas de março de "
            "2015 já estava em fonte_trecho desde a primeira rodada, sem campo que o "
            "acolhesse; o pesquisador decidiu que não é registro novo, é frame — e a "
            "distinção importa, porque frame se codifica no evento que o articula, não em "
            "evento próprio. PT-12 continua sendo onde o mesmo frame aparece em fonte "
            "primária. (c) a ressalva de datação virou nota redigida, abaixo. "
            "|| RESSALVA DE DATAÇÃO (encaminhamento 5, redigida em 04/10/2026). O registro "
            "data o evento em 2015-2016 e está correto: é nesse biênio que ocorrem as "
            "marchas verde-amarelas de massa, os panelaços e a convocação pelo MBL, Vem Pra "
            "Rua e Revoltados Online. O ATOR, porém, é anterior ao evento, e a literatura "
            "lida dá duas datas para isso. A primeira é de mobilização: “os grupos "
            "antipetistas já estão presentes em protestos organizados em 2011, mantendo a "
            "mesma estética e slogans” (Tatagiba e Galvão, 2019, p. 82). A segunda é de "
            "organização: “havia um intenso processo de organização e mobilização de forças "
            "sociais e políticas à direita do espectro político pelo menos desde a eleição "
            "de Lula em 2003” (Kunrath Silva, 2023, p. 77 impressa). O que 2015-2016 tem de "
            "próprio, portanto, não é o surgimento do ator nem a invenção do repertório: é a "
            "ESCALA — “em 15 de março de 2015, apenas em São Paulo, apareceu coisa de 1 "
            "milhão, mobilizados por apenas um campo” (Alonso, 2023, p. 224) — e a "
            "CONVOCAÇÃO, que passa a ser assumida por organizações identificadas. A "
            "consequência analítica é direta e é a razão de a nota existir: datar o ator em "
            "2015 produziria a leitura de ruptura que esta mesma tarefa retirou do codebook "
            "em 04/10/2026. A data do evento e a data do ator são coisas distintas, e o "
            "registro passa a dizer as duas."
        ),
    },
    # ------------------------------------------------------------------ PT-03
    "PT-03": {
        "mecanismo_causal": (
            "Ressignificação do protesto: a mobilização de rua é ressignificada como via "
            "legítima de deposição de governo eleito, e o protesto se incorpora ao "
            "repertório de ação das forças sociais e políticas à direita do espectro — "
            "precedente para T0. Nome atribuído pelo pesquisador em 04/10/2026, em "
            "substituição a “certificação de eficácia”"
        ),
        "+status_verificacao": (
            " TERCEIRA RODADA, 04/10/2026 — O NOME DO MECANISMO SAIU DA FILA DA TAREFA 19: "
            "o pesquisador atribuiu “ressignificação do protesto”, e a pendência registrada "
            "desde 30/09 está fechada neste registro. A razão da troca está na nota de "
            "auditoria."
        ),
        "+nota_auditoria": (
            " TERCEIRA RODADA, 04/10/2026 — mecanismo_causal renomeado por encaminhamento "
            "do pesquisador, de “Certificação de eficácia” para “RESSIGNIFICAÇÃO DO "
            "PROTESTO”. A explicação da mudança, que o encaminhamento 6 pediu que ficasse "
            "escrita. Certificação, em Dynamics of Contention (McAdam, Tarrow e Tilly), é a "
            "validação de um ator, de uma performance ou de uma reivindicação por uma "
            "AUTORIDADE EXTERNA — e o enunciado do registro nunca nomeou autoridade alguma. "
            "Era a cobrança do item 24.6 da agenda, aberta em 30/09/2026. A leitura da "
            "tarefa 14 não a resolveu: agravou-a, porque o que a literatura documenta aqui "
            "é validação pela imprensa e pela opinião pública, não por autoridade "
            "institucional. “Ressignificação” diz o que a fonte sustenta e não reivindica o "
            "que ela não mostra: o que muda é o SENTIDO atribuído ao protesto — “destaca-se "
            "a incorporação do protesto ao repertório de ação de forças sociais e políticas "
            "identificadas à direita do espectro ideológico” (Kunrath Silva, 2023, p. 85 "
            "impressa, já ancorado neste registro) —, e o processo se abre na Câmara "
            "“justificado como resposta ao clamor da rua” (Alonso, 2023, p. 225). O nome "
            "velho afirmava um mecanismo canônico cuja condição não se verificava; o novo "
            "descreve o mecanismo observado. NOTA DE ESCOPO: a troca vale para PT-03. As "
            "outras seis cobranças da seção 4 do documento 09 continuam na tarefa 19."
        ),
    },
    # ------------------------------------------------------------------ PT-04
    "PT-04": {
        "+fonte_trecho": (
            " ACRÉSCIMO DE 04/10/2026, TERCEIRA RODADA. O ARGUMENTO DO LABORATÓRIO PASSA A "
            "SER ANÁLISE ADOTADA, e não só achado de leitura, por decisão do pesquisador "
            "(encaminhamento 3): o ciclo de 2013 operou como laboratório de "
            "enquadramentos, simbologias, táticas e estruturas de mobilização reempregadas "
            "depois — é o que Kunrath Silva (2023, p. 86 impressa) sustenta, e é a hipótese "
            "de trabalho desta pesquisa para a passagem de T-1 conjuntural a T-1 "
            "operacional. DUAS ÂNCORAS NOVAS, de Araujo e Sales (2022), que estreitam a "
            "lacuna declarada no status. Sobre o enquadramento anti-sistema, que até aqui "
            "não tinha página: o bolsonarismo é “a expressão política antissistêmica "
            "derivada da crise de legitimidade do sistema político da Nova República após a "
            "eclosão das jornadas de junho de 2013” (p. 36 impressa — PDF p. 11). E sobre a "
            "continuidade do campo, que é o que a segunda rodada decidiu: “Acreditamos que a "
            "atomização das direitas nacionais foi, em parte, superada após 2013” (p. 36 "
            "impressa — PDF p. 11) — com o “em parte” mantido na transcrição, porque é "
            "ressalva dos autores e não do analista."
        ),
        "+fonte_local": "; " + AS22,
        "+fonte_pagina": " | ARAUJO E SALES 2022: 11",
        "+status_verificacao": (
            " TERCEIRA RODADA, 04/10/2026 — A LACUNA ESTREITOU, e o registro diz exatamente "
            "quanto. O enquadramento ANTI-SISTEMA ganhou âncora com página: Araujo e Sales "
            "(2022, p. 36 impressa) definem o bolsonarismo como a expressão política "
            "antissistêmica derivada da crise de legitimidade da Nova República após junho "
            "de 2013. CONTINUAM SEM ÂNCORA, e são três coisas, não mais quatro: o "
            "enquadramento “nova política”, o repertório da campanha de 2018 (campanha "
            "digital massiva e uso de WhatsApp) e a validação do resultado pelo TSE. "
            "Nenhuma das sete peças do eixo 12 e nenhuma das duas lidas do eixo 13 trata da "
            "eleição de 2018 em si."
        ),
        "+nota_auditoria": (
            " TERCEIRA RODADA, 04/10/2026 — o argumento do laboratório (Kunrath Silva, "
            "2023, p. 86 impressa) passa a compor a análise por decisão do pesquisador, e "
            "não apenas a figurar como citação. A mudança não é de campo: é de STATUS "
            "EPISTÊMICO da afirmação, e está escrita em fonte_trecho para que a redação do "
            "artigo não a trate como achado alheio. Duas âncoras novas de Araujo e Sales "
            "(2022, p. 36 impressa) entraram, e uma delas tira o enquadramento anti-sistema "
            "da lista de afirmações sem lastro."
        ),
    },
    # ------------------------------------------------------------------ PT-05
    "PT-05": {
        "fonte_trecho": (
            "RECODIFICADO EM 04/10/2026, TERCEIRA RODADA DA TAREFA 14 — o registro deixa de "
            "ser contextual. A literatura declarada no registro original — Abranches; "
            "Avritzer — CONTINUA FORA DO CORPUS e não foi lida; o que mudou foi a entrada "
            "de uma peça que cobre o período com página. Sobre o MECANISMO que o registro "
            "afirma, o atrito deliberado com os outros poderes: “diversos atos e motociatas "
            "ocorreram com o intuito de legitimar as hostilidades do mandatário em relação "
            "aos membros dos outros poderes constitucionais” (Araujo e Sales, 2022, p. 33 "
            "impressa — PDF p. 8). Sobre o instrumento constitucional invocado nesses atos, "
            "que é a forma institucional do enquadramento: o artigo 142 da Carta Magna foi "
            "“desfraldado pelos ativistas favoráveis à intervenção militar naquelas "
            "ocasiões” (p. 33 impressa — PDF p. 8), e “a intervenção militar para moderar o "
            "conflito entre os poderes estiveram entre as principais consignas bradadas pela "
            "turba bolsonarista” (p. 33 impressa — PDF p. 8). Sobre o uso das mobilizações: "
            "elas “foram instrumentalizadas por segmentos autoritários para pleitear a "
            "intervenção militar” (p. 31 impressa — PDF p. 6). E sobre o ator institucional "
            "do outro lado do atrito: “A partir de então, a caserna assumiu um papel mais "
            "assertivo no diálogo com líderes políticos” (p. 30 impressa — PDF p. 5). "
            "ACRÉSCIMO DA SEGUNDA RODADA, mantido: Kunrath Silva (2023, p. 86 impressa) "
            "nomeia o intervencionismo militar como um dos eixos em torno dos quais a "
            "extrema-direita se articula depois de 2013, e Alonso (2023, p. 226) registra "
            "que a zona de conflito em torno da violência legítima se alça ao primeiro plano "
            "na votação do impeachment."
        ),
        "fonte_local": AS22,
        "fonte_pagina": "ARAUJO E SALES 2022: 5, 6, 8",
        "status_verificacao": (
            "Confirmado quanto ao MECANISMO, ao REPERTÓRIO e ao ALVO, em literatura "
            "revisada por pares lida na fonte com página: Araujo e Sales (2022, p. 30, 31 e "
            "33 impressas — PDF p. 5, 6 e 8). O registro passou de Contextual a Confirmado "
            "em 04/10/2026 pelo mesmo critério que promoveu PT-04 na rodada anterior: a "
            "cadeia causal que ele afirma está ancorada. O QUE CONTINUA SEM ÂNCORA, e o "
            "registro não finge o contrário: as duas expressões exatas de "
            "framing_narrativa — “STF ditador” e “ativismo judicial” — NÃO foram "
            "localizadas na peça lida, que documenta a hostilidade aos outros poderes e o "
            "apelo ao artigo 142, não esses dois rótulos; e a resposta estatal (os "
            "inquéritos do STF) não é objeto da peça, embora esteja em fonte primária nos "
            "registros vizinhos PT-05A e PT-06A a PT-06C. A varredura de 04/10/2026 nos 145 "
            "arquivos da pasta de textos de ação coletiva continua valendo para o que ela "
            "mediu: zero ocorrências de 'Bolsonaro' e zero de 'pandemia' NAQUELA pasta — e "
            "a lição da segunda rodada vale aqui também, a varredura prova a lacuna da "
            "coleção varrida, não da literatura."
        ),
        "status_classe": "Confirmado",
        "+nota_auditoria": (
            " TERCEIRA RODADA, 04/10/2026 — PASSOU DE CONTEXTUAL A CONFIRMADO. A peça que o "
            "fez não veio de busca nova: estava entre as catorze coletadas pela tarefa 25 no "
            "mesmo dia, declarada como coletada-não-lida, e o pesquisador mandou lê-la "
            "(encaminhamento 8). Araujo e Sales (2022) cobrem exatamente o arco 2013-2022 do "
            "apelo militar, que era a lacuna mais cara da camada depois de PT-06. O critério "
            "da promoção é o de PT-04 e está dito no status: a cadeia causal afirmada está "
            "ancorada. O que a promoção NÃO cobre está declarado nominalmente — os dois "
            "rótulos de enquadramento e a resposta estatal. Três contextuais viram dois."
        ),
    },
    # ------------------------------------------------------------------ PT-06
    "PT-06": {
        "fonte_trecho": (
            "A literatura declarada no registro original — Cesarino (2022) — ENTROU no "
            "corpus em 04/10/2026 pela coleta da tarefa 25, e NÃO FOI LIDA. ACRÉSCIMO DE "
            "04/10/2026, TERCEIRA RODADA: o REPERTÓRIO e o ENQUADRAMENTO deste registro "
            "ganharam página, o MECANISMO não. Sobre o repertório: “diversos atos e "
            "motociatas ocorreram com o intuito de legitimar as hostilidades do mandatário "
            "em relação aos membros dos outros poderes constitucionais” (Araujo e Sales, "
            "2022, p. 33 impressa — PDF p. 8). Sobre a multiplicidade de pautas, que é o "
            "que o campo repertorio_acao agrega: “A multiplicidade de pautas políticas "
            "postuladas nos atos do sete de setembro destacou-se” (p. 33 impressa — PDF "
            "p. 8). Sobre o enquadramento da liberdade, que o registro nomeia: entre as "
            "consignas estavam “os pleitos da liberdade de expressão e do voto impresso "
            "auditável” (p. 33 impressa — PDF p. 8). A mesma página registra a "
            "reivindicação do tratamento precoce e do kit Covid — hidroxicloroquina, "
            "azitromicina e ivermectina — no combate ao vírus Sars-Cov-2, que é o lastro "
            "do negacionismo sanitário em repertorio_acao; a expressão não vai entre "
            "aspas aqui de propósito, porque na fonte ela já vem aspada, e aspa dentro de "
            "aspa torna a transcrição inconferível (ver nota de auditoria). O MECANISMO "
            "QUE O REGISTRO AFIRMA — a consolidação de um ecossistema "
            "informacional paralelo em Telegram e WhatsApp — CONTINUA SEM QUALQUER ÂNCORA "
            "NO CORPUS LIDO, e é a junta entre T-1 conjuntural e T-1 operacional. A peça "
            "que o fecharia está no corpus desde 04/10/2026 e não foi lida: von Bülow e "
            "Abers (2024, Government and Opposition 59:998-1016) argumentam que o "
            "bolsonarismo precisa ser entendido como MOVIMENTO SOCIAL, não só como "
            "ideologia, e analisam o negacionismo pandêmico de março de 2020 a outubro de "
            "2021 — o período exato deste registro. Ver tarefa 25."
        ),
        "fonte_local": AS22,
        "fonte_pagina": "ARAUJO E SALES 2022: 8",
        "status_verificacao": (
            "CONTEXTUAL, e a permanência é deliberada — não é falta de peça, é falta da "
            "peça certa. Repertório e enquadramento estão confirmados em literatura lida na "
            "fonte com página (Araujo e Sales, 2022, p. 33 impressa — PDF p. 8: motociatas, "
            "tratamento precoce e “kit Covid”). O MECANISMO não: a consolidação do "
            "ecossistema informacional paralelo segue sem leitura, e é ele que o registro "
            "afirma. O critério é o mesmo que promoveu PT-04 e PT-05 — o que se exige para "
            "sair de Contextual é a cadeia causal ancorada, não o repertório — e aplicá-lo "
            "com honestidade mantém ESTE registro onde está. É o registro de maior custo da "
            "camada, porque o mecanismo é a junta entre T-1 conjuntural e T-1 operacional. "
            "DUAS PEÇAS DO CORPUS O FECHARIAM, ambas coletadas em 04/10/2026 e não lidas: "
            "von Bülow e Abers (2024) e Cesarino (2022). A varredura dos 145 arquivos da "
            "pasta de textos de ação coletiva continua valendo para o que mediu, e apenas "
            "para isso."
        ),
        "+nota_auditoria": (
            " TERCEIRA RODADA, 04/10/2026 — ganhou âncora de repertório e de enquadramento, "
            "e PERMANECE CONTEXTUAL. A decisão de não promover é a parte que importa "
            "registrar, porque a tentação era promover: PT-04 saiu de contextual na rodada "
            "anterior e PT-05 saiu nesta, as duas com página nova, e PT-06 recebeu página "
            "nova no mesmo movimento. O que separa os três é QUAL campo ganhou âncora. Em "
            "PT-04 e PT-05 foi a cadeia causal; aqui foram repertório e enquadramento, e o "
            "mecanismo — ecossistema informacional paralelo — continua sem leitura. "
            "Promover seria trocar o critério no meio da aplicação, que é a forma "
            "metodológica do modo de falha deste projeto: o dado correto no referente "
            "errado. ITEM DE JULGAMENTO DO PESQUISADOR, e reversível em um comando: se a "
            "classe Confirmado passar a admitir registro com repertório e enquadramento "
            "ancorados e mecanismo declarado em aberto, este registro muda — mas aí o "
            "critério muda para todos, e PT-08 precisa ser reexaminado junto. "
            "|| DEFEITO PRÓPRIO, achado pela prova negativa e corrigido antes de o "
            "registro ser gravado. A primeira redação deste campo transcrevia “A "
            "reivindicação do tratamento precoce e do “kit Covid”” — com ASPAS "
            "ANINHADAS, porque na fonte a expressão já vem aspada. transcricoes() de "
            "conferir_paginas.py fatia fonte_trecho em todo caractere de aspa e fica com "
            "os índices ímpares; a aspa interna inverte a paridade, o pedaço restante "
            "fica com 43 caracteres, abaixo do mínimo de 45, e é DESCARTADO. O registro "
            "entraria no ciclo com uma transcrição conferida em vez de três, e a âncora "
            "do enquadramento sanitário não seria verificada por ninguém — um arquivo em "
            "Fontes/ com página ao lado, parecendo lastro. Substituída por dois trechos "
            "da mesma página sem aspas internas. A REGRA QUE ISTO DEIXA, e vale para todo "
            "o codebook: transcrição com aspa dentro de aspa não é conferida, e o "
            "silêncio do ciclo não distingue conferida-e-OK de nunca-conferida."
        ),
    },
    # ------------------------------------------------------------------ PT-12
    "PT-12": {
        "+fonte_trecho": (
            " GENEALOGIA DO FRAME, acrescentada em 04/10/2026 na terceira rodada da tarefa "
            "14 (encaminhamento 7). O frame que este registro codifica em fonte primária — "
            "“Intervenção militar”, “SOS Forças Armadas” — não nasce em novembro de 2022, e "
            "a literatura o data: “Após junho de 2013, o pleito de uma intervenção militar "
            "constitucional foi bradada por setores conservadores da sociedade” (Araujo e "
            "Sales, 2022, p. 29 impressa — PDF p. 4). A mesma peça registra que o artigo "
            "142 da Constituição foi “desfraldado pelos ativistas favoráveis à intervenção "
            "militar” nos atos de 2020-2021 (p. 33 impressa — PDF p. 8), o que põe o "
            "acampamento de 2022 como terceiro momento de um apelo que já tinha nove anos. "
            "O ACRÉSCIMO É GENEALÓGICO E NÃO ALTERA O QUE O REGISTRO AFIRMA: a existência, a "
            "escala nacional e o lastro material dos acampamentos continuam ancorados "
            "exclusivamente na CPMI, em fonte primária."
        ),
        "+fonte_local": "; " + AS22,
        "+fonte_pagina": " | ARAUJO E SALES 2022: 4, 8",
        "+nota_auditoria": (
            " | TERCEIRA RODADA DA TAREFA 14, 04/10/2026 — entrou a genealogia do frame de "
            "intervenção militar, com página, por encaminhamento do pesquisador. A "
            "classificação do registro NÃO muda: continua Confirmado em fonte primária, e o "
            "que a literatura acrescenta é a datação do frame, não a documentação do "
            "acampamento. A razão de a genealogia vir para cá, e não para um registro novo, "
            "é o encaminhamento 7: o apelo de intervenção militar é frame, articulado para "
            "angariar manifestantes do próprio campo, e frame se codifica no evento que o "
            "articula. PT-02 passou a carregar o mesmo frame em 2015; este registro é onde "
            "ele aparece em fonte primária, sete anos depois."
        ),
    },
}

NOTA_REVISAO = (
    "2026-10-04 (tarefa 14, TERCEIRA rodada) — executados os oito encaminhamentos do "
    "pesquisador. PT-01: mecanismo_causal passa a ser a formulação dele — janela de "
    "oportunidades políticas aberta em 2013, na qual as direitas passariam a disputar e "
    "ocupar posteriormente —, o que resolve a divergência que a segunda rodada apenas "
    "declarava com Kunrath Silva (2018, § 14). PT-02: “Tolerância policial” sai de "
    "resposta_estatal, contradita por Fernandes e Silva (2021, p. 492, 494, 498 "
    "impressas), que documentam predomínio de repressão física e seletividade pelo grau "
    "de contestação à ordem, com dois limites declarados (um estado, série até 2015); o "
    "apelo de intervenção militar entra em framing_narrativa como frame de recrutamento; "
    "e a ressalva de datação do ator virou nota redigida. PT-03: mecanismo_causal "
    "renomeado de “certificação de eficácia” para “ressignificação do protesto”, com a "
    "explicação em nota — a certificação de Dynamics of Contention exige autoridade "
    "externa, e o que a literatura documenta é validação pela imprensa e pela opinião "
    "pública; a cobrança do item 24.6 da agenda fecha neste registro. PT-04: o argumento "
    "do laboratório passa a compor a análise, e o enquadramento anti-sistema ganha "
    "âncora. PT-05: Contextual -> Confirmado, pelo critério de PT-04 — cadeia causal "
    "ancorada em Araujo e Sales (2022, p. 30, 31 e 33 impressas). PT-06: ganha âncora de "
    "repertório e de enquadramento e PERMANECE Contextual, porque o mecanismo que afirma "
    "— o ecossistema informacional paralelo — segue sem leitura; promovê-lo trocaria o "
    "critério no meio da aplicação. PT-12: genealogia do frame com página, sem mudança de "
    "classe. Duas peças novas ancoram registro, as duas do eixo 13 e as duas lidas na "
    "fonte: ARAUJO E SALES 2022 e FERNANDES E SILVA 2021. Contagem de contextuais: 3 -> "
    "2. Corpus: 48 -> 52 PDFs, 10.132 -> 10.207 páginas, porque o pesquisador entregou as "
    "quatro peças que a coleta automatizada não alcançara (Gohn 2019, von Bülow e Abers "
    "2024, Bastos e Recuero 2023, Farias, Casarões e Magalhães 2022), todas coletadas e "
    "NÃO lidas; a contagem documental continua em 22 PDFs e 6.951 páginas."
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
        print("  metadados revisoes += nota da terceira rodada")
        if not seco:
            dados["metadados"]["revisoes"].append(NOTA_REVISAO)
        tocados += 1
    return tocados


def main():
    seco = "--dry-run" in sys.argv
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    print("RECODIFICAÇÃO — terceira rodada, os oito encaminhamentos{}".format(
        "  (SECO)" if seco else ""))
    print("=" * 78)
    n = aplicar(dados, seco)
    print("-" * 78)
    print("{} alteração(ões)".format(n))
    if not seco and n:
        # newline="\n" é obrigatório: o .gitattributes do projeto traz `* -text`,
        # isto é, nenhuma conversão. Sem isso, o Python no Windows grava CRLF e o
        # git mostra as ~1.600 linhas do codebook como alteradas.
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
