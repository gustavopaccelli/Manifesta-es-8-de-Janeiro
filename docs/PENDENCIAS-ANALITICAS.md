# Pendências analíticas — pontos a incorporar na redação do artigo

Registro aberto em **12/08/2026** · **atualizado em 29/09/2026**. Não é codebook nem fonte: é a **agenda** do que ficou em aberto ao longo da verificação documental, e que precisa de decisão do pesquisador na hora de escrever.

Está fora do codebook de propósito. Codebook guarda dados; isto guarda perguntas. Misturá-los estraga os dois.

---

## Painel de estado — 29/09/2026

**O aparato está pronto, auditado, versionado e verificável por um comando; o artigo não começou.** Por decisão do pesquisador em 16/08/2026, a redação passou a ser o **último** item da fila: o conjunto de dados de todo o processo político vem primeiro. Nada mudou nessa decisão desde então.

| Frente | Estado |
|:--|:--|
| Codebook | **82 sub-eventos × 16 campos** — JSON, CSV e XLSX gerados de uma fonte única, com zero divergências |
| Ancoragem documental | **74 registros** com arquivo local vinculado · 68 com página ou seção atribuída · 0 referências quebradas |
| Classes de verificação | **60 em fonte primária** · 14 confirmados por outra via · 7 contextuais · **0 a verificar** · 1 inferência declarada |
| Caderno de evidências | **49 registros** com página e transcrição literal |
| Corpus documental | **20 PDFs / 6.819 p. de fonte documental** + o acórdão do TSE em HTML + 6 matérias arquivadas contra link rot + 7 sínteses. Com a bibliografia teórica do eixo 05, são 24 PDFs / 7.501 p. **Três peças sem camada de texto**, declaradas |
| Figuras | SVG da cadeia causal e cronologia navegável — **realinhadas ao codebook em 25/09**, 82 registros cobertos. São a única parte do aparato escrita à mão |
| Relatório de pesquisa | `reports/process_tracing_8jan_relatorio.md` — §3.2 corrigido em 11/09; §2.1 e a tabela da Etapa 2 em 25/09; "Próximos passos" reescrita na mesma data. Agora tem checagem no ciclo |
| Verificação | `bash scripts/ciclo.sh` — seis passos: dois geradores e quatro checagens, todas com código de saída ≠ 0 em caso de falha |
| Controle de versão | git desde 20/09/2026, sem remoto configurado |
| Eixo bibliográfico Lava Jato | 20 referências, 18 com DOI confirmado |
| Sínteses LeapSpace (não citáveis) | **411 DOIs verificados e triados em 29/09** — 408 existem, os 3 restantes com DOI correto registrado; **35 na camada A**, 65 em B, 308 fora. **Zero referências sobre o Brasil, e o cânone de mecanismos ausente** — itens 22 e 23 |
| **Redação do artigo** | **não iniciada — por decisão, é o último item da fila** |

**Fechados na rodada de 16/08/2026:** itens 1, 2 e 8, mais os seis novos — **12** (auditoria de fontes), **13** (estimativa de multidão), **14** (ressalvas restantes), **15** (balanço de 2026 e campanha), **16** (Manchetômetro → PT-50A), **17** (acórdão do TSE) e **18** (execução penal e arquivamento web).
**Fechados depois:** **19** (11/09 — relatório e páginas da execução penal), **20** (20/09 — reorganização pelo Cookiecutter Data Science) e **21** (25/09 — figuras, relatório e os dois novos passos do ciclo).
**Abertos e de redação:** itens 3, 4, 5, 6, 9 e 10.
**Abertos e de verificação:** item 7 (proveniência) e item 11 (coleta) estão **encerrados**. Nenhuma pendência de dado depende de você — as que restam são decisões, e estão no item 21.4.

> **✅ RESOLVIDO NO MESMO DIA — o balanço chegou.** PT-53 e PT-61 percorreram quatro estados em 16/08/2026: `Confirmado` (jornalístico) → **rebaixados** a `A verificar` pela auditoria → `Confirmado` por corroboração jornalística dupla → **`Confirmado em fonte primária`**, quando o pesquisador forneceu o documento: o **Relatório do Gabinete do Min. Alexandre de Moraes (29/04/2026, 15 p.)**, obtido do bucket oficial do STF e incorporado em `Fontes/10_Democracia-Inabalada/`. A cifra de **1.402 réus responsabilizados agora pode ser citada como dado oficial, com página** (p. 6). **Não resta nenhum registro em `A verificar` no codebook.** Detalhes nos itens 12–15 e em [`reports/AUDITORIA-FONTES.md`](../reports/AUDITORIA-FONTES.md).
>
> **Os dois gráficos vetoriais foram lidos por renderização no mesmo dia** — e a leitura corrigiu o codebook: o total de ações penais é **1.335**, não "mais de 1.600"; o 1.618 que circulava é de **audiências de custódia**. Resta uma ressalva da própria peça: a soma das denúncias por inquérito não fecha com o total (1.819 × 1.878).

---

## 1. Circulação paga da mobilização — ✅ ESCOPO DEFINIDO EM 12/08/2026

**Registro:** PT-19A · **Fonte:** NetLab UFRJ, 185 anúncios na biblioteca do Meta Ads

O codebook tratava só a **coordenação orgânica** (PT-19, "Festa da Selma"): grupos de mensagens, gratuitos, horizontais, sem rastro de autoria. A circulação paga é outra coisa — **anúncio tem anunciante, valor pago e decisão de aprovação pela plataforma**.

**Por que importa para o argumento.** Cada peça paga é, em princípio, um vínculo documentável entre financiamento e mensagem. Isso liga duas coisas que hoje estão soltas no corpus: o **núcleo dos financiadores** (que a CPMI trata no cap. 6.3 e o codebook menciona só de passagem, em PT-21 e PT-53) e a **responsabilidade das plataformas**, que o projeto não aborda.

**O que falta.** O levantamento do NetLab estabelece a existência do canal, **não seus operadores** — não identifica anunciantes nem valores. Para virar argumento, precisa de: (a) os dados de anunciante e gasto da própria Meta Ad Library, se ainda acessíveis; (b) cruzamento com a lista de financiadores da CPMI; (c) decisão sobre se a responsabilidade da plataforma entra no escopo do artigo ou fica como desdobramento.

**Decisão:** entra como **parágrafo**, dentro do tratamento do ecossistema informacional — mesma lógica aplicada ao financiamento no item 8. A evidência sustenta afirmar que houve canal pago e que a moderação falhou; não sustenta afirmar quem pagou. Os três fios sobre recursos (fretamento, anúncios pagos, rede de financiadores) ficam agora **conectados** pelo mecanismo de mobilização de recursos, e não mais soltos.

> ✅ **Revisado em 16/08/2026 (item 14 — Tier 4).** Sem pendência de dado. O limite declarado acima ("sustenta afirmar que houve canal pago; não sustenta afirmar quem pagou") já é a orientação correta para a redação e não muda com mais pesquisa — o próprio NetLab não identifica anunciantes. Nada a executar aqui além de escrever.

---

## 2. A contradição das 14h56 — ✅ VERIFICADO EM 12/08/2026

**Registros:** PT-32, PT-28, PT-39, PT-19B · **Fontes conferidas:** acórdão da AP 2668 (1.991 p.) e denúncia da PGR (272 p.)

Às **14h56**, Anderson Torres, dos EUA, manda ao grupo Difusão: *"Não deixem chegar ao Supremo"* (CPMI, p. 658).
Às **15h16**, o tenente Rafael Martins recolhe aos veículos a tropa que **ainda bloqueava** o acesso ao STF — "sem justificativa" (CPMI, p. 674).

**Resultado da conferência: negativo, e por isso mesmo informativo.**

Nem o acórdão nem a denúncia mencionam a mensagem das 14h56, o horário 15h16 ou o tenente Rafael Pereira Martins. *(Atenção a um falso positivo: o "Rafael Martins de Oliveira" que aparece na denúncia é outra pessoa, militar do grupo "Kids Pretos".)*

**O STF adotou uma terceira moldura** — nem insubordinação, nem mensagem performática, mas **omissão dolosa** da cúpula da SSP-DF. Torres, Fernando de Sousa Oliveira e Marília Alencar *"se omitiram no exercício de suas funções o que foi essencial para a consumação"* (p. 495); a *"omissão dolosa"* de Torres *"também caracterizou o crime de golpe de Estado"*, art. 359-M (p. 497).

**O que isso muda no artigo:**

1. A mensagem é **achado exclusivo da CPMI, sem validação judicial**. Citável como tal — nunca como fato assentado pelo STF. Registrado no status de PT-32.
2. A moldura é **omissiva, não comissiva**, e isso **coincide com a contraprova do interventor** (item 3, abaixo): a imputação recai sobre a cúpula civil da SSP-DF, não sobre a corporação militar. Os dois documentos convergem sem terem sido escritos um para o outro.
3. A contradição segue aberta — com a informação de que a mais alta corte, com acesso integral à prova, **não julgou necessário explicá-la**. Isso é reportável e vale mais que uma resposta forçada.

**Dois achados novos vieram da mesma leitura:**

- **PT-19B (registro novo)** — o grupo "Difusão" foi criado em **04/01/2023** pelo coronel Jorge Henrique da Silva Pinto (PMDF), com 7 participantes incluindo Torres, Fernando e Marília, para acompanhar as manifestações. Em **05/01** o coronel avisa ao grupo que havia "atos para os dias 06, 07, 08 e 09 de janeiro" e uma convocação para a **"Tomada de Poder"** (AP 2668, p. 495-496).
- **Reforço a PT-39** — a subsecretária de Inteligência **não escreveu uma única mensagem nesse grupo até as 16h50 de 8/1**, quando os prédios já estavam sendo retomados (p. 496). Silêncio de um dia inteiro no canal criado quatro dias antes exatamente para isso. É a evidência mais limpa da omissão que o STF veio a tipificar.

> ✅ **Revisado em 16/08/2026 (item 14 — Tier 4).** Sem pendência de dado. A orientação do ponto 1, acima ("citável como tal — nunca como fato assentado pelo STF"), já é a instrução completa para a redação.

---

## 3. Onde estava a ruptura da cadeia de comando

**Registro:** PT-28 · **Fonte:** Relatório Cappelli, conclusão G, p. 57

O Comandante-Geral da PMDF **esteve em campo e ficou entre os feridos** no ataque ao STF. Isso é contraprova direta à leitura de conivência no topo da corporação.

Mas o mesmo trecho diz que ele "perdeu a capacidade de liderar seus comandados diretos, uma vez que **suas solicitações por reforço não foram consideradas nem atendidas prontamente**".

**A pergunta em aberto:** se não era o comandante-geral e não era a tropa na ponta, **onde estava o bloqueio?** A conclusão H (p. 57) aponta uma direção: oito comandos de férias em 08/01, inclusive o do Batalhão de Choque, todos subordinados ao Cel. Jorge Eduardo Naime. Isso sugere o nível intermediário — mas é hipótese, não achado.

**Recomendação:** tratar explicitamente no artigo. Um parecerista que leia o relatório Cappelli vai encontrar a conclusão G e cobrar. Antecipá-la é mais forte que ser confrontado com ela.

---

## 4. O deslocamento do *smoking gun*

**Registros:** PT-41 → PT-18

A latência de duas horas do Batalhão de Choque **tem explicação mecânica**: regime de sobreaviso (2h30–3h de deslocamento) em vez de prontidão (~40 min), por decisão do Cel. Klepter Rosa, diversa da adotada na posse (CPMI, p. 646; Cappelli, conclusão D, p. 55).

A pergunta suspeita deixa de ser *"por que demorou duas horas"* — que agora tem resposta banal — e passa a ser *"por que o efetivo foi posto em sobreaviso, contrariando o protocolo da posse, dias depois de a Abin reportar convocações para ocupar prédios públicos"*.

**Cuidado na redação:** sustentar o *smoking gun* na demora em si, conhecendo o regime de sobreaviso, é erro que um parecerista identifica. O ônus migrou da execução para a decisão prévia — onde a evidência é **melhor** (ato administrativo nomeado e datado, não inferência sobre um intervalo).

---

## 5. Hipótese rival que a fonte primária sustenta

**Registro:** PT-23 · **Fonte:** CPMI, p. 374-375

O alerta da Abin de **07/01, 12h00** trazia a advertência sobre ocupações e violência **seguida de "mas sem coordenação concreta para tais ações"**. A qualificação não reaparece no alerta das 10h de 08/01.

Isso dá sustentação parcial à leitura de que o dispositivo foi calibrado por uma inteligência que ela própria relativizava o risco.

**Contrapeso:** o relatório Cappelli conclui, sobre o mesmo período, que **"não houve falta de informações e alertas sobre os riscos da manifestação"** (conclusão B, p. 54), citando o Relatório de Inteligência nº 006/2023 da própria SSP-DF, de 06/01, que falava em "tomada de poder".

**Recomendação:** apresentar as duas e tomar posição fundamentada. A leitura mais defensável é que a informação existia e era suficiente — mas dizer isso sem citar a ressalva de 07/01 é seletividade que enfraquece o texto.

---

## 6. Sri Lanka, não Capitólio — implicação teórica

**Registros:** PT-08, PT-19 · **Fonte:** CPMI, p. 614

O "Plano B" invocado pelos organizadores foi a revolta do **Sri Lanka de julho de 2022**, e não o Capitólio: *"seria como uma invasão do Capitólio que teria dado certo"*.

**O que isso faz com a teoria.** A difusão transnacional não seleciona o precedente culturalmente mais próximo — seleciona o **bem-sucedido**. Chamar o 8 de janeiro de "Capitólio brasileiro" descreve a forma e erra o cálculo dos atores.

Isso é contribuição teórica pequena mas própria, e vale um parágrafo na discussão. A literatura comparada do corpus (Levitsky & Ziblatt, Norris & Inglehart) não cobre esse ponto.

---

## 7. Seis ressalvas de proveniência a resolver ou declarar

Conferido contra o JSON em 14/08/2026. Os dois últimos não constavam da versão anterior desta lista — estavam marcados no campo `status_verificacao` e não tinham subido para a agenda.

| Registro | Afirmação | Situação |
|:--|:--|:--|
| ~~**PT-34**~~ | ~~"cerca de 4 mil pessoas" na Praça às 15h26~~ | ✅ **RESOLVIDA em 16/08/2026 — cifra retirada.** Busca em veículos de escala nacional mostrou fonte única (Agência Brasil, jan/2024, "policiais" sem órgão nomeado), ausência nas cronologias contemporâneas e aplicação a referente diverso pela Wikipédia. Substituída por faixa de **3.000 a 5.500** no conjunto mobilizado, com duas medições oficiais independentes. Ver [`ESTIMATIVA-MULTIDAO-8JAN.md`](ESTIMATIVA-MULTIDAO-8JAN.md) |
| ~~**PT-12**~~ | ~~"mais de 100 acampamentos" no país~~ | ✅ **RESOLVIDA em 16/08/2026 — cifra retirada, mesmo padrão do PT-34.** Busca exaustiva em todo o PDF da CPMI (não só a seção 5.5) e no Cappelli não a localizou; provinha da Agência Brasil sem órgão nomeado. Substituída pela caracterização geográfica ancorada "em todos os Estados" (CPMI, p. 510) |
| ~~**PT-17**~~ | ~~saída do país em 30/12~~ | ✅ **RESOLVIDA em 16/08/2026 — achado.** Busca exaustiva no corpus inteiro localizou a confirmação em CPMI, p. 612, no texto analítico da própria comissão: "principalmente após a partida de Bolsonaro para os EUA no dia 30 de dezembro" |
| ~~**PT-52**~~ | ~~≈1.200 presos em 40 ônibus~~ | ✅ **RESOLVIDA em 16/08/2026 — cifra substituída.** Adotadas as **2.151 prisões em flagrante** (CPMI, p. 76 e 688), primária, no lugar dos ~1.200 de imprensa, que mediam pessoas levadas à triagem nas primeiras levas da manhã. **Achado:** a CPMI se contradiz sobre o escopo — p. 76 diz "no próprio domingo ou no dia seguinte", p. 688 diz "no ato de desocupação". Adotada a p. 76, e o registro passou a dizer "8 e 9 de janeiro" |
| **PT-38** | detalhamento dos danos ao acervo | "Confirmado em linha geral — detalhamento a verificar em laudo". Busca de 16/08/2026 (item 14) confirma que a perícia segue sem prazo definido (Agência Brasil, 2023); os laudos não foram obtidos e provavelmente permanecem restritos |
| ~~**PT-58**~~ | ~~datas da prisão preventiva de Bolsonaro (22–25/11/2025)~~ | ✅ **RESOLVIDA em 16/08/2026 — achado.** Duas matérias independentes e datadas da Agência Brasil (22 e 25/11/2025) confirmam data, motivação (risco de fuga; tornozeleira eletrônica) e desfecho. Reclassificado para `Confirmado`. *Superado ainda no mesmo dia:* a decisão da Pet 14.129 foi obtida em inteiro teor e PT-58 é hoje **fonte primária** — ver item 18, que corrige também o fato de que a preventiva não decorre da execução da AP 2668 |

