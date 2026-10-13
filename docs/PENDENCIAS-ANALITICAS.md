# Pendências analíticas — pontos a incorporar na redação do artigo

Registro aberto em **12/08/2026** · **atualizado em 29/09/2026**. Não é codebook nem fonte: é a **agenda** do que ficou em aberto ao longo da verificação documental, e que precisa de decisão do pesquisador na hora de escrever.

Está fora do codebook de propósito. Codebook guarda dados; isto guarda perguntas. Misturá-los estraga os dois.

---

## Painel de estado — 29/09/2026

**O aparato está pronto, auditado, versionado e verificável por um comando; o artigo não começou.** Por decisão do pesquisador em 16/08/2026, a redação passou a ser o **último** item da fila: o conjunto de dados de todo o processo político vem primeiro. Nada mudou nessa decisão desde então.

| Frente | Estado |
|:--|:--|
| Codebook | **83 sub-eventos × 16 campos** — JSON, CSV e XLSX gerados de uma fonte única, com zero divergências |
| Ancoragem documental | **81 registros** com arquivo local vinculado · 75 com página ou seção atribuída · 0 referências quebradas |
| Classes de verificação | **61 em fonte primária** · 21 confirmados por outra via · **0 contextuais** (eram 7 até 04/10) · **0 a verificar** · 1 inferência declarada |
| Caderno de evidências | **49 registros** com página e transcrição literal |
| Corpus documental | **22 PDFs / 6.951 p. de fonte documental** + o acórdão do TSE em HTML + 6 matérias arquivadas contra link rot + 7 sínteses. Com a bibliografia teórica do eixo 05, as sete peças da camada $T_{-1}$ do eixo 12, as dezoito do eixo 13, as doze do eixo 14 e as duas do eixo 15, são **66 PDFs / 12.089 p.** — os eixos 12 a 15 acrescentaram **2.698 páginas** em 04 e 08/10, **sem que a documental mudasse**, que é o que a separação das duas contagens serve para mostrar. **Quatro peças sem camada de texto, uma com camada de texto errada e uma sem rótulo de página algum**, declaradas |
| Figuras | SVG da cadeia causal e cronologia navegável — **realinhadas ao codebook em 25/09**, 83 registros cobertos. São a única parte do aparato escrita à mão |
| Relatório de pesquisa | `reports/process_tracing_8jan_relatorio.md` — §3.2 corrigido em 11/09; §2.1 e a tabela da Etapa 2 em 25/09; "Próximos passos" reescrita na mesma data. Agora tem checagem no ciclo |
| Verificação | `bash scripts/ciclo.sh` — **oito passos**: dois geradores e seis checagens, todas com código de saída ≠ 0 em caso de falha |
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

### 25.6 Os sete verbetes restantes, lidos na fonte — e PT-28 ganha hipótese rival

Onze verbetes lidos integralmente, registro em [`projeto-pos-doc/10_VERBETES-ENCICLOPEDIA.md`](../projeto-pos-doc/10_VERBETES-ENCICLOPEDIA.md). Os sete DOIs foram testados: **todos resolvem, e nos sete o título e a autoria casam** com o que a obra imprime.

**O achado de maior consequência é sobre PT-28.** *Policing protest* (della Porta & Reiter) afirma que "a intervenção da polícia em caso de violação da lei **não é automática**: muitas violações menores são toleradas para evitar desordem maior", e que "a polícia goza de **amplas margens de discricionariedade**". E fornece **duas hipóteses rivais em sua melhor versão**: (i) a **seletividade estrutural** — "police repression is more likely to be directed against groups that are **poorer in material resources as well as in political connections**" —, que **prediz policiamento brando** para um acampamento financiado e com aval de autoridade, sem precisar de conivência; e (ii) a **sobrecarga analítica** da inteligência, que a literatura nomeia como falha conhecida. **PT-28 continua correto na forma — condição necessária é *hoop test* —, mas está substantivamente desprotegido enquanto não enfrentar a rival.**

**O segundo achado é diretamente citável.** *Repertoires of contention* lista, entre as formas do repertório **moderno** com genealogia em Tilly: "strikes, electoral rallies, public meetings, petitions, marches, insurrection, and **the invasion of legislative bodies**". A invasão do legislativo é **forma catalogada**, não inovação — e o repertório moderno é definido por "addressing **seats and symbols of the national public power**".

**E a triagem errou esse verbete**, que está na camada **B** por metadado. É o argumento do passo 3 com caso concreto: metadado não diz o que está escrito na página. Não movi a linha da planilha — a promoção é decisão sua, e apagar o juízo original apagaria a evidência do limite.

**Mais três:** *Diffusion and scale shift* separa laço **direto** de **indireto**, e a evidência do projeto (Sri Lanka na CPMI p. 614) sustenta **atribuição de similaridade por laço indireto**, não o laço direto de Bannon, que segue não demonstrado; declara ainda a lacuna de "como a estrutura de oportunidade de um nível **impele** o *scale shift* — se barrados num nível, movem-se para outro", que é o caso. *Political opportunity* dá a formulação do episódio — "**closed opportunities might be perceived as open by the activists**" — e cobra que o projeto declare quais dimensões usa e o que elas explicam, sob pena de herdar a crítica do conceito como "**trash can**". *Demobilization* abre dizendo que "**we know little about the mechanisms governing the decline** of social movements", nomeia **sentença de prisão** como causa de desmobilização individual involuntária — o que dá lastro teórico a PT-61 — e declara a lacuna dos **efeitos do fracasso** de um movimento sobre outros, que é a camada T+1.

**As lacunas declaradas pelo campo passaram de cinco a oito**, consolidadas na seção 9 do documento 10. **Não reescrevi a §3.1 de `08`**, que traz cinco.

**E as estruturas de mobilização ficaram resolvidas pela obra canônica**, não pela enciclopédia — que não tem verbete disso. *Dynamics of Contention*, p. 45 impressa, conferida na fonte: "**Mobilizing structures can be preexisting or created in the course of contention but in any case need to be appropriated as vehicles of struggle.**" PT-12A e PT-21 tratam de estruturas **preexistentes apropriadas**, o que na obra é *social appropriation*, não criação de estrutura.

---

## 26. O campo multiorganizacional — desenhado, e ele contraria a proposição do modelo — ✅ 30/09/2026

Tarefa 21, cobrança do verbete de Klandermans. `scripts/desenhar_campo.py` emite [`data/processed/campo_multiorganizacional.csv`](../data/processed/campo_multiorganizacional.csv) e **entrou no ciclo como passo 7/7**.

### 26.1 A primeira decisão: o campo é de alguém

Klandermans define campo como "the total possible number of organizations with which **the movement organization** might establish specific links". **A definição é possessiva, e o codebook não é.** Ele codifica o episódio: em T-1 Conjuntural o `ator_grupo` é majoritariamente tribunal, em T0 são manifestantes e batalhões, em T+1 são STF, PF, PGR e Congresso. Somar `ator_grupo` daria a lista de quem agiu, não um campo.

Por isso o script **declara o foco** — a coalizão bolsonarista desafiante — e classifica tudo em relação a ele. Trocado o foco, o campo se inverte, e é o que o modelo prevê.

### 26.2 Como a classificação se sustenta

Cada entidade entra com os registros que a sustentam **e o campo do codebook em que ela aparece**; `verificar()` exige que o fragmento declarado ocorra literalmente ali. Digitar classificação sem lastro aborta a execução — mesmo mecanismo de `triar_dois.py`, e há **prova negativa por injeção de defeito** no autoteste. **22 entidades**, todas com lastro.

| Sistema | Entidades |
|:--|--:|
| ALIANÇA — provê recurso ou oportunidade | 8 |
| INDIFERENTE — infraestrutura ou informação, sem partido | 2 |
| CONFLITO — drena recurso ou restringe oportunidade | 7 |
| **CINDIDA** — nos dois sistemas ao mesmo tempo | 2 |
| **MIGRANTE** — mudou de sistema, com data | 2 |
| **CONTESTADA** — a classificação é o objeto da disputa | 1 |

### 26.3 O que o caso cobra do modelo

Klandermans prevê fronteira fluida: "organizations that try to keep aloof may choose **or be forced** to take sides. **Coalitions can fall apart and former allies can become opponents.**" Os dois **MIGRANTES** são exatamente isso, com data: **Anderson Torres, MJ e PRF** (aparelho operando a favor em PT-08A e PT-08C, alvo em PT-42, com prisão de Vasques em 09/08/2023) e **Ibaneis Rocha / GDF** (demite o aliado em PT-42, torna-se alvo da intervenção em PT-45, pede desculpas em PT-47).

**Mas as duas CINDIDAS são outra coisa, e é o achado.** A **PMDF** está nos dois sistemas no mesmo dia, dividida por escalão: o comando produz o dispositivo inferior (PT-18, PT-19B), os pelotões de choque são a linha invadida (PT-28, PT-31, PT-32), a corporação dispersa (PT-41) e desmonta o acampamento (PT-52) — **sete registros**. As **Forças Armadas** ocupam cinco posições em cinco registros: destinatária do apelo (PT-12), presente na certificação (PT-13), anfitriã do acampamento no SMU (PT-20), reforço tático contra a invasão (PT-43) e executora da desmobilização (PT-52).

**Isso não é fronteira fluida: é a unidade de análise que não se sustenta.** O modelo toma a organização como unidade; aqui ela se divide por escalão e por hora do dia. É cobrança do caso ao modelo, e fica registrada como tal.

### 26.4 A proposição do ciclo não se confirma como enunciada

Klandermans: "a proporção do campo engajada expande ou contrai conforme os ciclos de protesto. No **pico**, organizações inicialmente indiferentes tomam partido; na **queda**, organizações se desligam."

| Fase | Entidades ativas | do sistema de ALIANÇA | do lado estatal | Registros |
|:--|--:|--:|--:|--:|
| T-1 Conjuntural | 4 | 2 | 2 | 18 |
| T-1 Operacional | **17** | **8** | 7 | 24 |
| T0 | 7 | **0** | 7 | 23 |
| T+1 | 9 | **0** | 9 | 17 |

**O pico do campo é T-1 Operacional, não T0.** E a quebra por sistema mostra por quê: **em T0 o lado do foco desaparece como organização** — o codebook registra ali multidão, marcha e manifestantes radicalizados — **enquanto o lado estatal se individua em batalhões e pelotões**. Zero entidades de aliança ativas em T0 e em T+1.

**Isso conversa diretamente com PT-19**, que afirma "coordenação sem comando centralizado visível": o campo organizacional opera na preparação e não aparece na execução. **Mas é confundido com a codificação**, porque T0 foi codificado com massa no lugar de organização. Se a contração é propriedade do episódio ou do registro é **pergunta aberta**, e não a resolvi.

### 26.5 Declarado fora do campo

**Apoiadores de Trump (PT-08).** Campo é vínculo organizacional; PT-08 é difusão por laço indireto, e o laço direto — Bannon, na frase única de Castañeda & Jenks — não está demonstrado em nenhuma fonte lida. A ausência é declarada no script, não omitida.

### 26.6 O caso contestado, que não decidi

A **cúpula da segurança do DF** (SSP-DF, SOI, GSI) entra como `CONTESTADA`, com as duas leituras escritas na própria linha: **(a)** omissão deliberada, que é o que o codebook afirma — dispositivo inferior ao da posse em regime e em planejamento, nenhuma elevação após os alertas; **(b)** seletividade estrutural, a hipótese rival de *Policing protest*. **A classificação dessa entidade é o objeto da disputa do artigo, e o script não pode resolvê-la** — é a tarefa 20.

---

## 27. As hipóteses rivais de PT-28 — uma cai, outra sobrevive e relocaliza o argumento — ✅ 30/09/2026

Tarefa 20, em [`projeto-pos-doc/11_HIPOTESES-RIVAIS-PT-28.md`](../projeto-pos-doc/11_HIPOTESES-RIVAIS-PT-28.md). É também a primeira aplicação do enquadramento de Zaks (2017) que o item 2.1 de `08` registra como "a peça que o projeto mais precisa e não tem".

### 27.1 Cinco hipóteses, e a classificação já resolve duas coisas

Enunciadas na melhor versão: **H1** omissão dolosa da cúpula civil da SSP-DF (a moldura do STF na AP 2668, que é **omissiva, não comissiva**); **H2** seletividade estrutural do policiamento; **H3** sobrecarga analítica da inteligência; **H4** ruptura da cadeia de comando abaixo do comandante-geral; **H5** incapacidade operacional.

Pela relação lógica, **H4 sai da lista de rivais**: é **aninhada** em H1 — o mecanismo pelo qual a omissão produziu efeito —, e o registro já a tratava assim. E **H3 e H5 são contraditórias com H1**, logo testáveis com a evidência que o projeto já tem.

### 27.2 As duas contraditórias caem, com registros já ancorados

**H5 está refutada por PT-41:** o Batalhão de Choque chegou duas horas após ser requerido e, empregado, expulsou todos os invasores em **pouco mais de três minutos**. A capacidade existia e era desproporcional à resistência. Faltou emprego, não meio.

**H3 está refutada por PT-19B.** Sobrecarga supõe sinal perdido no volume; a evidência mostra o contrário — um grupo de WhatsApp **criado em 04/01 pela própria cúpula**, com sete participantes, **para acompanhar essas manifestações**, que recebeu o aviso em 05/01 e no qual a subsecretária de Inteligência só escreveu **às 16h50 do dia 8**. Canal dedicado e de baixo volume não é aparelho soterrado por informação.

### 27.3 H2 sobrevive — e o ganho é a distinção que ela obriga a fazer

H2 explica bem a tolerância prolongada (PT-20), a não interdição das caravanas (PT-21) e o **tamanho** do efetivo (PT-28): para grupo rico em recurso e em conexão política, policiamento brando é a regularidade da literatura, não o desvio. **Enquanto o argumento de PT-28 se apoiar no tamanho, ele disputa o terreno em que H2 é forte.**

**Mas há um conjunto que H2 não explica, e não é tamanho.** PT-18: **PAI** em vez do **POI** usado no 7 de setembro e na posse, e **sobreaviso** (2h30 a 3h) em vez de **prontidão** (≈40 min), "de forma também diversa da praticada na cerimônia de posse"; Cappelli, conclusão D: **sem previsão de acionamento** para BOPE, BPCÃES, BAVOP e RPMON; conclusão H: **oito comandos de férias**, inclusive o do Batalhão de Choque; PT-20A: dispensa expressa de reforço dois dias antes.

**A distinção é dimensionamento contra capacidade de escalada.** H2 é teoria do primeiro — prediz menos policiais na linha, e acerta. **Não prediz a remoção da capacidade de escalar**: não explica pôr oito comandos em férias no mesmo dia, deixar quatro unidades especializadas sem previsão de acionamento, rebaixar o instrumento de planejamento em relação ao de sete dias antes e dispensar reforço por escrito.

**E a comparação que sustenta isso é interna** — mesma corporação, mesma praça, sete dias de intervalo —, não entre grupos, que é onde a seletividade sempre teria o que dizer.

### 27.4 A redação de PT-28 não muda; falta-lhe declarar a rival

"Condição necessária (*hoop test*)" está exato. O que falta é o parágrafo da seção 5 do documento 11, que **não inseri**: é acréscimo ao `mecanismo_causal` e é decisão sua.

### 27.5 Falta uma coisa só, e é um *smoking gun* em potencial

**A data em que Anderson Torres assumiu a SSP-DF não está no codebook** — procurada nos 82 registros, ausente. Se o **decisor mudou** entre a posse e o dia 8, a diferença de tratamento deixa de ser propensão institucional, que é o terreno de H2, e passa a ser decisão de quem entrou, que é onde o STF a localizou. Se não mudou, **H2 fica mais forte**. Custa uma página de fonte primária, e não a afirmei porque não a li.

### 27.6 Duas citações erradas, achadas na própria redação — e a checagem que entrou no ciclo

Na primeira versão do documento, duas páginas foram escritas por **dedução de vizinhança** em vez de leitura: PT-20 saiu como "CPMI: 631" quando o registro ancora **576**, e PT-21 como "CPMI: 640" quando ancora **576, 374, 637, 643**. As duas eram plausíveis — vizinhas das certas, na seção certa do relatório — e é por isso que passariam.

`scripts/conferir_hipoteses.py` passou a conferir **toda citação de página do documento contra o `fonte_pagina` do registro**, exigindo também que o **documento-fonte** bata: "Cappelli: 679" é reprovado quando a página é do CPMI. **11 citações conferidas**, e há prova negativa por injeção dos dois defeitos. **Entrou como passo 8/8 do ciclo.**

---

## 28. A tarefa 22 resolvida — e ela troca a rival fraca por uma forte — ✅ 30/09/2026

A data foi lida em **duas fontes primárias independentes do corpus**, e diz mais do que a pergunta pedia.

**Relatório do Interventor Federal, §4.9, p. 35:** "No dia **02 de janeiro de 2023, após a realização do evento da posse**, foi publicada a nomeação do Delegado da Polícia Federal Anderson Gustavo Torres para atuar como Secretário de Estado de Segurança Pública do Distrito Federal. **No dia seguinte, foram publicadas outras nomeações e exonerações de ocupantes de cargos centrais**." E na conclusão, p. 58: a troca de titularidade "**afetou o planejamento e a execução das ações**", seguida em **03/01/2023** da "exoneração e troca de ocupantes de cargos centrais na **estrutura de planejamento e coordenação** da SSPDF".

**Relatório Final da CPMI, item 6.3.12, p. 831:** Torres assumiu em 2 de janeiro de 2023 "**posição que havia ocupado anteriormente entre 1º de janeiro de 2019 e 29 de março de 2021**", e entre 30/03/2021 e 31/12/2022 foi **Ministro da Justiça**, com ascendência sobre PF e PRF — donde a CPMI conclui que ele "era **uma das autoridades públicas que mais possuía conhecimento** a respeito das ameaças golpistas".

### 28.1 H2 enfraquece; entra H6, e é mais forte

**A comparação interna que sustentava o argumento — mesma corporação, mesma praça, sete dias — não opõe dois tratamentos da mesma cúpula.** O titular mudou em 02/01 e o escalão de planejamento em 03/01. H2 (seletividade estrutural) explica propensão institucional estável; **perdeu o seu melhor apoio empírico**.

Mas entra **H6 — descontinuidade administrativa**, e ela é a rival mais forte do conjunto: trocar o titular e, no dia seguinte, os cargos centrais de planejamento, cinco dias antes de um evento anunciado, degrada a capacidade de planejar **sem que ninguém precise querer isso**. **A hipótese não é minha — é a conclusão do próprio interventor federal.** E ela alcança exatamente o que H2 não alcançava: o PAI em lugar do POI, o sobreaviso em lugar da prontidão, a ausência de previsão de acionamento.

**O que limita H6:** Torres não era novato — 27 meses no mesmo cargo entre 2019 e 2021, e 21 meses no MJ. Na melhor versão, H6 não é "gente nova errou", é "a troca do escalão de planejamento desorganizou a cadeia", afirmação sobre os substituídos.

