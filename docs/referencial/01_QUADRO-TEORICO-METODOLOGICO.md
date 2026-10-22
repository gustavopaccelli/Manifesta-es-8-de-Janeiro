# Quadro teórico e metodológico — conceitos, definições, construção e aplicação

**21/10/2026.** Varredura de todo o repositório, a pedido do pesquisador. Reúne **todo conceito e verbete lido na fonte**, com a referência bibliográfica, a definição como a fonte a escreve, a genealogia do conceito e a aplicação aos registros do codebook.

**Convenção de página.** `impressa` é a paginação do periódico ou do livro; `PDF` é a folha do arquivo do corpus. Onde as duas divergem, o *offset* está declarado e foi medido folha a folha:

| Obra | Offset medido |
|:--|:--|
| McAdam, Tarrow e Tilly (2001), *Dynamics of Contention* | impressa = PDF − 24 |
| Snow, Vliegenthart e Ketelaars (2019), cap. 22 | impressa = PDF + 390 |
| Collier (2011) | impressa = PDF + 822 |
| Ricks e Liu (2018) | impressa = PDF + 841 |
| Beach e Pedersen (2013) | impressa = PDF − 8 |
| *Wiley-Blackwell Encyclopedia* (2013) | numeração impressa própria por verbete |

---

## 1. O marco — Teoria do Processo Político

**Referência.** McADAM, Doug; TARROW, Sidney; TILLY, Charles. *Dynamics of Contention*. Cambridge: Cambridge University Press, 2001. ISBN 0-521-80588-0. DOI `10.1017/CBO9780511805431`. 411 folhas de PDF, com camada de texto. **Lida na fonte**, trechos definidores citados por folha impressa.

**O que o marco é, e o que ele deixou de ser.** O programa clássico explica confronto por quatro componentes — oportunidade política, estruturas de mobilização, enquadramento e repertório. **A obra lida é a autocrítica dos próprios proponentes**, e é dela que sai a tese mais importante para este projeto:

> *"Opportunities and threats are **not objective categories**, but depend on the kind of **collective attribution** that the classical agenda limited to framing of movement goals."* (p. 45 impressa)

> **Isto é o marco declarando que a sua categoria central depende da âncora de enquadramento.** A complementaridade entre as âncoras não é escolha de desenho deste projeto: é uma correção que a Teoria do Processo Político fez em si mesma.

**Limite medido em 21/10/2026, e ele restringe o que se pode citar por esta obra.** A expressão `political opportunity structure` tem **zero** ocorrências nas 411 folhas; `exogenous`, **uma** (p. 120 impressa). **O vocabulário de estrutura de oportunidade não se cita por *Dynamics of Contention*** — cita-se pelo verbete de della Porta (seção 4.1).

**E a definição canônica de estrutura de mobilização está aqui, não num verbete:**

> *"**Mobilizing structures can be preexisting or created in the course of contention but in any case need to be appropriated as vehicles of struggle.**"* (p. 45 impressa)

**Aplicação.** É o que resolve PT-12A e PT-21 com precisão: as estruturas do 8 de Janeiro eram **preexistentes** — associações de transporte, redes do agronegócio, igrejas, redes do ciclo de 2013-2015 —, e o que o codebook chama de mobilização de recursos é, no vocabulário da obra, **apropriação social**. Não é criação de estrutura; é conversão de estrutura existente em veículo de luta.

**Obra do marco que está no corpus e NÃO está lida.** TARROW, S. *O poder em movimento*. Trad. Ana Maria Sallum. Petrópolis: Vozes, 2009. 162 folhas de PDF, digitalização em **duas páginas por folha e sem camada de texto** — `conferir_paginas.py` não a lê, e não se faz OCR dela porque a paginação resultante erraria o que uma ficha precisa ancorar.

---

## 2. Âncora teórica I — *Mechanisms*

### 2.1 O conceito, no verbete de referência

**Referência.** TARROW, Sidney. "Mechanisms". In: SNOW, D.; DELLA PORTA, D.; KLANDERMANS, B.; McADAM, D. (orgs.). *The Wiley-Blackwell Encyclopedia of Social and Political Movements*. Oxford: Wiley-Blackwell, 2013, p. 368-371. DOI `10.1002/9780470674871.wbespm127`. **Lido na fonte, integral** (4 p.).

**O que ele entrega, e é posicional.** Tarrow estabelece *"a major methodological premise: that **a range of methodological strategies are compatible with a mechanism-based approach**"*, e cruza medição direta/indireta com sistemática/etnográfica. O primeiro quadrante — *"measured directly by using **systematic events data** to identify and track the mechanisms that produce episodes of contention"* — **é onde este projeto está**. Não é analogia: é a célula da tipologia que corresponde a um codebook de eventos construído sobre fonte documental.

**Os quatro problemas, que funcionam como lista de verificação:** (i) a dificuldade de medir mecanismo diretamente; (ii) a relação com variáveis, e o risco de o mecanismo virar *"as-if statement"*; (iii) o condicionamento por contexto, com Falleti e Lynch, e a advertência de Büthe (2002) sobre *"the placement of **starting and ending points** in research using historical narratives"* — que incide diretamente sobre onde os 85 sub-eventos começam e terminam; (iv) mecanismo confundido com processo.

**A objeção que o projeto terá de enfrentar:**