*Correção de 16/08/2026: até esta data, a linha de PT-58 afirmava ser ele o "único registro de $T_{+1}$ sem ancoragem documental". A auditoria mostrou que não — PT-53, PT-59, PT-60 e PT-61 também estavam sem arquivo local vinculado. PT-58 e PT-61 foram resolvidos por busca (ver item 14); PT-59 e PT-60 seguem sem mudança nesta rodada — não estavam entre as 12 ressalvas listadas para tratamento.*

**Todas as seis ressalvas deste item estão fechadas** desde 16/08/2026 — PT-34, PT-12, PT-17, PT-52, PT-58 e PT-38. Três delas (PT-34, PT-12 e PT-52) terminaram com a **retirada ou substituição de um número**, e o padrão que emergiu é o mesmo: cifra correta aplicada ao referente errado. **PT-38** confirmou a restrição de acesso ao laudo, sem novidade que a mude, mas ganhou a valoração do dano como série datada.

---

## 8. Financiamento — ✅ DECIDIDO EM 12/08/2026

**Registros:** PT-10A, PT-12A (novos) · PT-12 (mecanismo reforçado) · **Fonte:** CPMI, p. 577-578 e 880-890

A decisão não foi nenhuma das duas opções originalmente colocadas. **Nem seção própria, nem fora de escopo:** o financiamento entra como **substrato material do mecanismo que a pesquisa já afirmava** — o de que o acampamento era infraestrutura de mobilização (PT-12).

**Por que assim.** A afirmação "infraestrutura de mobilização" é a mais forte do process tracing e estava **asserida sem lastro**. Infraestrutura custa dinheiro, e a CPMI tem a contabilidade. Tratar o financiamento como objeto autônomo criaria um segundo tema competindo com o primeiro; tratá-lo como substrato **fortalece** o argumento existente sem dispersar o texto.

**O que entrou:**

- **Custo documentado** — R$ 376.043,64 à União em 70 dias, quase R$ 5 mil por dia, 200 militares a mais em prontidão (p. 577)
- **PT-10A** — o MBVA: os comboios não vieram de "caminhoneiros" difusos, mas de um grupo de empresários do agronegócio com mobilização nacional demonstrada desde 2019. **272 caminhões** identificados pela Abin (p. 884-887)
- **PT-12A** — a arquitetura de financiamento: captação pulverizada por Pix ("máfia do pix", nas palavras do comandante da PMDF) **com nós centralizadores** que convertem dinheiro em suprimento (p. 577-578, 880-884)

**O achado teórico.** A PCDF registra que "não foi identificada uma coordenação que envolvesse todos os manifestantes" — dispersão. O COAF mostra a USA Brasil Informática como "ponto centralizador". Não se contradizem: são **duas camadas** — captação sem comando único, execução concentrada em hubs. Padrão característico de movimentos **sem organização formal**, e conversa com a Teoria da Mobilização de Recursos, da mesma família de McAdam/Tarrow/Tilly já adotada.

**O que fica de fora, e está declarado no relatório.** Um tratamento próprio da rede de financiadores — nominal, com fluxos e responsabilização — é pesquisa distinta. O capítulo 6.3.29 da CPMI é o ponto de partida para quem quiser fazê-la.

**Decisão editorial registrada:** nomes reproduzidos apenas quando a CPMI os individualiza e recomenda providências; dados pessoais presentes no relatório (CPF) foram omitidos por não terem função analítica. A lista nominal de 200+ proprietários de caminhões (p. 887-890) não foi reproduzida — o dado analítico é o agregado.

---

## 9. PT-62 é inferência, e continua sem verificação

O registro sobre desmobilização das redes de rua e migração para arenas eleitorais **é declaradamente inferência do analista**. Nunca foi testado.

Para virar achado, exige PEA longitudinal ou análise de redes — pesquisa dedicada, fora do escopo deste artigo. **Recomendação:** manter como hipótese explicitada na conclusão, jamais como resultado.

> ✅ **Revisado em 16/08/2026 (item 14 — Tier 4).** Sem pendência de dado — e sem uma pendência **possível** dentro do escopo deste artigo, já que a única forma de testar a inferência é pesquisa dedicada fora dele. A recomendação acima já é a instrução completa para a redação.

---

## 10. O desequilíbrio da literatura sobre Lava Jato

Ver `Fontes/06_Lava-Jato-judicializacao-lawfare/LEIA-ME.md`.

A literatura revisada por pares posterior a 2019 é majoritariamente crítica à operação. Busquei trabalhos favoráveis e achei poucos. **Não simular simetria inexistente**; declarar o estado do campo é mais forte e é verdadeiro.

---

## 11. Coleta e bibliografia — o que está em aberto no aparato

*Seção aberta em 14/08/2026. Os dez itens acima são analíticos; este é operacional, e está aqui para não haver duas listas concorrentes.*

### 11.1 Coleta que depende de pessoa

~~**Acórdão do TSE — RCand 0600903-50.2018.6.00.0000 (PT-03E).**~~ ✅ **OBTIDO em 16/08/2026, sem captcha** — ver item 17. O arco judicial 2016-2021 está fechado.

### 11.2 Não localizados em fonte oficial — declarar como limite, não perseguir

| Documento | Registro | Situação |
|:--|:--|:--|
| Sentença de 1ª instância de Moro (12/07/2017), inteiro teor | PT-03A | Baixa prioridade — o dispositivo está transcrito no acórdão do TRF-4 (Revista 97, p. 395). Busca de 16/08/2026 achou só comentário de terceiro (6 p.), não a peça; e-proc da JFPR não consultado, provável exigência de login |
| ~~Balanço "Democracia Inabalada" (29/04/2026)~~ | PT-53, PT-61 | ✅ **OBTIDO em 16/08/2026 — ver item 15.1.** O PDF chegou pelo pesquisador, do bucket oficial do STF, e os dois registros passaram a `Confirmado em fonte primária`. *Registro do que se sabia antes, porque explica a busca:* o documento não estava indexado, e `portal.stf.jus.br/democraciainabalada` e `noticias.stf.jus.br` bloqueiam requisição automatizada com 403. **A leitura do documento corrigiu o codebook:** são 1.335 ações penais e 1.402 réus *responsabilizados*, não condenados |
| Laudos periciais do Instituto de Criminalística/PF | PT-38 | Provavelmente sob restrição de acesso — confirmado por busca em 16/08/2026 |
| Acórdão completo do HC 126.292 (todos os votos) | PT-02A | Busca de 16/08/2026 achou apenas o **voto individual do min. Barroso** (28 p.), em `luisrobertobarroso.com.br` — não baixado, por não ser o acórdão completo e por exigir confirmação antes de gravar em `Fontes/`. Ver pendência ao final deste documento |

### 11.3 Cinco sínteses de literatura chegaram à pasta em 13/08/2026 — e precisam de tratamento

Estão em `Fontes/05_Bibliografia-teorica/`, geradas pelo LeapSpace, cobrindo exatamente os cinco conceitos do referencial: **process tracing, mecanismos causais (Tilly), processo político (Tilly), estruturas de mobilização e ciclos de protesto**. Somam ~23 mil palavras e **325 DOIs distintos** — contagem de 13/08, quando eram cinco. Com as duas sínteses que chegaram em 11/09 o universo é de **411**; ver item 22.

**O que elas são e o que não são.** São sínteses geradas por sistema automatizado, com seções declaradas de escopo e limitações. **Não são fonte citável** — nem revisadas por pares, nem de autoria identificável. O valor delas é outro e é real: são **mapas de leitura** e, sobretudo, uma lista de 325 DOIs bem-formados que aponta para literatura de verdade.

**Encaminhamento proposto, em três passos:**

1. **Extrair os 325 DOIs** para uma planilha e **verificá-los no CrossRef** — mesmo protocolo já usado no eixo Lava Jato (18 de 20 confirmados) e no levantamento original. Barato e mecânico.
2. **Triar por pertinência** ao argumento: a maior parte dessa literatura é metodológica ou de teoria geral, não sobre o Brasil. Interessa o que sustenta os mecanismos efetivamente afirmados no codebook.
3. **Ler os selecionados na fonte.** A síntese entra na bibliografia do projeto como instrumento de busca — **nunca na do artigo**.

**Risco a nomear, porque é o mesmo que o projeto já enfrentou uma vez.** O levantamento original tinha um DOI fabricado (`10.1215/00382876-12345678`, corrigido em `LEIA-ME_metodologia_verificacao.md`). Material gerado automaticamente exige a mesma desconfiança — verificar antes de incorporar, sem exceção.

> **✅ PASSO 1 EXECUTADO EM 29/09/2026 — e o risco se confirmou, em forma pior.** 408 dos 411 DOIs existem; **3 não existem em nenhuma agência de registro** — os três já com DOI correto identificado e registrado (item 22.6), e um deles, o do Bennett & Checkel, **já corrigido na leva de 01/09**. E um DOI **válido** estava colado ao **autor errado** — defeito que nenhuma verificação de existência pegaria. Os passos 2 e 3 seguem abertos, e são juízo do pesquisador. Detalhe no **item 22**.

### 11.4 Literatura clássica brasileira ainda ausente

Werneck Vianna (1999), Arantes (2002), Kerche & Marona (2022) e correlatos sobre judicialização da política no Brasil. São **livros**, não indexáveis por DOI: entram por acréscimo manual ao eixo 06.

---

## 12. Auditoria de fontes — ✅ EXECUTADA EM 16/08/2026

Relatório completo em [`reports/AUDITORIA-FONTES.md`](../reports/AUDITORIA-FONTES.md), gerado por script e refeito a cada rodada de coleta.

A auditoria respondeu uma pergunta só, para todos os registros: **onde está o documento que sustenta esta afirmação, e em que página?** Não alterou nenhum fato, mecanismo ou enquadramento — só vínculo e status. Três achados:

**O inventário de fontes e o codebook divergiam em silêncio.** Cinco arquivos estavam no corpus sem vínculo com registro nenhum, e quatro deles já tinham atribuição declarada em `Fontes/LEIA-ME_fontes.md` que nunca chegara ao codebook. O caso mais grave: o livro oficial do STF sobre o vandalismo, atribuído a PT-38 no inventário e ausente do registro.

**PT-08 afirmava fonte primária sem apontar arquivo.** É o achado do **Sri Lanka, não do Capitólio** (item 6 desta agenda) — a contribuição teórica própria do projeto estava sem âncora rastreável. Corrigido: CPMI, p. 614.

**Dois registros declaravam mais confiança do que a evidência sustenta**, e foram rebaixados. Ver a nota do painel, acima.

**Um registro apontava para o documento errado.** PT-28 — o subdimensionamento crítico, *"apenas 20 policiais militares"* guarnecendo o Congresso às 14h45, que o codebook trata como **hoop test** — citava no texto "CPMI, p. 657" e vinculava o acórdão da AP 2668. A frase está na CPMI p. 657 e é **ausente das 1.991 páginas do acórdão**. Erro anterior a esta rodada, corrigido.

**A conferência integral contra o texto dos PDFs foi feita:** dos 58 registros com página em documento PDF, **53 tiveram a transcrição localizada na página citada e nenhum divergiu**. Os cinco restantes trazem referência de página sem citação entre aspas — não há o que casar, e são os candidatos naturais a ganhar transcrição literal na próxima passagem pelo caderno de evidências.

Além disso, **sete registros citavam dois documentos e declaravam apenas um** — a corroboração dupla, que é força do aparato, estava invisível. PT-18 é o caso exemplar: o regime de sobreaviso está na CPMI *e* nas conclusões D e H do Cappelli, dois documentos independentes que convergem.

**O que a auditoria não faz, e está declarado nela:** não confere se a página sustenta a afirmação (isso é o `Caderno-de-evidencias/`), não avalia qualidade de fonte, e não fecha as ressalvas de proveniência do item 7.

**Consequência operacional.** O JSON passou a ser a única fonte da verdade; CSV e XLSX são gerados por `scripts/gerar_codebook.py` e não devem ser editados à mão. `scripts/verificar_integridade.py` roda seis checagens e falha se os formatos divergirem.

---

## 13. A estimativa de multidão — ✅ RESOLVIDA EM 16/08/2026

Dossiê completo em [`ESTIMATIVA-MULTIDAO-8JAN.md`](ESTIMATIVA-MULTIDAO-8JAN.md). Era a ressalva mais antiga do projeto e a classificada como "a que preocupa".

**Decisão: a cifra de "cerca de 4 mil pessoas na Praça às 15h26" foi retirada.** A busca em veículos de escala nacional não corroborou o número — corroborou o contrário. Ele tem **fonte única** (Agência Brasil, jan/2024, atribuído a "policiais" sem órgão nomeado), **não aparece nas cronologias contemporâneas** ao fato (Poder360, 15/01/2023) nem na cronologia posterior da própria EBC (jan/2026), e a Wikipédia lusófona **aplica o mesmo número a referente diverso** — os que deixaram o QG. Número que migra de referente é número copiado, não medido.

**No lugar dele, uma faixa: 3.000 a 5.500 no conjunto mobilizado.** O que a sustenta não é uma fonte, são duas, por métodos que não se copiam:

| Medição | Órgão | Momento | Página |
|:--|:--|:--|--:|
| 105 ônibus, ~3.900 passageiros | **ANTT**, via alerta da Abin | 07/01, 12h | CPMI 374, 637 |
| 3.000 de público na área do SMU | **SSP/DF**, ao grupo CIISP-DF | 08/01, 9h | CPMI 643 |
| "um grupo de poucos milhares de manifestantes" | análise da própria CPMI | 08/01 | CPMI 695 |

Contagem de transporte e contagem policial de público convergem na mesma ordem de grandeza. A contagem da ANTT **não estava no codebook** e foi acrescentada a PT-21.

**O ganho analítico, que é o ponto.** A SSP/DF tinha estimativa própria de público às 9h da manhã. Seis horas depois, às 14h45, o Congresso estava guarnecido por **20 policiais militares** (PT-28). O número deixa de ser dado descritivo sobre a multidão e passa a ser **evidência sobre o conhecimento do Estado** — reforça o *hoop test* de PT-28 e conversa diretamente com a moldura de omissão dolosa que o STF adotou. A ressalva que enfraquecia o texto passou a sustentá-lo.

**Cuidado na redação, e é o que um parecerista vai cobrar.** Os 3.000 são das 9h, no SMU, antes da marcha — piso da manhã, não retrato da tarde. A faixa é do *conjunto mobilizado*, não dos invasores. E as duas contagens se corroboram, não se somam. A distribuição temporal da multidão segue sem fonte e **não deve ser perseguida**: exigiria laudo de contagem por imagem, que não consta do corpus, e a resposta não muda o argumento.

