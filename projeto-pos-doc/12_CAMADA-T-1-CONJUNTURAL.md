# A camada T₋₁ conjuntural, codificada sobre literatura lida na fonte

**04/10/2026 — tarefa 14, em três rodadas no mesmo dia.** Os sete registros contextuais do codebook (PT-01 a PT-06 e PT-08) sustentavam-se, desde agosto, numa lista de nomes: *"Literatura: Alonso (2017); Tatagiba (2014) — item contextual, sem fonte primária consultada"*. Nenhuma dessas obras estava no corpus e nenhuma havia sido lida.

A **primeira rodada** trocou a lista de nomes por ancoragem com página em três registros, declarou a lacuna em quatro, e terminou entregando seis pontos que exigiam juízo do pesquisador. A **segunda rodada** executa o primeiro e maior deles — a decisão entre descontinuidade e continuidade de 2013 para 2015-2016 — com três peças novas, e por causa delas um quarto registro deixa de ser contextual. A **terceira rodada** executa os oito encaminhamentos que o pesquisador devolveu: dois mecanismos mudam de nome, uma afirmação de dez anos sai do codebook porque a leitura a contradisse, um quinto registro deixa de ser contextual — e um sexto **não** deixa, por uma razão de critério que vale registrar.

O relatório de pesquisa chamava esta camada de *"a parte mais fraca do aparato e a mais exposta a um parecerista"*. Ela deixa de ser a mais fraca em 2013-2018 e continua sendo em 2019-2022, agora com o motivo escrito.

Contextuais: **7 → 4 → 3 → 2**.

---

## 1. O que foi lido

Sete peças, todas em `Fontes/12_Camada-T-1_Literatura/`. As quatro primeiras vêm da pasta de textos de ação coletiva anexada à sessão; as três últimas entraram na segunda rodada, de três origens distintas, declaradas peça por peça em `PROCEDENCIA`.

| Peça | Referência | Lida | Páginas que ancoram |
|:--|:--|:--|:--|
| **TATAGIBA 2014** | TATAGIBA, L. "1984, 1992 e 2013. Sobre ciclos de protestos e democracia no Brasil". *Política & Sociedade*, 13(28):35-62, 2014 | **Integral, por renderização** — é digitalização **sem camada de texto** | rev. 36, 38, 40, 47 |
| **TATAGIBA E GALVÃO 2019** | TATAGIBA, L.; GALVÃO, A. "Os protestos no Brasil em tempos de crise (2011-2016)". *Opinião Pública*, 25(1):63-96, 2019 | Método, séries, perfil de atores, conclusão | rev. 65, 69, 70, 71, 74, 82, 91 |
| **PINTO 2017** | PINTO, C. R. J. "A trajetória discursiva das manifestações de rua no Brasil (2013-2015)". *Lua Nova*, 100:119-153, 2017 | Os três momentos e a conclusão | rev. 128-131, 143-152 |
| **ALONSO 2012** | ALONSO, A. "Repertório, segundo Charles Tilly: história de um conceito". *Sociologia & Antropologia*, 2(3):21-41, 2012 | Formulações do conceito e apropriações posteriores | rev. 24, 29, 30, 34 |
| **KUNRATH SILVA 2018** | SILVA, M. K. "A apropriação conservadora do ciclo de protestos de 2013: rumo aos protestos anti-Dilma?". *Lusotopie*, 17(1):88-111, 2018 | **Integral** — teoria, fases, mecanismo, condições, conclusões | § 13, 14, 15, 41, 50, 54, 56, 58 |
| **KUNRATH SILVA 2023** | SILVA, M. K. "Ciclo de protestos de 2013: contribuições do campo de estudos de movimentos sociais e protesto para a análise de um objeto de disputa". *Desigualdade & Diversidade*, 23:57-90, 2023 | **Integral** | rev. 77, 79, 85, 86, 87 |
| **ALONSO 2023** | ALONSO, A. *Treze: a política de rua de Lula a Dilma*. São Paulo: Companhia das Letras, 2023 | "O espólio de junho", o epílogo que cobre o arco inteiro | PDF 219-227 |

**Três advertências de numeração, porque cada uma já custou caro a este projeto.**

A primeira: **a numeração da revista não coincide com a do PDF em nenhum dos cinco artigos**. O campo `fonte_pagina` guarda a **página do PDF**, que é a que `conferir_paginas.py` abre; a página da revista, citável, vai em `fonte_trecho`. Os deslocamentos estão declarados em `PROCEDENCIA` — 34, 62, 118, 20 e 56.

A segunda: **KUNRATH SILVA 2018 não tem paginação impressa**. A edição eletrônica da OpenEdition não reproduz as páginas 88-111 do impresso; a unidade citável é o **parágrafo (§)**, numerado pela própria OpenEdition. Não há deslocamento a declarar porque não há par de numerações a confundir — há uma que existe e outra que não está no arquivo.

A terceira, e é a mais escorregadia: **ALONSO 2023 também não tem paginação impressa**, mas por outro motivo — é edição digital, sem número de página de papel e sem rótulo de página no PDF. Citar "Alonso (2023, p. 224)" é citar a página **deste PDF**, e quem conferir no livro em papel não vai encontrar o mesmo número. Está declarado em `PROCEDENCIA` e repetido em cada `fonte_trecho` com a fórmula "da edição digital".

### 1.1 Duas peças a mais, e vêm do eixo 13

A terceira rodada leu duas peças que **não estão no eixo 12**: estavam entre as catorze que a tarefa 25 coletou no mesmo dia, declaradas como *coletadas, não lidas*, e o pesquisador mandou lê-las nesta ordem. Entraram no padrão do eixo 12 — offset declarado, transcrição conferida pelo ciclo —, mas continuam fisicamente em `Fontes/13_Bolsonarismo-mobilizacao/`, porque é de lá que vêm.