> *"By **selecting on the dependent variable** — in this case, successful collective action — analysts inevitably focus on the exceptional cases… In searching for causal mechanisms that produce collective action, we should be as interested in **cases where nothing much happens** as in those in which widespread action ensues."*

**A defesa disponível, e ela precisa ser escrita antes que o parecerista a escreva:** o desfecho estudado aqui é o **fracasso**, não o sucesso — o que coloca o caso justamente do lado que Tarrow diz estar sub-representado.

**Não lido:** a revisão `.pub2` de 2022 do mesmo verbete, que não está neste volume.

### 2.2 A ontologia do mecanismo, e há duas em disputa

**Referência.** MAYNTZ, Renate. "Mechanisms in the Analysis of Social Macro-Phenomena". *Philosophy of the Social Sciences*, v. 34, n. 2, 2004. **Lida na fonte, integral** (23 p.).

**A exigência que ela impõe.** Mayntz define mecanismo com **recorrência**: o mecanismo é o que se repete através de casos. Essa exigência é a que coloca em questão o uso que este codebook faz da palavra para 85 elos de **um episódio único** — e é a razão de existir `docs/analise/09_CONCEITO-MECANISMO.md`, que levantou **catorze** concepções do termo na literatura.

**O que a revisão descartou, e vale registrar.** Boudon (1998) seria suficiente para justificar o nome sem recorrência, **mas é a posição que Mayntz cita para recusar** — sustentar-se nela é apoiar-se no lado perdedor de uma controvérsia que a própria fonte relata.

### 2.3 A definição que o projeto adota, e ela vem da âncora metodológica

**Referência.** BEACH, Derek; PEDERSEN, Rasmus Brun. *Process-Tracing Methods: Foundations and Guidelines*. Ann Arbor: The University of Michigan Press, 2013. 208 folhas. **Lida na fonte: capítulos 1 a 3 e Apêndice A**, em 21/10/2026.

> *"a causal mechanism is defined as a theory of a **system of interlocking parts that transmits causal forces from X to Y**"* (p. 29 impressa)

E a decomposição operacional, que é o que torna a definição utilizável:

> *"Each of the parts of the causal mechanism can be conceptualized as composed of **entities that undertake activities**… Entities are the factors engaging in activities…, where the **activities are the producers of change**"* (p. 29 impressa, apoiada em Machamer, Darden e Craver 2000)

**E a lógica entre parte e todo**, adaptada das condições necessárias e suficientes: cada parte é *"an **individually insufficient but necessary** part of the whole mechanism"* (Apêndice A, p. 165 impressa), na forma `X → [(n1 →) * (n2 →) …] → Y`.

**Aplicação, e é uma cobrança sobre o codebook.** O campo `mecanismo_causal` nomeia **um** mecanismo por registro, em prosa. A conceptualização de Beach e Pedersen pede **entidade + atividade**, substantivo e verbo, decomposta em partes. Os 85 nomes do codebook satisfazem isso de forma desigual — *"defecção do agente de contenção"* tem entidade e atividade; *"gatilho"* não tem nenhuma das duas. **A grade existe; a sua aplicação registro por registro não está feita.**

### 2.4 Os mecanismos nomeados, com folha

Da obra do marco, lidos e citados por folha impressa:

| Mecanismo | Folha impressa | Registros |
|:--|:--|:--|
| *brokerage* (corretagem) | 26 | PT-12A, PT-19 |
| *certification* / descertificação | 145 e 158 | PT-13, PT-06B, PT-50 |
| *mobilizing structures* | 45 | PT-12, PT-12A, PT-21 |
| *threshold* (limiar) | 307 | PT-29 — **e o nome saiu**, ver 2.5 |
| *scale shift* | 332 | PT-08, PT-19 |
| difusão e *attribution of similarity* | 333 | PT-08 |

### 2.5 *Critical mass* — e o conceito que saiu do codebook

**Referência.** OLIVER, Pamela. "Critical mass theory". In: *Wiley-Blackwell Encyclopedia*, 2013, p. 163-166. DOI `…wbespm059`. **Lido na fonte, integral** (4 p.).

**A definição, e ela desmente o uso corrente.** Em Marwell e Oliver, massa crítica são **os organizadores**, não a multidão; Oliver classifica o uso para *"initial group of protesters"* como **metafórico e frouxo**. E o modelo de limiar de Granovetter pressupõe ação *"**not from coordination and planning**"*.

**Aplicação — e esta é a única entrada deste quadro que produziu retirada de vocabulário.** O termo *massa crítica* saiu de PT-34 em 10/10/2026 e de PT-21 em 18/10/2026, e a checagem 7 do ciclo passou a vigiar o **conceito**, não a frase de um registro. E a contradição que o limiar criava era **interna ao codebook**: PT-29 afirmava limiar, que pressupõe ausência de coordenação, enquanto PT-19 afirma coordenação por criptolinguagem. PT-29 passou a chamar-se **demonstração de viabilidade**.

---

## 3. Âncora teórica II — *Framing*

**Referência.** SNOW, David A.; VLIEGENTHART, Rens; KETELAARS, Pauline. "The Framing Perspective on Social Movements: Its Conceptual Roots and Architecture". In: SNOW, D.; SOULE, S.; KRIESI, H.; McCAMMON, H. (orgs.). *The Wiley Blackwell Companion to Social Movements*. 2. ed. Hoboken: Wiley Blackwell, 2019, cap. 22, p. 392-410. **Lido na fonte, integral** (20 p.). Paginação impressa = PDF + 390.