**Ganho lateral.** O espelho público do relatório Cappelli foi localizado e o arquivo conferido: byte-idêntico, SHA-1 `78adf23746d11ee1…`. Segue sem versão em domínio oficial — isso não mudou —, mas agora a cópia do projeto tem integridade verificável contra endereço estável.

### 13.1 Catálogo de atribuições da imprensa — instrumento separado

`data/processed/CATALOGO-IMPRENSA-MULTIDAO-8JAN.xlsx`, gerado por `scripts/gerar_catalogo_imprensa.py`.

**Por decisão do pesquisador em 16/08/2026, os números da imprensa NÃO entram no codebook nem na cronologia interativa.** O process tracing mantém apenas os números do documento legal. O catálogo é aparato de **conferência** e material para uma frente analítica própria: a de que os veículos disputam discursivamente o processo político pela via da quantificação.

Quatro abas: `Atribuicoes_Imprensa` (número · referente · atribuição declarada · data · link · citação ABNT · verificação), `Numeros_Documento_Legal` (os que ficam no codebook, com órgão, método e página), `Leitura_Analitica` e `Protocolo_Coleta`.

**Oito linhas verificadas por leitura direta da página. Quatro pendentes, e a razão precisa ficar registrada:** Folha (uol.com.br), O Globo e G1 (globo.com) e Estadão (estadao.com.br) **recusam acesso automatizado**. A recusa é do publisher, não falha de busca. Nenhum número desses veículos foi inserido sem leitura direta — durante esta pesquisa o sumarizador de busca chegou a atribuir ao Poder360 uma frase que a página não continha, e em catálogo de conferência snippet não verificado é pior que célula vazia. O protocolo de coleta manual está na quarta aba.

**O achado analítico que o catálogo já sustenta:** o "4 mil" aparece aplicado a **três referentes distintos** — público na Praça às 15h26, os que saíram do QG, e o acampamento que "aumentou para mais de quatro mil". Número que muda de objeto sem mudar de valor foi copiado, não medido. E o veículo de origem **recuou**: a EBC publica a cifra em jan/2024 e escreve apenas "milhares de apoiadores" na cronologia de jan/2026.

**Literatura para esta frente:** DRUMMOND, D.; MANGINELLI, F. *O ataque de 8 de janeiro nos editoriais dos jornais brasileiros.* SciELO Preprints, 2023. DOI 10.1590/SciELOPreprints.7040. Compara Folha, O Globo e Estadão. **Preprint, não revisado por pares** — ler na íntegra e verificar se houve publicação definitiva antes de citar.

---

## 14. As 12 ressalvas restantes — três resolvidas, duas reclassificadas, sete confirmadas como já adequadas

Rodada de 16/08/2026, executada por níveis de executabilidade — método registrado para não repetir trabalho, e para deixar claro o que foi verificação e o que foi decisão.

### 14.1 Proveniência de dado (Tier 1 — pesquisável, mesmo padrão do PT-34)

Detalhado no item 7, acima. **PT-12 e PT-17 fechados**, PT-52 **esclarecida sem substituição** — a lição inversa do PT-34: nem toda cifra sem fonte primária deve virar uma só resposta; às vezes duas cifras coexistem porque medem coisas diferentes.

### 14.2 Lacuna de coleta (Tier 2 — busca de melhor esforço)

**PT-58 e PT-61 fechados** por corroboração jornalística datada e independente (ver itens 7 e 11.2). **PT-38 e PT-03A** confirmaram, por busca, que a hipótese de restrição/ausência já registrada era a correta — sem mudança de status, mas com a busca documentada, não presumida.

**PT-53 permanece aberta**, e a busca revelou algo que não estava mapeado: **a `fonte_url` do registro aponta para um balanço diferente** do que o texto do registro descreve — "em-dois-anos-stf-responsabilizou-898-pessoas" (um balanço de dois anos, 898 pessoas) em vez de qualquer coisa ligada a "mais de 1.600 ações penais". A busca achou uma cifra próxima (~1.628 ações penais, contexto de uma decisão de apelação distinta) mas não a verificou contra documento primário. **Isso não foi corrigido nesta rodada** — decidir qual número é o certo para PT-53, e corrigir a URL, exige leitura que vai além de uma busca de melhor esforço. Fica na lista de pendências ao final deste documento.

**PT-02A achou um mirror parcial, não baixado.** `luisrobertobarroso.com.br` hospeda o **voto individual do min. Barroso** no HC 126.292 (28 p., SHA-1 `842ce8d6f04e050b0d2e69721348e4edc2668084`) — não o acórdão completo com todos os votos, que é o que a ressalva original pedia. Não foi salvo em `Fontes/`: primeiro porque não resolve a lacuna declarada, segundo porque a política do projeto exige confirmação antes de qualquer download. **Decisão pendente:** incorporar o voto do Barroso como material suplementar (útil, mas parcial) ou aguardar o acórdão completo.

### 14.3 Peso probatório e natureza declarada (Tier 4 — sem tarefa de dado)

PT-32, PT-19A e PT-62 foram revisados e **confirmados como já adequadamente documentados** — não pedem pesquisa nem recodificação, só orientação de redação. Ver a nota de fechamento correspondente, mais abaixo.

### 14.4 O que ficou de fora da execução, por exigir decisão do pesquisador

Nenhum destes foi executado — a regra desta rodada foi não decidir além do que cada ressalva autorizava textualmente:

1. **PT-53** — qual número é o correto (a cifra tangencial de ~1.628, um balanço diferente, ou nenhum dos dois) e correção da `fonte_url` desalinhada.
2. **PT-02A** — se o voto parcial do min. Barroso entra como material suplementar em `Fontes/`, dado que não é o acórdão completo pedido.
3. **PT-52** — qual dos dois números de detidos (triagem progressiva x prisão final) lidera no texto do artigo; nenhuma das duas cifras foi descartada.
4. **Obtenção do PDF "Democracia Inabalada"** (PT-53/61) — depende de contato direto com a assessoria do STF, ação fora do alcance das minhas ferramentas (sem acesso a e-mail, e contato institucional em nome do pesquisador exige a pessoa dele), ou do fluxo de cookie `aws-waf-token` já documentado em `scripts/baixar_fontes.sh`, desenhado para você rodar.
5. **PT-03E** — acórdão do TSE, hCaptcha. Sem mudança: já era só sua.

---

## 15. O balanço de 2026 chegou — e a campanha foi catalogada

Rodada final de 16/08/2026, a partir de links fornecidos pelo pesquisador. Nova pasta: `Fontes/10_Democracia-Inabalada/`, com `LEIA-ME.md` próprio.

### 15.1 O achado que fecha a última lacuna

**`STF_Gabinete-Moraes_Balanco-8-de-Janeiro_2026-04-29.pdf`** — 15 p., bucket oficial do STF em S3. É o documento que faltava desde a auditoria. **PT-53 e PT-61 passam a `Confirmado em fonte primária`**, e a `fonte_url` de PT-53 — que apontava para um balanço diferente, inconsistência levantada no item 14.2 — foi corrigida.

O que a peça traz, tudo conferido na camada de texto: **1.402 réus responsabilizados** (29 núcleos principais + 402 crimes graves + 419 crimes menos graves + 552 ANPPs, soma que fecha); 431 penas privativas de liberdade com R$ 30 mi de danos morais coletivos; 419 restritivas de direito com R$ 5 mi; **190 presos** (10,12%); pena máxima de 27 anos e 3 meses para 1 réu; 29 condenações nos núcleos, nas APs 2668, 2693, 2694 e 2696, em 21 sessões com 127 advogados e 154 testemunhas (8 de acusação, 146 de defesa).

### 15.2 A confusão que estava na origem da ressalva, agora desfeita

**"Democracia Inabalada" nomeia duas coisas diferentes, separadas por quase três anos** — e o projeto vinha tratando-as como uma só:

| Peça | Data | Natureza |
|:--|:--|:--|
| Livro/ebook `8.1.2023: Democracia Inabalada` | ago/2023 | fotográfica e narrativa, sobre o vandalismo e a restauração. **Sem estatística de responsabilização** |
| Relatório do Gabinete do Min. Moraes | **abr/2026** | **balanço estatístico** do ciclo judicial |

A página oficial da campanha tem **última atualização em 30/08/2023** e não cataloga o balanço — o que explica por que a busca da rodada anterior não o encontrou por ali.

**O ebook baixado é byte-idêntico ao livro que o projeto já tinha** em `03_T0_8-de-janeiro/` (mesmo SHA-1, 210 p.). Está marcado como `duplicata` no inventário para não ser contado duas vezes; quem ancora PT-38 continua sendo a cópia original. **Consolidar em uma só cópia é decisão sua.**

### 15.3 Catalogação da campanha

Duas peças novas na pasta, ambas de natureza analítica — a campanha é **objeto de enquadramento**, como a literatura do eixo 08, não fonte de evento:

- **`PAGINA-CAMPANHA-catalogacao.md`** — inventário completo: livro, 3 links de documentário, 15 vídeos publicitários em 4 conceitos (Edifício, Constituição, Estátua, Reconstrução), 13 cards/stories e o folder, com URLs e termos de uso.
- **`DOCUMENTARIO-catalogacao.md`** — ficha do documentário (57min01s, Rádio e TV Justiça, 30/08/2023).

**Três achados de enquadramento** que a catalogação sustenta: a **arquitetura de três tempos** (íntegro → destruído → restaurado) se repete no folder, no documentário e no vídeo-conceito "Reconstrução" — a campanha narra a superação, não o ataque; a **legitimação é buscada fora da política doméstica** (os cards citam ONU e Papa Francisco, além de três ministros, e nenhum ator do Executivo ou Legislativo); e a campanha **congelou em agosto de 2023**, enquanto o ciclo judicial seguiu até 2026 e foi relatado por outro canal, em outra linguagem — a instituição narra a ferida em imagens e a punição em números.

### 15.5 As duas pendências que o balanço abriu — fechadas no mesmo dia

**Os gráficos vetoriais foram lidos, e um deles corrigiu o codebook.** A camada de texto não entrega os valores das p. 5 e 6; renderizei as páginas com PyMuPDF e li visualmente.

**Achado: o total de ações penais é 1.335, não "mais de 1.600".** A cifra que PT-53 carregava estava errada. Por situação — condenações 850, absolvições 16, instrução em andamento 459, extinções de punibilidade 10. O número **1.618** que circulava pertence a **audiências de custódia** (p. 5), outro referente inteiramente.

É o **quarto caso do projeto de cifra correta aplicada ao objeto errado**, depois do "4 mil" de PT-34, dos "100 acampamentos" de PT-12 e do vínculo trocado de PT-28. O padrão já é reconhecível o bastante para virar rotina de conferência.

A leitura também fechou a coerência interna do balanço: **850 condenações + 552 ANPPs = 1.402 réus**, e 431 = 29 núcleos + 402 crimes graves. Os dois caminhos batem.

**A valoração do dano ao STF entrou em PT-38 — como série datada, não como número.** A busca pela fonte forte do R$ 11,4 mi foi exaustiva e **negativa**: não está no livro do STF, nem no balanço, nem na CPMI. E revelou que a cifra **foi superada** — o levantamento posterior chega a **~R$ 12 milhões** (R$ 8.616.822,30 de prejuízo direto + R$ 3.424.600,25 de reconstrução do Plenário), com 951 itens danificados e 106 de valor imensurável. Registrado como série (ago/2023 → jan/2025), com a ressalva de que nenhum documento primário do corpus a carrega. **Citar sempre com a data.**

### 15.6 Duplicata consolidada

Havia duas cópias byte-idênticas do livro do STF. SHA-256 conferido, mantida a baixada do domínio oficial em `10_Democracia-Inabalada/`, removida a de `03_T0_8-de-janeiro/` (backup em `.backup_pre_lula/`), **PT-38 repontado**. Corpus: **19 PDFs, 6.835 páginas**.

### 15.7 PT-52 resolvido — e a CPMI se contradizendo

A última ressalva de proveniência do projeto foi fechada em 16/08/2026. **Lidera o texto o número 2.151** — prisões em flagrante, CPMI p. 76 e 688 —, no lugar dos "~1.200 em 40 ônibus".

**Por quê:** os 2.151 são primários e é contagem fechada; os ~1.200 vêm da imprensa (Poder360, atribuídos ao então ministro Flávio Dino) e medem pessoas levadas à triagem *nas primeiras levas da manhã* — a mesma reportagem registra o número subindo para cerca de 2.000 à tarde. Liderar com um recorte de meio de manhã subestimaria em quase metade. E o que faz trabalho causal em PT-52 é quantas pessoas foram removidas do acampamento, não a logística do transporte.

**O achado do processo: a CPMI se contradiz sobre o escopo dos 2.151.**

| Página | Formulação |
|:--|:--|
| **p. 76** | "2.151 pessoas presas em flagrante, **no próprio domingo ou no dia seguinte**, durante a desocupação" |
| p. 688 | "**No ato de desocupação**, foram presas 2.151 pessoas" |

A p. 76 distribui o número entre os dias 8 e 9; a p. 688 o atribui inteiro ao dia 9. **Adotada a p. 76**, e o registro passou a dizer "8 e 9 de janeiro" — citar 2.151 como prisões da desocupação, que era o que o registro fazia, superestima o dia 9.

**Ganho analítico — o funil da responsabilização.** Cruzando a CPMI com o balanço de 2026:

| Etapa | N | Fonte |
|:--|--:|:--|
| Prisões em flagrante (8 e 9 jan) | **2.151** | CPMI, p. 76 e 688 |
| Audiências de custódia em 2023 | 1.397 | Balanço 2026, p. 5 |
| Denúncias do MPF até out/2023 | 1.390 | CPMI, p. 76 |
| Réus responsabilizados até abr/2026 | 1.402 | Balanço 2026, p. 6 |

**Três medições independentes convergem na casa de 1.400**, e cerca de **750 flagrantes — perto de 35% — não converteram em processo.** A repressão de massa do dia 9 é mais ampla que a responsabilização que dela resultou: prender no acampamento e responsabilizar judicialmente são operações de escalas distintas, e a diferença separa a desmobilização do repertório da punição de seus agentes. É um parágrafo de discussão que o codebook não tinha antes desta rodada.

*Ressalva declarada: a correspondência entre as 1.397 audiências de custódia e os flagrantes de 8-9/1 é inferência — forte, porque a custódia segue o flagrante em 24h e as prisões de 2023 foram esmagadoramente de janeiro, mas o balanço não a faz explicitamente.*

### 15.4 O que não foi feito, e por quê

**Não produzi o resumo por pontos do documentário.** A legenda automática existe, mas a API do YouTube devolve corpo vazio a requisição automatizada — testadas quatro vias, inclusive a API interna, que retorna `FAILED_PRECONDITION`. Resumir 57 minutos que não assisti seria a mesma falha que este projeto passou a semana corrigindo no PT-34 e no PT-12. A ficha traz metadados verificados e a sinopse oficial reproduzida; as vias para obter a transcrição estão listadas nela.

## 16. O Manchetômetro — ✅ VIRA REGISTRO (PT-50A), 16/08/2026

Era o último arquivo órfão do corpus. **Decisão: vira registro, não fica como contexto.** Com ele, **nenhum arquivo de `Fontes/` está sem vínculo ou sem procedência declarada.**

### Por que registro, e não contexto

**Traz achado datável que o codebook não cobria.** A atribuição dos atos a "infiltrados da esquerda" emerge **às 17h40 do próprio dia 8** e, em 9-10/01, desloca o debate para "o governo sabia". O codebook não tinha nada sobre a disputa discursiva imediata do pós-evento: PT-50 cobre só a nota de Bolsonaro das 21h17, e PT-62 é inferência sobre o longo prazo.

