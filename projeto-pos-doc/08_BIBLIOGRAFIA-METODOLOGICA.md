# Bibliografia metodológica e posicionamento do estudo

Documento de trabalho da candidatura, produzido em 01/09/2026 e ampliado em 29/09/2026 (seção 1.1) a partir das sete sínteses `*_LeapSpace.docx` de `Fontes/05_Bibliografia-teorica/`. Não é achado de pesquisa e não deve ser citado como fonte.

Responde a três encaminhamentos: extrair das sínteses a bibliografia útil ao projeto, sobretudo no ponto metodológico; situar o projeto na produção recente; e dizer em que ele se diferencia.

---

## 1. O estatuto das sínteses — e por que ele condiciona tudo o que segue

As sete sínteses são geradas por sistema automatizado, sem autoria identificável e sem revisão por pares. O inventário de fontes já as classificava como **mapa de leitura e lista de DOIs**, nunca como fonte citável, e exigia conferência no CrossRef antes de qualquer incorporação. A primeira leva de verificação confirmou que a cautela era necessária.

**Dez itens verificados, quatro divergentes:**

| # | Referência conferida | DOI | Veredito |
|:--|:--|:--|:--|
| 1 | BEACH, D.; PEDERSEN, R. B. *Process-tracing methods*: foundations and guidelines. Ann Arbor: University of Michigan Press, 2013. | `10.3998/mpub.2556282` | **Divergente** — é a 1ª ed. (2013), não a de 2019 |
| 2 | MACHAMER, P.; DARDEN, L.; CRAVER, C. F. Thinking about mechanisms. *Philosophy of Science*, v. 67, n. 1, p. 1-25, 2000. | `10.1086/392759` | Confirmado |
| 3 | CAMMAERTS, B. Protest logics and the mediation opportunity structure. *European Journal of Communication*, v. 27, n. 2, p. 117-134, 2012. | `10.1177/0267323112441007` | Confirmado |
| 4 | ALMEIDA, P. D. Opportunity organizations and threat-induced contention. *American Journal of Sociology*, v. 109, n. 2, p. 345-400, 2003. | `10.1086/378395` | Confirmado |
| 5 | MOTTA, Renata. Transnational discursive opportunities and social movement risk frames opposing GMOs. *Social Movement Studies*, v. 14, n. 5, p. 576-595, 2015. | `10.1080/14742837.2014.947253` | Confirmado |
| 6 | KOOPMANS, R. The missing link between structure and agency. *Mobilization*, v. 10, n. 1, p. 19-33, 2005. | `10.17813/maiq.10.1.t5767064661w2u34` | Confirmado |
| 7 | McCAMMON, H. Discursive opportunity structure. In: *The Wiley-Blackwell Encyclopedia of Social and Political Movements*, 2013. | `10.1002/9780470674871.wbespm073` | Confirmado |
| 8 | BENNETT, A.; CHECKEL, J. T. (Ed.). *Process tracing*: from metaphor to analytic tool. Cambridge: Cambridge University Press, 2014. | `10.1017/CBO9781139858472` | **Divergente** — DOI alegado era inexistente |
| 9 | WALDNER, D. Process tracing and qualitative causal inference. *Security Studies*, v. 24, n. 2, p. 239-250, 2015. | `10.1080/09636412.2015.1036624` | Confirmado |
| 10 | ESCRIBÀ-FOLCH, A. Participação arriscada: manifestações e tumultos em regimes ditatoriais. *Dados*, v. 51, n. 3, p. 719-750, 2008. | `10.1590/s0011-52582008000300006` | **Divergente** — título em português, não em inglês |

**Os quatro modos de falha encontrados**, que valem como advertência para os 400 DOIs ainda não conferidos:

1. **DOI de edição trocada.** `10.3998/mpub.2556282` é a 1ª edição de Beach e Pedersen, de 2013; a 2ª, de 2019, que o projeto cita, é `10.3998/mpub.10072208`. Um leitor que seguisse o DOI da síntese chegaria a um livro cujos capítulos de testes têm outra numeração.
2. **DOI inexistente.** `10.1007/9781139858472`, atribuído a Bennett e Checkel, retorna 404: o prefixo 10.1007 é da Springer, e a obra é da Cambridge. É exatamente o modo de falha do identificador fabricado que o projeto já registrou uma vez.
3. **Título de indexação em lugar do título publicado.** Escribà-Folch (2008) saiu em português na *Dados*; o título em inglês é apenas o título paralelo do SciELO.
4. **Colisão de homônimos.** A lista de *Process tracing* atribui a Derek Beach um artigo de cirurgia global no *The Lancet Global Health*. E há uma colisão que atinge diretamente este projeto: **MOTTA, Renata** (socióloga, oportunidades discursivas transnacionais) não é **MOTTA, Rodrigo Patto Sá** (historiador, anticomunismo e mito conspiratório), que o projeto já cita. Se as duas entrarem, a lista de referências precisa trazer o prenome por extenso.

Há ainda ruído bruto: um item datado de **2099**; uma entrada reduzida a link do Scopus, sem citação; entradas duplicadas; e, na síntese de oportunidades, seis itens sobre migração, clima de negócios nos Bálcãs e deslizamentos de terra, sem relação alguma com o tema.

> **Conclusão operacional.** As sínteses são bons instrumentos de descoberta e péssimas fontes de metadados. A regra do projeto — conferir todo dado contra a fonte, nunca contra outra citação dela — aplica-se a elas integralmente. Nada abaixo entra em texto sem a conferência já feita nas dez fichas acima.

---

### 1.1 Segunda leva — os 411 DOIs, por script (29/09/2026)

A primeira leva conferiu dez itens à mão. A segunda cobriu **todos os 411 DOIs distintos** das sete sínteses (444 menções) por `scripts/verificar_dois_sinteses.py`, que consulta o CrossRef e, em resposta 404, a DataCite. Resultado: **408 existem** — quatro deles registrados na DataCite e não no CrossRef, que uma verificação de uma agência só teria descartado como inexistentes — e **3 não existem**.

**O que a segunda leva não faz, e por isso não substitui a ficha.** Ela verifica duas coisas: se o identificador resolve, e se o título que a agência devolve aparece no texto que a síntese escreve antes dele. Não verifica **edição** (o modo de falha nº 1, de Beach e Pedersen), não desfaz **homônimo** (o nº 4, de Motta e de Beach) e não lê a obra. **A regra do projeto continua: nada entra em texto sem ficha**, e as fichas são as de 1 acima.

#### As três correções

| DOI que a síntese declara | Não existe porque | DOI correto, confirmado no CrossRef | Obra |
|:--|:--|:--|:--|
| `10.1007/9781139858472` | prefixo da Springer em obra da Cambridge | `10.1017/CBO9781139858472` | BENNETT, A.; CHECKEL, J. T. (Org.). *Process tracing*: from metaphor to analytic tool. Cambridge: Cambridge University Press, 2014 |
| `10.4324/9780203856949-48` | sufixo inexistente; o capítulo está no `-40` | `10.4324/9780203856949-40` | O'HALLORAN, K. How to use corpus linguistics in the study of media discourse. In: *The Routledge Handbook of Corpus Linguistics*. London: Routledge, 2010 |
| `10.4324/9781315731377-34` | sufixo inexistente; o capítulo está no `-28` | `10.4324/9781315731377-28` | CHENOWETH, E. Political mobilization and institutions. In: *Routledge Handbook of Comparative Political Institutions*. London: Routledge, 2015 |

**O primeiro caso já era conhecido** — é a ficha 8 da primeira leva, achada e corrigida em 01/09/2026. A varredura o reencontrou, o que serve de controle: a ferramenta acha o que a conferência à mão já havia achado.

**Os dois últimos precisaram de busca por título.** Testar o DOI do livro não basta: `10.4324/9781315731377` responde, e concluir dali que o capítulo não foi depositado é erro — ele está no `-28`. A consulta que resolve é a busca bibliográfica pelo título com filtro de prefixo, não o teste do identificador declarado.