**Por que esta peça e não outra.** O campo `marco_teorico` declarava *Framing (Snow e Benford, 2000)* até 21/10/2026 — obra `PENDENTE` e `closed`, sem depósito em repositório algum, **nunca lida**. O capítulo de 2019, do mesmo autor principal, apresenta-se como o enunciado da arquitetura: ela *"has not been fully elaborated in a single essay. We do so in the remainder of the chapter"* (p. 394). **Ter lido o capítulo de 2019 não autoriza citar a obra de 2000**, que fica como referência de genealogia.

### 3.1 Os nove conceitos-pilar

| # | Conceito | Definição, na fonte | Aplicação |
|--:|:--|:--|:--|
| 1 | **Collective action frames** | *"relatively coherent sets of action-oriented beliefs and meanings that legitimize and inspire social movement campaigns and activities"* (p. 395), com três funções: *action mobilization*, *consensus mobilization* e **contramobilização** | dá grade ao campo `framing_narrativa` — ver `02_GRADE-FUNCIONAL-ENQUADRAMENTO.md` |
| 2 | **Master frames** | os que surgem cedo num **ciclo de protesto** (Tarrow 1994) e passam a *"color and constrain"* os quadros posteriores (p. 395) | **é a ponte com a âncora do ciclo**: se 2013 abre o ciclo, a pergunta é se há quadro-mestre condicionando 2022-2023 |
| 3 | **Core framing tasks** | **diagnóstico** — problematização **mais** *"the attribution of blame or responsibility"* (p. 396) —, **prognóstico** e **motivacional** (p. 396-397) | *"fraude nas urnas"* é diagnóstica; *"intervenção federal"* é prognóstica. **São funções distintas, hoje no mesmo campo** |
| 4 | **Mecanismos discursivos** | **articulação** — *"the connection, or splicing together, and coordination of issues, events, experiences, and cultural items"* (p. 397) — e **elaboração** — *"accenting and highlighting some events, issues, and beliefs or ideas more than others"* (p. 398) | é o par que **nomeia o mecanismo de PT-07**, e a razão de o nome anterior ter saído |
| 5 | **Campos e estruturas de oportunidade discursiva** | campos que *"evolve during the course of debate"*; DOS torna a cultura política *"more or less receptive to some collective action framings over others"* (p. 398) | o capítulo cita Koopmans e Olzak (2004) exatamente aqui (p. 399) |
| 6 | **Frame crystallization** | a ascensão de um quadro sobre os competidores, de Snow, Vliegenthart e Corrigall-Brown (2007) sobre os motins franceses de 2005 (p. 399-400) | dá conceito à **disputa de nomeação** do projeto — e é uma das lacunas não resolvidas, ver `04_LACUNAS-DO-CAMPO.md` |
| 7 | **Frame alignment processes** | *"the strategic efforts of social movement actors and organizations to link their interests and goals with those of prospective adherents and resource providers"* (p. 400), em quatro tipos atribuídos a Snow *et al.* (1986): *bridging*, *amplification*, *extension*, *transformation* | é o que **PT-06** documenta, não PT-07 |
| 8 | **Frame resonance** | atributo **do quadro**, distinto do alinhamento, que é atributo de pessoas (Ketelaars 2016, p. 344, citada na p. 401) | ver a advertência de circularidade em 3.3 |
| 9 | **Framing hazards** | quatro: eventos ambíguos; **erros de enquadramento**; disputas de quadro; deslocamentos de quadro (p. 403-404) | **o caso é um caso do segundo**, e isso tensiona a categoria — ver 3.2 |

**Não lidos, e são justamente o que o capítulo resume:** BENFORD e SNOW (2000); SNOW *et al.* (1986); SNOW *et al.* (2014). Os quatro tipos de alinhamento **são atribuídos pelo capítulo** a Snow *et al.* (1986): citá-los pelo capítulo é citar o resumo; citá-los como de 1986 seria asserção sem leitura.

### 3.2 O modelo da articulação: gênero e espécie, não exclusão

> *"**frame bridging can be considered a specific form of frame articulation**, with the specific aim of connecting the movement's main frame with one which has a wider resonance in society"* (p. 400 impressa)

**A literatura de enquadramento opera por gênero e espécie.** *Bridging* não é o oposto de *articulação*: é a espécie estratégica, voltada a público, de um gênero mais amplo.

> **E é esse o modelo para as três âncoras deste quadro.** Elas não são três teorias disputando o mesmo objeto: são **três níveis de descrição** do mesmo processo — o elo, o significado e a fase. Quando duas parecem competir, a pergunta certa não é *"qual está certa?"*, é **"qual nomeia o gênero e qual nomeia a espécie?"**. O critério é operacional: foi o que resolveu o nome de PT-07.

### 3.3 Duas coisas que o capítulo cobra deste material

**O caso é um erro de enquadramento que mobilizou, e a categoria não prevê isso.** O segundo risco da lista é *"framing errors or misframings, **as when a diagnostic frame is inappropriately applied or just wrong**"* (p. 403), e o capítulo põe os riscos como aquilo que *"undermine the prospect of resonance"* — isto é, como **obstáculo**. Aqui o quadro central é diagnóstico e é **declarado falso pela fonte primária**: a denúncia da PGR fala de *"espalhar a **falsa narrativa** do emprego do sistema eletrônico de votação"* (p. 249). E o capítulo tem a lacuna escrita: *"we know comparatively little about the degree to which **frame ambiguities, errors, and shifts** function as mobilization impediments"* (p. 404).