**Há precedente direto.** PT-19A entrou a partir do NetLab — também relatório de laboratório universitário, não revisado por pares, com ressalvas declaradas. O ecossistema informacional fica completo: **PT-19** cobre a circulação orgânica no WhatsApp, **PT-19A** a paga na Meta, e faltava a **orgânica pública no Facebook**.

**Contra-argumento considerado e rejeitado:** o projeto decidiu tratar cobertura de imprensa como *objeto* de análise (eixo 08), não fonte. Mas o Manchetômetro **mede circulação em plataforma**, não interpreta cobertura jornalística — é da mesma família do NetLab. A distinção que vale é entre medir circulação e interpretar cobertura, não entre acadêmico e jornalístico.

### O achado, e por que importa

A conclusão do relatório descreve três fases: no pré-8/1 só o bolsonarismo se articula; **no dia 8 "a esquerda e o governo dominaram a narrativa nas redes"** e a acusação de infiltrados sai "ainda sem sucesso"; e no pós **"a extrema-direita reconstruiu o debate nos seus termos"**, deslocando a discussão de quem foi responsável para se o governo sabia — e "a esquerda, por fim, não conseguiu retomar o protagonismo".

**Mecanismo: recaptura do enquadramento.** É desmobilização de rua **com preservação da capacidade discursiva** — o repertório de ocupação se encerra materialmente com a desocupação (PT-52), mas a infraestrutura de circulação permanece intacta e opera em modo defensivo em 48 horas. Há inversão de sinal no próprio dia 8: o campo **suprime** as lives que até a véspera serviam de convocação para o QG, e no dia 9 volta a produzir os posts de maior engajamento do período.

**Isto ancora empiricamente o primeiro passo de PT-62** — a migração da contestação da rua para outras arenas —, que era leitura do analista sem lastro. Não a converte em achado, mas lhe dá ponto de partida datado.

Um detalhe fino que vale um parágrafo: na nuvem de palavras do dia 8, **"manifestante" (4.000 menções) supera "terrorista" (3.227) e "golpista" (2.356)**. A designação do evento ainda estava em disputa no próprio dia.

### Quatro ressalvas de método, a declarar sempre

1. **Não revisado por pares** — relatório técnico de laboratório, citável como tal. Classificado `Confirmado`, não `em fonte primária`, como PT-19A.
2. **A coleta usou o CrowdTangle, descontinuado pela Meta em 14/08/2024** — os dados **não são reproduzíveis** por terceiros.
3. **Só Facebook** — não cobre WhatsApp (PT-19), Telegram nem X.
4. **"Interações" é métrica de plataforma**, não medida de alcance nem de persuasão. E a seleção dos cinco posts por período é critério dos autores.

**Pendência:** a URL de origem do relatório não foi registrada quando o PDF entrou no corpus e precisa ser recuperada para citação formal.

---

## 17. O acórdão do TSE — ✅ OBTIDO SEM CAPTCHA, 16/08/2026

Era a última peça do arco judicial e a única pendência que o projeto dava como exclusivamente sua. **Foi resolvida sem que você precisasse fazer nada.**

**A rota.** O buscador de jurisprudência do TSE é uma SPA Angular cuja API exige verificação antirrobô — um POST sem token responde `{"mensagem":"Falha na verificação antirrobô."}`. **Nenhuma tentativa de contornar isso foi feita.** O que funcionou foi outra rota, pública e sem captcha: o endpoint de documento da **Consulta Unificada PJe** (`consultaunificadapje.tse.jus.br`), que serve o inteiro teor por caminho direto. O caminho do acórdão foi localizado por busca web.

**Duas correções de documentação que o projeto vinha repetindo:**

1. **O captcha do TSE é hCAPTCHA, não reCAPTCHA.** Verificado no bundle do buscador: carrega `js.hcaptcha.com/1/api.js`, e não há uma única referência a reCAPTCHA. Todo o material do projeto dizia o contrário.
2. **O acórdão é servido em HTML, não em PDF.** O parâmetro `extensaoArquivo` só muda o `Content-Type` — pedir `application/pdf` devolve o mesmo HTML. Por isso a citação é por estrutura interna (item da ementa, dispositivo), não por página, e o arquivo não entra na contagem de PDFs.

**O achado substantivo, que muda a leitura do arco judicial.** A ementa invoca a **Súmula 41/TSE**: *"não cabe à Justiça Eleitoral decidir sobre o acerto ou desacerto das decisões proferidas por outros órgãos do Judiciário (…) que configurem causa de inelegibilidade"*. E o item 3 liga formalmente a condenação do TRF-4 (PT-03B) à inelegibilidade.

Ou seja: **o efeito eleitoral opera por automatismo institucional** — basta a decisão colegiada existir. A Justiça Eleitoral declara-se incompetente para examinar se ela é boa. Isso explica, com fonte primária, por que a anulação por incompetência (PT-06A) e o reconhecimento da suspeição de Moro (PT-06B), ambos posteriores, **não puderam desfazer a exclusão consumada em 2018**. A remoção do competidor não dependeu de a condenação ser correta; dependeu de ela ser colegiada e existir a tempo.

Detalhe que vale registrar: entre os impugnantes arrolados no acórdão está **Jair Messias Bolsonaro** — o adversário direto no pleito figura formalmente como parte que pediu o indeferimento.

---

## 18. Execução penal e arquivamento web — ✅ 16/08/2026

**As três decisões da execução penal foram obtidas.** PT-58, PT-59 e PT-60 saem de "apoiado em notícia do portal do STF" para **fonte primária**. A rota: as páginas de notícia do STF, que recusam o WebFetch com 403, respondem a `curl` com user-agent de navegador — e trazem link direto para a peça. Nenhuma das três exigiu o cookie do WAF.

| Registro | Decisão | Rota |
|:--|:--|:--|
| PT-58 | Pet 14.129, 22/11/2025, 17 p. | PDF hospedado pela Agência Brasil |
| PT-59 | EP 169, 15/01/2026, 36 p. | bucket S3 do portal de notícias do STF |
| PT-60 | EP 169, 24/03/2026, 40 p. | `portal.stf.jus.br/processos/downloadPeca.asp` |

### Duas correções de fato que a leitura das decisões produziu

**1. A prisão preventiva não decorre da execução da AP 2668.** Foi decretada na **Petição 14.129** — processo distinto, por *coação no curso do processo* (art. 344 do CP), *obstrução de investigação de organização criminosa* (art. 2º, §1º, da Lei 12.850/13) e *abolição violenta do Estado Democrático de Direito* (art. 359-L), "em face de sua participação nos mesmos delitos de **Eduardo Nantes Bolsonaro**". O que a decisão faz é **converter em prisão as cautelares já impostas em 17/7/2025** naqueles autos. O cumprimento da pena da AP 2668 começa em **25/11**, e é ato distinto. **O registro anterior fundia os dois.**

Isso afina o mecanismo: a preventiva é **contenção de fuga**, não execução. A decisão encadeia quatro elementos — iminência do trânsito em julgado, a vigília convocada pelo senador Flávio Bolsonaro para a véspera, a evasão de Alexandre Ramagem para Miami, e a violação do monitoramento eletrônico às 0h08 do dia 22. Registra ainda que o réu "planejou (…) a fuga para a embaixada da Argentina, por meio de solicitação de asilo político", e que a embaixada dos EUA fica "cerca de 15 (quinze) minutos de carro" da residência.

**2. A domiciliar humanitária é de 24/03/2026**, não "mar/2026 com prorrogação em 03/07/2026". **A prorrogação de julho não tem lastro no corpus** — foi retirada do campo de data e marcada como não verificada. Não citar sem obtê-la.

### Duas precisões acrescentadas

**PT-59** — a transferência é para **Sala de Estado Maior** no 19º BPM, *dentro* da Papuda. Prerrogativa preservada, não equiparação ao regime comum. E a mesma decisão já ordena a junta médica oficial que dois meses depois fundamenta a domiciliar.

**PT-60** — a concessão é a **segunda tentativa**: o mesmo pedido fora **indeferido em 2/3/2026**, após perícia oficial da PF. O que muda entre março e março é o quadro clínico, não o critério — o que sustenta ler a decisão como modulação técnica, e não como recuo. A domiciliar vem com tornozeleira de área restrita, relatórios diários, fiscalização semanal da PMDF e vistoria documentada de todo veículo que deixe a residência.

### Arquivamento web

Seis matérias que ancoravam registros só por URL foram copiadas para `Fontes/09_Arquivamento-web/` — três da Agência Brasil (PT-03A, PT-03D, PT-38), duas de PT-58 e duas páginas de notícia do STF (PT-59, PT-60). **Não são fonte primária**: preservam a evidência de que a notícia existiu e do que dizia, contra link rot.

Uma falhou: a página de notícia do TSE sobre PT-03E devolve 403. Irrelevante agora — o acórdão está no corpus (item 17).

---

## 19. O relatório alinhado ao codebook — ✅ 11/09/2026

Rodada feita item por item, a pedido do pesquisador. O gatilho foi uma falha: **`verificar_integridade.py` voltou a reprovar** porque duas sínteses LeapSpace tinham entrado em `Fontes/05_Bibliografia-teorica/` sem declaração em `PROCEDENCIA`. A terceira checagem existe exatamente para isso e funcionou.

### 19.1 O relatório carregava cifras que o codebook já tinha corrigido

`reports/process_tracing_8jan_relatorio.md` estava quase um mês atrás do JSON. Cinco correções em §3.2 e no cabeçalho:

| Estava | Ficou | Onde |
|:--|:--|:--|
| "mais de 1.600 ações penais" (três ocorrências) | **1.335 ações penais** | Balanço 2026, p. 6 |
| "1.402 condenados" | **1.402 réus responsabilizados** — 850 condenados em ação penal (29 núcleos + 402 graves + 419 menos graves) e 552 ANPPs | Balanço 2026, p. 6 |
| "131 ações extintas por cumprimento de pena" | **retirado** — ausente da camada de texto do balanço | — |
| execução penal citada por imprensa | fonte primária, com a **preventiva da Pet 14.129 separada do início da pena**, a Sala de Estado Maior nomeada, a domiciliar datada em 24/03/2026 e o indeferimento anterior de 2/3/2026 | Pet 14.129 e EP 169 |
| prorrogação de 03/07/2026 | **retirada** — sem lastro no corpus | — |
| "81 × 16" no cabeçalho | **82 × 16** | — |

O cabeçalho ganhou um bloco de revisão declarando o que foi e o que **não** foi revisto nessa passagem — o resto do relatório não foi reconferido linha a linha.

### 19.2 O achado que vale como método: a checagem amostral aprovava pelo motivo errado

`scripts/recodificar_paginas_execucao.py` corrigiu `fonte_pagina` de PT-58, PT-59 e PT-60, que apontavam para a **capa e a assinatura** das peças em vez das páginas onde as transcrições estão. E corrigiu `metadados.n_subeventos` de 81 para 82, que estava defasado desde a entrada do 82º registro.

O importante é **por que ninguém tinha visto**. `conferir_paginas.py` dava OK nos três:

- **PT-58 e PT-60** passavam porque a primeira citação de cada um está mesmo na p. 1 — a capa. O verificador aprova quando *qualquer* citação casa com *qualquer* página listada, e parava na primeira.
- **PT-59 passava sem que a página do dispositivo fosse aberta.** Uma janela de 60 caracteres com o endereço do 19º BPM casou com a p. 36, e o verificador parou ali; o dispositivo da transferência começa na **p. 33**.

> **Correção de 25/09/2026, feita ao endurecer a ferramenta.** A frase acima dizia, até esta data, que PT-59 passara "pela citação errada". Está imprecisa, e a verificação desmentiu-a: a decisão da EP 169 tem o dispositivo **começando na p. 33 e seguindo até a p. 36**, e a janela que casava na p. 36 é parte legítima da mesma transcrição — 300 caracteres adiante. O vínculo antigo não era falso, era **incompleto**: confirmava a página final sem nunca abrir a inicial. A correção de 11/09 continua certa; o diagnóstico é que estava exagerado. Ver a ressalva no cabeçalho de `scripts/conferir_paginas.py`.

É o **quinto caso do projeto de cifra ou referência correta aplicada ao objeto errado**, e o primeiro em que a ferramenta de conferência participou do erro. A correção das páginas foi feita medindo cobertura por página, não assumindo.

> **Pendência aberta aqui, e é de decisão sua:** endurecer o `conferir_paginas.py` para exigir que **cada** citação apareça, substancialmente, em alguma das páginas listadas — e não qualquer uma em qualquer uma. Antes de adotar, rodar contra os 68 registros com página: é provável que apareçam outros casos como o do PT-59, e o custo da mudança é justamente esse trabalho.

---

## 20. Reprodutibilidade: o diretório reorganizado — ✅ 20/09/2026

Reorganização pelos princípios do *Cookiecutter Data Science* — dado bruto imutável, derivados gerados por script, fluxo em um sentido só —, em seis commits, **sem quebrar uma única âncora**.

**O que entrou onde não havia nada:** controle de versão (o projeto não era repositório git), `README.md`, `requirements.txt` com versões travadas, e `scripts/ciclo.sh` no lugar do Makefile que o padrão prevê — não há `make` na máquina, e o ciclo é linear.

**O que se moveu:** os derivados saíram da raiz para `data/processed/` (CSV, XLSX, catálogo da imprensa), `reports/` (auditoria, relatório, figuras), `docs/` (esta agenda, os dossiês de método, o documento-base) e `data/external/` (o levantamento bibliográfico original). Na raiz ficaram o JSON, o README e o `requirements.txt`.

**O que deliberadamente não se moveu:** `Fontes/` e `scripts/` mantiveram os nomes em português. São citados por **290 referências** no JSON, nos scripts e nos documentos; renomeá-los custaria mais do que a nomenclatura do padrão vale.

**Duas armadilhas técnicas fechadas na mesma rodada:**

1. `.gitattributes` com `* -text`. O CSV é gerado com terminador `\n` e BOM de UTF-8, por decisão registrada em `gerar_codebook.py` — deixar o git normalizar para CRLF faria o arquivo em disco divergir do que o gerador escreve, e cada regeração apareceria como diferença fantasma.
2. O XLSX saiu do versionamento. O openpyxl carimba a hora em `docProps/core.xml` e nos *timestamps* do zip: o arquivo muda de bytes sem mudar de conteúdo. Nada se perde — ele sai do JSON por script, e o CSV com os mesmos 82 × 16 está no histórico.

**Verificação da mudança:** ciclo completo a cada etapa, mais um varredor de links relativos — 0 quebrados ao final.

> **Ponteiros não atualizados, de propósito.** O JSON menciona nomes de arquivos movidos dentro de campos de texto (`PENDENCIAS-ANALITICAS.md`, `ESTIMATIVA-MULTIDAO-8JAN.md`, `Pesquisa-sobre-Mobilizações-de-8-de-Janeiro.md`). Corrigi-los reescreve o CSV e a auditoria na próxima execução do ciclo — é decisão sua se vale o ruído no histórico.

---

## 21. As figuras, e o buraco que elas revelaram no ciclo — ✅ 25/09/2026

### 21.1 Seis semanas publicando cifras retiradas

As duas peças de `reports/figures/` estavam paradas em 12/08 e traziam **treze divergências em relação ao codebook** — seis delas cifras retiradas nas rodadas de 16/08 e 11/09, as demais correções de data, de referente e de vocabulário:

| Registro | A figura dizia | O codebook diz |
|:--|:--|:--|
| PT-24 | marcha de **9 km** | **7,9 km** pela via N1, com escolta da PMDF (CPMI, p. 645 e 648) |
| PT-22 | alertas da Abin **às 8h20** | **8h53 e 9h** — 8h20 é o corte da contagem, não o horário de emissão |
| PT-34 | **~4 mil** na Praça | faixa construída de **3.000 a 5.500** no conjunto mobilizado |
| PT-12 | **+100** acampamentos | **em todos os Estados** (CPMI, p. 510) |
| PT-10 | **>1.000** pontos de bloqueio | **1.300** pontos, cifra do diretor-geral da PRF (CPMI, p. 999) |
| PT-52 | **~1.200** presos | **2.151** em flagrante nos dias 8 e 9 (CPMI, p. 76) |
| PT-53 | **+1.600** ações penais | **1.335** — o 1.618 é de audiências de custódia |
| PT-61 | 1.402 **condenados**; 131 ações extintas | 1.402 **responsabilizados**; a linha das extintas retirada |
| PT-58 | "prisão preventiva e início da pena" | preventiva pela **Pet 14.129**, ato distinto do cumprimento da pena |
| PT-59 | "transferência para a Papuda" | **Sala de Estado Maior** no 19º BPM, dentro do complexo |
| PT-60 | "mar/2026 (prorrog. 03/07)" | **24/03/2026**, sem a prorrogação |
| PT-07 | "2021" | **22/03/2021**, primeira deliberação datada pela denúncia da PGR |
| contagem | 81 (HTML) e 75 (SVG) | **82** |

Na cronologia interativa entraram ainda duas mudanças de estrutura: o selo de status passou a **distinguir "Confirmado em fonte primária" (60) de "Confirmado" (14)**, como o codebook faz; e **32 registros que citavam a cronologia da Agência Brasil**, onde já existe ancoragem primária, passaram a citar documento e página, com a transcrição literal remetida ao campo `fonte_trecho`.

*Correção registrada: a reescrita automática aplicou "Fonte primária" a PT-27 e PT-38, que o codebook classifica só como `Confirmado`. Corrigido no mesmo dia.*

### 21.2 A causa, que é estrutural

**`reports/figures/` é a única parte do aparato que não é gerada.** A cronologia interativa carrega uma cópia manual dos 82 registros dentro do `<script>`; o SVG é rótulo por rótulo, em coordenadas absolutas. Editar o JSON não as atualiza, e **nada no ciclo percebia**: `verificar_integridade.py` cobre JSON ↔ CSV ↔ XLSX ↔ `Fontes/`, e as figuras estão fora desse circuito.

### 21.3 A correção estrutural: `conferir_figuras.py` entra no ciclo

Quatro checagens: cobertura dos 82 ids, selo de status contra `status_classe`, uso de "fonte primária" só onde o codebook confirma, e 11 cifras mortas procuradas no SVG, cada uma com o registro onde foi retirada. Entrou como passo 4 de 6 em `scripts/ciclo.sh`, e foi testado por injeção de defeito — reprova nos cinco casos ensaiados: selo trocado, "fonte primária" indevida, id inexistente, cifra morta ressuscitada no SVG e contagem antiga.

**O que ele não faz, e está declarado no cabeçalho:** compara o que as figuras *declaram*, não o conteúdo dos rótulos. Uma cifra nova e errada passa por ele, como passaria pelo estrutural. A correção das figuras continua manual.

Na mesma rodada, `gerar_auditoria.py` deixou de contar à mão: os "81 registros" estavam fixos no código desde que o codebook chegou a 82, em duas passagens, e a contagem do caderno de evidências também. E o item 3 dos limites da auditoria afirmava que PT-12, PT-17 e PT-52 seguiam abertas — as três foram fechadas em 16/08/2026, como registram seus próprios `nota_auditoria`.

### 21.4 O que espera decisão sua

Nenhum destes é falta de dado. Todos são escolha.

1. ~~**Endurecer o `conferir_paginas.py`**~~ ✅ **feito em 25/09/2026** (item 21.7). Achou dois erros de página, em PT-02A e PT-03A, e desmentiu o diagnóstico que o projeto vinha repetindo sobre PT-59.
2. **PT-61, "Conclusão dos julgamentos"** no campo `resposta_estatal`, contra as **459 ações penais ainda em instrução** que o próprio balanço registra (p. 6). O balanço é do gabinete e usa a palavra; o codebook a reproduz. Manter com ressalva, ou reformular?
3. ~~**A seção "Próximos passos recomendados" do relatório**~~ ✅ **reescrita em 25/09/2026.** Estava na versão de 14/08 e fechava recomendando começar a redigir, contrariando a decisão de 16/08. Agora abre declarando a decisão que a ordena e registra por que as rodadas seguintes lhe deram razão. Quatro frentes que ela dava como abertas foram para "concluído", com data, e os abertos passaram a separar o que vem antes da redação do que se resolve nela.
4. **Ponteiros de arquivo dentro do JSON** (item 20) — atualizar reescreve CSV e auditoria no próximo ciclo.
5. **Divergências figura ↔ codebook que o verificador não cobre:** PT-17 e PT-18 preenchem *Target* e *Framing* no HTML onde o codebook traz "—"; PT-38 omite a restauração e os 106 itens de valor imensurável.
6. **`.backup_pre_lula/`** ficou redundante desde que existe histórico git. Apagar?
7. **Licença e remoto do git** — nenhum dos dois definido.
8. ~~**Duas lacunas de `fonte_pagina`**~~ ✅ **corrigidas em 25/09/2026** (item 21.6). PT-28 precisava de dois documentos, não um: o varredor só viu o segundo depois que o `mecanismo_causal` entrou na varredura.

### 21.5 O relatório também entrou no ciclo — e já tinha três defasagens

`scripts/conferir_relatorio.py`, criado na mesma rodada, fecha o último buraco: o relatório de pesquisa era a peça que reproduzia números do codebook sem nenhuma checagem. Quatro comparações — cobertura da tabela da Etapa 2 contra os ids do codebook, páginas citadas contra `fonte_pagina`, cifras retiradas linha a linha, e caminhos citados em *code span*.

**Na primeira execução achou quatro divergências, todas reais:**

| Onde | O que estava |
|:--|:--|
| §2.1, narrativa das 13h00 | "a **9 km** em linha reta dos três edifícios pelo Eixo Monumental" — são **7,9 km pela via N1, com escolta da PMDF** (CPMI, p. 645 e 648), corrigido no codebook desde 12/08 |
| Tabela da Etapa 2, linha PT-24 | repetia "**Marcha (9 km)**" |
| §2.6 | `Fontes/01_` era abreviação de prosa, não caminho — vira `Fontes/01_Arco-judicial_2017-2021/` |
| PT-10 | a tabela citava "CPMI, p. 999, **1021** e 1023" e o `fonte_pagina` trazia só 999 e 1023 |

**O caso PT-10 inverte a expectativa e por isso vale registro.** Nas duas rodadas anteriores o JSON estava certo e a peça derivada, errada. Aqui foi o contrário: o relatório citava a página certa e o campo estruturado do codebook a havia perdido — o próprio registro nomeia as três páginas em `fonte_trecho` e em `status_verificacao`. A p. 1021 foi lida no PDF antes da correção e sustenta a afirmação: o diretor-geral da PRF declara ali que "essa foi, talvez, a maior manifestação do mundo, com **1,3 mil bloqueios montados**", a mesma cifra que a p. 999 registra como "um total de 1.300 pontos de interdição no País". Corrigido por `scripts/recodificar_pagina_pt10.py`.

**O limite dos dois verificadores, declarado:** comparam o que a peça *declara* — ids, páginas, selo, cifras mortas, caminhos —, não a prosa. Uma cifra nova e errada passa; uma afirmação causal sem lastro passa. Eles pegam **regressão declarada**, não erro de interpretação.

Os dois foram testados por injeção de defeito, um de cada vez, com a árvore restaurada em seguida. O do relatório reprova nos sete casos ensaiados: registro que some da tabela, id inexistente, página não ancorada, página de um documento atribuída a outro, cifra morta ressuscitada, vocabulário revertido para "condenados" e contagem antiga no cabeçalho.

---

### 21.6 O varredor de `fonte_pagina` — e as duas âncoras que faltavam

O caso PT-10 apareceu de raspão: o relatório citava uma página a mais, e por isso a lacuna no campo estruturado ficou visível. Onde nenhuma peça derivada cita, ninguém veria. `scripts/varrer_fonte_pagina.py` compara, nos 82 registros, as **223 citações de página** que a prosa faz (`fonte_trecho`, `mecanismo_causal`, `status_verificacao`, `nota_auditoria`) com o que o `fonte_pagina` ancora.

**É triagem, não gate, e fica fora do ciclo.** Página citada na prosa não é, por si, página que falta: pode ser refutação, remissão a outro registro ou menção de passagem. Ele imprime o trecho em volta de cada achado para que a decisão leve segundos, e sai com código 0 por padrão. Testado contra o próprio PT-10: revertendo o campo ao estado anterior, o registro reaparece na lista.

**Na estreia, oito candidatos: seis legítimos e dois reais.** Os legítimos ficam registrados porque vão reaparecer a cada execução — PT-12 e PT-34 citam páginas para *refutar* uma cifra, PT-39 remete à página de PT-08A, PT-06C à denúncia que ancora PT-07, e PT-59 é artefato do varredor ("PGR" ali é parte processual, não documento).

**Os dois reais foram corrigidos em 25/09/2026**, por `scripts/recodificar_ancoras_pt15_pt28.py`. Li as quatro páginas no PDF antes de mexer:

| Registro | A prosa citava | O campo ancorava | O que a página traz |
|:--|:--|:--|:--|
| **PT-15** | "CPMI, p. 25, 53 **e 274**" | `CPMI: 25, 53` | A p. 274 traz o atentado de 12/12/2022 e o pretexto alegado — a prisão do cacique Tserere —, que é o acréscimo que o `status_verificacao` credita a ela |
| **PT-28** | Cappelli, **conclusão G, p. 57**, e AP 2668, **p. 495 e 497** | `CPMI: 657`, e o `fonte_local` só com a CPMI | Cappelli p. 57: o comandante-geral "esteve em campo", "figurou entre os policiais militares feridos" e "perdeu a capacidade de liderar seus comandados diretos". AP 2668 p. 495 e 497: "a clara omissão de altos funcionários da Secretaria de Segurança Pública" e "a omissão dolosa do réu ANDERSON GUSTAVO TORRES também caracterizou o crime de golpe de Estado" |

**PT-28 rendeu duas lições.** A primeira: o registro que o codebook trata como *hoop test* discutia a contraprova do interventor e a moldura do STF sem vincular nenhum dos dois documentos — é a mesma família que a auditoria de 16/08 fechou ("sete registros citavam dois documentos e declaravam apenas um"), e este escapou. O vínculo da AP 2668 sumiu na própria correção de 16/08, que trocou o arquivo errado pelo certo **em vez de somar os dois**.

A segunda é sobre o varredor: a primeira versão não lia o `mecanismo_causal`, e era ali que PT-28 citava os dois documentos. O campo entrou na varredura na mesma rodada — oito citações a mais, dois achados reais a mais, zero ruído a mais. **Uma varredura só encontra onde olha**, e o limite de escopo é mais fácil de errar que o de lógica.

Sobram seis candidatos, todos legítimos, e o ciclo completo passa: seis checagens APROVADO, figuras e relatório OK, 59 confirmados / 0 falhas.

> **Ressalva que esta rodada deixa mais visível.** O `conferir_paginas.py` não exercitou as quatro páginas novas: ele para na primeira citação que casa, e nos dois registros a primeira já casava. As páginas foram conferidas por leitura direta do PDF, não pela ferramenta. É mais um argumento para o item 1 da lista abaixo.

---

### 21.7 O conferidor endurecido — e um diagnóstico meu que caiu

Era a decisão mais antiga da lista, aberta desde 11/09. A versão anterior do `conferir_paginas.py` aprovava o registro assim que **uma** transcrição casasse com **uma** página listada, e parava ali. Quatro consequências, todas fechadas nesta rodada:

| O que passava batido | Efeito |
|:--|:--|
| Só o **primeiro documento** de `fonte_pagina` era aberto | As âncoras novas de PT-28 — Cappelli e AP 2668 — seriam invisíveis |
| Intervalos viravam **só as pontas** | "CPMI: 880-884" abria 880 e 884; duas transcrições de PT-12A estão nas p. 881 e 882 |
| A elisão **"(...)"** quebrava o casamento | A janela literal atravessava o buraco (PT-34) |
| Bastava **uma** transcrição de várias | O resto nunca era conferido |

Agora cada transcrição precisa ser localizada, intervalos são expandidos, a elisão parte a citação em fragmentos e a normalização de busca apaga aspas — duas "não localizadas", PT-08A e PT-36, eram só isso: o PDF escreve «o painel "as mulatas", de di cavalcanti» e o codebook transcreve sem as aspas internas.

**Dois erros de página reais na estreia**, corrigidos por `scripts/recodificar_paginas_pt02a_pt03a.py` com as páginas lidas antes:

- **PT-02A** citava a **p. 3** do acórdão das ADC 43/44/54, que é a **autuação** — folha de rosto com partes e advogados. O trecho está na **p. 6**, onde começa o relatório do min. Marco Aurélio.
- **PT-03A** ancorava só a p. 395, do dispositivo. A segunda transcrição — "a sentença condenou o ex-presidente por um único ato de corrupção" — está na **p. 348** do mesmo volume.

A correção de PT-02A propagou: o `conferir_relatorio.py` reprovou em seguida, porque a tabela da Etapa 2 e a nota de fonte da §1.1 ainda diziam "p. 3 e 9", e a cronologia interativa também. **Os verificadores passaram a pegar os efeitos uns dos outros** — que é o comportamento que se quer de um ciclo.

#### O que ele não pega, e a retificação que isso me obrigou a fazer

**PT-59 continua passando com o vínculo de antes de 11/09.** Ao testar a ferramenta contra o caso que a motivou, o resultado foi negativo — e a investigação desmentiu o diagnóstico que este projeto vinha repetindo em quatro lugares.

A decisão da EP 169 tem o dispositivo **começando na p. 33 e seguindo até a p. 36**. A janela de 60 caracteres que casava na p. 36, com o endereço do 19º BPM, é **parte legítima da mesma transcrição** — 300 caracteres adiante. Não era "a citação errada": era a citação certa, casada no fim em vez do começo. **O vínculo antigo era incompleto, não falso.**

A correção de 11/09 continua certa — as p. 33 e 35 precisavam entrar. O que estava errado era a explicação, mais forte do que a evidência sustentava. A retificação está registrada no cabeçalho de `scripts/conferir_paginas.py`, no da migração de 11/09, em `metadados.revisoes` do JSON e no item 19.2 acima.

**O que aponta para esse caso não é a falha, é o aviso.** A ferramenta agora lista as **páginas listadas que nenhuma transcrição alcança** — com o vínculo antigo de PT-59, a p. 1 aparecia ali. São 59 páginas nessa situação no corpus inteiro, e não é falha: a página pode sustentar um fato que o registro não transcreve entre aspas. É onde olhar primeiro quando uma âncora estiver sob suspeita.

Testado por injeção de defeito: página trocada em PT-24 reprova (1/2 localizadas), documento trocado em PT-28 reprova (0/1). Uma exceção registrada em `EXCECOES`, com motivo: a manchete do STF que PT-06A cita de passagem e que não está — nem deveria estar — no PDF da denúncia da PGR.

---

## 22. Os 411 DOIs das sínteses, verificados — ✅ 29/09/2026

Tarefa 9 da ordem de ataque, aberta desde 14/08/2026 — e **não intocada**: dez itens foram conferidos à mão em **01/09/2026**, quatro divergentes, nas fichas de [`projeto-pos-doc/08_BIBLIOGRAFIA-METODOLOGICA.md`](../projeto-pos-doc/08_BIBLIOGRAFIA-METODOLOGICA.md). Os quatro modos de falha que essa leva nomeou orientaram esta. `scripts/verificar_dois_sinteses.py` extrai os DOIs das sete sínteses LeapSpace, consulta cada um no CrossRef — e, se lá não estiver, na DataCite — e emite [`data/processed/dois_sinteses_leapspace.csv`](../data/processed/dois_sinteses_leapspace.csv). Fica **fora do ciclo**, como o varredor de `fonte_pagina`: é instrumento de triagem, não gate.