#### Um quinto modo de falha: DOIs de vizinhos trocados

Os quatro modos de falha da primeira leva tratam de **metadados errados** num item. Este é outro: **os identificadores certos nos itens errados**, dentro de uma sequência.

A síntese `Framing_process_and_alignment` lista, em ordem, dois capítulos do mesmo manual:

| A síntese atribui | ao DOI | que é, de fato, de |
|:--|:--|:--|
| Vaughan (2010), *How can teachers use a corpus for their own research?* | `…-40` | **O'Halloran** — o capítulo sobre discurso midiático |
| O'Halloran (2010), *How to use corpus linguistics in the study of media discourse* | `…-48` | **ninguém** — não existe |

Reconstruído pelo CrossRef, o par correto é: **Vaughan → `10.4324/9780203856949-34`** e **O'Halloran → `10.4324/9780203856949-40`**.

**Por que este modo é o mais perigoso dos cinco.** O `-40` resolve, tem metadados completos e passaria por qualquer verificação que pergunte apenas "este DOI existe?". Só a comparação entre o título registrado e o título declarado o revela — é o segundo eixo do verificador, e é o mesmo princípio do `conferir_paginas.py`, que abre o PDF na página em vez de confiar no campo. **Um identificador confirma a si mesmo, nunca o vínculo.**

Das 444 menções, 435 casam título com título; das 9 restantes, oito são título traduzido (a síntese escreve em inglês o que a *Dados*, a *Revista de Sociologia e Política*, a *CIAN*, a *Revista de Ciencia Política* e a *Polis* publicaram em português, espanhol ou russo — o mesmo caso do modo de falha nº 3) e a nona é este par.

---

### 1.2 Terceira leva — a leitura na fonte (29 e 30/09/2026)

A primeira leva conferiu metadado de dez itens à mão; a segunda, o identificador de todos os 411 por script. **Esta é a primeira que abre a obra.** Cobre cinco dos 43 itens da camada A; as rotas de acesso dos outros estão em `data/processed/camada_a_acesso.csv`, e **29 dos 43 dependem de acesso institucional** — Cloudflare barra SAGE, Wiley, Oxford e Chicago inclusive em navegador real.

| Ficha | Obra | Veredito da leitura |
|:--|:--|:--|
| 11 | COLLIER, D. Understanding process tracing. *PS*, v. 44, n. 4, p. 823-830, 2011 | **Divergente na atribuição** — os quatro testes são de Van Evera (1997), via Bennett (2010) |
| 12 | MAYNTZ, R. Mechanisms in the analysis of social macro-phenomena. *PSS*, v. 34, n. 2, p. 237-259, 2004 | **Divergente no conceito** — define mecanismo como processo recorrente |
| 13 | GONZÁLEZ-BAILÓN, S. et al. The dynamics of protest recruitment through an online network. *Scientific Reports*, v. 1, art. 197, 2011 | Confirmado, **com achado invertido**: recrutadores não são centrais |
| 14 | CASTAÑEDA, E.; JENKS, D. January 6th and de-democratization in the United States. *Social Sciences*, v. 12, n. 4, art. 238, 2023 | Confirmado como **asserção de uma frase**, não como demonstração |
| 15 | McADAM, D.; TARROW, S.; TILLY, C. *Dynamics of contention*. Cambridge: CUP, 2001 | Definições localizadas; **um registro do codebook não passa** |

**Ficha 11 — Collier (2011).** Tipo declarado na revista: *The Teacher*. A nota de fonte da tabela 1 diz que os quatro testes são "adapted from Bennett (2010, 210), who builds on categories formulated by Van Evera (1997, 31-32)". O projeto os atribui a **Beach e Pedersen (2019)** em `01_PROJETO-PESQUISA_v1-compacto.md`, §3.2. Collier adverte ainda que a distinção entre os quatro "should not be taken rigidly" — a mesma evidência pode sustentar um teste ou outro conforme o conhecimento prévio e a formulação da hipótese, **logo o teste nomeado exige a premissa declarada**. Sobre o teste de argola: estabelece critério **necessário**, elimina quem não passa e **não confirma quem passa**. A redação de PT-28 — "condição necessária (hoop test)" — está correta nesses termos.