**E a armadilha é metodológica.** O capítulo registra a crítica de que *"resonance inferences are subject to **circular-reasoning** in the sense that resonance may be automatically conflated with the occurrence of a protest event"* (p. 402). **Inferir que o quadro de fraude ressoou porque o 8 de Janeiro aconteceu é exatamente essa circularidade.** Quem quiser afirmar ressonância tem de medi-la fora do evento — adesão declarada, financiamento, acampamento —, e o codebook tem as três ancoradas em registros próprios (PT-19A, PT-12A, PT-12).

---

## 4. Âncora teórica III — *Ciclo de protesto*

**Referência.** DELLA PORTA, Donatella. "Protest cycles and waves". In: *Wiley-Blackwell Encyclopedia*, 2013, p. 513-518. DOI `…wbespm168`. **Lido na fonte, integral** (6 p.).

**A definição, que o projeto pode usar literalmente** — e o verbete a atribui a Tarrow (1994, p. 153):

> ciclo de protesto é *"a phase of heightened conflict and contention across the social system that includes: a **rapid diffusion** of collective action from more mobilized to less mobilized sectors; a **quickened pace of innovation** in the forms of contention; **new or transformed collective action frames**; a combination of organised and unorganised participation; and **sequences of intensified interactions** between challengers and authorities which can end in reform, repression and sometimes revolution"*

**São cinco componentes, e o codebook pode ser lido contra cada um.**

**Onde o caso se situa.** *"the final stages of the cycle thus see **both** processes of institutionalization **and** of radicalization, as indicated by a growing number of violent actions"* — o que dá posição teórica precisa: **fase final de ciclo, com institucionalização e radicalização simultâneas**, que é o par PT-62 (migração para arena institucional) e PT-29/PT-34 (ação violenta).

**O declínio, que descreve PT-52 e PT-62.** *"Authorities tend to increase repression, but also to **learn how to better target it**… they aim at dividing the movement, through a mix of co-optation and exclusion… they also push elites and countermovements to form **law-and-order coalitions**."*

**A ressalva que o projeto incorporou ao `marco_teorico`.** A teoria do ciclo *"has been criticized for its tendency to too quickly generalize from specific historical circumstances"* — foi construída sobre a Itália de 1966-1973 —, e *"**radicalization in a violent form does not seem to be an unavoidable consequence**"* de dinâmica cíclica. **Logo a radicalização de 2022-2023 não pode ser apresentada como fase esperada de ciclo: tem de ser explicada.**

**A abertura teórica, e é o achado do verbete.** Ele apresenta a crítica da visão determinista pela via da *eventful protest*: eventos *"transform structures largely by constituting and empowering new groups of actors or by re-empowering existing groups in new ways"* (SEWELL 1996, p. 271). **É a via pela qual um episódio único entra na literatura de movimentos por direito próprio** — e é uma das três saídas examinadas em `docs/analise/09_CONCEITO-MECANISMO.md` §3.

### 4.1 *Political opportunity* — e as dimensões que o projeto declara usar

**Referência.** DELLA PORTA, Donatella. "Political opportunity / political opportunity structure". In: *Wiley-Blackwell Encyclopedia*, 2013, p. 478-483. DOI `…wbespm159`. **Lido na fonte, integral** (6 p.).

**A formulação teórica do caso:**

> *"changes in the political opportunity structure **do not have any effect** on a social movement unless they are **perceived** as being important by the movement itself; alternatively, **closed opportunities might be perceived as open by the activists**."*

**O 8 de Janeiro é o segundo membro dessa disjunção.** A oportunidade estava fechada — resultado diplomado, posse consumada, comando militar sem adesão — e foi percebida como aberta.

**A cobrança do verbete, e é a mais dura das onze.** Duas advertências: o conceito sofreu *"an exponential growth in the concept's dimensions, up to the point of making it a sort of **trash can** for any contextual dimensions which could have an effect on social movements"*; e há *"**a lack of clarity concerning the explanandum**"* — oportunidade política foi usada para explicar mobilização, emergência de ciclo, comportamento de aliados e escolha de estratégia. **O projeto tem de declarar quais dimensões usa e o que exatamente elas explicam, ou herda as duas críticas.**