### 22.1 A contagem certa é 411, não 325

O extrator foi calibrado contra um número que esta agenda já trazia: a união dos DOIs das **cinco** sínteses de 13/08 dá **exatamente 325**, o que o item 11.3 declara desde 14/08. A regex reproduz o levantamento anterior, então não está inventando nem perdendo DOIs — e o `--autoteste` prende essa contagem.

Mas duas outras sínteses chegaram em **01/09** — `Political_and_discursive_opportunities` e `Framing_process_and_alignment` — e acrescentam **86 DOIs distintos**. O universo de hoje é **411 DOIs em 444 menções**.

**A defasagem era desta agenda, não do projeto.** O inventário `Fontes/LEIA-ME_fontes.md` já registrava as sete sínteses, a substituição das cinco primeiras por reemissões em 01/09 e a contagem por arquivo — chegando a 410 distintos. Só o item 11.3 daqui ficou quatro semanas anunciando a conta de cinco arquivos enquanto sete estavam na pasta. A diferença de um DOI entre os 410 do inventário e os 411 daqui está resolvida no fim de 22.6: eram 90 em `Causal_mechanisms`, não 89.

### 22.2 Eixo 1 — o DOI existe?

| Situação | Quantos |
|:--|:--|
| Confirmado no CrossRef | 404 |
| Confirmado na **DataCite** — existe, mas não é o CrossRef que registra | 4 |
| Não existe em nenhuma das duas | **3** |

Os quatro da DataCite seriam **falsos negativos** se o CrossRef fosse a única via: dois da *Partecipazione e Conflitto* (Università del Salento) e dois da *European Papers*. Um deles é Chironi & Fittipaldi (2017) sobre o Podemos como partido híbrido — literatura do próprio campo, que uma verificação de uma agência só teria descartado como inexistente.

**Os três que nenhuma agência registra**, com o que a leitura da própria síntese mostrou:

| DOI declarado | O que é, de fato |
|:--|:--|
| `10.1007/9781139858472` | Prefixo da Springer colado a um ISBN da Cambridge. A obra é real e é **central para este projeto**: Bennett & Checkel (2014, org.), *Process Tracing: From Metaphor to Analytic Tool*. O DOI verdadeiro é `10.1017/CBO9781139858472`. **Já achado e corrigido na leva de 01/09** — ver a retificação 1 em 22.6 |
| `10.4324/9780203856949-48` | Sufixo inexistente. O capítulo de O'Halloran está no `-40` — ver 22.3, é pior do que parece |
| `10.4324/9781315731377-34` | Sufixo inexistente, mas **o capítulo existe**: Chenoweth (2015), *Political mobilization and institutions*, está em `10.4324/9781315731377-28`. Ver a retificação 2 em 22.6 |

### 22.3 Eixo 2 — o DOI certo no autor errado

**Confirmar que o DOI existe não confirma que a síntese o atribuiu à obra certa.** A `Framing_process_and_alignment` lista, em sequência:

> Vaughan, E. (2010) *How can teachers use a corpus for their own research?* → `10.4324/9780203856949-40`
> O'Halloran, K. (2010) *How to use corpus linguistics in the study of media discourse* → `10.4324/9780203856949-48`

O `-48` não existe. E o `-40`, que **existe e passou como confirmado**, é justamente o capítulo de O'Halloran sobre discurso midiático — não o de Vaughan. Os dois DOIs estão deslocados: um real, colado ao autor errado.

Reconstruído pelo CrossRef, o par correto é **Vaughan → `10.4324/9780203856949-34`** e **O'Halloran → `10.4324/9780203856949-40`**.

É o mesmo modo de falha que esta agenda já registrou quatro vezes dentro do codebook (itens 7 e 15.7) — *a cifra correta aplicada ao referente errado* — agora fora dele, na bibliografia gerada, e invisível a qualquer verificação que só pergunte "este DOI responde?". Daí o segundo eixo: para cada menção, o título que a agência devolve é procurado na janela de 300 caracteres que antecede o DOI na síntese. Abaixo de 60% dos termos significativos presentes, a menção vai para conferência **com o trecho impresso**.

**435 das 444 menções casam; 9 vão para conferência.** Oito das nove são benignas e a leitura do trecho as absolve em segundos: a síntese escreve o título em inglês e a revista registrou em português ou espanhol (*Dados*, *Revista de Sociologia e Política*, *CIAN*, *Revista de Ciencia Política*, *Polis*), ou a síntese omitiu o título e deixou só o nome do periódico. A nona é o caso O'Halloran. **O `--autoteste` exige que ela seja pega** — um segundo eixo que não pegasse o caso que o motivou não serviria para nada.

### 22.4 O que a triagem tem diante de si — e por que ela é sua

Ordenação **mecânica** por termo no título e nos assuntos declarados, que é instrumento de triagem e não juízo bibliográfico:

| Eixo | DOIs confirmados |
|:--|:--|
| movimentos sociais, protesto, enquadramento | 149 |
| método (process tracing, estudo de caso, inferência causal) | 49 |
| América Latina | 5, dos quais 2 também de movimentos |
| nenhum termo do referencial no título | **203** |

Os 203 sem termo dão a medida do que as sínteses arrastam: entre eles, "Basics of Bayesian methods", publicado em *Methods in Molecular Biology*, e onze verbetes de enciclopédia. É literatura real e verificada — e boa parte não tem relação com o argumento.

**E um achado que fecha o item 11.4 com número: das 411 referências, zero mencionam o Brasil** — nem no título, nem no veículo, nem nos assuntos. As cinco de América Latina são sobre difusão, repertórios e ondas de protesto no continente. A literatura clássica brasileira sobre judicialização **não vai sair destas sínteses**; entra por acréscimo manual, como o item 11.4 já previa.

### 22.5 O que não fiz, porque é decisão sua

1. **A triagem por pertinência (passo 2) e a leitura na fonte (passo 3).** O que sustenta os mecanismos afirmados no codebook é juízo seu; a planilha existe para que esse juízo leve horas em vez de semanas.
2. **O que fazer com os três DOIs quebrados e com a atribuição trocada.** As sínteses estão em `Fontes/`, que é imutável por princípio — não as editei. A correção pertence à bibliografia do projeto, quando essas obras forem incorporadas.
3. **O "polite pool" do CrossRef.** Ele pede um e-mail no cabeçalho da requisição; não mandei o seu a serviço de terceiro sem você pedir. O pool público atendeu as 411 consultas sem recusa.

### 22.6 Os três corrigidos — e duas retificações do que escrevi acima

A pedido seu, os três DOIs quebrados ganharam substituto verificado no CrossRef:

| Declarado na síntese | Correto | Obra |
|:--|:--|:--|
| `10.1007/9781139858472` | `10.1017/CBO9781139858472` | Bennett & Checkel (2014, org.), *Process tracing* |
| `10.4324/9780203856949-48` | `10.4324/9780203856949-40` | O'Halloran (2010), capítulo sobre discurso midiático |
| `10.4324/9781315731377-34` | `10.4324/9781315731377-28` | Chenoweth (2015), *Political mobilization and institutions* |
| — (par deslocado) | `10.4324/9780203856949-34` | Vaughan (2010), o capítulo a que a síntese deu o `-40` |

Registrados em três lugares: a ficha da **segunda leva** em [`projeto-pos-doc/08_BIBLIOGRAFIA-METODOLOGICA.md`](../projeto-pos-doc/08_BIBLIOGRAFIA-METODOLOGICA.md) §1.1, a lista de achados de [`Fontes/LEIA-ME_fontes.md`](../Fontes/LEIA-ME_fontes.md), e os dicionários `NAO_EXISTEM` e `VIZINHOS_TROCADOS` de `scripts/verificar_dois_sinteses.py`. **As sínteses não foram editadas** — `Fontes/` é imutável por princípio, e a correção pertence ao registro bibliográfico, não à fonte.

**Isto corrige identificadores, não incorpora obras.** Se Vaughan, O'Halloran ou Chenoweth entram na bibliografia do artigo continua sendo juízo seu, e depende da triagem do passo 2.

#### Retificação 1 — o caso Bennett & Checkel não era achado desta rodada

**A primeira leva de verificação já o tinha achado e corrigido, em 01/09/2026.** Está na ficha 8 de `08_BIBLIOGRAFIA-METODOLOGICA.md`, com o diagnóstico completo — prefixo da Springer em obra da Cambridge — e na lista de achados de `Fontes/LEIA-ME_fontes.md`. Quando escrevi o item 22.2 eu não havia lido nenhum dos dois, e apresentei como novo o que o projeto já registrava. A varredura o **reencontrou**, o que vale como controle da ferramenta, não como descoberta.

Pela mesma razão, a abertura deste item 22 está corrigida: a tarefa 9 não estava intocada desde 14/08 — dez itens foram conferidos à mão em 01/09, quatro divergentes, e os quatro modos de falha que essa leva nomeou são o que orientou esta.

#### Retificação 2 — o capítulo do Chenoweth existe

Em 22.2 eu disse que ele "nunca foi depositado" e que o caminho era citar pelo livro. **Errado.** Ele está em `10.4324/9781315731377-28`, com metadados completos no CrossRef. O engano tem causa identificável e vale como método: testei o DOI **do livro**, que responde, e concluí do sufixo inexistente que o capítulo não existia. A consulta que resolve é a **busca bibliográfica pelo título**, com filtro de prefixo — foi ela que achou o `-28` e, no mesmo movimento, o `-34` de Vaughan. **Sufixo inexistente não é capítulo inexistente.**

#### A divergência de contagem, resolvida: 90, e a tabela deixa de ser digitada

O inventário de fontes declarava **410** DOIs distintos e **89** em `Causal_mechanisms`; a `PROCEDENCIA` de `gerar_codebook.py` declarava **90** para esse arquivo. A recontagem que chegou a 89 é de 01/09 e **não deixou registro do critério** — o git começa em 20/09, depois dela, então o histórico não a recupera. Restava contar de novo, dizendo a regra.

**Nenhum critério principiado reproduz 89.** A anatomia do arquivo:

| Critério | Número |
|:--|--:|
| Menções de DOI no texto | 91 |
| **DOIs distintos** — cadeia normalizada em `word/document.xml` | **90** |
| Obras distintas, colapsando as duas versões `.pub2` com as suas v1 | 88 |
| Entradas da lista de referências (quatro sem DOI) | 95 |

As 91 menções para 90 DOIs têm causa identificada, e é a mesma família dos achados de 22.3: **duas entradas, de capítulos diferentes, recebem o mesmo DOI de livro** — `10.4324/9781315100371`, *Immigration and Categorical Inequality*. Repetição de DOI dentro de um arquivo não é anomalia deste: ocorre em **cinco das sete** sínteses.

**Adotado: 90 no arquivo, 411 no total, e 89 corrigido como erro de contagem à mão.** Os três lugares passaram a concordar. E a causa estrutural foi fechada do jeito que este projeto fecha: **a tabela por arquivo agora é impressa por `scripts/verificar_dois_sinteses.py` a cada execução**, com o critério no cabeçalho, e o script **cobra as duas contagens escritas à mão** — a de `PROCEDENCIA` e a do inventário de fontes —, saindo com código 1 quando divergem. Provado por injeção: 89 posto de volta no inventário reprova, nomeando arquivo e número.

Era a **terceira cópia manual de uma cifra** do projeto, depois das figuras e do relatório, e falhou pelo mesmo mecanismo das outras duas: alguém corrigiu uma cópia e não a outra, e nada avisou. A regra da página anterior vale também para número de metadado: **se é digitado em dois lugares, vai divergir.**

## 23. A triagem por pertinência — e o buraco que ela encontrou — ✅ 29/09/2026

Passo 2 do encaminhamento do item 11.3, a pedido seu. `scripts/triar_dois.py` classifica os 411 em três camadas e emite [`data/processed/triagem_dois.csv`](../data/processed/triagem_dois.csv), com o uso declarado item por item.

### 23.1 O critério, que não é de gosto

Pertinência aqui significa uma coisa só: **sustentar um mecanismo que o codebook efetivamente afirma**. O vocabulário causal foi extraído dos **82 campos `mecanismo_causal` do JSON**, não de uma ideia geral do que seja literatura de movimentos sociais — certificação e descertificação, apropriação e mudança de repertório, difusão e emulação transnacional, alinhamento de quadros, estrutura de oportunidade e sua reversão, estruturas de mobilização e rede com nós, *policing* e defecção do agente de contenção, limiar e contágio, radicalização de flanco, repressão escalonada, ciclo e desmobilização, mais o próprio método.

| Camada | Quantos | O que é |
|:--|--:|:--|
| **A** | **43** | Sustenta um mecanismo afirmado, ou é a referência canônica do conceito que o codebook usa pelo nome |
| **B** | 72 | Leitura útil, decisão na escrita: teoria geral, caso comparável, verbete, instrumento adjacente |
| **C** | 313 | Fora. Não é juízo de qualidade: é ausência de relação com o argumento |
| — | 3 | Os DOIs inexistentes do item 22 |

São **431 linhas**: os 411 DOIs impressos, 12 recuperados por busca de título, 5 sem DOI em agência alguma (23.5) e as 3 do cânone acrescentado à mão (23.6).

**A camada A nomeia 31 dos 82 registros** — eram 25 antes de o cânone entrar, em 23.6. Cada linha da planilha diz qual — "PT-27, PT-31 e PT-32: presença e ação policial como variável do desfecho", e assim por diante.

### 23.2 O buraco, que é o achado principal

Procurei no corpus, um por um, os mecanismos que o codebook afirma **pelo nome**. O resultado importa mais do que os 35 selecionados:

| O que o codebook afirma | O que as sínteses trazem |
|:--|:--|
| `Dynamics of Contention` (McAdam, Tarrow & Tilly, 2001) — a obra do vocabulário | **zero ocorrências** |
| `Power in Movement` (Tarrow) | **zero ocorrências** |
| *certification* / certificação — PT-03, PT-13, PT-50, PT-06B | **nenhum título** |
| *brokerage* / corretagem | **nenhum título** |
| *blame shifting* — PT-42 | **nenhum título** |
| *threshold* e *critical mass* — PT-29, PT-34 | **nenhum título** |
| McCarthy & Zald (1977), mobilização de recursos | ausente; há Zald & Ash (1966) |

PT-03D diz, com essas palavras, "em vocabulário de Tilly e Tarrow" — e a obra desse vocabulário não está na lista de 411. O mais perto que o corpus chega é o verbete **"Mechanisms", de Tarrow**, na *Wiley-Blackwell Encyclopedia*, que por isso foi para a camada A.

**A explicação é estrutural, e vale como regra sobre este tipo de insumo.** Uma lista gerada por sistema é densa onde a produção recente é densa — enquadramento, ativismo digital, e um bloco grande sobre formação do Estado em Tilly, que o codebook não usa — e rala exatamente nos clássicos que o desenho mobiliza. **Contar DOIs não revela isso. Só revela procurar, no corpus, cada mecanismo que o codebook afirma.**

Consequência prática: o cânone de mecanismos entra **à mão**, pela mesma via da literatura clássica brasileira do item 11.4. São duas lacunas do mesmo tipo, e nenhuma delas se resolve com mais DOIs de síntese.

### 23.3 O que a camada A cobre

| Função no desenho | Itens |
|:--|--:|
| Método — process tracing, testes, mecanismo, catálogo de eventos, seleção de evento | 12 |
| Enquadramento, alinhamento de quadros e oportunidade discursiva | 10 |
| Repertório, difusão e contágio | 4 |
| Estruturas de mobilização, recursos e rede | 4 |
| *Policing*, repressão e defecção do agente de contenção | 4 |
| Contestação de resultado eleitoral e o 6 de Janeiro | 2 |
| Verbete de Tarrow sobre mecanismo (duas versões) | 2 |
| Dinâmica relacional da radicalização | 1 |
| Ciclo de protesto e desmobilização | 1 |

