# A camada T₋₁ conjuntural, codificada sobre literatura lida na fonte

**04/10/2026 — tarefa 14.** Os sete registros contextuais do codebook (PT-01 a PT-06 e PT-08) sustentavam-se, desde agosto, numa lista de nomes: *"Literatura: Alonso (2017); Tatagiba (2014) — item contextual, sem fonte primária consultada"*. Nenhuma dessas obras estava no corpus e nenhuma havia sido lida. Esta rodada troca a lista de nomes por ancoragem com página onde a leitura existe — **três registros** — e declara a lacuna, datada e reproduzível, onde ela não existe — **quatro**.

O relatório de pesquisa chamava esta camada de *"a parte mais fraca do aparato e a mais exposta a um parecerista"*. Ela deixa de ser a mais fraca em 2013–2016 e continua sendo em 2018–2022, agora com o motivo escrito.

---

## 1. O que foi lido, e o que isso custou

As quatro peças vêm da pasta de textos de ação coletiva anexada à sessão, e entraram em `Fontes/12_Camada-T-1_Literatura/`. Todas são **artigos revisados por pares**, o que as distingue das sete sínteses LeapSpace: aqui a citação é legítima.

| Peça | Referência | Lida | Páginas que ancoram |
|:--|:--|:--|:--|
| **TATAGIBA 2014** | TATAGIBA, L. "1984, 1992 e 2013. Sobre ciclos de protestos e democracia no Brasil". *Política & Sociedade*, 13(28):35-62, 2014 | **Integral, por renderização** — é digitalização **sem camada de texto** | rev. 36, 38, 40, 47 |
| **TATAGIBA E GALVÃO 2019** | TATAGIBA, L.; GALVÃO, A. "Os protestos no Brasil em tempos de crise (2011-2016)". *Opinião Pública*, 25(1):63-96, 2019 | Seções de método, séries, perfil de atores e conclusão | rev. 65, 69, 70, 71, 74, 82, 91 |
| **PINTO 2017** | PINTO, C. R. J. "A trajetória discursiva das manifestações de rua no Brasil (2013-2015)". *Lua Nova*, 100:119-153, 2017 | Os três momentos e a conclusão | rev. 128-131, 143-152 |
| **ALONSO 2012** | ALONSO, A. "Repertório, segundo Charles Tilly: história de um conceito". *Sociologia & Antropologia*, 2(3):21-41, 2012 | Formulações do conceito e apropriações posteriores | rev. 24, 29, 30, 34 |

**Duas advertências de método, porque as duas já custaram caro a este projeto.**

A primeira: **a numeração da revista não coincide com a do PDF em nenhuma das quatro**. O campo `fonte_pagina` guarda a **página do PDF**, que é a que `conferir_paginas.py` abre; a página da revista, citável, vai em `fonte_trecho` e nas tabelas abaixo. Os deslocamentos estão declarados em `PROCEDENCIA`, peça por peça. Confundir as duas produziria exatamente a cifra correta no referente errado.

A segunda: **Tatagiba (2014) não tem camada de texto.** `PyPDF2` devolve string vazia nas 28 páginas. Foi lida por renderização a 170 dpi — a mesma técnica com que o projeto leu os dois gráficos vetoriais do balanço do STF em 16/08/2026 — e as duas transcrições que dela entram no codebook estão registradas em `EXCECOES`, no alto de `conferir_paginas.py`, com o motivo. **Ausência de texto extraível não é ausência de conteúdo**, e é a mesma lição da ligadura *ﬁ*.

---

## 2. Três achados, e o primeiro muda um registro

### 2.1 PT-01 atribuía ao ator o enquadramento do adversário

O campo `framing_narrativa` de PT-01 dizia: **"'Não é só por 20 centavos' — antipolítica"**. As duas obras lidas contradizem a atribuição, e por duas vias independentes.

Tatagiba sustenta o contrário em termos diretos: *"Portanto, desde o começo, foi sim uma luta por 0,20 centavos"* (2014, rev. p. 40). E, na mesma página, nega que tenha havido quadro unificador: *"não houve a conformação de um frame capaz de conferir unidade a essa diversidade para além do estopim: contra o aumento da tarifa do transporte público"*.