**Ficha 12 — Mayntz (2004).** "Most authors agree that mechanism statements are causal generalizations about **recurrent** processes. In this sense, the term shall be used in this article." Mecanismos "são" sequências de eventos causalmente ligados "**that occur repeatedly in reality**". A posição oposta ela atribui a **Boudon (1998, p. 172)**, para quem mecanismos sociais "tend to be idiosyncratic and singular", e a recusa para uso próprio. **O codebook chama de mecanismo os elos de um episódio único: a citação que autoriza isso é Boudon, não Mayntz.** Em compensação, a última frase do resumo de Mayntz sustenta a camada estrutural do projeto — falta à literatura tratamento sistemático de mecanismos geradores em que instituições e configurações estruturais sejam decisivas. E ela nomeia o procedimento: **causal reconstruction**, que "seeks to explain a given social phenomenon — a given event, structure, or development — by identifying the processes through which it is generated".

**Ficha 13 — González-Bailón et al. (2011).** Áreas declaradas pela revista: física, física aplicada, física estatística. É ciência de redes, não sociologia de movimentos, e o dado é o Twitter espanhol de maio de 2011 — **rede aberta**, enquanto PT-06 descreve ecossistema fechado de Telegram e WhatsApp. O achado central é mais preciso do que a triagem supôs e em parte o inverte: **os participantes iniciais, isto é, os recrutadores, não têm posição topológica típica**; só os disseminadores de cascata são mais centrais. Casa com PT-19 ("coordenação sem comando centralizado visível") e qualifica PT-12A: "nós centralizadores" vale no nível da difusão, não do recrutamento.

**Ficha 14 — Castañeda & Jenks (2023).** O artigo não contém as palavras *diffusion* nem *emulation*. O Brasil aparece **uma vez**: o ataque ao congresso para contestar eleição "has now become a **contentious performance** that was used by the equivalent actors in Brazil on January 8, 2023", ambos com encorajamento de Steve Bannon. É literatura revisada por pares nomeando o 8 de Janeiro como a mesma *contentious performance* — termo de Tilly, cuja obra homônima está na camada A. **Mas é asserção de uma frase, sem evidência no próprio artigo.** Serve para mostrar que a leitura circula no campo; não estabelece a difusão, e PT-08 já registra que o precedente invocado pelos organizadores foi o Sri Lanka.

**Ficha 15 — *Dynamics of Contention*.** Desvio de paginação conferido pelo rodapé: física − 24 = impressa. **Certification**, p. 145: "the validation of actors, their performances, and their claims **by external authorities**". **Brokerage**, p. 26: "the linking of two or more previously unconnected social sites by a unit that mediates their relations". **Diffusion**, p. 333: "the transfer of information along established lines of interaction", com **attribution of similarity** como mecanismo companheiro e **scale shift** (p. 332) como o processo de dois caminhos, difusão/emulação e corretagem/coalizão. Contra a definição, PT-13, PT-06B e PT-50 passam; **PT-03 não** — "certificação de eficácia" não nomeia autoridade externa alguma, e o que valida ali é o desfecho. E o **limiar não vem desta obra**: *threshold* aparece três vezes, uma idiomática e duas na crítica — p. 307, "we have claimed that the threshold effect occurs rarely".

**Um sexto modo de falha: o depósito vazio.** O repositório da LSE registra Cammaerts (2012) como acesso verde, e o PDF depositado tem **uma página e 1.348 caracteres** — é a folha de capa, cujo texto termina aconselhando consultar o editor. O inverso também ocorre: Mayntz (2004), que o registro dava como sem arquivo, tem as 23 páginas no repositório do Max Planck. **Rota declarada não é texto disponível**, e a checagem é abrir e medir.