Três itens da camada A merecem nota, porque respondem a pontos que a agenda já tinha em aberto:

- **`Event Catalogs as Theories`** (Tilly, 2002) — catálogo de eventos *é* teoria. É a descrição do que este codebook de 82 sub-eventos é, e o argumento pronto para quem o tratar como mera cronologia.
- **`Focusing on Focusing Events`** (2018) — seleção de evento e viés de cobertura, que é a ressalva central da análise de eventos de protesto e que este corpus enfrenta por ser documental, não jornalístico.
- **`January 6th and De-Democratization`** e **`Comparing the #StopTheSteal Movement`** — o caso de que PT-08 afirma ser emulação, lido pela literatura. Sem eles, a difusão transnacional fica asserida.

### 23.5 As 21 entradas sem DOI, que nunca estiveram no universo

A triagem tinha um limite que só apareceu quando fui conferir uma afirmação de `08_BIBLIOGRAFIA-METODOLOGICA.md`: ele diz que **Bröer e Duyvendak (2009)**, sobre oportunidades discursivas e regras de sentimento, "aparece nas sínteses". Procurei entre os 411 e não estava. A síntese o cita — mas **por link do Scopus, sem DOI**.

**São 21 entradas nessa situação**, distribuídas nas sete sínteses. Elas nunca entraram no universo verificado, porque o universo era "DOIs impressos". E não eram periféricas:

| Recuperado por busca de título | Camada | Por quê |
|:--|:--|:--|
| SNOW *et al.* (2014), *The Emergence, Development, and Future of the Framing Perspective* | **A** | PT-07: o balanço de 25 anos do alinhamento de quadros, pelos autores da formulação |
| BRÖER & DUYVENDAK (2009), *Discursive Opportunities, Feeling Rules* | **A** | PT-07 e PT-50A: é o item que `08_BIBLIOGRAFIA` já apontava como de interesse |
| ALIMI *et al.* (2012), *Relational Dynamics and Processes of Radicalization* | **A** | PT-06, PT-15 e PT-16: a radicalização de flanco em quadro relacional |
| mais quatro em B e um em C | | oportunidade política em contexto repressivo, engajamento organizacional, desempregados, crítica ao estrutural |

**Os 21 links apontam para 18 entradas distintas** — duas são citadas em duas sínteses, e um dos links é um **segundo identificador** na entrada do Waldner, que já tem DOI. As 18 foram resolvidas uma a uma:

| Desfecho | Quantas |
|:--|--:|
| **Identificador recuperado** por busca de título, no CrossRef ou na DataCite | **12** |
| **Sem DOI em agência alguma** — e com evidência disso, não só ausência de busca | 5 |
| Duplicata de entrada que já tem DOI entre os 411 (Beach & Pedersen, 2013) | 1 |

Cinco dos doze recuperados foram para a **camada A**: Snow *et al.* (2014), Bröer & Duyvendak (2009), Alimi *et al.* (2012), **Goertz & Mahoney (2012)** — as duas culturas de inferência, que é antecipação de crítica dos itens 3 a 5 — e **Jung (2010)**, análise de história de eventos de ciclos de protesto, que é o assunto de PT-62 com o instrumento que este codebook também usa.

**Os cinco sem DOI, e a evidência de que não é falha de busca.** Para cada um perguntei ao CrossRef se o veículo depositou **qualquer** DOI naquele ano: a *Demokratizatsiya* não depositou nada em 2018; a *Política y Gobierno* nada em 2017; a *Kölner Zeitschrift* nada em 1999; a *Sociological Theory and Methods* (JAMS) não está no CrossRef; e o texto de Durán é working paper de instituto. Ficam na planilha com o metadado que a **síntese** declara, marcado como tal, porque nenhuma agência o confirma — e dois deles valem leitura: Inclán (2017) sobre o legado conceitual de Tarrow, e Rössel (1999) sobre por que o conflito social vira violento, que é a pergunta de PT-29 a PT-33 em outro caso.

**Uma armadilha nova, e ela repete a lição da rodada.** A busca por *A Tale of Two Cultures* devolve primeiro o **artigo** homônimo de 2006, dos mesmos autores (`10.1093/pan/mpj017`); a entrada é o **livro** de 2012. Título parecido, autoria idêntica, obra outra. **Casar título e autor não basta quando o autor se repete** — o ano também entra na conferência. O livro tem três DOIs, de três plataformas; registrei o da Princeton.

**A lição é sobre o desenho da varredura, não sobre o LeapSpace.** Eu defini o universo pelo identificador que sabia extrair, e o que não tinha identificador ficou invisível — inclusive a referência mais central do eixo de enquadramento. **Um universo definido pelo que a ferramenta lê não é o universo.** `verificar_dois_sinteses.py` passou a imprimir a contagem dessas entradas a cada execução, para elas não voltarem a desaparecer.

### 23.6 O cânone entrou — e a cifra do corpus estava conflacionada

O buraco de 23.2 foi fechado pelo pesquisador, que forneceu os dois livros. Os dados abaixo foram **lidos das próprias folhas de rosto**, não de catálogo:

| Obra | Onde está | DOI |
|:--|:--|:--|
| McADAM, TARROW & TILLY, *Dynamics of Contention* (CUP, 2001) | `Fontes/05_Bibliografia-teorica/`, 411 p., com camada de texto | `10.1017/CBO9780511805431` |
| TARROW, *O poder em movimento* (Vozes, 2009, trad. Ana Maria Sallum) | idem, 162 folhas **em duas páginas por folha** e **sem camada de texto** | `10.1017/CBO9780511813245` (2ª ed. inglesa) |
| McCARTHY & ZALD, *Resource Mobilization and Social Movements* (AJS, 1977) | referência acrescentada, **arquivo não coletado** | `10.1086/226464` |

Os três DOIs foram confirmados no CrossRef. **A camada A vai a 43 e a cobertura sobe de 25 para 31 dos 82 registros** — três obras fecharam seis lacunas, entre elas a certificação de PT-13 e PT-50 e a mobilização de recursos de PT-10A e PT-19A, que nenhum dos 411 sustentava.

A edição brasileira do Tarrow **não declara qual edição inglesa traduz**; o sumário, em três partes e onze capítulos, corresponde à 2ª (1998), e é esse o DOI registrado. A verificação foi por renderização de página, porque o arquivo não tem texto — é a terceira peça do corpus nessa condição.

#### A cifra que a entrada dos livros obrigou a conferir

Acrescentar dois PDFs ao eixo 05 mudou o total do corpus, e ao recontar apareceu um defeito **anterior** a esta rodada:

| Onde | Dizia | É |
|:--|:--|:--|
| Painel, README, relatório | 22 PDFs / 6.928 p. | 24 PDFs / 7.501 p., dos quais **20 / 6.819 p. são fonte documental** |
| `projeto-pos-doc/01_PROJETO-PESQUISA.md` | "**22 documentos oficiais** que somam 6.928 páginas" | **20 documentos oficiais / 6.819 páginas** |

**Dois dos 22 nunca foram documentos oficiais:** eram os livros de método que já estavam no eixo 05. A contagem era medida com PyPDF — o `LEIA-ME` do dossiê até se gaba disso, "não copiado do painel" — e ainda assim somava o que não devia. **Medir certo não garante contar a coisa certa.** Documento oficial, neste projeto, é o que ancora registro; livro de teoria não ancora nenhum.

`verificar_integridade.py` passou a conferir **as duas contagens**, total e documental, com a linha de base de 29/09/2026.

### 23.4 Os limites, que precisam ser ditos

1. **A triagem lê metadado, não obra.** Título, veículo, ano, autoria e assunto — o que a agência registra. **Nada da camada A é citável antes do passo 3**, a leitura na fonte. As dez fichas de `08_BIBLIOGRAFIA-METODOLOGICA.md` mostram quanto de metadado não sobrevive à leitura.
2. **A camada C não é lixo.** São 308 itens reais e verificados, sem relação com este argumento. Entre eles, o bloco de formação do Estado em Tilly, que seria pertinente a outra pesquisa.
3. **Uma atribuição ficou marcada para conferência:** o balanço crítico de análise de enquadramento que o CrossRef devolve sob a autoria de van Dijk. Está na camada B com a ressalva escrita na própria linha.
4. **A chave da triagem é o título, não o DOI.** Digitar 100 DOIs à mão seria convidar o defeito que este projeto persegue desde agosto; cada linha traz um fragmento de título e quantas correspondências espera, e o script aborta se achar número diferente. **Foi o que pegou onze fragmentos ambíguos na primeira execução** — `Mechanisms` casava com dezesseis títulos, `Democracy` com sete.

---

## 24. A leitura na fonte — onde os 43 estão, e os cinco que foram lidos — 🔶 29-30/09/2026

Passo 3 do item 11.3. `scripts/localizar_camada_a.py` responde a pergunta que a triagem não respondeu — **desta lista, o que eu consigo abrir?** — e emite [`data/processed/camada_a_acesso.csv`](../data/processed/camada_a_acesso.csv).

### 24.1 As quatro rotas

| Rota | Itens | O que autoriza |
|:--|--:|:--|
| CORPUS | 2 | arquivo em `Fontes/`; ficha sem rede |
| ABERTO | 7 | texto integral livre declarado |
| VITRINE | 5 | o registro diz aberto e só devolve página de destino |
| FECHADO | 29 | depende de acesso institucional |

**"is_oa: true" não significa texto disponível**, e a distinção é o ponto do script. Dois casos provam:

- **Cammaerts (2012)**, rota verde no repositório da LSE: o PDF depositado tem **1 página e 1.348 caracteres** — é a folha de capa, cujo texto termina aconselhando consultar o editor. O artigo não está lá.
- **Mayntz (2004)**, classificada VITRINE pelo registro: o repositório do Max Planck tem o **texto integral, 23 páginas**. A rota estava no arquivo, não no registro.

**Sete dos 43 já tinham ficha** da primeira leva (01/09) — Beach & Pedersen, Machamer, Cammaerts, Almeida, Motta, Koopmans e Waldner.

### 24.2 O muro de acesso, que é o achado operacional

Cloudflare barrou **SAGE, Wiley, Oxford, Chicago e eScholarship**, inclusive em navegador real; a eScholarship apresentou verificação humana, que não se contorna. Passaram **Cambridge Core, MDPI, Nature e MPG.PuRe**. Isso não é obstáculo técnico a resolver: é a constatação de que **29 dos 43 dependem do seu acesso institucional**, e que a leitura na fonte não é tarefa de script.

### 24.3 Os artigos lidos, e o que a leitura mudou

**COLLIER (2011), *Understanding Process Tracing*** — lido integralmente no Cambridge Core. Tipo declarado: *The Teacher*, PS 44(4), p. 823-830. A nota de fonte da tabela 1 diz que os quatro testes são **"adapted from Bennett (2010, 210), who builds on categories formulated by Van Evera (1997, 31-32)"**. O projeto os atribui a **Beach e Pedersen (2019)** em `01_PROJETO-PESQUISA_v1-compacto.md`; a proposta de disciplina já traz Collier ao lado. **A genealogia dos testes precisa ser decidida.** E Collier adverte que a distinção entre os quatro "should not be taken rigidly": a mesma evidência pode ser um teste ou outro conforme o conhecimento prévio e a formulação da hipótese — logo o teste nomeado exige a premissa declarada. Sobre PT-28, a leitura **confirma** a redação do codebook: o teste de argola estabelece critério **necessário**, elimina quem não passa e não confirma quem passa; "condição necessária (hoop test)" está correto nos termos de Collier.

**MAYNTZ (2004), *Mechanisms in the Analysis of Social Macro-Phenomena*** — 23 páginas, texto integral no MPG.PuRe. **É a objeção mais séria que a leitura encontrou.** Mayntz registra as duas posições e adota uma: "most authors agree that mechanism statements are causal generalizations about **recurrent** processes. **In this sense, the term shall be used in this article.**" Mecanismos "são" sequências de eventos causalmente ligados "**that occur repeatedly in reality**". A posição oposta ela atribui a **Boudon (1998, p. 172)**, para quem mecanismos sociais "tend to be idiosyncratic and singular". O codebook chama de `mecanismo_causal` os elos de **um episódio único**. Nos termos que Mayntz adota, não são mecanismos — são **causal reconstruction**, nome que ela própria dá ao procedimento e que descreve o que este projeto faz. **Se o projeto mantém a palavra "mecanismo" para caso único, a citação que o autoriza é Boudon, não Mayntz.** E a última frase do resumo de Mayntz sustenta a camada estrutural: falta à literatura tratamento sistemático de mecanismos geradores em que instituições e configurações estruturais sejam decisivas.

**GONZÁLEZ-BAILÓN et al. (2011), *Scientific Reports* 1:197** — 7 páginas, PDF aberto. Áreas declaradas: física, física aplicada, física estatística — é artigo de ciência de redes, não de sociologia de movimentos. O achado central é **negativo e mais preciso do que a triagem supôs**: os participantes iniciais, isto é, os recrutadores, **não têm posição topológica típica**; só os disseminadores de cascata são mais centrais. Isso casa com PT-19 ("coordenação sem comando centralizado visível") e qualifica PT-12A: "nós centralizadores" vale no nível da difusão, não do recrutamento. **Limite a declarar:** os dados são do Twitter espanhol de maio de 2011 — rede aberta —, enquanto PT-06 descreve ecossistema fechado de Telegram e WhatsApp.

**CASTAÑEDA & JENKS (2023), *January 6th and De-Democratization*** — texto integral na MDPI, cc-by. Não contém as palavras *diffusion* nem *emulation*. O Brasil aparece **uma vez**, em uma frase: o ataque ao congresso para contestar eleição "has now become **a contentious performance** that was used by the equivalent actors in Brazil on January 8, 2023", ambos com encorajamento de Steve Bannon. **É literatura revisada por pares nomeando o 8 de Janeiro como a mesma *contentious performance* — o termo de Tilly, e `Contentious Performances` está na camada A.** Mas é asserção de uma frase, sem evidência no próprio artigo. Serve para mostrar que a leitura do 8/1 como emulação circula no campo; **não estabelece a difusão**, e PT-08 já registra que o precedente invocado pelos organizadores foi o Sri Lanka, não o Capitólio.

### 24.4 Uma armadilha de extração, que quase produziu um achado falso

Ao indexar o vocabulário causal em *Dynamics of Contention*, a busca por `certification` devolveu **zero páginas** — o que teria sustentado a afirmação de que a obra do vocabulário não usa o termo. **Errado.** O PDF grava a ligadura tipográfica **ﬁ** (U+FB01), e "certiﬁcation" não casa com "certification". Normalizada a ligadura, aparecem **42 páginas**. Conferido: *certification* 42, *decertification* 21, *brokerage* 93, *identity shift* 37, *radicalization* 34, *diffusion* 31, *category formation* 28, *social appropriation* 21, *object shift* 21, *emulation* 11, *escalation* 9, *attribution of similarity* 5, *threshold* 3. **Ausência em busca de PDF não é ausência na obra** — é a mesma regra do `conferir_paginas.py`, que abre a página em vez de confiar no campo.

### 24.5 *Dynamics of Contention* lida na fonte — as definições, e o que elas cobram do codebook

A obra do vocabulário está no corpus e foi lida nos trechos definidores. **O desvio de paginação é de 24**: a página física 356 traz no rodapé "Part III: Applications and Conclusions **332**", e as páginas impressas abaixo estão convertidas por essa conferência, não por estimativa.

| Mecanismo | Definição na obra | Página impressa |
|:--|:--|--:|
| **Brokerage** | "the linking of two or more previously unconnected social sites by a unit that mediates their relations with one another and/or with yet other sites" | 26 |
| **Certification** | "refers to the validation of actors, their performances, and their claims **by external authorities**" | 145; repetida em 158 |
| **Diffusion** | "the transfer of information along established lines of interaction" | 333 |
| **Attribution of similarity** | o mecanismo pelo qual atores reconhecem outros como semelhantes o bastante para a ação se transferir | 333 |
| **Scale shift** | processo com dois caminhos: o de **difusão/emulação** e o de **corretagem/formação de coalizão** | 332 |