Pinto traz a palavra do próprio ator. A militante do MPL Nina Cappello: *"Interessava tanto à direita quanto à esquerda dar um golpe na nossa pauta. [...] Interessava para vários setores dizer que a luta não era somente pelos R$ 0,20. [...] Para nós do movimento, era, sim, pelos R$ 0,20"* (2017, rev. p. 131).

**A leitura ampliada dos 20 centavos não era o quadro do MPL: era o quadro que terceiros lhe impuseram** — e o MPL identifica os terceiros nos dois flancos. A frase que circulou, e que Tatagiba localiza num cartaz compartilhado em 14/06/2013, é *"E você ainda acha que é por 20 centavos?"* (2014, rev. p. 43), citando Judensnaider et al.

E "antipolítica" muda de referente. Em Pinto, o *"discurso antipolítico"* que emerge *"investindo contra as bandeiras de partido"* está *"claramente à direita no espectro político"* e aparece **depois da retirada do MPL das ruas** (rev. p. 131). O termo documentado para junho de 2013 é outro e é mais estreito: **antipartidarismo** — *"cresceu de forma inédita o nível de hostilidade em relação à presença dos partidos e dos militantes partidários nos protestos"* (Tatagiba, 2014, rev. p. 47), com o episódio de 21/06 em que bandeiras partidárias foram arrancadas e queimadas (rev. p. 49).

> **É a quarta variante do modo de falha do projeto.** Depois da cifra correta no referente errado (oito vezes), do termo técnico no referente errado (PT-03) e da frase própria com proveniência emprestada (PT-61), esta é **o enquadramento do adversário posto na boca do ator**. As três primeiras eram erros de proveniência; esta é um erro de atribuição — e é pior, porque inverte quem disse o quê num registro cujo objeto é justamente a disputa pelo sentido.

O campo foi reescrito para dizer o que as fontes sustentam, incluindo a ausência de quadro unificador. A redação antiga está preservada em `nota_auditoria`.

### 2.2 A obra citada em dois registros nunca esteve no corpus

PT-01 e PT-02 citavam **"Alonso (2017)"**. Essa obra não está na pasta, não está no corpus e não foi lida. O que existe é **Alonso (2012)**, texto diferente — a história do conceito de repertório —, e ele cobra do codebook algo que o codebook não resolveu:

> *"Tilly não detalha o processo de apropriação do repertório pelos atores."* (rev. p. 24)

PT-02 nomeia seu mecanismo **"apropriação de repertório (spin-off)"**. Na fonte do conceito, segundo sua historiadora, o processo de apropriação **não está detalhado**. O que Alonso detalha é outra coisa, e é o que de fato sustenta a passagem de PT-01 a PT-02: a **modularidade**. *"Decantam as performances modulares [...], que podem servir a muitos atores, assuntos, situações [...]. A modularidade facilita a transposição"* (rev. p. 30); e cada transposição *"sofreria processos de negociação e adaptação"*, de modo que as performances têm *"duas faces. 'Modulares' [...] Mas cada qual é singularizada pelo uso"* (rev. p. 29).

Nada disso foi aplicado ao campo `mecanismo_causal`: **o nome é decisão da tarefa 19**, e este documento só entrega a evidência.

### 2.3 O apelo à intervenção militar está nas ruas em março de 2015

Pinto documenta, nas manifestações de 15 de março de 2015:

> *"Havia também, nas manifestações, faixas pedindo intervenção militar; elas eram de duas naturezas: faixas de indivíduos ou pequenos grupos, algumas inclusive em inglês: 'we want military intervention now', e faixas produzidas profissionalmente por um movimento chamado 'SOS Forças Armadas', que, numericamente, era pouco expressivo, mas que **atualizava o espaço político das Forças Armadas**."* (rev. p. 150)

O codebook trata o apelo às Forças Armadas em **T₋₁ operacional** — PT-12, os acampamentos, onde elas são "destinatária do apelo" — e no campo multiorganizacional ele aparece como traço de 2022-2023. A fonte o documenta **oito anos antes**, na mesma série de manifestações de que PT-02 trata, e com a observação de que o movimento era numericamente pequeno mas politicamente atualizador.

Isso é continuidade citável entre T₋₁ conjuntural e T₋₁ operacional, e o codebook não a registra. **Está anotado em PT-02**; se merece registro próprio, é decisão sua — a mesma forma do PT-18A da tarefa 23, e pela mesma razão: criar registro é juízo, não execução.

---

## 3. Os três que mudaram de classe