**Uma armadilha de extração, registrada porque quase produziu achado falso.** A busca por `certification` em *Dynamics of Contention* devolveu **zero páginas**. O PDF grava a ligadura **ﬁ** (U+FB01), e "certiﬁcation" não casa com "certification"; normalizada, são 42 páginas. **Ausência em busca de PDF não é ausência na obra.**

---

## 2. A bibliografia metodológica extraída

Organizada por função no desenho da pesquisa, não por ordem alfabética. Só entram itens verificados.

### 2.1 A lógica dos testes — o que falta explicitar no projeto

O projeto nomeia os quatro testes de Beach e Pedersen, mas não cita a literatura que discute **como** eles operam e o que autorizam concluir. Três itens fecham essa lacuna:

- **MAHONEY (2012)**, *The logic of process tracing tests in the social sciences*. Reconstrói a lógica dos quatro testes em termos de necessidade e suficiência da evidência para a hipótese. É a referência que sustenta a afirmação de que o teste aplicado determina a força da conclusão — hoje afirmada no projeto sem lastro bibliográfico.
- **ZAKS (2017)**, *Relationships among rivals (RAR)*. Propõe um enquadramento para tratar hipóteses concorrentes segundo a relação lógica entre elas — se são contraditórias, contrárias, independentes ou aninhadas. **É a peça que o projeto mais precisa e não tem.** A rubrica da disciplina cobra do estudante "uma hipótese rival formulada em sua melhor versão e enfrentada com evidência"; a seção 3 do projeto não diz como a própria pesquisa fará isso.
- **BENNETT; CHECKEL (2014)**, *Process tracing: from metaphor to analytic tool*. A coletânea de referência sobre boas práticas. Vale como âncora do padrão de qualidade que o projeto reivindica.

### 2.2 O que conta como mecanismo — e o problema da caixa-preta

- **MACHAMER; DARDEN; CRAVER (2000)**, *Thinking about mechanisms*. A definição de mecanismo como entidades e atividades organizadas de modo a produzir mudanças regulares. É a fonte filosófica de que a literatura de *process tracing* deriva a exigência de continuidade produtiva entre os elos.
- **WALDNER (2015)**, *Process tracing and qualitative causal inference*. Formula o critério de **completude do grafo causal**: uma cadeia só explica se não houver elo em que o analista precise supor o que não observou. É a crítica direta ao que o projeto chama de reconstruir sem explicar.
- **FALLETI; LYNCH (2009)**, *Context and causal mechanisms in political analysis* (`10.1177/0010414009331724`, confirmado). Mecanismos não operam no vácuo: o mesmo mecanismo produz desfechos diferentes em contextos diferentes. Sustenta metodologicamente o desenho em camadas — a camada estrutural é o contexto que condiciona a operação das demais.

### 2.3 A camada discursiva

- **McCAMMON (2013)**, verbete *Discursive opportunity structure*. Fixa o conceito e sua genealogia. Atenção: **há duas versões com DOIs distintos**, a de 2013 e a `.pub2`, de 27/09/2022 — escolher uma e declarar qual.
- **KOOPMANS (2005)**, *The missing link between structure and agency*. Do mesmo autor de Koopmans e Olzak (2004), articula estrutura e agência por seleção discursiva. Reforça o elo teórico que o projeto já usa.
- **CAMMAERTS (2012)**, *Protest logics and the mediation opportunity structure*. Desloca a oportunidade discursiva para o terreno da mediação — quem consegue ser noticiado, em que termos e sob qual designação. **É a referência que falta à disputa de nomeação da seção 2**, hoje apoiada apenas no relatório do Manchetômetro e em uma dissertação.
- **MOTTA, Renata (2015)**, *Transnational discursive opportunities*. Oportunidades discursivas que atravessam fronteiras. **É o suporte teórico do argumento do Sri Lanka**, hoje sustentado só pela fonte primária: se a difusão transmite cálculo de eficácia, ela opera num espaço discursivo transnacional, e há literatura que o nomeia.

### 2.4 Ameaça, e não só oportunidade