> ### A DECLARAÇÃO, e ela responde à cobrança — 21/10/2026
>
> **Este projeto usa TRÊS dimensões de oportunidade política, e nenhuma outra.** Cada uma é observável num ato datado, e nenhuma é atribuição difusa de contexto:
>
> | Dimensão | O que é, operacionalmente | O que ela explica — e só isso | Registros |
> |:--|:--|:--|:--|
> | **D1. Regra de competição eleitoral** | alteração, por decisão de autoridade com data, de quem pode concorrer | **quem está na disputa** em cada momento do arco 2016-2022 | PT-02A, PT-03B, PT-03C, PT-03D, PT-03E, PT-05A, PT-06A, PT-06C |
> | **D2. Configuração de aliança no Executivo** | presença ou ausência do aliado **no governo**, com data de entrada e de saída | **o custo de agir** para o campo desafiante: o aliado deixou o governo sete dias antes do 8/1 | PT-04, PT-05, PT-11, PT-13, PT-17, PT-20A |
> | **D3. Disposição do agente de contenção** | dimensionamento e estilo de policiamento declarados em ordem ou em depoimento | **a viabilidade física** da ação no dia | PT-20A, PT-20B, PT-22, PT-23, PT-28, PT-31, PT-37 |
>
> **E o que estas três dimensões NÃO explicam, declarado:** não explicam **a decisão de agir** — que é da âncora de enquadramento (o quadro de fraude, PT-07) e da de mobilização de recursos (PT-10A, PT-12A) —, nem explicam **a percepção** da oportunidade, que por definição da própria fonte não se deduz da estrutura. **D1 a D3 explicam a janela; não explicam quem entrou nela.**
>
> **Por que exatamente três, e não mais:** porque são as três que têm **ato datado e fonte primária** em registros do codebook. Acrescentar cultura política, grau de centralização do poder ou história democrática — todas presentes no verbete — seria importar dimensões sem lastro neste corpus, que é precisamente o mecanismo do *"trash can"* que o verbete denuncia.

### 4.2 *Demobilization*

**Referência.** FILLIEULE, Olivier. "Demobilization". In: *Wiley-Blackwell Encyclopedia*, 2013, p. 177-180. DOI `…wbespm064`. **Lido na fonte, integral** (4 p.).

**Abre declarando a lacuna:** *"**We know little about the mechanisms governing the decline of social movements**"*, citando Taylor (1989, p. 772).

**Os quatro níveis, e o caso tem três datados.** (i) desmobilização **de um campo inteiro**, com o exemplo de *"the brutal ending of the 1956 protest movement in Poland **due to harsh repression**"*; (ii) colapso de uma **campanha**; (iii) **meso**, uma organização, inclusive por *"the **banning or removal of the leadership**"*; (iv) **micro**, e *"individual demobilization is **not always voluntary**. It may also result from… **being sidelined due to forced exile or a prison sentence**"*.

**Aplicação:** o campo inteiro em PT-52; a liderança em PT-58 e PT-59; o nível individual em PT-61 — as 1.402 responsabilizações são, nos termos do verbete, **desmobilização individual involuntária por sentença**.

**As rotas de desmobilização**, que o verbete lista a partir de Taylor (1989): burocratização, institucionalização, assimilação pelo Estado, **radicalização** e ***abeyance***. Ver `04_LACUNAS-DO-CAMPO.md` §3 para a situação de PT-62 nessa tipologia.

### 4.3 *Repertoires of contention*

**Referência.** DELLA PORTA, Donatella. "Repertoires of contention". In: *Wiley-Blackwell Encyclopedia*, 2013, p. 547-549. DOI `…wbespm178`. **Lido na fonte, integral** (3 p.).

**A definição.** Repertório é *"the **whole set of means** [a group] has for making claims of different types on different individuals"* (Tilly 1986, p. 2); em formulação posterior, *"claims making routines that apply to the same **claimant-object pairs**"* (Tilly e Tarrow 2006, p. 16). E Tilly (2008) passou a falar de ***contentious performances***, *"stressing the constant innovation"*.

**O achado, e responde a uma pergunta que o artigo terá de responder.** Ao descrever o repertório **moderno**, o verbete lista suas formas:

> *"In the nineteenth century, a new repertoire of protests started to develop, including actions such as strikes, electoral rallies, public meetings, petitions, marches, insurrection, and **the invasion of legislative bodies**."*

**A invasão de corpos legislativos é forma catalogada do repertório moderno, com genealogia em Tilly.** O 8 de Janeiro é **forma conhecida**, não inovação — e o projeto pode dizê-lo com citação. Vale também para PT-08: o que difundiu não foi invenção, foi reativação de forma disponível.

**E as três marcas do repertório moderno descrevem a Praça dos Três Poderes:** **nacional** — *"addressing **seats and symbols of the national public power**"* —, **autônomo** e **modular**, *"used by a variety of actors to achieve a variety of objectives"*.

**A cobrança:** *"people tend to act within known limits, to **innovate at the margins** of the existing forms"* (Tilly 1986, p. 390). **Se o projeto afirma inovação, tem de dizer qual é a margem.**

### 4.4 *Policing protest*

**Referência.** DELLA PORTA, Donatella; REITER, Herbert. "Policing protest". In: *Wiley-Blackwell Encyclopedia*, 2013, p. 452-458. DOI `…wbespm152`. **Lido na fonte, integral** (7 p.).

**É o verbete de maior consequência para o projeto**, porque incide sobre o registro mais contestado: PT-28, o subdimensionamento do dispositivo, tratado como condição necessária.

**A definição.** *"the police strategies and practices used in order to control protest"* (della Porta e Reiter 1998a).

**Duas afirmações que retiram de "20 policiais" a evidência automática de conivência:**

> *"**The intervention of the police in the case of violations of law is additionally not automatic: in public order, many minor violations are tolerated in order to avoid major disorders.**"* E: *"**the police enjoy broad margins of discretion, at different hierarchical levels, as most decisions are taken on the spot.**"*

**As duas hipóteses rivais, em sua melhor versão:**