| Peça | Referência | Lida | Páginas que ancoram | Offset |
|:--|:--|:--|:--|:--|
| **ARAUJO E SALES 2022** | ARAUJO, R.; SALES, J. R. "Atuação política das Forças Armadas e o fenômeno bolsonarista no Brasil (2013-2022)". *Cadernos do Tempo Presente*, 13(1):26-42, 2022 | **Integral** | PDF 4, 5, 6, 8, 11 | impressa = PDF + 25, **derivado** |
| **FERNANDES E SILVA 2021** | FERNANDES, E. G.; SILVA, C. F. "Dinâmicas do controle à ação coletiva: o policiamento a protestos no Rio Grande do Sul". *Mediações*, 26(3):485-502, 2021 | **Integral** | PDF 2, 8, 10, 14 | impressa = PDF + 484, **lido** |

**Uma quarta advertência de numeração, e é de outra espécie.** Nos cinco artigos do eixo 12 o deslocamento foi **lido** num rótulo de página. Em `ARAUJO E SALES 2022` não há rótulo nenhum: nenhuma página do PDF imprime número. O deslocamento de 25 é **derivado** — o cabeçalho corrente de toda página traz o intervalo do artigo, *"p. 26-42"*, e o PDF tem exatamente 17 páginas, que é 42−26+1. A derivação é aritmética e verificável, mas é derivação, e está declarada como tal em `PROCEDENCIA`. Em `FERNANDES E SILVA 2021` o offset é lido: a p. 1 do PDF imprime *485*.

---

## 2. Primeira rodada: três achados, e o primeiro muda um registro

### 2.1 PT-01 atribuía ao ator o enquadramento do adversário

O campo `framing_narrativa` dizia: **"'Não é só por 20 centavos' — antipolítica"**. As obras lidas contradizem a atribuição por duas vias independentes.

Tatagiba sustenta o contrário em termos diretos: *"Portanto, desde o começo, foi sim uma luta por 0,20 centavos"* (2014, rev. p. 40). E, na mesma página, nega que tenha havido quadro unificador: *"não houve a conformação de um frame capaz de conferir unidade a essa diversidade para além do estopim: contra o aumento da tarifa do transporte público"*.

Pinto traz a palavra do próprio ator. A militante do MPL Nina Cappello: *"Interessava para vários setores dizer que a luta não era somente pelos R$ 0,20. [...] Para nós do movimento, era, sim, pelos R$ 0,20"* (2017, rev. p. 131).

**A leitura ampliada dos 20 centavos não era o quadro do MPL: era o quadro que terceiros lhe impuseram** — e o MPL identifica os terceiros nos dois flancos. E "antipolítica" muda de referente: em Pinto, o *"discurso antipolítico"* está *"claramente à direita no espectro político"* e aparece **depois da retirada do MPL das ruas** (rev. p. 131). O termo documentado para junho de 2013 é outro e é mais estreito: **antipartidarismo** (Tatagiba, 2014, rev. p. 47).

> **É a quarta variante do modo de falha do projeto.** Depois da cifra correta no referente errado (oito vezes), do termo técnico no referente errado (PT-03) e da frase própria com proveniência emprestada (PT-61), esta é **o enquadramento do adversário posto na boca do ator**. As três primeiras eram erros de proveniência; esta é de atribuição — e é pior, porque inverte quem disse o quê num registro cujo objeto é justamente a disputa pelo sentido.

A redação antiga está preservada em `nota_auditoria`.

### 2.2 A obra citada em dois registros nunca esteve no corpus

PT-01 e PT-02 citavam **"Alonso (2017)"**. Essa obra não está na pasta, não está no corpus e não foi lida. O que existe é **Alonso (2012)**, texto diferente — a história do conceito de repertório.

### 2.3 O apelo à intervenção militar está nas ruas em março de 2015

Pinto documenta, nas manifestações de 15 de março de 2015, faixas pedindo intervenção militar, algumas em inglês, e um movimento *"SOS Forças Armadas"* que, pouco expressivo em número, *"atualizava o espaço político das Forças Armadas"* (rev. p. 150). O codebook trata o apelo às Forças Armadas em **T₋₁ operacional**, em PT-12. A fonte o documenta **oito anos antes**, na mesma série de manifestações de que PT-02 trata. Está anotado em PT-02.

---

## 3. Segunda rodada: a descontinuidade sai do codebook

A primeira rodada deixou isto como decisão: *"o par PT-01 → PT-02, com mecanismo de spin-off, codifica ruptura. Se a leitura das autoras for adotada, o mecanismo vira difusão intraciclo."* **O pesquisador decidiu pela continuidade** e indicou a literatura. As três peças novas a sustentam, e uma delas nomeia o mecanismo.

### 3.1 O que foi apropriado foi um repertório — e isso corrige a primeira rodada

Kunrath Silva (2018) distingue sua tese das duas apropriações já existentes na literatura: a **apropriação social** de McAdam, Tarrow e Tilly (uso de organizações preexistentes) e a **apropriação institucional** de Tarrow (uso de recursos de instituições). E então:

> *"não há uma apropriação de recursos ou de estruturas organizativas, mas sim de um repertório: o protesto"* (§ 15)