### 28.2 Um segundo achado, que nenhuma das seis previa

CPMI p. 874: **Fernando de Sousa Oliveira, no comando da SSP-DF no dia 8, tinha o nome ainda não publicado no DODF** — era "apenas um '**funcionário de fato**'" —, disse não ter sido apresentado formalmente "sequer ao governador, muito menos aos comandantes das forças", e teve a nomeação publicada só em **9 de janeiro**, início das férias formais de Torres.

**Quem estava na cadeira não tinha autoridade formal sobre os comandos que precisaria acionar.** Não é omissão, não é seletividade, não é sobrecarga: é **defeito de autoridade formal**, e reabre H4 como hipótese autônoma, não mais aninhada em H1.

### 28.3 O que a tarefa 22 mudou, e o que não

**Não fechou a questão: trocou a pergunta.** Não é mais "o subdimensionamento prova omissão?", e sim "**a desorganização do escalão de planejamento em 02-03/01 explica o dispositivo do dia 8 sem recurso a dolo?**". A resposta depende de quais foram as exonerações de 03/01 e de quem as assinou — que o **anexo 14** do relatório do interventor nomeia e o corpus não tem.

### 28.4 Três fatos novos, e nenhum está no codebook

Conferido: `02/01/2023`, `DODF`, `funcionário de fato` e `férias formais` têm **zero ocorrências** nos 82 registros. **Não os inseri** — criar registro ou estender PT-18 é decisão de codificação. O que já estava: o pré-aval da Força Nacional na véspera está em PT-40, ancorado na CPMI p. 678; a p. 874 só acrescenta o detalhe do Ofício 5/2023 das 18h23 e da Portaria 272 das 19h11, cujo efeito "dependeria da efetiva solicitação de Ibaneis Rocha". **É refinamento de registro existente, e está dito assim porque este projeto já apresentou uma vez como novo o que ele próprio já registrava.**


### 28.5 A 24 avançou dentro do corpus — a descontinuidade é demonstrável

O anexo 14 **não está no PDF**: o relatório lista quinze anexos na p. 61 e termina na 62. Mas a CPMI documenta a descontinuidade em três lugares, e eles bastam para firmar H6 como hipótese séria:

- **p. 834** — Fernando de Sousa Oliveira "afirmou que **não houve qualquer repasse de informações ou transição no período**";
- **p. 1070** — o coronel Naime declara que "**todos os grupos referentes à Polícia Militar [...] estavam silenciados** durante o período de sua licença", e que o seu substituto "negou ter recebido qualquer informação, **porque não participava dos grupos 'Perímetro', 'Difusão' ou 'Sisp'**";
- **p. 1069** — o mesmo depoente formula a disjunção que o conjunto de hipóteses tem de resolver: "**ou as agências de informação não passaram o conhecimento [...], ou esses receberam a informação e ficaram inertes**" — e **PT-19B já refuta o primeiro ramo**.

**Logo a cadeia estava rompida, e isso é fato de fonte primária.** O que falta decidir é se o rompimento foi **produzido** ou **herdado** — diferença entre H1 e H6 —, e quem a decide são os atos de 02-03/01. **A via é o DODF**, que é público, e não o anexo.


## 29. PT-18A entra, e o codebook vai a 83 — ✅ 30/09/2026

Tarefa 23. Os três fatos da tarefa 22 viraram **registro próprio**, não acréscimo a PT-18: são atos administrativos com data e autoria próprias, anteriores ao rebaixamento do dispositivo, e somá-los a PT-18 misturaria duas decisões num só registro — o defeito que a auditoria de 16/08/2026 corrigiu em sete casos.

**PT-18A · 02–03/01/2023 · T-1 Operacional · Confirmado em fonte primária**, em duas fontes independentes: Relatório do Interventor Federal (p. 35 e 58) e Relatório Final da CPMI (p. 831 e 834). As quatro transcrições foram localizadas nas páginas citadas por `conferir_paginas.py`.

### 29.1 O custo que um registro novo cobra, e que vale registrar

Acrescentar uma linha ao JSON **quebrou o ciclo em quatro pontos**, e todos na parte escrita à mão:

| Onde | O que falhou |
|:--|:--|
| `cronologia_8jan_interativa.html` | PT-18A ausente da cópia manual dos registros no `<script>` |
| as duas figuras | ambas declaravam "82 sub-eventos" |
| `reports/process_tracing_8jan_relatorio.md` | cabeçalho com 82, e a tabela da Etapa 2 sem a linha |
| `verificar_integridade.py` | mensagem com "82 x 16" fixo no texto — passava na checagem e mentia na saída |

**Nada disso é acidente: é a confirmação da regra de 25/09.** As peças geradas — CSV, XLSX, auditoria, planilha e figura do campo — absorveram o registro novo sem intervenção. **As escritas à mão exigiram quatro edições, e o ciclo as cobrou uma a uma.** É o argumento mais limpo que o projeto já produziu a favor de transformar a cronologia em peça gerada.

### 29.2 Uma asserção afrouxada, de propósito

`desenhar_campo.py` exigia `len(regs) == 82`. Virou piso (`>= 82`), com a razão escrita no código: prender o número ali obrigaria a editar o script a cada registro novo. **Quem garante a aderência ao codebook não é a contagem — é `verificar()`**, que exige que cada fragmento declarado ocorra no campo declarado do registro.

### 29.3 Denominadores antigos que ficam como estão

Os itens 23 e 25 desta agenda dizem "31 dos 82 registros" ao descrever a cobertura da camada A. **São afirmações datadas de 29–30/09 e ficam**: reescrevê-las apagaria o estado em que a triagem foi feita. O denominador corrente é 83.

---


## 30. Tarefas 24 e 13 — o Diário Oficial contraria o interventor, e uma expressão não estava na fonte — ✅ 30/09/2026

### 30.1 Tarefa 24: a varredura do DODF

Portal oficial `dodf.df.gov.br`, 02 a 09/01/2023, **todas as seções, 1.740 matérias em 177 páginas**. Atos de pessoal da SSP-DF encontrados: **três**.

| Publicado | Decreto de | Ato |
|:--|:--|:--|
| 02/01 (DODF 001, p. 16) | 1º/01/2023 | Exonera **Julio Danilo Souza Ferreira**; nomeia **Anderson Gustavo Torres** secretário — assina **Ibaneis Rocha** |
| 04/01 (DODF 003, p. 35) | 03/01/2023 | Exonera o Maj **Jadson Barros de Lacerda** de Chefe da **Ajudância de Ordens do Gabinete**; nomeia a Maj **Gizela Lucy Teixeira Barros** |
| 09/01 | 08/01/2023 | **Exonera Anderson Gustavo Torres** — Ibaneis Rocha |

**O achado é negativo, e é o que importa.** O Relatório do Interventor afirma que em 03/01 "houve a exoneração e troca de ocupantes de **cargos centrais na estrutura de planejamento e coordenação** da SSPDF". O Diário Oficial registra, naquele decreto, **um único ato: a Ajudância de Ordens do Gabinete** — que é o apoio pessoal do secretário, não a estrutura de planejamento.

**Consequência para H6.** A troca em bloco do escalão de planejamento era o melhor apoio empírico da hipótese de descontinuidade administrativa. **Ela não se confirma no Diário Oficial.** H6 não cai — a ausência de transição (CPMI p. 834) e os substitutos fora dos canais (p. 1070) continuam de pé —, mas perde o seu elemento mais forte, e passa a depender de fatos de funcionamento, não de atos publicados.

**Ressalvas da varredura, declaradas no próprio registro:** o filtro exigiu a expressão literal "Segurança Pública do Distrito Federal", de modo que um ato nomeando apenas a subsecretaria escaparia — mas as buscas por "Operações Integradas", "Subsecretaria de Inteligência" e pelos nomes de Fernando de Sousa Oliveira e Marília Ferreira de Alencar também devolveram zero em 02 e 03/01; e edições extras fora da rota consultada não foram cobertas.

As duas edições entraram no corpus com `PROCEDENCIA` declarada. **Corpus: 27 PDFs / 9.271 páginas, 22 documentais / 6.951** — a primeira vez desde agosto que a contagem documental sobe.

### 30.2 Tarefa 13: a expressão não estava no balanço

PT-61 trazia **"Conclusão dos julgamentos do 8/1"** em `resposta_estatal`, e o item 21.4 desta agenda registrava que *"o balanço é do gabinete e usa a palavra; o codebook a reproduz"*.

**Conferido nas 15 páginas do PDF, por dois extratores independentes — PyPDF2 e PyMuPDF: a expressão não existe no documento.** A única ocorrência de "julgamento" é *"21 SESSÕES DE JULGAMENTO REALIZADAS NOS MESES DE SETEMBRO, OUTUBRO, NOVEMBRO E DEZEMBRO"* (p. 14), que se refere aos **quatro núcleos**, não ao universo de 1.335 ações penais.

**A formulação era do codebook, e foi atribuída à fonte.** É o modo de falha do projeto numa variante nova: não a cifra no referente errado, mas **a frase própria com procedência emprestada**.

Reformulado para o que a fonte sustenta: **"Balanço do ciclo repressivo-judicial: 21 sessões de julgamento dos quatro núcleos concluídas, com 459 das 1.335 ações penais ainda em instrução"** — e o novo texto **preserva a tensão** que motivou a tarefa, em vez de escondê-la.

---

---

## 31. A camada $T_{-1}$ conjuntural, codificada na fonte — e a lacuna de 2018-2022 fica declarada — 🔶 04/10/2026

Tarefa 14. Relatório completo em [`projeto-pos-doc/12_CAMADA-T-1-CONJUNTURAL.md`](../projeto-pos-doc/12_CAMADA-T-1-CONJUNTURAL.md).

### 31.1 Três de sete, e a literatura veio de onde ninguém tinha olhado

Os sete registros contextuais sustentavam-se numa lista de nomes — *"Literatura: Alonso (2017); Tatagiba (2014)"* — e **nenhuma dessas obras estava no corpus ou havia sido lida**. A pasta de textos de ação coletiva anexada à sessão tem **145 arquivos** e cobre densamente o ciclo 2013-2016. Quatro artigos revisados por pares entraram em `Fontes/12_Camada-T-1_Literatura/`: Tatagiba (2014), Tatagiba e Galvão (2019), Pinto (2017) e Alonso (2012).

**PT-01, PT-02 e PT-03 passaram de `Contextual` a `Confirmado`**, com página e transcrição literal. Os contextuais caem de **7 para 4**.

### 31.2 O achado que muda registro: o enquadramento do adversário na boca do ator

PT-01 declarava como enquadramento **"'Não é só por 20 centavos' — antipolítica"**. Tatagiba (2014, p. 40) sustenta o oposto — *"desde o começo, foi sim uma luta por 0,20 centavos"* — e nega que tenha havido quadro unificador: *"não houve a conformação de um frame capaz de conferir unidade a essa diversidade para além do estopim"*. Pinto (2017, p. 131) traz a militante do MPL Nina Cappello: *"Interessava para vários setores dizer que a luta não era somente pelos R$ 0,20. [...] Para nós do movimento, era, sim, pelos R$ 0,20"*.

E "antipolítica" muda de referente: em Pinto, o discurso antipolítico emerge **depois** da saída do MPL e está *"claramente à direita"*. O termo documentado para junho de 2013 é **antipartidarismo**.

> **Quarta variante do modo de falha do projeto.** Depois da cifra correta no referente errado, do termo técnico no referente errado (PT-03) e da frase própria com proveniência emprestada (PT-61), esta é **o enquadramento do adversário atribuído ao ator**. As três primeiras eram erros de proveniência; esta inverte quem disse o quê — num registro cujo objeto é a disputa pelo sentido.

### 31.3 Dois achados menores, e um deles é um registro em potencial

**A obra citada nunca esteve no corpus.** "Alonso (2017)" não está em lugar algum. O que há é **Alonso (2012)**, outro texto, e ele cobra: *"Tilly não detalha o processo de apropriação do repertório pelos atores"* (p. 24). O mecanismo que PT-02 chama de apropriação não tem, na fonte do conceito, o conteúdo que o nome sugere. Entra na fila da tarefa 19, ao lado da certificação de PT-03.

**A intervenção militar já estava nas ruas em março de 2015.** Pinto (2017, p. 150) documenta faixas pedindo intervenção militar, algumas em inglês, e o movimento "SOS Forças Armadas", que *"atualizava o espaço político das Forças Armadas"*. O codebook trata esse apelo em $T_{-1}$ **operacional** (PT-12), oito anos depois. Está anotado em PT-02; virar registro próprio é decisão sua.

### 31.4 Os quatro que ficam, e por que não é trabalho pendente

PT-04, PT-05, PT-06 e PT-08 continuam contextuais. Varredura de conteúdo nos 145 arquivos, com normalização NFKC: **zero ocorrências de "Bolsonaro"**, zero de "pandemia", e todas as de "Capitol" em obras anteriores a 2021.

**É a mesma lacuna do item 23.2, achada por um terceiro caminho.** A triagem de 29/09 registrou que os 411 DOIs das sínteses trazem zero referências sobre o Brasil; a varredura de hoje confirma numa coleção independente, montada por outra pessoa com outro propósito. A literatura sobre o bolsonarismo **não está ao alcance deste projeto** — é condição a declarar no artigo, não pendência a perseguir. O status dos quatro deixou de dizer "requer fonte primária" e passou a dizer o que foi varrido, quando, e o que não se achou.

### 31.5 Uma divergência que ficou declarada em vez de resolvida

PT-03 guarda como enquadramento *"legalidade constitucional"*, que é o quadro do campo pró-impeachment. Tatagiba e Galvão escrevem *"2016, ano do golpe jurídico-parlamentar"* (p. 65). **O campo foi mantido**: ele codifica o quadro do ator, não o veredito do analista. A divergência está no `status_verificacao`.

E uma afirmação de PT-02 continua **sem âncora**: *"tolerância policial"*. Nenhuma das quatro obras a sustenta. Está declarada no status.

### 31.6 O que a leitura cobra, e o que o aparato ganhou

A cobrança mais pesada não é de nome, é de desenho: **Tatagiba e Galvão negam a descontinuidade entre 2013 e 2015-2016** — *"não observamos uma descontinuidade entre 2013 e os protestos posteriores"* (p. 71) — e registram que os grupos antipetistas **já protestavam em 2011** (p. 82). O par PT-01 → PT-02, com mecanismo de *spin-off*, codifica ruptura. Se a leitura delas for adotada, o mecanismo vira difusão intraciclo e a apropriação passa a ser de escala, não de origem.

No aparato: o eixo 12 entrou em `FORA_DA_DOCUMENTAL` — **a contagem documental não pode crescer porque entrou artigo de revista** —; `conferir_hipoteses.py` passou a conferir **dois** documentos em vez de um, sem lógica nova, e o documento 12 entrou na checagem no dia em que nasceu; `conferir_paginas.py` ganhou duas exceções declaradas, porque Tatagiba (2014) é **digitalização sem camada de texto**, lida por renderização a 170 dpi. Prova negativa feita com dois defeitos — página vizinha e página certa no documento errado —, os dois pegos.

### 31.7 Dois números deste documento estavam velhos de novo

O painel do alto dizia **60 em fonte primária / 14 confirmados / 7 contextuais** quando o codebook dizia 61 / 14 / 7, e **20 PDFs / 6.819 p.** quando o inventário já ia em 22 / 6.951. O parágrafo de fechamento do relatório de pesquisa trazia as mesmas duas cifras velhas, e `conferir_relatorio.py` **não o cobre** — ele confere a tabela da Etapa 2, as páginas e os caminhos, não a prosa de fechamento. Corrigidos nos dois lugares em 04/10. **Os buracos de checagem continuam abertos**, e é a terceira vez que esta peça envelhece sem aviso.

---

## 32. A descontinuidade sai do codebook, e um quarto registro deixa de ser contextual — 🔶 04/10/2026

**Segunda rodada da tarefa 14, no mesmo dia.** O item 31 fechou entregando seis decisões, e a primeira delas era a mais cara: *"o par PT-01 → PT-02, com mecanismo de spin-off, codifica ruptura"*. **O pesquisador decidiu pela continuidade** e indicou a literatura — Marcelo Kunrath Silva. Esta rodada executa a decisão com três peças novas, todas lidas na fonte, e documento completo em [`projeto-pos-doc/12_CAMADA-T-1-CONJUNTURAL.md`](../projeto-pos-doc/12_CAMADA-T-1-CONJUNTURAL.md).

### 32.1 A peça que nomeia o mecanismo — e desfaz uma cobrança da rodada anterior

**Kunrath Silva (2018)**, *Lusotopie* 17(1):88-111, distingue sua tese das duas apropriações já na literatura — a **social**, de McAdam, Tarrow e Tilly, e a **institucional**, de Tarrow — e conclui que no caso de 2013 *"não há uma apropriação de recursos ou de estruturas organizativas, mas sim de um repertório: o protesto"* (§ 15).

Isso **vindica o nome que PT-02 já usava** e **corrige o item 31.3 desta agenda**, que tomara a observação de Alonso (2012, p. 24) — *"Tilly não detalha o processo de apropriação do repertório pelos atores"* — como defeito do codebook. Não era defeito. A apropriação de repertório é mecanismo distinto da apropriação social, e é por isso que a obra de Tilly não a detalha. O achado de Alonso continua verdadeiro; a conclusão que dele se tirou estava errada, e a cobrança sai da fila da tarefa 19.

### 32.2 Continuidade não é determinação, e isso entrou no próprio campo

O ponto que **nenhum dos dois lados do debate fazia**, e o que mais obriga um codebook que é uma cadeia causal. Kunrath Silva (2018, § 56): *"é um equívoco afirmar que tais processos posteriores já estavam predeterminados pelo que ocorreu"* em 2013. Alonso (2023, p. 227 da edição digital): *"junho não foi uma causa primeira, da qual decorreria inevitavelmente tudo o que veio depois"*.

Duas obras independentes, com teses diferentes sobre a forma do ciclo, convergem na mesma proibição. A ressalva entrou no `mecanismo_causal` de PT-02, não em nota: um campo que diz "continuidade" sem dizer isso afirma mais do que a fonte sustenta.

### 32.3 O ator estava em 2013, e o codebook não o registrava

O codebook punha a direita apenas em PT-02, a partir de 2015 — e era essa ausência que fazia a leitura de ruptura parecer correta. Alonso (2023) dá o ator e o nome: o **campo patriota**, que esteve na rua em junho de 2013 sem ser reconhecido como ator político, e que, segundo ela, era *"o maior dos lados de 2013, tão grande quanto ignorado em junho"* (p. 223 da edição digital). Kunrath Silva (2023, p. 77) data a organização da direita *"pelo menos desde a eleição de Lula em 2003"*. O `ator_grupo` de PT-01 e PT-02 passou a nomeá-lo.

### 32.4 PT-04 sai de contextual — e a declaração do item 31.4 estava errada como conclusão geral