**Quatro registros usam "certificação". Três passam, um não.** Contra a definição da obra — validação **por autoridade externa** —, PT-13 ("o aval da autoridade máxima"), PT-06B ("a autoridade que havia certificado é ela própria declarada parcial") e PT-50 ("retirada de apoio simbólico") estão corretos: em todos há autoridade externa que valida ou retira validação. **PT-03 não.** "Certificação de eficácia: a mobilização de rua **é validada** como via legítima de deposição" — validada por quem? Não há autoridade no enunciado: o que valida é o **desfecho**, e isso não é certificação nos termos da obra. É, nos próprios termos dela, matéria do caminho de difusão/emulação e da atribuição de similaridade. **O rótulo de PT-03 precisa ou nomear a autoridade, ou mudar de nome.** Decisão sua.

**O limiar não vem daqui — e a obra argumenta contra ele.** *Threshold* aparece três vezes em 411 páginas. Uma é idiomática ("at the threshold of the twenty-first century", p. 272). As outras duas são a **crítica**: a p. 306 apresenta o limiar crítico pela analogia da caldeira a vapor como um dos "standard accounts", e a p. 307 conclui que "**we have claimed that the threshold effect occurs rarely**", preferindo mecanismos relacionais — corretagem, certificação, formação de coalizão entre classes. PT-29 ("transposição do limiar... dispara o contágio") e PT-34 ("massa crítica") usam, portanto, vocabulário que a obra do vocabulário **rejeita como raro**. A triagem já havia registrado que *threshold* e *critical mass* não têm nenhum título no corpus (item 23.2); a leitura na fonte fecha a questão: **o cânone que está no corpus também não os fornece.** Se PT-29 e PT-34 permanecem, precisam de Granovetter ou da literatura de massa crítica — que não está coletada.

### 24.6 A mesma objeção, das duas fontes do próprio vocabulário

Mayntz adota mecanismo como processo **recorrente**. E *Dynamics of Contention* diz, na p. 13: "**Instead of seeking to identify necessary and sufficient conditions** for mobilization, action, or certain trajectories, **we search out recurrent causal mechanisms**."

O codebook faz as duas coisas que essa frase separa: chama de `mecanismo_causal` os elos de **um episódio único** e os submete a testes de **condição necessária** (PT-28, *hoop test*). Não é incoerência de execução — é a junção de dois programas: o vocabulário vem de McAdam, Tarrow e Tilly, que buscam recorrência entre episódios e recusam a linguagem de necessidade e suficiência; o aparato de teste vem de Van Evera, Bennett, Collier e Beach & Pedersen, que testam hipóteses em caso único. **As duas fontes mais citadas do desenho apontam a mesma objeção, e ela chega ao artigo pela pena do parecerista se não chegar antes pela do autor.** Fica registrada aqui, com as três saídas visíveis: manter "mecanismo" e citar Boudon (1998, p. 172); trocar para *causal reconstruction*, nome de Mayntz para o procedimento; ou declarar a junção e defendê-la. É decisão sua, e é a que mais muda o texto.

### 24.7 O Tarrow não foi lido, e a razão é física

`TARROW_O-poder-em-movimento_Vozes-2009.pdf` é digitalização **sem camada de texto**, duas páginas do livro por folha. A edição foi conferida por renderização em 29/09; a **leitura** exigiria OCR de 162 folhas, e OCR de varredura em duas páginas por folha erra paginação, que é justamente o que uma ficha precisa ancorar. **Não foi feito, e não deve ser apresentado como feito.** Os usos declarados — ciclo de confronto (PT-62), estruturas de mobilização (PT-12A, PT-21), oportunidade política (PT-01, PT-03D, PT-05A) — seguem sem ficha.

---

## 25. A enciclopédia entra, e com ela a decisão sobre "mecanismo" fica instruída — 🔶 30/09/2026

O pesquisador acrescentou ao eixo 05 a **Wiley-Blackwell Encyclopedia of Social and Political Movements** (Snow, della Porta, Klandermans e McAdam, orgs., 2013; 1.638 p., com camada de texto). **É a obra-contêiner de boa parte dos 411 DOIs das sínteses** — 434 verbetes com DOI próprio —, e por isso destrava a tarefa 17: sete verbetes da camada A e adjacências deixam de depender de assinatura de editor.

**Quatro verbetes lidos integralmente na fonte:** *Mechanisms* (Tarrow), *Protest cycles and waves* (della Porta), *Resource mobilization theory* (Edwards & Gillham) e *Critical mass theory* (Oliver). O resultado está em [`projeto-pos-doc/09_CONCEITO-MECANISMO.md`](../projeto-pos-doc/09_CONCEITO-MECANISMO.md), com a tabela de **quatorze concepções de mecanismo causal** e o preço de cada saída.

**Só um dos quatro estava nos 411, e isso confirma o buraco do item 23.2.** *Mechanisms* (`wbespm127`) é o item 39-40 da camada A. Os outros três — **protest cycles, resource mobilization e critical mass** — **não aparecem em nenhuma das sete sínteses**, embora duas delas se chamem `Protest_cycle_LeapSpace.docx` e `Mobilization_structures_LeapSpace.docx`. As sínteses citam 411 DOIs e não citam o verbete de referência do próprio conceito que dá nome ao arquivo. **A leitura na fonte, portanto, subiu de 5 para 6 dos 43** — o `.pub2` de 2022 é revisão posterior e não está neste volume.

### 25.1 A decisão do item 24.6 deixou de ser aposta

A objeção era: o codebook nomeia mecanismo em episódio único e o testa por condição necessária, enquanto Mayntz e *Dynamics of Contention* exigem recorrência. **A saída apareceu no manual brasileiro que já estava no corpus** — CUNHA & ARAÚJO (2018, Enap), que registra: os estudos de caso causais diferem "ao nível no qual a relação causal opera (regularidade... ou **singularidade, num único caso**)", e **Beach e Pedersen (2016) admitem a singularidade**, indicando o *process tracing* como o método próprio dela. É a mesma tradição de que o projeto já toma o aparato de teste. **Boudon deixa de ser necessário.**

E Tarrow acrescenta o critério que falta: **processo é "larger-scale causal event that contains sequences or combinations of mechanisms"**, e "distinguishing mechanisms from processes is essential". Vários dos 82 registros são processos — PT-62 entre eles. Com o esquema `X [A → B → C] → Y` de Machamer via Beach & Pedersen, a triagem é aplicável registro a registro.

### 25.2 Sete cobranças ao codebook, todas decisão sua

PT-03 (certificação sem autoridade), a tensão PT-19/PT-29 (limiar pressupõe ausência de coordenação, e PT-19 afirma coordenação), PT-34 (massa crítica são os organizadores, não a multidão), PT-12A (tipificável nas quatro vias de acesso a recurso), PT-28 (**confirmado**, agora com âncora em português), PT-62 (processo, não mecanismo) e a atribuição dos quatro testes. Detalhadas na seção 4 do documento 09.

### 25.3 Uma lacuna do campo que PT-52 responde

O verbete de RMT encerra dizendo que "**resource demobilization** ... needs further investigation, as it is **currently assumed** that the processes for mobilizing resources are reversed when SMOs fail". PT-52 é um caso em que não se inverte: é interrompido de fora, por remoção coercitiva com decisão judicial. Entrou como quinta lacuna em `08_BIBLIOGRAFIA-METODOLOGICA.md` §3.1.

### 25.4 O identificador impresso na obra não existe

A enciclopédia imprime no rodapé de cada verbete `10.1002/9781405198431.wbespmNNN` — prefixo do ISBN impresso. Os quatro testados retornam **404 no CrossRef**. O que resolve é `10.1002/9780470674871.wbespmNNN`, o do ISBN eletrônico, **que é o que as sínteses automatizadas declaram**. É a primeira vez que a fonte impressa erra o identificador e a síntese acerta. **A regra deixa de ser "confiar na fonte contra a síntese" e passa a ser "testar o identificador, qualquer que seja a origem".** Registrado na `PROCEDENCIA` da obra.

### 25.5 Duas obras que já estavam no corpus e não constavam do inventário com referência completa

`Livro_Process tracing.pdf` é **CUNHA & ARAÚJO (2018)**, Enap — a referência metodológica em português, com o esquema de mecanismo e a definição de condição necessária que PT-28 usa. `process-tracing-research-designs-a-practical-guide.pdf` é **RICKS & LIU (2018)**, *PS*, seção *The Teacher*, a mesma de Collier (2011). Ambas passaram a constar de `Fontes/LEIA-ME_fontes.md` com referência completa. **Nenhuma das duas obras de Beach e Pedersen está no corpus** — nem a de 2013, nem a de 2016, nem a 2ª edição de 2019 que o projeto cita.

**Corpus:** 25 PDFs / 9.139 páginas; **documental inalterado em 20 / 6.819**, que é o que a separação de 29/09 existe para garantir.

---

## Ordem de ataque — revista em 29/09/2026

**A decisão que ordena tudo continua sendo a de 16/08/2026: a redação é o último item.** A ordem anterior a essa data tratava o aparato como suficiente e punha a escrita como ponto de virada; esta trata o conjunto de dados do processo político como pré-requisito.

**A mudança desta revisão é de contabilidade, não de rumo.** A tabela vinha mostrando como abertas quatro tarefas concluídas em 16/08 — o arquivamento web (4), a obtenção do balanço (8) e a reauditoria (11), além da 6. Foram fechadas aqui com a data correta. E entraram as tarefas nascidas das rodadas 19, 20 e 21.

### Fechadas

| # | Tarefa | Item desta agenda | Quando |
|:--|:--|:--|:--|
| 1 | ~~Sincronizar JSON/CSV/XLSX no esquema de 16 campos~~ | 12 | ✅ 16/08 |
| 2 | ~~Aplicar as correções de vínculo e status da auditoria~~ | 12 | ✅ 16/08 |
| 3 | ~~Publicar `AUDITORIA-FONTES.md`~~ | 12 | ✅ 16/08 |
| 4 | ~~Arquivamento web e notícias do STF~~ — seis matérias em `Fontes/09_Arquivamento-web/` | 18 | ✅ 16/08 |
| 5 | ~~Coleta manual: acórdão do TSE (PT-03E)~~ — obtido sem captcha, por rota pública | 11.1, 17 | ✅ 16/08 |
| 6 | ~~Fechar PT-58~~ — e mais que isso: as três decisões da execução penal viraram fonte primária | 7, 18 | ✅ 16/08 |
| 7 | ~~Resolver ou retirar PT-34 — os "4 mil" sem lastro~~ | 7, 13 | ✅ 16/08 |
| 8 | ~~Obter o PDF do balanço "Democracia Inabalada"~~ — chegou pelo pesquisador; PT-53 e PT-61 a fonte primária | 15.1 | ✅ 16/08 |
| 11 | ~~Reincorporar as peças novas ao codebook e reauditar~~ — hoje é `bash scripts/ciclo.sh` | 12, 20 | ✅ 16/08 |
| — | ~~Alinhar o relatório de pesquisa ao codebook (§3.2 e cabeçalho)~~ | 19.1 | ✅ 11/09 |
| — | ~~Corrigir as páginas de PT-58, PT-59 e PT-60 e o `n_subeventos`~~ | 19.2 | ✅ 11/09 |
| — | ~~Reorganizar o diretório e pôr o projeto sob git~~ | 20 | ✅ 20/09 |
| — | ~~Realinhar as duas figuras ao codebook~~ | 21.1 | ✅ 25/09 |
| — | ~~Fechar o buraco: `conferir_figuras.py` no ciclo~~ | 21.3 | ✅ 25/09 |
| — | ~~Reescrever "Próximos passos recomendados" no relatório~~ — parava em 14/08 e contrariava a ordem de 16/08 | 21.4 | ✅ 25/09 |
| — | ~~Fechar o último buraco: `conferir_relatorio.py` no ciclo~~ — achou quatro divergências na primeira execução | 21.5 | ✅ 25/09 |
| — | ~~Varrer `fonte_pagina` contra a prosa dos 82 registros~~ — 8 candidatos, 2 lacunas reais | 21.6 | ✅ 25/09 |
| — | ~~Ancorar as páginas e documentos que PT-15 e PT-28 citavam sem vincular~~ — 4 páginas lidas no PDF antes da correção | 21.6 | ✅ 25/09 |
| — | ~~Endurecer o `conferir_paginas.py`~~ — toda transcrição precisa ser localizada; 2 erros de página achados | 21.7 | ✅ 25/09 |
| — | ~~Verificar os DOIs das sínteses~~ — são **411**, não 325; 3 inexistentes e 1 DOI real no autor errado, **os quatro já com identificador correto** | 22, 22.6 | ✅ 29/09 |
| 9 | ~~Triar por pertinência~~ — 43 na camada A, cobrindo 31 dos 82 registros | 23 | ✅ 29/09 |
| 18 | ~~Acrescentar à mão o cânone de mecanismos~~ — DoC, Tarrow e McCarthy & Zald | 23.6 | ✅ 29/09 |

### Abertas

| # | Tarefa | Item desta agenda | Depende de |
|:--|:--|:--|:--|
| 10 | Acrescentar a literatura clássica brasileira (livros, sem DOI) — as sínteses têm **zero** referências sobre o Brasil | 11.4, 22.4 | — |
| 17 | **Ler na fonte os 43 da camada A** (passo 3 do item 11.3) — **6 lidos**, 7 já tinham ficha, 1 sem camada de texto; a enciclopédia destravou 7 verbetes, e ~26 seguem atrás de muro | 23, 24, 25 | acesso institucional |
| 19 | **Decidir o nome de `mecanismo_causal`** e aplicar as sete cobranças da seção 4 do documento 09 | 24.6, 25.1, 25.2 | decisão sua |
| — | ~~Acrescentar à mão o cânone de mecanismos~~ — os dois livros no eixo 05, McCarthy & Zald como referência; cobertura de A sobe a 31 dos 82 | 23.6 | ✅ 29/09 |
| 13 | Decidir o "Conclusão dos julgamentos" de PT-61 contra as 459 em instrução | 21.4 | decisão sua |
| 14 | Codificar a camada $T_{-1}$ conjuntural — 7 registros ainda contextuais | 11.3, 19 | 9 |
| 15 | Higiene do repositório: licença, remoto, `.backup_pre_lula/`, ponteiros no JSON | 20, 21.4 | decisão sua |
| 16 | **Redação do artigo** | 3, 4, 5, 6, 9, 10 | tudo acima |

**Nenhuma pendência de dado depende de você** — isso vale desde 16/08 e continua valendo. As tarefas 12 a 15 são decisões, não coleta; nenhuma bloqueia a redação, e as três primeiras podem ser tomadas durante a escrita.

**Quando a redação começar**, os itens 3, 4 e 5 desta agenda vêm primeiro: são antecipação de crítica, os pontos que um parecerista atento levantaria, e os que mais mudam o texto. Os itens 6, 9 e 10 são parágrafos de discussão, resolvidos na escrita.

**A lição das três últimas rodadas, que vale como regra de trabalho.** Em 11/09 o relatório estava quase um mês atrás do codebook; em 25/09 as figuras estavam seis semanas atrás. Nos dois casos o JSON estava certo e a peça derivada, errada — e nos dois casos nada avisou, porque o ciclo só cobria o que é gerado por script. **Toda peça escrita à mão que reproduz números do codebook precisa ou virar gerada, ou ganhar uma checagem no ciclo.** As três que existiam — as duas figuras e o relatório — ganharam a sua em 25/09, e a do relatório achou mais três defasagens no primeiro uso. A regra vale para a próxima peça que nascer: se ela repete um número do codebook e ninguém a gera, ela vai envelhecer.
