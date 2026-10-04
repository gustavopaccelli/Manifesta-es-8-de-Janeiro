# A camada T₋₁ conjuntural, codificada sobre literatura lida na fonte

**04/10/2026 — tarefa 14, em duas rodadas no mesmo dia.** Os sete registros contextuais do codebook (PT-01 a PT-06 e PT-08) sustentavam-se, desde agosto, numa lista de nomes: *"Literatura: Alonso (2017); Tatagiba (2014) — item contextual, sem fonte primária consultada"*. Nenhuma dessas obras estava no corpus e nenhuma havia sido lida.

A **primeira rodada** trocou a lista de nomes por ancoragem com página em três registros, declarou a lacuna em quatro, e terminou entregando seis pontos que exigiam juízo do pesquisador. A **segunda rodada** executa o primeiro e maior deles — a decisão entre descontinuidade e continuidade de 2013 para 2015-2016 — com três peças novas, e por causa delas um quarto registro deixa de ser contextual.

O relatório de pesquisa chamava esta camada de *"a parte mais fraca do aparato e a mais exposta a um parecerista"*. Ela deixa de ser a mais fraca em 2013-2018 e continua sendo em 2019-2022, agora com o motivo escrito.

Contextuais: **7 → 4 → 3**.

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

## 4. Os quatro que mudaram de classe

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

Os quatro passaram de **`Contextual`** a **`Confirmado`**. Não a `Confirmado em fonte primária`: artigo de revista e livro são fonte secundária para o evento, e o registro não reivindica mais do que tem.

**Duas afirmações de PT-02 continuam sem âncora, e estão declaradas no status.** *"Tolerância policial"* não aparece em nenhuma das sete obras. E o enquadramento midiático favorável está documentado para **2013** (Kunrath Silva, 2018, § 41-45; Pinto, 2017, rev. p. 130, nota 11), **não para 2015-2016** — transferir a âncora de um período para o outro seria a cifra correta no referente errado, pela décima segunda vez.

**Uma divergência de PT-03 ficou declarada em vez de resolvida.** O campo `framing_narrativa` guarda *"legalidade constitucional"*, que é o quadro do campo pró-impeachment — o que o registro deve codificar. A literatura lida adota a caracterização oposta: Tatagiba e Galvão escrevem *"2016, ano do golpe jurídico-parlamentar"* (rev. p. 65). O codebook registra o quadro do ator, não o veredito do analista.

---

## 5. Os três que continuam contextuais

**PT-05** (atrito institucional 2019-2022), **PT-06** (pandemia e ecossistema informacional) e **PT-08** (Capitólio) não mudaram de classe.

Varredura de conteúdo em 04/10/2026, nos **145 arquivos** da pasta anexada, com normalização NFKC: **zero ocorrências de `Bolsonaro`**, zero de `pandemia`, 2 arquivos com `negacion` e nenhum sobre o Brasil, 11 com `Capitol` e **todos anteriores a 2021**.

O que a segunda rodada mudou aqui é a **precisão da lacuna**, não o seu tamanho:

- **PT-05** ganhou a nota de que as peças novas cobrem a **genealogia** do atrito — Kunrath Silva (2023, rev. p. 86) nomeia o intervencionismo militar como um dos eixos em torno dos quais a extrema-direita se articula depois de 2013; Alonso (2023, p. 226 da edição digital) registra que a zona de conflito em torno da violência legítima se alça ao primeiro plano na votação do impeachment — **mas nenhuma cobre 2019-2022**. Falta a literatura que interpreta o período, não a documentação do atrito: essa PT-05A e PT-06A a PT-06C têm em fonte primária.
- **PT-06 é o mais caro dos três.** O mecanismo que afirma — consolidação do ecossistema informacional paralelo — é a junta que liga T₋₁ conjuntural a T₋₁ operacional, e é a que está sem leitura.
- **PT-08** segue com o evento contextual e o essencial confirmado em fonte primária: o precedente efetivamente invocado pelos organizadores como "Plano B" não foi o Capitólio, foi a revolta do Sri Lanka (CPMI, p. 614).

---

## 6. O que a leitura cobra do codebook — e é decisão sua

Dos seis pontos que a primeira rodada deixou, **dois foram resolvidos** nesta segunda e estão riscados abaixo. Os outros quatro continuam, mais dois novos. Nenhum foi executado; todos exigem juízo.

1. ~~**A descontinuidade de 2013 para 2015-2016 não é consensual, e o codebook adota um lado sem dizer.**~~ **RESOLVIDO em 04/10/2026:** você decidiu pela continuidade; PT-02 perdeu o "(spin-off)"; PT-01 e PT-02 nomeiam o campo patriota; a ressalva anti-determinista entrou no mecanismo. A divergência segue visível — Alonso e Mische (2016), citadas por Kunrath Silva (2018, nota 6), sustentam a leitura oposta.