| | A hipótese | O que ela prevê aqui |
|:--|:--|:--|
| **Rival 1** | seletividade estrutural: *"police repression is more likely to be directed against groups that are **poorer in material resources as well as in political connections**"*, com estilos mais duros contra grupos percebidos como *"**larger threats to political elites**"* | os acampamentos eram **ricos** em recursos e em conexão política. **A literatura prediz policiamento brando, sem necessidade de conivência** — e, para sustentar omissão dolosa, o projeto tem de mostrar o que **excede** essa expectativa |
| **Rival 2** | sobrecarga analítica da inteligência: *"**The massive amount of information collected on single activists and groups… seem to have overstretched their analytical capacities.**"* | a existência de informação sem ação é **falha analítica conhecida**, não indício de intenção |

**O quadro explicativo em três partes**, que dá a PT-28 estrutura em vez de asserção: características **externas** (oportunidades políticas, incluindo *"divisions among the elites"*), **internas** (recursos, cultura profissional, militarização), *"both filtered through **police knowledge**"*. E: *"**the organizational imperative is keeping control over situations, rather than enforcing the law**"*.

**A tipologia de estilos, que o caso atravessa inteira:** *escalated force* → ***negotiated management*** (anos 1980, *"recognition of the right to demonstrate, tolerance for (even disruptive) forms of protest… limited use of coercion"*) → ***command and control*** (Vitale 2005) ou ***selective incapacitation*** (Noakes e Gillham 2006), com *"a **return to coercion, also employed preemptively**"*. **O caso muda de estilo em 24 horas** — tolerância negociada nos acampamentos, força mínima na invasão, incapacitação seletiva em massa depois. **Nomear a transição é mais forte do que afirmar omissão.**

### 4.5 *Diffusion and scale shift*

**Referência.** SOULE, Sarah A. "Diffusion and scale shift". In: *Wiley-Blackwell Encyclopedia*, 2013, p. 1338-1342. DOI `…wbespm430`. **Lido na fonte, integral** (5 p.).

**As definições.** Difusão é *"the spread or flow of an innovation across actors in a social system"* (Rogers 1995). ***Scale shift*** é *"the change in the number and level of coordinated contentious actions to a different focal point, involving a new range of actors, different objects, and broadened claims"* (McAdam, Tarrow e Tilly 2001, p. 331) — isto é, **difusão vertical** (Tarrow 2005, p. 121).

**Onde PT-08 se decide.** O verbete separa **laços diretos** — *"point-to-point contact between people via communication"* — de **laços indiretos**, em que *"shared cultural understandings and **identification of similarity** to others can lead activists to imitate the actions of others to whom they are **not directly connected**"*; mais a mídia de massa como canal indireto e a **equivalência estrutural**.

**Aplicado à evidência:** a CPMI (p. 614) registra que os organizadores invocaram o **Sri Lanka** de julho de 2022 como *"Plano B"*. Isso é **atribuição de similaridade por laço indireto**, com a mídia como canal. A tese do **laço direto** — Bannon, na frase única de Castañeda e Jenks (2023) — **não está demonstrada em nenhuma das duas fontes**.

**A tipologia de adotantes**, mais fina que "emulação": **innovators**, **early adopters** — que *"help to **legitimate** it by demonstrating its effectiveness"* —, **later adopters** e **non-adopters**. O Capitólio de 2021 e o Sri Lanka de 2022 ocupam a posição de **demonstração de eficácia**; Brasília, a de adotante tardio. E o desfecho separa os casos: no Sri Lanka a invasão derrubou o presidente; em Brasília, não.

**A cobrança:** dizer **o que exatamente difundiu** — *"is this a behavior… or an idea… or a campaign?… Are these innovations being **transplanted whole cloth or are they borrowed with some degree of adaptation**?"*

### 4.6 *Multiorganizational fields*

**Referência.** KLANDERMANS, Bert. "Multiorganizational fields". In: *Wiley-Blackwell Encyclopedia*, 2013, p. 407-408. DOI `…wbespm139`. **Lido na fonte, integral** (2 p.).

**A definição.** Campo multiorganizacional é *"the **total possible number of organizations** with which the movement organization might establish specific links"* (Curtis e Zurcher 1973; Klandermans 1992), decomposto em **alliance system** e **conflict system**, mais os indiferentes. *"Alliance systems provide resources and create political opportunities; conflict systems drain resources and restrict opportunities."*

**O que entrega a PT-50.** *"The boundaries between the two systems remain **fluid**… **Coalitions can fall apart and former allies can become opponents.**"* A descertificação tardia de PT-50 é migração de aliança para conflito, e o verbete diz que é **dinâmica esperada do campo, não anomalia**.

**E o elo com o ciclo, que amarra duas âncoras.** *"The proportion of the field engaged in one of the two systems **expands or contracts according to the cycles of protest**. At the **peak**… initially indifferent organizations may choose sides, while in a **downturn** organizations may **drop off**."*

**A cobrança:** *"The composition of a movement's organizational field is **not random**, but relates to existing cleavages in a society."* Ver `04_LACUNAS-DO-CAMPO.md` §2.

### 4.7 *Resource mobilization theory*

**Referência.** EDWARDS, Bob; GILLHAM, Patrick F. "Resource mobilization theory". In: *Wiley-Blackwell Encyclopedia*, 2013, p. 1418-1423. DOI `…wbespm447`. **Lido na fonte, integral** (6 p.).

**O que entrega.** A tipologia de acesso a recurso: **quatro mecanismos × cinco tipos de recurso = 20 relações de troca**. Recurso moral é *"bestowed by an external source"*, incluindo *"certification by an external credentialing body"*.