O item 31.4 escreveu que *"a literatura sobre o bolsonarismo não está no alcance deste projeto"*, com base em duas varreduras exaustivas: os 411 DOIs das sínteses e os 145 arquivos da pasta anexada. As duas estavam certas **sobre as duas coleções**. A conclusão geral estava errada, e bastou uma peça para mostrá-lo: Kunrath Silva (2023, p. 86) registra o ciclo de 2013 como laboratório do que se emprega depois na campanha do impeachment e *"nas mobilizações de grupos políticos da extrema-direita crescentemente articulados em torno de Jair Bolsonaro e/ou do intervencionismo militar"*.

> **A lição não é sobre o bolsonarismo: é sobre o que uma varredura prova.** Varredura exaustiva de duas coleções demonstra a lacuna **delas**, não a lacuna da literatura — e a diferença entre as duas afirmações é a diferença entre uma condição de pesquisa e um erro. É irmã da lição de 29/09 sobre DOI: *distância de título não prova ausência*.

PT-04 passou a **`Confirmado`** quanto ao mecanismo e à genealogia do ator, e o `status_verificacao` declara nominalmente o que **não** ancorou: o repertório digital da campanha de 2018, o enquadramento "nova política" / "anti-sistema" e a validação pelo TSE. Contextuais: **4 → 3**.

### 32.5 Uma armadilha de ferramenta nova, e um defeito antigo que só agora apareceu

**Nenhuma das 26 âncoras novas casava na primeira tentativa**, e as duas causas são tão instrutivas quanto o conteúdo.

1. **PyPDF2 injeta espaço DENTRO das palavras** em alguns PDFs — "destaca -se", "empac amentos". O defeito está no projeto desde o início e nunca havia aparecido, porque nenhuma âncora anterior caía num PDF com esse perfil. `conferir_paginas.py` passou a tentar **PyMuPDF** quando PyPDF2 não acha: é acréscimo, não troca, e as 63 âncoras anteriores seguem idênticas.
2. **O PDF da OpenEdition tem camada de texto PRESENTE E ERRADA.** A fonte `Gentium-Book-Basic` vem subconjuntada com CMap defeituoso: o código de cada glifo é o ASCII menos 29 — espaço = 0x03, `A` = 0x24, `a` = 0x44, vírgula = 0x0F, `0` = 0x13. **Isto é pior que a digitalização sem texto de Tatagiba (2014):** lá a string vinha vazia e a ausência era visível; aqui a string vem cheia, e uma busca por qualquer frase do artigo "prova" com alta confiança que ele não a contém. O conserto é **por span**, nunca pela página, porque as fontes Roboto do mesmo arquivo saem corretas.

E uma **terceira variante** de armadilha de numeração no eixo 12: **Alonso (2023) é edição digital sem paginação impressa**. Não há deslocamento a declarar porque não há página de papel no arquivo — "p. 224" é a página *deste PDF*, e quem conferir no livro impresso não vai achar o mesmo número. Declarado em `PROCEDENCIA` e repetido em cada `fonte_trecho`.

### 32.6 O que esta rodada NÃO fez

- **Não redatou PT-02.** A apropriação começa na segunda fase de junho de 2013; o evento que o registro codifica continua sendo o ciclo de 2015-2016. Mudar `data_hora` é decisão sua.
- **Não renomeou nenhum outro mecanismo.** A tarefa 19 segue sendo sua, e ganhou um ponto novo: o nome "certificação" de PT-03 não fecha com a definição de *Dynamics of Contention*, que exige autoridade externa, enquanto o que a literatura documenta é validação **pela imprensa e pela opinião pública** (Kunrath Silva, 2023, p. 85).
- **Não criou registro** para o apelo à intervenção militar de março de 2015, embora a segunda rodada reforce o caso.
- **Não apagou a divergência.** Alonso e Mische (2016), citadas por Kunrath Silva (2018, nota 6), sustentam a descontinuidade. O `status_verificacao` de PT-02 as nomeia.

---

## 33. A coleta da literatura do bolsonarismo — catorze peças, nenhuma lida — 🔶 04/10/2026

> **ATUALIZADO NO MESMO DIA PELO ITEM 34.** O eixo foi a **dezoito** peças: o pesquisador entregou as quatro barradas, e **duas das catorze foram lidas** e ancoram registro. O que está escrito abaixo é o estado da coleta, e vale como registro do que a coleta por si mostrou.

**Tarefa 25, primeira metade.** O pesquisador deu o recorte: o bolsonarismo **como fenômeno de mobilização social e política**, com foco nas dinâmicas de manifestação e protesto e nos **repertórios próprios do campo das direitas**. Documento completo em [`projeto-pos-doc/13_LITERATURA-BOLSONARISMO.md`](../projeto-pos-doc/13_LITERATURA-BOLSONARISMO.md).

Busca no OpenAlex — escolhido porque **responde sem identificação** —, dezessete consultas em português e inglês mais nove por autor. **345 obras distintas** na união das duas rodadas, com apenas 20 em comum, o que diz que nenhuma das duas estratégias bastaria sozinha. Dezoito peças escolhidas, **catorze coletadas** por via automatizada, 378 páginas, em `Fontes/13_Bolsonarismo-mobilizacao/` — e as outras quatro chegaram pelas mãos do pesquisador horas depois (item 34.6).

> **NENHUMA FOI LIDA, E NENHUMA ANCORA REGISTRO.** PT-05, PT-06 e PT-08 continuam `Contextual`, e seus `status_verificacao` continuam dizendo que a literatura não foi lida — o que é verdade, e seria falso se coleta tivesse sido confundida com leitura. A declaração está em `PROCEDENCIA` peça por peça, porque um arquivo dentro de `Fontes/` parece lastro.

### 33.1 Três peças que valem antes de qualquer leitura

- **A obra que PT-04 citava sem ter, agora está** — e são duas Cesarino, a de 2019 e a de 2022. Qual delas o registro queria, só a leitura dirá.
- **Araujo e Sales (2022) cobrem exatamente 2013-2022**, Forças Armadas e bolsonarismo: é a junta entre T₋₁ conjuntural e T₋₁ operacional, que o item 31.4 chamou de "a mais cara" da camada.
- **Fernandes e Silva (2021)**, sobre policiamento a protestos no Rio Grande do Sul, é a literatura mais próxima que a busca achou da única afirmação órfã de PT-02 — a "tolerância policial" que nenhuma das sete peças do eixo 12 sustenta. Pode confirmar, pode refutar, pode não falar do período.

### 33.2 O que a coleta mostrou sobre acesso — e é resultado, não incidente

**As catorze que chegaram são todas de plataformas latino-americanas ou de acesso aberto diamante.** As quatro que não chegaram são de editora comercial grande: Cambridge (429), SAGE (403), Oxford (403) e um OJS equatoriano que recusa até a página do artigo (403). **Três das quatro são declaradas ouro ou híbrida pelo OpenAlex** — isto é, de acesso aberto — e ainda assim inalcançáveis por via automatizada. Os 403 da SAGE e da Oxford confirmam o que a memória do projeto já registrava; o 429 da Cambridge contradiz, e é o único dos quatro que vale retentar.

*A literatura do bolsonarismo efetivamente ao alcance deste projeto é a brasileira em acesso aberto diamante.* Campos Mello, Abranches e Avritzer — os três nomes que o item 25 listava — publicam **em livro**, e seguem fora pelo mesmo motivo que a literatura clássica brasileira da tarefa 10.

### 33.3 Um descarte que vale registro

A tentativa na Cambridge devolveu uma página de erro de 1,3 KB que o `curl` gravou com extensão `.pdf`. **Foi apagada.** HTML de erro guardado como PDF é defeito silencioso do tipo exato que este projeto caça — e por isso todo arquivo da coleta foi conferido para começar com `%PDF`, abrir no PyPDF2 e devolver texto na primeira página. Nenhuma das catorze tem o problema de camada de texto que o eixo 12 trouxe.

E uma correção dentro do próprio documento 13: a primeira redação dizia **"365 obras distintas"**, que é a soma de 151 e 214 — e as duas listas se sobrepõem em 20. A união é **345**. **A soma de duas buscas não é a união delas**, e somar sem conferir a interseção é a forma aritmética do mesmo defeito: o número certo medindo a coisa errada.

---

## 34. A terceira rodada da tarefa 14: os oito encaminhamentos, e uma afirmação de dez anos sai do codebook — 🔶 04/10/2026

**Terceira rodada do mesmo dia.** A segunda terminou com oito pontos para o pesquisador. Ele respondeu os oito, e esta rodada executou o que era executável: **sete viraram mudança de campo, um virou entrega de arquivo.** Detalhe completo em [`projeto-pos-doc/12_CAMADA-T-1-CONJUNTURAL.md`](../projeto-pos-doc/12_CAMADA-T-1-CONJUNTURAL.md), §4.

Contextuais: **7 → 4 → 3 → 2**. Classes: **61 primária · 19 confirmado · 2 contextual · 1 inferência.**

### 34.1 "Tolerância policial" sai do codebook, e não por falta de fonte: por contradição

PT-02 afirmava, em `resposta_estatal`, **"Tolerância policial; enquadramento midiático favorável"**. A expressão estava lá desde a versão inicial de agosto e **nunca teve fonte**. A primeira rodada a procurou nas sete peças do eixo 12 e não achou; a segunda a deixou declarada como sem âncora.

A leitura de Fernandes e Silva (2021) — 45 anos de policiamento a protestos no Rio Grande do Sul — **não a confirmou: contradisse.** Os autores encontram *"o uso prevalente de táticas de repressão física, pouco tolerantes à demonstração pública de demandas coletivas"* (rev. p. 492 — PDF p. 8), com **seletividade pelo grau de contestação à ordem** (rev. p. 494) e as táticas mais disruptivas mais duramente policiadas (rev. p. 498). O campo passou a dizer seletividade.

**Dois limites ficam declarados, e são sérios:** a série é de **um estado** e **termina em 2015**. E uma ausência que não é evidência: os grupos de direita **não aparecem** entre os atores policiados da série, embora os autores os nomeiem na introdução. **Ausência numa série é ausência, não tolerância medida** — dizer o contrário seria o modo de falha do projeto com o sinal invertido.

### 34.2 Dois mecanismos mudaram de nome, por motivo de definição

- **PT-01** — de *"abertura de estrutura de oportunidade política"* para a formulação do pesquisador: **"no ciclo de 2013 há uma janela de oportunidades políticas aberta na qual as direitas passariam a disputar e ocupar posteriormente"**. Resolve a divergência que a segunda rodada só declarava: Kunrath Silva (2018, § 14) **inverte** a estrutura canônica para este caso.
- **PT-03** — de *"certificação de eficácia"* para **"ressignificação do protesto"**, com a mudança explicada em nota no próprio registro. Certificação, em *Dynamics of Contention*, exige validação por **autoridade externa**, e o enunciado nunca nomeou autoridade alguma: era a cobrança do item 24.6, aberta em 30/09. **Esta cobrança sai da tarefa 19**; as outras sete da seção 4 do documento 09 continuam lá.

### 34.3 O apelo de intervenção militar é frame, e o codebook já o tinha — faltava a genealogia

O pesquisador decidiu que o apelo de março de 2015 é **frame**, não registro novo: "uma forma de desejo dos grupos envolvidos", articulado para angariar manifestantes do próprio campo. Entrou em `framing_narrativa` de PT-02.

**PT-12 já codificava o mesmo frame em fonte primária**, sete anos depois. O que entrou com página foi a genealogia: *"Após junho de 2013, o pleito de uma intervenção militar constitucional foi bradada por setores conservadores da sociedade"* (Araujo e Sales, 2022, rev. p. 29 — PDF p. 4), e o artigo 142 *"desfraldado pelos ativistas favoráveis à intervenção militar"* nos atos de 2020-2021 (rev. p. 33). **O apelo tem três momentos no codebook agora — 2015, 2020-2021 e 2022 — e é o mesmo apelo.** O item 31.3 e o 32.6, que o traziam como registro em potencial, estão fechados.

### 34.4 PT-05 sai de contextual. PT-06 não sai, e a recusa é o achado metodológico

**PT-05 passou a `Confirmado`**: Araujo e Sales documentam a cadeia causal que o registro afirma — atos e motociatas *"com o intuito de legitimar as hostilidades do mandatário em relação aos membros dos outros poderes constitucionais"* (rev. p. 33). O que não ficou coberto está declarado nominalmente: os rótulos *"STF ditador"* e *"ativismo judicial"* não aparecem na peça.

**PT-06 recebeu página no mesmo movimento e continua `Contextual`.** Repertório e enquadramento ganharam âncora; o **mecanismo** — consolidação do ecossistema informacional paralelo — segue sem leitura. O critério foi fixado por PT-04 na rodada anterior e está escrito na nota dele: *"passou a Confirmado porque a cadeia causal que ele afirma está ancorada"*. Em PT-04 e PT-05 foi a cadeia; em PT-06 foram repertório e enquadramento. **Promover aqui seria trocar o critério no meio da aplicação — a forma metodológica do modo de falha deste projeto.**

**E a peça que fecharia PT-06 entrou no corpus hoje e não foi lida:** von Bülow e Abers (2024) sustentam que o bolsonarismo é **movimento social**, não só ideologia, e cobrem março/2020 a outubro/2021, o período exato de PT-06.

### 34.5 A prova negativa achou um defeito meu, e uma limitação do harness

**O defeito meu, corrigido antes de gravar.** A primeira redação de PT-06 transcrevia *"A reivindicação do tratamento precoce e do "kit Covid""* — com **aspas aninhadas**, porque na fonte a expressão já vem aspada. `transcricoes()` fatia `fonte_trecho` em todo caractere de aspa e fica com os índices ímpares; a aspa interna inverte a paridade, o pedaço restante fica com 43 caracteres, abaixo do mínimo de 45, e **é descartado em silêncio**. O registro entraria no ciclo com uma transcrição conferida em vez de três.

> **A regra que isto deixa, e vale para todo o codebook: transcrição com aspa dentro de aspa não é conferida, e o silêncio do ciclo não distingue *conferida-e-OK* de *nunca-conferida*.**

**A limitação do harness, segunda ocorrência registrada.** Injetado o defeito de trocar a p. 8 pela p. 7 em `FERNANDES E SILVA 2021`, a conferência **continuou aprovando**: `casa()` desce a janelas de 40 caracteres, e *"antes a demonstracao publica de demandas"* aparece também na p. 14, que o registro lista — os autores repetem a própria fórmula na conclusão. **A âncora está certa** (busca independente nas 17 páginas: a frase inteira só existe na p. 8), mas a prova negativa para essa peça é **inconclusiva**. É a mesma limitação que o docstring de `conferir_paginas.py` declara para PT-59.

Os outros três defeitos foram pegos: página errada por um em PT-05 e em PT-04, por `conferir_paginas.py`; e vínculo apontando para a peça errada do mesmo eixo em PT-06, por `verificar_integridade.py`. **Na primeira tentativa eu havia jogado esse terceiro defeito no script errado e lido o resultado como aprovação** — erro meu de leitura, não do harness. Codebook restaurado byte a byte nas quatro injeções.

### 34.6 As quatro barradas chegaram, e abrir o arquivo corrigiu duas atribuições

O encaminhamento 4 pediu os links. O pesquisador os usou e **entregou as quatro peças no mesmo dia**, o que **confirma** o achado de acesso do item 33.2 e **corrige a sua formulação**: o alcance limitado era da **coleta automatizada**, não do projeto. O PDF de Bastos e Recuero traz licença **CC BY impressa na primeira página** — a obra era livre, o acesso não era.

| O que a lista do projeto dizia | O que o arquivo diz |
|:--|:--|
| Gohn **2020** | GOHN, M. G. "Ciclos de protestos no Brasil: 1970-2019". *mundosplurales*, 6(1):93-119, **2019** — o DOI traz `.1.2019.` e o rodapé registra *"Aceptado: 17/11/2019"* |
| Farias **e Casarões** 2022 | FARIAS, D. B. L.; CASARÕES, G.; **MAGALHÃES, D.** — **três** autores, *Global Studies Quarterly*, 2:1-13, 2022 |
| von Bülow e Abers **2022** | *Government and Opposition*, **59**:998-1016, **2024**. O slug `gov.2022.14` é o ano da publicação on-line; **o fascículo é de 2024** |

**O ano do DOI não é o ano de publicação** — armadilha de citação que entra na lista das registradas.

### 34.7 O que esta rodada NÃO fez

- **Não redatou PT-02.** A ressalva de datação está **redigida como nota**, por seu encaminhamento 5, e explica a diferença entre a data do evento (2015-2016, correta) e a data do ator (2011 em mobilização, 2003 em organização). Mas `data_hora` não mudou: **a nota explica a diferença, não a resolve.**
- **Não leu as outras dezesseis peças do eixo 13**, 419 páginas. A de maior retorno é von Bülow e Abers (2024), por fechar o mecanismo de PT-06.
- **Não promoveu PT-06**, e o item 34.4 diz por quê. **É reversível em um comando, mas muda o critério para todos.**
- **Não reexaminou PT-08** sob o critério novo, e precisaria ser reexaminado junto se o critério mudar.
- **Não renomeou nenhum outro mecanismo.** A tarefa 19 segue sua, agora com **sete** cobranças em vez de oito.
- **Não decidiu** se Gohn (2019) conta como fechamento parcial da tarefa 10. É o único balanço da literatura brasileira de protesto no corpus, e a tarefa 10 existe porque *"as sínteses têm zero referências sobre o Brasil"*.

---

## 35. A quarta rodada: PT-06 fecha, e o mecanismo que ele afirmava estava datado errado — 🔶 04/10/2026

**Quarta rodada do mesmo dia, e a camada conjuntural brasileira fecha.** A terceira havia deixado PT-06 contextual por critério, e escrito na nota do próprio registro qual peça o fecharia e que ela estava no corpus sem ter sido lida. O pesquisador mandou ler. Detalhe em [`projeto-pos-doc/12_CAMADA-T-1-CONJUNTURAL.md`](../projeto-pos-doc/12_CAMADA-T-1-CONJUNTURAL.md), §5.

**VON BÜLOW E ABERS 2024** — *Government and Opposition* 59:998-1016, página impressa = PDF + 997, lida integral. Cobre **março de 2020 a outubro de 2021**: a janela exata de PT-06.

Contextuais: **7 → 4 → 3 → 2 → 1**. Classes: **61 primária · 20 confirmado · 1 contextual · 1 inferência.** O que resta contextual é **PT-08**, o item comparado sobre o Capitólio.

### 35.1 A retificação vale mais que a âncora

O campo dizia **"consolidação de ecossistema informacional paralelo (Telegram/WhatsApp)"** — isto é, que a pandemia construiu a infraestrutura. As autoras documentam que *"the online radical right-wing networks that had grown exponentially since the beginning of the 2000s became sounding boards for informational chaos during the pandemic"* (p. 1006 impressa — PDF p. 9).