Isto **vindica o nome que PT-02 já usava** e corrige o que a primeira rodada deste mesmo dia registrou como cobrança. Ela havia tomado a observação de Alonso (2012, rev. p. 24) — *"Tilly não detalha o processo de apropriação do repertório pelos atores"* — como defeito do codebook. Não era defeito: a apropriação de repertório é **mecanismo distinto** da apropriação social, e é exactamente por isso que a obra de Tilly não a detalha. O achado de Alonso continua verdadeiro; a conclusão que dele se tirou estava errada.

### 3.2 A oportunidade está invertida em relação ao cânone

No cânone, oportunidade vem de realinhamento, fragilidade ou conflito entre atores dominantes. Aqui, não:

> *"conflitos produzidos por movimentos sociais foram interpretados por atores de contramovimentos conservadores como oportunidades para sua mobilização"* (§ 14)

E a condição que tornou possível a convivência improvável foi um alvo comum: *"a crítica ao PT ofereceu um alvo comum a uma parcela significativa dos atores heterogêneos que compartilhavam as ruas"* (§ 50). A oportunidade, portanto, é **endógena ao ciclo** — o que é a formulação forte da continuidade. O campo `mecanismo_causal` de PT-01 continua dizendo "abertura de estrutura de oportunidade política", expressão do cânone; a divergência está declarada no `status_verificacao`, e o nome é da tarefa 19.

### 3.3 Continuidade não é determinação, e as duas fontes insistem nisso

Este é o ponto que **nenhum dos dois lados do debate anterior fazia**, e é o que mais obriga o codebook, porque o codebook é uma cadeia causal:

> *"é um equívoco afirmar que tais processos posteriores já estavam predeterminados pelo que ocorreu"* em 2013 (Kunrath Silva, 2018, § 56)

> *"junho não foi uma causa primeira, da qual decorreria inevitavelmente tudo o que veio depois"* (Alonso, 2023, p. 227 da edição digital)

Duas obras independentes, com teses diferentes sobre a forma do ciclo, convergem na mesma proibição. A ressalva entrou no próprio `mecanismo_causal` de PT-02 — não em nota de rodapé —, porque um campo que diz "continuidade" sem dizer isso afirma mais do que a fonte sustenta. E a convergência foi curta: *"observa-se uma clara demarcação e confrontação dos campos progressista e conservador"* (§ 58).

### 3.4 O ator estava lá em 2013, e o codebook não o registrava

O codebook punha a direita apenas em PT-02, a partir de 2015. Era essa ausência que fazia a leitura de ruptura parecer correta — se a direita só aparece em 2015, a passagem só pode ser entre ciclos.

Alonso dá o ator e o nome: o **campo patriota**, que em junho de 2013 esteve na rua e não foi reconhecido como ator político, e que, segundo ela, era *"o maior dos lados de 2013, tão grande quanto ignorado em junho"* (p. 223 da edição digital). Contra a tese da novidade: *"Vários de seus movimentos tinham surgido nos anos Lula ou antes"* (p. 224). Kunrath Silva data a organização: *"havia um intenso processo de organização e mobilização de forças sociais e políticas à direita do espectro político pelo menos desde a eleição de Lula em 2003"* (2023, rev. p. 77).

O campo `ator_grupo` de PT-01 e de PT-02 passou a nomear o campo patriota. **É a correção que faltava para que a continuidade seja legível no dado, e não só na prosa.**

### 3.5 PT-04 deixa de ser contextual — e a declaração da primeira rodada estava errada como conclusão geral

A primeira rodada escreveu que *"a literatura sobre o bolsonarismo não está no alcance deste projeto"*, com base em duas varreduras exaustivas: os 411 DOIs das sínteses e os 145 arquivos da pasta anexada. As duas varreduras estavam certas **sobre as duas coleções**. A conclusão geral estava errada, e bastou uma peça para mostrá-lo:

> o ciclo de 2013 funcionou como laboratório de enquadramentos, simbologias, táticas e estruturas de mobilização empregadas depois na campanha do impeachment e *"nas mobilizações de grupos políticos da extrema-direita crescentemente articulados em torno de Jair Bolsonaro e/ou do intervencionismo militar"* (Kunrath Silva, 2023, rev. p. 86)

E a genealogia do ator, em Alonso: *"A ocupação da presidência da República pela facção mais extrema do campo patriota resultou do longo e lento processo político de conflito nas ruas, mas também nas instituições"* (p. 227 da edição digital).

**A lição não é sobre o bolsonarismo: é sobre o que uma varredura prova.** Varredura exaustiva de duas coleções demonstra a lacuna **delas**, não a lacuna da literatura — e a diferença entre as duas afirmações é a diferença entre uma condição de pesquisa e um erro.

PT-04 passou a **`Confirmado`** quanto ao mecanismo e à genealogia do ator. O `status_verificacao` declara, nominalmente, o que **não** ancorou: o repertório digital da campanha de 2018, o enquadramento "nova política" / "anti-sistema" e a validação do resultado pelo TSE. O registro não reivindica o que não tem.

---

## 4. Terceira rodada: os oito encaminhamentos, executados

A segunda rodada terminou com oito pontos. O pesquisador respondeu os oito; **sete viraram mudança de campo e um virou entrega de arquivo**. O que segue é o que cada resposta produziu, e não a resposta em si.

### 4.1 A ordem de leitura foi dada, e importava

O encaminhamento 8 pediu Araujo e Sales primeiro, Fernandes e Silva depois. A ordem não é detalhe: a primeira peça datava o apelo de intervenção militar e a segunda dizia como o Estado reage a protesto. Lidas nessa ordem, a segunda responde a uma pergunta que a primeira formula. Lidas ao contrário, a conclusão sobre policiamento ficaria sem o ator a que se aplica.

### 4.2 O conflito que se resolveu em vez de ficar declarado