**Aplicação, e foi ela que nomeou dois registros.** A conta que recebe de várias unidades é **agregação**; o empresariado é **patrocínio**; o uso de estrutura preexistente é **cooptação/apropriação**. PT-12A passou a chamar-se *agregação na base e intermediação concentrada*; e o valor de `autonomia_movimento` de PT-10A passou a `Conduzido por patrocínio de setor organizado` — **a mesma fonte lida que nomeou PT-12A, cuja definição já excluía patrocínio em letras**.

### 4.8 *Discursive opportunity structure*

**Referência.** McCAMMON, Holly. "Discursive opportunity structure". In: *Wiley-Blackwell Encyclopedia*, 2013, p. 211-213. DOI `…wbespm073`. **Lido na fonte, integral** (3 p.).

**A definição de origem.** Koopmans e Statham (1999, p. 228) introduziram DOS para identificar as ideias na cultura política tidas por *"**sensible**"*, *"**realistic**"* e *"**legitimate**"*. O conceito *"**synthesizes theories of social movement framing and political opportunity structure**"*, porque *"**framing theory by itself is limited in its ability to explain why some collective action frames are more successful than others**"*.

> **É uma síntese declarada pela própria literatura entre duas das âncoras deste quadro** — e por isso é a melhor peça para sustentar a tese de complementaridade.

**A ponte para a judicialização.** Ferree (2003), no verbete: a importância dos *"**public debates over law and legal rights**"* e das formas pelas quais os atores *"must often **invoke legal constructs and negotiate legal institutions** in their collective discursive work"*. **A disputa de nomeação do 8 de Janeiro é travada em construtos jurídicos** — golpe, terrorismo, dano ao patrimônio, omissão dolosa.

**E a volatilidade, que é PT-50A.** McCammon *et al.* (2007) alertam para *"both **stability and volatility** in discursive opportunities"*. **A recaptura do enquadramento em cerca de 48 horas é volatilidade de oportunidade discursiva, não mudança de estrutura.**

---

## 5. O aparato metodológico

### 5.1 *Process tracing* — a âncora, e o estado da leitura

**Referência.** BEACH, D.; PEDERSEN, R. B. *Process-Tracing Methods: Foundations and Guidelines*. Michigan, 2013. **No corpus desde 21/10/2026, fornecida pelo pesquisador.** 208 folhas, impressa = PDF − 8. Licença lida no arquivo: **RESERVADA**. **Lidos: capítulos 1 a 3 e Apêndice A.**

A adaptação ao projeto, com as três variantes e o checklist, está em [`03_ADAPTACAO-METODOLOGICA.md`](03_ADAPTACAO-METODOLOGICA.md).

### 5.2 Os quatro testes — e a genealogia corrigida

**Referência.** COLLIER, David. "Understanding Process Tracing". *PS: Political Science & Politics*, v. 44, n. 4, 2011, p. 823-830. DOI `10.1017/S1049096511001429`. **Lido na fonte, integral** (8 folhas; impressa = PDF + 822).

**A genealogia, e ela foi corrigida no repositório em 10/10/2026.** Collier (tab. 1) declara: *"adapted from Bennett (2010), who builds on categories formulated by **Van Evera (1997)**"*. Logo os quatro testes — *straw-in-the-wind*, ***hoop***, ***smoking gun***, *doubly decisive* — são de **Van Evera (1997)**, na formulação de **Bennett (2010)**, na apresentação de **Collier (2011)**. A atribuição anterior a Beach e Pedersen saiu de seis lugares, e os três nomes entraram no registro de atribuições retiradas da checagem 7 do ciclo.

**O teste que o codebook usa.** PT-28 afirma **condição necessária (*hoop test*)**, e a âncora em português é precisa: condição necessária *"tem que estar presente para um resultado ocorrer… mas ela não produz tal resultado quando isolada"* (CUNHA e ARAÚJO 2018, p. 97).

### 5.3 O manual em português

**Referência.** CUNHA, Eleonora Schettini Martins; ARAÚJO, Carmem E. Leitão. *Process tracing nas Ciências Sociais: fundamentos e aplicabilidade*. Brasília: Enap, 2018. Coleção Metodologias. 104 folhas. **Lida na fonte**, trechos conceituais com página.

**O que ela é, no aparato:** a fonte em português dos conceitos de condição necessária e suficiente, e a peça pela qual o projeto conhecia Beach e Pedersen por **citação colhida** até 21/10/2026.

### 5.4 O desenho em sete passos

**Referência.** RICKS, Jacob I.; LIU, Amy H. "Process-Tracing Research Designs: A Practical Guide". *PS: Political Science & Politics*, v. 51, n. 4, 2018, p. 842-846. DOI `10.1017/S1049096518000975`. **Lido na fonte, integral** (5 folhas; impressa = PDF + 841). **Lida em 21/10/2026** — estava no corpus e fora do inventário de leitura.

**Os sete passos:** (1) identificar hipóteses; (2) **estabelecer linhas de tempo**; (3) **construir o grafo causal**; (4) identificar a escolha ou evento alternativo em cada momento; (5) identificar o **desfecho contrafactual** de cada alternativa; (6) achar evidência para a hipótese primária; (7) repetir para a rival.

**O que os autores declaram sobre o próprio recorte:** cobrem **uma** variante, a de **teoria-teste**, *"(Beach and Pedersen 2013)"*.