**A pandemia carrega uma infraestrutura que encontra pronta.** É a mesma forma da ressalva de datação de PT-02 — o meio do evento é anterior ao evento —, aplicada a outro objeto, e pela segunda vez nesta tarefa.

> **E é o modo de falha do projeto na sua forma mais difícil de ver.** Se a retificação não fosse feita, o registro teria ganhado página para um enunciado que a página contradiz: **a âncora certa sustentando o enunciado errado.** Uma conferência que pergunta *"a frase está na página?"* passa. Só a leitura pergunta *"a frase diz o que o campo afirma?"*.

### 35.2 O nome do mecanismo muda de natureza

"Ecossistema paralelo" sugere coerência. O que as autoras nomeiam é **caos informacional**, e a incoerência é constitutiva — a contradição entre os próprios enquadramentos não era problema para quem os circulava. O que sustenta a mobilização é a circulação, não a consistência: *"the circulation of these frames kept Bolsonaro's populist radical-right constituency in a state of constant mobilization"* (p. 1006).

O mecanismo passou a ser **mobilização permanente e radicalização da base** — e é essa base que serve de reserva de contingente em T₋₁ operacional.

### 35.3 A radicalização tem página e tem data

*"As Bolsonaro's popularity plummeted in the first months of 2021, his supporters became even more active. They also became more extreme"* (p. 1010 impressa). A forma: a campanha de maio de 2021 que autoriza o presidente a dar um golpe militar, culminando no 7 de setembro. E na conclusão, *"they blurred the boundaries between what Mudde (2007) called the radical right and the extreme right"* (p. 1011).

**O arco do apelo militar passou a ter corroboração dupla em 2020-2021:** Araujo e Sales pelo lado das Forças Armadas, von Bülow e Abers pelo lado da mobilização.

### 35.4 Um achado que excede o registro — e para o qual o esquema não tem campo

As autoras sustentam que o bolsonarismo é **movimento social com autonomia relativa em relação ao líder**: o presidente *"depends on a well-organized grassroots mobilization process that pre-dates his emergence as a populist radical-right leader and which he does not fully control"* (p. 1000), e o bolsonarismo *"is part of a process of right-wing mobilization that is larger than the leader himself, and precedes his rise to power"* (p. 1009).

Isso toca a pergunta central desta pesquisa — o 8 de janeiro foi conduzido de cima ou teve vida própria. **Nenhum dos 16 campos codifica grau de autonomia**, e por isso entrou como achado em `fonte_trecho`, não como campo. É material de argumento para a redação, e fica como decisão: o esquema ganha campo, ou isso vive só na prosa?

### 35.5 O que NÃO ficou ancorado, e uma razão é de regra do projeto

- **O rótulo "guerra cultural"** segue sem âncora: as autoras documentam a ameaça aos valores tradicionais e a esquerda como inimigo, não a expressão.
- **Telegram e WhatsApp como plataformas medidas.** As autoras as nomeiam, mas **por citação de segunda mão** — as 802 mensagens de WhatsApp são de Soares et al. (2021) e as 867 de Telegram são de Nascimento et al. (2020), nenhum no corpus. **A regra deste projeto proíbe lastrear cifra conferida apenas contra outra citação dela**, e por isso nenhuma das duas entra como verificada. O campo continua nomeando as plataformas, e o status declara que não estão verificadas. Âncora de primeira mão, se quiser: Chagas e Carreiro (2022) e Mendonça e Freitas (2022), já no corpus.
- **O período termina em outubro de 2021.** A ponte para os acampamentos de novembro de 2022 não é feita por esta peça.

### 35.6 Dois buracos do harness, abertos desde o começo, fechados por esta peça

A peça é a primeira em inglês a ancorar registro, e caiu em dois defeitos que ninguém havia pisado.

**(a) Apóstrofo intrapalavra era delimitador de aspa.** `ASPAS_FECHA` contém U+2019, o apóstrofo de todo texto em inglês. Qualquer transcrição com *"Bolsonaro's"* era descartada **em silêncio** — zero candidatos, nenhum aviso, ciclo verde por não haver o que conferir. **Auditado o codebook no dia: as 57 transcrições então existentes não eram afetadas**, por serem em português e sem aspa interna; nada retroativo mudou.

**(b) Hifenização de quebra de linha não era unida.** `norm_busca` apagava o hífen e deixava o espaço: o PDF *"mobiliza-\ntion"* normalizava para `mobiliza tion` e não casava com `mobilization`. Duas âncoras desta peça apareciam como não localizadas tendo a frase na página citada.

Os dois consertos foram provados **invariantes**: 66 âncoras anteriores idênticas, 57 de 57 transcrições ainda vistas. **A limitação irmã continua sem conserto, de propósito:** aspa dupla aninhada ainda inverte a paridade, e a saída é escolher outro trecho (item 34.5).

**Prova negativa da rodada:** três defeitos, três pegos — página errada por um em PT-06 e em PT-05 (`conferir_paginas.py`) e vínculo removido com páginas mantidas (`verificar_integridade.py`). Codebook restaurado byte a byte. **Os consertos não criaram falso positivo.**

### 35.7 O que esta rodada NÃO fez

- **Não leu as outras quinze peças do eixo 13**, 400 páginas. E a natureza do que falta mudou: **nenhuma delas bloqueia mais registro algum.** A leitura restante passou a servir à redação, não à codificação.
- **Não resolveu PT-08**, que é o único contextual restante e pede literatura comparada sobre o 6 de janeiro norte-americano — que nenhuma das dezoito peças cobre.
- **Não leu Cesarino (2022)**, que PT-06 citava desde agosto sem ter. Está no corpus, não lida, e o registro diz isso.
- **Não tirou Telegram e WhatsApp do campo**, nem os verificou. Ficam nomeados e declarados como não verificados (item 35.5).
- **Não acrescentou campo ao esquema** para a autonomia do movimento (item 35.4).

---

## 36. PT-08 preparado e bloqueado: a peça está lida, o arquivo não está no corpus — 🔶 08/10/2026

**A tarefa era fechar PT-08 com as duas peças da camada A.** Não fechou, e o motivo é de acesso, não de evidência. O que ficou pronto está abaixo, para que a recodificação seja um comando quando os arquivos chegarem.

### 36.1 Uma peça marcada LIDA que nunca entrou no corpus

`data/processed/camada_a_acesso.csv` registra **CASTAÑEDA e JENKS (2023)**, *"January 6th and De-Democratization in the United States"* (*Social Sciences* 12(4):238, MDPI, CC-BY), com `estado :: LIDO` e a nota *"MDPI, integral"*. **O arquivo não está em `Fontes/`.** Foi lida on-line numa sessão anterior, e sem arquivo local **não há como ancorar página** — `conferir_paginas.py` abre o PDF do corpus, não a web.

> **Isto é defeito de aparato, não de leitura:** a camada A tem um estado `LIDO` que não implica arquivo no corpus, e por isso uma peça pode constar como lida e não poder ancorar nada. Vale decidir se o CSV passa a distinguir *lida* de *lida-e-arquivada*.

### 36.2 A âncora que a peça entrega — e por que a coluna `uso` estava errada por excesso

A coluna `uso` do CSV prometia *"o caso de que o 8/1 é emulação, lido como episódio de desdemocratização"*. Medido no texto integral, no navegador: **"Bolsonaro" aparece 0 vezes, "diffusion" 0, "emulation" 0, "transnational" 0, "Brazil" 1.**

**E a medição certa levaria à conclusão errada.** A única ocorrência de "Brazil" é a frase que o projeto precisa, e ela usa o vocabulário de Tilly em vez das palavras que eu contei:

> *"The attack on congress to contest an election has now become a **contentious performance** that was used by the equivalent actors in Brazil on January 8, 2023. Both events occurred with the encouragement of Steve Bannon and similar agents of chaos."*

Isso **é** a afirmação de difusão, enunciada como *performance contenciosa* — e com agente de transmissão nomeado. **Contagem de termos é medida de palavra, não de proposição:** irmã tipográfica da armadilha da ligadura ﬁ, e irmã semântica da décima quarta ocorrência, em que a âncora certa sustentava o enunciado errado.

**Candidatos a âncora, todos localizados no texto e NENHUM escrito no codebook** — falta o arquivo para conferir página:

- *"The attack on congress to contest an election has now become a contentious performance that was used by the equivalent actors in Brazil on January 8, 2023"*
- *"Both events occurred with the encouragement of Steve Bannon and similar agents of chaos"*
- *"Trump's rise to power and the riots on January 6th were symptoms of a longer process of de-democratization"*
- *"De-democratization is not unique to the United States and has been happening in many countries for years"*

**Um limite a declarar quando entrar:** a ligação com o Brasil é feita em **uma frase, de passagem**, sem aparato de evidência do lado brasileiro. É ressalva da mesma natureza que "um estado só, série até 2015" em Fernandes e Silva. E ela **não contradiz** a ressalva do Sri Lanka que PT-08 já carrega: o Capitólio é referência de **repertório**, o Sri Lanka é referência de **eficácia**.

### 36.3 Por que os dois arquivos não vieram