PT-02 afirmava, em `resposta_estatal`, **"Tolerância policial; enquadramento midiático favorável"**. A expressão estava no codebook desde a versão inicial de agosto e **nunca teve fonte**: a primeira rodada a procurou nas sete obras do eixo 12 e não achou; a segunda a deixou declarada como sem âncora.

A leitura não a confirmou. **Contradisse.** Fernandes e Silva analisam 45 anos de policiamento a protestos e encontram *"o uso prevalente de táticas de repressão física, pouco tolerantes à demonstração pública de demandas coletivas"* (rev. p. 492 — PDF p. 8). O que existe é **seletividade, não tolerância**: *"Os dados tendem a confirmar a seletividade da ação policial sobre os grupos mais contestadores à ordem social"* (rev. p. 494 — PDF p. 10), e *"as táticas da ação coletiva mais disruptivas tendem a ser mais duramente policiadas"* (rev. p. 498 — PDF p. 14).

O campo passou a dizer **policiamento seletivo pelo grau de contestação à ordem — não tolerância**, com o enquadramento midiático mantido e datado em 2013.

**Dois limites desta âncora ficam declarados, e são sérios.** A série é de **um estado** (Rio Grande do Sul) e **termina em 2015**: não cobre 2016 nem o período posterior. E há uma observação que não é evidência: os grupos de direita **não aparecem** entre os atores policiados da série, embora os autores nomeiem na introdução *"a mobilização de grupos de extrema direita favoráveis à intervenção militar"* como marcador recente (rev. p. 486 — PDF p. 2). Ausência numa série é ausência, **não tolerância medida**. Dizer o contrário seria repetir o modo de falha do projeto com sinal invertido.

### 4.3 O apelo à intervenção militar é frame, e isso fecha um ponto aberto desde a primeira rodada

A primeira rodada achou, em Pinto (2017, rev. p. 150), faixas pedindo intervenção militar já em março de 2015 e um movimento "SOS Forças Armadas" *"pouco expressivo em número"*. O achado ficou em `fonte_trecho` sem campo que o acolhesse, e a pergunta — vira registro próprio? — foi parar na lista de decisões.

O pesquisador decidiu: **é frame**, "uma forma de desejo dos grupos envolvidos", articulado "como forma de angariar mais manifestantes do campo da direita e extrema-direita que pensam ideologicamente como eles". Frame se codifica no evento que o articula, não em evento próprio — e por isso entrou em `framing_narrativa` de PT-02, não num PT novo.

Isso tem uma consequência que vale notar: **o frame já estava no codebook, em fonte primária, sete anos depois.** PT-12 codifica *"Intervenção militar"* e *"SOS Forças Armadas"* desde sempre, ancorados na CPMI. O que faltava era a **genealogia**, e ela entrou com página: *"Após junho de 2013, o pleito de uma intervenção militar constitucional foi bradada por setores conservadores da sociedade"* (Araujo e Sales, 2022, rev. p. 29 — PDF p. 4). O mesmo artigo registra o artigo 142 da Constituição *"desfraldado pelos ativistas favoráveis à intervenção militar"* nos atos de 2020-2021 (rev. p. 33 — PDF p. 8). **O apelo tem três momentos no codebook agora — 2015, 2020-2021 e 2022 —, e é o mesmo apelo.**

### 4.4 Dois mecanismos mudaram de nome, e os dois por motivo de definição

**PT-01.** O campo dizia *"Abertura de estrutura de oportunidade política e difusão de repertório de rua massivo, posteriormente apropriado pela direita"*. A segunda rodada mostrou que Kunrath Silva (2018, § 14) **inverte** essa estrutura para este caso — a oportunidade não vem de realinhamento de elites, vem do confronto produzido pelos movimentos progressistas, lido como oportunidade pelos contramovimentos —, e deixou a divergência declarada no status, remetendo o nome à tarefa 19.

O encaminhamento 2 fechou isso com uma formulação própria, que entrou no campo com as palavras do pesquisador: **"no ciclo de 2013 há uma janela de oportunidades políticas aberta na qual as direitas passariam a disputar e ocupar posteriormente"**. O campo passou a carregar também a zona de indefinição de Kunrath Silva (2023, rev. p. 79), que é o que dá conteúdo empírico à janela, e a proibição da leitura determinista, que antes só existia em PT-02.

**PT-03.** De *"Certificação de eficácia"* para **"Ressignificação do protesto"**, por encaminhamento 6, que pediu que a mudança fosse explicada em nota. A explicação está em `nota_auditoria` e é esta: certificação, em *Dynamics of Contention*, é validação por **autoridade externa**, e o enunciado do registro nunca nomeou autoridade alguma — cobrança aberta em 30/09/2026 (item 24.6 da agenda). A leitura da tarefa 14 não a resolveu, **agravou**: o que a literatura documenta é validação pela imprensa e pela opinião pública. "Ressignificação" diz o que a fonte sustenta — *"destaca-se a incorporação do protesto ao repertório de ação de forças sociais e políticas identificadas à direita do espectro ideológico"* (Kunrath Silva, 2023, rev. p. 85) — e não reivindica o que ela não mostra.

**Uma cobrança sai da tarefa 19.** Era a única nova que a tarefa 14 tinha acrescentado. As outras sete da seção 4 do documento 09 continuam lá.

### 4.5 A ressalva de datação virou nota redigida

O encaminhamento 5 pediu que a ressalva de datação de PT-02 fosse **redigida como nota**, para compor o artigo. Está em `nota_auditoria`, delimitada por `RESSALVA DE DATAÇÃO`, e diz o seguinte.