Cada linha abaixo declara o registro, o que a fonte sustenta e a âncora. **A coluna de páginas traz a página do PDF**, que é a que o codebook ancora e a que `conferir_hipoteses.py` confere; a página da revista está no texto acima.

| PT-01 | a repressão de 13/06 em São Paulo nacionaliza o ciclo, e os protestos produzem a redução das tarifas — a sequência que o campo `resposta_estatal` afirma | TATAGIBA 2014: 2, 6 |
| PT-01 | a leitura ampliada dos 20 centavos é atribuída a terceiros pelo próprio MPL | PINTO 2017: 13 |
| PT-01 | junho de 2013 como "extraordinária oportunidade para os setores oposicionistas, à esquerda e à direita"; o MPL como quem deflagrou as Jornadas | TATAGIBA E GALVAO 2019: 10, 12 |
| PT-02 | a vaia de 12/06/2014 como momento inaugural do discurso conservador antipetista | PINTO 2017: 25 |
| PT-02 | o deslocamento de antipartidarismo (2013) para anti-PT (2015); as faixas por intervenção militar e o "SOS Forças Armadas" | PINTO 2017: 31, 32 |
| PT-02 | MBL, Vem Pra Rua e Revoltados Online como convocantes, com forte uso de redes sociais — e já presentes em 2011 | TATAGIBA E GALVAO 2019: 20 |
| PT-02 | "Tilly não detalha o processo de apropriação do repertório pelos atores"; a modularidade como o que facilita a transposição | ALONSO 2012: 4, 10 |
| PT-03 | a data — 31/08/2016, afastamento definitivo pelo Senado — e a cadeia que liga o pico de 2013 ao impeachment | TATAGIBA E GALVAO 2019: 3, 7, 29 |

Os três passaram de **`Contextual`** a **`Confirmado`**. Não a `Confirmado em fonte primária`: artigo de revista é fonte secundária para o evento, e o registro não reivindica mais do que tem.

**Uma afirmação de PT-02 continua sem âncora** e está declarada no status: *"tolerância policial"*. Nenhuma das quatro obras a sustenta. O outro termo do mesmo campo, o enquadramento midiático favorável, está em Pinto (rev. p. 130, nota 11), que descreve a Rede Globo *"em campanha declarada a favor das manifestações"* e a divisão editorial entre "vândalos" e "cidadãos de bem".

**Uma divergência de PT-03 ficou declarada em vez de resolvida.** O campo `framing_narrativa` guarda *"legalidade constitucional"*, que é o quadro do campo pró-impeachment — o que o registro deve codificar. A literatura lida adota a caracterização oposta: Tatagiba e Galvão escrevem *"2016, ano do golpe jurídico-parlamentar"* (rev. p. 65). Manter o campo e declarar a divergência no status é o tratamento correto: o codebook registra o quadro do ator, não o veredito do analista.

---

## 4. Os quatro que continuam contextuais — e a varredura que os fecha

**PT-04** (eleição de 2018), **PT-05** (atrito institucional 2019-2022), **PT-06** (pandemia e ecossistema informacional) e **PT-08** (Capitólio) não mudaram de classe, e agora se sabe por quê.

Varredura de conteúdo em 04/10/2026, nos **145 arquivos** da pasta anexada, com normalização NFKC:

| Termo | Ocorrências |
|:--|:--|
| `Bolsonaro` | **zero, em 145 arquivos** |
| `pandemia` | zero |
| `negacion` | 2 arquivos, nenhum sobre o Brasil |
| `Capitol` | 11 arquivos, **todos anteriores a 2021** — enciclopédias e obras sobre história norte-americana |

As obras que os quatro registros citam — Campos Mello (2020), Cesarino (2022), Abranches, Avritzer, Levitsky & Ziblatt, Norris & Inglehart — **não estão em lugar algum ao alcance**: nem no corpus, nem nos 411 DOIs das sínteses, nem nesta pasta.

> **É a mesma lacuna, encontrada por um terceiro caminho.** A triagem de 29/09 já havia registrado que as sínteses trazem **zero referências sobre o Brasil** (agenda, item 23.2). A varredura de hoje confirma a lacuna numa coleção independente, montada por outra pessoa com outro propósito — e mostra que ela não é um acidente das sínteses: **a literatura sobre o bolsonarismo não está no alcance deste projeto**, e isso é condição a declarar, não pendência a perseguir.