2. ~~**"Apropriação de repertório" é nome que a fonte do conceito não detalha.**~~ **RESOLVIDO:** Kunrath Silva (2018, § 15) mostra que é mecanismo distinto da apropriação social de McAdam, Tarrow e Tilly. O nome estava certo; a cobrança estava errada. Ver §3.1.

3. **Os antipetistas já estavam na rua em 2011**, com *"a mesma estética e slogans que caracterizaram sua atuação nos anos de 2015 e 2016"* (Tatagiba e Galvão, rev. p. 82) — e, segundo Kunrath Silva (2023, rev. p. 77), organizados desde 2003. PT-02 continua datando o ator em 2015-2016. O `ator_grupo` passou a dizer que a origem é anterior ao ciclo, mas o campo `data_hora` não mudou: **redatar o registro é decisão sua.**

4. **O apelo à intervenção militar em março de 2015 pode virar registro próprio** (§2.3) — mesma forma do PT-18A da tarefa 23, e pela mesma razão: criar registro é juízo, não execução. A segunda rodada reforça o caso: Kunrath Silva (2023, rev. p. 86) põe o intervencionismo militar no mesmo arco.

5. **A tese de doutorado do pesquisador está no corpus e analisa exatamente estes ciclos.** `PROCEDENCIA` a declara, desde 19/08/2026, como antecedente teórico que *"NÃO é fonte de evento e não deve ancorar registro do codebook"*. A decisão foi respeitada nas duas rodadas. Vale reabri-la?

6. **Alonso (2017) continua citada no relatório de pesquisa e no projeto de pesquisa**, e segue não lida. O codebook já não a cita.

7. **NOVO — o mecanismo de PT-03 continua se chamando "certificação", e a definição não fecha.** *Dynamics of Contention* exige validação por **autoridade externa**; o que a literatura documenta é validação pela imprensa e pela opinião pública (Kunrath Silva, 2023, rev. p. 85). Há nome melhor na própria fonte — **ressignificação do protesto** —, e trocá-lo é tarefa 19.

8. **NOVO — o eixo 12 agora contém um livro de editora comercial.** `ALONSO 2023` entrou seguindo o precedente do eixo 05, que já traz dois livros de método. Se o repositório algum dia ganhar remoto público (tarefa 15), isso precisa ser decidido antes, não depois.

---

## 7. O que mudou no aparato

- **`Fontes/12_Camada-T-1_Literatura/`** — de quatro para **sete peças**. É o **primeiro caso no corpus de peça que é literatura secundária e ancora registro**: até aqui, quem ancorava era documento oficial, e teoria não ancorava nada. Por isso o eixo 12 está na lista `FORA_DA_DOCUMENTAL` de `verificar_integridade.py`, ao lado do eixo 05 — *a contagem documental não pode crescer porque entrou artigo de revista*. Corpus: **34 PDFs / 9.754 páginas**, dos quais **22 / 6.951 documentais**, inalterados. O corpus cresceu 363 páginas sem que um único documento oficial entrasse, e é exatamente isso que a separação das duas contagens serve para mostrar.
- **`scripts/recodificar_camada_t1.py`** e **`scripts/recodificar_camada_t1_arco.py`** — as duas rodadas, as duas com `--dry-run`.
- **`conferir_paginas.py`** ganhou **duas leituras adicionais da mesma página**, concatenadas para busca de substring. Não é troca de extrator, é acréscimo: o que casava antes continua casando, e as 63 âncoras anteriores seguem idênticas. Os motivos estão no docstring de `texto_pagina` e valem como armadilha registrada:
  - **PyPDF2 injeta espaço dentro das palavras** em alguns PDFs — "destaca -se", "empac amentos" — e por isso **nenhuma** das 26 âncoras novas casava, embora todas as frases estivessem nas páginas certas;
  - e o PDF da OpenEdition tem **camada de texto presente e errada**: a fonte `Gentium-Book-Basic` vem com CMap defeituoso, em que o código de cada glifo é o ASCII menos 29. É pior que a digitalização sem texto de Tatagiba (2014): lá a string vinha vazia e a ausência era visível; aqui a string vem cheia, e uma busca "prova" com alta confiança que o artigo não diz o que diz. O conserto é **por span**, nunca pela página, porque as outras fontes do mesmo arquivo saem corretas.
- **`conferir_hipoteses.py`** confere **dois** documentos; este entrou na checagem no dia em que nasceu, pela regra de 25/09.
- **`gerar_codebook.py`** declara a procedência das sete peças, cada uma com a sua armadilha de numeração, e passou a declarar também **de onde veio** cada peça — campo novo, porque as quatro primeiras vinham todas da mesma pasta e a origem estava fixa no código.

Classes de verificação: **61 em fonte primária · 18 confirmados · 3 contextuais · 0 a verificar · 1 inferência declarada.**