O registro data o **evento** em 2015-2016 e está correto: é nesse biênio que ocorrem as marchas verde-amarelas de massa, os panelaços e a convocação pelo MBL, Vem Pra Rua e Revoltados Online. O **ator**, porém, é anterior ao evento, e a literatura dá duas datas para isso — de mobilização, *"os grupos antipetistas já estão presentes em protestos organizados em 2011, mantendo a mesma estética e slogans"* (Tatagiba e Galvão, 2019, rev. p. 82); e de organização, *"havia um intenso processo de organização e mobilização de forças sociais e políticas à direita do espectro político pelo menos desde a eleição de Lula em 2003"* (Kunrath Silva, 2023, rev. p. 77).

O que 2015-2016 tem de próprio não é o surgimento do ator nem a invenção do repertório: é a **escala** — *"em 15 de março de 2015, apenas em São Paulo, apareceu coisa de 1 milhão, mobilizados por apenas um campo"* (Alonso, 2023, p. 224) — e a **convocação**, que passa a ser assumida por organizações identificadas.

**A consequência analítica é a razão de a nota existir:** datar o ator em 2015 produziria exatamente a leitura de ruptura que esta tarefa retirou do codebook. A data do evento e a data do ator são coisas distintas, e o registro passa a dizer as duas. **Redatar o `data_hora` continua sendo decisão sua** — a nota explica a diferença, não a resolve.

### 4.6 PT-05 sai de contextual. PT-06 não sai, e a recusa é o achado

**PT-05 passou a `Confirmado`.** Araujo e Sales documentam a cadeia causal que o registro afirma: *"diversos atos e motociatas ocorreram com o intuito de legitimar as hostilidades do mandatário em relação aos membros dos outros poderes constitucionais"* (rev. p. 33 — PDF p. 8), com a intervenção militar *"para moderar o conflito entre os poderes"* entre as principais consignas, as mobilizações *"instrumentalizadas por segmentos autoritários"* (rev. p. 31 — PDF p. 6) e a caserna assumindo *"um papel mais assertivo no diálogo com líderes políticos"* (rev. p. 30 — PDF p. 5).

**PT-06 recebeu página no mesmo movimento e continua contextual.** Araujo e Sales ancoram o repertório — os atos de sete de setembro e as motociatas — e o enquadramento — os pleitos da liberdade de expressão, a reivindicação do tratamento precoce e do kit Covid (rev. p. 33 — PDF p. 8). Mas o **mecanismo** que o registro afirma é a consolidação do ecossistema informacional paralelo, e esse segue sem leitura.

O critério não é novo: foi PT-04 que o fixou, na rodada anterior, e está escrito na nota dele — *"passou a Confirmado porque a cadeia causal que ele afirma está ancorada"*. Em PT-04 e PT-05 o que ganhou âncora foi a cadeia causal. Em PT-06 foram repertório e enquadramento. **Promover aqui seria trocar o critério no meio da aplicação**, que é a forma metodológica do modo de falha deste projeto: o dado correto no referente errado.

E há uma ironia que o registro declara: **a peça que fecharia PT-06 entrou no corpus hoje e não foi lida.** Von Bülow e Abers (2024) argumentam, com pesquisa, que o bolsonarismo precisa ser entendido como **movimento social** e não só como ideologia, e analisam o negacionismo pandêmico de março de 2020 a outubro de 2021 — o período exato de PT-06. É uma das quatro que o pesquisador entregou hoje.

### 4.7 As quatro obras barradas chegaram — e duas estavam mal atribuídas na minha própria lista

O encaminhamento 4 pediu os links das quatro peças que a coleta automatizada não alcançou. O pesquisador os usou e **entregou as quatro no mesmo dia**, o que confirma o achado de acesso do documento 13: *o bloqueio era do acesso automatizado, não da obra*. Entraram no eixo 13 como **coletadas, não lidas**.

**Abrir os arquivos corrigiu duas atribuições que eu vinha repetindo.**

| O que a lista dizia | O que o arquivo diz | Onde estava o erro |
|:--|:--|:--|
| Gohn **2020** | GOHN, M. G. "Ciclos de protestos no Brasil: 1970-2019". *mundosplurales*, 6(1):93-119, **2019** | O próprio DOI traz `.1.2019.`, e o rodapé registra *"Recibido: 3/4/2019 - Aceptado: 17/11/2019"* |
| Farias **e Casarões** 2022 | FARIAS, D. B. L.; CASARÕES, G.; **MAGALHÃES, D.** "Radical Right Populism and the Politics of Cruelty". *Global Studies Quarterly*, 2:1-13, 2022 | **Três autores.** David Magalhães (PUC-SP e FAAP) faltava |
| von Bülow e Abers **2022** | VON BÜLOW, M.; ABERS, R. N. "Denialism and Populism: Two Sides of a Coin in Jair Bolsonaro's Brazil". *Government and Opposition*, **59**:998-1016, **2024** | O slug do DOI é `gov.2022.14` e a publicação on-line é de 10/05/2022, **mas o fascículo é de 2024** |

A terceira linha é a mais instrutiva, e é uma armadilha de citação que vale guardar: **o ano do DOI não é o ano de publicação.** Um artigo publicado on-line em 2022 e paginado num fascículo de 2024 tem duas datas verdadeiras, e citar a do DOI produz uma referência que não localiza o texto na revista.

A quarta peça confirmou-se como esperado — Bastos e Recuero (2023), *"The Insurrectionist Playbook: Jair Bolsonaro and the National Congress of Brazil"*, *Social Media + Society*, p. 1-16 —, e é, entre as dezoito do eixo 13, **a mais próxima do objeto central desta pesquisa**.