- **ALMEIDA (2003)**, *Opportunity organizations and threat-induced contention*. Mostra que ondas de protesto em contextos de fechamento são deflagradas por **ameaça**, não por abertura, e que organizações constituídas em ciclos anteriores são o que permite converter ameaça em ação. É a peça que melhor dialoga com a camada organizacional do projeto: os acampamentos não nasceram de uma abertura política, mas da derrota eleitoral — uma ameaça —, e se apoiaram em redes formadas no ciclo de 2013-2015.

### 2.5 Itens registrados, ainda não conferidos

Aparecem nas sínteses e interessam ao projeto, mas **não passaram por verificação** e por isso não devem ser citados ainda: Bennett, Charman e Fairfield (2022) sobre bayesianismo aplicado ao *process tracing*; Barrenechea e Mahoney (2019) sobre a versão conjuntista; Falleti e Mahoney (2015) sobre o método sequencial comparado; Mayntz (2004) sobre mecanismos e macrofenômenos; Bröer e Duyvendak (2009) sobre oportunidades discursivas e regras de sentimento; Ekman (2018) sobre mobilização de extrema-direita em mídias sociais.

> **Atualização de 29/09/2026 — existência conferida, ficha ainda não.** A varredura dos 411 DOIs (item 22 da agenda) e a triagem por pertinência (item 23) alcançaram estes itens. **Mayntz (2004)** e **Ekman (2018)** estão na camada A — e **Mayntz já tem ficha**, a nº 12 de 1.2 acima, lida na fonte em 30/09; Ekman continua sem, porque o editor barra o acesso; **Fairfield & Charman (2021)** e **Falleti & Mahoney** (o método sequencial comparado) em B; o **Barrenechea & Mahoney** conjuntista ficou em C, porque o desenho deste projeto não é conjuntista. **Bröer & Duyvendak não tinha DOI na síntese** — era citado por link do Scopus, como outras 20 entradas, e por isso esteve fora do universo verificado até ser procurado por título; está na camada A, em `10.17813/maiq.14.3.kx87723664558jm4`. **A frase acima continua valendo no essencial:** camada A não é ficha, e nenhum destes itens é citável antes da leitura na fonte.

---

## 3. Como o projeto dialoga com a produção recente

As sínteses trazem, cada uma, uma seção em que a própria literatura declara onde está travada. É aí que o projeto se posiciona melhor — não contra achados, mas contra lacunas que o campo reconhece ter.

### 3.1 Cinco lacunas declaradas pelo campo, e a resposta do projeto

**Primeira: padrões de reprodutibilidade em rastreamento documental.** A síntese de *process tracing* lista, entre as pesquisas ainda necessárias, "expandir o trabalho sobre análise de casos negativos, evidência ausente e padrões de reprodutibilidade para rastreamento arquivístico e por entrevistas". É uma lacuna de infraestrutura, não de teoria — e é exatamente o que o projeto já construiu antes de começar: 82 sub-eventos em 16 campos, 60 ancorados em fonte primária com página e transcrição literal, estatuto probatório classificado registro a registro, verificação automatizada a cada alteração e depósito previsto em repositório aberto com DOI. **Este é o ponto em que o projeto não acompanha o campo: ele o precede.** Vale dizê-lo assim na entrevista.

**Segunda: uso correto dos testes.** O campo pede que se estude "com que frequência os testes evidenciais clássicos são usados corretamente" na produção publicada. O projeto já faz disso um procedimento interno — os mecanismos hoje no banco são atribuições, não achados, e serão submetidos a teste nomeado elo a elo. Com Mahoney (2012) e Zaks (2017) no aparato, essa promessa deixa de ser afirmação de intenção e passa a ter critério declarado.

**Terceira: oportunidade como estrutura, percepção ou realização relacional.** A síntese de oportunidades registra que a controvérsia mais aguda do campo é se oportunidades são estruturas objetivas, percepções subjetivas ou algo produzido na própria interação. O projeto tem uma posição empírica sobre isso, e ela é forte: no 8 de janeiro a oportunidade discursiva é **verificável em documento** — a convocação codificada, os anúncios pagos, o precedente nomeado pelos organizadores. Não é uma percepção reconstruída em entrevista *a posteriori*; é registro. O caso permite testar a tese relacional com evidência que a maior parte da literatura não tem.