**A cobrança, e ela é a mais citada deste quadro:** *"**Counterfactuals are vital to process-tracing, especially when no alternative cases are considered**"*, e *"if a researcher is primarily focused on **one single case**… then this counterfactual exercise is important"*.

> **Os passos 2 e 3 são o que este codebook é.** Os passos 4 e 5 são o que ele **não tem de forma sistemática**: existem em **um** nó, PT-28, em `docs/analise/11_HIPOTESES-RIVAIS-PT-28.md`.

---

## 6. A literatura aplicada — o que ancora registro sem ser âncora teórica

**Distinção que esta seção mantém:** as peças abaixo **ancoram registros** do codebook com página conferida, mas não fornecem o vocabulário conceitual do desenho. São 42 peças de literatura no corpus; a lista completa com folhas, bytes, licença e rota de obtenção está em `Fontes/MANIFESTO-CORPUS.csv`, e o percurso de cada leitura, em `docs/analise/12` a `15`.

| Peça | O que ancora |
|:--|:--|
| TATAGIBA (2014); TATAGIBA e GALVÃO (2019); PINTO (2017); ALONSO (2012) | o ciclo 2013-2016 — PT-01, PT-02, PT-03. **E duas ressalvas que a leitura impôs:** o enquadramento de 2013 **não** era *"não é só por 20 centavos"*, e as autoras **negam a descontinuidade** entre 2013 e 2015-2016, o que converteu o mecanismo de PT-02 |
| KUNRATH SILVA (2018; 2023) | a apropriação conservadora do ciclo, e a inversão da estrutura de oportunidade: a oportunidade vem do confronto produzido pelos movimentos progressistas, não de realinhamento de elites |
| ARAUJO e SALES (2022) | o arco 2013-2022 do apelo militar — PT-05, PT-06 |
| VON BÜLOW e ABERS (2024) | PT-06, **e a retificação**: as redes digitais da direita radical cresciam desde o início dos anos 2000, de modo que a pandemia **carrega** uma infraestrutura que encontra pronta |
| CESARINO (2019; 2022) | o ambiente informacional em camadas, incluindo os aplicativos fechados — PT-06 |
| FERNANDES e SILVA (2021) | o policiamento seletivo, **e a contradição que retirou um enunciado**: PT-02 deixou de afirmar *"tolerância policial"*, que nunca teve fonte |
| CARVALHO e TATAGIBA (2025) | PT-62, o efeito de processo |
| CASTAÑEDA e JENKS (2023); CHEN, LUKITO e KOO (2023) | PT-08, o comparado com o 6 de janeiro — **com o limite declarado**: a ligação com o Brasil é frase de passagem, sem aparato do lado brasileiro |
| **SINGER, ARAUJO e RUGITSKY (2022)** | **lida em 22/10/2026.** Duas coisas, e nenhuma é âncora de registro. (i) O capítulo de **Lacerda** (p. 355 impressa) dá o **lado brasileiro** da difusão do Capitólio, que PT-08 declara faltar — *"Bolsonaro tem ensaiado seu equivalente de tomada do Capitólio"*, e a fala de Eduardo Bolsonaro de janeiro de 2021 lamentando que o 6 de janeiro *"não tivesse sido mais estruturada"*. **Mas é citação colhida via imprensa (SCAPA, 2021): autoriza dizer que a literatura registra a declaração, não vale como âncora primária do que foi dito.** (ii) Um enquadramento macro para a introdução do artigo — o ***interregno*** de Streeck e a Constituição como **pacto social tácito** em perda de aderência (Araujo e Belinelli, p. 165-166). **Licença CC, acesso aberto.** Offset: **deriva em sete faixas**, de −1 a +5 |
| GURZA LAVALLE *et al.* (2018) | a crítica ao marco: identificar institucionalização com desmobilização e cooptação é defeito da literatura estadunidense, e os autores nomeiam **Tarrow (1997), McAdam, Tarrow e Tilly (2001) e Tilly e Tarrow (2007)** — isto é, o marco deste projeto |

---

## 7. O que este quadro deixa declarado

| | |
|:--|:--|
| **a cobertura das âncoras é desigual** | *Mechanisms* tem três verbetes lidos mais a obra inteira do marco; *Ciclo de protesto* tem dois; **Framing não tem verbete próprio** — sustenta-se **só** no capítulo de 2019. É a âncora com **uma perna** |
| **cinco dos onze verbetes são de della Porta** | sozinha ou com Reiter, mais a coorganização do volume. **Quem lê este referencial lê, em boa medida, uma autora** — e isso vale declarar no artigo |
| **três verbetes convergem na mesma cobrança** | *Policing protest*, *Diffusion and scale shift* e *Mechanisms* pedem, cada um por sua via, **hipótese rival explícita** — a mesma exigência dos passos 4 e 5 de Ricks e Liu. **Quatro fontes lidas, uma cobrança só**, e o projeto a satisfaz em **um** nó |
| **um identificador que inverte a regra da casa** | a enciclopédia imprime no rodapé de cada verbete um DOI `10.1002/9781405198431.wbespmNNN` que **não existe** — testados quatro no CrossRef, todos 404. O que resolve é o prefixo do ISBN eletrônico, `10.1002/9780470674871.wbespmNNN`, **que é o que as sínteses automatizadas declaram**. A regra não é *confiar na fonte contra a síntese*: é **testar o identificador, seja qual for a origem** |