### 4.8 A prova negativa achou um defeito meu e uma limitação do harness

**O defeito meu.** A primeira redação de PT-06 transcrevia *"A reivindicação do tratamento precoce e do "kit Covid""* — com **aspas aninhadas**, porque na fonte a expressão já vem aspada. `transcricoes()` fatia `fonte_trecho` em **todo** caractere de aspa e fica com os índices ímpares; a aspa interna inverte a paridade, o pedaço restante fica com 43 caracteres, abaixo do mínimo de 45, e **é descartado em silêncio**. O registro entraria no ciclo com uma transcrição conferida em vez de três, e a âncora do enquadramento sanitário não seria verificada por ninguém — um arquivo em `Fontes/` com página ao lado, parecendo lastro. Corrigido antes de gravar, com dois trechos da mesma página sem aspas internas.

> **A regra que isto deixa, e vale para todo o codebook: transcrição com aspa dentro de aspa não é conferida, e o silêncio do ciclo não distingue *conferida-e-OK* de *nunca-conferida*.**

**A limitação do harness.** Injetado o defeito de trocar a p. 8 pela p. 7 em `FERNANDES E SILVA 2021`, a conferência **continuou aprovando**. `casa()` desce a janelas de 40 caracteres, e *"antes a demonstracao publica de demandas"* aparece também na p. 14, que o registro lista — os autores repetem a própria fórmula na conclusão. **A âncora está certa**: a frase inteira só existe na p. 8, verificado por busca independente nas 17 páginas do PDF. Mas a prova negativa para essa peça é **inconclusiva**, e é a mesma limitação que o docstring de `conferir_paginas.py` já declara para PT-59. **Segunda ocorrência registrada.**

Os outros três defeitos foram pegos: página errada por um em PT-05 e em PT-04 (por `conferir_paginas.py`), e vínculo apontando para a peça errada do mesmo eixo em PT-06 (por `verificar_integridade.py`, que é de quem é o trabalho — na primeira tentativa eu havia jogado esse defeito no script errado e lido o resultado como aprovação). Codebook restaurado byte a byte nas quatro.

---

## 5. Os cinco que mudaram de classe

Cada linha declara o registro, o que a fonte sustenta e a âncora. **A coluna de páginas traz a página do PDF** — é a que o codebook ancora e a que `conferir_hipoteses.py` confere a cada rodada do ciclo.

| PT-01 | a repressão de 13/06 em São Paulo nacionaliza o ciclo, e os protestos produzem a redução das tarifas | TATAGIBA 2014: 2, 6 |
| PT-01 | a leitura ampliada dos 20 centavos é atribuída a terceiros pelo próprio MPL | PINTO 2017: 13 |
| PT-01 | junho de 2013 como oportunidade para os setores oposicionistas à esquerda e à direita; o MPL como quem deflagrou as Jornadas | TATAGIBA E GALVAO 2019: 10, 12 |
| PT-01 | a zona de indefinição sobre quem promovia os protestos, que é a condição da apropriação; a direita organizada desde 2003 | KUNRATH SILVA 2023: 21, 23 |
| PT-01 | quem leu a abertura como oportunidade; o que foi apropriado; a virada do enquadramento midiático dentro de 2013; o alvo comum | KUNRATH SILVA 2018: 6, 11, 13 |
| PT-01 | junho como mosaico: os campos lado a lado, sem serem aliados | ALONSO 2023: 220 |
| PT-02 | a vaia de 12/06/2014 como momento inaugural do discurso conservador antipetista | PINTO 2017: 25 |
| PT-02 | o deslocamento de antipartidarismo (2013) para anti-PT (2015); as faixas por intervenção militar e o "SOS Forças Armadas" | PINTO 2017: 31, 32 |
| PT-02 | MBL, Vem Pra Rua e Revoltados Online como convocantes — e já presentes em 2011 | TATAGIBA E GALVAO 2019: 20 |
| PT-02 | a modularidade como o que facilita a transposição do repertório | ALONSO 2012: 4, 10 |
| PT-02 | o mecanismo nomeado na fonte; o desenho do processo; e a proibição da leitura determinista | KUNRATH SILVA 2018: 6, 14, 15 |
| PT-02 | ciclos contínuos de protesto desde 2013, sem estabilização política entre eles | KUNRATH SILVA 2023: 30 |
| PT-02 | o campo patriota incha; o ciclo de 2015 como ciclo de um só campo; e a origem anterior aos anos Lula | ALONSO 2023: 219, 223, 224 |
| PT-03 | a data — 31/08/2016, afastamento definitivo pelo Senado — e a cadeia que liga o pico de 2013 ao impeachment | TATAGIBA E GALVAO 2019: 3, 7, 29 |
| PT-03 | a incorporação do protesto ao repertório da direita, que é a evidência mais próxima da certificação que o registro nomeia | KUNRATH SILVA 2023: 29 |
| PT-03 | o processo aberto na Câmara como resposta ao clamor da rua; a rua partida ao meio em 2016 | ALONSO 2023: 225, 226 |
| PT-04 | o ciclo de 2013 como laboratório do que se emprega depois nas mobilizações em torno de Bolsonaro e do intervencionismo militar | KUNRATH SILVA 2023: 30 |
| PT-04 | a presidência ocupada pela facção mais extrema do campo patriota como desfecho não planejado de um processo longo | ALONSO 2023: 227 |
| PT-04 | o bolsonarismo como a expressão política antissistêmica derivada da crise de legitimidade da Nova República após junho de 2013; e a atomização das direitas superada "em parte" depois de 2013 | ARAUJO E SALES 2022: 11 |
| PT-02 | a genealogia do apelo de intervenção militar: bradado por setores conservadores já depois de junho de 2013 | ARAUJO E SALES 2022: 4 |
| PT-02 | predomínio de repressão física; seletividade pelo grau de contestação à ordem; táticas disruptivas mais duramente policiadas; a extrema direita pró-intervenção nomeada na introdução | FERNANDES E SILVA 2021: 2, 8, 10, 14 |
| PT-05 | atos e motociatas para legitimar as hostilidades aos outros poderes; o artigo 142 desfraldado; as mobilizações instrumentalizadas por segmentos autoritários; a caserna mais assertiva | ARAUJO E SALES 2022: 5, 6, 8 |