**Quarta: instrumentos que atravessem o híbrido on-line/off-line.** Tanto a síntese de oportunidades quanto a de estruturas de mobilização registram que falta instrumental unificado para arenas híbridas, e que não há métrica padronizada para comparar estruturas de mobilização. A camada organizacional do projeto faz precisamente essa junção numa só cadeia causal: convocação digital, financiamento por Pix, fretamento de ônibus, comboios, acampamento. Digital e material no mesmo grafo, não em capítulos separados.

**Quinta, acrescentada em 30/09/2026 — e é a única lida na fonte, não em síntese.** O verbete *Resource mobilization theory* da *Wiley-Blackwell Encyclopedia* (EDWARDS & GILLHAM, 2013), lido integralmente, encerra a seção de direções promissoras assim: "**Resource demobilization or reduction of resources to SMOs also needs further investigation, as it is currently assumed that the processes for mobilizing resources are reversed when SMOs fail.**"

**PT-52 é um caso dessa lacuna, e não do que ela supõe.** A desmobilização de recursos no 8 de Janeiro não foi o inverso da mobilização: foi **remoção coercitiva por autoridade estatal**, com data, decisão judicial e ordem de desocupação — "eliminada a base logística, o ciclo de rua se encerra materialmente, não por convencimento, mas por remoção da capacidade de agir". O campo, em 2013, dizia **presumir** que o processo se inverte quando a organização fracassa; o caso mostra um desfecho em que ele não se inverte, é interrompido de fora. É a contribuição mais nítida que o material oferece à teoria de mobilização de recursos, e a que menos depende de leitura adicional — o verbete está no corpus e a evidência de PT-52 está ancorada.

### 3.2 Onde o projeto tensiona com a produção

**Tensão 1 — contra a leitura da desinformação como causa autônoma.** A produção brasileira sobre o 8 de janeiro concentrada na comunicação trata a desinformação como motor. A síntese de oportunidades mostra que o campo internacional há tempos opera com a mediação como *estrutura de oportunidade*, e não como causa: Cammaerts (2012) trata a mídia como terreno em que a legitimidade da reivindicação é disputada. O projeto adota essa posição e, com ela, contraria a leitura dominante no debate nacional. O dado do Manchetômetro — "manifestante" superando "terrorista" e "golpista" no próprio dia 8 — é a evidência de que a designação era disputa em curso, não efeito de mensagem.

**Tensão 2 — contra a tese da irracionalidade.** A escolha do Sri Lanka como "Plano B", e não do Capitólio, mostra atores selecionando o precedente eficaz. Isso contraria frontalmente a literatura que trata esses agentes como crédulos capturados por narrativa. Com Renata Motta (2015), a difusão deixa de ser contágio e passa a ser transmissão de cálculo em espaço discursivo transnacional — que é uma afirmação sobre racionalidade estratégica, não sobre engano.

**Tensão 3 — contra a Mobilização de Recursos em sua formulação clássica.** McCarthy e Zald (1977) pressupõem organização formal. O caso não tem uma, e a resposta usual da literatura recente é dissolver o problema no conceito de ação conectiva. O projeto recusa as duas saídas: sustenta que houve **função organizacional sem organização**, com contabilidade, logística e nós de intermediação documentados. É uma extensão do modelo, e uma extensão é sempre uma tensão com a formulação original.

**Tensão 4 — contra o próprio par oportunidade/estrutura como suficiente.** Almeida (2003) mostra que ondas em contextos de fechamento respondem a **ameaça**, não a abertura. O 8 de janeiro é isso: a mobilização se ergue depois da derrota eleitoral. Incorporar Almeida obriga o projeto a admitir que "oportunidade" não descreve bem o gatilho — o que é uma tensão com o próprio referencial que ele adota, e vale mais declarada do que contornada.