O status dos quatro deixou de dizer "requer fonte primária" — frase que sugeria uma coleta ao alcance — e passou a dizer o que foi varrido, quando, e o que não se achou.

Duas observações que a releitura produziu e que não são leitura:

- **PT-05 é o menos grave dos quatro.** O atrito institucional de 2019-2022 que ele descreve tem, no próprio codebook, registros vizinhos ancorados em fonte primária: PT-05A e PT-06A a PT-06C, do arco judicial. O que falta é a literatura que interpreta o período, não a documentação dele.
- **PT-06 é o mais caro.** O mecanismo que ele afirma — consolidação do ecossistema informacional paralelo — é exatamente o que liga T₋₁ conjuntural a T₋₁ operacional. É a junta da cadeia, e é a que está sem leitura.

---

## 5. O que a leitura cobra do codebook — e é decisão sua

Nenhum dos pontos abaixo foi executado. Todos exigem juízo.

1. **A descontinuidade de 2013 para 2015-2016 não é consensual, e o codebook adota um lado sem dizer.** Tatagiba e Galvão são explícitas: *"diferentemente da perspectiva de Alonso e Mische (2015), não observamos uma descontinuidade entre 2013 e os protestos posteriores"* (rev. p. 71), e na conclusão tratam o conjunto como *"parte de um mesmo processo histórico de mudanças"* (rev. p. 91). O par PT-01 → PT-02, com mecanismo de *spin-off*, codifica ruptura. Se a leitura das autoras for adotada, o mecanismo vira **difusão intraciclo**, não apropriação entre ciclos — e isso muda o desenho da camada, não só o rótulo.

2. **Os antipetistas já estavam na rua em 2011.** *"os grupos antipetistas já estão presentes em protestos organizados em 2011, mantendo a mesma estética e slogans que caracterizaram sua atuação nos anos de 2015 e 2016"* (Tatagiba e Galvão, rev. p. 82). A apropriação do repertório, então, é de **escala**, não de origem. PT-02 data o ator em 2015-2016.

3. **"Apropriação de repertório" é nome que a fonte do conceito não detalha** (§2.2). Entra na fila da tarefa 19, ao lado da certificação de PT-03.

4. **O apelo à intervenção militar em março de 2015 pode virar registro próprio** (§2.3).

5. **A tese de doutorado do pesquisador está no corpus e analisa exatamente estes ciclos** — 1992, 2013, 2015, incluindo a entrada dos movimentos de direita. `PROCEDENCIA` a declara, desde 19/08/2026, como **antecedente teórico que "NÃO é fonte de evento e não deve ancorar registro do codebook"**. A decisão foi tomada e foi respeitada aqui. Vale reabri-la? Ela é a única peça do corpus que cobre a camada inteira — mas autocitação como âncora de registro é escolha que só você pode fazer.

6. **Alonso (2017) continua citada no relatório de pesquisa e no projeto de pesquisa**, e segue não lida. O codebook já não a cita; as outras peças, sim.

---

## 6. O que mudou no aparato

- **`Fontes/12_Camada-T-1_Literatura/`** — eixo novo, quatro PDFs. É o **primeiro caso no corpus de peça que é literatura secundária e ancora registro**: até aqui, quem ancorava era documento oficial, e teoria não ancorava nada. Por isso o eixo 12 entrou na lista `FORA_DA_DOCUMENTAL` de `verificar_integridade.py`, ao lado do eixo 05 — *a contagem documental não pode crescer porque entrou artigo de revista*. Corpus: **31 PDFs**, dos quais **22 documentais**, inalterados.
- **`scripts/recodificar_camada_t1.py`** — a recodificação, com `--dry-run`.
- **`conferir_hipoteses.py`** passou a conferir **dois** documentos em vez de um. Este documento entrou na checagem no mesmo dia em que nasceu, pela regra de 25/09: *toda peça escrita à mão que reproduz números do codebook precisa ou virar gerada, ou ganhar uma checagem no ciclo*. Custo: nenhuma linha de lógica nova.
- **`conferir_paginas.py`** ganhou duas exceções declaradas, pelo motivo da digitalização sem texto.
- **`gerar_codebook.py`** declara a procedência das quatro peças **com o deslocamento de página de cada uma**.

Classes de verificação: **61 em fonte primária · 17 confirmados · 4 contextuais · 0 a verificar · 1 inferência declarada.**