Os cinco passaram de **`Contextual`** a **`Confirmado`**. Não a `Confirmado em fonte primária`: artigo de revista e livro são fonte secundária para o evento, e o registro não reivindica mais do que tem.

**Das duas afirmações de PT-02 que não tinham âncora, uma saiu do campo e a outra continua declarada.** *"Tolerância policial"* **saiu**: a terceira rodada não a achou, achou o contrário, e o campo passou a dizer seletividade (ver §4.2). O enquadramento midiático favorável continua documentado para **2013** (Kunrath Silva, 2018, § 41-45; Pinto, 2017, rev. p. 130, nota 11), **não para 2015-2016** — transferir a âncora de um período para o outro seria a cifra correta no referente errado, pela décima segunda vez.

**Uma divergência de PT-03 ficou declarada em vez de resolvida.** O campo `framing_narrativa` guarda *"legalidade constitucional"*, que é o quadro do campo pró-impeachment — o que o registro deve codificar. A literatura lida adota a caracterização oposta: Tatagiba e Galvão escrevem *"2016, ano do golpe jurídico-parlamentar"* (rev. p. 65). O codebook registra o quadro do ator, não o veredito do analista.

---

## 6. Os dois que continuam contextuais

**PT-06** (pandemia e ecossistema informacional) e **PT-08** (Capitólio) não mudaram de classe. **PT-05 saiu desta lista na terceira rodada** — ver §4.6.

Varredura de conteúdo em 04/10/2026, nos **145 arquivos** da pasta anexada, com normalização NFKC: **zero ocorrências de `Bolsonaro`**, zero de `pandemia`, 2 arquivos com `negacion` e nenhum sobre o Brasil, 11 com `Capitol` e **todos anteriores a 2021**.

**E a varredura continua valendo apenas para o que mediu.** A lição da segunda rodada vale aqui também: varredura exaustiva de duas coleções prova a lacuna **delas**, não a lacuna da literatura. Foi uma peça de fora das duas coleções que tirou PT-04 de contextual, e foi uma peça da coleta da tarefa 25 que tirou PT-05.

O que a terceira rodada mudou aqui é o **tamanho** da lacuna, não só a precisão:

- **PT-06 é agora o mais caro dos dois, e por um motivo preciso.** Repertório e enquadramento ganharam página (Araujo e Sales, 2022, rev. p. 33). O mecanismo que o registro afirma — consolidação do ecossistema informacional paralelo — é a junta que liga T₋₁ conjuntural a T₋₁ operacional, e é a que segue sem leitura. **A peça que o fecharia está no corpus desde 04/10/2026 e não foi lida**: von Bülow e Abers (2024) cobrem março de 2020 a outubro de 2021 e sustentam que o bolsonarismo é movimento social, não só ideologia. Cesarino (2022), que o registro citava desde agosto sem ter, também entrou e também não foi lida.
- **PT-08** segue com o evento contextual e o essencial confirmado em fonte primária: o precedente efetivamente invocado pelos organizadores como "Plano B" não foi o Capitólio, foi a revolta do Sri Lanka (CPMI, p. 614).

---

## 7. O que a leitura cobra do codebook — e é decisão sua

Dos oito pontos que as duas primeiras rodadas deixaram, **cinco estão resolvidos** e riscados abaixo — dois pela segunda rodada, três pela terceira. **Três continuam, e um deles é novo.** Nenhum dos três foi executado; todos exigem juízo.

1. ~~**A descontinuidade de 2013 para 2015-2016 não é consensual, e o codebook adota um lado sem dizer.**~~ **RESOLVIDO em 04/10/2026:** você decidiu pela continuidade; PT-02 perdeu o "(spin-off)"; PT-01 e PT-02 nomeiam o campo patriota; a ressalva anti-determinista entrou no mecanismo. A divergência segue visível — Alonso e Mische (2016), citadas por Kunrath Silva (2018, nota 6), sustentam a leitura oposta.

2. ~~**"Apropriação de repertório" é nome que a fonte do conceito não detalha.**~~ **RESOLVIDO:** Kunrath Silva (2018, § 15) mostra que é mecanismo distinto da apropriação social de McAdam, Tarrow e Tilly. O nome estava certo; a cobrança estava errada. Ver §3.1.

3. **Os antipetistas já estavam na rua em 2011**, com *"a mesma estética e slogans que caracterizaram sua atuação nos anos de 2015 e 2016"* (Tatagiba e Galvão, rev. p. 82) — e, segundo Kunrath Silva (2023, rev. p. 77), organizados desde 2003. **A ressalva está redigida como nota em PT-02 desde a terceira rodada** (§4.5), por seu encaminhamento, e explica a diferença entre a data do evento e a data do ator. Mas **o campo `data_hora` continua em 2015-2016**: a nota explica a diferença, não a resolve. **Redatar o registro é decisão sua** — e é a única das três pendências antigas que a terceira rodada não fechou.