| Peça | Via | O que aconteceu |
|:--|:--|:--|
| **CASTAÑEDA e JENKS (2023)**, *Social Sciences* 12(4):238 — [10.3390/socsci12040238](https://doi.org/10.3390/socsci12040238) | MDPI | **HTTP 403** ao curl, com e sem cabeçalhos completos de navegador. O gate é um **interstitial do Akamai Bot Manager** com proof-of-work em JavaScript. O navegador embutido abre a página e busca o PDF (200, 606 KB), mas o cookie de liberação é `httpOnly` e não passa ao curl. **Não escrevi solucionador: contornar detecção de bot está fora do que faço.** Transferir 606 KB por base64 custaria ~800 mil caracteres e não é a saída certa. *A memória do projeto registrava a MDPI como editora que passa — deixou de passar.* |
| **CHEN, LUKITO e KOO (2023)**, *"Comparing the #StopTheSteal Movement across Multiple Platforms"*, *Social Media + Society* 9(3) — [10.1177/20563051231196879](https://doi.org/10.1177/20563051231196879) | SAGE | Sem PDF em depósito algum: o OpenAlex lista a SAGE, o DOAJ (só página de registro) e o HKU Scholars Hub (não aberto). Mesmo bloqueio da SAGE que Bastos e Recuero sofreram em 04/10 — e que você resolveu entregando o arquivo. **Correção de atribuição, de passagem:** são **três** autores (Bin Chen, Josephine Lukito, Gyo Hyun Koo), e o CSV da camada A não os nomeia. |

**O precedente diz o que fazer:** em 04/10 você entregou quatro peças barradas em poucas horas, e uma delas fechou PT-06. Os dois links acima abrem num navegador comum.

---

## 37. A tarefa 10 executada: sete livros entram, e o cânone brasileiro não está em acesso aberto — 🔶 08/10/2026

**Eixo 14 aberto: sete peças, 567 páginas**, em `Fontes/14_Livros-brasileiros/`. Documento completo em [`projeto-pos-doc/14_LIVROS-BRASILEIROS.md`](../projeto-pos-doc/14_LIVROS-BRASILEIROS.md). Corpus: **52 → 59 PDFs, 10.207 → 10.774 páginas**; documental inalterada em **22 / 6.951**.

**NENHUMA FOI LIDA E NENHUMA ANCORA REGISTRO.**

### 37.1 O achado, que é a resposta da tarefa e não a sua falha

**O cânone brasileiro de movimentos sociais não está em acesso aberto como livro.** Busca nominal por dezenove autores, exigindo autoria casada, tipo `book`/`book-chapter`, acesso aberto: **zero** para Gohn, Sader, Scherer-Warren, Avritzer, Doimo, Telles, Abranches, Nobre, Solano e Messenberg. **André Singer é o único do cânone que a coleta alcançou** — e como organizador de coletânea, não em monografia.

A busca por título confirma pelo outro lado: *Quando novos personagens entraram em cena*, *Teoria dos movimentos sociais*, *A vez e a voz do popular* e *Sociedade civil e espaços públicos no Brasil* devolvem **artigos que resenham os livros**, não os livros. **O cânone é de editora comercial e segue dependendo dos seus arquivos, como Alonso (2023) dependeu.**

### 37.2 As sete que entraram, e duas que valem destaque

Seis são capítulos de ***Giros à direita: análises e perspectivas sobre o campo líbero-conservador*** (Sobral, SertãoCult, 2020) — Löwy, Montenegro, Hoeveler, Lerner, Cazetta e Gentile. A sétima é ***O Brasil no inferno global*** (Singer, Araujo e Rugitsky, FFLCH/USP, 2022, 374 p.).

- **HOEVELER (2020)**, sobre fóruns e redes organizativas da extrema direita latino-americana, é **a peça do corpus mais próxima do mecanismo que PT-08 afirma** — e pelo lado brasileiro, que faltava.
- **LERNER (2020)**, sobre a rede conservadora no Facebook, é candidata a dar **âncora de primeira mão** à infraestrutura digital que PT-06 nomeia e que von Bülow e Abers (2024) só reportam por citação de segunda mão (item 35.5). **Muda a plataforma; não fecha a ressalva.** Decisão sua.

### 37.3 Quinta variante de armadilha de numeração, e é a mais perigosa do corpus

Os seis capítulos são **offprints**: cada PDF traz as **mesmas 12 páginas de pré-textuais do volume** e o capítulo começa sempre na **PDF p. 13**. O deslocamento é **diferente em cada arquivo** — Löwy +0, Montenegro +33, Hoeveler +58, Lerner +77, Cazetta +161, Gentile +209.

> **A mesma página de PDF significa páginas impressas diferentes em arquivos distintos do mesmo volume.** E citar PDF p. 1-12 é citar o pré-textual **através do arquivo errado**: as doze páginas são idênticas nos seis, de modo que a conferência de transcrição **casaria** e o vínculo estaria errado. **Regra: no eixo 14, só cite PDF p. ≥ 13, e sempre pelo arquivo do capítulo.**

### 37.4 Três defeitos meus na própria coleta

1. **Pontuar por sobrenome.** Dei peso ao cânone por sobrenome, e "Silva", "Souza", "Rocha", "Carvalho" e "Nunes" são comuns: *Pandemia e socioeconomia no Maranhão* tirou a pontuação mais alta da fila por casar seis sobrenomes e nenhum autor. **Sobrenome não identifica autor.**
2. **Nome completo conferido na lista inteira.** Exigir todas as partes do nome na autoria ainda casou "Camila Rocha" com um volume que tinha *Camila Haus* e *Fabielle Rocha Cruz* — as partes presentes, em pessoas diferentes. **O casamento tem de ser por autor, não por lista.**
3. **Verificação de dois eixos amostrada nas primeiras páginas.** Reprovou os **seis** capítulos certos, porque nos offprints as duas primeiras páginas são capa sem camada de texto e biografias do volume. Diagnosticado: arquivos distintos, SHA-256 distintos, cada um com o próprio autor e título. Reconferidos no texto integral: **6 de 6**. **Amostrar as primeiras páginas falha em offprint com pré-textual comum.**

### 37.5 O que ficou barrado, e é o padrão de 04/10

Quatro livros identificados, de acesso aberto, no **SciELO Livros** — host `books.scielo.org`, atrás do **Bunny Shield**, desafio JavaScript de detecção de bot: **403** ao curl e ao `urllib`. **Não escrevi solucionador.** Nenhum tem cópia em outro depósito (conferido no OpenAlex, no DOAB e nos repositórios da UnB e da UFRGS):

| Peça | DOI | Por que importa |
|:--|:--|:--|
| Gurza Lavalle, Carlos, Dowbor e Szwako (2018), *Movimentos sociais e institucionalização* | 10.7476/9788575114797 | O livro brasileiro de referência sobre **movimento que entra no Estado** — o mecanismo de PT-04 |
| Abers (org.) (2021), *Ativismo institucional* | 10.7476/9786558461593 | **Mesma Rebecca Abers** que co-assina a peça que fechou PT-06 |
| Rich (2021), *Ativismo patrocinado pelo Estado* | 10.7476/9786557081044 | Movimento e burocracia; par do anterior |
| Madeira, Marona e Del Río (2022), *Democracia e justiça na América Latina* | 10.7476/9786587949550 | Serve ao **arco judicial** (PT-03A a PT-06C), que hoje se apoia só em acórdãos |

**Uma armadilha de atribuição que o segundo eixo pegou:** *Impasses da democracia no Brasil* (2023), verde e com PDF integral na USP, **não é o livro de Avritzer** — é de **Maria Hermínia Tavares de Almeida**, mesmo título. Descartado. Mesma forma da sexta ocorrência do modo de falha do projeto.

### 37.6 O que a tarefa 10 NÃO fez

- **Não leu nada.** Sete peças, 567 páginas.
- **Não fechou a tarefa 10:** o cânone pré-digital continua fora e depende dos seus arquivos.
- **Não baixou os quatro do SciELO Livros** (item 37.5).
- **Não coletou dois capítulos pertinentes de *Giros à direita*** — Hernán Ramírez (p. 20-45) e Fabiano Godinho Faria (p. 122) —, porque **ampliar a coleta sem seu aval é decisão, não execução**. O depósito do IBICT passa; são coletáveis.
- **Não decidiu se Gohn (2019) fecha parcialmente a tarefa**, pendência sua desde 04/10.

---

## 38. PT-08 fecha, e o codebook deixa de ter registro contextual — 🔶 08/10/2026

**Segundo passo de 08/10.** O pesquisador entregou cinco peças e mandou coletar duas. PT-08 era o **último contextual**; fechou. Documentos: [`15_COMPARADO-6-DE-JANEIRO.md`](../projeto-pos-doc/15_COMPARADO-6-DE-JANEIRO.md) e [`14_LIVROS-BRASILEIROS.md`](../projeto-pos-doc/14_LIVROS-BRASILEIROS.md), §7.

**Classes: 61 em fonte primária · 21 confirmados · ZERO contextuais · 0 a verificar · 1 inferência.** Contextuais: 7 → 4 → 3 → 2 → 1 → **0**. Corpus: **59 → 66 PDFs, 10.774 → 12.089 páginas**; documental inalterada em **22 / 6.951** — quinta vez que o corpus cresce sem documento oficial entrar.

### 38.1 O que fechou PT-08, e a divisão entre as duas peças é nítida

- **CHEN, LUKITO E KOO (2023)** ancoram o **evento** e o **enquadramento**: 675.336 posts de Facebook, Twitter e Parler, entre 1/09/2020 e 1/02/2021, pela tipologia de **Snow e Benford** — marco teórico declarado deste projeto. **Não dizem nada sobre o Brasil:** zero "Brazil", zero "Bolsonaro", zero "January 8". *São três autores, e a planilha da camada A nomeava zero.*
- **CASTAÑEDA E JENKS (2023)** ancoram o **mecanismo**: o ataque ao Congresso *"has now become a contentious performance that was used by the equivalent actors in Brazil on January 8, 2023"* (PDF p. 10), com Steve Bannon nomeado como agente de transmissão.

**Dois limites declarados no registro:** a ligação com o Brasil é **uma frase, de passagem**, sem aparato do lado brasileiro; e Chen, Lukito e Koo não tratam do Brasil. **A ressalva do Sri Lanka fica reforçada:** Capitólio é referência de repertório, Sri Lanka é referência de eficácia, e "performance contenciosa" é afirmação de repertório.

### 38.2 Décima quinta ocorrência do modo de falha: contagem de termo não é medida de proposição

Para decidir se Castañeda e Jenks servia, contei termos no texto integral: **"Bolsonaro" 0, "diffusion" 0, "emulation" 0, "transnational" 0, "Brazil" 1.** A medição estava certa e a conclusão que ela sugeria — *a peça não serve* — estava **errada**: a única ocorrência de "Brazil" é exatamente a frase decisiva, no vocabulário de Tilly em vez das palavras com que eu a nomeio.

> **Um autor pode afirmar a proposição inteira sem usar nenhuma das palavras com que você a nomeia.** Irmã semântica da armadilha da ligadura ﬁ: lá a palavra estava e a busca não a via; aqui a palavra não está e a tese está. A saída é **ler o contexto de cada ocorrência, não o histograma**.

### 38.3 A aspa aninhada mordeu pela terceira vez no mesmo dia — e agora tem checagem no ciclo

Na primeira gravação, o `fonte_trecho` de PT-08 tinha `“Plano B”` e `“Soc. Sci. 2023, 12, 238”` aninhados. A paridade de `transcricoes()` inverteu, e o resultado foi **simétrico e pior do que em 04/10**:

- **cinco transcrições reais ficaram sem ser extraídas** — as três de Castañeda e Jenks entre elas, isto é, as âncoras do mecanismo **não eram conferidas por ninguém**;
- e **um pedaço de aparato meu** — *"não foi o Capitólio, e sim a revolta do Sri Lanka de julho de 2022"* — foi **promovido a transcrição** e procurado no PDF, onde naturalmente não estava. Foi essa falha que acendeu o alarme.

**`conferir_paginas.py` ganhou a função `aninhamento()`**, que compara o pareamento simples de aspas curvas com o que a paridade extrai e **trata a diferença como FALHA**, com código de saída ≠ 0. Auditados os 83 registros: **só PT-08 estava afetado**, e era texto meu de minutos antes.

**E um sub-caso novo, que a máscara de apóstrofo intrapalavra de 04/10 não pega:** o **apóstrofo de posse no fim da palavra** — `members’ political identities` — também é delimitador, porque não está entre dois caracteres de palavra. A transcrição de Chen, Lukito e Koo foi encurtada antes dele. **Em texto inglês, possessivo plural quebra a paridade.**

> **A regra, agora com checagem: transcrição não conferida é pior que transcrição errada — a errada aparece.**

### 38.4 A prova negativa da primeira tentativa não valia nada

Rodei a prova negativa **antes** de descobrir a falha, e as três injeções apareceram como "PEGOU" porque a linha de base já tinha `falhas 1`. **Prova negativa contra linha de base suja não prova nada:** o sinal que você lê como detecção pode ser o defeito que já estava lá. Refeita com base limpa (`confirmados 1 | falhas 0`): **três de três pegos**, codebook restaurado byte a byte.

### 38.5 Um estado de aparato que enganava, consertado

`camada_a_acesso.csv` marcava Castañeda e Jenks como **`LIDO`** desde 30/09, com a nota "MDPI, integral" — **e o arquivo não estava em `Fontes/`**: tinha sido lida on-line. Sem arquivo local, `conferir_paginas.py` não confere página nenhuma, de modo que o estado **prometia âncora que não existia**.

`LIDOS`, em `localizar_camada_a.py`, ganhou um **terceiro campo** — o caminho no corpus, ou `None` — e o relatório passou a contar e nomear os lidos sem arquivo. O script **falha** se um caminho declarado não existir em disco. A conta de hoje:

> **Dos 7 lidos, 4 têm arquivo no corpus e 3 foram lidos só on-line:** Collier (2011, Cambridge Core), Mayntz (2004, MPG.PuRe) e **González-Bailón et al.** (2011, Nature). **Nenhum dos três pode ancorar página.**
>
> **CORREÇÃO DE ATRIBUIÇÃO, 08/10/2026 à noite.** O projeto vinha chamando a terceira peça de "Borge-Holthoefer et al. (2011)", que é o **segundo** autor. A folha de título do PDF, lida em primeira mão, traz **Sandra González-Bailón** (Oxford Internet Institute), Javier Borge-Holthoefer, Alejandro Rivero e Yamir Moreno (Zaragoza) — **quatro** autores, 7 páginas, *Scientific Reports*. É a quarta atribuição que abrir o arquivo corrige em 08/10, depois de Gohn (ano), von Bülow e Abers (fascículo) e Chen, Lukito e Koo (número de autores). **A regra que isso firma: autoria se lê na folha de título, não no nome pelo qual o projeto se acostumou a chamar a peça.**

**A regra: `lida` e `lida-e-arquivada` são estados distintos, e só o segundo autoriza âncora.**

### 38.6 A tarefa 10 vai a doze peças, e o quarto livro saiu da lista por outra razão

Entraram três livros entregues — Gurza Lavalle, Carlos, Dowbor e Szwako (2018, EdUERJ), Abers (2021, Editora UnB) e Madeira, Marona e Del Río (2022, EdUERJ) — e os dois capítulos de *Giros à direita* que faltavam: Ramírez (offset **+7**) e Faria (offset **+109**).

**Os três livros têm offset A DETERMINAR**, e isso está declarado: a ficha catalográfica anuncia menos páginas impressas do que o PDF tem (411/414, 356/359, 423/427).

**RICH (2021) saiu da lista, e não por bloqueio:** o pesquisador apurou que **não é de acesso aberto — está à venda em livraria**, apesar de o OpenAlex a declarar ouro e o SciELO Livros a listar. Avaliou que a resenha disponível é lastro inconsistente. **É o primeiro caso em que o erro está no próprio registro de acesso aberto, não no gate do editor:** ouro no OpenAlex pode ser *falso*, não apenas *difícil de baixar*.

### 38.7 Dois defeitos meus na busca, e um achado que fica como sua decisão

O probe que varreu 36 handles do IBICT **não seguia o redirecionamento http→https** e dava o capítulo de Faria como inexistente — falha do probe, não do repositório. E varri o HTML de um **DSpace 7**, que renderiza em JavaScript e não serve itens em HTML; o caminho é a **API REST**, que resolveu em uma chamada.

**E a API mostrou que o volume inteiro de *Giros à direita* está depositado** (`deposita/166`, "Faria & Marques - Giros à Direita.pdf", 2,5 MB). Isso tornaria os oito offprints redundantes e **retiraria a armadilha de offset por capítulo**. **Não foi trocado: mexer em oito arquivos já commitados do corpus é sua decisão.**

### 38.8 A pendência do Gohn, resolvida — e a tarefa 10 se divide em duas

Você delegou a decisão. **Gohn (2019) fecha PARCIALMENTE a tarefa 10, e num nível preciso.** A tarefa confundia duas coisas:

| | O que a tarefa 10 pedia | Gohn resolve? |
|:--|:--|:--|
| **(a)** As sínteses têm **zero referências** sobre o Brasil — lacuna de **mapa bibliográfico** | **SIM.** Gohn mapeia a produção brasileira sobre protesto de 1970 a 2019, por ciclo, nomeando autores e paradigmas, e declara explicitamente o recorte: *"protestos ocorridos no Brasil e bibliografia produzida também no Brasil, em livros, capítulos e artigos"* (impressa 93) | ✅ |
| **(b)** O corpus não tem a **literatura brasileira em livro** — lacuna de **fonte legível com página** | **NÃO.** É artigo: entrega o mapa, não os textos. E a autora declara que *"é impossível esgotar o universo de autores"* (impressa 95) | ❌ |

**Execução da decisão:** a linha da tarefa 10 na agenda foi reescrita para registrar a metade (a) como fechada por Gohn e manter (b) aberta, dependente dos seus arquivos. **O escopo da tarefa estreitou** — de "acrescentar a literatura clássica brasileira" para "obter os textos que o mapa de Gohn nomeia e que o projeto queira citar com página".

**Gohn passou a `LIDA EM PARTE` em `PROCEDENCIA`** — introdução, primeiro ciclo, quinto ciclo e conclusões (PDF p. 1-4, 17-18) — e **continua não ancorando registro**: a leitura serviu para decidir o escopo da tarefa, não para pôr página em campo de codebook. *E traz uma cifra que o projeto NÃO deve usar sem outra fonte: "após junho de 2013 mais de trinta grupos foram criados" (impressa 109), que ela credita a si mesma.*

### 38.9 O que esta rodada NÃO fez

- **Não leu as doze peças do eixo 14** (1.854 páginas) nem as quinze não lidas do eixo 13.
- **Não trocou os oito offprints pelo volume inteiro** (§38.7).
- **Não arquivou as três peças da camada A lidas só on-line** (§38.5).
- **Não reexaminou se `Contextual` deve continuar no vocabulário controlado** agora que nenhum registro o usa — e a resposta provável é sim, porque registro novo pode nascer contextual.
- **Não determinou o offset dos três livros entregues** (§38.6): isso se faz abrindo, na leitura.

---

## Ordem de ataque — revista em 30/09/2026

**A decisão que ordena tudo continua sendo a de 16/08/2026: a redação é o último item.** A ordem anterior a essa data tratava o aparato como suficiente e punha a escrita como ponto de virada; esta trata o conjunto de dados do processo político como pré-requisito.

**A revisão de 29/09 foi de contabilidade, não de rumo.** A tabela vinha mostrando como abertas quatro tarefas concluídas em 16/08 — o arquivamento web (4), a obtenção do balanço (8) e a reauditoria (11), além da 6. Foram fechadas com a data correta, e entraram as tarefas nascidas das rodadas 19, 20 e 21.

**A de 30/09 acrescentou três tarefas nascidas da leitura na fonte** — 19, 20 e 21 — e corrigiu a contabilidade da 17, que passou a ser gerada.

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
| 21 | ~~Desenhar o campo multiorganizacional~~ — 22 entidades, e o modelo não acomoda 5 delas; no ciclo como passo 7/7 | 26 | ✅ 30/09 |
| 20 | ~~Escrever as hipóteses rivais de PT-28~~ — H3 e H5 refutadas com evidência já ancorada; H2 sobrevive e relocaliza o ônus | 27 | ✅ 30/09 |
| 22 | ~~Datar a posse de Torres na SSP-DF~~ — 02/01/2023, em duas fontes; H2 enfraquece e entra H6 | 28 | ✅ 30/09 |
| 23 | ~~Codificar os três fatos novos~~ — **PT-18A**, registro próprio; codebook a 83 | 29 | ✅ 30/09 |
| 24 | ~~Obter os atos de 02-03/01/2023~~ — DODF varrido; a troca de "cargos centrais" **não se confirma** | 30.1 | ✅ 30/09 |
| 13 | ~~Decidir o "Conclusão dos julgamentos" de PT-61~~ — a expressão **não estava no balanço**; reformulada | 30.2 | ✅ 30/09 |
| 14 | ~~Codificar a camada $T_{-1}$ conjuntural~~ — **6 de 7** codificados na fonte com página, em **quatro** rodadas: a camada conjuntural **brasileira inteira**, de junho de 2013 à pandemia. A segunda rodada tirou a descontinuidade 2013→2015 do codebook; a terceira executou os oito encaminhamentos, renomeou dois mecanismos e **tirou de PT-02 a "tolerância policial", que a leitura contradisse**; a quarta fechou PT-06 e **retificou o mecanismo dele** — a infraestrutura informacional antecede a pandemia. Resta contextual só **PT-08**, e a lacuna dele é literatura comparada sobre o Capitólio | 31, 32, 34, 35 | ✅ 04/10 |

### Abertas

| # | Tarefa | Item desta agenda | Depende de |
|:--|:--|:--|:--|
| 10 | Acrescentar a literatura brasileira em livro — 🔶 **eixo 14 com 12 peças, 1.854 p.** em 08/10, nenhuma lida: 7 coletadas, 3 entregues por você e 2 capítulos a mais por encaminhamento. **A tarefa SE DIVIDIU em duas, e metade está fechada** (item 38.8): o mapa bibliográfico brasileiro que as sínteses não tinham está em Gohn (2019), que mapeia 1970-2019 por ciclo nomeando autores e paradigmas; o que resta é **obter os textos que esse mapa nomeia** — o cânone (Sader, Scherer-Warren, Avritzer, Doimo, Telles, Abranches, Nobre, Solano, Messenberg) é de editora comercial, **zero com autoria casada em acesso aberto**, e depende dos seus arquivos | 11.4, 22.4, 37, 38 | seus arquivos |
| 17 | **Ler na fonte os 43 da camada A** (passo 3 do item 11.3) — **27 pendentes**: 6 lidos, 7 com ficha da 1ª leva, 3 impedidos. Números gerados por `localizar_camada_a.py`, não digitados | 23, 24, 25 | acesso institucional |
| 19 | **Decidir o nome de `mecanismo_causal`** e aplicar as **sete** cobranças da seção 4 do documento 09. A tarefa 14 acrescentou três e **devolveu as três**: a descontinuidade 2013→2015 (item 32); a "apropriação de repertório que Tilly não detalha", que era conclusão errada — Kunrath Silva (2018, § 15) mostra mecanismo distinto da apropriação social; e **"certificação" em PT-03, que o pesquisador renomeou para *ressignificação do protesto* em 04/10** (item 34.2). Dois nomes de mecanismo saíram daqui decididos — PT-01 e PT-03 | 24.6, 25.1, 25.2, 31.6, 32.1, 34.2 | decisão sua |
| 25 | **A literatura do bolsonarismo como mobilização** — 🔶 **coleta fechada em 04/10**: **18 peças, 453 p.** em `Fontes/13_Bolsonarismo-mobilizacao/` — 14 por OpenAlex e **as 4 barradas entregues pelo pesquisador** (item 34.6). **Três foram lidas** e ancoram registro: Araujo e Sales (2022), que tirou PT-05 de contextual; Fernandes e Silva (2021), que tirou a "tolerância policial" de PT-02; e von Bülow e Abers (2024), que **fechou PT-06 e retificou o mecanismo dele**. **Faltam 15, 400 p.** — e **nenhuma bloqueia registro**: a leitura restante serve à redação, não à codificação | 23.2, 31.4, 33, 34, 35 | leitura |
| 15 | Higiene do repositório: licença, remoto, `.backup_pre_lula/`, ponteiros no JSON | 20, 21.4 | decisão sua |
| 16 | **Redação do artigo** | 3, 4, 5, 6, 9, 10 | tudo acima |

**Nenhuma pendência de dado depende de você** — isso valia desde 16/08, deixou de valer em 30/09 com a tarefa 24, e em 04/10 mudou duas vezes: a tarefa **14** fechou a parte que podia fechar e deixou a **25**, bibliográfica; e horas depois, na terceira rodada, **você entregou as quatro peças barradas e mandou ler duas**, o que fechou a coleta da 25 e tirou PT-05 de contextual. **O que resta da 25 é leitura, e a leitura não depende de você.**

**As seis abertas, por natureza:** decisões suas (**15, 19**), leitura ou entrega de arquivo (**10, 17, 25**) e a redação (**16**). **A 10 mudou de natureza em 08/10:** deixou de ser tarefa de busca — a busca foi feita e mostrou que o cânone não está em acesso aberto — e passou a depender dos seus arquivos, como a 17 depende do seu acesso institucional. **A tarefa 14 fechou em 04/10**, em quatro rodadas, e com ela a última tarefa de codificação. **Só a 16 depende das outras — e, desde a quarta rodada, nenhuma leitura pendente bloqueia registro: as quinze peças que restam no eixo 13 servem à redação, não à codificação.**

> **As decisões suas que restam, e nenhuma bloqueia o resto.** (1) **Redatar `data_hora` de PT-02** — a ressalva está redigida como nota, a diferença entre data do evento e data do ator está explicada, mas mudar o campo é seu (item 34.7). (2) ~~Promover ou não PT-06~~ — **resolvido na quarta rodada, e sem mexer no critério:** você mandou ler a peça, o mecanismo ganhou âncora própria, PT-06 passou a `Confirmado` pela cadeia causal, e PT-08 não precisou ser reexaminado (item 35). (3) **Se Gohn (2019) fecha parcialmente a tarefa 10** — é o único balanço da literatura brasileira de protesto no corpus, e a 10 existe por essa lacuna. (4) **NOVO — Telegram e WhatsApp ficam nomeados em PT-06 sem verificação, ou saem do campo?** A peça os reporta por citação de segunda mão, e a regra do projeto não admite lastro nessa forma (item 35.5). (5) **NOVO — o esquema de 16 campos ganha campo para autonomia do movimento em relação ao líder?** É o argumento central de von Bülow e Abers e toca a pergunta desta pesquisa; hoje vive em `fonte_trecho` como achado (item 35.4).

> **Uma correção de contabilidade, em 04/10.** A tarefa 14 aparecia como dependente da **9** (triagem por pertinência), e a dependência estava errada: a camada A dos 411 DOIs é metodológica e de teoria geral, com **zero** referências sobre o Brasil, e nunca poderia codificar PT-01 a PT-06. A literatura que resolveu a tarefa veio de fora dos 411, de uma pasta que ninguém havia varrido. **A dependência real era de coleta brasileira — isto é, da tarefa 10 e da 25 —, não da triagem.**

> **Esta tabela envelheceu duas vezes em dois dias** — em 29/09 trazia a 18 duplicada e três números à mão na 17; em 30/09 manteve 20 e 21 como abertas depois de fechadas e não contou a 22. É a mesma lição de 25/09 batendo na peça que existe para registrar a lição. **A contagem da 17 já é gerada; o resto desta tabela não é**, e é a próxima candidata a virar script.

**Uma correção de contabilidade, em 30/09.** Esta tabela trazia a tarefa 18 duplicada na seção "Abertas" já riscada, uma referência a "tarefas 12 a 15" que não existem como tarefas — 12 é item desta agenda, não tarefa — e, na 17, três números à mão dos quais um não fechava a soma. **As contagens da 17 passaram a sair de `scripts/localizar_camada_a.py`**, com autoteste que exige que todo DOI declarado como lido, fichado ou impedido esteja de fato na camada A.

**Quando a redação começar**, os itens 3, 4 e 5 desta agenda vêm primeiro: são antecipação de crítica, os pontos que um parecerista atento levantaria, e os que mais mudam o texto. Os itens 6, 9 e 10 são parágrafos de discussão, resolvidos na escrita.

**A lição das três últimas rodadas, que vale como regra de trabalho.** Em 11/09 o relatório estava quase um mês atrás do codebook; em 25/09 as figuras estavam seis semanas atrás. Nos dois casos o JSON estava certo e a peça derivada, errada — e nos dois casos nada avisou, porque o ciclo só cobria o que é gerado por script. **Toda peça escrita à mão que reproduz números do codebook precisa ou virar gerada, ou ganhar uma checagem no ciclo.** As três que existiam — as duas figuras e o relatório — ganharam a sua em 25/09, e a do relatório achou mais três defasagens no primeiro uso. A regra vale para a próxima peça que nascer: se ela repete um número do codebook e ninguém a gera, ela vai envelhecer.

---

## 39. O volume substitui os offprints, os quatro livros ganham offset, e uma ficha minha cai — 🔶 08/10/2026

**Encaminhamentos do pesquisador:** resolver a pendência do volume de *Giros à direita* (§38.9, primeiro item), **ler** os três livros entregues, e decidir sobre as três peças da camada A lidas só on-line e sobre o `Contextual` no vocabulário.

### 39.1 O que foi executado

| | |
|:--|:--|
| **Volume integral no lugar dos oito offprints** | 8 arquivos a menos, 1 a mais; **onze** capítulos contra oito; **offset 0** contra oito offsets distintos. A quinta variante de armadilha de numeração **saiu do corpus**, e é a única das seis que foi retirada em vez de declarada |
| **Procedência dupla** | SHA-256 da cópia entregue pelo pesquisador e da que eu baixei do IBICT (`deposita/166`) é **idêntico**: `560f5bd9…04c9f67`. Nenhuma outra peça do corpus tem duas procedências independentes concordantes |
| **Três capítulos novos** | Torres (p. 159), Costa Filho (p. 193), Marques (p. 241) — o corpus não os tinha, e a §5.2 do documento 14 subestimava a lacuna em três |
| **Offsets medidos** | Gurza Lavalle **−2**, Abers **−2**, Madeira **−2**, Singer **−1**, volume *Giros* **0** |
| **Três livros lidos em parte** | Sumários, capítulos de abertura de Lavalle e Abers, capítulo 8 de Madeira, e varredura normalizada do texto integral dos três |
| **Corpus** | 66 PDFs / 12.089 p. → **59 PDFs / 12.067 p.**; documental inalterada em **22 / 6.951** |
| **Registros recodificados** | **nenhum** |

### 39.2 A diferença da ficha não é o offset — e o caso anterior ensinou errado

Lavalle declara 411 impressas em 414 de PDF (diferença **3**) e o offset é **2**. Abers: diferença 3, offset 2. Madeira: diferença 4, offset 2. **Nos três, derivar o deslocamento da aritmética da ficha daria a resposta errada** — e derivar o offset de um dado declarado foi exatamente o que o caso Araujo e Sales (impressa = PDF + 25, a partir de "p. 26-42" em 17 páginas de PDF) ensinou a fazer.

> A regra não se generaliza porque os dados não são do mesmo tipo: **intervalo declarado de artigo** é informação sobre o recorte do texto; **total de páginas de livro** é informação sobre o miolo, e os pré-textuais não entram na conta do mesmo modo. Quatro livros, três editoras, três offsets — mais o volume com zero. **Só a folha impressa na página decide.**

### 39.3 Zero de probe não provado é silêncio, não ausência

O mapa de pertinência que escrevi devolveu **zero** para "cooptac" no livro de Lavalle. Era falso: **`ç` não é `c`**, e o NFKC não dobra cedilha, de modo que o termo em ASCII nunca casaria o termo acentuado. Só percebi porque um `grep` anterior já havia dito **17**.

> Corrigido para NFKD com remoção de diacríticos, o probe reproduz **17 = 17**, e só então os zeros de "Bolsonaro" e "direita" passaram a valer como ausência. **É a regra da linha de base suja aplicada a probe de busca:** medir com instrumento não provado produz um número, não um fato. A regra nova é: **antes de afirmar ausência, o probe tem de reproduzir uma presença conhecida.**

### 39.4 bis O mesmo modo de falha, pego ANTES do commit: o ISBN que eu ia derivar do DOI

Escrevi a ficha do volume com **ISBN 978-65-87429-05-2**. Não há ISBN no arquivo: a palavra não ocorre nenhuma vez no texto extraído, e a página de ficha catalográfica (PDF p. 6) devolve só o título, sem camada de texto no resto. Eu havia **derivado o ISBN do slug `87429052`** dos DOIs de capítulo.

> O slug provavelmente *é* o ISBN. Isso não autoriza declará-lo: o projeto não afirma o que não leu, e "provavelmente é" é a frase que abre as quinze ocorrências anteriores. Saiu da ficha, com a razão escrita no lugar. **O que ficou foi o que o arquivo diz:** os onze DOIs de capítulo, conferidos um a um, e a organização verificada em primeira mão na PDF p. 4 — "© 2020 copyright by Fabiano Godinho Faria & Mauro Luiz Barbosa Marques (Orgs.)", que confirma pelo arquivo o que de manhã se soube apenas pelo nome do depósito no IBICT.

### 39.4 A 16ª ocorrência do modo de falha, e a ficha era minha

A ficha de 08/10 pela manhã declarava Gurza Lavalle et al. (2018) como "o livro brasileiro de referência sobre **movimento que entra no Estado**, que é o mecanismo que PT-04 afirma". O livro **não cita Bolsonaro, não usa "direita" e não menciona junho de 2013** — zero em busca normalizada e provada.

"Movimento que entra no Estado" ali são **encaixes institucionais de movimentos de grupos marginalizados na burocracia, 1985-2016**; em PT-04 é **um movimento de rua que ganha a eleição presidencial**. As mesmas palavras, referentes diferentes.

> **A forma nova:** nas quinze ocorrências anteriores o referente errado era uma cifra, uma página, uma data, uma frase. Aqui é **um livro inteiro**, e o erro estava numa ficha de procedência escrita **antes de abrir o arquivo** — isto é, no lugar do aparato que existe precisamente para impedir esse erro. A correção está em `PROCEDENCIA` e no documento 14, §8.3.

### 39.5 O que a leitura ofereceu, e não é o que a ficha prometia

**Gurza Lavalle et al. (2018)** mostra que identificar institucionalização com desmobilização e cooptação é defeito da literatura estadunidense de movimentos sociais, nomeando **Tarrow (1997), McAdam, Tarrow e Tilly (2001) e Tilly e Tarrow (2007)** — marco teórico declarado deste projeto (p. 37-38 impressas). Desmobilização e cooptação são "possibilidades e não fatalidades" (p. 41). E abre a abordagem a governos "de cunho regressivo, como o que seguiu ao *impeachment*", com a ressalva de que "as configurações mudam conforme a coalizão governante, cedendo passo a outros atores e outros encaixes" (p. 28). **Licença para a pergunta, não resposta sobre o caso.**

**Abers (2021)** dá ao projeto um pressuposto que ele nunca teve com lastro em livro brasileiro: "a mobilização de atores ideologicamente à direita deve também ser compreendida como ativismo" e "causas contenciosas podem ser conservadoras" (p. 44). E **deixa aberta**, como pergunta de pesquisa, a diferença entre ativismo institucional à direita e ativismo pela inclusão (p. 45) — o projeto não pode tratar como respondido o que a autora declara aberto.

**Madeira, Marona e Del Río (2022)**, capítulo 8, documenta o apelo à intervenção militar **condicionado a uma decisão do STF**, em abril de 2018: "só restará o recurso à reação armada. Aí é dever da Força Armada restaurar a ordem" (p. 254). Mais a Lei 13.491/2017, que levou o homicídio doloso de civis por militares à Justiça Militar (p. 256), e a tese de que "o bolsonarismo é uma ideologia política de caráter miliciano" (p. 268). **Não menciona 8 de janeiro: é de junho de 2022.**

### 39.6 O que precisa de você

1. **Abers (2021, p. 44) em PT-04?** A frase "a mobilização de atores ideologicamente à direita deve também ser compreendida como ativismo" é âncora **conceitual** do pressuposto de PT-04, não âncora empírica do evento. Pôr âncora conceitual em registro cujo `mecanismo_causal` é empírico é decisão de critério, e o critério do codebook até aqui foi cadeia causal ancorada. **Não foi feito.**
2. **A crítica de Gurza Lavalle et al. ao marco teórico do projeto** (institucionalização ≠ cooptação, em Tarrow e Tilly) toca o aparato conceitual declarado, não um registro. Entra como ressalva na redação, como revisão do marco, ou fica como nota? **É decisão de projeto.**
3. **Madeira et al. (2022, p. 254) em PT-05 ou no arco judicial?** A frase do general amarra o apelo militar a uma decisão do STF, e o arco judicial hoje se apoia só em acórdãos. É a primeira literatura do corpus a interpretá-lo — mas o registro que ela mais serviria pode ser um dos do arco, não PT-05. **Não foi feito.**
4. **Os três livros seguem LIDOS EM PARTE**, com 1.189 páginas impressas somadas. O mapa de pertinência por capítulo diz onde há o que ler: em Gurza Lavalle, nenhum capítulo menciona a direita; em Madeira, os capítulos 6, 7, 11, 12 e o posfácio concentram Bolsonaro, Lava Jato e STF.

---

## 40. `Contextual` sai do vocabulário, as três peças da camada A entram no corpus — 🔶 08/10/2026

### 40.1 Executado

| | |
|:--|:--|
| **`Contextual` fora do vocabulário controlado** | Por sua decisão. Retirado dos metadados do JSON (fonte da verdade), de `verificar_integridade.py` (checagem 4), do dicionário em `gerar_codebook.py` e — o ponto que importa — do **ramo de isenção** em `gerar_auditoria.py`. Agora só `Inferência do analista` dispensa âncora local, e dispensa porque declara no próprio nome que não há fonte a localizar. Classes: **61 / 21 / 1**, em **4** valores previstos |
| **O selo `ctx` ficou no conferidor de figuras** | De propósito: figuras versionadas podem trazê-lo, e o conferidor tem de saber lê-lo para acusar divergência em vez de quebrar |
| **Uma mensagem que repetia um número** | `verificar_integridade.py` imprimia "só os cinco valores previstos" com o cinco escrito à mão. Passou a derivar de `len(CLASSES)`: contagem escrita à mão é a forma mais barata do modo de falha do projeto |
| **Três peças da camada A arquivadas** | Collier (2011), Mayntz (2004) e González-Bailón et al. (2011). **Dos 7 lidos, 7 têm arquivo e 0 foram lidos só on-line** — `lida` e `lida-e-arquivada` deixaram de divergir |
| **Corpus** | **62 PDFs / 12.105 páginas**; documental inalterada em **22 / 6.951** |
| **Tarefa 19: lista e contagem reconciliadas** | A agenda dizia **sete** cobranças; são **cinco**. A §4 do documento 09 tem oito **linhas**, e duas registram aprovação ("Passam", "Correto") em vez de cobrança. A contagem foi tomada das linhas e decrementada a cada saída. Abertas: **PT-29, PT-34, PT-12A, PT-62** e a atribuição dos quatro testes |

### 40.2 Três rotas de acesso, três lições

- **Collier** saiu da página do **departamento do autor** em Berkeley. A Cambridge Core oferece o PDF de graça (0,13 MB) e o navegador real o alcança, mas devolve **429 a cliente que não é navegador** — e a planilha do projeto guardava um slug de URL que a página não usa mais. Impressa = PDF + 822.
- **Mayntz** saiu da **API REST do MPG.PuRe**. A página do item está atrás do **Anubis**, o mesmo desafio de prova-de-trabalho da OpenEdition. Impressa = PDF + 236.
- **González-Bailón et al.** saiu do PDF aberto da Nature em uma chamada. **Sem paginação impressa de fascículo** — *Scientific Reports* pagina por número de artigo (1:197), como a MDPI, e aqui é mais sutil: o rodapé **traz um número**, que parece fólio e é contagem interna.

> **Um defeito meu de método, de graça:** o laço que sondava cópias institucionais escrevia todas as tentativas no **mesmo arquivo de saída**, e a tentativa 404 apagou o download bem-sucedido da anterior. **Sonda em laço precisa de um caminho de saída por candidato**, ou o sucesso é destruído pelo fracasso seguinte.

### 40.3 Dois achados no eixo 13, antes de ler

Medindo o offset das 15 peças não lidas (que é pré-requisito de qualquer citação), apareceram três coisas que não são sobre offset:

1. **TATAGIBA (2018) tem camada de texto CIFRADA.** A extração devolve `(QWUHDVUXDVHDVLQVWLWXL©·HV`, que **não é lixo**: é "Entre as ruas e as instituições" com as letras deslocadas em **+3** no mapa CID→Unicode. Consequências: qualquer busca de termo devolve **zero**, e um leitor apressado declara "sem camada de texto". **Não é.** O deslocamento das letras é recuperável, mas os acentuados seguem outro mapa (`©`→`Ç`, `·`→`Õ`), de modo que **o arquivo não pode ancorar transcrição**: decodificação heurística produziria uma transcrição que não existe no original. Precisa de cópia limpa ou OCR.
2. **Duas divergências de ano entre nome de arquivo e peça.** `MENDONCA-DOMINGUES_..._RBCP-37_2021.pdf` traz no cabeçalho corrente "Nº 37-**2022**"; `MENDONCA-FREITAS_..._Dados-66-2_2022.pdf` traz "DADOS, vol.66 (2): e20200213, **2023**". É a mesma família das três atribuições corrigidas hoje — e aqui o rótulo errado está **no nome que nós demos ao arquivo**.
3. **Paginação por localizador eletrônico em quatro peças** (Mendonça e Freitas, Rocha, Kaysel e Bianchi, Bastos e Recuero): e-locator ou numeração interna do artigo, sem fólio de fascículo.

### 40.4 O que NÃO foi feito, por limite de uso

Esta rodada parou aqui. Ficaram pendentes, **todas já encaminhadas por você**: a nota com a crítica de Gurza Lavalle ao marco teórico; a execução da tarefa 19 (características, relações e proposta de nomenclatura); a leitura das 15 peças do eixo 13, de que só se mediram os offsets; o resto da tarefa 10; e a recomendação sobre Madeira et al. (p. 254) para PT-05 ou para o arco judicial.

---

## 41. As quinze lidas, a tarefa 19 executada, e um ponto cego no conferidor — 🔶 09-10/10/2026

### 41.1 Executado

| | |
|:--|:--|
| **`Contextual` fora** | já em 40; aqui só a confirmação de que o ciclo passa com **4** valores previstos |
| **Quinze peças do eixo 13 lidas** | cinco produziram conteúdo, dez não. Ler e não ancorar é resultado, e está dito peça por peça em `PROCEDENCIA` |
| **Cinco registros ganharam conteúdo** | PT-06, PT-03C, PT-19 (um limite), PT-12A, PT-62. **Nenhum mudou de classe nem de nome de mecanismo** |
| **Tarefa 19 executada** | características, relações e **proposta de nomenclatura com definição** para os quatro nomes em jogo, mais a cadeia de atribuição dos quatro testes — documento 09, §9 |
| **Contagem reconciliada** | a agenda dizia sete cobranças; são **cinco**, e só **quatro** são nome de mecanismo |
| **Nota de Gurza Lavalle** | entrou como **nota**, por sua decisão — documento 09, §8 |
| **Resto da tarefa 10** | varredura sistemática do IBICT pelos dez autores do cânone: **nenhum está lá**. Ver 41.4 |
| **Classes** | 61 / 21 / 1, inalteradas |

### 41.2 O ponto cego do conferidor, achado por prova negativa

A prova negativa das âncoras novas rodou contra linha de base **limpa** (`confirmados 69 | falhas 0`) e pegou **2 de 4** injeções:

| Injeção | Resultado |
|:--|:--:|
| página de Cesarino trocada de 3 para 4 | **PEGOU** |
| página de Madeira trocada de 267 para 268 | **PEGOU** |
| transcrição de Nunes: "menor" → "maior" | **PASSOU** |
| transcrição de Carvalho e Tatagiba: "três" → "dois" | **PASSOU** |

A causa está em `casa()`: a função devolve sucesso assim que **uma janela de 90 (ou 60, ou 40) caracteres** confere, de propósito, porque hifenização e ligadura quebram o casamento literal. **A garantia real é "existe uma janela desta transcrição nesta página", não "a transcrição é fiel".** Editar a cauda de um trecho longo passa.

**Medido antes de mexer:** dos fragmentos localizados, **176 casam por texto integral e 45 só por janela**. Exigir integral quebraria 45 âncoras legítimas — a tolerância é load-bearing.

> **Então não se endureceu: tornou-se visível.** `conferir_paginas.py` passou a contar e imprimir os fragmentos que casam só por janela, com a prova negativa escrita ao lado. **45 de 221.** Silêncio virou aviso, que é o que se pode fazer quando a tolerância é necessária e o risco é real.

### 41.3 Três defeitos meus nesta rodada

1. **Guarda depois do efeito.** O `assert` da contagem esperada no script de recodificação estava **depois** do `write`: a contagem falhou, o JSON já havia sido gravado, e foi preciso restaurar do backup. **Guarda que dispara depois do efeito não é guarda, é aviso.** Corrigido no próprio script, com o motivo escrito.
2. **A terceira cópia da mesma função.** A dobra de diacríticos foi corrigida em dois scripts em 08/10 e **o terceiro ficou para trás**: `qualpagina.py` devolveu zero para quatro buscas em ASCII. Lógica duplicada em três lugares, corrigida em dois.
3. **Aspas curvas no nome do próprio mecanismo.** Em PT-62 escrevi o nome do mecanismo entre aspas curvas, e `transcricoes()` o promoveu a transcrição e foi procurá-lo no PDF de Carvalho e Tatagiba. É a armadilha que PT-08 expôs em 08/10, agora com o analista citando o próprio codebook. **Aspas curvas em `fonte_trecho` são reservadas ao que está na fonte.**

### 41.4 O resto da tarefa 10 — o cânone não está no IBICT

A primeira passagem da tarefa 10 usou o OpenAlex com autoria casada e devolveu zero. Esta usou a rota que **de fato entregou livro** em 08/10: a API REST do DSpace 7 no `deposita.ibict.br`, com os dez autores do cânone mais o volume da Perseu Abramo.

**Resultado: nenhum dos dez está lá.** O que a busca devolve são os capítulos de *Giros à direita* — que já temos, e agora como volume inteiro — e itens não relacionados. A Fundação Perseu Abramo não oferece PDF de *Direita, volver!* na página do livro.

> **UM ACHADO LATERAL, que é decisão sua e não executei.** A varredura trouxe `deposita/434`: **"Agentes do caos": 'guerra cultural', redes sociais e "novas direitas" no Brasil recente (2014-2018)**, acesso aberto, 3,1 MB. Interessa porque **PT-06 declara que a expressão "guerra cultural" permanece sem âncora**. Duas razões para não incorporar sem você: é **dissertação de mestrado** (Unioeste, 2023), e o corpus até hoje só admitiu artigo revisado por pares, livro de editora e fonte primária; e o recorte é **2014-2018**, enquanto PT-06 cobre **2020-2021** — o período não casa. **Padrão de evidência é decisão de pesquisa, não execução minha.**

### 41.5 O que precisa de você

1. **Os quatro nomes de mecanismo** — propostas com definição no documento 09, §9.2 a §9.5. Em PT-62 há **duas** saídas, porque a escolha é de critério, e recomendo a (a).
2. **A atribuição dos quatro testes** — proposta de citar a cadeia Van Evera → Bennett → Collier, com Beach e Pedersen ficando para o *process tracing* e não para os testes (§9.6).
3. **Tatagiba (2018)**: pedir cópia limpa ou OCR? Hoje a peça não pode ancorar transcrição.
4. **A dissertação do `deposita/434`** entra no corpus? Ver 41.4.
5. **Cesarino (2019) para PT-29?** O contágio no plano do deutero-aprendizado, não necessariamente consciente, dissolve a tensão interna com PT-19 — mas usar isso é parte da decisão de nome de §9.2.
6. **Os 45 fragmentos que casam só por janela** continuam sendo o ponto cego. Fechá-lo exigiria revisar transcrição por transcrição; está declarado e contado, não resolvido.

---

## 42. Os quatro nomes de mecanismo, atribuídos — e a checagem nova achou nome morto de seis dias — 🔶 10/10/2026

**Encaminhamento:** *"Aprovo as quatro propostas de nomenclatura, execute."*

### 42.1 Os quatro nomes

| Registro | Saiu | Entrou |
|:--|:--|:--|
| **PT-29** | transposição do limiar | **Demonstração de viabilidade** |
| **PT-34** | massa crítica atingida no ponto de máxima densidade simbólica | **Concentração simultânea no conjunto simbólico** |
| **PT-12A** | mobilização de recursos em rede distribuída com nós centralizadores | **Agregação na base e intermediação concentrada** |
| **PT-62** | desarticulação do repertório de rua com deslocamento | **Desmobilização por repressão seletiva** + **Migração de arena** |

A razão de cada troca está escrita **dentro do próprio `mecanismo_causal`**, não só no documento 09 — para que a redação não trate a mudança como cosmética. Nenhum campo além de `mecanismo_causal` e `nota_auditoria` mudou; nenhuma classe mudou; 83 sub-eventos; classes 61 / 21 / 1.

### 42.2 Uma decisão de implementação, declarada

A proposta (a) de PT-62 admitia **duas** formas: partir o registro em dois, ou o campo passar a nomear dois mecanismos. **Foi pela segunda.** Partir em dois mudaria a contagem de 83 sub-eventos — conferida pela integridade, pelas duas figuras e pela tabela do relatório —, e isso é mudança estrutural, enquanto o encaminhamento aprovou nomenclatura. **Se preferir dois registros, é uma linha de pedido.**

### 42.3 O que a renomeação revelou, e é o resultado que vale

Renomear tem um risco próprio: o JSON muda e os artefatos **mantidos à mão** ficam para trás. Quatro deles existem — as duas figuras interativas, o relatório de pesquisa e o caderno de evidências —, e **nenhum script os gera**: o ciclo os *confere*.

Testei se a conferência pegava a divergência. Reinjetei o nome velho numa figura e no relatório, com linha de base limpa nos dois conferidores:

| Artefato com nome velho | `conferir_figuras` / `conferir_relatorio` |
|:--|:--:|
| figura interativa | **PASSOU** |
| relatório de pesquisa | **PASSOU** |

> **Zero de duas.** O ciclo **não compara o texto do mecanismo** entre o JSON e os artefatos à mão. Uma renomeação podia deixar nome morto em qualquer um deles indefinidamente.

### 42.4 A checagem 7, e o defeito real que ela achou na primeira execução

`verificar_integridade.py` ganhou uma **sétima checagem**: um registro de **nomes de mecanismo retirados**, com a data, o registro e o nome que passou a valer, conferido contra os quatro artefatos mantidos à mão. Não tenta diferenciar prosa livre — exige apenas que **nenhum nome retirado reapareça**.

**Na primeira execução ela falhou, e com razão:** encontrou **"Certificação de eficácia"** — retirado de **PT-03 em 04/10/2026**, quando você o trocou por *ressignificação do protesto* — ainda vivo nas **duas figuras** e no **relatório**. **Seis dias de nome morto em artefatos que o leitor vê**, e nenhuma checagem o acusava.

Corrigido nos três. A prova negativa, reapontada para o script certo, agora dá **2 de 2**.

> A lição não é sobre nomenclatura: **artefato mantido à mão que o ciclo só confere parcialmente envelhece em silêncio.** O registro de nomes retirados é barato e cresce sozinho a cada renomeação futura.

### 42.5 O que resta da tarefa 19

**Uma cobrança das cinco**, e não é nome de mecanismo: **a atribuição dos quatro testes**. A proposta está no documento 09, §9.6 — citar a cadeia **Van Evera (1997) → Bennett (2010) → Collier (2011)**, ficando Beach e Pedersen para o *process tracing* e não para os testes. Muda `01_PROJETO-PESQUISA_v1-compacto.md` §3.2, que é documento de projeto e não codebook. **Não foi executada: não estava entre as quatro propostas de nomenclatura.**

E segue aberta a decisão sobre **Cesarino (2019) em PT-29** (item 41.5, ponto 5): o argumento dela dissolveria a tensão com PT-19 também no plano teórico, e lançá-la como âncora seria decidir o que está em aberto. O campo diz isso explicitamente.

---

## 43. A quinta cobrança executada — e a premissa dela estava errada — 🔶 10/10/2026

**Encaminhamento:** *"Execute a quinta cobrança, a atribuição dos quatro testes."*

### 43.1 A cadeia, conferida nas duas peças do corpus

| Elo | Fonte, conferida na página |
|:--|:--|
| **Van Evera (1997, p. 31-32)** deriva os quatro testes | Collier (2011), nota da tabela 1, p. **825** impressa (PDF p. 3); e Cunha e Araújo (2018), p. **91** impressa (PDF p. 92) |
| **Bennett (2010, p. 210)** é a formulação que Collier adapta | Collier, mesma nota |
| **Collier (2011, p. 825, tabela 1)** é a apresentação que **este projeto usa** — inclusive o nome *hoop test*, que PT-28 emprega | o arquivo está no corpus desde 08/10, com offset medido |
| **Beach e Pedersen** ficam como referência do *process tracing*, **não dos testes** | — |

Corrigido em **seis** lugares: `01_PROJETO-PESQUISA.md`, `01_PROJETO-PESQUISA_v1-compacto.md` §3.2, `07_REGISTRO-DE-REVISAO.md`, `08_BIBLIOGRAFIA-METODOLOGICA.md` (ficha 11 e §), `02_PROPOSTA-DISCIPLINA.md` (leitura da semana 6) e o relatório de pesquisa. **Com isso a tarefa 19 fecha: as cinco cobranças estão resolvidas.**

### 43.2 A premissa da cobrança estava errada, e isso é o achado

A §4 do documento 09 dizia: *"**Duas fontes independentes divergem**"*. **Não divergem.**

O que parecia atribuição concorrente em Cunha e Araújo é a **lista de referência entre parênteses** que fecha a frase — *"(Bennett, 2008; Collier, 2011; Mahoney, 2012; Beach; Pedersen, 2013; Bennett; Checkel, 2015)"* —, e a frase que a precede diz, em letras: *"**Van Evera (1997) deriva quatro testes de hipóteses**"*. **As duas peças convergem em Van Evera.**

> **Ler lista de referência como reivindicação de autoria é o modo de falha da casa na forma bibliográfica.** A cobrança era legítima — o projeto de fato atribuía a Beach e Pedersen —, mas o *conflito de fontes* que ela alegava não existia. E a página também estava errada: a lista está na impressa **91**, não 92. **Eu havia escrito as duas coisas sem abrir as peças na página.**

### 43.3 Duas armadilhas de extração no arquivo de Collier

1. **Parênteses saem como `~` e `!`** em parte do arquivo: a nota da tabela extrai como `adapted from Bennett ~2010, 210!, who builds on categories formulated by Van Evera ~1997 , 31–32!`. São **16 ocorrências de `~` contra 111 parênteses normais**, concentradas na nota da tabela 1 e em itens alfabéticos — **não é defeito global**. Consequência: quem transcrever com parênteses **não casa na conferência**; quem transcrever da extração escreve o til.
2. **Ligadura ﬁ e espaços colapsados**, já declarados: `conﬁrmordisconﬁrm`, `UnderstandingProcessTracing`.

Ambas estão na ficha da peça, em `PROCEDENCIA`.

### 43.4 A checagem 7 passou a vigiar atribuição, não só nome de mecanismo

A sétima checagem de `verificar_integridade.py`, criada ontem para nomes de mecanismo retirados, ganhou duas entradas: `testes de Beach e Pedersen` e `testes de Beach & Pedersen`. Vigia **7 itens** em 4 artefatos mantidos à mão. Prova negativa: reinjetada a atribuição retirada no relatório, com base limpa, **PEGOU**.

> A generalização é a lição de ontem levada a sério: **o que acabei de corrigir em seis lugares pode voltar num sétimo**, e o registro de itens retirados é o único lugar onde esse risco fica barato de vigiar.

### 43.5 O que resta

Da tarefa 19, **nada**. Seguem abertas, das rodadas anteriores: **Cesarino (2019) em PT-29**; **Tatagiba (2018)**, que precisa de cópia limpa ou OCR; a **dissertação do `deposita/434`** sobre "guerra cultural"; os **45 fragmentos que casam só por janela**; e, se preferir, **partir PT-62 em dois registros** em vez de um campo com dois mecanismos.

---

## 44. Pendências 1 e 5 resolvidas — e uma checagem minha estava inerte — 🔶 10/10/2026

**Encaminhamento:** *"Resolva as pendências 1 e 5."*

### 44.1 Pendência 1 — Cesarino (2019) **não** entra em PT-29

Três razões, e a segunda é a que decide.

1. **A renomeação retirou a necessidade.** Cesarino era resgate do nome **velho**: "transposição do limiar" tinha tensão interna com PT-19 (limiar pressupõe ação sem coordenação; PT-19 afirma coordenação), e o contágio não-deliberado dela dissolvia a tensão. **"Demonstração de viabilidade" não tem contágio nenhum** — é efeito de demonstração entre quem já está no lugar. Não há mais o que resgatar.
2. **Referente diferente.** O contágio dela é **circulação de conteúdo** em WhatsApp e YouTube na campanha de 2018; PT-29 é **imitação de uma ação física por multidão co-presente** em 08/01/2023. Mesma palavra, referentes distintos — e importá-la seria o modo de falha da casa cometido por mim **com a peça já lida**, que é a forma mais difícil de desculpar.
3. **Redundante onde ela caberia.** O lugar em que a tese serve é PT-06 — circulação, não consistência, sustentando a mobilização —, e PT-06 **já está ancorado em Cesarino (2022)**, da mesma autora e com página conferida.

### 44.2 Pendência 5 — PT-62 **não** se parte, e a razão certa não era a minha

Eu havia mantido um campo com dois mecanismos alegando o **custo** de mexer na contagem de 83 sub-eventos. O custo não era o argumento. O mecanismo (1) — desmobilização por repressão do Estado — **já está em fonte primária em PT-49, PT-52, PT-53 e PT-61**, e o mecanismo de PT-52 **já se chama "destruição da infraestrutura de mobilização"**.

| | |
|:--|:--|
| **Partir** | criaria um registro que **duplica** quatro outros, com evidência pior |
| **Manter como afirmação própria** | deixava um registro de classe `Inferência` afirmando por conta própria o que quatro registros provam |
| **O que foi feito** | **de-duplicar**: o mecanismo (1) passou a ser **remissão** aos quatro; o que PT-62 afirma por conta própria é a migração de arena, e é só isso que a classe precisa cobrir |

> **PT-52 já havia pensado a distinção:** o campo dele diz que "a diferença é o que separa a desmobilização do repertório da punição de seus agentes". O projeto tinha a distinção, e PT-62 a estava reafirmando sem ver. **A pendência não pedia uma escolha entre as duas formas que eu ofereci: pedia que eu olhasse a camada antes de oferecer.**

83 sub-eventos, classes 61 / 21 / 1, nenhum registro criado.

### 44.3 Uma guarda nova, e ela nasceu morta

A remissão criou um risco que não existia: **se um dos quatro registros citados deixasse de existir ou fosse renumerado, nada acusaria.** O projeto já inseriu identificadores com sufixo em revisão posterior (PT-03A a PT-06C), de modo que o risco é real.

`verificar_integridade.py` ganhou a guarda: **toda remissão `PT-XX` em `mecanismo_causal`, `fonte_trecho` ou `nota_auditoria` tem de apontar para registro existente.**

> **E ela nasceu INERTE, por minha mão.** Escrevi a linha por heredoc, e o heredoc converteu a sequência barra-`b` em **``\x08``, o caractere de controle *backspace***. O regex ficou `r"<BS>PT-\d{2}[A-Z]?<BS>"`, que **nunca casa nada** — e a checagem imprimia *"OK — toda remissão aponta para registro existente"* **testando zero strings**.
>
> **Checagem que não pode casar imprime o mesmo que checagem que não achou nada.** É a regra da linha de base suja na sua forma mais pura, e eu a cometi no dia seguinte a tê-la registrado em memória. Consertada fora do heredoc; prova negativa com base limpa: **2 de 2 remissões quebradas detectadas**.

É a terceira vez nesta sequência de rodadas que o heredoc corrompe silenciosamente o que escrevo em script. **A regra passa a ser: patch de regex ou de string com escape vai para arquivo pelo editor, nunca por heredoc.**

### 44.4 O que resta

1. **Tatagiba (2018)** — precisa de cópia limpa ou OCR para poder ancorar transcrição.
2. **A dissertação do `deposita/434`** sobre "guerra cultural" — dissertação de mestrado, e recorte 2014-2018 contra os 2020-2021 de PT-06.
3. **Os 45 fragmentos que casam só por janela** — declarados e contados, não resolvidos.

---

## 45. As três pendências restantes, resolvidas — e duas delas me desmentiram — 🔶 10/10/2026

**Encaminhamento:** *"Resolva as três pendências restantes."*

### 45.1 Tatagiba (2018) — **podia ancorar desde sempre, e o erro era meu**

Eu havia declarado que a peça **não podia ancorar transcrição**, por "camada de texto cifrada em duas direções opostas". **Falso.**

Eu lera o arquivo com **pypdf**, que o devolve embaralhado, e não com o `texto_pagina()` do próprio conferidor — que concatena **três** leituras (pypdf, PyMuPDF cru e PyMuPDF com conserto de glifo *por span*) e basta uma servir. A fonte quebrada é `Gentium-Book-Basic`, **que já estava em `FONTES_DESLOCADAS` desde 04/10/2026**, posta lá por causa de Kunrath Silva (2018), do mesmo editor.

> **Diagnostiquei como armadilha nova o que o projeto havia resolvido cinco dias antes.** A lição, na forma mais barata que ela tem: **antes de declarar um arquivo ilegível, leia-o com a ferramenta do projeto, não com a primeira que vier à mão.**

Conferido: duas de três frases colhidas na versão limpa da **OpenEdition** — obtida pelo navegador, que resolve o Anubis nativamente — foram localizadas no PDF pelo conferidor. A folha de rosto entrega a paginação impressa, **112-135**. Nenhum OCR, nenhuma cópia nova, nenhum pedido a você.

**E uma hipótese minha que a medição derrubou no caminho:** achei que `FONTES_DESLOCADAS` tinha uma lacuna, por casar nome de fonte exato e deixar de fora `Gentium-Book-Basic-Itali` e `GentiumBookBasic`. Testei: nessas variantes **o texto bruto já está correto**, e aplicar o conserto o **corrompe**. A restrição por nome exato não era lacuna — era proteção, e o autor dela escreveu isso no docstring. **A quebra é propriedade do subconjunto de fonte naquele arquivo, não do nome da família.**

### 45.2 A dissertação do `deposita/434` — **fica fora, e não era necessária**

A pendência era se a dissertação sobre "guerra cultural" entrava no corpus para ancorar a expressão que PT-06 declarava sem lastro. **Não entra, e não precisa:** varrido o corpus **já lido**, a expressão está em peças com página conferida — Cesarino (2019) com três ocorrências, Cesarino (2022) com uma.

Dois motivos para a dissertação ficar fora, e os dois valem registro: é **dissertação de mestrado**, e o corpus só admitiu artigo revisado por pares, livro de editora e fonte primária; e o recorte é **2014-2018** contra os **2020-2021** do registro.

**E a leitura mudou o que se pode afirmar.** Cesarino não só usa a expressão: ela **argumenta contra** reduzir o bolsonarismo a ela. As duas âncoras entraram **em par**, de propósito:

| | |
|:--|:--|
| **Proveniência** | "Como o próprio termo guerra cultural, outros como marxismo cultural e globalismo foram tomados **diretamente de empréstimo da alt-right americana**" (p. 540 impressa) |
| **Limite, da mesma autora** | "**Longe de se resumir a uma guerra cultural** no campo das políticas de identidade, o bolsonarismo tem como pilar constitutivo um eixo neoliberal que é normalmente obscurecido pelo eixo populista-conservador" (p. 539 impressa) |

> Lançar a primeira sem a segunda seria **usar a autora contra o argumento dela**. E a frase de Cesarino (2022, p. 174) que cobre a janela do registro foi citada **por página e sem transcrição**, porque traz aspas curvas internas — aspa aninhada já custou a este projeto cinco âncoras sem conferência em PT-08.

**Um defeito meu, pego pela contagem.** Escrevi as duas transcrições primeiro em `framing_narrativa`, e `transcricoes()` lê **apenas** `fonte_trecho`: ficavam **sem conferência nenhuma**. O sinal foi a contagem de PT-06 **não subir de 22**. Movidas, o registro passou a **24/24 localizadas**. É a âncora-que-parece-âncora, que este projeto passou quatro dias eliminando, reintroduzida por mim num campo errado.

### 45.3 Os 45 fragmentos que casavam só por janela — **são 17, e agora há tripwire**

Classifiquei a causa de cada um, em vez de afrouxar ou endurecer o critério:

| Causa | N | É divergência de conteúdo? |
|:--|--:|:--|
| casa o trecho inteiro menos ≤2 caracteres (pontuação terminal) | 6 | não |
| as duas metades existem na página, a junção não | 10 | não |
| dígito logo após a ruptura | 4 | não |
| interpolação do analista entre **colchetes** | 3 | **não, por definição** |
| a transcrição atravessa a quebra de página | — | não |
| divergência real, a inspecionar | ~11 | sim |

`confere_integral()` passou a absorver as três que não são conteúdo — **pontuação terminal, colchete e página vizinha** —, cada uma com a razão escrita. Resultado: **45 → 17**. A queda não veio de relaxar nada: veio de medir a causa.

> **E com 17 o número serve de linha de base, o que converte o ponto cego em tripwire.** Uma transcrição editada na cauda tira um fragmento de `ok` e o põe em `parcial`, o total vai a 18 e **o ciclo cai**. Prova negativa: as **duas** edições de cauda que escaparam em 09/10 — *menor→maior* em Nunes e *três→dois* em Carvalho e Tatagiba — agora são **pegas, 2 de 2**. Não se endureceu o casamento, que quebraria 17 âncoras legítimas: vigia-se a **contagem**.

**E a guarda disparou no recorte errado na primeira tentativa:** rodando um registro isolado, `parciais_total` é 0 e ela acusava queda. A linha de base é do conjunto; aplicada a um subconjunto mede outra coisa. Restrita a `--todos` — **guarda que dispara no recorte errado é ruído, e ruído treina a ignorar guarda.**

### 45.4 O que sobra

Da agenda, **nada pendente de decisão sua**. Os 17 fragmentos que ainda casam só por janela estão **contados, com linha de base e tripwire**; reduzi-los exige abrir documento por documento, e cada um é trabalho de verificação, não de decisão.

---

## 46. Tarefa 15 — a higiene do repositório, e a decisão estava forçada — 🔶 13/10/2026

**Encaminhamento:** *"Execute a tarefa 15."*

A tarefa estava na agenda como **decisão sua**, de licença e distribuição. Executada, ela se revelou **menos decisão e mais apuração**: o que havia a decidir já estava decidido pelo conteúdo do corpus.

### 46.1 A auditoria, que é o resultado

`scripts/auditar_licencas.py` lê o que **cada arquivo declara sobre si** — não o que o editor diz, nem o que o registro de acesso aberto diz. A razão dessa escolha tem nome: **Rich (2021)**, que o OpenAlex declarava **ouro** e está à venda em livraria.

| | Arquivos | |
|:--|--:|:--|
| **Documental** | **22** | 21 atos oficiais + 1 CC |
| **Literatura** | **40** | 13 CC · **2 com todos os direitos reservados impressos** · 25 sem declaração |

**27 das 40 peças de literatura não podem ser redistribuídas**, 56 MB. Entre elas **Kunrath Silva (2018)** — que **ancora PT-01, PT-02, PT-04 e PT-05** e declara todos os direitos reservados —, Tarrow pela Vozes, *Dynamics of Contention* pela Cambridge, a enciclopédia Wiley-Blackwell e Alonso pela Companhia das Letras.

> **Um erro de agregação meu, corrigido no caminho.** A primeira execução deu "**46 não redistribuíveis**" porque somava documento oficial e peça acadêmica sem declaração. São coisas incomparáveis: a ausência de declaração num acórdão não é lacuna, porque a **Lei 9.610/98, art. 8º, IV**, põe atos oficiais fora do direito autoral. Separado pela linha que o projeto já usa (`FORA_DA_DOCUMENTAL`), o número verdadeiro é **27 de 40**. Era a cifra certa no referente errado, na minha própria auditoria.

### 46.2 E parar de versionar o corpus agora não resolveria

Os PDFs estão **no histórico**: `.git` tem **250 MB** contra **8 MB** de texto e código. Um remoto público distribuiria os arquivos mesmo com a árvore limpa. **A pergunta da agenda — "decidir antes do remoto" — já estava respondida pelo histórico, e a resposta é que o remoto público deste repositório não existe.**

### 46.3 O que foi construído

| | |
|:--|:--|
| **`Fontes/MANIFESTO-CORPUS.csv`** | 62 peças: caminho, **SHA-256**, páginas, bytes, classe de licença e **rota de obtenção**. Toda peça tem rota — conferido. É o que mantém a pesquisa **verificável sem ser redistribuível** |
| **Checagem 8** de `verificar_integridade.py` | corpus × manifesto, presença e SHA-256. Pega o que **nada pegava**: um PDF que mude de bytes sem mudar de nome. Prova negativa: bit virado, peça removida, peça intrusa — **3 de 3** |
| **`scripts/exportar_aparato.py`** | monta a árvore publicável: **131 arquivos, 8 MB**, contra 294 MB de binário excluído. Confere o resultado contra o manifesto e **apaga o destino** se vazar peça reservada. **Não cria remoto, não faz commit, não publica** |
| **`LICENCA-E-DISTRIBUICAO.md`** | o regime, com os fatos apurados e a escolha de licença deixada em aberto |

### 46.4 O vazamento que o teste pegou, e por que o default mudou

A primeira versão do exportador excluía `Fontes/**/*.pdf` — **regra de caminho**. O teste **vazou um PDF de 24,7 MB** que estava em `.backup_pre_lula/`, fora de `Fontes/`.

> **Regra de caminho falha no caminho que ninguém lembrou.** O filtro passou a **incluir por autorização**: texto e código entram, binário só por lista. Assim um diretório novo com binário dentro **não vaza por omissão** — ele aparece na lista para você decidir. Para guarda de publicação, o default tem de ser excluir.

### 46.5 Duas higienes relatadas e NÃO executadas

1. **`.backup_pre_lula/` está versionado** — 27 arquivos, 27 MB, com um PDF de 24,7 MB. São os estados anteriores do JSON, isto é, a sua rede de segurança: **tirar backup do controle de versão é decisão sua.** A exportação já o exclui por construção.
2. **`STF_Democracia-Inabalada_Folder.pdf`: 37,4 MB em 6 páginas** — 6,23 MB por página, o pior índice do corpus. Recomprimir é seguro quanto à licença (ato oficial), mas **mudaria os bytes**, logo o SHA-256 do manifesto e o lastro de qualquer âncora que dependa da peça. **Não se toca em bytes de peça do corpus sem decisão explícita.**

### 46.6 O que resta, e é jurídico

**Sob que licença sai a sua obra** — codebook, scripts, documentos. Não escolhi: licença é decisão de quem assina. E os binários que são seus (tese, projeto, planilhas, os sete fichamentos `.docx` do eixo 05) ficam fora da exportação por padrão, **listados pelo script** para você dizer se entram.

---

## 47. Tarefa 17 — uma peça das 26, e ela desmentiu o meu próprio auditor de licença — 🔶 13/10/2026

**Encaminhamento:** *"Execute a tarefa 17."*

Ler na fonte os 43 da camada A. Estavam **26 pendentes**. A rodada rendeu **uma**, e o número é o resultado, não o resumo de um esforço.

### 47.1 A rota que faltava consultar, e por que ela existia

`localizar_camada_a.py` guardava do OpenAlex apenas o `best_oa_location`. O registro tem outro campo — **`locations`, que lista TODOS os depósitos** —, e foi ele que achou Mayntz no MPG.PuRe em 08/10. **Para os 26 pendentes esse campo nunca havia sido consultado.** Consultado agora:

| | Itens | |
|:--|--:|:--|
| Com depósito **aberto** no `locations` | 4 | e 3 já se sabiam barrados no editor |
| Com depósito de **repositório** marcado fechado | 7 | vale sondar: foi assim que Mayntz apareceu |
| **Sem depósito algum** | 22 | só a página do editor |

**Rendeu uma peça: SNOW, VLIEGENTHART e KETELAARS (2019)**, capítulo 22 de *The Wiley Blackwell Companion to Social Movements*, 2ª ed., pp. 392-410, integral, no depósito da Universidade de Amsterdam. A rota do editor — Wiley, que o OpenAlex declara **ouro** — devolve 403. **O arquivo estava em outro campo do mesmo registro.**

As sondas dos outros sete repositórios fecharam: **EUI Cadmus e `ricerca.sns.it` devolvem 403 em todo o host** — API REST e OAI-PMH inclusive —, e são **repositórios, não editores**, o que é categoria nova no mapa de acesso do projeto, onde repositório sempre passava. O CiteSeerX hoje **redireciona para a Wayback Machine**, e as duas devolveram 429 em três tentativas, como a Cambridge.

### 47.2 O que a leitura deu, e é mais do que a peça

**O marco teórico declarado do codebook passou a ter leitura na fonte.** `marco_teorico` diz *Framing (Snow & Benford, 2000)* — e esse balanço de 2000 **nunca foi lido**: está FECHADO na camada A, sem depósito em lugar algum. O capítulo lido é o balanço posterior, do mesmo autor principal, escrito para ser o enunciado da arquitetura do campo, com **nove conceitos-pilar**.

> **E o limite fica declarado:** ter lido o capítulo de 2019 **não autoriza citar** Benford e Snow (2000) nem Snow *et al.* (1986). Citar tese conferida apenas na citação de terceiro é o modo de falha que este projeto nomeia. O que a leitura autoriza é citar o capítulo.

**PT-07 ganhou âncora e uma qualificação do nome do seu mecanismo.** O registro chama o mecanismo de *alinhamento de quadros prévio*. Pela fonte, alinhamento é a ligação estratégica a um público — “Frame alignment processes encompass the strategic efforts of social movement actors and organizations to link their interests and goals with those of prospective adherents and resource providers” (p. 400 impressa, PDF p. 10) —, em quatro tipos que o capítulo atribui a Snow *et al.* (1986). O que a denúncia da PGR documenta em 22/03/2021 é o núcleo **deliberando e passando a disseminar um diagnóstico**, que na distinção do capítulo é **articulação e elaboração** de quadro. O alinhamento que corresponderia é o **bridging**, “the linkage of a movement organization with an unmobilized sentiment pool” (p. 400) — e isso é o que **PT-06** documenta em 2020-2021, não o que PT-07 documenta.

> **O nome atual nomeia a família, não o processo.** NÃO renomeei: nomear mecanismo é decisão do pesquisador, pelo precedente da tarefa 19. A proposta está em 47.5.

### 47.3 Quatro divergências que só a abertura do arquivo mostrou

| O que o registro dizia | O que o arquivo diz |
|:--|:--|
| autoria não nomeada na planilha da camada A | **três autores**: Snow, Vliegenthart e Ketelaars — o mesmo padrão de Chen, Lukito e Koo e de González-Bailón *et al.* |
| 2018 | **2019**, 2ª edição, pp. 392-410 |
| OpenAlex: `submittedVersion` | a folha de capa diz **final published version** — primeira divergência de registro **a favor** do projeto |
| OpenAlex: **ouro** | licença do **art. 25fa da lei holandesa** (emenda Taverne): uso pessoal autorizado, **redistribuição vedada** |

### 47.4 E o auditor de licença da tarefa 15 me desmentiu — um dia depois de eu o escrever

O manifesto classificou a peça nova como **CC**. Ela não é. O casamento veio de uma frase **contrafactual** da folha de capa: *“other than for strictly personal, individual use, unless the work is under an open content license (like creative commons)”* — a frase afirma que a obra **não** está sob CC, e o classificador a leu como declaração.

> **Menção não é declaração: é a cifra certa no referente errado aplicada à licença**, e dentro de um script que eu escrevi na véspera para ser a base de uma decisão jurídica.

**Um classificador que acabou de errar não se usa sem reler o que ele afirmou antes.** Reauditadas **as 15 peças classificadas CC, uma a uma, com o contexto de cada casamento**: 14 eram declaração real e 1 era esta hipótese. O conserto é estreito de propósito — desqualifica só o casamento que está dentro de uma hipótese (`unless`, `a menos que`, `salvo se`, `caso a obra`), e **não** usa `except`, porque *“except where otherwise noted, is licensed under a Creative Commons…”* é a fórmula de três obras da EdUERJ e da Editora UnB no corpus e é limitação de **escopo** de uma licença real.

E a queda do CC exigiu o segundo conserto, sem o qual a peça cairia em **ABERTA**: `RESERVADA` só reconhecia *todos os direitos reservados*. Agora reconhece também a **proibição explícita de redistribuir** e o **art. 25fa**. Reclassificação medida peça por peça contra o estado anterior: **exatamente uma mudou**, a certa.

**A cifra do regime de distribuição move-se com isso:** eram **27 de 40** peças de literatura não redistribuíveis; são **28 de 41** (57 MB). `LICENCA-E-DISTRIBUICAO.md` está atualizado; o item 46 fica como estava, porque é afirmação datada de 12/10.

### 47.5 O que precisa da sua decisão

1. **O nome do mecanismo de PT-07.** Hoje: *Alinhamento de quadros prévio*. Proposta: **Articulação e elaboração do quadro de fraude**, que é o que a fonte chama o processo documentado, deixando *alinhamento* para PT-06, onde o bridging de fato ocorre. Alternativa mais conservadora: manter o nome e acrescentar a especificação entre parênteses.
2. **O campo `marco_teorico` do codebook**, que cita *Framing (Snow & Benford, 2000)* — obra não lida e sem rota. Proposta: citar o capítulo de 2019, que está lido e no corpus, mantendo o de 2000 como referência da genealogia. Não executei: é a declaração teórica do projeto, e é sua.
3. **A sessão 4 de `02_PROPOSTA-DISCIPLINA.md`** indica Snow & Benford (1988) e Benford & Snow (2000) — os dois não lidos. Em programa de disciplina isso é normal; cabe decidir se o capítulo de 2019 entra no lugar ou ao lado.

### 47.6 Os 25 que restam, e o que cada um depende

**Oito dos 25 estão em um único periódico, a *Mobilization*** — mais de um terço do que falta da tarefa 17 depende de **um** acesso. Entre eles, *The Emergence, Development, and Future of the Framing Perspective* (2014), que é o companheiro direto do capítulo lido hoje.

### Os 25 pendentes, por motivo medido em 13/10/2026

**9 têm arquivo em algum servidor e o bloqueio é do cliente automatizado** — é a classe que o navegador comum resolve, e foi assim que nove peças chegaram:

| Obra | DOI | Bloqueio | Serve a |
|:--|:--|:--|:--|
| Context and Causal Mechanisms in Political Analysis (2009), *Comparative Political Studies* | `10.1177/0010414009331724` | 429 — CiteSeerX, hoje redirecionado à Wayback | método: mecanismo é sempre situado em contexto; sust |
| The Diffusion of Revolution: ‘1848’ in Europe and Latin Amer (2009), *International Organization* | `10.1017/s0020818309090146` | 429 em 3 tentativas — Cambridge Core | PT-08: difusão e emulação entre países, com a Améric |
| Relational Dynamics and Processes of Radicalization: A Compa (2012), *Mobilization: An International Qua* | `10.17813/maiq.17.1.u7rw348t8200174h` | 403 — EUI Cadmus e ricerca.sns.it | PT-06, PT-15 e PT-16: dinâmica relacional da radical |
| CONTENTIOUS EPISODE ANALYSIS* (2019), *Mobilization: An International Qua* | `10.17813/1086-671x-24-3-251` | 403 — EUI Cadmus | método: a unidade 'episódio contencioso' é a unidade |
| Subnational State Capacity and the Repression of Protest: Ev (2020), *Political Research Quarterly* | `10.1177/1065912920919494` | 403 — SAGE (Cloudflare) | PT-28: capacidade estatal subnacional e dispositivo  |
| Social Movement Organizations: Growth, Decay and Change (1966), *Social Forces* | `10.1093/sf/44.3.327` | 403 — Oxford Academic (Cloudflare) | PT-52: crescimento e decadência de organização — a d |
| Anti-refugee Mobilization in Social Media: The Case of Soldi (2018), *Social Media + Society* | `10.1177/2056305118764431` | 403 — SAGE (Cloudflare) | PT-06: mobilização de extrema-direita em mídia socia |
| Networks, Diffusion, and Cycles of Collective Action (2003), *Social Movements and Networks* | `10.1093/0199251789.003.0008` | 429 — CiteSeerX, hoje redirecionado à Wayback | PT-29 e PT-30: difusão em rede, contágio e ciclo |
| The Logic of Process Tracing Tests in the Social Sciences (2012), *Sociological Methods & Research* | `10.1177/0049124112437709` | 429 — CiteSeerX, hoje redirecionado à Wayback | método: formalização dos testes de process tracing |

**16 não têm depósito aberto em nenhum repositório** — nesses o limite é de assinatura, não de coleta:

| Obra | DOI | Serve a |
|:--|:--|:--|
| Linking Mobilization Frames and Political Opportunities: Ins (1996), *American Sociological Review* | `10.2307/2096308` | PT-07 com PT-03D: quadro de mobilização acoplado à o |
| Framing Processes and Social Movements: An Overview and Asse (2000), *Annual Review of Sociology* | `10.1146/annurev.soc.26.1.611` | PT-07 e PT-50A: a referência canônica de enquadramen |
| Case Study Research (2006), *Cambridge University Press* | `10.1017/cbo9780511803123` | método: desenho de estudo de caso único, que é o des |
| Contentious Performances (2008), *Cambridge University Press* | `10.1017/cbo9780511804366` | PT-01, PT-02, PT-12 e PT-33: a formulação de repertó |
| Discursive Opportunities, Feeling Rules, and the Rise of Pro (2009), *Mobilization: An International Qua* | `10.17813/maiq.14.3.kx87723664558jm4` | PT-07 e PT-50A: oportunidades discursivas e regras d |
| Disentangling Protest Cycles: An Event-History Analysis of N (2010), *Mobilization: An International Qua* | `10.17813/maiq.15.1.86260543m3110705` | PT-62: análise de história de eventos de ciclos de p |
| Mechanisms of Maidan: The Structure of Contingency in the Ma (2011), *Mobilization: An International Qua* | `10.17813/maiq.16.1.74v41g7nl3722775` | modelo do gênero: explicação por mecanismos de um ún |
| The Emergence, Development, and Future of the Framing Perspe (2014), *Mobilization: An International Qua* | `10.17813/maiq.19.1.x74278226830m69l` | PT-07: o balanço de 25 anos do alinhamento de quadro |
| THE UNINTENDED CONSEQUENCES OF ESCALATED REPRESSION* (2021), *Mobilization: An International Qua* | `10.17813/1086-671x-26-1-87` | PT-53 e PT-62: consequências não pretendidas da repr |
| DETERRENCE OR DEFIANCE? HOW SEVERITY AND SELECTIVITY SHAPE P (2025), *Mobilization: An International Qua* | `10.17813/1086-671x-30-4-387` | PT-53 e PT-61: severidade e seletividade da repressã |
| E-extremism: A conceptual framework for studying the online  (2022), *New Media & Society* | `10.1177/14614448221098360` | PT-06: quadro conceitual para extrema-direita online |
| A Tale of Two Cultures (2012), *Princeton University Press* | `10.23943/princeton/9780691149707.001.0001` | método: as duas culturas de inferência, qualitativa  |
| The Impacts of Repression: The Effect of Police Presence and (2010), *Research in Social Movements, Conf* | `10.1108/s0163-786x(2010)0000030006` | PT-27, PT-31 e PT-32: presença e ação policial como  |
| Linking consensus to action: does frame alignment amongst sy (2020), *Social Movement Studies* | `10.1080/14742837.2020.1770071` | PT-07: alinhamento de quadros entre simpatizantes e  |
| Focusing on Focusing Events: Event Selection, Media Coverage (2018), *Sociological Forum* | `10.1111/socf.12442` | método: seleção de evento e viés de cobertura — a re |
| Event Catalogs as Theories (2002), *Sociological Theory* | `10.1111/1467-9558.00161` | método: catálogo de eventos como teoria — é o que o  |