### 3.3 A objeção que o projeto precisa enfrentar antes que o avaliador a faça

A síntese de *process tracing* nomeia, entre as vulnerabilidades recorrentes, a **seleção pela variável dependente**: estudos que escolhem o caso justamente por exibir o desfecho esperado. Este projeto faz isso. Estuda um evento de ruptura porque a ruptura ocorreu, e estuda um só.

A resposta existe e é padrão na literatura de caso único: a inferência não é entre casos, é **dentro** do caso — não se afirma que tais mecanismos produzem ruptura em geral, mas que estes elos, nesta sequência, sobreviveram a testes que poderiam tê-los derrubado. Waldner (2015) fornece o critério de completude que torna essa resposta verificável, e Zaks (2017) fornece o modo de tratar as explicações rivais que sobrevivem.

**Mas a resposta precisa estar escrita.** Hoje a seção 3 do projeto declara limites de fonte — o que a evidência não sustenta sobre anunciantes e valores — e não declara este limite de desenho, que é o que um avaliador metodologicamente atento perguntará primeiro. É a alteração de maior retorno por palavra gasta.

---

## 4. O que isso implicaria no texto do projeto

O projeto está em **2.495 palavras**, com teto de 2.500. Não há espaço livre: qualquer incorporação exige corte equivalente. Abaixo, a proposta mínima, com a aritmética.

### 4.1 Alteração recomendada — seção 3, item 2

Acrescentar, ao fim do item, o tratamento de hipóteses rivais e o limite de desenho (+58 palavras):

> Explicações rivais serão tratadas segundo a relação lógica que mantêm com a explicação proposta, na forma sistematizada por Zaks (2017), e cada elo será avaliado pelo critério de completude de Waldner (2015): não há explicação onde houver elo suposto e não observado. Declare-se desde já o limite de desenho: trata-se de caso único selecionado pelo desfecho, e a inferência pretendida é intracaso, não entre casos.

**Compensação sugerida (−60 palavras):** condensar o item 5 do mesmo capítulo, cuja lista de procedimentos de verificação repete o que o item 1 já estabelece.

### 4.2 Alterações opcionais, por ordem de retorno

| Onde | Acréscimo | Custo | Ganho |
|:--|:--|--:|:--|
| §2, camada discursiva | Cammaerts (2012) na disputa de nomeação | ~12 palavras | Ancora em teoria o que hoje se apoia só no Manchetômetro |
| §2, parágrafo do Sri Lanka | Motta, Renata (2015) | ~8 palavras | Converte a correção empírica em contribuição teórica |
| §3, item 2 | Mahoney (2012) junto a Beach e Pedersen | ~6 palavras | Sustenta a lógica dos testes |
| §2, camada organizacional | Almeida (2003) sobre contenção induzida por ameaça | ~20 palavras | Responde à objeção de que não houve abertura política |

### 4.3 O que **não** recomendo fazer agora

Incorporar as referências ainda não conferidas de 2.5; e citar qualquer item das sínteses sem passar pelas fichas de verificação. O ganho marginal não compensa o risco em um dossiê cuja credibilidade se apoia justamente no protocolo de verificação.

> ⚠️ **Nenhuma dessas alterações foi aplicada.** O projeto, o PDF e o DOCX permanecem como estavam. Se o dossiê já foi enviado, estas notas servem à entrevista de 09/09 e às versões futuras; se ainda não, a alteração de 4.1 é a única que eu faria sob pressão de prazo.

---

## 5. Encaminhamento para o item 11.3 das pendências

Restam **400 DOIs não conferidos** nas sete sínteses. Dada a taxa de divergência observada — 4 em 10 —, a conferência integral é trabalho de semanas, não de dias, e cabe na atividade de leitura integral prevista para o 1º semestre do cronograma. Sugiro a ordem: primeiro os itens que o projeto pretende citar; depois os da síntese de *process tracing* e da de oportunidades, que são as duas que sustentam o desenho; por último as demais.