4. ~~**O apelo à intervenção militar em março de 2015 pode virar registro próprio**~~ **RESOLVIDO em 04/10/2026:** você decidiu que é **frame**, não registro — articulado para angariar manifestantes do próprio campo. Entrou em `framing_narrativa` de PT-02; a genealogia entrou em PT-12 com página. Ver §4.3.

5. **A tese de doutorado do pesquisador está no corpus e analisa exatamente estes ciclos.** `PROCEDENCIA` a declara, desde 19/08/2026, como antecedente teórico que *"NÃO é fonte de evento e não deve ancorar registro do codebook"*. A decisão foi respeitada nas duas rodadas. Vale reabri-la?

6. **Alonso (2017) continua citada no relatório de pesquisa e no projeto de pesquisa**, e segue não lida. O codebook já não a cita.

7. ~~**O mecanismo de PT-03 continua se chamando "certificação", e a definição não fecha.**~~ **RESOLVIDO em 04/10/2026:** você atribuiu **ressignificação do protesto**, e a mudança está explicada em nota no próprio registro. Ver §4.4. Esta cobrança **sai da tarefa 19**; as outras sete da seção 4 do documento 09 continuam lá.

8. **O eixo 12 agora contém um livro de editora comercial.** `ALONSO 2023` entrou seguindo o precedente do eixo 05, que já traz dois livros de método. Se o repositório algum dia ganhar remoto público (tarefa 15), isso precisa ser decidido antes, não depois. **A terceira rodada agravou o ponto**: as quatro peças que você entregou incluem três de editoras comerciais — Cambridge, SAGE e Oxford —, duas delas com licença Creative Commons declarada na própria peça e uma sem declaração visível no PDF.

9. **NOVO — PT-06 ficou contextual por escolha de critério, e o critério é reversível.** Repertório e enquadramento têm página; o mecanismo não. Mantive `Contextual` porque foi a cadeia causal que promoveu PT-04 e PT-05, e trocar o critério no meio da aplicação é o modo de falha deste projeto em forma metodológica. **Se você decidir que `Confirmado` admite registro com repertório e enquadramento ancorados e mecanismo declarado em aberto, PT-06 muda em um comando — mas o critério muda para todos, e PT-08 precisa ser reexaminado junto.** Ver §4.6.

---

## 8. O que mudou no aparato

- **`Fontes/12_Camada-T-1_Literatura/`** — de quatro para **sete peças**. É o **primeiro caso no corpus de peça que é literatura secundária e ancora registro**: até aqui, quem ancorava era documento oficial, e teoria não ancorava nada. Por isso o eixo 12 está na lista `FORA_DA_DOCUMENTAL` de `verificar_integridade.py`, ao lado do eixo 05 — *a contagem documental não pode crescer porque entrou artigo de revista*. Corpus: **34 PDFs / 9.754 páginas**, dos quais **22 / 6.951 documentais**, inalterados. O corpus cresceu 363 páginas sem que um único documento oficial entrasse, e é exatamente isso que a separação das duas contagens serve para mostrar.
- **`scripts/recodificar_camada_t1.py`**, **`scripts/recodificar_camada_t1_arco.py`** e **`scripts/recodificar_camada_t1_frames.py`** — as três rodadas, as três com `--dry-run`.
- **`conferir_paginas.py`** ganhou **duas leituras adicionais da mesma página**, concatenadas para busca de substring. Não é troca de extrator, é acréscimo: o que casava antes continua casando, e as 63 âncoras anteriores seguem idênticas. Os motivos estão no docstring de `texto_pagina` e valem como armadilha registrada:
  - **PyPDF2 injeta espaço dentro das palavras** em alguns PDFs — "destaca -se", "empac amentos" — e por isso **nenhuma** das 26 âncoras novas casava, embora todas as frases estivessem nas páginas certas;
  - e o PDF da OpenEdition tem **camada de texto presente e errada**: a fonte `Gentium-Book-Basic` vem com CMap defeituoso, em que o código de cada glifo é o ASCII menos 29. É pior que a digitalização sem texto de Tatagiba (2014): lá a string vinha vazia e a ausência era visível; aqui a string vem cheia, e uma busca "prova" com alta confiança que o artigo não diz o que diz. O conserto é **por span**, nunca pela página, porque as outras fontes do mesmo arquivo saem corretas.
- **`conferir_hipoteses.py`** confere **dois** documentos; este entrou na checagem no dia em que nasceu, pela regra de 25/09.
- **`gerar_codebook.py`** declara a procedência das sete peças, cada uma com a sua armadilha de numeração, e passou a declarar também **de onde veio** cada peça — campo novo, porque as quatro primeiras vinham todas da mesma pasta e a origem estava fixa no código.

- **Terceira rodada, 04/10/2026.** O eixo 12 não cresceu: as duas peças lidas são do eixo 13 (§1.1). O corpus foi a **52 PDFs / 10.207 páginas** porque você entregou as quatro peças barradas; a contagem documental continua em **22 / 6.951**. Em três rodadas do mesmo dia o corpus cresceu **816 páginas sem que um único documento oficial entrasse** — e a linha de base de `verificar_integridade.py` foi atualizada junto, como a regra manda.
- **`gerar_codebook.py`** reescreveu o eixo 13 em **três blocos de procedência**, porque as dezoito peças já não têm a mesma origem: doze coletadas e não lidas, duas lidas que ancoram registro, quatro entregues pelo pesquisador e não lidas. A distinção não é burocrática — é o que impede que um arquivo em `Fontes/` seja tomado por lastro.

Classes de verificação: **61 em fonte primária · 19 confirmados · 2 contextuais · 0 a verificar · 1 inferência declarada.**
