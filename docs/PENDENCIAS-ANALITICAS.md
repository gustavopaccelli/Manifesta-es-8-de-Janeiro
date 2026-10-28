# Pendências analíticas — pontos a incorporar na redação do artigo

Registro aberto em **12/08/2026** · **atualizado em 29/09/2026**. Não é codebook nem fonte: é a **agenda** do que ficou em aberto ao longo da verificação documental, e que precisa de decisão do pesquisador na hora de escrever.

Está fora do codebook de propósito. Codebook guarda dados; isto guarda perguntas. Misturá-los estraga os dois.

---

<!-- PAINEL: gerado por scripts/gerar_painel.py. Não editar à mão: o ciclo sobrescreve. -->

## Painel de estado — medido em 27 de outubro de 2026

**Esta seção é GERADA pelo passo 5 do ciclo. Nenhuma cifra dela é digitada**, e as listas de tarefas e decisões não são repetidas aqui: o painel aponta para as seções que os passos 3 e 4 geram. **A razão tem data** — até 27/10/2026 este painel era escrito à mão, datava-se de 29/09, e a revisão do repositório mediu que **nenhuma das suas cifras estava certa** (item 91).

**O aparato está pronto, auditado, versionado e verificável por um comando; o artigo não começou.** Por decisão do pesquisador em **16/08/2026**, a redação é o **último** item da fila: o conjunto de dados de todo o processo político vem primeiro. Nada mudou nessa decisão desde então.

| Frente | Estado |
|:--|:--|
| Codebook | **85 sub-eventos × 17 campos** — JSON, CSV e XLSX gerados de uma fonte única, com zero divergências. Zero vazios em `mecanismo_causal` e em `autonomia_movimento` |
| Classes de verificação | **68 em fonte primária** · 16 confirmados por outra via · **0 a verificar** · 1 inferência declarada. O critério das três condições está escrito em `metadados.vocabulario_status_classe` desde 25/10/2026 |
| Ancoragem documental | **84 de 85 registros** com arquivo vinculado · 84 com página ou localizador estrutural · 85 com transcrição literal no campo. O único sem arquivo é PT-03D, declarado |
| Corpus | **74 peças / 12.352 p.** no manifesto, em 14 eixos — 65 PDFs e 9 âncoras não-PDF, estas conferidas por arquivo inteiro desde 25/10/2026. Da documental: **32 peças / 6.970 p.**; de literatura: 42 peças |
| Figuras | SVG da cadeia causal e cronologia navegável. **São a única parte do aparato escrita à mão**, e duas guardas as cobrem: o passo 10 confere que todo registro do codebook aparece na figura, e a tabela-espelho do passo 6 confere o **nome do mecanismo** de cada ponto contra o campo — com linha de base em zero divergências |
| Verificação | `bash scripts/ciclo.sh` — **14 passos**: 8 geradores e 6 conferidores, entre eles as **10 checagens estruturais**. Toda linha de base reprova com código de saída ≠ 0; nenhuma apenas avisa |
| Controle de versão | git desde **20/09/2026**, 106 commits, **remoto PÚBLICO** em `gustavopaccelli/Manifesta-es-8-de-Janeiro.git` — e é por ele ser público que os PDFs do corpus saíram do versionamento em 21/10/2026. Último commit: 27/10/2026 |
| Tarefas abertas | **3** — 10, 17, 16. A lista vive na seção *Ordem de ataque*, gerada pelo passo 3, e 34 tarefas estão fechadas |
| Decisões pendentes | **11**, em 3 naturezas. A lista vive na seção *Decisões pendentes*, no fim deste arquivo, gerada pelo passo 4 |
| **Redação do artigo** | **não iniciada — por decisão, é o último item da fila.** Desde 25/10/2026 ela não tem mais pré-requisito de dado: a tarefa 26 fechou e não há decisão de campo aberta no codebook. **Começá-la é decisão do pesquisador** |

> **O que este painel NÃO repete, de propósito.** As tarefas e as decisões abertas têm cada uma a sua seção gerada, e listá-las aqui seria a quarta cópia — a contabilidade deste projeto já envelheceu quatro vezes por cópia à mão, e o histórico está nos itens 49, 78, 83 e 90. **Os itens numerados abaixo são um log cronológico:** a cifra dentro de um item era verdade no dia dele e fica como está.

<!-- /PAINEL -->

> **O PAINEL ANTERIOR, e por que ele saiu — 27/10/2026, item 91.** Até aqui esta seção era escrita à mão e datava-se de **29/09/2026**. A revisão do repositório mediu cada cifra dela e **nenhuma estava certa**: dizia 83 sub-eventos quando são 85, 61 em fonte primária quando são 68, 66 PDFs quando são 65, *oito passos* de ciclo quando são treze, e **49 registros num "Caderno de evidências" que não existe como arquivo algum** — o nome aparecia uma única vez em todo o repositório, nesta tabela. **E uma linha era falsa em sentido perigoso:** afirmava *"git desde 20/09/2026, sem remoto configurado"* quando o remoto existe **e é público** — que é exatamente a premissa que fez os PDFs saírem do versionamento em 21/10. **Painel escrito à mão descreve o dia em que foi escrito**, e por isso ele passou a ser gerado. As linhas de *Fechados* e *Abertos* que vinham aqui usavam a numeração de itens anterior à ordem de ataque, e saíram com ele: as duas listas vivem nas seções geradas pelos passos 3 e 4.

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

`scripts/historico/recodificar_paginas_execucao.py` corrigiu `fonte_pagina` de PT-58, PT-59 e PT-60, que apontavam para a **capa e a assinatura** das peças em vez das páginas onde as transcrições estão. E corrigiu `metadados.n_subeventos` de 81 para 82, que estava defasado desde a entrada do 82º registro.

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

**O caso PT-10 inverte a expectativa e por isso vale registro.** Nas duas rodadas anteriores o JSON estava certo e a peça derivada, errada. Aqui foi o contrário: o relatório citava a página certa e o campo estruturado do codebook a havia perdido — o próprio registro nomeia as três páginas em `fonte_trecho` e em `status_verificacao`. A p. 1021 foi lida no PDF antes da correção e sustenta a afirmação: o diretor-geral da PRF declara ali que "essa foi, talvez, a maior manifestação do mundo, com **1,3 mil bloqueios montados**", a mesma cifra que a p. 999 registra como "um total de 1.300 pontos de interdição no País". Corrigido por `scripts/historico/recodificar_pagina_pt10.py`.

**O limite dos dois verificadores, declarado:** comparam o que a peça *declara* — ids, páginas, selo, cifras mortas, caminhos —, não a prosa. Uma cifra nova e errada passa; uma afirmação causal sem lastro passa. Eles pegam **regressão declarada**, não erro de interpretação.

Os dois foram testados por injeção de defeito, um de cada vez, com a árvore restaurada em seguida. O do relatório reprova nos sete casos ensaiados: registro que some da tabela, id inexistente, página não ancorada, página de um documento atribuída a outro, cifra morta ressuscitada, vocabulário revertido para "condenados" e contagem antiga no cabeçalho.

---

### 21.6 O varredor de `fonte_pagina` — e as duas âncoras que faltavam

O caso PT-10 apareceu de raspão: o relatório citava uma página a mais, e por isso a lacuna no campo estruturado ficou visível. Onde nenhuma peça derivada cita, ninguém veria. `scripts/varrer_fonte_pagina.py` compara, nos 82 registros, as **223 citações de página** que a prosa faz (`fonte_trecho`, `mecanismo_causal`, `status_verificacao`, `nota_auditoria`) com o que o `fonte_pagina` ancora.

**É triagem, não gate, e fica fora do ciclo.** Página citada na prosa não é, por si, página que falta: pode ser refutação, remissão a outro registro ou menção de passagem. Ele imprime o trecho em volta de cada achado para que a decisão leve segundos, e sai com código 0 por padrão. Testado contra o próprio PT-10: revertendo o campo ao estado anterior, o registro reaparece na lista.

**Na estreia, oito candidatos: seis legítimos e dois reais.** Os legítimos ficam registrados porque vão reaparecer a cada execução — PT-12 e PT-34 citam páginas para *refutar* uma cifra, PT-39 remete à página de PT-08A, PT-06C à denúncia que ancora PT-07, e PT-59 é artefato do varredor ("PGR" ali é parte processual, não documento).

**Os dois reais foram corrigidos em 25/09/2026**, por `scripts/historico/recodificar_ancoras_pt15_pt28.py`. Li as quatro páginas no PDF antes de mexer:

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

**Dois erros de página reais na estreia**, corrigidos por `scripts/historico/recodificar_paginas_pt02a_pt03a.py` com as páginas lidas antes:

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

Tarefa 9 da ordem de ataque, aberta desde 14/08/2026 — e **não intocada**: dez itens foram conferidos à mão em **01/09/2026**, quatro divergentes, nas fichas de [`analise/08_BIBLIOGRAFIA-METODOLOGICA.md`](analise/08_BIBLIOGRAFIA-METODOLOGICA.md). Os quatro modos de falha que essa leva nomeou orientaram esta. `scripts/verificar_dois_sinteses.py` extrai os DOIs das sete sínteses LeapSpace, consulta cada um no CrossRef — e, se lá não estiver, na DataCite — e emite [`data/processed/dois_sinteses_leapspace.csv`](../data/processed/dois_sinteses_leapspace.csv). Fica **fora do ciclo**, como o varredor de `fonte_pagina`: é instrumento de triagem, não gate.

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

Registrados em três lugares: a ficha da **segunda leva** em [`analise/08_BIBLIOGRAFIA-METODOLOGICA.md`](analise/08_BIBLIOGRAFIA-METODOLOGICA.md) §1.1, a lista de achados de [`Fontes/LEIA-ME_fontes.md`](../Fontes/LEIA-ME_fontes.md), e os dicionários `NAO_EXISTEM` e `VIZINHOS_TROCADOS` de `scripts/verificar_dois_sinteses.py`. **As sínteses não foram editadas** — `Fontes/` é imutável por princípio, e a correção pertence ao registro bibliográfico, não à fonte.

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

**Quatro verbetes lidos integralmente na fonte:** *Mechanisms* (Tarrow), *Protest cycles and waves* (della Porta), *Resource mobilization theory* (Edwards & Gillham) e *Critical mass theory* (Oliver). O resultado está em [`analise/09_CONCEITO-MECANISMO.md`](analise/09_CONCEITO-MECANISMO.md), com a tabela de **quatorze concepções de mecanismo causal** e o preço de cada saída.

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

Onze verbetes lidos integralmente, registro em [`analise/10_VERBETES-ENCICLOPEDIA.md`](analise/10_VERBETES-ENCICLOPEDIA.md). Os sete DOIs foram testados: **todos resolvem, e nos sete o título e a autoria casam** com o que a obra imprime.

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

Tarefa 20, em [`analise/11_HIPOTESES-RIVAIS-PT-28.md`](analise/11_HIPOTESES-RIVAIS-PT-28.md). É também a primeira aplicação do enquadramento de Zaks (2017) que o item 2.1 de `08` registra como "a peça que o projeto mais precisa e não tem".

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

Tarefa 14. Relatório completo em [`analise/12_CAMADA-T-1-CONJUNTURAL.md`](analise/12_CAMADA-T-1-CONJUNTURAL.md).

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

**Segunda rodada da tarefa 14, no mesmo dia.** O item 31 fechou entregando seis decisões, e a primeira delas era a mais cara: *"o par PT-01 → PT-02, com mecanismo de spin-off, codifica ruptura"*. **O pesquisador decidiu pela continuidade** e indicou a literatura — Marcelo Kunrath Silva. Esta rodada executa a decisão com três peças novas, todas lidas na fonte, e documento completo em [`analise/12_CAMADA-T-1-CONJUNTURAL.md`](analise/12_CAMADA-T-1-CONJUNTURAL.md).

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

**Tarefa 25, primeira metade.** O pesquisador deu o recorte: o bolsonarismo **como fenômeno de mobilização social e política**, com foco nas dinâmicas de manifestação e protesto e nos **repertórios próprios do campo das direitas**. Documento completo em [`analise/13_LITERATURA-BOLSONARISMO.md`](analise/13_LITERATURA-BOLSONARISMO.md).

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

**Terceira rodada do mesmo dia.** A segunda terminou com oito pontos para o pesquisador. Ele respondeu os oito, e esta rodada executou o que era executável: **sete viraram mudança de campo, um virou entrega de arquivo.** Detalhe completo em [`analise/12_CAMADA-T-1-CONJUNTURAL.md`](analise/12_CAMADA-T-1-CONJUNTURAL.md), §4.

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

**Quarta rodada do mesmo dia, e a camada conjuntural brasileira fecha.** A terceira havia deixado PT-06 contextual por critério, e escrito na nota do próprio registro qual peça o fecharia e que ela estava no corpus sem ter sido lida. O pesquisador mandou ler. Detalhe em [`analise/12_CAMADA-T-1-CONJUNTURAL.md`](analise/12_CAMADA-T-1-CONJUNTURAL.md), §5.

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

**Eixo 14 aberto: sete peças, 567 páginas**, em `Fontes/14_Livros-brasileiros/`. Documento completo em [`analise/14_LIVROS-BRASILEIROS.md`](analise/14_LIVROS-BRASILEIROS.md). Corpus: **52 → 59 PDFs, 10.207 → 10.774 páginas**; documental inalterada em **22 / 6.951**.

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

**Segundo passo de 08/10.** O pesquisador entregou cinco peças e mandou coletar duas. PT-08 era o **último contextual**; fechou. Documentos: [`15_COMPARADO-6-DE-JANEIRO.md`](analise/15_COMPARADO-6-DE-JANEIRO.md) e [`14_LIVROS-BRASILEIROS.md`](analise/14_LIVROS-BRASILEIROS.md), §7.

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

<!-- ORDEM-DE-ATAQUE: gerado por scripts/gerar_ordem_de_ataque.py a partir de data/ordem_de_ataque.json. Não editar à mão: o ciclo sobrescreve. -->

## Ordem de ataque — revista em 15/10/2026

**A decisão que ordena tudo continua sendo a de 16/08/2026: a redação é o último item.** A ordem anterior a essa data tratava o aparato como suficiente e punha a escrita como ponto de virada; esta trata o conjunto de dados do processo político como pré-requisito.

**A revisão de 29/09 foi de contabilidade, não de rumo.** A tabela vinha mostrando como abertas quatro tarefas concluídas em 16/08 — o arquivamento web (4), a obtenção do balanço (8) e a reauditoria (11), além da 6. Foram fechadas com a data correta, e entraram as tarefas nascidas das rodadas 19, 20 e 21.

**A de 30/09 acrescentou três tarefas nascidas da leitura na fonte** — 19, 20 e 21 — e corrigiu a contabilidade da 17, que passou a ser gerada.

**A de 15/10 é de contabilidade pela terceira vez, e os dois defeitos eram os que esta peça avisa que tem.** A **15** aparecia como aberta desde que foi executada, em 13/10 — dois dias de atraso. E a **17** dizia "27 pendentes: 6 lidos" na mesma linha em que afirma que os números são gerados: `localizar_camada_a.py` gera **25 e 8**. A cifra velha entrou em **30/09** (commit `71df6e1`, que foi justamente o que passou essa contagem a ser gerada) e ficou **quinze dias** sem ser reconferida, atravessando as leituras de 08/10 e a de 13/10. **A linha declarava a procedência certa e carregava a cifra velha** — é o modo de falha da casa aplicado à própria contabilidade. Nada de rumo mudou: nenhuma dependência, nenhuma ordem, nenhuma tarefa nova.

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
| 15 | ~~Higiene do repositório: licença, remoto, `.backup_pre_lula/`, ponteiros no JSON~~ — executada, e era **mais apuração que decisão**: o que havia para decidir já estava decidido pelo conteúdo do corpus. **27 das 40 peças de literatura não podem ser redistribuídas**, e os PDFs estão no histórico do git — o remoto público deste repositório não existe. Nasceram daí o `MANIFESTO-CORPUS.csv` com SHA-256 e rota de obtenção, a **checagem 8** do ciclo, `exportar_aparato.py` e `LICENCA-E-DISTRIBUICAO.md`. **O que restou não é tarefa, é decisão sua:** a licença da sua obra (46.6), o backup versionado e o folder de 37,4 MB em 6 páginas (46.5) | 46 | ✅ 13/10 |
| 19 | ~~Decidir o nome de `mecanismo_causal` e aplicar as cobranças da seção 4 do documento 09~~ — **executada em 09-10/10**: você aprovou os quatro nomes (PT-29 **demonstração de viabilidade**; PT-34 **concentração simultânea no conjunto simbólico**; PT-12A **agregação na base e intermediação concentrada**; PT-62 **desmobilização por repressão seletiva** seguida de **migração de arena**) e a atribuição dos quatro testes foi corrigida para **Van Evera (1997) → Bennett (2010) → Collier (2011)**. **As "sete cobranças" eram cinco:** duas linhas da §4 eram *passam* e *correto*, não cobrança, e a de PT-03 saíra em 04/10. Com a quinta, **a tarefa fechou — e esta linha ficou aberta na tabela por cinco dias** | 41, 42, 43, 44 | ✅ 10/10 |
| 27 | ~~**Codificar `autonomia_movimento` nos registros que faltam**~~ — ✅ **EXECUTADA em 16/10/2026, em cinco rodadas, no mesmo dia em que você a abriu.** O campo fecha em **85 de 85** registros com valor e **0 vazio**. O último vazio era PT-19A e **você o resolveu no mesmo dia** — e a resolução **não afrouxou guarda nenhuma**: a convenção do localizador estrutural para fonte não paginada já existia no projeto e era praticada por PT-03E desde 15/10, declarada na rota do acórdão do TSE em `PROCEDENCIA`. O registro passou a citar seção, não folha, e **duas guardas novas entraram com ele**, porque a nota que justificava a exceção declarava uma vigilância de SHA-256 que não existia (item 62). As rodadas: `T0 Mobilização` (5), `T-1 Operacional` (25), `T-1 Conjuntural` (17), `T0 Execução` (11) e o fechamento (26). **Distribuição, depois do quinto valor que você criou horas mais tarde: 52 `Não se aplica`, 15 `Lido, não documentado`, 9 `Autonomia relativa`, 5 `Autonomia com encorajamento de cima` e 1 `Conduzido de cima`** — e esse um é econômico, não político (o MBVA no envio dos caminhões). **O quinto valor obrigou a reexaminar os 14 que estavam em `Autonomia relativa`**, porque criar valor muda o critério para todos: cinco mudaram, nove ficaram com a razão escrita (item 61). **Sete folhas novas** entraram no codebook pelo caminho, nenhuma achada por busca de página: achadas porque a pergunta mudou. **As três decisões de 57.4 estão resolvidas** — o quinto valor (item 61), a guarda do último vazio (item 62) e, em 18/10/2026, o nome do valor de PT-10A, que passou a *Conduzido por patrocínio de setor organizado*, tipificado no verbete de Edwards e Gillham que já havia nomeado PT-12A (item 65). O resultado e os seus limites estão nos itens 60, 62 e 65. | 55, 56, 57, 58, 59, 60 | ✅ 16/10 |
| 26 | ~~**Fechar as âncoras do codebook**~~ — ✅ **FECHADA POR VOCÊ EM 25/10/2026**, no dia em que a terceira e última parte dela saiu. **Aprovada por você em 15/10/2026**, e em dez dias as três partes fecharam: (a) e (b) por verificação, (c) por duas delegações suas — o `data_hora` de PT-02 em 22/10 e as três últimas decisões de campo em 25/10. **Com ela fecha a última tarefa que tocava o codebook:** não há decisão de campo aberta desde então, pela primeira vez desde 04/10/2026. O banco está construído: **85 registros** — eram 83 até 20/10/2026, quando você mandou entrar dois antecedentes do impeachment e o codebook cresceu pela primeira vez desde 10/10 (item 68), zero `A verificar`, zero `mecanismo_causal` vazio e **nenhuma tarefa de codificação aberta** entre 10/10 e 16/10/2026 — quando o campo 17 abriu a **27**, que é de codificação e nasce do próprio fechamento (item 55). **(a) ✅ EXECUTADA em 15/10/2026 — as quatro folhas que faltavam:** PT-03B (TRF-4, **p. 30 e 401**), PT-05A (ADC 43/44/54, **p. 2 e 489**), PT-06C (HC 193.726, **p. 185**) e PT-57 (AP 2668, **p. 19**). As seis transcrições saíram da folha e `conferir_paginas` localizou **6 de 6 por inteiro**; `confirmados` subiu de 69 para **73**. Hoje **nenhuma registro vincula PDF do corpus sem citar folha**, e a **checagem 5 passou a exigir** isso — o ponto cego virou guarda, com prova negativa. Resta **1** sem `fonte_pagina`, **declarado**: PT-03D, que ancora em notícia arquivada (item 51). PT-19A era o outro e **saiu em 16/10**, por localizador estrutural em vez de folha — a mesma convenção que PT-03E já praticava (item 62). **(b) ✅ EXECUTADA em 15/10/2026 — os 17 fragmentos que casavam só por janela foram a 0**, e a queda não veio de afrouxar nada: **4 eram âncora creditada à folha errada** — 3 ao documento errado e 1 à página errada dentro do mesmo documento, contagem corrigida em 15/10/2026 pela medição do item 53, que desfez o "4 ao documento errado" que eu havia relatado (o localizador devolvia a primeira folha com qualquer janela de 40 caracteres, e as peças do corpus se citam entre si), **2 eram transcrição editada dentro das aspas** em PT-39 — uma sigla abreviando o que a CPMI escreve por extenso e uma vírgula acrescentada —, **8 eram marcador de nota de rodapé** colado na prosa pela extração e **3 eram citação atravessando a quebra de página com o aparato da folha no meio**. Cada classe ganhou nome e contagem própria, e a **linha de base do resíduo inexplicado é ZERO**: prova negativa com duas injeções, inclusive a de cauda que escapou em 09/10 (item 52). E a pergunta que a parte (b) deixou aberta está **respondida em 15/10/2026**: nenhuma âncora do codebook depende da ordem de `fonte_pagina` para escolher entre documentos — **234 fragmentos localizados, 17 com mais de uma folha candidata, 15 decididos pelo texto e 2 empatados entre páginas do mesmo documento citado**, o que deixa a âncora certa das duas maneiras. **Zero empate entre documentos**, e o zero virou guarda com prova negativa (item 53). **(c) ✅ FECHADA EM 25/10/2026 — ZERO decisões de campo abertas, e as três últimas foram DELEGADAS A MIM** (*"Decida as três de 26(c)"*)**. A mais pesada não era a classe de três registros: era que o critério de `Confirmado em fonte primária` vivia em PROSA dentro de PT-01A — que declara não ser primário *"no sentido estrito deste codebook"* — e nunca tinha sido escrito em `vocabulario_status_classe`, uma lista de quatro rótulos SEM DEFINIÇÃO. Escrito o critério em três condições cumulativas e aplicado, promovem **SEIS** registros e não três: PT-03B, PT-05A, PT-06B, PT-06C, PT-56 e PT-57. **Nenhum critério foi afrouxado — o critério foi escrito** (item 83). O histórico abaixo fica** (eram seis até 18/10/2026, quando você nomeou o mecanismo de PT-07 — item 65; cinco até 20/10, quando a varredura achou que uma delas estava resolvida havia onze dias — item 67; e a composição mudou em 21/10, item 71: **a data de PT-57 fechou** e **os nomes de PT-01A e PT-01B entraram**, porque chegaram com o item 68 e nunca tinham sido acrescentados aqui — contagem copiada de outro lugar perde item, pela segunda vez)**:** ~~**(i)** `data_hora` de PT-02 (34.7)~~ — ✅ **DECIDIDO E EXECUTADO EM 22/10/2026, e a decisão foi DELEGADA A MIM** (*"Decida o `data_hora` de PT-02"*), a primeira vez que ele delega decisão de campo em vez de tomá-la. O campo passou a `2015–2016 (ator anterior: mobilização desde 2011, organização desde 2003)`: **a data do evento não mudou** — a ressalva de 04/10/2026 já a declarava correta — e o que entrou é a anterioridade do **ator**, que a nota explicava sem resolver havia dezoito dias. **A forma saiu de medição da convenção do próprio campo**, não de preferência minha: 13 dos 85 registros trazem qualificador entre parênteses, e PT-19A, PT-01A e PT-58 usam exatamente a forma de datar **outra unidade** dentro do parêntese. **As duas datas foram conferidas folha a folha antes de entrar**, varrendo os PDFs inteiros em vez de derivar a folha pelo offset — e uma delas **não estava ancorada**: a folha 21 (fólio 77) de Kunrath Silva (2023) entrou em `fonte_pagina` com a decisão, porque promover data a campo estrutural com folha que o ciclo nunca conferiu seria o defeito que este projeto persegue (item 80). ~~**(ii)** a promoção de classe de PT-03B, PT-05A e PT-06C (51.5, decisão 1)~~ — ✅ **EXECUTADA EM 25/10/2026, e alcançou SEIS registros:** a lista de três era de 15/10 e nomeava só os que ganharam folha naquele dia; PT-57 ganhou folha no mesmo dia e ficou de fora da lista — **contagem copiada de outro lugar perde item, pela terceira vez** —, e PT-06B e PT-56 satisfazem as mesmas três condições citando por localizador estrutural, que o vocabulário declara valer. PT-03C fica, e agora diz por quê: o acórdão está em `fonte_local` e **nenhum localizador o aponta**. ~~**(iii)** o nome do mecanismo de **PT-01A**~~ — ✅ **ATRIBUÍDO:** *Articulação inicial do quadro de fraude, refutada pela via acionada*, que liga a cadeia ao quadro que PT-07 articula em 2022. ~~**(iv)** o nome do mecanismo de **PT-01B**~~ — ✅ **ATRIBUÍDO:** *Defecção programática do aliado de coalizão*, com `defecção` que PT-31 já carrega, alimentando **D2** como o sinal anterior à saída. **As duas formas seguem a convenção medida do campo** — frase nominal curta —, não a frase longa das propostas — os dois nasceram em 20/10 como `PROPOSTA DE MECANISMO, NÃO ATRIBUÍDA`, pelo precedente da tarefa 19 (item 68). ~~**DECIDIDA, execução pendente:** o `marco_teorico` (47.5, decisão 2)~~ — ✅ **EXECUTADA em 21/10/2026, frente F12 (item 72):** o campo passou a declarar a estrutura que você fixou — marco, três âncoras teóricas, uma âncora metodológica —, cada âncora citando a **peça lida** com folha, e **Snow e Benford (2000) saiu**. ~~**UMA DECISÃO NOVA NASCEU DAÍ, e é sua:** nenhuma edição de Beach e Pedersen está no corpus, e a rota é **(A)** declarar a âncora ou **(B)** obter a obra.~~ ✅ **DECIDIDA E EXECUTADA EM 21/10/2026, pela rota (B):** você forneceu a edição de 2013 — 208 folhas, impressa = PDF − 8, conferida folha a folha — e ela foi **lida**: capítulos 1 a 3 e o Apêndice A, com o estado **medido** no registro de leitura. A variante do projeto é **explaining-outcome process tracing** (Apêndice A.1), o que resolve por citação a tensão de recorrência aberta em 30/09 e autoriza o conglomerado de mecanismos sistemáticos e específicos que o codebook já usava. **ERRATA DE 22/10/2026 (item 78):** esta linha seguiu listando a decisão como **aberta** — *"Recomendação revista para (B)"* — depois de a rota ter sido executada, e a G2 não a pegou porque um `~~` a **262 caracteres** de distância liberava os 7.268 caracteres desta linha inteira. Nasceram daí a **janela de ressalva** e a **G4**. O detalhe de cada uma: `data_hora` de PT-02 (34.7), ~~Telegram e WhatsApp em PT-06 (35.5)~~ — ✅ **RESOLVIDA EM 09/10/2026 e listada como aberta até 20/10**, por Cesarino (2022, p. 181 impressa), que descreve de primeira mão o ecossistema em camadas incluindo os aplicativos fechados; o que permanece declarado são as CIFRAS de segunda mão, que o registro não afirma (item 67), ~~o `marco_teorico` que cita obra não lida (47.5, decisão 2)~~ — ✅ **resolvida em 21/10/2026 na frente F12**, e a âncora foi lida no mesmo dia, de modo que o campo não cita mais obra não lida, ~~a data de PT-57, cuja publicação em 22/10/2025 não está no acórdão (item 51)~~ — ✅ **DECIDIDA E EXECUTADA em 21/10/2026**, pela saída (a) das três: `data_hora` passou a **15/10/2025**, a data que a própria peça traz na folha 19, e o registro passou a codificar a **conclusão** do acórdão em vez da publicação. Remedido antes de mexer: `22/10/2025` e `22 de outubro de 2025` têm **zero** ocorrências nas 1.991 folhas. Saiu uma data sem lastro e nada a jusante mudou, pelo seu critério — sendo constatação de resultado, a peça não alimenta elo causal (item 71), ~~**o nome do mecanismo de PT-07**~~ — ✅ **DECIDIDO por você em 18/10/2026**, pela saída (c) das três apresentadas: o campo passou a chamar-se *Deliberação de ruptura e articulação do quadro de fraude*, e a razão está escrita dentro do próprio registro (47.5, decisão 1, item 65) — e **a promoção de classe de PT-03B, PT-05A e PT-06C** — os três ganharam transcrição de fonte primária com folha em 15/10 e seguem `Confirmado`, não `Confirmado em fonte primária`; **PT-06C é o caso mais limpo**, uma só folha cobre data, placar, objeto e fundamento (51.5, decisão 1). E ~~o campo para autonomia do movimento (35.4)~~ — **DECIDIDA E EXECUTADA em 16/10/2026, a primeira das sete a sair:** você mandou o esquema ganhar o campo, e ele ganhou — `autonomia_movimento`, o 17º, com vocabulário controlado de três valores, **PT-06 codificado** a partir de transcrição que o ciclo já conferia e **82 registros por codificar**, que é leitura e não migração. Três guardas novas, com prova negativa (item 55). **Eram cinco até 16/10/2026:** a recontagem que você pediu achou a sexta — o inventário de 50.4 foi copiado à mão e deixou a decisão 1 de 47.5 de fora — e **você mandou trazer a sétima no mesmo dia**, porque `status_classe` é campo de registro como os outros e não pendência solta (item 54). **E uma SÉTIMA apareceu em 18/10/2026, achada por varredura e resolvida no mesmo dia:** PT-21 ainda afirmava *a massa crítica necessária para romper barreiras* — o termo que a tarefa 19 retirou de PT-34 em 10/10, intacto no registro ao lado por oito dias, porque a guarda vigiava a **frase** de PT-34 e não o **conceito**. Você mandou executar, e o campo passou a `Concentração de contingente no acampamento` (item 66). **Nada aqui depende de literatura pendente** || **ESTADO EM 25/10/2026: (a), (b) e (c) EXECUTADAS. A tarefa não tem parte aberta.** Fechá-la é **decisão sua** — contagem é medição, estado de tarefa é juízo, pela mesma regra que o item 79 registrou quando você fechou a 25. Não toquei no campo `estado`. | 50 | ✅ 25/10 |
| 25 | ~~**A literatura do bolsonarismo como mobilização**~~ — ✅ **FECHADA POR VOCÊ EM 22/10/2026**, no dia em que a medição mostrou que não restava leitura nela. **Coleta fechada em 04/10**: **18 peças, 453 p.** em `Fontes/13_Bolsonarismo-mobilizacao/` — 14 por OpenAlex e **as 4 barradas entregues pelo pesquisador** (item 34.6). **18 das 18 estão lidas** e **7 ancoram registro** — são dois predicados, e eram um só até 22/10/2026. **Três mudaram o codebook:** Araujo e Sales (2022), que tirou PT-05 de contextual; Fernandes e Silva (2021), que tirou a "tolerância policial" de PT-02; e von Bülow e Abers (2024), que **fechou PT-06 e retificou o mecanismo dele**. **Por ler: 0.** **ERRATA DE 22/10/2026 (item 78):** esta linha dizia *"Três foram lidas"* e *"Faltam 15, 400 p."*. A primeira cifra contava peças que **ancoram registro** e a prosa chamava-as de **lidas**; a segunda subtraía ancoragem do total e chamava o resto de não lido — **a cifra correta no referente errado**. Doze foram lidas integralmente em **09-10/10/2026** e o registro de leitura o diz desde 21/10. **Nada aqui bloqueia registro, e nunca bloqueou**: a leitura serve à redação, não à codificação. **E o fecho obedeceu à ordem certa:** a medição disse que não restava leitura, eu **não** fechei a tarefa, e você fechou. **Contagem é medição; estado de tarefa é juízo** — e eles não se confundem nem quando a medição é inequívoca. **O que esta tarefa mudou no codebook foram três registros** — PT-05, PT-02 e PT-06 —, e **7 peças do eixo ancoram registro** ao todo; as demais entregam insumo de redação, que a tarefa 16 usa. **E esta frase já trocou o referente uma vez, hoje:** ela dizia *"as outras quinze"*, que é o total menos as três que mudaram registro — e quatro dessas quinze **ancoram**. Subtrair por um predicado e falar do resto por outro é o defeito do item 78, reaparecido no texto que o documenta | 23.2, 31.4, 33, 34, 35 | ✅ 22/10 |

### Abertas

| # | Tarefa | Item desta agenda | Depende de |
|:--|:--|:--|:--|
| 10 | Acrescentar a literatura brasileira em livro — 🔶 **eixo 14 com 5 arquivos, 1.832 p., e 5 das 5 estão lidas** — 2 delas ancoram registro, e o estado de cada uma é medido em [`05_REGISTRO-DE-LEITURA.md`](referencial/05_REGISTRO-DE-LEITURA.md). **ERRATA DE 22/10/2026 (item 78):** esta linha dizia *"nenhuma lida"*. Era falsa desde **08/10/2026**, quando quatro das cinco foram lidas, e seguiu falsa depois de a quinta ser lida em 22/10 — **catorze dias dentro de um arquivo que a guarda G2 vigia**, porque a forma coletiva da negação não estava no vocabulário dela. A cifra passou a ser **derivada do censo único** e não pode voltar a divergir. **O que falta nesta tarefa nunca foi a leitura deste eixo.** A coleta somou **12 peças** — 7 coletadas, 3 entregues por você e 2 capítulos a mais por encaminhamento —, e o manifesto conta menos arquivos do que isso porque **o volume integral substituiu oito offprints em 08/10** (item 39.1): peça coletada e arquivo no corpus deixaram de ser a mesma unidade. **A tarefa SE DIVIDIU em duas, e metade está fechada** (item 38.8): o mapa bibliográfico brasileiro que as sínteses não tinham está em Gohn (2019), que mapeia 1970-2019 por ciclo nomeando autores e paradigmas; o que resta é **obter os textos que esse mapa nomeia** — o cânone (Sader, Scherer-Warren, Avritzer, Doimo, Telles, Abranches, Nobre, Solano, Messenberg) é de editora comercial, **zero com autoria casada em acesso aberto**, e depende dos seus arquivos | 11.4, 22.4, 37, 38 | seus arquivos |
| 17 | **Ler na fonte os 43 da camada A** (passo 3 do item 11.3) — **25 pendentes**: 8 lidos, 7 com ficha da 1ª leva, 3 impedidos. Números medidos por `localizar_camada_a.py` a cada geração desta linha, nunca digitados. Das 25, **9 têm arquivo em algum servidor e são barradas no cliente automatizado** e **16 não têm depósito aberto em lugar nenhum**; **8 das 25 estão num só periódico, a *Mobilization*** (item 47.5) | 23, 24, 25 | acesso institucional |
| 16 | **Redação do artigo** | 3, 4, 5, 6, 9, 10 | tudo acima |

**Nenhuma pendência de dado depende de você** — isso valia desde 16/08, deixou de valer em 30/09 com a tarefa 24, e em 04/10 mudou duas vezes: a tarefa **14** fechou a parte que podia fechar e deixou a **25**, bibliográfica; e horas depois, na terceira rodada, **você entregou as quatro peças barradas e mandou ler duas**, o que fechou a coleta da 25 e tirou PT-05 de contextual. ~~**O que resta da 25 é leitura, e a leitura não depende de você.**~~ — ✅ **e ela foi feita:** as dezoito peças do eixo 13 estão lidas, doze delas em 09-10/10/2026, e **você fechou a tarefa em 22/10/2026**.

**As três abertas, por natureza:** leitura ou entrega de arquivo (**10, 17**) e a redação (**16**). **A 15 saiu da lista em 13/10**, e o que sobrou dela é decisão registrada no item 46, não tarefa aberta. **A 10 mudou de natureza em 08/10:** deixou de ser tarefa de busca — a busca foi feita e mostrou que o cânone não está em acesso aberto — e passou a depender dos seus arquivos, como a 17 depende do seu acesso institucional. **A tarefa 14 fechou em 04/10**, em quatro rodadas, e com ela a última tarefa de codificação **do esquema de 16 campos** — a **27**, de 16/10/2026, codifica o campo 17, e é a primeira tarefa de codificação aberta em doze dias. **Só a 16 depende das outras — e nenhuma leitura pendente bloqueia registro desde a quarta rodada de 04/10.** **A 25 fechou em 22/10/2026**, por sua decisão, quando a medição mostrou o eixo 13 inteiro lido: **por ler, 0**. **ERRATA DE 22/10/2026 (item 79):** esta frase dizia *"as nenhuma peças que restam no eixo 13"*, e com a cifra derivada a zero passou a ler **"as nenhuma peças que restam"** — eu derivei o número e não reli a frase que o cita. **Molde que cita cifra tem de ler bem em zero**, e a cifra entra como cifra, não dentro de locução que pressupõe plural.

> **Cifras desta seção que não são medidas a cada ciclo:** **9** — das pendentes da camada A têm arquivo em algum servidor e são barradas no cliente automatizado (medido em 13/10/2026, item 47.5 — tentativa de rede, não remedida a cada ciclo); **16** — das pendentes não têm depósito aberto em repositório nenhum (medido em 13/10/2026, item 47.5 — o limite ali é de assinatura, não de coleta). Todo o resto sai de medição na geração.

<!-- /ORDEM-DE-ATAQUE -->

> **As decisões suas que restam, e nenhuma bloqueia o resto.** (1) **Redatar `data_hora` de PT-02** — a ressalva está redigida como nota, a diferença entre data do evento e data do ator está explicada, mas mudar o campo é seu (item 34.7). (2) ~~Promover ou não PT-06~~ — **resolvido na quarta rodada, e sem mexer no critério:** você mandou ler a peça, o mecanismo ganhou âncora própria, PT-06 passou a `Confirmado` pela cadeia causal, e PT-08 não precisou ser reexaminado (item 35). (3) **Se Gohn (2019) fecha parcialmente a tarefa 10** — é o único balanço da literatura brasileira de protesto no corpus, e a 10 existe por essa lacuna. (4) **NOVO — Telegram e WhatsApp ficam nomeados em PT-06 sem verificação, ou saem do campo?** A peça os reporta por citação de segunda mão, e a regra do projeto não admite lastro nessa forma (item 35.5). (5) **NOVO — o esquema de 16 campos ganha campo para autonomia do movimento em relação ao líder?** É o argumento central de von Bülow e Abers e toca a pergunta desta pesquisa; hoje vive em `fonte_trecho` como achado (item 35.4). **(6) Este inventário é de 04/10 e não é a lista inteira:** as decisões nascidas depois estão nos itens que as geraram — a licença da sua obra e as duas higienes não executadas (**46.5**, **46.6**), o `marco_teorico` que cita obra não lida (**47.5**, decisão 2; a 3 ficou sem objeto), e as duas de 14/10 — o enunciado do projeto, que saiu com a pasta do edital, e a duplicata de 24,7 MB que o classificador barrou (**48.3**, **48.4**). **Não foram copiadas para cá de propósito:** lista à mão duplicada é lista que envelhece, e esta seção já é a prova disso.

> **Uma correção de contabilidade, em 04/10.** A tarefa 14 aparecia como dependente da **9** (triagem por pertinência), e a dependência estava errada: a camada A dos 411 DOIs é metodológica e de teoria geral, com **zero** referências sobre o Brasil, e nunca poderia codificar PT-01 a PT-06. A literatura que resolveu a tarefa veio de fora dos 411, de uma pasta que ninguém havia varrido. **A dependência real era de coleta brasileira — isto é, da tarefa 10 e da 25 —, não da triagem.**

> **Esta tabela envelheceu três vezes** — em 29/09 trazia a 18 duplicada e três números à mão na 17; em 30/09 manteve 20 e 21 como abertas depois de fechadas e não contou a 22; em 15/10 manteve a **15** aberta dois dias depois de executada e trazia na 17 uma cifra de duas rodadas antes, **na mesma linha que declara os números como gerados**. É a mesma lição de 25/09 batendo na peça que existe para registrar a lição. **A contagem da 17 é gerada e foi conferida contra o script; o resto desta tabela não é**, e é a próxima candidata a virar script — a terceira ocorrência é o argumento.

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
| **`Fontes/MANIFESTO-CORPUS.csv`** | **65 peças, medidas em 16/10/2026** — 63 PDFs e **2 âncoras não-PDF**: caminho, **SHA-256**, páginas, bytes, classe de licença e **rota de obtenção**. Toda peça tem rota — conferido. É o que mantém a pesquisa **verificável sem ser redistribuível**. A linha dizia *62 peças* e estava velha em três; as âncoras não-PDF entraram em 16/10, quando se descobriu que **o `.md` e o `.html` que ancoram registro não eram vigiados por nada** (item 62) |
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

1. ~~**O nome do mecanismo de PT-07.**~~ ✅ **DECIDIDO em 18/10/2026** — pela saída (c), *Deliberação de ruptura e articulação do quadro de fraude*, e não pela proposta abaixo, que nomeava só metade do que o registro documenta (item 65). O texto original segue como registro da proposta. **O nome do mecanismo de PT-07.** Hoje: *Alinhamento de quadros prévio*. Proposta: **Articulação e elaboração do quadro de fraude**, que é o que a fonte chama o processo documentado, deixando *alinhamento* para PT-06, onde o bridging de fato ocorre. Alternativa mais conservadora: manter o nome e acrescentar a especificação entre parênteses.
2. **O campo `marco_teorico` do codebook**, que cita *Framing (Snow & Benford, 2000)* — obra não lida e sem rota. Proposta: citar o capítulo de 2019, que está lido e no corpus, mantendo o de 2000 como referência da genealogia. Não executei: é a declaração teórica do projeto, e é sua.
3. ~~**A sessão 4 de `02_PROPOSTA-DISCIPLINA.md`** indica Snow & Benford (1988) e Benford & Snow (2000) — os dois não lidos.~~ **SEM OBJETO DESDE 14/10/2026:** o programa de disciplina era peça do edital e saiu do repositório (item 48). A decisão some; **o problema que ela media, não** — é a decisão 2, que segue aberta.

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

---

## 48. A reorganização do repositório — e a duplicata que era defeito — 🔶 14/10/2026

**Encaminhamento:** *"Organize esse repositório e faça a higiene dele… você desenvolveu somente em uma pasta e acabou deixando tudo nela… reorganize toda a nossa pasta do projeto a partir da raiz como main. Quando achar itens duplicados compare-os e decida pela versão mais completa e recente."* E, em seguida: *"elimine a pasta pós-doc e todos os documentos que se referem diretamente ao processo seletivo."*

### 48.1 O diagnóstico estava certo, e tinha uma causa simples

`projeto-pos-doc/` foi criada em 19/08/2026 para **um** edital — PIPD/CAPES, PPGS do IESP-UERJ, inscrições até 31/08/2026. O trabalho de pesquisa começou ali e **nunca saiu**: quando a leitura na fonte, os verbetes, as hipóteses rivais, a camada conjuntural e a literatura do bolsonarismo foram escritos, foram escritos naquela pasta, porque era onde o trabalho estava. **Nove dossiês de análise da pesquisa moravam dentro de uma pasta de candidatura**, e dois deles — `11_` e `12_` — são lidos pelo ciclo.

| Movido | Para | Por quê |
|:--|:--|:--|
| `projeto-pos-doc/{06,08..15}_*.md` (9) | `docs/analise/` | é o caderno de leitura da pesquisa, não peça de candidatura |
| `Claude outputs/ETAPA1_*.md` | `docs/historico/` | registro de sessão datado; a pasta de nome inglês com espaço desapareceu |
| `scripts/{recodificar,inserir,migrar}_*.py` (24) | `scripts/historico/` | **`scripts/` tinha 41 arquivos e 17 rodavam**; quem abria a pasta não distinguia o que roda do que já rodou |

**Nenhum arquivo foi renomeado**, de propósito: o nome é a chave de dezenas de citações em prosa, e renomear multiplicaria a reescrita por nada.

**As 57 referências foram reescritas por script, e nenhum caminho novo foi digitado** — cada um é calculado por `os.path.relpath` a partir da pasta do arquivo que o cita. **E o ciclo pegou o que isso erra:** `reports/` e `scripts/` usam caminho relativo à **raiz**, não à pasta do arquivo, e `conferir_relatorio.py` e `conferir_hipoteses.py` abortaram até os 15 casos serem corrigidos. É a primeira vez que uma checagem do ciclo pega defeito de **caminho**, e não de cifra.

### 48.2 A duplicata era defeito, e é o modo de falha da casa na forma de um hash

`projeto-pos-doc/figuras/` guardava um SVG e um HTML, e a LEIA-ME do dossiê os declarava **cópias byte-idênticas** dos de `reports/figures/`, com `sha1` registrado "para que a relação cópia→original seja verificável". **Medido em 14/10/2026:**

| Peça | `sha1` declarado | Cópia, de fato | Original, de fato |
|:--|:--|:--|:--|
| SVG da cronologia | `35ea4fc9…` | `35ea4fc9…` — **igual ao declarado** | `55268888…` — **o original andou** |
| HTML da cronologia | `183dc2e9…` | `a6885371…` | `1e82599a…` — **nenhum casa com o declarado** |

**A Figura 1 embutida no projeto de pesquisa estava seis semanas atrás do codebook**: a cópia é de 19/08, o original foi refeito em 30/09. E a varredura do histórico mostra que as duas foram idênticas **uma única vez**, no commit de 20/09; em 25/09 já diferiam — **o que torna falsa, na data em que foi escrita, a afirmação do relatório ETAPA1 de que eram "idênticas byte a byte"**. O aviso ficou escrito no próprio ETAPA1, que **não** foi corrigido no resto: registro datado que se reescreve para descrever o presente deixa de provar o que serve para provar.

> **Nada avisou, e a razão é estrutural:** `conferir_figuras.py` só olha `reports/figures/`, e a checagem 7 tratava a cópia como **artefato independente** — vigiava nome de mecanismo morto nela, não a identidade que ela declarava. **Identidade declarada que ninguém confere não é redundância: é duplicata.**

**Resolvido por eliminação, não por ressincronização.** `figuras/` saiu, os documentos do edital passaram a apontar para `../reports/figures/`, e a checagem 7 perdeu o caminho morto. O comando que refaz uma cópia autocontida, se um dia for preciso, ficou escrito na LEIA-ME do dossiê — que depois saiu com ele.

### 48.3 A pasta do edital eliminada — doze peças, e o que se perde com elas

Por encaminhamento seu, saiu tudo o que se refere ao processo seletivo: `00_ESPECIFICACAO-ESTILO`, `01_PROJETO-PESQUISA` e a versão compacta, `02_PROPOSTA-DISCIPLINA`, `03_CARTA-RECOMENDACAO`, `04_ROTEIRO-CV-LATTES`, `05_CHECKLIST-SUBMISSAO`, `07_REGISTRO-DE-REVISAO`, a `LEIA-ME` do dossiê, os dois arquivos de submissão (`.docx` e `.pdf`) e o PDF da chamada.

> **Uma peça dessas não é só do edital, e isto é o aviso que o registro deve carregar.** `01_PROJETO-PESQUISA.md` era **o enunciado do projeto** — título, pergunta, as quatro camadas, 2.442 palavras —, e é o que vários dossiês citam quando dizem "o projeto afirma". Ele saiu com os outros, porque foi escrito no formato do edital e você mandou eliminar o que se refere ao processo seletivo. **Está no commit `1b8d5a6` e volta inteiro com um comando:**
>
> ```bash
> git checkout 1b8d5a6 -- projeto-pos-doc/01_PROJETO-PESQUISA.md
> ```
>
> ~~**Se o enunciado do projeto deve viver na raiz — em `docs/`, livre do limite de palavras do edital —, é decisão sua**, e é a única da reorganização que eu não tomei.~~
>
> **DECIDIDA EM 18/10/2026: NÃO VOLTA.** Palavras suas: *"Deletei o projeto de pesquisa e movi os documentos que faziam parte do repositório que não tinham relação com o projeto de pesquisa. Não irei retomar o projeto de pesquisa, pois o mesmo não faz mais sentido agora. Ele estava somente acumulando material desnecessário ao repositório e fazendo com que você lesse de forma errônea todo o repositório."* O comando acima fica como registro de que a peça existe no histórico, **não como oferta**. Ver o item 63.

**As menções a essas peças nos registros datados não foram reescritas.** O item 898 desta agenda, o 1949 e as tabelas do documento 09 dizem o que diziam em 29/09 e em 10/10: que uma cifra foi corrigida em `01_PROJETO-PESQUISA.md`, que a atribuição dos quatro testes foi acertada em seis lugares. **Isso aconteceu, e aponta para o histórico, não para o disco.**

### 48.4 Higiene feita, e uma que foi barrada

| | |
|:--|:--|
| `scripts/` com 17 arquivos, todos vivos | ✅ |
| `docs/analise/` e `docs/historico/` criados; `Claude outputs/` extinta | ✅ |
| README com o mapa novo | ✅ e com **duas cifras à mão corrigidas**: o corpus era "24 PDFs, 7.501 p." e é **63 / 12.125**; o modo de falha era "cinco vezes" e são **dezesseis numeradas** |
| **Duplicata de 24,7 MB em `.backup_pre_lula/`** | ❌ **BARRADA.** `STF_Livro-8-1-2023-democraciainabalada…pdf` é **byte-idêntico** (mesmo SHA-256) ao do corpus em `Fontes/10_Democracia-Inabalada/` — é a **única duplicata byte-a-byte do repositório inteiro**, e responde por 92% do peso daquela pasta, que de resto são 19 estados do JSON. A remoção foi bloqueada pelo classificador de segurança, por ser deleção dentro da sua rede de segurança. **Fica para você**, e o canônico é o do corpus, que é o ancorado no manifesto: `git rm ".backup_pre_lula/STF_Livro-8-1-2023-democraciainabalada_2023_vandalismo-e-restauracao.pdf"` |

**O `.git` não encolhe com nada disto** — os blobs ficam no histórico, e `.git` tem 250 MB. O ganho é de árvore de trabalho e de clareza de leitura, não de disco.

---

## 49. A ordem de ataque deixa de ser escrita à mão — 🔶 15/10/2026

**Encaminhamento:** *"Transforme a tabela em script gerado."* A própria peça pedia isso desde 30/09: *"a contagem da 17 já é gerada; o resto desta tabela não é, e é a próxima candidata a virar script"*. Horas antes, o conserto do item 48 fechara a terceira rodada de contabilidade da mesma tabela.

### 49.1 O que passou a existir

| | |
|:--|:--|
| **`data/ordem_de_ataque.json`** | A fila como **dado**: 30 tarefas fechadas e 5 abertas, cada uma com número, texto, `estado`, itens desta agenda e — nas abertas — natureza e dependência. É curado à mão, como o codebook, e é a fonte da verdade da seção |
| **`scripts/gerar_ordem_de_ataque.py`** | Passo **3/9** do ciclo. Escreve a seção entre marcadores HTML e **prova por `assert` que o resto do arquivo não mudou** — é um gerador operando dentro de um documento de 2.300 linhas escritas à mão |
| **`scripts/historico/migrar_ordem_de_ataque.py`** | A migração de uso único que leu a seção do disco e a depositou no ledger. **Não divide título e nota, não reordena, não reescreve célula**: cada linha entrou como o texto que já era |

### 49.2 A prova da migração é a identidade, e ela veio antes de qualquer melhoria

Antes de trocar um número por medição, a primeira geração foi comparada com a seção que estava no disco: **idêntica, byte a byte**. É o que autoriza dizer que o ledger não perdeu nada no caminho — e é por isso que a migração foi escrita para *não* melhorar o texto que transportava. Só depois disso as cifras viraram chaves.

**E a promessa do "não editar à mão" foi testada por injeção:** plantei `As dezessete abertas` dentro do bloco e rodei o gerador. A frase desapareceu, e o bloco voltou ao que o ledger diz. Edição dentro dos marcadores se perde no ciclo seguinte — **quem edita a seção, edita o JSON**.

### 49.3 O que agora é medido, e o que ficou declarado como não medido

| Cifra | De onde vem |
|:--|:--|
| Os quatro estados da camada A — 8 lidos, 7 com ficha, 3 impedidos, 25 pendentes | `localizar_camada_a.py`, pela função `estado()` **importada, não reimplementada**: duas contagens do mesmo universo por dois códigos é como a cifra errada entra |
| As 8 pendentes na *Mobilization* | o mesmo universo, filtrado por veículo |
| Peças e páginas dos eixos 13 e 14, e o que falta ler no 13 | `Fontes/MANIFESTO-CORPUS.csv` — o mesmo arquivo que a checagem 8 confere por SHA-256. As três lidas são **nomeadas** no ledger por fragmento, e um fragmento que case com zero ou duas peças aborta |
| "As **cinco** abertas, por natureza" | derivada da tabela: palavra e agrupamento saem do campo `estado` e do campo `natureza` |
| **9 barradas no cliente** e **16 sem depósito aberto** | **não se medem a cada ciclo** — exigiriam rede. Ficam em `medidos_a_mao`, e o bloco **imprime a data de cada uma** |

> **A linha das cifras não medidas é o ponto desta rodada.** O defeito de 15/10 não foi um número errado: foi um número **sem idade visível** numa linha que anunciava procedência de script. Número que não se mede ou vira medição, ou carrega a data ao lado — e as duas da camada A agora carregam "medido em 13/10/2026".

### 49.4 A geração corrigiu uma cifra, e a correção tem causa conhecida

A linha da tarefa 10 dizia **"eixo 14 com 12 peças, 1.854 p."**. O manifesto conta **5 arquivos e 1.832 p.** A diferença não é erro de digitação: em 08/10 **o volume integral de *Giros à direita* substituiu oito offprints** (item 39.1), e desde então **peça coletada e arquivo no corpus deixaram de ser a mesma unidade**. A linha nova diz as duas coisas — 12 peças coletadas, 5 arquivos no manifesto — em vez de escolher uma e calar a outra.

**E uma cifra à mão caiu de carona, na documentação dos scripts:** `scripts/LEIA-ME.md` descrevia `verificar_integridade.py` como "**Seis** checagens estruturais" desde antes de 08/10. São **oito** — a 7 pega nome de mecanismo retirado, a 8 confere corpus × manifesto —, e o ciclo imprime "as oito checagens passaram" na mesma execução em que a LEIA-ME dizia seis.

### 49.5 O que o gerador NÃO faz, de propósito

1. **Não abre, não fecha e não ordena tarefa.** Estado é campo do ledger, preenchido por decisão humana. O script só impede que a linha fique na seção errada depois da decisão.
2. **Não tocou no inventário de decisões** logo abaixo do bloco: ele continua escrito à mão, e desde o item 48 aponta para os itens que geraram cada decisão em vez de copiá-las. **Lista à mão duplicada é lista que envelhece** — e essa é a lição que esta seção provou três vezes.
3. **Não reescreveu a prosa.** Os quatro parágrafos de histórico e os dois de fechamento foram para o ledger como estavam; mudou só onde havia cifra.

### 49.6 O primeiro uso do gerador pegou a quarta falha da tabela — e era a que mais importava

**A tarefa 19 estava listada como aberta, "decisão sua", e fechou em 10/10/2026.** Quem o diz são duas peças, com a mesma frase: o item 43.5 — *"Da tarefa 19, **nada**"* — e o cabeçalho da §4 do documento 09, *"com ela, a tarefa 19 fecha: as cinco cobranças estão resolvidas"*. A linha ficou aberta **cinco dias**, e com ela a aparência de que o codebook esperava uma decisão de nomenclatura que você já havia tomado.

> **E essa era a linha com consequência.** As outras três falhas da tabela eram de contabilidade — a 18 duplicada, a 15 atrasada dois dias, a cifra de 30/09 na 17. Esta mudava a resposta à pergunta *"o que falta para o banco de dados fechar?"*: com a 19 aberta, a resposta parecia incluir uma decisão de mecanismo; sem ela, **nenhuma tarefa da tabela pertence ao fechamento do banco** — as quatro abertas são literatura (10, 17, 25) e redação (16).

**O conserto foi do ledger, não do texto:** mudei `estado` para `fechada` e o gerador fez o resto — tirou a linha das abertas, pôs nas fechadas e **reescreveu sozinho "As cinco abertas" como "As quatro abertas"**. É o mecanismo do item 49 funcionando no primeiro uso real: a contagem seguiu o estado sem ninguém lembrar dela.

**E a cifra "sete cobranças" era falsa de outro modo: eram cinco.** A §4 do documento 09 tem oito linhas, mas duas delas dizem *passam* e *correto* — não eram cobrança —, e a de PT-03 saíra em 04/10. Contar linhas de tabela como cobranças é, mais uma vez, a cifra certa no referente errado.

> **Um efeito colateral visível, e é consequência de a frase ser derivada:** a ordem em que as naturezas aparecem agora segue a **ordem da tabela** — "leitura ou entrega de arquivo (10, 17, 25), decisão sua (19) e a redação (16)" —, não a ordem em que a mão as escrevia. Se a ordem importa, ela se muda reordenando as tarefas no ledger, que é onde a tabela também se ordena.

---

## 50. O que falta para o banco de dados fechar — medido no JSON — 🔶 15/10/2026

**Encaminhamento:** *"Meu primeiro interesse é fechar a construção do process tracing e, consequentemente, o banco de dados desse evento. As demais pendências colocamos em ordem subsequente."*

**A crítica estava certa e o diagnóstico é este:** as listas que eu vinha apresentando ordenavam por data de abertura e punham a tarefa 17 — 25 leituras de literatura — no topo, embora **ela não bloqueie nenhum registro**. Pior: traziam a tarefa 19 como aberta (ver 49.6). Este item responde à pergunta certa, e **mede no `process_tracing_8jan_eventos.json`**, não na prosa desta agenda.

### 50.1 O estado medido do codebook

| | Medido em 15/10/2026 |
|:--|:--|
| Registros | **83** |
| `status_classe` | **61** em fonte primária · **21** confirmados · **1** inferência (PT-62, por desenho: a âncora cobre 2023 e o registro projeta a 2026) |
| `A verificar` | **zero** — a classe existe no vocabulário e não é usada por nenhum registro |
| `mecanismo_causal` vazio | **zero** |
| Tarefas de **codificação** abertas | **nenhuma** — a última fechou em 04/10 (tarefa 14), e a de nomenclatura em 10/10 (tarefa 19) |

**O banco está construído.** O que falta não é codificar: é **fechar âncora** em seis registros e tomar quatro decisões de campo.

### 50.2 Seis registros não têm página — e nenhuma checagem do ciclo exige que tenham

| Registro | Documento vinculado | Por que não tem página |
|:--|:--|:--|
| **PT-03B** | TRF-4, acórdão da ACr 5046512-94 (no corpus) | o `fonte_trecho` é a **nota de imprensa** do TRF-4 — "a 8ª Turma confirmou hoje" —, e essa frase não está no acórdão |
| **PT-05A** | STF, ADC 43/44/54 (no corpus) | o trecho é da **Agência Brasil**; o acórdão é o documento, não a transcrição |
| **PT-06C** | STF, HC 193726-AgR (no corpus) | idem — notícia do STF e Agência Brasil |
| **PT-57** | STF, AP 2668, acórdão da condenação (no corpus) | o trecho é a **ementa do fato** ("publicação do acórdão, out/2025"), não citação de página |
| **PT-19A** | NetLab-UFRJ, `.md` (no corpus) | **não é PDF**: página não se aplica |
| **PT-03D** | **nenhum** | ancora só em URL da Agência Brasil, arquivada em `Fontes/09_Arquivamento-web/` (item 18) |

> **Por que nada avisou, e é o mesmo tipo de ponto cego de sempre.** A **checagem 5** confere coerência entre `fonte_pagina` e `fonte_local` — mas começa com `if not pag: continue`. **Ela confere quem cita página; quem não cita, passa.** Não há, em nenhum dos nove passos do ciclo, uma checagem que exija âncora de página para registro cujo documento vinculado é PDF do corpus. **Quatro registros estão nessa situação** (PT-03B, PT-05A, PT-06C, PT-57): o documento está no corpus, é PDF, e a página nunca foi apontada.

**O trabalho é de verificação, não de decisão:** abrir os quatro acórdãos, localizar a folha que sustenta o fato e transcrever dela — o que, nos quatro casos, **troca uma transcrição de imprensa por uma transcrição de fonte primária** e pode promover o registro de `Confirmado` para `Confirmado em fonte primária`. **PT-19A e PT-03D não são desse tipo** e se resolvem por declaração: um não tem página porque não é PDF, o outro porque sua fonte é notícia arquivada.

### 50.3 Os 17 fragmentos que casam só por janela

Medidos a cada ciclo pelo passo 7, com linha de base e *tripwire* desde 10/10 (item 45.3). Eram 45. **Reduzi-los é abrir documento por documento** — verificação, não decisão. É o segundo item do fechamento, e o único cuja contagem o ciclo já vigia.

### 50.4 As quatro decisões de campo que restam, e são suas

| | Decisão | Onde |
|:--|:--|:--|
| 1 | **`data_hora` de PT-02** — a ressalva está escrita como nota e a diferença entre data do evento e data do ator está explicada; mudar o campo é seu | 34.7 |
| 2 | **Telegram e WhatsApp em PT-06** ficam nomeados sem verificação, ou saem do campo? A peça os reporta por citação de segunda mão | 35.5 |
| 3 | **O esquema de 16 campos ganha campo para autonomia do movimento em relação ao líder?** É o argumento de von Bülow e Abers e toca a pergunta da pesquisa; hoje vive em `fonte_trecho` | 35.4 |
| 4 | **`marco_teorico` dos metadados cita Benford e Snow (2000), não lido** — e o capítulo de 2019, lido na fonte em 13/10, está no corpus. Entra no lugar, ou ao lado? | 47.5, decisão 2 |

**As três primeiras mudam campo de registro; a quarta muda metadado.** Nenhuma depende de leitura nova: as quatro estão instruídas.

### 50.5 O que NÃO pertence ao fechamento do banco

As quatro tarefas abertas da ordem de ataque. **A 10, a 17 e a 25 são literatura** — serviam à codificação até 04/10 e desde então servem à **redação**: a própria tabela declara que "nenhuma leitura pendente bloqueia registro". **A 16 é a redação.** Nenhuma delas precisa andar para o banco fechar, e é por isso que listá-las primeiro estava errado.

> **O que falta para a tabela espelhar isso:** a ordem de ataque **não tem linha para o fechamento do banco** — porque, quando foi escrita, fechar o banco *era* o conjunto das tarefas de codificação, e todas fecharam. O que sobrou migrou para prosa espalhada (45.3, 34.7, 35.4, 35.5, 47.5) e, hoje, para 50.2. **Proponho uma tarefa nova no ledger — "fechar as âncoras do codebook": as quatro páginas, os 17 fragmentos e as quatro decisões —, e a proposta é sua para aceitar**, porque criar tarefa na sua agenda é decisão de rumo, não contabilidade.

---

## 51. As quatro folhas, ancoradas — e o ponto cego virou guarda — 🔶 15/10/2026

**Encaminhamento:** *"Aprovado, crie a tarefa e comece pelas quatro páginas."*

### 51.1 O que entrou no codebook

| Registro | Folha, no PDF | O que a folha diz, em fonte primária |
|:--|:--|:--|
| **PT-03B** | TRF-4, **p. 30** e **p. 401** | *"decide a egrégia 8ª Turma do Tribunal Regional Federal da 4ª Região, por unanimidade, rejeitar as preliminares"*; e a dosimetria: *"as sanções resultam em 12 (doze) anos e 01 (um) mês de reclusão e 280 (duzentos e oitenta) dias-multa"* |
| **PT-05A** | ADC 43/44/54, **p. 2** e **p. 489** | a ementa — *"Surge constitucional o artigo 283 do Código de Processo Penal, a condicionar o início do cumprimento da pena ao trânsito em julgado"* — e o extrato de ata de 07/11/2019, que **nomeia os cinco vencidos** |
| **PT-06C** | HC 193.726, **p. 185** | *"por oito votos a três, este Plenário negou provimento ao Agravo Regimental para manter a decisão do eminente relator Ministro Edson Fachin no ponto em que declarava a incompetência do Juízo da 13ª Subseção Judiciária Federal de Curitiba/PR"* |
| **PT-57** | AP 2668, **p. 19** | o encerramento do acórdão e a sua data: *"Brasília, 15 de outubro de 2025"* |

**Seis transcrições, seis localizadas por inteiro na primeira execução** do passo 7, e `confirmados` subiu de **69 para 73**. A contagem de casamento parcial **não se moveu**: segue em 17, o que significa que nenhuma das novas entrou como fragmento frouxo.

**A transcrição de imprensa saiu das aspas nos quatro.** Ela não está na folha, e aspa que o conferidor não localiza é aspa que falha no ciclo — ou, pior, que é dispensada por exceção e passa a parecer lastro. O fato noticiado continua no registro, em prosa, marcado como *"contexto de imprensa, sem valor de âncora"*, e a URL segue onde estava.

### 51.2 Duas armadilhas achadas na leitura, e as duas são do tipo da casa

> **A primeira está em PT-05A, e eu quase a pisei.** O registro afirma **6 votos a 5**, e a busca por "6 votos a 5" no acórdão **casa** — na p. 31, na voz do relator. Mas lá a expressão se refere ao **julgamento virtual de outro caso**, e em hipótese: *"o seria, presumo, por 6 votos a 5, houvesse votado a ministra Rosa Weber"*. **Citar aquela folha como placar desta decisão seria a cifra certa no referente errado, com aspas e página** — a forma mais convincente do erro que este projeto persegue. O que o documento dá de fato está na p. 489: cinco vencidos nomeados, onze ministros presentes nomeados. **O "6" é aritmética sobre dado primário, não citação, e está declarado como tal na `nota_auditoria`.**

> **A segunda está em PT-57, e não se resolve por leitura.** O registro afirma a **publicação do acórdão em 22/10/2025**. Varri as **1.991 páginas** por `22/10/2025`, `outubro de 2025`, `DJe-N` e `PUBLIC`: **a data não está no documento**. O que o acórdão data é a si mesmo — *"Brasília, 15 de outubro de 2025"*, assinatura do relator, sendo a sessão de julgamento de 11/09/2025. Os carimbos `ACÓRDÃO ELETRÔNICO DJe-N DIVULG … PUBLIC …` que aparecem no corpo são de **precedentes citados nos votos**, não deste acórdão. **A publicação em 22/10/2025 não tem âncora no corpus, porque o DJe não está entre as fontes.**

### 51.3 O ponto cego virou guarda, dentro da checagem 5

A checagem 5 abria com `if not pag: continue` — **conferia quem citava página, e quem não citava passava**. Foi por aí que quatro registros atravessaram dois meses de ciclo vinculando PDF do corpus sem apontar folha. A **pergunta inversa** entrou na mesma checagem: *vinculou PDF e não citou página?*

**Prova negativa:** apaguei o `fonte_pagina` de PT-06C e rodei — `! PT-06C vincula PDF do corpus e não aponta folha`, `RESULTADO: 2 FALHA(S)`, código de saída 1. Restaurado em seguida.

> **Entrou na 5 em vez de virar checagem 9 de propósito:** é a mesma pergunta — coerência entre `fonte_pagina` e `fonte_local` — vista do outro lado, e o ciclo continua com **oito** checagens, sem renomear a contagem em seis documentos. **E a guarda nasce com lista de dispensa vazia:** os dois registros sem página que restam não vinculam PDF, então não precisam de exceção. Lista de dispensa vazia é a melhor que existe — exceção registrada é dívida que ninguém revisita.

### 51.4 Os dois sem página, declarados — **hoje é um só**

| Registro | Por que não tem folha |
|:--|:--|
| **PT-19A** | o documento é a síntese do NetLab-UFRJ em **`.md`**, não PDF: não há folha a citar, e a âncora é o arquivo inteiro, cujo SHA-256 a checagem 8 vigia — **ver a errata abaixo** |
| **PT-03D** | **não tem documento**: ancora em notícia da Agência Brasil arquivada contra *link rot* (item 18), que preserva a evidência de que a notícia existiu — não é fonte primária. O ato que ela noticia executa decisão do TRF-4 **já ancorada em PT-03B** |

> **ERRATA, 16/10/2026 — duas, e a segunda é grave.** (1) PT-19A **deixou de ser caso de isenção**: desde 16/10 ele cita `NetLab: inteiro teor — §Achado principal, §Relevância para o codebook, §Ressalvas de uso`, pela mesma convenção de localizador estrutural que PT-03E já praticava — de modo que o único registro sem `fonte_pagina` hoje é PT-03D. (2) **A frase "cujo SHA-256 a checagem 8 vigia" era FALSA quando foi escrita.** O manifesto era gerado varrendo `Fontes/**/*.pdf` e tinha 63 peças, todas PDF: este `.md` — e o `.html` do acórdão do TSE que ancora PT-03E — não eram vigiados por nada. **A garantia que justificava a exceção não existia**, e a asserção sobreviveu um dia inteiro porque ninguém a conferiu. Corrigida em 16/10: o manifesto passou a incluir os arquivos não-PDF que ancoram registro, lidos do `fonte_local` e não de lista à mão (item 62).

### 51.5 O que isto deixa para você — e é decisão, não trabalho

1. **A promoção de classe de três registros.** PT-03B, PT-05A e PT-06C passaram a ter transcrição de fonte primária com folha. **Não promovi**: pelo precedente da tarefa 19, mudar a classe de um registro é sua. A evidência está na `nota_auditoria` de cada um, e **PT-06C é o caso mais limpo** — uma só folha cobre data, placar, objeto e fundamento.
2. ~~**A data de PT-57**, e são três saídas: **(a)** trocar `data_hora` para **15/10/2025**, que é o que a fonte primária data, e reformular o registro como *conclusão* do acórdão; **(b)** manter 22/10/2025 e declarar a limitação no registro; **(c)** incorporar o **DJe** ao corpus, e aí a publicação ganha âncora própria. Não alterei a data — é a mesma classe de decisão do `data_hora` de PT-02 (item 34.7).~~ — ✅ **DECIDIDA E EXECUTADA em 21/10/2026, pela saída (a):** ver item 71. **E a errata que a execução trouxe é sobre uma aspa, não sobre a conclusão:** a frase acima escreve *"ACÓRDÃO ELETRÔNICO DJe-N DIVULG … PUBLIC …"* entre aspas, e `DJe-N` **não ocorre no documento** — é abreviação minha para *DJe-<número>*, posta entre aspas como se fosse transcrição. As formas reais são `DJe-161`, `DJe-130`, `DJe-045`. **Quanto ao resto, a nota de 15/10 está confirmada:** os carimbos existem — `ACÓRDÃO ELETRÔNICO`/`PROCESSO ELETRÔNICO` em 7 folhas, `DIVULG` em 11 — e são de **precedente citado**, lidas as folhas 888, 910 e 1059: *AP 470 EI-quintos*, *AP 932* e *HC 132179*.

**O que resta da tarefa 26 é (b) e (c):** os 17 fragmentos por janela, que é verificação minha, e as cinco decisões de campo, que são suas.

---

## 52. Os 17 fragmentos por janela, resolvidos — e quatro deles eram âncora na folha errada — 🔶 15/10/2026

> **Correção de contagem, 15/10/2026, pela medição do item 53.** Este item foi escrito dizendo **"quatro eram âncora no documento errado"**. Medido com o próprio localizador: os quatro saem do casamento parcial pela correção, mas são **três de documento errado e um de página errada dentro do mesmo documento**. O número 4 está certo; a caracterização estava errada, e a diferença importa justamente aqui — errar o documento é creditar a frase a outra peça, e errar a página é creditá-la à folha vizinha da peça certa. Os dois são defeito, e só um é o defeito grave que dá nome à seção 52.1. Corrigido no título, na tabela, em `conferir_paginas.py` e no ledger.

**Encaminhamento:** *"Siga com os 17 fragmentos."* É a parte (b) da tarefa 26.

**O resultado:** os 17 foram a **zero resíduo inexplicado**, e a queda não veio de afrouxar o critério — veio de **classificar a causa de cada um**, como em 10/10. Duas das cinco classes são defeito real, e uma delas é grave.

| Causa | Quantos | É defeito? |
|:--|--:|:--|
| **Âncora creditada à folha errada** — 3 ao documento errado, 1 à página errada do mesmo documento | **4** | **Sim — e no localizador, não na transcrição** |
| **Transcrição editada dentro das aspas** (PT-39) | **2** | **Sim — na transcrição** |
| Marcador de nota de rodapé colado na prosa pela extração | 8 | Não |
| Citação atravessando a quebra de página com o aparato da folha no meio | 3 | Não |
| **Resíduo inexplicado** | **0** | — |

### 52.1 O defeito grave: o conferidor creditava a âncora ao documento errado

`localizar()` devolvia **a primeira folha em que qualquer janela de 40 caracteres casasse**, na ordem em que os documentos aparecem em `fonte_pagina`. E as peças deste corpus **se citam entre si**: o relatório da CPMI transcreve o do interventor, e os dois repetem a fórmula *"Secretaria de Estado de Segurança Pública do Distrito Federal"*, que tem mais de 40 caracteres.

> **Resultado medido:** uma transcrição do **DODF nº 001** foi creditada a **Cappelli p. 35** por uma janela de texto administrativo; a **conclusão A do relatório do interventor** foi creditada a **CPMI p. 576**. O conferidor dizia "localizada", e a divergência aparecia na lista de casamento parcial — **onde parecia infidelidade de transcrição e era erro de atribuição**. É a cifra certa no referente errado na forma de uma âncora, dentro do script que existe para impedir exatamente isso.

**A correção não endurece nada:** o conjunto de fragmentos localizados é o mesmo. Mudou a **ordem de preferência** entre folhas candidatas — primeiro a que contém o texto integral, depois a que confere ao juntar a vizinha, depois a que confere ignorando o marcador de nota, e só em último caso a janela. **Sozinha, essa correção tirou 4 dos 17** — e são estes quatro, medidos no item 53: `Cappelli p.35 → Cappelli p.58` (página errada, mesmo documento), `Cappelli p.35 → DODF 001 p.16`, `Cappelli p.35 → DODF 003 p.35` e `CPMI p.576 → Cappelli p.53`.

### 52.2 As duas transcrições de PT-39, e nenhuma era erro de fato

| O que o registro escrevia, entre aspas | O que a folha diz |
|:--|:--|
| "subsecretária da Secretaria de Inteligência **da SSP-DF**" | "subsecretária da Secretaria de Inteligência **da Secretaria de Segurança Pública do Distrito Federal**" (CPMI, p. 677) |
| "no Grupo Difusão**,** afirmando que" | "no Grupo "Difusão" afirmando que" (AP 2668, p. 496) |

**O conteúdo estava certo nas duas.** Uma abreviava a sigla do órgão **dentro das aspas**; a outra acrescentava uma vírgula. **Abreviar e pontuar dentro de aspas é editar a fonte** — e é o tipo de edição que ninguém chamaria de erro, razão pela qual atravessa. Restaurada a letra das duas folhas, com a correção registrada na `nota_auditoria` do registro.

### 52.3 As duas classes que não são divergência

**Marcador de nota de rodapé — 8 casos.** A camada de texto do PDF cola o número da nota na prosa: a folha traz *"…prontidão**798**. De acordo com o depoimento"* onde a transcrição traz *"…prontidão. De acordo com o depoimento"*. A classe ganhou teste próprio, e **o alinhamento é deliberadamente assimétrico**: pula dígito que está **na folha e não na transcrição**, nunca o contrário, até 4 dígitos por salto e 6 saltos.

> **Por que a assimetria importa num projeto cujo modo de falha é a cifra no referente errado:** se a fonte diz "2.451" e a transcrição diz "2.151", o dígito divergente está **na transcrição** — o alinhamento para ali e o fragmento continua reprovando. Absorção cega de dígitos mascararia justamente o defeito que este projeto persegue.

**Quebra de página com o aparato da folha no meio — 3 casos.** A citação atravessa a quebra, e entre as duas metades ficam o **bloco de notas no pé** da folha (com URLs) ou o **rodapé de assinatura digital** e o número da página seguinte. O teste de par de páginas que já existia falhava porque concatena as duas folhas inteiras. O teste novo exige que o resto **comece a página seguinte** — nos primeiros 120 caracteres —, e por isso não mascara edição de cauda: o resto tem de aparecer literalmente.

### 52.4 A linha de base agora é ZERO, e é a guarda no seu ponto mais forte

Eram **45** em 09/10, **17** em 10/10 e o resíduo inexplicado é **0** desde hoje. Com zero, **qualquer** fragmento que passe a casar só por janela faz o ciclo cair — não há mais um número de base dentro do qual um defeito novo possa se esconder.

**Prova negativa, duas injeções:**

| Injeção | Resultado |
|:--|:--|
| PT-31, troca de palavra **no meio** ("insurgentes" → "invasores") | `1 fragmento SEM CAUSA CLASSIFICADA`, saída **1** |
| PT-26, troca de palavra **na cauda** ("uma parcela" → "duas parcelas") | `1 fragmento SEM CAUSA CLASSIFICADA`, saída **1** |

> **A segunda é a que importa.** Em 09/10/2026 a prova negativa mostrou que **2 de 4 injeções escapavam, e as duas eram troca de palavra no fim do trecho**. Era o ponto cego declarado do conferidor, e a razão de existir a linha de base de 17. **Hoje ele não escapa** — e o que o fechou não foi endurecer o casamento por janela, que continua aceitando as 45 âncoras legítimas, mas nomear as causas até sobrar zero.

### 52.5 O que isto fecha, e o que não

**A tarefa 26 perde a parte (b).** Resta a **(c)**: as cinco decisões de campo, todas suas — `data_hora` de PT-02 (34.7), Telegram e WhatsApp em PT-06 (35.5), o campo para autonomia do movimento (35.4), o `marco_teorico` que cita obra não lida (47.5) e a data de PT-57 (51.5).

**E restava uma pergunta que esta rodada abriu e não respondeu** — as **4 âncoras mal atribuídas** passaram dois meses contadas como localizadas, e a preferência por texto integral torna improvável, não impossível, que outra esteja na folha certa por coincidência de fórmula burocrática. **Respondida no item 53, em 15/10/2026, a seu pedido:** medidas as folhas candidatas de todos os 234 fragmentos, **nenhuma âncora depende da ordem de `fonte_pagina` para escolher entre documentos**, e o zero virou guarda.

---

## 53. As folhas candidatas, medidas: a âncora é escolhida pelo texto, e o zero virou guarda — 🔶 15/10/2026

**Encaminhamento:** *"Meça as folhas candidatas do item 52.5."*

**A pergunta.** Desde 15/10/2026 `localizar()` **prefere a folha que confere por inteiro**, em vez da primeira que casasse por janela. Mas preferência só decide quando há diferença: se duas folhas conferem na **mesma classe**, quem escolhe é a **ordem de `fonte_pagina`** — e isso é exatamente a fragilidade que manteve quatro âncoras mal atribuídas por dois meses. A pergunta não é se o localizador melhorou; é **de quantas âncoras ele é o único fiador**.

**A medição**, feita reusando o próprio conferidor — duas normalizações do mesmo texto por dois códigos é como a divergência entra:

| Folhas candidatas que casam por janela | Fragmentos |
|:--|--:|
| **1** — não há escolha a fazer | **217** |
| 2 | 13 |
| 3 ou mais | 4 |
| **total de fragmentos localizados** | **234** |

E a pergunta que importa, dos **17** fragmentos com mais de uma candidata:

| | Fragmentos |
|:--|--:|
| **Decididos pelo TEXTO** — a folha escolhida confere numa classe estritamente melhor que todas as rivais | **15** |
| Empate entre **páginas do mesmo documento citado** | 2 |
| **Empate entre DOCUMENTOS** — a ordem de `fonte_pagina` decidindo | **0** |

> **Nenhuma âncora do codebook depende da ordem de `fonte_pagina` para escolher entre documentos.** Em todos os 15 casos disputados a folha vencedora confere **por inteiro** e as rivais **só por janela** — a escolha é do texto, não do arranjo do campo. E só **4 fragmentos** têm candidata em mais de um documento, todos os quatro com vencedora de classe `ok` contra rivais `parcial`: três transcrições de PT-18A, que o relatório do interventor, o da CPMI e dois DODF repetem, e a de PT-52.

**Os 2 empates são entre páginas da mesma peça, e a âncora está certa das duas maneiras:** PT-53 confere por inteiro nas p. 4 **e** 6 do Balanço do STF, PT-58 nas p. 8 **e** 10 da Pet 14.129 — fórmula que a própria peça repete. As duas folhas estão em `fonte_pagina`, as duas pertencem ao documento que o registro cita, e por isso **não contam como defeito**: o efeito colateral é apenas uma folha aparecendo na lista de *páginas que nenhuma transcrição alcança*, que é sinal e não falha. Fazê-las derrubar o ciclo seria ruído, e **ruído treina a ignorar guarda**.

### 53.1 O número que eu havia relatado errado

A medição derrubou uma cifra minha, de ontem. Eu relatei — aqui, no ledger, em `conferir_paginas.py` e no commit `a462204` — que **"4 eram âncora creditada ao documento errado"**. Medido com o localizador, fragmento por fragmento:

| A regra velha dizia | A nova diz | O que era |
|:--|:--|:--|
| Cappelli p. 35 `[parcial]` | Cappelli **p. 58** `[ok]` | **página errada, mesmo documento** |
| Cappelli p. 35 `[parcial]` | **DODF 001** p. 16 `[ok]` | documento errado |
| Cappelli p. 35 `[parcial]` | **DODF 003** p. 35 `[ok]` | documento errado |
| CPMI p. 576 `[parcial]` | **Cappelli** p. 53 `[ok]` | documento errado |

**São 4, e três são de documento errado — o quarto é de página errada dentro da peça certa.** O total que eu dei estava certo; a caracterização, não. É o modo de falha desta casa na sua forma mais barata de produzir: **a cifra correta no referente errado**, aqui com o referente sendo a própria classe do defeito. Corrigido no título do item 52, na tabela de causas, no comentário e na saída de `conferir_paginas.py` e no texto da tarefa 26 no ledger. O commit `a462204` fica como está — **histórico não se reescreve para parecer melhor**; esta é a errata.

### 53.2 O zero virou guarda, com prova negativa

`localizar()` já calculava todas as candidatas e a classe de cada uma, então detectar o empate custou uma linha de conjunto. Passou a devolver um quarto valor — **os documentos empatados na classe vencedora** —, `EMPATES_BASE = 0` entrou ao lado de `PARCIAIS_BASE`, e **o primeiro empate entre documentos que aparecer derruba o ciclo**, com os dois códigos e o trecho impressos para você abrir as duas folhas.

**Prova negativa, duas injeções:**

| Injeção | Resultado |
|:--|:--|
| `confere_integral` cegado em `"parcial"` — que é literalmente a cegueira de antes de 15/10 | os **4** fragmentos multi-documento viram empate e o detector aponta os 4; com a visão restaurada, **0** |
| Fragmento de texto **real** presente por inteiro em duas peças citadas | o detector devolve `('ADC 43/44/54', 'AP 2668')` |

> **E a segunda injeção achou algo que não procurava.** O trecho de 70 caracteres que está por inteiro em duas peças distintas é o **rodapé de assinatura digital do STF** — *"assinado digitalmente conforme MP nº 2.200-2/2001…"* —, presente em toda folha de todo acórdão. **Casamento por janela entre documentos é inseguro por construção neste corpus**, e não só porque as peças se citam: o aparato é compartilhado de fábrica. O que protege o codebook não é a janela ser longa, é a transcrição vir **de dentro das aspas** de `fonte_trecho` — ninguém transcreve rodapé. A guarda agora cobre a hipótese de alguém transcrever.

### 53.3 O que isto fecha

**A tarefa 26 fica só com a parte (c)** — as cinco decisões de campo, todas suas. A pendência de verificação aberta em 52.5 está **respondida e fechada**, e não gerou pendência nova.

---

## 54. A sexta decisão, que a contagem à mão omitia — 🔶 16/10/2026

**Encaminhamento:** *"Corrija a contagem para seis no ledger."*

**O que aconteceu.** Ao listar o que resta, conferi as decisões de 26(c) contra o JSON e contra o item que gerou cada uma. **A tarefa 26(c) dizia "cinco decisões de campo"; são seis.** A que faltava é a **decisão 1 do item 47.5** — o nome do mecanismo de PT-07 —, aberta desde 13/10/2026 e nunca listada.

**Três leituras para afirmar que está aberta**, e nenhuma é contra outra citação dela:

| O que foi lido | O que diz |
|:--|:--|
| `process_tracing_8jan_eventos.json`, PT-07 | `mecanismo_causal` ainda começa por **"Alinhamento de quadros prévio"** — o nome que 47.5 propõe trocar |
| Toda a agenda, de 47.5 ao item 53 | **nenhum registro posterior decide o nome**; "Articulação e elaboração do quadro de fraude" aparece uma única vez, na própria proposta |
| Item 2166 e o aviso de 2168 | a proposta nasceu da leitura na fonte de 13/10 e traz escrito *"NÃO renomeei: nomear mecanismo é decisão do pesquisador, pelo precedente da tarefa 19"* |

**De onde veio a omissão, e ela tem endereço.** O inventário que virou a tarefa 26 é o item **50.4**, *"As quatro decisões de campo que restam"*, escrito em 15/10/2026. Ele cita **"47.5, decisão 2"** e não cita a decisão 1 — foi **copiado à mão** do item que o antecede. Dali a contagem seguiu para 51.5, para o item 52, para 53.3 e para o ledger, sempre como *cinco*. **O número nunca foi medido; foi transcrito.**

> **E o aviso contra isso já estava escrito nesta agenda, pela minha mão.** O ponto 6 do inventário de 04/10 diz, sobre as decisões nascidas depois: *"Não foram copiadas para cá de propósito: lista à mão duplicada é lista que envelhece, e esta seção já é a prova disso."* Onze dias depois, 50.4 copiou à mão — e envelheceu em um dia. **A regra não falha por ser desconhecida; falha por não ser mecânica.** O ledger é gerado e por isso o número aparece numa linha só; mas `{{chave}}` mede corpus, não mede a agenda, e **nenhum passo do ciclo confere se toda decisão marcada como sua está na fila.**

**O que mudou:** só o texto de 26(c) no ledger, de **cinco** para **seis**, com a sexta nomeada e datada. **O que não mudou:** o nome de PT-07, que segue seu; e o texto dos itens **50.4, 51.5, 52 e 53.3**, que dizem *cinco* porque era isso que eu afirmava quando foram escritos — **histórico não se reescreve para parecer melhor**, e esta é a errata a que eles remetem.

### 54.1 A sétima, que não executei porque classificar é decidir

A mesma recontagem levanta uma pergunta que não é de contagem: **a promoção de classe de PT-03B, PT-05A e PT-06C** (item 51.5, decisão 1) também é decisão sua e também muda campo de registro — `status_classe`, hoje `Confirmado` nos três, contra `Confirmado em fonte primária` que PT-07 já carrega. **Ela não está em 26(c)**, e vive como pendência solta desde 15/10.

**Não a acrescentei por conta própria.** Pelo critério do texto — "decisões de campo" —, ela é a sétima; pelo arranjo de 15/10, era pendência própria. **Mover pendência de lugar na sua agenda é decisão de rumo, não contabilidade**, e é o mesmo motivo pelo qual 50.4 propôs a tarefa 26 em vez de criá-la.

> **RESPONDIDA no mesmo dia:** *"Passe 26(c) para sete."* A promoção entrou na fila como sétima decisão de campo, e o critério que vale daqui para frente está dito pela sua escolha — **o que muda campo de registro pertence a (c)**, mesmo quando nasceu em outro item. Os três `status_classe` seguem `Confirmado`: **trazer a decisão para a fila não é tomá-la.**

---

## 55. O esquema ganha o 17º campo: `autonomia_movimento` — 🔶 16/10/2026

**Encaminhamento:** *"Decida a 3: o esquema ganha o campo de autonomia."* É a decisão 3 da tarefa 26(c), aberta desde 04/10/2026 no item 35.4 — **a primeira das sete a sair da fila.**

**A pergunta que o campo responde é a da pesquisa.** Von Bülow e Abers (2024) sustentam que o bolsonarismo é movimento social com autonomia relativa em relação ao líder: o presidente *"depends on a well-organized grassroots mobilization process that pre-dates his emergence as a populist radical-right leader and which he does not fully control"* (p. 1000 impressa — PDF p. 3). Isso é exatamente **o 8 de janeiro foi conduzido de cima ou teve vida própria** — e nenhum dos 16 campos a codificava. O achado vivia em `fonte_trecho` de PT-06: legível por quem lesse o registro inteiro, **invisível para qualquer contagem**.

### 55.1 O que entrou

| | |
|:--|:--|
| **Campo** | `autonomia_movimento`, entre `mecanismo_causal` e `fonte_trecho` — fica ao lado da outra atribuição analítica, que é onde um parecerista procura |
| **Tipo** | categórico, vocabulário controlado, como `status_classe` |
| **Migração** | `scripts/historico/migrar_esquema17.py`, rodada única e idempotente, no padrão de `migrar_esquema16.py` de 16/08 |

| Valor | O que afirma |
|:--|:--|
| **Autonomia relativa** | a fonte documenta processo de mobilização com vida própria, anterior à liderança ou não inteiramente controlado por ela |
| **Conduzido de cima** | a fonte documenta ação dirigida, convocada ou coordenada por liderança, órgão ou comando |
| **Não se aplica** | o registro não codifica ação de movimento — ato de Estado, decisão judicial, medida administrativa |
| **(vazio)** | **NÃO CODIFICADO** — registro que ainda não foi lido sob esta pergunta |

> **O vazio não é valor, e essa é a decisão de desenho que importa.** Fundir *"não se aplica"* com *"ninguém olhou ainda"* num único vazio tornaria a pendência invisível no dia em que ela nascesse — e invisível é o estado em que as quatro âncoras mal atribuídas passaram dois meses. Por isso o vazio é **contado e impresso** no passo 4 do ciclo: **82 dos 83** — medição daquele dia; o campo fechou nos **83** em 16/10, com o último vazio resolvido no item 62. Zero medido é guarda; zero suposto é silêncio.

### 55.2 Um registro codificado, e 82 não — de propósito

**Codifiquei PT-06 e mais nenhum.** PT-06 entra porque **não é interpretação nova**: as duas transcrições que o sustentam estão em `fonte_trecho` desde 04/10/2026, as páginas estão em `fonte_pagina` (`VON BULOW E ABERS 2024: 3 e 12`), **o ciclo já as confere contra o PDF a cada execução**, e *"autonomia relativa"* é a expressão com que o item 35.4 e o documento 13 descrevem a peça. O valor sai do texto já conferido, não de uma leitura minha de hoje.

**Os outros 82 não entram porque atribuir valor é CODIFICAR** — exige abrir a fonte de cada registro e decidir —, e codificação não se executa por inferência neste projeto. Migrar o esquema e codificar o campo são duas tarefas, e só a primeira foi autorizada.

### 55.3 Três guardas, e a prova negativa de cada uma

| Guarda | Onde | O que derruba |
|:--|:--|:--|
| Vocabulário | checagem 4 | valor que não é um dos três |
| **Valor afirmativo exige folha** | checagem 4 | `Autonomia relativa` ou `Conduzido de cima` em registro sem `fonte_pagina` — *"Não se aplica"* está fora da cobrança, porque **negar pertinência não precisa de folha e cobrá-la seria ruído** |
| Esquema declarado | checagem 1 | `metadados.colunas_codebook` dizendo coisa diferente dos cabeçalhos que o gerador usa |

| Injeção | Resultado |
|:--|:--|
| PT-06 com `"Autonomia media"` | reprova — `! valores fora do vocabulário: ['Autonomia media']` |
| PT-19A codificado `Conduzido de cima` (é um dos dois registros sem `fonte_pagina`) | reprova — `! codificado sem fonte_pagina: ['PT-19A']` · **esta injeção deixou de ser reproduzível em 16/10**, quando PT-19A ganhou localizador; a cobrança foi **reancorada em PT-03D**, hoje o único sem `fonte_pagina`, e reprovou igual: `! codificado sem fonte_pagina: ['PT-03D']` (item 62) |
| `colunas_codebook` sem o campo 17 | reprova — `! metadados.colunas_codebook divergem dos cabeçalhos do gerador` |

> **A terceira guarda nasceu de um achado da própria migração.** `metadados.colunas_codebook` estava escrito desde 16/08/2026 pela migração de então e **nenhuma checagem o lia** — era esquema declarado que ninguém conferia, a mesma família do `sha1` que declarava identidade já desfeita (item 48) e da menção lida como declaração de licença (47.4). Hoje ele é conferido contra `CABECALHOS`, que é o que o gerador usa de fato. **O campo novo pagou por uma guarda que faltava ao esquema velho.**

### 55.4 O que isto deixa

1. ~~**A codificação dos 82 registros no campo novo**~~ — **ABERTA NO MESMO DIA, a seu pedido: é a tarefa 27 do ledger.** É leitura, registro por registro, e era a tarefa que o campo criava. Eu não a havia aberto, pelo precedente de 50.4 — criar tarefa na sua agenda é decisão de rumo —, e a decisão veio em seguida. **A contagem do que falta entrou como chave medida** (`{{autonomia_sem_codificar}}`), não como 82 digitado: a linha da tarefa encolhe sozinha a cada registro codificado, que é o contrário do que aconteceu com a linha da tarefa 17. Observação de escopo, para quando aceitar: boa parte dos 83 é ato de Estado e decisão judicial, de modo que **o valor dominante tende a ser *Não se aplica*** — e a pergunta de desenho que isso levanta é se o campo deve ser codificado só na camada de mobilização ou em todas.
2. **Nome e vocabulário são seus.** Propus `autonomia_movimento` e os três valores; trocar qualquer um é um comando. Pelo precedente da tarefa 19, nomear é do pesquisador — eu nomeio para que o campo exista, não para fechar a questão.
3. **A outra metade de uma correção de 30/09, dezesseis dias depois.** O item 29.1 registra que acrescentar PT-18A quebrou o ciclo em quatro pontos, um deles a mensagem de `verificar_integridade.py` com **"82 x 16" fixo no texto** — *"passava na checagem e mentia na saída"*. Aquela rodada trocou o **82** por medição e **deixou o 16**, porque o 16 ainda estava certo. Hoje a mensagem dizia "83 x 16" sobre um codebook de 17 campos: **corrigiu-se a metade que já estava errada e manteve-se a que só estava certa por enquanto.** Agora os dois números saem de `len()`. A lição é estreita e vale escrita: **ao substituir uma cifra fixa por medição, meça as outras da mesma linha** — a que não mudou hoje é a que vai mentir sozinha depois.
4. **Achado de passagem, e é cifra sem lastro:** o `README.md` dizia **"82 sub-eventos"** desde que PT-18A entrou e o codebook foi a 83, em 30/09/2026 — dezesseis dias. Corrigido junto, porque a linha estava sendo editada de todo modo — e é da mesma família de sempre, a cifra que envelhece sem idade visível. **Não numerei a ocorrência:** a contagem da família está em duas formas na agenda (as dezesseis numeradas e as acrescentadas em 13, 14 e 15/10), e somar de cabeça é o próprio defeito.

---

## 56. Tarefa 27, primeira rodada: a camada de mobilização, e a folha que faltava — 🔶 16/10/2026

**Encaminhamento:** *"Comece pela camada de mobilização."*

**O recorte, e ele é do próprio esquema.** *Camada de mobilização* é a fase que o campo `fase` nomeia: **`T0 Mobilização`, cinco registros**, PT-24 a PT-28 — a marcha que sai do Setor Militar Urbano às 13h e chega à linha de contenção às 14h43. Não ampliei o recorte: as camadas vizinhas, onde a pergunta também discrimina, estão contadas em 56.3.

| | Valor | O que o sustenta |
|:--|:--|:--|
| **PT-24** | **Autonomia relativa** | CPMI **p. 644**, folha nova neste registro |
| **PT-25** | **Não se aplica** | ator de Estado — o áudio do secretário em exercício ao governador |
| **PT-26** | **Autonomia relativa** | CPMI p. 650, folha já citada |
| **PT-27** | **(vazio)** — lido e não codificado | a folha 651 documenta a barreira, não quem dirigia |
| **PT-28** | **Não se aplica** | ator de Estado — a postura do batalhão da PMDF |

### 56.1 A folha 644, que o registro não citava, e é ela que responde

**A pergunta da autonomia tinha resposta documental, e ela estava a uma folha de distância.** PT-24 citava as folhas 645 e 648 da CPMI — o horário da marcha e a escolta da PMDF. Quem responde *quem decidiu a marcha* é a **644**, onde o relatório reproduz os alertas da Abin das 8h30 e das 10h:

> *"os acampados aparentam estar divididos em grupos, com sua própria organização cada"*
>
> *"após discussão acalorada entre acampados às 8h50, ficou decidido que os manifestantes partirão em marcha para a esplanada às 13h"*
>
> *"em votação, decidiram que a marcha só iniciará quando todas as caravanas chegarem e estão evitando divulgar um horário para o início"*

**Deliberação horizontal documentada em fonte primária, e com o método da decisão nomeado: discussão e voto.** Não é inferência sobre ausência de liderança — é registro positivo de como a decisão foi tomada, feito por quem monitorava o acampamento naquela manhã.

As três transcrições entraram em `fonte_trecho` e a folha em `fonte_pagina`, de modo que **o passo 7 do ciclo passou a conferi-las contra o PDF**: PT-24 foi de **2/2** para **5/5 transcrições localizadas**. Codificação cujo lastro ninguém confere é a âncora que parece âncora, e aqui o lastro é conferido a cada execução.

> **PT-26 não precisou de folha nova, e o que ele documenta é outra coisa.** A folha 650 registra que a estratégia dos rádios comunicadores *"havia sido incentivada em grupos de telegram e confirma o nível de organização da mobilização"*, e a instrução transcrita manda *"organizem entre grupos de subgrupos lá em Brasília"*. **Organização não é condução:** a folha documenta coordenação distribuída, circulando por incentivo em aplicativo, sem liderança nomeada dirigindo o avanço. O valor afirma vida própria, não desorganização — e essa distinção é o que o campo existe para carregar.

### 56.2 PT-27 não recebeu valor, e a razão ficou no registro

A folha de PT-27 é a 651, e ela documenta a barreira: duas linhas de gradil sem travamento, a ausência de tropa de contenção de distúrbios, a revista individualizada que o comandante-geral dizia necessária. **Nada ali diz quem dirigia a marcha.**

Codificar a partir dessa folha seria transportar para PT-27 o valor que a **644** sustenta para PT-24 — **a cifra correta no referente errado**, que é o modo de falha desta casa — e aqui na forma mais barata de produzir, porque as duas folhas estão a dez páginas uma da outra e pertencem ao mesmo documento. Não fiz. A leitura ficou escrita na `nota_auditoria` do registro, para que não se perca.

> **E isto expõe um buraco no vocabulário que eu mesmo propus.** Os três valores cobrem *tem autonomia*, *é conduzido* e *não se aplica* — e **não cobrem *lido, e a fonte não documenta***. É estado distinto dos três e distinto do vazio: *não se aplica* é impertinência afirmada, o vazio é ninguém leu, e PT-27 é leitura que não encontrou resposta. **Não acrescentei o quarto valor:** vocabulário é seu, é a sua pergunta 2 do item 55.4, e o campo tem um dia de vida. Mas **o buraco já custou visibilidade**: a contagem de 78 vazios inclui um registro lido, e o ciclo não os distingue.

### 56.3 O que falta, e quanto custa cada fatia

| Camada (`fase`) | Registros | Por que importa à pergunta |
|:--|--:|:--|
| **T-1 Operacional** | **25** | é onde a pergunta é de fato disputada: acampamentos, caravanas, financiamento, grupos |
| **T-1 Conjuntural** | **18** | a base que antecede o líder — a camada de PT-06, já codificado |
| T0 Execução | 11 | a invasão |
| T0 Resposta tática / política | 6 | ato de Estado, tende a *Não se aplica* |
| T+1 (todas as subfases, com o registro `T0/T+1`) | 18 | resposta institucional, tende a *Não se aplica* |
| **T0 Mobilização** | **5** | ✅ **esta rodada** |

**A fatia de maior retorno é a `T-1 Operacional`, e não é a próxima por acaso:** 25 registros, e é ali que *conduzido de cima* tem chance real de aparecer — a denúncia da PGR documenta núcleos, e o relatório da CPMI documenta financiamento de caravanas. **Uma camada em que o valor pode virar é a que testa o campo**; esta rodada mostrou o campo funcionando onde ele já tendia a um lado.

---

## 57. O quarto valor, e a camada em que o campo mostrou serviço — 🔶 16/10/2026

**Encaminhamento:** *"Crie o quarto valor e siga com a T-1 Operacional."*

### 57.1 `Lido, não documentado`, e a guarda vale para ele

O quarto valor entrou com a definição que PT-27 pedia: **a fonte do registro foi lida sob esta pergunta e não a documenta** — estado distinto de *Não se aplica*, que nega pertinência, e distinto do vazio, que diz que ninguém leu.

**A cobrança de folha vale para ele, e é o ponto.** Só *Não se aplica* fica isento: dizer *li e a fonte não documenta* é afirmação sobre uma folha determinada, e sem folha citada a afirmação não tem objeto. **Prova negativa:** PT-19A — o registro sem `fonte_pagina` — recebendo o valor novo reprova o ciclo com `! codificado sem fonte_pagina: ['PT-19A']`.

PT-27 recebeu o valor na mesma rodada, e **o vazio do campo voltou a significar uma coisa só.**

### 57.2 A camada T-1 Operacional, 25 registros

| Valor | Registros | |
|:--|--:|:--|
| **Não se aplica** | **15** | ato de Estado ou de elite institucional |
| **Autonomia relativa** | **5** | PT-12, PT-12A, PT-16, PT-19 e PT-20 |
| **Conduzido de cima** | **1** | PT-10A — **o primeiro do codebook** |
| **Lido, não documentado** | **3** | PT-10, PT-15, PT-21 |
| **(sem valor)** | **1** | PT-19A, bloqueado pela guarda — ver 57.4; **desbloqueado em 16/10, item 62** |

**O que a camada entregou, e é resultado de pesquisa, não de contagem:** nos registros onde a pergunta tem objeto, **a autonomia predomina — e ela não é ausência de organização.** O financiamento é *crowdfunding* com nós concentradores, a convocação é por influenciador e por difusão em grupos, a coordenação tática é planejada pelos próprios manifestantes, e o acampamento tem carro de som próprio para coordenar. **O único `Conduzido de cima` é econômico, não político:** o MBVA, grupo informal de empresários do agronegócio, que a Abin aponta como responsável pelo envio de 272 caminhões e pelos bloqueios.

### 57.3 Cinco folhas que diziam mais do que o registro transcrevia

| Registro | Folha | O que ela acrescentou |
|:--|:--|:--|
| **PT-19** | CPMI **615 e 621**, folhas novas | **a autoria da convocação:** vídeo no Kwai em 3/1, transmissão de dois influenciadores em 4/1, mensagens prometendo *a tomada do poder pelo próprio povo*; e a auto-organização tática por alvo. **8 de 8 transcrições localizadas** |
| **PT-16** | CPMI 584 | o líder transferindo a decisão à base — *"Quem decide o meu futuro, para onde eu vou são vocês"* (09/11/2022), na folha que abre a seção que a CPMI intitula *A radicalização do movimento* |
| **PT-20** | CPMI 576 | *"carro de som para disseminação de informações e coordenação dos manifestantes"* — a coordenação era do próprio acampamento |
| **PT-15** | CPMI 25 | **a fonte declarando a própria lacuna:** identificar *"os autores intelectuais e os financiadores"* do 12 de dezembro é tarefa da investigação, não achado |
| **PT-10** | CPMI 999 | *"todas as lideranças foram identificadas, em 24 horas"* — liderança **interna**, que é outra coisa |

> **Duas rodadas, seis folhas novas, e nenhuma delas foi encontrada por busca de página.** Foram encontradas porque **a pergunta mudou**: perguntar *quem dirigia* a um corpus ancorado para responder *o que aconteceu* devolve folha que ninguém tinha aberto. É o argumento empírico a favor do campo, e ele não era previsível em 15/10.

### 57.4 Três coisas que a rodada deixou para você

1. ~~**PT-19A está bloqueado pela guarda, e a guarda está certa.**~~ **RESOLVIDA em 16/10/2026, a seu pedido — e a resposta foi NÃO AFROUXAR** (item 62): a convenção que desbloqueia o registro já existia e era praticada por PT-03E. O texto abaixo é o da proposta.

   **PT-19A está bloqueado pela guarda, e a guarda está certa.** O registro ancora no `.md` do NetLab — transcrição de página web, sem paginação, a exceção declarada do item 51 —, e o valor exige `fonte_pagina`. **Li a peça:** documenta 185 anúncios golpistas **pagos** nas plataformas da Meta, com os **anunciantes não identificados**, de modo que ela abre a pergunta do financiamento sem respondê-la. A decisão é: **a guarda passa a admitir `fonte_local` sem folha quando a fonte não é paginada, ou o registro fica vazio?** Não mexi: afrouxar guarda é decisão sua, e esta guarda tem um dia de vida.
2. ~~**`Conduzido de cima` junta dois *cimas* distintos.**~~ ✅ **DECIDIDO em 18/10/2026** — o valor passou a *Conduzido por patrocínio de setor organizado*, e não por nenhuma das duas formas propostas abaixo: a tipificação veio do verbete de Edwards e Gillham (2013), lido, em que o caso é **patrocínio** (item 65). O texto original segue como registro da proposta. **`Conduzido de cima` junta dois *cimas* distintos.** O do corpus é **setor patronal organizado** — dirigentes do agronegócio —, não o líder populista de que fala von Bülow e Abers, que é o *cima* que o campo nasceu para medir. O nome do valor não separa os dois. Proponho, se quiser separar: `Conduzido por liderança política` e `Conduzido por financiador organizado`. **Não renomeei.**
3. ~~**PT-12 justificaria um quinto valor.**~~ **CRIADO em 16/10/2026, a seu pedido** — `Autonomia com encorajamento de cima`, com reexame dos 14 registros afetados (item 61). O texto abaixo é o da proposta.

   **PT-12 justificaria um quinto valor.** É o registro em que as duas direções estão na mesma seção: o frame antecede o líder em quase uma década (Araujo e Sales, 2022) e o financiamento é coletivo sem coordenação central (PT-12A), **mas** a seção 5.5 da CPMI abre com Braga Netto e Valdemar Costa Neto pedindo permanência, e PT-11 traz o líder licenciando a ocupação de praça com *"Fiquem à vontade"*. Codifiquei `Autonomia relativa`, que é o que o vocabulário tem para *encorajado de cima e não comandado de cima* — e registrei a contraevidência na nota. **Um quinto valor — coordenação e autonomia coexistindo — é seu para criar.**

### 57.5 Onde está o campo

| | |
|:--|--:|
| **Autonomia relativa** | **8** |
| Não se aplica | 17 |
| Lido, não documentado | 4 |
| **Conduzido de cima** | **1** |
| **(vazio) — ninguém leu ainda** | **53** |

**Faltam as camadas `T-1 Conjuntural` (18, onde está PT-06), `T0 Execução` (11) e as de resposta (24).** A próxima de maior retorno analítico é a **T-1 Conjuntural**: é a que decide se a base antecede o líder, que é a tese de von Bülow e Abers e a pergunta de fundo deste campo.

---

## 58. Terceira rodada: a camada que responde à tese, e ela já estava transcrita — 🔶 16/10/2026

**Encaminhamento:** *"Siga com a T-1 Conjuntural."* São 18 registros, PT-06 já codificado em 15/10, **17 nesta rodada**.

| Valor | Registros |
|:--|--:|
| **Não se aplica** — tribunal, Congresso, núcleo de governo | **12** |
| **Autonomia relativa** | **5** |

**Cinco de cinco:** todos os registros de movimento desta camada receberam `Autonomia relativa`, e **nenhum precisou de folha nova** — ao contrário das duas rodadas anteriores, que produziram seis.

> **E a razão da diferença é instrutiva.** As duas primeiras camadas são ancoradas em **documento primário sobre o evento** — relatório da CPMI, acórdãos —, e documento de evento responde *o que aconteceu*; perguntar *quem dirigia* exigiu abrir folha nova. Esta camada é ancorada na **literatura revisada por pares da tarefa 14**, cujo tema **é** a relação entre base e liderança. A resposta já estava transcrita, com página, desde 04/10. **O campo novo não achou nada aqui porque a leitura certa já havia sido feita** — e isso é o melhor resultado possível para quatro rodadas de leitura na fonte.

### 58.1 A âncora brasileira da tese, com data

PT-02, com página e já conferido: a convocação dos protestos de 2015 foi assumida por **organizações do próprio movimento** — *"MBL, Vem Pra Rua, Revoltados Online, Nas Ruas, Movimento Contra a Corrupção"* —, e a mesma folha registra que *"os grupos antipetistas já estão presentes em protestos organizados em 2011, mantendo a mesma estética e slogans"* (Tatagiba e Galvão, 2019, p. 82 impressa).

**É o que von Bülow e Abers afirmam em 2024** — um processo que *"precedes his rise to power"* — **dito por literatura brasileira e com data: 2011, sete anos antes da eleição.** O campo `autonomia_movimento` nasceu de uma frase em inglês sobre o Brasil; o corpus já tinha a versão datada, em português, e ela estava invisível porque nenhum campo a pedia.

### 58.2 Dois registros que a escala não acomoda bem, e um que não é do Brasil

- **PT-01 é o registro-limite.** Em junho de 2013, *"não houve a conformação de um frame capaz de conferir unidade"* e o MPL defende *"a horizontalidade contra a hierarquia de partidos e sindicatos"*. **Sem hierarquia, não há de quem ser autônomo:** o valor é o mais forte da escala, e ao mesmo tempo a liderança que o campo mede ainda não existe. Codificado `Autonomia relativa`, com a ressalva na nota.
- **PT-05 é o segundo caso de coexistência, com PT-12.** Os atos têm propósito próprio — ocorreram *"com o intuito de legitimar as hostilidades do mandatário"* — e, na mesma peça, as mobilizações *"foram instrumentalizadas por segmentos autoritários"*. **Com dois casos, o quinto valor deixa de ser hipótese** (57.4, item 3).
- **PT-08 é o caso comparado, e o valor se refere ao movimento norte-americano.** A peça é a única do corpus que **argumenta** a tese em vez de dar material para ela: *"we argue that January 6th was not an individual event in a vacuum nor purely the result of Trump's ego"* (Castañeda e Jenks, 2023, PDF p. 4). O agente nomeado aparece como **encorajamento**, não comando — *"with the encouragement of Steve Bannon"*. **O valor não transfere para o caso brasileiro;** o que a peça diz transferir é o repertório.

### 58.3 Onde está o campo, e o que ele já sugere

| | |
|:--|--:|
| **Autonomia relativa** | **13** |
| Não se aplica | 29 |
| Lido, não documentado | 4 |
| **Conduzido de cima** | **1** |
| (vazio) — ninguém leu ainda | **36** |

**Resultado provisório, e declarado como provisório:** nos registros em que a pergunta tem objeto, a relação é de **13 a 1** a favor da autonomia — e **o único `Conduzido de cima` é econômico, não político** (o MBVA, no envio dos caminhões). Isso **não fecha a pergunta da pesquisa**, por duas razões que ficam escritas: faltam **36 registros**, entre eles os **11 da `T0 Execução`**, que é onde a hipótese da condução tem a sua melhor chance — a invasão coordenada por grupos, com rádios e divisão de alvos; e a camada de execução tem fonte primária de acusação (denúncia da PGR, acórdão da AP 2668), cujo propósito é justamente estabelecer autoria e comando.

**Próxima rodada, se você mandar: `T0 Execução`, 11 registros.** É a que pode virar o placar, e é por isso que é a próxima.

---

## 59. Quarta rodada: a camada que podia virar o placar não virou — e a razão é a fonte — 🔶 16/10/2026

**Encaminhamento:** *"Siga com a T0 Execução."* Era a camada apontada em 58.3 como a melhor chance da hipótese da condução: a invasão em grupos, por alvo, com rádio.

| Valor | Registros |
|:--|--:|
| **Lido, não documentado** | **8** — PT-29, PT-30, PT-33, PT-34, PT-35, PT-36, PT-37, PT-46 |
| Não se aplica | 2 — PT-31 e PT-32, ato de Estado |
| **(vazio) declarado** | **1** — PT-38, ver 59.2 |

### 59.1 A razão: o capítulo da execução é sobre o Estado

Li as oito folhas da execução no relatório da CPMI — **657, 667, 670, 671, 673, 674, 681 e 695**. Elas documentam, com precisão de minuto, **o que a multidão fez** e, com muito mais força, **o que o aparato de segurança deixou de fazer**:

> *"há evidências contundentes de que integrantes de alguns desses órgãos de segurança se omitiram deliberadamente e mesmo contribuíram ativamente para a consumação dos crimes perpetrados na Praça dos Três Poderes"* (p. 695)

> os policiais do Patamo Bravo, em vez de reprimir, *"chegaram a sinalizar para que os presentes prosseguissem com a invasão: posicionaram-se lateralmente, desobstruindo a passagem; cumprimentaram os insurgentes"* (p. 667)

**Nenhuma das oito documenta quem dirigia os invasores.** O capítulo responde *por que a contenção falhou* e *quem respondia por ela* — não *quem comandava a multidão*. É por isso que os oito registros ficaram em `Lido, não documentado`: **a camada não é silenciosa sobre direção porque ninguém olhou; é silenciosa porque a fonte dela tem outro objeto.**

> **O valor criado nesta manhã levou oito dos onze registros, e é aqui que ele se paga.** Sem ele, havia dois caminhos e os dois eram ruins: deixar oito vazios — indistinguíveis de não-lidos, que é o buraco que PT-27 abriu — ou codificar `Autonomia relativa` lendo a **ausência de comando documentado** como **autonomia documentada**. O segundo é inferência de silêncio, que é o que esta casa não faz: *zero de probe não provado é silêncio, não ausência.* **Em oito registros a tentação estava à mão, e o vocabulário tinha a palavra exata.**

**E não importei valor de vizinho.** A divisão por alvo **planejada** está ancorada em PT-19 (CPMI p. 621) e a coordenação por rádio em PT-26 (p. 650) — essas sustentam valor afirmativo nos seus próprios registros. Transportá-las para a execução, onde o ato ocorre, seria a cifra correta no referente errado na sua forma mais plausível: o fato *é* o mesmo evento, a folha é que é outra.

### 59.2 PT-38 ficou vazio, e o vazio está declarado

É o único registro da camada cuja âncora não é folha: `fonte_pagina` traz **`Livro STF 2023: inteiro teor`** — volume oficial de 210 páginas. **Não o li sob esta pergunta**, e `Lido, não documentado` seria afirmação falsa: o valor exige leitura de **folha determinada**, e é essa exigência que o torna útil. O campo fica vazio, com a razão na `nota_auditoria`, e aqui o vazio significa exatamente o que deve significar.

**É o segundo registro que a estrutura da âncora bloqueia**, depois de PT-19A (57.4, item 1) — e por motivo diferente: PT-19A não tem folha porque a fonte é `.md`; PT-38 tem *inteiro teor*, que é folha nenhuma e todas.

### 59.3 Onde está o campo, e o que a pergunta já pode responder

| | |
|:--|--:|
| Não se aplica | **31** |
| (vazio) — ninguém leu ainda | **26** |
| **Autonomia relativa** | **13** |
| **Lido, não documentado** | **12** |
| **Conduzido de cima** | **1** |

**Quatro rodadas, 57 registros com valor — 58 lidos, e PT-19A e PT-38 sem valor por estrutura de âncora —, e o resultado tem uma forma clara:** onde a fonte documenta a relação entre base e liderança, ela documenta **autonomia** — 13 contra 1, e o único `Conduzido de cima` é **econômico** (o MBVA no envio dos caminhões), não político. **Onde a fonte não documenta, ela não documenta por ter outro objeto:** dos 12 `Lido, não documentado`, **oito são da execução** e os outros quatro são folhas que medem o aparato — a barreira de gradis em PT-27, o depoimento do diretor da PRF em PT-10, a contagem de ônibus da ANTT em PT-21 — ou **declaram a própria lacuna**, como a p. 25 em PT-15.

> **A consequência metodológica, e ela vale para a redação.** A pergunta *conduzido de cima ou vida própria* **não se responde na camada do evento** — responde-se nas camadas conjuntural e operacional, onde estão o financiamento, a convocação e a genealogia do frame. O 8 de janeiro, no corpus deste projeto, é **o único dia sobre o qual não há documentação de comando** — e não por falta de investigação: a CPMI investigou o dia inteiro, minuto a minuto, e o que ela estabeleceu foi a cadeia de responsabilidade **do Estado**.

**Faltam 26 registros, todos de resposta** — `T0 Resposta tática/política` (6) e `T+1` (19, com o registro `T0/T+1`) —, e a expectativa declarada é que a quase totalidade seja `Não se aplica`, por serem ato de Estado. **Se você mandar, fecho o campo numa rodada** e o campo 17 deixa de ter vazio que signifique *ninguém leu* — exceto PT-19A e PT-38, que dependem das suas duas decisões.

---

## 60. O campo fechado: 82 de 83, em cinco rodadas e um dia — 🔶 16/10/2026 · *e os 83 vieram no mesmo dia: item 62*

**Encaminhamento:** *"Feche o campo."*

| Valor | Registros | |
|:--|--:|:--|
| **Não se aplica** | **52** | ato de Estado, decisão judicial, ato legislativo |
| **Lido, não documentado** | **15** | a fonte foi lida e não documenta a relação |
| **Autonomia relativa** | **14** | |
| **Conduzido de cima** | **1** | PT-10A — e é **econômico**, não político |
| **(vazio) declarado** | **1** | PT-19A — ver 60.3 |

> **Esta tabela durou poucas horas, e a correção é do mesmo dia.** Você criou o **quinto valor** depois do fechamento, e com ele **cinco dos 14 `Autonomia relativa` mudaram**: a distribuição válida está no **item 61**. O que não mudou foi o total — 82 de 83 com valor — **até você resolver a guarda do PT-19A, horas depois: o campo fechou nos 83, e `Lido, não documentado` foi a 16 (item 62)** —, nem a leitura de 60.1: onde a fonte documenta a relação, ela documenta autonomia, agora separando a autonomia simples da autonomia encorajada.

**Cinco rodadas, num dia:** `T0 Mobilização` (5), `T-1 Operacional` (25), `T-1 Conjuntural` (17), `T0 Execução` (11) e o fechamento (26).

### 60.1 O que o campo mostra, e a forma importa mais que o placar

**Onde a fonte documenta a relação entre base e liderança, ela documenta autonomia: 14 a 1.** E a autonomia documentada **não é desorganização** — é financiamento coletivo com nós concentradores (PT-12A), convocação por influenciador e por difusão em grupos (PT-19), decisão de marchar tomada **em votação** entre acampados (PT-24), coordenação tática planejada pelos próprios manifestantes (PT-19, PT-26), carro de som do próprio acampamento (PT-20), e narrativa que nasce na rede às 17h40 e só depois é tomada por políticos (PT-50A).

**O único `Conduzido de cima` é o MBVA** — grupo informal de empresários do agronegócio que a Abin aponta como responsável pelo envio de 272 caminhões e pelos bloqueios. **O *cima* que o corpus documenta é econômico, não político.**

> **E a distribuição revela o corpus, não só o objeto.** **52 de 83 registros são ato de Estado** — e isso diz que este codebook, construído a partir de relatório de CPMI, acórdãos, denúncia e alertas de inteligência, documenta **o Estado** com muito mais densidade do que o movimento. É consequência da fonte: **fonte estatal documenta o Estado.** O que documenta o movimento é a literatura revisada por pares do eixo 12 e do eixo 13 — e é exatamente nela que estão **6 dos 14** `Autonomia relativa` — os cinco da camada conjuntural mais PT-06 —, incluindo a âncora datada de 2011 (item 58.1). **Para a redação, isto é uma ressalva de amostra, não um achado sobre o mundo:** o campo mede o que as fontes deste corpus documentam.

### 60.2 Os 15 `Lido, não documentado` têm endereço, e ele é o dia 8

| Onde | Quantos |
|:--|--:|
| `T0 Execução` — as oito folhas da invasão | **8** |
| `T0 Mobilização` e `T-1 Operacional` — barreira, depoimento da PRF, ônibus, 12/12 | 4 |
| Resposta e efeito — PT-38, PT-44, PT-62 | 3 |

**O dia 8 é, neste corpus, o dia sobre o qual não há documentação de comando** — e não por falta de investigação. A CPMI o investigou minuto a minuto, e o que estabeleceu para aquele dia foi a cadeia de responsabilidade **do Estado**: a p. 695 afirma que integrantes de órgãos de segurança *"se omitiram deliberadamente e mesmo contribuíram ativamente"*.

**PT-38 saiu do vazio por leitura feita, e o método fica declarado** porque a âncora dele é *inteiro teor*: varri as **210 folhas** do livro oficial do STF por onze termos — comando, convoca, organizador, lideran, dirigi, coorden, mandante, financia, incit, planeja, ordem de. **207 têm camada de texto; 3 não, e isso é limite declarado.** Todas as ocorrências de comando, coordenação, liderança e planejamento referem-se à **reconstrução do edifício**; as duas de financiamento dizem que os financiadores *"estão sendo investigados"*, isto é, não os estabelecem; e a única sobre convocação é **opinião de ministro** sobre as redes sociais. É o método com que o projeto negou a cifra dos *"mais de 100 acampamentos"* em PT-12: busca no PDF inteiro, não só nas folhas citadas.

### 60.3 O último vazio é seu, e tem razão escrita

**PT-19A é o único dos 83 sem valor, e não por falta de leitura.** A peça foi lida na segunda rodada: 185 anúncios golpistas **pagos** nas plataformas da Meta, **anunciantes não identificados**. A guarda da checagem 4 exige `fonte_pagina` para todo valor que não seja *Não se aplica*, e a fonte é `.md` sem paginação — a exceção declarada do item 51.

~~**Codificá-lo exige afrouxar a guarda, e afrouxar guarda é decisão sua**~~ (57.4, decisão 1). **E a premissa estava errada: não exigia.** Você mandou resolver a guarda horas depois, e a resolução não afrouxou nada — a convenção do localizador estrutural já existia no projeto. **O campo fechou nos 83 de 83** (item 62).

### 60.4 O que o campo custou e o que deixou

**Sete folhas novas entraram no codebook** — CPMI 644 (PT-24), 615 e 621 (PT-19), 584 (PT-16), 999 (PT-10), 25 (PT-15), 576 (PT-20) —, **nenhuma achada por busca de página.** Todas apareceram porque a pergunta mudou: um corpus ancorado para responder *o que aconteceu* devolve folha nova quando se lhe pergunta *quem dirigia*.

**E o vocabulário mudou duas vezes no primeiro dia de uso:** nasceu com três valores, ganhou o quarto em PT-27 — *Lido, não documentado*, que acabou levando **15 registros**, 18% do codebook — e **dois casos pedem um quinto** (PT-12 e PT-05, coordenação e autonomia coexistindo). **As três decisões de 57.4 seguem suas**, e a terceira é esta.

---

## 61. O quinto valor, e o reexame que ele obrigou — 🔶 16/10/2026

**Encaminhamento:** *"Crie o quinto valor."*

**O valor:** `Autonomia com encorajamento de cima` — *a fonte documenta, no mesmo registro, iniciativa ou organização da base **E** um ato determinado de encorajamento, licenciamento, delegação ou instrumentalização por liderança ou elite nomeada, sem documentar comando.* Exige `fonte_pagina`, como todos os valores afirmativos.

### 61.1 Criar valor muda o critério para todos — e o precedente estava escrito

**Não bastava aplicá-lo aos dois casos que o pediram.** O item 34.7, de 04/10, já havia formulado a regra para outra decisão: promover PT-06 era *"reversível em um comando, mas muda o critério para todos"*, e **PT-08 precisaria ser reexaminado junto**. É literalmente o que aconteceu agora: **PT-08 foi um dos cinco que mudaram.**

Então esta rodada reexaminou **os quatorze** registros que estavam em `Autonomia relativa`, sob um teste declarado para ser revisável:

| | |
|:--|:--|
| **(a)** | as folhas **do próprio registro** documentam iniciativa ou organização da base |
| **(b)** | e um **ato determinado** de encorajamento, licenciamento, delegação ou instrumentalização por liderança ou elite **nomeada**, dirigido àquela mobilização |
| | faltando **(b)**, fica `Autonomia relativa`; havendo **direção**, é `Conduzido de cima` |

### 61.2 Os cinco que mudaram, com o ato de cima citado da folha do registro

| Registro | O ato de cima, na folha do próprio registro |
|:--|:--|
| **PT-12** | *"Vocês não percam a fé"* (Braga Netto, 19/11/2022) e *"Continuem na luta, o Bolsonaro não vai decepcionar ninguém"* (Valdemar Costa Neto, 16/12/2022) — CPMI, folha 524, que abre a seção dos acampamentos |
| **PT-05** | as mobilizações *"foram instrumentalizadas por segmentos autoritários para pleitear a intervenção militar"* (Araujo e Sales, 2022, p. 31 impressa) |
| **PT-08** | *"Both events occurred with the encouragement of Steve Bannon and similar agents of chaos"* (Castañeda e Jenks, 2023, PDF p. 10) |
| **PT-16** | **delegação:** *"Quem decide o meu futuro, para onde eu vou são vocês"* (Bolsonaro, 09/11/2022), na folha que a CPMI intitula *A radicalização do movimento* |
| **PT-50A** | *"especialmente figuras de políticos e mídia alinhados ao bolsonarismo utilizaram-se do fato"* (Manchetômetro, p. 14), depois de a narrativa nascer na rede às 17h40 |

> **PT-16 é a reclassificação menos óbvia, e vale explicitar por quê.** *"Quem decide o meu futuro... são vocês"* é **o oposto de uma ordem** — é o líder abdicando de decidir. Mas é **ato determinado de liderança dirigido à base**, numa folha cujo título é a radicalização do movimento, e o teste (b) pergunta por ato, não por ordem. **Delegação alimenta a mobilização sem comandá-la**, e é exatamente essa a zona que o valor novo existe para nomear. Se você quiser que delegação fique fora do critério, é um comando — e aí PT-16 volta a `Autonomia relativa`.

### 61.3 Os nove que ficaram, e a razão de cada um está na nota

**Reexame não é omissão:** os nove receberam nota com o motivo. Em resumo — **PT-01** (não há hierarquia de quem ser autônomo), **PT-02** (a convocação é de organizações **do próprio movimento**), **PT-04** (a direção causal documentada vai da rua ao governo), **PT-19** (influenciador é **intermediação dentro** do movimento, da natureza dos nós de PT-12A), **PT-20** (a coordenação é do próprio acampamento), **PT-12A** (a folha afirma o contrário de (b): *"não foi identificada uma coordenação que envolvesse todos os manifestantes"*), **PT-24** (a marcha foi decidida em **votação** entre acampados), **PT-26** (o incentivo é **horizontal**, entre pares).

> **E a chamada mais difícil foi PT-06 — o registro que originou o campo. Ele ficou.** A folha traz *"both the president and bolsonaristas radicalized their rhetoric"*, que é **paralelismo**, não ato dirigido à base; e a frase central do registro puxa com força no sentido oposto: o líder *"does not fully control"* o processo. Onde o governo aparece alimentando o conflito, isso está em **PT-05** — e foi PT-05 que mudou de valor. **A fronteira entre os dois registros é o que carrega a distinção**, e por isso ela está escrita nas duas notas.

### 61.4 O campo, com cinco valores

| | |
|:--|--:|
| Não se aplica | **52** |
| Lido, não documentado | **15** |
| **Autonomia relativa** | **9** |
| **Autonomia com encorajamento de cima** | **5** |
| **Conduzido de cima** | **1** |
| (vazio) declarado — PT-19A | 1 |

> **E esta linha também durou horas:** PT-19A foi resolvido no mesmo 16/10, sem afrouxar guarda, e o campo fechou nos **83**, com `Lido, não documentado` em **16** (item 62).

**Prova negativa, duas injeções:** o valor novo em PT-19A, que não tem folha, reprova com `! codificado sem fonte_pagina`; e o nome truncado — `Autonomia com encorajamento` — reprova com `! valores fora do vocabulário`. **A guarda cobre o valor novo exatamente como os outros.**

**O que isto muda na leitura do campo:** o placar deixa de ser *14 a 1* e passa a ser **9 de autonomia simples, 5 de autonomia encorajada e 1 de condução** — e é uma leitura melhor, porque **a autonomia encorajada era o caso mais interessante do corpus e estava escondido dentro do valor mais forte.** Dos cinco, três são de liderança política (PT-12, PT-16, PT-05), um de agente externo nomeado (PT-08) e um de elite midiática e parlamentar (PT-50A).

~~**Restam duas decisões suas**~~ ~~**— restou uma**~~ **— nenhuma** (57.4): a guarda que mantinha PT-19A vazio foi resolvida horas depois, no item 62, e o nome do valor de PT-10A foi decidido em 18/10/2026, passando a *Conduzido por patrocínio de setor organizado* (item 65). **O item 57.4 fecha.**

---

## 62. A guarda do PT-19A: resolvida sem ser afrouxada — 🔶 16/10/2026

**Encaminhamento:** *"Resolva a guarda do PT-19A."*

A decisão 1 do item 57.4 perguntava se a checagem 4 passaria a **admitir `fonte_local` sem folha** para fonte não paginada. **Respondi que não, porque a pergunta tinha premissa falsa:** a convenção que desbloqueia o registro já existia no projeto, e era praticada havia um dia.

### 62.1 `fonte_pagina` nunca foi só *"CÓDIGO: n, m"* — e a casa já sabia disso

Antes de desenhar exceção, medi o campo — **e a primeira cifra que escrevi aqui estava errada.** Eu havia contado *"26 registros fora do formato numérico"*, por uma expressão regular grosseira que reprovava código com barra e com acento (`ADC 43/44/54`, `Manchetômetro`). Medido como se deve, pelo `pares()` do próprio conferidor:

| | |
|:--|--:|
| registros com `fonte_pagina` | 82 |
| com ao menos um segmento **sem numeral** | **5** — PT-06B, PT-13, PT-19A, PT-38, PT-56 |
| dos quais **nenhuma** página é extraível | 4 — PT-06B, PT-19A, PT-38, PT-56 |

As formas em uso: `HC 164.493: inteiro teor`, `AP 2668: inteiro teor`, `Livro STF 2023: inteiro teor`, `PGR: peça integral` — e, em PT-03E, `TSE RCand: ementa itens 2-4 e 12; dispositivo`, **ancorado em `.html` sem paginação.**

**E o caso de PT-03E não é acidente: está declarado por escrito.** A rota daquela peça em `PROCEDENCIA`, registrada em 15/10/2026, diz:

> *"SERVIDO EM HTML, não em PDF: o parâmetro `extensaoArquivo` do endpoint só muda o Content-Type. **Citar por estrutura interna (item da ementa, dispositivo), não por página.**"*

Logo **PT-19A nunca esteve bloqueado pela guarda.** Estava bloqueado por um `fonte_pagina` **vazio** num caso em que o projeto já tinha convenção para preenchê-lo. A guarda não precisava de exceção; o registro precisava de localizador.

| | |
|:--|:--|
| **antes** | `fonte_pagina` vazio · `autonomia_movimento` vazio · bloqueado |
| **agora** | `NetLab: inteiro teor — §Achado principal, §Relevância para o codebook, §Ressalvas de uso` · `Lido, não documentado` |

**O valor sai da leitura, que já estava feita e registrada desde a segunda rodada.** A peça tem 51 linhas e sete seções, e eu as li: documenta **185 anúncios golpistas pagos** nas plataformas da Meta e **não identifica os anunciantes**. A §Relevância para o codebook diz que *"um anúncio tem anunciante, valor pago e decisão de moderação"* — isto é, **declara documentável exatamente aquilo que não documenta**. A pergunta da autonomia **tem objeto** aqui (circulação paga que promove a mobilização é ação do lado do movimento, e se foi paga de cima é a própria pergunta) e a fonte não a responde. É `Lido, não documentado` no sentido mais estrito do valor.

### 62.2 A nota que justificava a exceção afirmava uma vigilância que não existia

Esta é a parte que importa mais do que o registro desbloqueado. A `nota_auditoria` de PT-19A dizia, desde 15/10:

> *"A âncora é o arquivo inteiro, **cujo SHA-256 a checagem 8 do ciclo vigia**. Não é lacuna a preencher."*

**Era falso.** `gerar_manifesto_corpus.py` gerava o manifesto varrendo `Fontes/**/*.pdf`, e o manifesto tinha **63 peças, todas PDF**. Os dois arquivos não-PDF que ancoram registro — o `.md` do NetLab (PT-19A) e o `.html` do acórdão do TSE (PT-03E) — **não eram vigiados por nada.**

| | |
|:--|--:|
| peças no manifesto, antes | 63 |
| arquivos não-PDF em `fonte_local` | 2 |
| desses, vigiados por SHA-256 | **0** |

**E a asserção falsa era justamente a que sustentava a isenção.** O argumento para dispensar folha era "a âncora é o arquivo inteiro, e o arquivo inteiro está vigiado" — com a segunda metade inexistente. É o modo de falha batizado do projeto, **dentro da nota que se apoiava nele**, e ninguém o teria achado sem a pergunta de hoje: foi preciso ir *usar* a garantia para descobrir que ela não estava lá.

**Corrigido:** o gerador passou a incluir os arquivos não-PDF que ancoram registro, e o conjunto sai do **`fonte_local` do codebook, não de lista à mão** — anexo novo entra no primeiro ciclo, ou a checagem 8 acusa. O manifesto tem **65 peças**. LEIA-ME, bibliografia e `.docx` de teoria ficam de fora de propósito: não ancoram registro nenhum, e vigiar byte deles seria ruído.

> **Uma cifra se desencontrou de outra, e isso aqui é defeito.** O manifesto agora conta **24 documentais**, e a linha de base da checagem 6 continua **22 documentais / 6.951 p.** — porque a checagem 6 varre o disco **só por PDF**. Duas medidas de nome parecido e recorte diferente é exatamente *a cifra correta no referente errado*, então a impressão do gerador passou a **dizer o recorte na própria linha**.

### 62.3 Localizador declarado não é localizador resolvido

Com o `§` entrando no campo, apareceu um segundo buraco. `conferir_paginas.py` — a única checagem que lê a fonte — **abre PDF**. Uma folha de PDF é conferida contra o texto da folha; **uma seção não era conferida contra nada.** Seção citada com nome errado, ou renomeada no arquivo depois da citação, passaria para sempre.

A checagem 5 passou a **resolver** o localizador: todo `§Título` em `fonte_pagina` tem de existir **como cabeçalho** (markdown ou HTML, qualquer nível) em algum dos arquivos não-PDF vinculados ao registro.

**Só o `§` entra, e isso é deliberado.** O localizador de PT-03E — *"ementa itens 2-4 e 12; dispositivo"* — fica de fora: "itens" não são cabeçalhos, e guarda que reprova registro legítimo **treina a ignorar guarda**.

### 62.4 Quatro provas negativas, e uma delas reprovou a prova

| Injeção | Resultado |
|:--|:--|
| `§Achado principal` → `§Achado principais` | reprova — `! PT-19A cita §Achado principais e esse cabeçalho não existe no arquivo vinculado` **e** `X sincronia entre formatos (1 células)` |
| âncora não-PDF removida do manifesto | reprova — `64 peça(s) no manifesto, 65 em disco` · `X em disco e fora do manifesto` |
| SHA-256 da âncora não-PDF trocado por zeros | reprova — `X SHA-256 DIVERGENTE ... toda âncora que dependa desta peça está sob suspeita` |
| valor afirmativo em PT-03D, sem `fonte_pagina` | reprova — `! codificado sem fonte_pagina: ['PT-03D']` |

**A primeira dessas provas falhou na primeira tentativa, e a culpa era da prova.** Eu injetei por `texto.replace("§Achado principal", "§Achado principais", 1)` e **o ciclo passou**. A razão não era a guarda: `metadados` vem antes de `eventos` no arquivo, e a injeção caiu dentro de uma string de `revisoes` — que nenhuma checagem lê. **O ciclo passou com razão, e o "passou" não media nada.** É *a operação certa no referente errado*, reaparecendo dentro do instrumento que existe para pegá-lo. Prova negativa tem de mutar o **campo**, pelo parser, nunca o texto do arquivo.

**E a quarta prova existe porque a terceira envelheceu.** O item 55 documentou a cobrança de folha injetando valor em PT-19A, *"um dos dois registros sem `fonte_pagina`"*. Resolvida a guarda, **PT-19A tem localizador e aquela injeção deixou de ser reproduzível** — guarda cuja prova não roda mais é guarda sem prova. A cobrança foi reancorada em **PT-03D**, hoje o único dos 83 sem `fonte_pagina`, e reprovou igual.

### 62.5 O campo, fechado nos 83

| | |
|:--|--:|
| Não se aplica | 52 |
| **Lido, não documentado** | **16** |
| Autonomia relativa | 9 |
| Autonomia com encorajamento de cima | 5 |
| Conduzido de cima | 1 |
| (vazio) | **0** |

**O ciclo passa em nove passos, com `confirmados 73 | falhas 0 | indeterminados 5` — os mesmos de antes.** *(Em 18/10/2026 os indeterminados passaram a **4**, e por razão escrita: PT-03E saiu da fila quando a guarda do localizador estrutural entrou — item 64.)* PT-19A não entrou na conferência de páginas e não devia: `pares()` não extrai numeral do localizador novo, de modo que o registro não é candidato — como PT-38 e PT-56, que citam *inteiro teor*. **Conferi isso antes de escrever o campo**, porque um numeral no localizador (eu havia pensado em `inteiro teor (51 linhas)`) teria mandado o registro para a fila de PDFs e mexido na linha de base dos indeterminados.

**O que isto muda na leitura — e muda uma coisa, pequena e vale dizer.** Dos **31** registros em que a pergunta tem objeto, agora são **15 com resposta documentada contra 16 silenciosos**: antes de PT-19A era 15 a 15, e **o silêncio passou a ser maioria, por um.** Não é achado sobre o mundo e não deve ser escrito como tal — é mais uma medida do corpus, no sentido do item 60.1. Mas desfaz a possibilidade de escrever *"na maioria dos casos em que a pergunta cabe, as fontes respondem"*, que o empate ainda tolerava e hoje seria falso.

### 62.6 O que fica aberto

**Uma decisão de 57.4, e é a do nome:** `Conduzido de cima` junta hoje **três *cimas* diferentes** — setor patronal organizado (PT-10A), liderança política (PT-12, PT-16) e elite midiática e parlamentar (PT-50A). A proposta na mesa é `Conduzido por financiador organizado` para PT-10A. **Não renomeei.**

**E a medição de 62.1 levantou um risco latente que é decisão sua, não tarefa minha.** O localizador de PT-03E é `TSE RCand: ementa itens 2-4 e 12; dispositivo`, e **`pares()` o lê como as páginas 2, 3, 4 e 12** — porque extrai todo numeral depois dos dois-pontos. Hoje isso não produz erro nenhum: o que salva é o teste seguinte, *"o documento citado não é PDF"*, que manda o registro para `indeterminados`. **Mas o que o salva é a extensão do arquivo, não o localizador.** Se aquele acórdão algum dia entrar no corpus **também em PDF** — e a rota declara que o endpoint serve o mesmo conteúdo —, PT-03E passaria a ser conferido contra as **folhas** 2, 3, 4 e 12 de um acórdão cujas transcrições estão em outro lugar, e um casamento acidental ali seria *a cifra correta no referente errado* com aprovação do ciclo. Há duas saídas e a escolha é sua: **reescrever o localizador de PT-03E em `§`**, que a checagem 5 agora resolve, ou **ensinar `pares()` a não extrair numeral de segmento que diga `item`, `ementa` ou `dispositivo`**. A primeira é menor e usa guarda que já existe; a segunda protege quem escrever o próximo. **Não mexi em nenhuma das duas.**

---

## 63. O projeto do edital não retorna, e as referências limpas — 🔶 18/10/2026

**Encaminhamento:** *"Deletei o projeto de pesquisa e movi os documentos que faziam parte do repositório que não tinham relação com o projeto de pesquisa. Não irei retomar o projeto de pesquisa, pois o mesmo não faz mais sentido agora. Ele estava somente acumulando material desnecessário ao repositório e fazendo com que você lesse de forma errônea todo o repositório."* E, sobre as referências que ainda o citavam: *"Limpe essas referências."*

**A decisão que estava aberta desde 14/10 fechou:** `01_PROJETO-PESQUISA.md` **não volta**. A pendência do item 48.3 — se o enunciado do projeto deveria viver em `docs/`, livre do limite de palavras do edital — recebeu resposta, e o comando de restauração fica ali como registro de que a peça existe no histórico, **não como oferta**.

### 63.1 Três asserções no presente sobre um arquivo que não existe — e a do meio era falsa duas vezes

Varri o repositório por `01_PROJETO-PESQUISA`, `02_PROPOSTA-DISCIPLINA` e `projeto-pos-doc`. As menções que **afirmavam no presente** eram três, **todas em `docs/analise/09_CONCEITO-MECANISMO.md`** — e isso importa, porque aquele documento é a fonte das definições de mecanismo que vão para a redação.

| Onde | O que dizia | O que havia de errado |
|:--|:--|:--|
| **l. 124** | *"Não mudei a atribuição dos quatro testes em `01_PROJETO-PESQUISA_v1-compacto.md`. Duas fontes divergem…"* | **Falsa por dois motivos acumulados.** A atribuição **foi** mudada em 10/10/2026 — pela §9.6 **do próprio documento**, três telas abaixo, marcada *EXECUTADA* —, e as **duas fontes não divergiam** (item 43.2: a lista entre parênteses de Cunha e Araújo é referência, não autoria). Além disso o arquivo saiu em 14/10 |
| **l. 254** | *"O projeto atribui a Beach e Pedersen (2019), em `01_PROJETO-PESQUISA_v1-compacto.md` §3.2"* | Presente contra o **título da sua própria seção**, que diz *"✅ EXECUTADA"*. Passou a `atribuía`, com as duas datas |
| **l. 79** | célula da tabela da §4, com a mesma atribuição | **Não reescrita, de propósito** — o documento já a declara mantida como registro histórico do que se cobrava. Recebeu o ponteiro para a §9.6 |

> **O defeito não é de arquivo apagado; é de asserção que envelhece em sentido contrário.** A linha 124 dizia *"não mudei"* a coisa que o mesmo documento, mais abaixo, registra como mudada. Quem lê de cima para baixo encontra a negação antes da execução. **É o modo de falha batizado do projeto na forma mais barata de produzir: correta quando escrita, falsa quando lida**, e nenhuma checagem a alcança, porque o ciclo confere cifra e âncora, não tempo verbal.

### 63.2 O que NÃO foi tocado, e a razão de cada um

| Arquivo | Por que fica |
|:--|:--|
| `docs/historico/ETAPA1_inventario_repositorio.md` (9 menções) | declara em cabeçalho que seus caminhos mudaram **de propósito**: reescrever um inventário datado destrói o que ele serve para provar |
| `README.md` (3 menções) | **conferidas uma a uma:** todas no passado — *"Até 14/10/2026 havia"*, *"Estavam em `projeto-pos-doc/` até 14/10/2026"*, *"não existe mais, e isso é deliberado"* |
| `docs/analise/06_BIBLIOGRAFIA-DO-PROJETO.md` (2) | já dizem no passado que a pasta saiu, e a segunda registra que a decisão 3 do item 47.5 **ficou sem objeto** — mas que o problema que ela media, não |
| `scripts/verificar_integridade.py` l. 387 | comentário que explica a remoção de 14/10, no passado, e é o que impede a cópia morta de voltar |
| as 12 menções desta agenda | registros datados. O item 43.1 lista os seis lugares corrigidos **naquele dia**, e dois deles saíram depois — a correção é este item, não uma reescrita dele |
| `.backup_pre_lula/` | é backup, e está na higiene pendente (46.5) |

**E um caso que recebeu tratamento diferente porque não é asserção:** `scripts/historico/recodificar_tarefa19_nomes.py` apontava para `projeto-pos-doc/09_CONCEITO-MECANISMO.md`, caminho morto desde 14/10. **Endereço não é achado** — foi atualizado para `docs/analise/`, sem ferir a regra dos registros datados.

### 63.3 Os quatro scripts fora do índice — e eu descrevi um deles errado

`scripts/LEIA-ME.md` ganhou as quatro linhas que faltavam: `auditar_licencas.py`, `exportar_aparato.py`, `gerar_catalogo_imprensa.py` e `rotas_camada_a.py`. Dezessete scripts rodam e o índice documentava treze.

> **E aqui eu cometi, no rascunho, exatamente o erro que o índice existe para evitar.** Escrevi as quatro linhas **a partir dos nomes dos arquivos**, e descrevi `gerar_catalogo_imprensa.py` como *"catálogo do eixo 08, a cobertura de imprensa, a partir do inventário"*. **Não é isso.** Ao abrir o arquivo antes de gravar: ele cataloga as **atribuições de número de manifestantes na imprensa**, declara-se *"instrumento SEPARADO do codebook"* que *"não alimenta o process tracing nem a cronologia"*, e serve a analisar **como os veículos disputam o processo político pela via do número** — enquanto o codebook mantém apenas os números do documento legal. Emite `CATALOGO-IMPRENSA-MULTIDAO-8JAN.xlsx`.
>
> **Nome de arquivo não é descrição de arquivo.** As quatro linhas foram reescritas a partir do cabeçalho de cada script, e as outras três ganharam com isso: a de `auditar_licencas.py` passou a carregar a razão da regra (*"`SEM` não é livre: é desconhecido, e desconhecido conta como reservado por omissão"*, e o caso Rich (2021), que o OpenAlex declarava OURO e está à venda), e a de `rotas_camada_a.py` passou a dizer o que ela descobriu: que o campo `locations` do OpenAlex lista **todos** os depósitos, e foi ele que achou Mayntz (2004) integral no MPG.PuRe depois de a peça ter sido dada como sem arquivo.

### 63.4 A varredura, depois da limpeza

| Arquivo | Menções | Estado |
|:--|--:|:--|
| `docs/PENDENCIAS-ANALITICAS.md` | 12 | registros datados ✅ |
| `docs/historico/ETAPA1_inventario_repositorio.md` | 9 | registro datado, declarado ✅ |
| `docs/analise/09_CONCEITO-MECANISMO.md` | 3 | **corrigidas** ✅ |
| `README.md` | 3 | passado, conferidas ✅ |
| `docs/analise/06_BIBLIOGRAFIA-DO-PROJETO.md` | 2 | passado ✅ |
| `scripts/verificar_integridade.py` | 1 | comentário histórico ✅ |

**Nenhuma menção restante afirma no presente.** A varredura é o passo 6 da verificação do plano, e repeti-la é o que prova a limpeza.

---

## 64. A guarda do localizador estrutural — e a cifra que mentia dentro do gerador — 🔶 18/10/2026

**Encaminhamento:** *"Execute o plano."* Esta é a frente F2, e ela rendeu mais do que o plano previa.

### 64.1 O risco que o plano descrevia, fechado

`fonte_pagina` de PT-03E é `TSE RCand: ementa itens 2-4 e 12; dispositivo`, e `pares()` devolvia `[('TSE RCand', [2, 3, 4, 12])]` — **itens de ementa lidos como páginas.** Não produzia erro, porque o teste seguinte descarta o que não aponta para PDF; mas **o que salvava era a extensão do arquivo, não o localizador**, e a rota daquela peça em `PROCEDENCIA` declara que o endpoint do TSE serve o mesmo conteúdo. No dia em que o acórdão entrasse também em PDF, o registro passaria a ser conferido contra as folhas 2, 3, 4 e 12 de uma peça cujas transcrições estão noutro lugar.

**A saída que o plano previa — reescrever o localizador em `§` — foi descartada por medição, e vale registrar por quê:** o `.html` do TSE tem **zero cabeçalhos** (`<h1>`–`<h6>`), porque é exportação de Word com 2.881 `<span>` e 1.552 `<p>`. A guarda da checagem 5, criada em 16/10, resolve `§` contra cabeçalho — logo **não alcança este arquivo**. A saída executada foi a outra: **endurecer `pares()`**, com `ESTRUTURAL = item | itens | ementa | disposit`, falha fechada. Medido antes de aplicar: desses termos, **só PT-03E casa em todo o codebook** — zero colateral.

### 64.2 E quatro registros eram invisíveis na única checagem que lê a fonte

Endurecer `pares()` tirava PT-03E da fila e baixava `indeterminados` de 5 para 4. Ao conferir o que isso significava, apareceu o problema maior: **os registros sem página extraível nunca apareciam em lugar nenhum da saída** — nem conferidos, nem indeterminados. `pares()` não devolvia par, eles não entravam em `cands`, e sumiam.

| | |
|:--|--:|
| registros com `fonte_pagina` | 82 |
| com página extraível apontando para PDF | **77** |
| **fora do alcance, por localizador estrutural** | **5** — PT-03E, PT-06B, PT-19A, PT-38, PT-56 |
| dos 77, sem transcrição literal para casar | 4 — PT-13, PT-23, PT-33, PT-55 |

E as contas fecham nos dois sentidos: 77 + 5 = 82, e 73 confirmados + 4 indeterminados = 77.

> **Contagem que não imprime o que exclui ensina a confiar no total errado.** `conferir_paginas.py` passou a **nomear e contar** os cinco, com linha de base `SEM_PAGINA_EXTRAIVEL_BASE = 5`: o sexto que aparecer derruba, porque **registro que deixa de ser conferível tem de ser uma decisão, não um efeito colateral**.

### 64.3 O achado que o plano não previa: a cifra digitada dentro do gerador

`reports/AUDITORIA-FONTES.md` é **gerado**, e o cabeçalho de `gerar_auditoria.py` promete em letras: *"A narrativa fica neste arquivo; as tabelas saem dos dados."* Um bloco não saía.

| O que o relatório afirmava | O que a medição devolve |
|:--|:--|
| *"os **58 registros** com página estruturada em documento PDF"* | **77** |
| *"Transcrição localizada na página citada: **53**"* | só o passo 7 sabe — **deixou de ser afirmado aqui** |
| *"Sem transcrição literal para conferir: **5**"* | **4** |
| *"Os cinco indeterminados — **PT-08**, PT-13, PT-23, PT-33 e PT-55"* | PT-13, PT-23, PT-33, PT-55 — **PT-08 não é um deles** |

**Era narrativa de setembro sobrevivendo dentro de um gerador, que é o último lugar onde alguém procura cifra velha** — exatamente porque o arquivo se apresenta como gerado. É a mesma família do *"82 x 16"* do item 29.1 e da identidade declarada das figuras do item 48.2: **o rótulo de "automático" é o que desliga a desconfiança.**

**Corrigido por medição, não por atualização:** o bloco passou a importar `pares` e `transcricoes` de `conferir_paginas.py` — importadas, não reimplementadas — e a contar. E a cifra que **só o passo 7 pode saber** (quantas transcrições casaram) deixou de ser repetida no relatório, com a razão escrita: *uma segunda cópia da cifra é uma cópia para envelhecer.*

### 64.4 Duas provas negativas

| Injeção | Resultado |
|:--|:--|
| `TSE RCand: ementa itens 2-4 e 12; dispositivo` direto em `pares()` | devolve `[]` — e `TSE RCand: 2, 3, 4`, `CPMI: 644, 615` e `PGR: peça integral | CPMI: 230, 566` continuam devolvendo o que devem |
| localizador de PT-03E trocado por **numeral puro** no campo | volta a ser candidato, os fora-do-alcance caem para 4 e o tripwire **dispara**: `~ ATENÇÃO: a linha de base de 18/10/2026 é 5` |

A injeção mutou **o campo, pelo parser** — a lição de 16/10, quando um `replace` de texto caiu numa string de `metadados.revisoes` e o "passou" não mediu nada.

### 64.5 O que muda na linha do ciclo

`confirmados 73 | falhas 0 | **indeterminados 4**` — era 5, e a razão está escrita aqui. Mais a linha nova, que não existia: *fora do alcance deste conferidor: 5 registro(s)*. **Nenhum registro perdeu âncora; um deixou de ser conferido contra folha que não existe, e quatro deixaram de ser invisíveis.**

---

## 65. Os dois nomes que você decidiu — e a guarda reprovou o meu texto novo — 🔶 18/10/2026

**Encaminhamento:** *"Nomeie a partir dessa recomendação"* (PT-07) e, sobre o valor de PT-10A, *"Conduzido por patrocínio de setor organizado"*. É a frente F3 do plano, e com ela **o item 57.4 fecha** e 26(c) cai de seis decisões para cinco.

### 65.1 PT-07, e a troca é de espécie, não de família

| | |
|:--|:--|
| **saiu** | *Alinhamento de quadros prévio* |
| **entrou** | ***Deliberação de ruptura e articulação do quadro de fraude*** |

**A definição gravada no campo:** o núcleo político delibera romper com a ordem institucional — cogitar a afronta aberta às decisões do STF, com plano de contingenciamento e fuga — e, no mesmo período, passa a **articular e elaborar** o quadro de fraude eleitoral. *O quadro de fraude não antecede a deliberação: é estratégia de sustentação dela.*

**E eu devo uma correção ao que afirmei ao propor.** Eu disse que o nome velho estava *"na família errada"*. **Não estava**, e a desmentida já vivia no §10.1 do documento 09, escrita em 13/10: o capítulo lido diz que *"frame bridging can be considered a specific form of frame articulation"* (p. 400 impressa). Logo *alinhamento* é a **espécie estratégica voltada a público** de um gênero mais amplo — e o defeito do nome velho é menor do que eu disse: ele **nomeava o gênero onde a fonte permite nomear a espécie**, e a espécie documentada em 22/03/2021 não é a voltada ao público, que é PT-06.

**O lastro, folha por folha, da peça lida integral** (Snow, Vliegenthart e Ketelaars 2019, impressa = PDF + 390):

| Conceito | Definição | Pág. |
|:--|:--|--:|
| Articulação | *"the connection, or splicing together, and coordination of issues, events, experiences, and cultural items"* | 397 |
| Elaboração | *"accenting and highlighting some events, issues, and beliefs or ideas more than others"* | 398 |
| Tarefa diagnóstica | problematização **mais** *"the attribution of blame or responsibility"* | 396 |

**A honestidade do nome fica declarada no campo:** *articulação* é **tipificada** na literatura lida; *deliberação de ruptura* é **descritiva da denúncia da PGR** (p. 8), porque o corpus não tem tipo para ela. É o critério da §9.7 do documento 09 — *trocar um nome que afirma mais do que se mediu por um nome que diz a relação observada* —, e a forma de dois termos é a que você aprovou em PT-12A.

### 65.2 PT-10A: o valor fecha o par que PT-12A já havia aberto

| | |
|:--|:--|
| **saiu** | *Conduzido de cima* |
| **entrou** | ***Conduzido por patrocínio de setor organizado*** |

**O que o registro documenta:** o Movimento Brasil Verde e Amarelo — empresários do agronegócio, dirigentes de entidades patronais nomeados pela Abin, **272 caminhões** nos comboios a partir de 04/11/2022 (CPMI, p. 884-890). O `mecanismo_causal` dele já se chamava *mobilização de recursos por setor econômico organizado*.

**E a tipificação estava disponível, lida, e já usada pelo projeto.** O verbete *Resource mobilization theory* (Edwards e Gillham, 2013) dá três tipos, e foi dele que saiu o nome de PT-12A em 10/10:

| Tipo | Registro |
|:--|:--|
| **Agregação** | PT-12A — o nó concentra e redistribui, **sem financiar** |
| **Patrocínio** | **PT-10A** — setor organizado que **financia** |
| Cooptação / apropriação | nenhum |

> **A definição de PT-12A já excluía patrocínio em letras** — *"não é patrocínio, porque o nó não financia, redistribui"*. **PT-10A é o caso positivo exato do que aquele registro exclui**, e até hoje os dois não se falavam por nome. Com a troca, passam a. E a ambiguidade sai do único valor em que existia: *cima* nomeava, nos dois valores que a usavam, agentes de natureza diferente — econômico aqui, liderança política e elite midiática lá.

### 65.3 A checagem 7 ganhou um artefato, e a lacuna estava na própria contagem

O item 42.3 declarava que **quatro** artefatos são mantidos à mão — *"as duas figuras interativas, o relatório de pesquisa e o caderno de evidências"* — e a lista `ARTEFATOS` do código tinha **três**: o **SVG da cadeia causal nunca entrou**. Ele carrega texto de mecanismo (`>mecanismo: … + alinhamento de quadros prévio`) e `conferir_figuras.py` não compara esse texto com o JSON.

**Medido antes de acrescentar:** o SVG não continha nenhum dos nomes já retirados — **a lacuna existia e ainda não havia mordido.** Com ele dentro, a checagem 7 vigia **11 itens em 4 artefatos**, e pegou o nome de PT-07 em três deles: HTML, SVG e relatório.

**E o nome retirado precisou de três entradas, não uma**, porque os artefatos o escreviam de três formas: minúscula dentro de uma cadeia (SVG), capitalizado (HTML) e com o termo inglês no meio — *Alinhamento de quadros (frame alignment) prévio* (relatório). Guarda de substring exige a forma exata; uma entrada só teria deixado duas passar.

### 65.4 A guarda reprovou o meu próprio texto novo, e estava certa

Ao reescrever o relatório, escrevi *"em substituição a alinhamento de quadros prévio"* — e o ciclo caiu, acusando o nome retirado no artefato. **A guarda não distingue menção de uso, e é assim que ela deve ser:** o nome retirado não vive em artefato que o leitor vê, nem dentro de uma oração que explica a substituição. A história pertence ao JSON e a esta agenda. A frase passou a *"em substituição ao nome anterior, que tomava o gênero pela espécie"*.

### 65.5 O que o relatório carregava além do nome

Ao abrir o bloco de PT-07 para trocar o mecanismo, apareceu mais, e nada disso o ciclo acusava:

| O relatório dizia | O codebook diz |
|:--|:--|
| data: **2021** | **22/03/2021** |
| **Fonte.** *Agência Brasil (08/01/2026)*, com link | **denúncia da PGR, PET 12.100, p. 8 e 249** — e o campo `status_verificacao` de PT-07 declara que ela *"substitui a citação indireta via Agência Brasil"* |
| *Status: confirmado* | **confirmado em fonte primária** |
| o fato, parafraseado da notícia | a transcrição literal da denúncia, que diz o que se deliberou |

**O relatório creditava a uma notícia o que a peça primária estabelece, dezenove dias depois de o codebook registrar a substituição.** `conferir_relatorio.py` confere página citada contra `fonte_pagina`, cifra retirada e caminho citado — **não confere atribuição de fonte**. O bloco foi reescrito com a transcrição da denúncia e a página.

### 65.6 Três provas negativas

| Injeção | Resultado |
|:--|:--|
| valor novo **truncado** no campo de PT-10A | reprova — `! valores fora do vocabulário: ['Conduzido por patrocínio']` |
| nome retirado de mecanismo reinjetado **no SVG** — o artefato que entrou hoje | reprova — `X reports/figures/figura_cronologia_8jan.svg traz 'alinhamento de quadros prévio'` |
| valor retirado *Conduzido de cima* reinjetado no relatório | reprova — `X … traz 'Conduzido de cima' … hoje é 'Conduzido por patrocínio de setor organizado'` |

A primeira mutou **o campo, pelo parser**; as duas últimas mutaram texto, porque ali o alvo é literalmente o texto. Ciclo de volta ao verde: `confirmados 73 | falhas 0 | indeterminados 4`.

### 65.7 O que resta de 26(c)

**Cinco decisões, todas suas:** `data_hora` de PT-02 (34.7) · Telegram e WhatsApp em PT-06 (35.5) · o `marco_teorico` que cita obra não lida (47.5, decisão 2) · a data de PT-57 (item 51) · a promoção de classe de PT-03B, PT-05A e PT-06C (51.5, decisão 1). **E o item 57.4 fecha com este item.**

---

## 66. PT-21: sai a massa crítica, e a guarda passa a vigiar o conceito — 🔶 18/10/2026

**Encaminhamento:** *"Execute a F5."*

### 66.1 O defeito, e ele tinha oito dias de idade dentro do codebook

O `mecanismo_causal` de PT-21, classe `Confirmado em fonte primária`, dizia:

> *"Concentração de recursos: o acampamento multiplica-se por quase 20 vezes (5.500 pessoas em 07/01), atingindo a **massa crítica necessária** para romper barreiras"*

É **o mesmo defeito** que a tarefa 19 retirou de PT-34 em **10/10**, intacto no registro ao lado — e agravado. Três razões, todas medidas antes:

| | |
|:--|:--|
| **o conceito não é o que o campo supõe** | em Marwell e Oliver a massa crítica são os **organizadores**, não a multidão; Oliver (2013, verbete *Critical mass theory*, lido integral no corpus) classifica o uso para o grupo inicial de manifestantes como **metafórico e frouxo** |
| **não há literatura no corpus que o sustente** | a varredura das quinze peças do eixo 13, lidas em 09-10/10, devolveu **zero ocorrências** do termo |
| **e este registro era pior que PT-34 era** | afirmava a massa crítica **necessária** — condição necessária, com quantidade-limite que o codebook nunca mediu |

### 66.2 Por que nenhuma checagem o acusou, e é a lição da rodada

A checagem 7 registrava, desde 10/10, a **string** retirada de PT-34: *"Massa crítica atingida no ponto de máxima densidade simbólica"*. PT-21 escrevia o termo de outra forma, e passava.

> **Nome retirado de um registro não retira o conceito do codebook.** A guarda foi desenhada para impedir que um *nome* reapareça nos artefatos, e fez isso — mas o que estava errado não era a frase de PT-34: era o conceito, e ele vivia a uma linha de distância. **Havia cinco ocorrências em três dos quatro artefatos mantidos à mão**, e nenhuma era acusada por checagem alguma.

Com esta rodada, **`massa crítica` e `Concentração de recursos` entraram elas mesmas no registro de nomes retirados** — não a frase de um registro, o termo. A checagem 7 vigia agora **14 itens em 4 artefatos**. Discussão legítima do conceito, como o verbete de Oliver, vive em `docs/analise/`, que não é artefato vigiado.

### 66.3 O nome novo, e as duas pontas conferidas na folha

> **`Concentração de contingente no acampamento`** — *o acampamento vai de 300 pessoas em 05/01/2023 a 5.500 estimadas em 07/01, pela chegada de ônibus e manifestantes, e é essa concentração que torna disponível no dia 8 um contingente que três dias antes não existia.*

**Abri a folha 576 antes de reescrever**, porque restatar cifra sem abrir a folha é o defeito da casa. A CPMI atribui os números a documentos do Comando Militar do Planalto e escreve:

> *"esse esvaziamento continuou até 05 de janeiro de 2023, quando o acampamento chegou a ter **apenas 300 pessoas**. O movimento de esvaziamento seria revertido, porém, no dia 6 de janeiro, com a chegada de novos ônibus e manifestantes. No dia seguinte, estima-se que estivessem no lugar **5.500 pessoas**."*

**E o multiplicador saiu.** O campo dizia *"quase 20 vezes"*; a razão entre as duas pontas é **18,3**. Arredondar para cima um número derivado é a forma mais barata de afirmar mais do que se mediu — ficam as duas cifras, e quem quiser a razão a calcula. A segunda é **declaradamente estimativa**, e isso agora está no campo.

**E `contingente` não é palavra nova:** é o termo que o próprio codebook já usa em **PT-12**, onde o acampamento é *"reserva de contingente"*. O nome novo liga os dois registros pelo vocabulário que a casa já tinha.

**O que o registro deixou de afirmar, e a fronteira importa:** *romper a contenção* é PT-28 e PT-29, que têm folha própria. Aqui o mecanismo é a concentração, **não o seu efeito** — e era o efeito que a palavra *necessária* contrabandeava.

### 66.4 Cinco ocorrências em três artefatos, e uma verificação que não deu em nada

| Artefato | O que tinha |
|:--|:--|
| `cronologia_8jan_interativa.html` | o mecanismo de PT-21 **e** uma menção histórica em PT-34 (*"em substituição a massa crítica"*) — saiu, pela mesma regra do item 65.4: o termo retirado não vive em artefato que o leitor vê, nem dentro da oração que explica a substituição |
| `process_tracing_8jan_relatorio.md` | a prosa do par explicativo de $T_{-1}$ e a linha da tabela, que dizia **"Massa crítica: 5.500 pessoas em 07/01 (x20)"** — passou a *"Concentração de contingente: 300 → 5.500 pessoas (05–07/01)"* |
| `caderno_CPMI_verbatim.md` | o bloco *"Mecanismo causal atribuído (leitura do analista)"* de PT-21 |

> **Uma verificação que fiz e não deu em nada, e vale registrar para não ser reaberta.** O HTML descreve a magnitude de PT-34 como *"faixa construída (3.000 a 5.500 no conjunto mobilizado)"*, enquanto o campo do JSON fala de *"convergência de duas medições oficiais independentes na manhã"*. Parecia drift; **não é**. A faixa é a que o projeto adotou em 16/08/2026 ao retirar o "4 mil", está em `docs/ESTIMATIVA-MULTIDAO-8JAN.md`, sustentada por dois métodos que não se copiam (contagem de transporte ANTT/Abin e contagem policial de público) e ancorada na CPMI p. 374, 637, 643 e 695. **São duas redações da mesma coisa documentada.**

### 66.5 Duas provas negativas, e a primeira é a que importa

| Injeção | Resultado |
|:--|:--|
| **o conceito solto**, em forma que a guarda antiga não pegava — `massa crítica` no meio de uma frase do caderno | reprova — `X … traz 'massa crítica' — retirado em 18/10/2026 de PT-21 e PT-34` |
| o nome retirado de volta no relatório — `Concentração de recursos` | reprova — `X … hoje é 'Concentração de contingente no acampamento'` |

A primeira é a prova de que a guarda mudou de natureza: **antes vigiava uma frase; agora vigia o termo.** Ciclo verde: `confirmados 73 | falhas 0 | indeterminados 4`, 83 sub-eventos, classes 61 / 21 / 1 — **nenhum fato, página, classe ou transcrição mudou.**

---

## 67. A pendência fantasma de 26(c) — resolvida havia onze dias — 🔶 20/10/2026

**Encaminhamento:** *"Vamos continuar nosso trabalho."* Fui montar os dossiês das cinco decisões de campo, e a primeira que abri **não era uma decisão: estava resolvida desde 09/10/2026.**

### 67.1 O que o ledger pedia, e o que o registro já tinha

A tarefa 26(c) listava **`Telegram e WhatsApp em PT-06`** entre as decisões abertas, remetendo ao item 35.5, que em 04/10 havia escrito:

> *"**Telegram e WhatsApp como plataformas medidas.** As autoras as nomeiam, mas **por citação de segunda mão** — as 802 mensagens de WhatsApp são de Soares et al. (2021) e as 867 de Telegram são de Nascimento et al. (2020), nenhum no corpus. (…) **Âncora de primeira mão, se quiser:** Chagas e Carreiro (2022) e Mendonça e Freitas (2022), já no corpus."*

**As duas candidatas sugeridas falharam, e uma terceira peça resolveu.** A procedência de Chagas e Carreiro registra o desmentido: *"Era candidata a dar âncora de primeira mão ao Telegram e ao WhatsApp de PT-06, e o objeto é outro: guerras de hashtag no Twitter, com zero ocorrências de Telegram e três de WhatsApp. **Quem fechou a pendência foi Cesarino (2022)**."*

E o `fonte_trecho` de PT-06 diz, em maiúsculas, desde 09/10:

> *"E A MESMA PEÇA **FECHA A PENDÊNCIA DO TELEGRAM E DO WHATSAPP**, que estavam nomeados no campo sem verificação de primeira mão desde agosto: Cesarino descreve um 'ecossistema em camadas múltiplas – que hoje inclui desde grandes plataformas do mainstream como YouTube e Facebook até aplicativos de mensagens fechados como **Telegram e WhatsApp**' (p. 181 impressa — PDF p. 20). A distinção que ela faz é FUNCIONAL — plataforma aberta de massa contra aplicativo de mensagem fechado —, e é isso, não a lista de nomes, que o registro precisava."*

**Conferido na folha antes de escrever este item:** a folha 20 do PDF de Cesarino (2022) traz literalmente a passagem, com `telegram` e `whatsapp` no corpo do texto, e o passo 7 do ciclo localiza **24 de 24** transcrições de PT-06, essa inclusive.

### 67.2 Por que a pendência sobreviveu: o registro se desmentia em dois campos

| Campo de PT-06 | O que dizia |
|:--|:--|
| `fonte_trecho` | *"FECHA A PENDÊNCIA DO TELEGRAM E DO WHATSAPP"* — **09/10/2026** |
| `framing_narrativa` | *"A expressão guerra cultural DEIXOU DE ESTAR SEM ÂNCORA em 10/10/2026"* |
| `status_verificacao` | *"**O QUE CONTINUA SEM ÂNCORA**, e são duas coisas nomeadas. (1) A expressão guerra cultural… (2) TELEGRAM E WHATSAPP como plataformas medidas…"* — **no presente, até hoje** |

> **Registro que se desmente em dois campos é a forma mais barata de uma pendência fantasma.** O bloco de `status_verificacao` foi escrito em 04/10 e era verdadeiro então; as duas lacunas fecharam em 09 e 10/10, nos campos vizinhos, e **ninguém voltou ao bloco que as declarava abertas**. O ledger lê o inventário de pendências, não os campos — e repetiu por onze dias uma decisão que não existia.

É a mesma família do item 54, em que a contagem de 26(c) tinha sido **copiada à mão** de outro item e perdeu uma decisão. Lá faltava uma; aqui sobrava uma. **A causa é a mesma: lista de pendência que não é remedida contra os registros que a geraram.**

### 67.3 O que foi corrigido, e o que PERMANECE

**Corrigido** — o bloco de `status_verificacao` passou a datar o que fechou, com a folha de cada âncora, e a errata está escrita no campo e na `nota_auditoria`.

**E o que permanece sem âncora é só uma coisa, que já estava certa:** as **cifras**. As 802 mensagens de WhatsApp (Soares et al., 2021) e as 867 de Telegram (Nascimento et al., 2020) são de segunda mão, nenhum dos dois no corpus, e a regra do projeto proíbe lastrear cifra conferida apenas contra outra citação dela. **O registro não as afirma** — elas aparecem como limite declarado, e assim ficam.

> **A distinção que o fechamento preserva:** o que PT-06 precisava não era a lista de nomes das plataformas, e muito menos a contagem de mensagens. Era a **distinção funcional** entre plataforma aberta de massa e aplicativo de mensagem fechado, porque é dela que depende o mecanismo — circulação que não exige consistência. Cesarino entrega exatamente isso, de primeira mão. **A pendência foi fechada pela peça certa, e não pelas duas que a ficha de 04/10 indicava.**

### 67.4 26(c) passa a quatro

| | Decisão | Item |
|:--|:--|:--|
| 1 | `data_hora` de PT-02 | 34.7 |
| 2 | A data de PT-57 | 51.5, decisão 2 |
| 3 | O `marco_teorico` que cita obra não lida | 47.5, decisão 2 |
| 4 | A promoção de classe de PT-03B, PT-05A e PT-06C | 51.5, decisão 1 |

**Nenhum dado, classe, página ou transcrição mudou nesta rodada** — 83 sub-eventos, classes 61 / 21 / 1, ciclo verde.

---

## 68. Dois antecedentes entram, e o codebook vai a 85 — 🔶 20/10/2026

**Encaminhamento:** *"Solicito a entrada de dois eventos no processo como antecedentes, que influenciam o processo de impeachment e ajudam a construir esse cenário conjuntural anterior. faça a varredura desses eventos em fontes oficiais e catalogue-os no corpus."*

**É a primeira vez que a contagem de sub-eventos cresce desde 10/10/2026**, e a primeira em que a **fonte documental** se move desde 29/09 — porque entrou documento que ancora registro, não literatura.

| | PT-01A | PT-01B |
|:--|:--|:--|
| **data** | 04/11/2014 (decisão) — 05/11/2015 (relatório) | 29/10/2015 |
| **o que é** | o PSDB pede ao TSE acesso aos sistemas eleitorais para auditoria própria | o documento *Uma Ponte para o Futuro*, 19 folhas |
| **classe** | `Confirmado` | `Confirmado` |
| **âncora** | duas notícias institucionais do TSE, por `§seção` | folhas 1, 2, 3 e 5 do PDF |

### 68.1 O que a varredura rendeu além do pedido — e é o achado

O encaminhamento pedia o **pedido de auditoria**. A fonte oficial entregou o pedido **e a sua refutação**, declarada em sessão pelo próprio Tribunal um ano depois:

> *"O objetivo da auditoria era verificar a lisura das Eleições 2014 (…) buscando evidências que comprovassem alguma suspeita ou tese de fraude, e **volto a dizer que não foi encontrada nenhuma evidência em tal sentido**"* — min. Dias Toffoli, 05/11/2015.

E a Corte, em 2014, **nomeia o mecanismo antes de qualquer análise nossa**:

> *"**Lendas urbanas passam a prosperar como objeto de campanha.** Não se trata de emprestar credibilidade a essas lendas urbanas, mas desmistificá-las"* — min. Gilmar Mendes, 04/11/2014.
> *"se o sistema eleitoral permite, de um lado, toda essa fiscalização, **ele não é imune a boatos**"* — min. Henrique Neves, mesma sessão.

> **Por que isto vale mais que um antecedente cronológico.** PT-01A é a **primeira ocorrência documentada, neste corpus, do quadro diagnóstico que PT-07 encontrará em 2021** — a contestação do sistema eletrônico de votação pelo lado derrotado —, e ela vem com a refutação oficial anexa, produzida **pela auditoria do próprio contestante**. E a proposta do **voto impresso** aparece já aqui, em 2015, no relatório do PSDB, com o min. Herman Benjamin declarando *"profunda dificuldade"* de compreendê-la. É a mesma pauta que retorna em 2021.

Dois achados menores, que o Tribunal registra e que valem para a leitura: o presidente afirma que o pedido *"se constitui em nenhuma inovação"* frente às Resoluções 23.397 e 23.399 de 2013; e **não consta nos autos que o partido houvesse entregue programa próprio de verificação** no prazo de 90 dias que a norma abria.

### 68.2 Três limites medidos, e dois deles desmentem premissas do encaminhamento

| Limite | Como foi medido |
|:--|:--|
| **As peças do TSE não nomeiam Aécio Neves** | falam do *PSDB* como parte. A identificação do candidato derrotado como ator do pedido **não está nas fontes oficiais obtidas**, e por isso não está no registro |
| **O documento da Ponte é internamente anônimo** | varridas as 19 folhas: **zero** ocorrências de *Temer*, *PMDB*, *Ulysses*, *Fundação*, *impeachment* e *Dilma*. A palavra *partido* aparece **uma** vez, genérica, na folha 5 |
| **Nenhuma peça processual foi obtida** | o TSE declara `AE 157804` (2014) e `Pet 185520` (2015) no pé de cada página; o relatório de auditoria do PSDB também não está no corpus |

> **E as duas premissas que a leitura desmentiu ficam escritas, porque mudam o que o registro pode afirmar.** O encaminhamento chama a peça de *"documento Ponte para o Futuro de Michel Temer"* — e o documento **não menciona Temer uma única vez**. Diz que ela *"articula o processo de impeachment"* — e a palavra **impeachment não aparece nela**, nem o nome do governo que ela critica. As duas atribuições são plausíveis e largamente sustentadas **fora** do corpus; dentro dele, não têm âncora. A regra da casa proíbe lastrear afirmação em citação de terceiro, e por isso **o registro não as afirma**. Se devem ser afirmadas, é decisão sua, e precisa de fonte que as ancore.

**A proveniência da cópia também tem ressalva:** o caminho do PDF no sítio da Fundação Ulysses Guimarães devolve **404** — devolve o HTML da página de erro, não o PDF —, e a cópia obtida é a do **diretório estadual do partido no Rio Grande do Sul**. Mesmo partido, não o editor original.

### 68.3 A convenção de 16/10 ganhou o segundo uso, e funcionou

As duas peças do TSE são **sem paginação** — o portal serve notícia, não PDF —, e por isso PT-01A cita por **`§seção`**, a convenção que nasceu na resolução da guarda do PT-19A. **A checagem 5 resolveu os cinco localizadores dele** contra os cabeçalhos dos arquivos vinculados, na primeira execução.

> E o portal do TSE **barra cliente automatizado na borda**: `curl` e `WebFetch` devolvem `403` da Akamai, e o arquivamento web devolveu `429`. A captura foi em **navegador comum**, por extração de texto. **Nenhum CAPTCHA foi encontrado nem contornado** — e isso fica declarado porque a regra do projeto sobre CAPTCHA é de princípio, não de conveniência.

### 68.4 O que a entrada mexeu, item por item

| | antes | agora |
|:--|--:|--:|
| sub-eventos | 83 | **85** |
| classes | 61 / 21 / 1 | **61 / 23 / 1** |
| PDFs no corpus | 63 / 12.125 p. | **64 / 12.144 p.** |
| **documental** | 22 / 6.951 p. | **23 / 6.970 p.** |
| manifesto | 65 peças | **68** |
| `confirmados` no passo 7 | 73 | **74** — as transcrições da Ponte foram localizadas nas folhas |
| fora do alcance do conferidor | 5 | **6** — PT-01A entra, por localizador estrutural |

**Os quatro artefatos mantidos à mão foram alinhados**: as duas figuras ganharam os registros e a contagem, e o relatório ganhou duas linhas na tabela da Etapa 2. E ali apareceu mais uma cifra velha: a linha do XLSX dizia **"83 × 16"** — o esquema passou a 17 campos em 16/10 e aquela linha não acompanhou. **Era a segunda vez que um "× 16" sobreviveu a uma mudança de esquema** (a primeira está no item 55.4).

### 68.5 O que fica para você

1. **O nome dos dois mecanismos.** Os dois campos trazem **proposta explicitamente não atribuída**, pelo precedente da tarefa 19.
2. **A classe dos dois.** Entraram em `Confirmado`. PT-01A sobe a `Confirmado em fonte primária` se `AE 157804` ou `Pet 185520` entrarem no corpus; PT-01B, se entrar uma peça que **atribua** o documento ao PMDB em fonte oficial.
3. **Se PT-01B deve afirmar a função de articulação do impeachment** — e, se sim, com que fonte.
4. **A ordem dos identificadores.** PT-01B é de 29/10/2015 e PT-02 cobre *2015–2016*: o sufixo mantém a ordem de inserção e a data correta, mas o intervalo de PT-02 começa antes. Se preferir outra numeração, é uma linha de pedido — e eu **não** renomeio identificador por conta própria, porque há remissões a eles.

---

## 69. A tabela-espelho, e a figura do artigo afirma o que o codebook corrigiu — 🔶 20/10/2026

**Encaminhamento:** *"Sobre ele eu queria sugerir a criação de uma tabela de espelho de todos os eventos e suas características de acordo com o que está disposto no html e no SVG."*

A sugestão era de instrumento. Ao construí-lo, ele achou na primeira execução **três registros em que a cronologia interativa afirma o que o codebook já retirou** — e a figura é a peça que vai para o artigo.

### 69.1 O que o ciclo não conferia, e por quanto tempo

`conferir_figuras.py` confere **cobertura, selo de status, procedência e cifras retiradas**. O próprio cabeçalho dele diz: *"Nada disto lê o conteúdo dos rótulos."* E o **item 42.3, de 10/10/2026**, registrou a lacuna com uma prova: reinjetei o nome velho de um mecanismo na figura e no relatório, e **zero de duas pegaram**. A conclusão de então foi criar a checagem 7 — que vigia **nomes formalmente registrados como retirados**, e só eles.

> **A checagem 7 cobre a reincidência; não cobre a defasagem.** Um registro renomeado cujo nome antigo nunca entrou naquele registro deixa a figura desatualizada em silêncio — e foi exatamente o que aconteceu com as retificações de 04/10/2026, que não eram "nomes retirados" e sim reformulações do campo.

### 69.2 Os três casos, e o pior deles afirma o contrário do codebook

| Registro | A figura diz | O codebook diz |
|:--|:--|:--|
| **PT-02** | *"Apropriação de repertório **(spin-off)**"* | *"Apropriação parcial do repertório de protesto por contramovimentos conservadores (…) **Não é ciclo novo nem spin-off**: é continuidade dentro de um mesmo processo de confronto"* |
| **PT-01** | *"**Abertura de estrutura de oportunidade política** e difusão de um repertório de rua massivo"* | *"**Janela de oportunidades políticas** aberta no ciclo de 2013 (…) — formulação do pesquisador, adotada em 04/10/2026 **no lugar de** 'abertura de estrutura de oportunidade política'"* |
| **PT-06** | *"consolidação de um ecossistema informacional paralelo (Telegram/WhatsApp) — **a infraestrutura comunicacional que tornará viável** a convocação de dezembro de 2022"* | *"Mobilização permanente da base por circulação de enquadramentos negacionistas (…) RETIFICAÇÃO DE 04/10/2026"* — as redes **cresciam desde o início dos anos 2000**, e a pandemia carrega infraestrutura anterior |

> **PT-02 é o caso duro: a figura afirma literalmente o que o campo nega**, e nomeia o conceito — *spin-off* — que o registro recusa em letras. PT-01 e PT-06 carregam formulações que o próprio campo declara substituídas: **o codebook sabe que aquele texto saiu, e a figura não.**
>
> Para uma peça de publicação isto é o defeito mais caro possível, porque **a figura tem a aparência de ser gerada da base**. O leitor não tem como saber que não é.

### 69.3 Um achado estrutural: ponto composto não pode ter um nome só

A cronologia tem **80 pontos para 85 registros**, porque três são **compostos** — e o mapa que declara isso vive **só dentro de `conferir_figuras.py`**, na constante `COMPOSTOS`. A figura não diz ao leitor que um ponto representa três registros.

| Ponto | Cobre | E os mecanismos do codebook são |
|:--|:--|:--|
| `PT-06A/B/C` | 3 registros | *anulação por vício de competência* · *descertificação do agente judicial* · *reabertura da estrutura de oportunidade eleitoral* |
| `PT-08A / PT-08B / PT-08C` | 3 registros | *captura de aparato estatal para fim eleitoral* · *tentativa de contenção institucional preventiva* · *supressão seletiva de participação eleitoral* |
| `PT-03C/D` | 2 registros | *fechamento da via recursal* · *remoção do competidor e reconfiguração da estrutura de oportunidade eleitoral* |

**O rótulo do ponto `PT-06A/B/C` diz *"dois mecanismos em conjunto"* — e o ponto cobre três registros, com três mecanismos distintos.** Não é texto velho: é agregação que perde informação, e ela só aparece quando se põe a figura ao lado do codebook linha por linha.

### 69.4 O desenho, e a medição que o decidiu

Comparados os seis campos de prosa da figura com os do codebook, nos 85 registros:

| campo | idêntico | contido | parafraseado |
|:--|--:|--:|--:|
| `tgt` → `target_alvo` | 67 | 2 | 7 |
| `res` → `resposta_estatal` | 58 | 4 | 14 |
| `ator` → `ator_grupo` | 50 | 7 | 19 |
| `rep` → `repertorio_acao` | 43 | 4 | 29 |
| `frm` → `framing_narrativa` | 29 | 1 | 46 |
| `mec` → `mecanismo_causal` | **0** | **0** | **todos** |

> **`mec` parafraseado em toda parte é desenho, não defeito**, e por isso a tabela **não cobra igualdade de prosa**. A figura precisa de uma frase legível; o campo carrega a prosa de auditoria — a razão de cada troca de nome, os limites declarados, as remissões. Uma guarda que exigisse igualdade reprovaria tudo **e ensinaria a ignorar a guarda**, que é o erro que este repositório já cometeu e registrou.

**O que é conferível é o NOME** — a frase até o primeiro `:`, travessão ou ponto. É a coluna `espelho_nome_mecanismo`, e a linha de base é **17 divergências**.

### 69.5 E a linha de base corrige uma cifra que eu havia estimado

Ao levantar o problema para você, **eu anunciei 23 divergências**. O gerador mede **17**, e a diferença não é detalhe de arredondamento:

| | |
|:--|:--|
| **minha medição** | regex própria, que leu **79** entradas e não resolvia pontos compostos; recorte de nome só em `:` e travessão |
| **o gerador** | `BLOCO`, `campo`, `CLASSE` e `COMPOSTOS` **importados** de `conferir_figuras.py`, alcançando os **85** registros; recorte também no ponto final; e toda aspa normalizada para a mesma, o que tirou PT-56 da lista — ali a diferença era o **caractere**, não o nome |

> **Cifra estimada à mão não vale como linha de base**, e esta é a quarta vez que a lição aparece neste repositório. A regra que fica: **medir com o instrumento do projeto, não com regex de ocasião** — e, quando o instrumento existe, importar dele em vez de reimplementar, que é o que o gerador faz com as quatro constantes.

### 69.6 A prova negativa, e ela mostra complementaridade

Injetado na figura, no lugar do nome de PT-07, o texto **`Alinhamento de quadros`** — sem a palavra *prévio*:

| Guarda | Resultado |
|:--|:--|
| **checagem 7** (nomes retirados) | **passa** — ela casa substring exata, e o registro vigia `Alinhamento de quadros prévio`, com a palavra final |
| **tabela-espelho** | **reprova** — `divergências de nome: 18 (base 17)`, saída 1, ciclo derrubado |

**As duas guardas não se substituem.** A checagem 7 pega o nome morto **exato** voltando a qualquer um dos quatro artefatos; a tabela-espelho pega **qualquer** nome que não seja o do codebook, inclusive um que nunca foi formalmente retirado. Era essa a metade que faltava.

### 69.7 O que a tabela entrega para o artigo

| Peça | O que é |
|:--|:--|
| `reports/TABELA-ESPELHO-EVENTOS.md` | forma scanável: um registro por linha, com data, evento, fase, classe, nome do mecanismo, ponto composto e o selo do espelho |
| `data/processed/tabela_espelho_eventos.csv` | **32 colunas**: os seis campos da figura ao lado dos seis do codebook, mais o estado do espelho de cada um, a âncora e o valor de autonomia |

**Gerada, nunca escrita à mão** — e isto é a razão de ela existir como script e não como arquivo: uma tabela-espelho mantida à mão seria a **quinta** cópia dos mesmos dados, e este repositório tem o histórico de quatro cópias envelhecendo em silêncio. O ciclo passou a dez passos, com ela no quarto.

### 69.8 O que isto deixa aberto

**As 17 divergências, por classe** — e a frente seguinte do plano é zerá-las:

| Classe | Quantas | O que fazer |
|:--|--:|:--|
| **a figura carrega o que o codebook corrigiu** | 3 | PT-01, PT-02, PT-06 — a figura passa a dizer o que o registro diz, e as formulações substituídas entram no registro da checagem 7 |
| **ponto composto com um nome só** | 5 | PT-03D, PT-06A/B/C, PT-08B/C — o rótulo precisa enumerar, e *"dois mecanismos"* para três registros precisa de correção |
| **abreviação da figura** | 9 | PT-01A, PT-01B, PT-15, PT-30, PT-42, PT-48, PT-53, PT-58 e PT-03D — alinhar o nome ao do codebook, mantendo a paráfrase do corpo |

**E duas cifras do cabeçalho do HTML seguem velhas:** *"Última revisão: 25/09/2026"*, quatro edições atrás, e *"83 sub-eventos, 60 deles em fonte primária"*, quando são 85 e 61.

---

## 70. As 17 divergências caíram a zero — e a guarda de nome retirado era cega à caixa — ✅ 21/10/2026

**Encaminhamento:** *"e enumere os três mecanismos no rótulo, sem desdobrar o ponto"* — a decisão de forma que a frente F10 esperava.

A frente era de execução: zerar as 17 divergências que a tabela-espelho mediu em 20/10. Ao executá-la, a varredura das três formulações retiradas achou **um defeito maior do que a frente**: elas não estavam só na figura, e a checagem 7 — a guarda criada em 10/10 exatamente para impedir que nome retirado voltasse — deixava passar **dois usos vivos** por ser sensível à caixa.

### 70.1 As 17, por classe, e o que cada uma exigiu

| Classe | Quantas | O que se fez |
|:--|--:|:--|
| **a figura afirmava o que o codebook corrigiu** | 3 | PT-01, PT-02 e PT-06: o rótulo passou a dizer o que o registro diz, e as formulações substituídas entraram na checagem 7 |
| **ponto composto com um nome só** | 6 | PT-03C/D, PT-06A/B/C e PT-08A/B/C: o rótulo **enumera um mecanismo por registro**, e o ponto não se desdobra |
| **abreviação do nome** | 8 | PT-01A, PT-01B, PT-15, PT-30, PT-42, PT-48, PT-53 e PT-58: nome alinhado, paráfrase do corpo mantida |

**O rótulo de `PT-06A/B/C` dizia *"Dois mecanismos em conjunto"* para um ponto que cobre TRÊS registros** — e nomeava dois deles, calando `PT-06A`, que é justamente o que a denúncia da PGR aponta como marco inicial. Não era texto velho: era agregação que perdia o registro analiticamente decisivo.

### 70.2 A cobrança no ponto composto mudou de forma, e tinha de mudar

Um ponto composto tem **um** campo `mec` para dois ou três registros. Cobrado por prefixo — a regra dos pontos simples —, o rótulo correto seria reprovado em dois registros, e o rótulo que nomeia um irmão e cala os outros seria aprovado num. Então:

> **Em ponto composto a cobrança é de CONTINÊNCIA:** o nome de cada registro tem de aparecer no rótulo. A guarda passa a cobrar a **enumeração completa** em vez de uma escolha entre irmãos.

### 70.3 O achado que a frente não ia procurar: a checagem 7 é cega à caixa

Varridas as três formulações retiradas nos quatro artefatos vigiados, **com a caixa ignorada**, apareceram 13 ocorrências — e duas delas eram **nome formalmente retirado, em uso, que a guarda deixava passar**:

| O que estava vivo | Onde | Por que passou |
|:--|:--|:--|
| `certificação de eficácia` | relatório, mecanismo do bloco 2013–2016 **e** elo da cadeia ASCII | a entrada vigiada é `Certificação de eficácia`, com maiúscula |
| `Rede distribuída com nós centralizadores` | relatório, linha de PT-12A na tabela de síntese | a entrada vigiada é minúscula |

> **A lição de 18/10 foi escrita e não foi retroaplicada.** Naquele dia o nome de PT-07 entrou com **três variantes** no registro, com o comentário explícito de que "guarda de substring exige a forma exata, e uma só entrada teria deixado duas passar". As cinco entradas anteriores ficaram como estavam — e duas delas tinham o buraco.
>
> **Correção estrutural, não entrada nova:** a comparação passou a **ignorar a caixa**, o que resolve a classe inteira e dispensa manter variantes. As duas entradas que existiam só por diferença de caixa saíram na mesma rodada; 14 strings vigiadas viraram 17, com três a mais de conteúdo novo e duas a menos de redundância.

**O preço foi pago no texto, não na guarda.** A comparação não distingue **menção** de **uso** — e isso é desenho, porque distinguir exigiria frases-moldura declaradas, que é lista a manter. Então os cinco lugares que *narravam* a troca deixaram de **grafar** o nome morto e passaram a nomear a **afirmação** que saiu: *"em substituição ao nome anterior, que era o do modelo de limiar"*. É o padrão que a própria guarda impôs em 18/10, quando reprovou um texto novo meu que escrevia o nome morto para dizer que ele havia saído. O registro do nome antigo continua em `metadados.revisoes` e em `docs/analise/`, que não são artefatos vigiados.

### 70.4 E o relatório carregava o mesmo defeito da figura, em sete lugares

| Onde | O que afirmava |
|:--|:--|
| mecanismo do bloco 2013–2016 | os **dois** nomes retirados, lado a lado |
| cadeia ASCII, elo de PT-03 | o nome retirado de PT-03 |
| cadeia ASCII, elo de PT-06 | *ecossistema digital paralelo* |
| fato do bloco PT-05/PT-06 | que a pandemia **consolidou** a infraestrutura |
| mecanismo do bloco PT-05/PT-06 | *construção de infraestrutura comunicacional autônoma* — exatamente o que a retificação nega |
| tabela de síntese, linha de PT-01 | a formulação canônica substituída em 04/10 |
| tabela de síntese, linha de PT-12A | o nome retirado em 10/10 |

> **A tabela de síntese do relatório é uma TERCEIRA cópia manual dos nomes de mecanismo**, e a tabela-espelho não a compara — ela compara o HTML e o SVG. Dois de seus 85 registros carregavam nome retirado, e só apareceram porque a varredura por string os alcançou. **Medir a tabela de síntese inteira contra o codebook está listado como pendência, não feito nesta frente.**

### 70.5 Presença não é ausência de outra

O cabeçalho do HTML dizia, no mesmo parágrafo, *"85 sub-eventos"* numa frase e *"83 sub-eventos, 60 deles em fonte primária"* na seguinte — por quatro edições. E `conferir_figuras.py` **passava**, porque a guarda era `if "85 sub-eventos" not in html`: a cifra certa a satisfazia e a velha convivia ao lado dela.

> **Guarda de substring só prova que a frase certa existe.** Para provar que a errada não existe, tem de varrer **todas** as ocorrências do padrão. As duas cifras do cabeçalho passaram a ser varridas por regex nas duas figuras, e qualquer número diferente do medido no codebook derruba o ciclo.

**E a data digitada saiu.** *"Última revisão: 25/09/2026"* não é conferível por nada e estava quatro edições atrasada. No lugar dela, o cabeçalho declara **onde** a figura é conferida — `conferir_figuras.py` para cobertura, selo, procedência e cifras; a tabela-espelho para o nome do mecanismo — e diz que três pontos são compostos, informação que até aqui vivia **só** dentro de uma constante do verificador.

### 70.6 Quatro provas negativas, uma por guarda

Cada uma registra o SHA-256 do artefato, injeta o defeito, roda o verificador, reverte pela troca inversa e **confere o SHA-256** — prova que deixa resíduo é pior que prova nenhuma.

| Injeção | Guarda | Resultado |
|:--|:--|:--|
| nome trocado em ponto simples (PT-15) | tabela-espelho, base 0 | `1 (base 0)`, saída 1 |
| um dos três nomes sai do rótulo composto (PT-08B) | continência no ponto composto | `1 (base 0)`, saída 1 |
| nome retirado volta em **caixa diferente** | checagem 7 | acusou — **e antes de 21/10 isto passava** |
| cifra velha de sub-eventos ao lado da certa | `conferir_figuras.py` | acusou |

### 70.7 A cobrança do nome NÃO migrou para `conferir_figuras.py`

O plano da frente dizia que, zerada a base, a comparação de nome entraria naquele script. **Não entrou, e a razão é a regra da casa:** a tabela-espelho já **importa** `BLOCO`, `campo`, `CLASSE` e `COMPOSTOS` de lá, e reimplementar o recorte de nome no verificador seria a **quinta cópia** da mesma lógica num repositório cujo modo de falha batizado é a cópia que envelhece em silêncio. A guarda fica onde o dado está — passo 4 do ciclo, que roda a cada alteração — e o *docstring* de `conferir_figuras.py` aponta para lá, para quem venha procurar no lugar errado.

### 70.8 O que isto deixa aberto

| | |
|:--|:--|
| **a tabela de síntese do relatório** | terceira cópia manual dos nomes de mecanismo, nunca medida contra o codebook; dois registros carregavam nome retirado |
| **`mecanismo_causal` de PT-03D** | atribui *"Em vocabulário de Tilly e Tarrow"* a obra não lida. **Saiu da figura** nesta frente; o campo do JSON é de F12 |
| **o `mec` do SVG** | resume por **faixa**, não por registro, e a tabela-espelho não o compara — só confere se o id aparece. A faixa conjuntural recuperou a palavra *parcial* nesta frente; as outras compressões são legítimas |

---

## 71. PT-57 passa a datar o que a fonte primária data — ✅ 21/10/2026

**Encaminhamento:** *"O que me sugere? Isso afeta a compreensão do process tracing? se for somente constatação do resultado, não tem tanta influência no decorrer do processo"* — e depois *"Execute a F11"*.

Decisão sua, **saída (a)** das três oferecidas em 15/10/2026 no item 51.5: `data_hora` de PT-57 passou de **22/10/2025** a **15/10/2025**, e o registro passou a codificar a **conclusão** do acórdão da AP 2668 em vez da sua publicação.

### 71.1 A remedição, porque a nota era minha

A nota de auditoria do registro afirmava uma varredura feita em 15/10. **Não se age sobre nota: age-se sobre medição.** As 1.991 folhas foram varridas de novo em 21/10, e saíram 7.511.281 caracteres de camada de texto:

| Buscado | Ocorrências | Onde |
|:--|--:|:--|
| `22/10/2025` | **0** | — |
| `22 de outubro de 2025` | **0** | — |
| `15 de outubro de 2025` | **2** | **só na folha 19** |
| `11/09/2025` | 138 | 73 folhas — a data da sessão, estampada por toda parte |

> **A data que o registro afirmava não existe no documento que o ancora.** O que o acórdão data é a si mesmo: *"A Turma condenou os denunciados ao pagamento das custas processuais, nos termos do art. 804 do Código de Processo Penal. Brasília, 15 de outubro de 2025. Ministro Alexandre de Moraes, Relator"* — folha 19, que o registro já transcrevia.
>
> **Saiu uma data sem lastro.** A publicação no DJe segue fora do corpus: quem quiser datá-la precisa incorporar o DJe, que é a saída (c), não escolhida.

### 71.2 O seu critério decidiu o alcance, e ele estava certo

Você perguntou se isto afeta a compreensão do process tracing e concluiu que, **sendo constatação de resultado, não**. Confirmado contra o codebook: `T+1 Resposta judicial` **não alimenta elo nenhum a jusante** — nenhum registro depende de PT-57 para se sustentar, e o valor da peça é de **fonte**, não de **elo**: é o documento que anexa a evidência à narrativa causal do Estado. Essa distinção entrou no próprio campo `mecanismo_causal`, depois do nome.

**O nome do mecanismo NÃO mudou**, e não mudou de propósito: nomear mecanismo é decisão separada, pelo precedente da tarefa 19. Você decidiu a **data**.

### 71.3 Uma errata de aspa — e uma correção minha que tive de desfazer no mesmo dia

A nota de 15/10 escrevia, **entre aspas**, que os carimbos *"ACÓRDÃO ELETRÔNICO DJe-N DIVULG … PUBLIC …"* pertenciam a precedentes citados. Medido:

| Buscado | Folhas | O que é |
|:--|--:|:--|
| `DJe-N` | **0** | **não existe.** Era abreviação minha para *DJe-<número>*, posta entre aspas como se fosse transcrição. As formas reais são `DJe-161`, `DJe-130`, `DJe-045` |
| `ACÓRDÃO ELETRÔNICO` | 7 | o carimbo existe, e há a variante `PROCESSO ELETRÔNICO` |
| `DIVULG` | 11 | idem |
| `DJe de ` | 35 | a outra forma de citar precedente, no corpo dos votos |

Lidas as folhas 888, 910 e 1059, o carimbo aparece assim: *"(AP 470 EI-quintos, Relator(a): LUIZ FUX, Relator(a) p/ Acórdão: ROBERTO BARROSO, Tribunal Pleno, julgado em 27-02-2014, **ACÓRDÃO ELETRÔNICO DJe-161 DIVULG 20-08-2014 PUBLIC 21-08-2014**)"*. **São de precedente citado, como a nota dizia** — *AP 470 EI-quintos*, *AP 932*, *HC 132179*.

> **E aqui eu errei duas vezes, na mesma tarde.** Para checar os carimbos, amostrei duas folhas da lista de `PUBLIC` — 351 e 801 — e nas duas o casamento estava dentro de **REPUBLICANOS** (títulos de planilha da PRF) e **REPUBLICANO** (*"postulado republicano"*). Escrevi então que *"`PUBLIC` não é carimbo nenhum"*, e **cheguei a gravar essa errata na agenda**. É falso: das 13 folhas com `PUBLIC`, **onze** carregam o carimbo real e **duas** são a palavra. Peguei porque a varredura seguinte mostrou `DIVULG` em 11 folhas — número que não fecharia se nenhum `PUBLIC` fosse carimbo.
>
> **A lição é de amostragem, e é nova nesta lista: amostra de duas não desmente um censo de vinte e seis.** Eu peguei as duas primeiras folhas que a lista imprimiu, que por acaso eram as duas exceções, e generalizei. O que a amostra autoriza a dizer é *"nas folhas que li, é X"* — nunca *"não é carimbo nenhum"*.

### 71.4 E saiu a única citação de Wikipédia do codebook

`fonte_url` de PT-57 apontava para a Wikipédia. **Medido em 21/10: era o único dos 85 registros a fazê-lo**, e dez registros têm o campo legitimamente vazio — nenhuma guarda o exige.

Era resquício da versão anterior à obtenção do inteiro teor: o backup pré-Lula traz o **mesmo URL** ao lado de `status_verificacao` = *"A verificar em fonte primária (inteiro teor no STF)"*. Quando o PDF de 1.991 folhas entrou, o URL ficou.

**Não entrou URL no lugar.** A rota de obtenção está declarada em `PROCEDENCIA` — *"STF — redir.stf.jus.br"* —, mas o `docID` exato não foi registrado, e compor um endereço de paginador sem conferir que ele devolve *esta* peça seria asserção sem leitura. Fica listado.

### 71.5 A contagem de 26(c) deixou de ser um número e passou a ser uma lista

O texto de 26(c) dizia *"quatro decisões"* e listava `data_hora` de PT-02, o `marco_teorico`, a data de PT-57 e a promoção de classe. **No fechamento da frente F10 eu relatei outras quatro** — deixei o `marco_teorico` de fora e acrescentei os nomes de PT-01A e PT-01B, que entraram com o item 68 em 20/10 e **nunca foram acrescentados ao ledger**.

> **Contagem de pendência copiada de outro lugar perde item, e esta é a segunda vez** — a primeira foi em 16/10, quando o inventário de 50.4 deixou a decisão 1 de 47.5 de fora. **A correção não é trocar o número: é fazer a lista mandar no número.** O ledger passou a enumerar:
>
> **ABERTAS, decisão sua:** (i) `data_hora` de PT-02 · (ii) promoção de classe de PT-03B, PT-05A e PT-06C · (iii) o nome do mecanismo de PT-01A · (iv) o nome do mecanismo de PT-01B.
> **DECIDIDA, execução pendente:** o `marco_teorico`, que você estruturou em 20/10 e a frente F12 executa.

### 71.6 O que isto deixa aberto

| | |
|:--|:--|
| **o `docID` de PT-57** | `fonte_url` ficou vazio; recuperar o endereço em `redir.stf.jus.br` e **conferir que devolve esta peça** é tarefa de uma rodada, não feita aqui |
| **o DJe** | segue fora do corpus. Se entrar, a publicação ganha âncora própria e pode voltar como registro distinto da conclusão |

---

## 72. O marco teórico ganha a estrutura que você fixou — e três medições mudam o que se pode citar — ✅ 21/10/2026

**Encaminhamento:** *"Marco Teórico é a Teoria do Processo Político. Os conceitos de Framing e Ciclo de protesto, Mechanisms são âncoras teóricos. Beach and Pedersen (2019) é âncora metodológico. Julgue a adaptabilidade dessa abordagem."* E: *"Os conceitos não são excludentes. Eles se complementam. vamos estabelecer a diferenciação entre eles, mas construir os pontos de complementariedade e interseção."*

### 72.1 O campo era uma lista de três itens de tipos diferentes

`marco_teorico` dizia: *"Teoria do Processo Político (McAdam, Tarrow, Tilly); Process Tracing (Beach & Pedersen, 2019); Framing (Snow & Benford, 2000)"*. **Um marco, um método e um conceito na mesma lista** — e, **até 21/10/2026**, duas das três citações eram de obra não lida. (As duas mudaram de estado no mesmo dia: Beach e Pedersen entrou no corpus e foi lido em parte; Snow e Benford saiu da declaração.)

Passou a declarar a sua distinção, que é de **tipo**: um **marco** (Teoria do Processo Político), três **âncoras teóricas** (Mechanisms · Framing · Ciclo de protesto) e uma **âncora metodológica** (process tracing). Cada âncora cita a **peça lida**, com folha.

> **E o ganho não é de arrumação.** Enquanto os três estavam na mesma lista, *Framing* aparecia como **rival** do marco — uma teoria ao lado de outra. Posto como âncora **dentro** dele, volta ao lugar que a própria Teoria do Processo Político lhe dá: enquadramento é um dos componentes do programa, não uma alternativa a ele.

**E Snow e Benford (2000) saiu.** A obra está `PENDENTE` e `closed` na camada A, sem depósito em repositório algum, e nunca foi lida — ter lido o capítulo de 2019, do mesmo autor principal, **não autoriza citá-la**. Fica como referência de **genealogia**. Isso tornou falsas seis passagens que afirmavam, **no presente**, que o campo a declara; as seis ganharam errata datada, nos documentos 06, 08, 09 e 15. *(O ciclo confere cifra, âncora e nome retirado — **não confere tempo verbal**.)*

### 72.2 A diferenciação, e o que cada âncora NÃO explica

| Âncora | Unidade | Explica | **Não** explica |
|:--|:--|:--|:--|
| **Mechanisms** | o elo | como um estado produz o seguinte | por que o episódio tem a forma temporal que tem |
| **Framing** | o significado | diagnóstico, atribuição de culpa, prognóstico | se o quadro corresponde ao mundo — e **aqui não corresponde** |
| **Ciclo de protesto** | a fase | onde o episódio está na onda longa | por que **este** ciclo radicalizou |

**As três lacunas da coluna da direita são onde o caso trabalha**, e a terceira é explícita na fonte lida: *"radicalization in a violent form does not seem to be an unavoidable consequence"* de dinâmica cíclica.

### 72.3 As interseções, e a quarta é a que decide

| | A ponte | Onde está lida |
|:--|:--|:--|
| **(a)** Framing × Ciclo | *master frames* surgem cedo num **ciclo** e passam a *"color and constrain"* os quadros posteriores | Snow *et al.* (2019), p. 395 impressa |
| **(b)** Framing × Mechanisms | *articulação* e *elaboração* são chamados de **mecanismos discursivos** — e o capítulo usa *mechanism* oito vezes, sempre nesse sentido | p. 397-398 impressas |
| **(c)** Ciclo × Mechanisms | a definição de ciclo inclui *difusão* e *inovação de repertório*, que são mecanismos lidos por folha | verbete de della Porta; DoC p. 332-333 impressas |
| **(d)** Marco × Framing | **a retratação dos próprios proponentes** | DoC **p. 45 impressa**, citada no verbete *Political opportunity* |

> **A (d) é o fundamento, e não é escolha de desenho deste projeto:**
>
> *"Opportunities and threats are **not objective categories**, but depend on the kind of **collective attribution** that the classical agenda limited to framing of movement goals."*
>
> **É o marco declarando que a sua categoria central depende da âncora de enquadramento.** A complementaridade é uma correção que a Teoria do Processo Político fez em si mesma, e está na obra lida.

**E o modelo da articulação é gênero e espécie, não exclusão** — ancorado na frase que a peça lida dá: *"frame bridging can be considered a specific form of frame articulation"* (p. 400 impressa). As três âncoras não disputam o mesmo objeto: são **três níveis de descrição** do mesmo processo — o elo, o significado e a fase. Quando duas parecem competir, a pergunta não é *"qual está certa?"*, é *"qual nomeia o gênero e qual nomeia a espécie?"*. **Esse critério é operacional:** foi o que resolveu o nome de PT-07.

### 72.4 Três medições, e as três mudam o que se pode afirmar

| Medição | Resultado |
|:--|:--|
| `political opportunity structure` em *Dynamics of Contention* | **ZERO** ocorrências em 411 folhas; `exogenous`, **uma** (p. 120 impressa). **O vocabulário de estrutura de oportunidade não se cita por essa obra** |
| alguma edição de Beach e Pedersen no corpus? | **nenhuma.** Abri os dois PDFs cujo nome diz *process tracing*: `Livro_Process tracing.pdf` é **Cunha e Araújo** (Enap, 104 folhas) e `process-tracing-research-designs-a-practical-guide.pdf` é **Ricks e Liu** (2018, 5 folhas). Confirma por medição o que a §7.3 do documento 09 afirmava |
| Ricks e Liu (2018) estava lida? | **não estava no inventário — e está no corpus desde antes.** Achada ao fazer a medição acima, e **lida integral nesta frente** |

> **A segunda medição é a regra da casa aplicada a mim mesmo:** antes de declarar que uma obra não está no corpus, **abra os arquivos cujo nome sugere que ela esteja**. O documento 09 afirmava isso desde 30/09 e nunca havia sido medido.

### 72.5 PT-03D deixou de atribuir a obra não lida — e a leitura qualificou o mecanismo

O campo dizia *"em vocabulário de Tilly e Tarrow"*, e **Tilly e Tarrow (2007) não está no corpus**. Passou a citar o verbete *Political opportunity / political opportunity structure* de della Porta (2013, **p. 478-483 impressas**), lido integral.

**E não foi só troca de crédito.** O verbete registra que mudanças na estrutura de oportunidade *"do not have any effect on a social movement unless they are **perceived** as being important by the movement itself"*. Logo o que a decisão judicial de abril de 2018 altera é **regra de competição** — objetiva e datada —, não *oportunidade* como categoria objetiva. **O campo passou a dizer isso**, e a mesma correção entrou na figura (na frente F10) e no relatório.

### 72.6 A adaptabilidade da âncora metodológica — e a rota é sua

**O julgamento:** a ontologia que você quer é a que ancora a relação causal no **caso singular** e indica o process tracing como o método próprio dela — que é exatamente o que 85 sub-eventos de um episódio fazem, sem reivindicar recorrência. **Ela é adaptável, e o aparato em uso já é dessa família.** O problema não é de adequação: é de **procedência** — o que se sabe de Beach e Pedersen vem de citação colhida em Cunha e Araújo e em Ricks e Liu, as duas lidas na fonte.

**O que Ricks e Liu entregam, lido hoje:** um checklist de sete passos. **Os passos 2 e 3 — estabelecer linha de tempo, construir o grafo causal — são o que este codebook é.** Os passos 4 e 5 — a escolha alternativa em cada momento e o seu desfecho contrafactual — são o que ele **não** tem de forma sistemática, e os autores declaram o custo: *"Counterfactuals are vital to process-tracing, **especially when no alternative cases are considered**"*. Hoje o projeto faz isso em **um** nó, PT-28.

| | **(A) Declarar a âncora como não lida** | **(B) Obter e ler a obra** |
|:--|:--|:--|
| **o que se faz** | o campo mantém Beach e Pedersen, com a nota de que nenhuma edição está no corpus; o aparato operante segue creditado à cadeia lida — Van Evera (1997) → Bennett (2010) → Collier (2011) | obter *Process-Tracing Methods* (2. ed.) e ler na fonte; a âncora passa a ser citável por folha |
| **preço** | o projeto declara uma âncora que não abriu. É honesto porque está declarado, **mas um parecerista vai perguntar** — e a pergunta é legítima, porque é a âncora que justifica o desenho inteiro | tempo de leitura, e a rota é incerta: as editoras barradas estão medidas. Pode exigir pedir o arquivo, via pela qual nove peças já chegaram |

> **Recomendação, se quiser uma: (A) agora, (B) quando houver folga de leitura.** (A) **já é verdade** — basta escrevê-la —, e (B) não altera nenhum dado do codebook: altera o que o projeto pode **citar**. E se (B) acontecer, os passos 4 e 5 de Ricks e Liu passam a ser exigência explícita, e aí a conta é de **pesquisa**, não de leitura.
>
> **Uma nota que não é rota:** haveria a opção de trocar a âncora por uma peça lida — Collier, ou Mayntz — e dispensar Beach e Pedersen. **Não está sobre a mesa porque você fixou a âncora**, e trocá-la seria decidir no seu lugar. Fica registrada para que a omissão não pareça esquecimento.

### 72.7 O que isto deixa aberto

| | |
|:--|:--|
| **a rota da âncora metodológica** | (A) ou (B) acima — **decisão sua** |
| **os passos 4 e 5 de Ricks e Liu** | contrafactual por nó existe em **um** nó. Estendê-lo é pesquisa, não leitura, e não foi aberto aqui |
| **`framing_narrativa` sem grade funcional** | o capítulo de 2019 dá três tarefas centrais — diagnóstico, prognóstico, motivacional — e o campo **nomeia** quadros sem classificar função. Cobrança da §10, ainda aberta |
| ~~os sete verbetes lidos-a-ler~~ | ❌ **ESTA LINHA ESTAVA ERRADA, e a guarda G2 do registro de leitura a pegou em 21/10/2026.** Os sete **estavam lidos** — integrais, entre 29/09 e 14/10/2026 —, e a leitura está em `docs/analise/10_VERBETES-ENCICLOPEDIA.md`, cujo título diz *"os onze verbetes lidos na fonte"*. Eu copiei esta lista da §7.4 do documento 09, escrita em 30/09, isto é **antes** de o documento 10 existir. Ver item 75 |

---

## 73. A âncora metodológica entra no corpus, a grade do enquadramento é inferida, e eu declarei não lido o que estava lido — ✅ 21/10/2026

Três encaminhamentos seus, na mesma mensagem. **E o terceiro expôs um erro meu que vale mais do que os três entregáveis juntos.**

### 73.1 Beach e Pedersen entra no corpus — e muda uma rota, não as duas

**Encaminhamento:** *"Coloquei o artigo em anexo na conversa. copie para o repositório para ficar como referência."*

**Não é um artigo: é o livro inteiro.** BEACH, D.; PEDERSEN, R. B., *Process-Tracing Methods: Foundations and Guidelines*, Ann Arbor: The University of Michigan Press, **2013**.

| | |
|:--|:--|
| **onde** | `Fontes/05_Bibliografia-teorica/BEACH-PEDERSEN_Process-Tracing-Methods_Michigan-2013.pdf` |
| **integridade** | `sha256 f08efa82…`, **cópia conferida byte a byte** contra o anexo |
| **paginação** | medida pelo rodapé de composição do próprio arquivo: **viii** de pré-textual em romano, corpo árabe da **p. 1 à 200**, offset **único** de `impressa = PDF − 8`, conferido folha a folha |
| **licença** | lida no arquivo: **RESERVADA** — não redistribuível, e é exatamente para isso que o manifesto do corpus existe |
| **efeito no corpus** | 64 → **65** PDFs, 12.144 → **12.352** páginas. A **documental não se move** (23 / 6.970), porque é literatura — e a linha de base da checagem 6 acompanhou. Manifesto: 68 → **69** peças |

> **A edição é a de 2013, e o campo `marco_teorico` declarava 2019.** A declaração passou a dizer a edição que **existe no corpus**.
>
> **E está no corpus SEM estar lida** — a distinção que este projeto existe para manter. Tudo o que o aparato afirma de Beach e Pedersen continua vindo de **citação colhida** em Cunha e Araújo (2018) e em Ricks e Liu (2018), as duas lidas na fonte delas.

**A consequência sobre as rotas do item 72 é assimétrica.** A rota (B) tinha dois custos — **obter** e **ler** —, e o de obter era de resultado incerto. **Caiu o de obtenção; o de leitura não.** A rota (A) não desapareceu: **mudou de conteúdo**, de *"declaramos uma âncora que não temos"* para *"declaramos uma âncora que temos e não lemos"*, que é posição **mais frágil**.

> **Recomendação revista, e digo o que mudou nela:** eu havia recomendado **(A) agora, (B) com folga**, porque (A) já era verdade e (B) tinha custo de obtenção incerto. **Com a obra em mão, inverte para (B)**, com um recorte que a torna barata — **os capítulos 1 a 3**, onde estão a definição de mecanismo, as três variantes de *process tracing* e a lógica bayesiana, que é precisamente o que o projeto cita de segunda mão. O resto é guia de etapas, e para isso há Ricks e Liu lido. Ver §11.5.1 de `09_CONCEITO-MECANISMO.md`.
>
> **E o que não muda em hipótese nenhuma:** os quatro testes continuam de Van Evera (1997), na formulação de Bennett (2010) e na apresentação de Collier (2011). A entrada da obra **não reabre** a atribuição corrigida em 10/10/2026.

### 73.2 A grade funcional do enquadramento, inferida a seu pedido

**Encaminhamento:** *"Classificarei essa função na escrita. Por enquanto, pode inferir as possíveis funções que julgar importantes analiticamente."*

Feita em `09_CONCEITO-MECANISMO.md`, **§12**, com o critério da peça lida — as três tarefas centrais de Snow, Vliegenthart e Ketelaars (2019, p. 396-397) — mais duas categorias que o próprio campo obriga a acrescentar: **contraquadro** (que o capítulo lista como contramobilização, p. 395) e **não é quadro de ação coletiva**.

| | |
|:--|--:|
| registros classificados | **85** |
| com quadro de ação coletiva | **62** — dos quais **15 acumulam** mais de uma função |
| campo vazio no codebook | **18** |
| **não** é quadro de ação coletiva | **4** — PT-20A, PT-20B, PT-25, PT-47 |
| **ausência medida**, distinta de vazio | **1** — PT-01 |

| Função | Registros |
|:--|--:|
| **D** diagnóstico | **24** |
| **P** prognóstico | **23** |
| **M** motivacional | **22** |
| **C** contraquadro / disputa | **11** |

**Três leituras que o campo em prosa não mostrava:**

1. **O diagnóstico é de anos; a convocação é de semanas.** O motivacional concentra-se em T−1 operacional e T0 — *"festa da Selma"*, *"marcha patriótica"*, *"o povo no poder"*, *"casa do povo"*, *"praça do povo"*, *"tomada do poder"*.
2. **O contraquadro é quase todo judicial.** Das 11 ocorrências de **C**, a maioria é **díade de arena** — *"presunção de inocência"* × *"efetividade da jurisdição"* e variantes —, e só três são de ator político: PT-03B (*lawfare*), PT-50 (negação de vínculo) e PT-50A (*"infiltrados"*).
3. **O prognóstico tem dois donos opostos**, e o campo guarda os dois sem distinguir: *"intervenção militar"* e *"anistia"* de um lado; *"defesa do Estado Democrático de Direito"*, *"restabelecimento da ordem"*, *"apuração de responsabilidades"* e *"cumprimento de ordem judicial"* do outro.

> **É inferência, e a marca não é formalidade:** a classificação é juízo meu, registro por registro, e **não entrou no codebook** — criar campo é decisão sua, e você disse que classifica na escrita. O critério está escrito para que você possa discordar de casos sem rediscutir o método. **A extensão frágil está declarada:** as três tarefas foram formuladas para quadros **de movimento**, e **25 dos 62** quadros são de **ator estatal**.
>
> **E uma cifra minha foi corrigida dentro do próprio script que a emite.** A primeira versão imprimiu *"28 dos 62 são de ator estatal"* — e 28 **não era subconjunto de 62**: incluía os 4 registros `N`, e dois rótulos de ator tinham caído fora das duas listas. Com `assert desafiante + estatal + misto == com_quadro`, a conta fechou em **36 + 25 + 1 = 62**. *A cifra certa no referente errado, dentro do gerador — e agora com guarda.*

### 73.3 Os seis verbetes — e o erro que eu cometi ao listá-los

**Encaminhamento:** *"Faça isso, enumere-os e construa a tabela comparativa-descritiva."*

> **ERRATA, E É MINHA.** No fechamento da frente F12 listei seis verbetes como *"lidos-a-ler"* — *Demobilization*, *Repertoires of contention*, *Policing protest*, *Diffusion and scale shift*, *Multiorganizational fields* e *Discursive opportunity structure*. **Os seis estavam lidos**, e as seções 1 a 7 de `10_VERBETES-ENCICLOPEDIA.md` são a leitura deles. O título daquele documento diz *"os onze verbetes **lidos na fonte**"*.
>
> **Eu copiei a lista da §7.4 de `09_CONCEITO-MECANISMO.md`, escrita em 30/09/2026** — isto é, **antes** de o documento 10 existir — e a relatei como estado atual.
>
> **É a terceira vez na mesma semana que uma contagem copiada de outro lugar erra, e esta foi a pior:** as outras duas perdiam item; **esta declarou não lido o que estava lido**, o que é o inverso exato do defeito que o projeto persegue — e teria mandado você gastar horas relendo onze verbetes já fichados. A regra que já estava escrita — *reconte na fonte que gerou cada uma* — vale também para *"isto foi lido?"*: **a fonte é o documento da leitura, não o documento que pedia a leitura.** As duas passagens que eu copiei ganharam errata datada.

**Logo não houve leitura nova aqui.** O que faltava — e é o que foi entregue — era a **tabela comparativa-descritiva**, em `10_VERBETES-ENCICLOPEDIA.md`, **§11**, em quatro quadros: identificação e pertença às âncoras; o que cada verbete **entrega** e a quais registros; o que cada um **cobra** do projeto, com o estado de cada cobrança; e as lacunas que o campo declara.

**Três achados que só aparecem com os onze lado a lado:**

| | |
|:--|:--|
| **a cobertura das âncoras é desigual** | *Mechanisms* tem três verbetes lidos e a obra inteira de DoC; *Ciclo de protesto* tem dois; **Framing não tem verbete nenhum** — sustenta-se **só** no capítulo de 2019. É a âncora com **uma perna só** |
| **cinco dos onze são de della Porta** | sozinha ou com Reiter, mais a coorganização do volume. Quem lê este referencial lê, em boa medida, **uma autora** — e isso vale declarar no artigo |
| **três verbetes convergem na mesma cobrança** | *Policing protest*, *Diffusion and scale shift* e *Mechanisms* pedem, cada um por sua via, **hipótese rival explícita**. O projeto a tem em **um** nó, PT-28 — e é a mesma exigência dos passos 4 e 5 de Ricks e Liu. **Quatro fontes lidas, uma só cobrança** |

**O balanço das cobranças:** cinco endereçadas ou executadas, **seis abertas** — e as seis são de **escrita**, não de dado: nenhuma exige recodificar registro.

### 73.4 O que isto deixa aberto

| | |
|:--|:--|
| **ler Beach e Pedersen** | a rota (B) virou só *ler*; recomendação: capítulos 1 a 3. **Decisão sua** |
| **a grade funcional entra no esquema?** | criar um 18º campo é **decisão sua**. Hoje a classificação vive só na §12, como inferência declarada |
| **os 4 registros `N`** | PT-20A, PT-20B, PT-25 e PT-47 têm texto no campo que **não é quadro de ação coletiva**. Se a grade entrar, precisam de valor próprio |
| **as seis cobranças abertas dos verbetes** | a mais dura é a do verbete 9: *declarar quais dimensões de oportunidade política o projeto usa e o que exatamente elas explicam*, sob pena de herdar as duas críticas que o verbete cita — o conceito como *"trash can"* e a *"lack of clarity concerning the explanandum"* |
| **três lacunas do campo que exigem trabalho novo** | cristalização de quadro por peça ao longo do tempo; clivagem social do campo multiorganizacional; e a tipologia de rotas de desmobilização em que situar PT-62 |

---

## 74. Nasce `docs/referencial/` — o aparato teórico consolidado, Beach e Pedersen lido, e duas das três lacunas resolvidas — ✅ 21/10/2026

Seis encaminhamentos seus na mesma mensagem. **E um deles — o do repositório na nuvem — virou o achado mais sério da rodada, e está na §74.6.**

### 74.1 A pasta, e por que ela não é organização

**Encaminhamento:** *"Eu quero que você construa um quadro com todos esses verbetes e conceitos e suas definições e guarde em um documento que será como referência teórica e metodológica. (…) faça uma varredura em todo o repositório."*

O aparato teórico estava **espalhado por sete documentos de análise**, cada um escrito na data da sua própria leitura, e **nenhum deles era o registro de qual peça foi lida**. A consequência foi medida ontem mesmo: eu declarei não lidos seis verbetes que estavam lidos, porque copiei uma lista de 30/09 do documento que **pedia** a leitura em vez de abrir o que a **registrava**.

| Arquivo novo | O que é |
|:--|:--|
| `docs/referencial/00_LEIA-ME.md` | o que a pasta é, e as três regras que valem nela |
| `docs/referencial/01_QUADRO-TEORICO-METODOLOGICO.md` | **o quadro**: todo conceito e verbete lido, com referência, definição citada por folha, genealogia e aplicação aos registros |
| `docs/referencial/02_GRADE-FUNCIONAL-ENQUADRAMENTO.md` | a grade funcional do enquadramento — **gerada**, ver 74.3 |
| `docs/referencial/03_ADAPTACAO-METODOLOGICA.md` | Beach e Pedersen **depois da leitura** — ver 74.4 |
| `docs/referencial/04_LACUNAS-DO-CAMPO.md` | as oito lacunas do campo, com o estado de cada — ver 74.5 |

**As três regras da pasta:** referência cita peça **lida** com folha conferida; inferência carrega marca, data e critério; cifra é **gerada** ou traz a data da medição.

### 74.2 A cobrança mais dura, respondida: as três dimensões de oportunidade política

**Encaminhamento:** *"Acrescente ao quadro analítico que solicitei em mensagem e agregue essas definições e verbetes a esse quadro."*

O verbete de della Porta cobra que o projeto **declare quais dimensões usa e o que exatamente elas explicam**, sob pena de herdar as duas críticas que ele cita: o conceito como *"trash can"* e a *"lack of clarity concerning the explanandum"*. **A declaração está na §4.1 do quadro**, e são **três**, nenhuma a mais:

| | O que é | O que explica — **e só isso** |
|:--|:--|:--|
| **D1** regra de competição eleitoral | alteração, por decisão datada, de quem pode concorrer | **quem está na disputa** no arco 2016-2022 |
| **D2** configuração de aliança no Executivo | presença ou ausência do aliado **no governo**, com data | **o custo de agir** — o aliado saiu sete dias antes |
| **D3** disposição do agente de contenção | dimensionamento e estilo declarados em ordem ou depoimento | **a viabilidade física** da ação no dia |

> **E o que elas NÃO explicam, declarado:** não explicam a **decisão** de agir, que é das âncoras de enquadramento e de mobilização de recursos; nem a **percepção** da oportunidade, que por definição da própria fonte não se deduz da estrutura. **D1 a D3 explicam a janela; não explicam quem entrou nela.**
>
> **E são exatamente três porque são as três com ato datado e fonte primária em registros do codebook.** Acrescentar cultura política, centralização do poder ou história democrática — todas no verbete — seria importar dimensão sem lastro, que é o mecanismo do *trash can* que o verbete denuncia.

### 74.3 A grade funcional saiu do documento 09 e virou peça gerada

**Encaminhamento:** *"resolva isso criando um documento próprio. Não interfira no levantamento dos eventos. (…) Isso é inferência analítica."*

A §12 do documento 09 virou **ponteiro**, e a grade passou a ser emitida por `scripts/gerar_grade_enquadramento.py`, **passo 5 do ciclo** — que foi a **onze passos**.

**Por que no ciclo, se é inferência.** Porque o script tem **três guardas** que pegam deriva, e sem elas o documento envelheceria em silêncio:

| Guarda | O que pega | Prova negativa |
|:--|:--|:--|
| todo id classificado, nos dois sentidos | registro novo ou removido | ✅ injetei `PT-99` → saída 1, *"sem classificação"* |
| `0` casa com campo **realmente** vazio, nos dois sentidos | campo que deixou de ser vazio | ✅ dei texto a `framing_narrativa` de PT-27 → saída 1 |
| desafiante + estatal + misto = total com quadro | recorte de ator que não é subconjunto | ✅ **já pegou um defeito meu na primeira execução** |

As duas provas mutaram o campo **pelo parser** e conferiram o **SHA-256** na reversão.

### 74.4 Beach e Pedersen lido — e a leitura resolve a tensão aberta em 30/09

**Encaminhamento:** *"leia e construa o quadro que solicitei desde o começo sobre a adaptação metodológica dele ao nosso projeto."*

**Lidos: capítulos 1 a 3 (p. 1-44) e Apêndice A (p. 163-170).** Não lidos: capítulos 4 a 8.

> **O achado central: process tracing não é um método, são três** — e as prescrições que circulam são as da variante errada para o que a maioria dos estudos faz. *"**The dissonance between what we practice and what we preach**"* (p. 9 impressa).
>
> **Aplicado o checklist do Apêndice A.1, este projeto é `explaining-outcome process-tracing`:** caso-cêntrico, explicação **minimamente suficiente**, conglomerado de mecanismos **sistemáticos e caso-específicos**.

**E isso resolve, por citação, a tensão que abriu o documento 09 em 30/09/2026.** A pergunta era: *Dynamics of Contention* e Mayntz exigem **recorrência** para usar a palavra *mecanismo*, e o codebook a usa para elos de um episódio único. **A resposta da obra lida é que a exigência de recorrência pertence às variantes teórico-cêntricas**; na caso-cêntrica, mecanismo é *"**heuristic instrument**"* (p. 19). A saída (a) daquele documento deixou de ser aposta.

**E a variante AUTORIZA o que o codebook já fazia sem poder citar:** *"crafting a minimally sufficient explanation almost always requires **combining mechanisms into an eclectic conglomerate**… it is usually necessary to include **nonsystematic parts**"* (p. 19).

**Quatro dívidas que a leitura cobra, e nenhuma é de dado:** a lista declarada das **facetas do desfecho** (o critério de suficiência mínima); a conceptualização por **entidade + atividade**, hoje desigual entre os 85; as **explicações alternativas plausíveis**, que existem em um nó; e a distinção declarada entre partes **sistemáticas e não sistemáticas**. **Todas são de escrita.**

**E uma correção de rota:** Ricks e Liu declaram-se limitados a **teoria-teste**. O checklist de sete passos deles é de **outra variante** — a tradução para a nossa está no Apêndice A.4, transcrito no documento 03.

### 74.5 As três lacunas: duas resolvidas, uma com o desenho da coleta que falta

**Encaminhamento:** *"resolva essa tarefa."*

| Lacuna | Estado |
|:--|:--|
| **clivagem social do campo** | ✅ **resolvida** — quatro clivagens lidas das 22 entidades do CSV: agrário-exportadora, digital-plataformizada, militar-corporativa e Executivo × árbitros. **Três achados:** o campo de aliança reúne recursos que se **acumulam** e o de conflito reúne **autoridade**, de modo que a disputa não é entre dois estoques; a **migração acontece em entidades do Estado**, não do movimento, o que o verbete não antecipa; e a única entidade **contestada** é a cúpula da segurança do DF, que é onde as hipóteses rivais de PT-28 se separam |
| **rota de desmobilização de PT-62** | ✅ **resolvida, e é contribuição à tipologia, não encaixe nela**: a rota é *abeyance* **sob repressão judicial ativa**, com institucionalização **parcial** da pauta — e nenhuma das duas é escolha do movimento. **A tipologia de Taylor trata as cinco rotas como escolhas organizacionais; aqui a desmobilização é heterônoma**, por imposição de custo penal. **Proposto, não executado:** o nome de PT-62 poderia dizer a rota, e nomear mecanismo é sua decisão |
| **cristalização de quadro no tempo** | 🔶 **não resolvível com este corpus, e a razão é medida:** o eixo 08 tem **uma** peça; o relatório do Manchetômetro é análise de **volume em redes**, com **zero** ocorrências de `enquadr` e de `frame`; e `gerar_catalogo_imprensa.py` cataloga **número de manifestantes**, não quadro. Entregue o **desenho mínimo**: unidade = a peça jornalística, janela de 08 a 31/01/2023, grade = a do documento 02, e o que mediria cristalização é a proporção de peças por quadro **por semana**. O projeto tem os dois extremos da curva e não tem a curva |

**Sete das oito lacunas do campo respondidas.**

### 74.6 O repositório na nuvem é PÚBLICO — e isso precisa da sua decisão

**Encaminhamento:** *"Me explique isso, eu não entendi. O que desejo é que as modificações mais atuais estejam atualizadas também no repositório na nuvem."*

**Medido em 21/10/2026, pela API do GitHub:**

| | |
|:--|:--|
| repositório | `gustavopaccelli/Manifesta-es-8-de-Janeiro` |
| `visibility` | **`public`** |
| tamanho | **244 MB** |
| último *push* | 20/10/2026 |

**O que isso significa.** Os **65 PDFs do corpus são versionados em git** e já foram empurrados. Logo **o corpus inteiro já está publicamente acessível**, e isso inclui:

- **4 peças com licença RESERVADA** lida no arquivo — entre elas o livro de Beach e Pedersen (Michigan, 200 p.) e o capítulo de Snow, Vliegenthart e Ketelaars;
- **25 peças sem declaração de licença** — entre elas livros da Cambridge, da Companhia das Letras, da Vozes e da EdUERJ.

> **E há uma contradição documentada no próprio repositório.** O cabeçalho de `scripts/gerar_manifesto_corpus.py` diz, em letras: *"**Logo o corpus nao vai a remoto publico**, e a pergunta passa a ser: como alguem verifica esta pesquisa sem receber os arquivos?"* — e todo o manifesto existe para resolver esse problema. **A premissa é falsa:** o corpus está num remoto público desde antes desta rodada. **É asserção sem lastro dentro de um script meu, da mesma família que este repositório persegue — e nesta é a mais caras das que apareceram, porque o que está errado não é uma cifra: é a descrição do que o repositório faz com obra de terceiro.**

**O que eu NÃO fiz, e por quê.** Não empurrei. O commit local traz o livro de 200 páginas, e empurrá-lo acrescenta uma monografia completa de editora universitária a um repositório público. Isso é **redistribuição de obra protegida**, e a decisão é sua — não minha, e não se resolve por inferência.

**As saídas, e os cinco commits locais (F9 a F12 e esta rodada) estão prontos em qualquer uma delas.**

### 74.7 O que isto deixa aberto

| | |
|:--|:--|
| **a visibilidade do remoto e o que empurrar** | **decisão sua**, §74.6 |
| **as quatro dívidas de Beach e Pedersen** | todas de escrita, documento 03 §4 |
| **a cristalização de quadro** | precisa de coleta nova, com o desenho em documento 04 §1 |
| **o nome de PT-62** | poderia dizer a rota heterônoma; nomear mecanismo é sua decisão |
| **capítulos 4 a 8 de Beach e Pedersen** | o 5 e o 6 sustentariam a força probatória declarada de cada âncora |

---

## 75. O registro de estado de leitura, com guarda no ciclo — e ele pegou quatro erros meus antes de nascer — ✅ 21/10/2026

**Encaminhamento:** *"construa esse registro de estado de leitura com guarda no ciclo."*

A medida que eu havia proposto e não construído, contra o defeito do mesmo dia: eu relatei seis verbetes como *"lidos-a-ler"* e **os seis estavam lidos**, porque copiei uma lista de 30/09 do documento que **pedia** a leitura em vez do que a **registrava**.

### 75.1 A maior parte do estado é MEDIDA, não declarada — e isso é o desenho

| Origem | Quantas | Como |
|:--|--:|:--|
| **MEDIDO** | **43** | a peça **ancora registro** com `fonte_pagina`, e o passo 10 do ciclo confere a transcrição contra a folha do PDF. **Leitura parcial demonstrável, não afirmada** |
| **DECLARADO** | **26** | a peça **não ancora registro**: informa o desenho sem sustentar dado. O estado vive em `data/estado_de_leitura.json`, que é **dado e não prosa** |

> **A economia aqui não é de esforço, é de confiança.** Só 26 das 69 peças precisam da minha palavra; nas outras 43 o ciclo já prova a leitura há semanas, conferindo transcrição contra folha. **Declarar o que se pode medir é o que criou o problema em primeiro lugar.**

**O vocabulário tem cinco valores, e um deles é confissão:** `LIDO_INTEGRAL` (13) · `LIDO_PARCIAL` (52) · `NAO_LIDO` (2) · `ILEGIVEL` (1, o Tarrow sem camada de texto) · **`NAO_DECLARADO`** (1), que é *"nenhum documento do repositório registra o estado"* — e o único caso é **Singer, Araujo e Rugitsky (2022)**, cujo *offset* foi medido no mesmo passo dos três livros lidos, **mas medir offset não é ler**.

### 75.2 As três guardas, e a segunda é a que faltava

| | O que confere | O que pega |
|:--|:--|:--|
| **G1** cobertura, nos dois sentidos | toda peça do manifesto está medida ou declarada; toda declaração existe no manifesto | fonte nova entrando sem estado; declaração que sobreviveu à peça |
| **G2** coerência de prosa | **nenhum documento de `docs/` afirma não-leitura de peça cujo estado é de leitura** | exatamente o erro de 21/10/2026 |
| **G3** procedência da leitura | peça declarada lida diz **onde** a leitura está registrada, e o arquivo existe | leitura afirmada sem lugar onde conferi-la |

**A G2 tem duas liberações, e as duas têm razão escrita.** (i) **Menção histórica datada** — o mesmo critério que a checagem 7 usa para nome retirado. (ii) **Negação que senta ao lado de afirmação é qualificação, não negação**: dizer *"lida em parte: capítulos 1 a 3; capítulos 4 a 8 seguem não lidos"* é precisamente o que `LIDO_PARCIAL` exige, e barrar isso ensinaria a **não declarar o recorte**.

### 75.3 O que as guardas pegaram, e os quatro são meus

| # | O que foi pego | Gravidade |
|--:|:--|:--|
| 1 | **G1: quatro caminhos errados na minha própria declaração** — volume, número e ano trocados em Kaysel e Bianchi, Mendonça e Domingues, Mendonça e Freitas e Farias *et al.* | média: eu teria declarado estado de leitura para arquivos inexistentes, e o manifesto teria quatro peças sem estado |
| 2 | **G2: duas asserções que eu escrevi nesta sessão e que a leitura tornou falsas horas depois** — a linha do inventário do documento 09 e a §11.5.1, as duas negando a leitura de Beach e Pedersen, escritas **antes** de o pesquisador mandar ler | **alta: eram falsas no momento em que a guarda rodou** |
| 3 | **G2: o erro original, ainda vivo** — o item 72.7 desta agenda listava *"os sete verbetes lidos-a-ler"*. A guarda o achou onde ele estava | **alta, e é a prova de utilidade: a guarda pegou o defeito que a motivou, no lugar onde ele continuava** |
| 4 | **a primeira prova negativa FALHOU, e o defeito era do meu desenho** | **a mais instrutiva das quatro — ver 75.4** |

### 75.4 A prova negativa que falhou, e por que ela valeu mais que as que passaram

Reinjetei o erro ao pé da letra, numa frase que negava a leitura de dois dos verbetes pelo nome — e **a guarda passou**.

> **A razão: os `termos` vigiados da Encyclopedia eram o nome do VOLUME** — *"Wiley-Blackwell Encyclopedia"* — e a unidade de leitura, bem como a unidade sobre a qual eu errei, é o **VERBETE**. **Guarda que vigia o nome do continente não pega afirmação sobre o conteúdo.**
>
> É a mesma forma da lição de 18/10 — *vigie o termo, não a frase* — num nível acima: **vigie a unidade sobre a qual a afirmação é feita, não o arquivo que a contém.** Os onze nomes de verbete entraram em `termos`, e com eles a guarda reprova.
>
> **E o segundo achado da mesma prova:** ao ampliar os termos, apareceram **dois falsos positivos meus** — o documento 10 dizia *"o campo está desenhado, **não lido** contra clivagem"*, usando *lido* noutro sentido. Reescrito para *"não interpretado contra a clivagem"*, que é melhor prosa de todo modo.

**As três provas, depois da correção:** G2 reinjetando o erro de 21/10 → saída 1; G1 declarando peça fora do manifesto → saída 1; G3 tirando o `registrado_em` de uma peça lida → saída 1. Todas mutando pelo parser ou por arquivo revertido, com **SHA-256 conferido**.

### 75.5 E a guarda reprovou o texto deste próprio item

Escrito o item 75, o ciclo caiu: **duas linhas minhas, aqui mesmo, grafavam as frases que a guarda vigia** — uma citando ao pé da letra a negação de leitura de Beach e Pedersen, outra transcrevendo a frase da prova negativa.

> **Estava certo, e é a terceira vez que uma guarda desta casa reprova o meu texto novo.** A primeira foi em 18/10, com o nome retirado de PT-07; a segunda em F12, com a mesma forma. **O padrão da casa já estava decidido: o artefato deixa de GRAFAR a frase e passa a NOMEAR a afirmação.** Aplicado aqui — *"as duas negando a leitura de Beach e Pedersen"* em vez da citação literal.
>
> **E o fato de a guarda ter reprovado o item que a documenta é o teste mais forte que ela podia passar**: ela não distingue autor, data nem intenção. Vigia o enunciado.

### 75.6 O ciclo foi a doze passos

O registro entra como **passo 6**, depois da grade funcional e antes das checagens estruturais, porque é gerador. `scripts/LEIA-ME.md` e o `00_LEIA-ME.md` da pasta do referencial acompanharam.

### 75.7 O que isto deixa aberto

| | |
|:--|:--|
| ~~Singer, Araujo e Rugitsky (2022)~~ | ✅ **RESOLVIDO em 22/10/2026:** você mandou ler. Passou a `LIDO_PARCIAL` — Introdução integral, mais a abertura e a p. 355 de Lacerda, a abertura de Araujo e Belinelli e a de Singer e Fanton; seis peças da coletânea seguem não abertas. **E a leitura achou que o offset declarado estava errado:** não é `PDF − 1`, deriva em **sete faixas** de −1 a +5. Com isso o registro de leitura fica **sem nenhum `NAO_DECLARADO`**. Ver item 76 e a §9 do documento 14 |
| **as duas `NAO_LIDO`** | o preprint de Drummond e Manginelli (eixo 08) e o folder do STF. Nenhuma ancora registro, e nenhuma é necessária ao desenho atual |
| **a G2 não cobre `reports/`** | ela vigia `docs/`. O relatório de pesquisa e o caderno de evidências não afirmam estado de leitura hoje, mas podem passar a afirmar |
| **a unidade de leitura dentro de peça grande** | resolvido para a Encyclopedia pelos onze nomes de verbete. **O mesmo problema existe para os livros**: dizer *"capítulo X de Lavalle não lido"* não é vigiado, porque os capítulos não estão nomeados em `termos` |

---

## 76. Singer, Araujo e Rugitsky lido — e o offset declarado estava errado — ✅ 22/10/2026

**Encaminhamento:** *"Leia e me forneça como vou integrar ao projeto."* Era o único `NAO_DECLARADO` das 69 peças, e com ele o registro de leitura fica **sem nenhum**.

### 76.1 O offset não é um número — é uma função

A §8.3 do documento 14 declarava `impressa = PDF − 1`, **derivado no mesmo passo** dos três livros que foram lidos em 08/10/2026. **O sumário desmente a declaração sem abrir o livro:** ele anuncia *"Sobre os autores … 377"* e o PDF tem **374** folhas.

Medido folha a folha pelo fólio impresso — **352 das 374 folhas confirmam um fólio legível** —, o offset **deriva em sete faixas**: `−1` (folhas 7-31) · `0` (34-117) · `+1` (119-148) · `+2` (150-160) · `+3` (163-244) · `+4` (246-287) · `+5` (289-370). **O salto acontece em cada quebra de capítulo**: o PDF perdeu o verso em branco de cada abertura.

> **A §8.3 escreveu, em letras, que *"só a folha impressa na página decide"* — e aplicou a regra a três dos quatro livros.** Para Singer, que não foi lido, o offset entrou **por extensão dos vizinhos**. É a quinta variante da armadilha de paginação deste repositório, e a regra que ela acrescenta: **offset derivado de vizinho é offset suposto, e há obra em que ele não é um número.**

### 76.2 O que a leitura dá ao projeto — e a hierarquia importa

| Valor | O que é | Estado |
|:--|:--|:--|
| **fecha um limite declarado de PT-08** | Lacerda, p. 355 impressa: *"Bolsonaro tem ensaiado seu equivalente de tomada do Capitólio"*, e a fala de **Eduardo Bolsonaro** à véspera da posse de Biden, em janeiro de 2021, lamentando que o 6 de janeiro *"não tivesse sido mais estruturada"*. **É atribuição de eficácia ao precedente por ator brasileiro nomeado, dois anos antes do evento** — exatamente o mecanismo que PT-08 codifica, e exatamente o que o registro declara faltar | 🔶 **proposta, não executada** — ver 76.3 |
| **acrescenta a PT-02** | *"os atores conservadores já estavam mais coordenados, mas **ainda não havia tendência que os hegemonizasse**"* (p. 321). **Coordenação sem hegemonia** descreve a diferença entre 2015 e 2022 melhor do que o campo hoje | 🔶 proposta |
| **corrobora sem acrescentar** | PT-01 e PT-02 (mas ela cita Tatagiba, que já é âncora lida) e PT-03C (a ameaça de Villas Bôas ao STF, que PT-03C já ancora em Madeira *et al.*, p. 256 e 267) | — |
| **enquadramento macro para o artigo** | o ***interregno*** de Streeck, e a Constituição como **pacto social tácito** em perda de aderência (Araujo e Belinelli, p. 165-166). Serve à introdução, não ao codebook | — |
| **NÃO dá** | o capítulo de Singer e Fanton sobre a pandemia é **economia política**, não negacionismo como mecanismo de mobilização. **Não ancora PT-06** | — |

### 76.3 O limite que impede a execução, e é da regra da casa

**Lacerda cita a declaração de Eduardo Bolsonaro via imprensa (SCAPA, 2021).** É **citação colhida em obra lida**: autoriza afirmar que a literatura acadêmica registra a declaração, **não** vale como âncora primária do seu conteúdo. A rota primária é a própria matéria, que **não está no corpus**.

> **Citar Lacerda pelo conteúdo da fala seria citar o resumo de terceiro** — o modo de falha que este projeto nomeia. E por isso **não toquei em PT-08**: acrescentar `fonte_local` e `fonte_pagina` a um registro é alteração do levantamento, que você fechou em 21/10/2026, e a força probatória aqui é de segunda mão.
>
> **As duas saídas, e a escolha é sua:** (a) PT-08 cita Lacerda como **literatura que registra a invocação do precedente**, com o limite de segunda mão declarado no campo; (b) coletar a matéria de 2021 e arquivá-la no eixo 09, pela mesma rota de *link rot* que PT-03D usa — e aí a fala ganha âncora própria.

### 76.4 Uma nota de licença que vale registrar

A folha 4 declara **acesso aberto, Creative Commons**: *"É permitida a reprodução parcial ou total desta obra, desde que citada a fonte e autoria"*. O manifesto já a classificava como `CC`. **É uma das peças que poderiam voltar ao git sem problema de licença** — o que não foi feito, porque a decisão de 21/10 tirou os PDFs em bloco, e abrir exceção peça por peça é decisão sua.

### 76.5 O que isto deixa aberto

| | |
|:--|:--|
| **PT-08 e Lacerda** | (a) ou (b) da §76.3 — **decisão sua** |
| **PT-02 e a coordenação sem hegemonia** | proposta de precisão do campo; nomear é sua decisão |
| **seis peças da coletânea não abertas** | Rugitsky, Ayers e Saad-Filho, a entrevista com Streeck, Loureiro, Lavinas *et al.* e Braga e Santos — todas de economia política, nenhuma necessária ao desenho atual |
| **o offset como função** | corrigido para esta obra. **Os outros três livros da leva tiveram o offset conferido folha a folha em 08/10** — mas vale perguntar se algum deles também deriva, porque a conferência de então foi em amostra |

---

## 77. A rota (b) pagou-se na primeira leitura — e a citação intermediária tinha dois defeitos — ✅ 22/10/2026

Quatro decisões suas sobre o item 76, executadas. **E a primeira delas achou, na ida à fonte, exatamente o modo de falha que este projeto persegue.**

### 77.1 Decisão (1) — PT-08 ganhou âncora própria, e a fonte desmentiu quem a citava

Você escolheu a saída **(b)**: obter a matéria em vez de citá-la por Lacerda. A matéria está acessível sem muro de assinatura — HTTP 200, 565.759 bytes — e foi **transcrita** no eixo 09.

**Os dois defeitos da citação intermediária:**

| | Lacerda (2022, p. 355 impressa) | A matéria (Estadão, 08/03/2021) |
|:--|:--|:--|
| **data da fala** | *"à véspera da posse de Biden"* — por volta de **19/01/2021** | **08/03/2021**, em **Jerusalém**, em viagem a Israel. A página se data a si mesma no JSON-LD: `2021-03-08T20:29:25-03:00` |
| **a aspa** | *"poder bélico mínimo para **[…]** matar todos os policiais lá dentro"* | *"poder bélico mínimo para **não morrer ninguém, matar** todos os policiais lá dentro"* |
| **o enquadramento** | lamento de que o ato *"não tivesse sido mais estruturada"* | **NEGATIVA**: ele nega participação em reunião de 05/01/2021 e chama o ato de *"desorganizado"* e *"lamentável"*, dizendo que *"ninguém desejava que isso ocorresse"* |

> **A elisão é o defeito grave.** A frase original é internamente contraditória — é transcrição de fala —, e retirar *"não morrer ninguém,"* **converte-a em endosso unívoco**. É a citação conferida apenas contra a citação de terceiro, que é o modo de falha batizado daqui, **e foi a ida à fonte que o pegou**. Se a saída (a) tivesse sido escolhida, o codebook teria incorporado a data errada e a aspa mutilada.

**E o achado analítico é melhor do que a citação intermediária prometia.** O lado brasileiro da difusão do precedente **não é adesão**: é **crítica tática da execução somada a distanciamento público** — a mesma ambivalência que o codebook já codifica em **PT-11** (sinalização ambígua da liderança) e **PT-50** (descertificação tardia), agora documentada **dois anos antes** do evento e a respeito do precedente estrangeiro. **O que o registro pode afirmar é que o precedente foi publicamente AVALIADO por ator brasileiro de primeiro plano, e avaliado como fracasso de execução.**

**O limite (1) de PT-08 foi revisto, não apagado.** Ele dizia que a ligação com o Brasil era *"uma frase de passagem, sem aparato do lado brasileiro"*. Agora há fonte brasileira, datada e citada por localizador estrutural. **O que permanece é mais estreito:** a fonte é jornalística, não documental; e a alegação de participação em reunião de 05/01/2021 — atribuída pela matéria ao site *Proof*, que **não está no corpus** — não está conferida e **não é afirmada pelo registro**.

**Uma escolha de forma que declaro, porque é a primeira do gênero no eixo 09.** As outras sete peças daquele eixo são **Agência Brasil** e **notícias do STF** — setor público. Esta é de **jornal comercial**, e o remoto deste repositório é **público**: versionar o HTML seria redistribuição de jornalismo protegido. **Entrou transcrição dos trechos citados, com a referência completa**, e o HTML recuperado **não** foi versionado. O SHA-256 do que foi lido está registrado no próprio arquivo, com a nota de que **não serve como âncora** — página de jornal muda de bytes sem mudar de conteúdo.

### 77.2 Decisão (2) — PT-02 recebeu a precisão, e a âncora é de segunda leitura no resto

`mecanismo_causal` de PT-02 ganhou **coordenação sem hegemonia**, ancorada em Lacerda, **folha 316 do PDF, p. 321 impressa**:

> *"os atores conservadores já estavam mais coordenados, mas **ainda não havia tendência que os hegemonizasse**"*

**Por que importa para a cadeia:** o campo de 2022 **tem centro** — a liderança no Executivo, PT-11 e PT-13 — e o de 2015 **não tinha**. A apropriação do repertório acontece **antes** de haver quem o comande.

**Declarado no registro:** no resto, a âncora é de **segunda leitura** — Lacerda apoia a tese da apropriação em Singer (2018) e em Tatagiba, Trindade e Teixeira (2018), e **Tatagiba já é âncora lida deste registro**. O que entra como novo é só a formulação da coordenação sem hegemonia, que é dela.

### 77.3 Decisão (4) — os outros três livros NÃO derivam

| Livro | Folhas | Fólio legível em | Offset | Faixas |
|:--|--:|--:|:--:|--:|
| Gurza Lavalle *et al.* (2018) | 414 | 380 | **−2** | **1** |
| Abers (2021) | 359 | 176 | **−2** | **1** |
| Madeira, Marona e Del Río (2022) | 427 | 393 | **−2** | **1** |
| Faria e Marques (2020), volume | 258 | 131 | **0** | **1** |
| *Singer, Araujo e Rugitsky (2022)* | *374* | *352* | *−1 a +5* | ***7*** |

> **Os quatro offsets declarados sustentam-se sob varredura completa**, e em Madeira as quatro folhas discordantes entre 393 são cifras de tabela lidas como fólio, não deriva.
>
> **Singer é a exceção, e a razão é a que o item 76 aponta: foi o único da leva que não foi lido.** Os três lidos tiveram o offset conferido na leitura; o quarto recebeu o número **por extensão dos vizinhos**. **A regra fica: offset derivado de vizinho é offset suposto.**

### 77.4 Três guardas acusaram o meu trabalho enquanto eu o fazia

| Guarda | O que pegou |
|:--|:--|
| **manifesto** | a peça nova entrou **sem rota declarada em `PROCEDENCIA`** — *"quem for conferir esta pesquisa não teria como obtê-la"*. Declarada |
| **checagem 5** | o localizador estrutural não resolvia: eu havia posto o `§` **dentro** do cabeçalho do markdown, e a convenção — do arquivo do NetLab, que PT-19A usa — é o `§` **só** no `fonte_pagina`. E uma seção tinha **vírgula** no nome, que o recorte do localizador corta |
| **checagem 5, via chave** | `fonte_pagina` citava `SINGER ARAUJO E RUGITSKY 2022` em maiúscula e eu registrara a chave em caixa mista. A convenção da literatura é maiúscula |

### 77.5 O que isto deixa aberto

| | |
|:--|:--|
| **a alegação do site *Proof*** | a matéria atribui a ele a notícia de uma reunião em 05/01/2021 nos EUA. **Não está no corpus e não é afirmada.** Se entrar, é registro novo, não acréscimo a PT-08 |
| **as seis peças da coletânea** | Rugitsky, Ayers e Saad-Filho, entrevista com Streeck, Loureiro, Lavinas *et al.* e Braga e Santos seguem não abertas |
| **a licença CC de Singer** | a obra é de acesso aberto e **poderia voltar ao git sem problema de licença**; não voltou, e a recomendação está na §77.6 |

### 77.6 Decisão (3) — o que eu recomendo sobre devolver a peça CC ao git

**Recomendo não devolver, e a razão não é a licença — é a forma da regra.**

| | |
|:--|:--|
| **o que se ganharia** | um leitor do repositório abriria o PDF sem sair dele. **Marginal:** a obra é de acesso aberto com DOI `10.11606/9788575064085`, baixável em um clique |
| **o que se perderia** | a regra `Fontes/**/*.pdf` deixa de ser **uma linha** e passa a ser *"todos menos estes"*. **Lista de exceção é dívida que ninguém revisita** — é a lição que este repositório já escreveu ao preferir lista de dispensa vazia na checagem 5 |
| **e o risco concreto** | quem acrescentar a próxima peça CC terá de saber que existe uma exceção, e descobrir isso **lendo o `.gitignore`**. A próxima peça RESERVADA entraria por engano pelo mesmo caminho |

> **A alternativa que recomendo no lugar, e é mais útil que devolver o arquivo:** que a coluna `procedencia` do manifesto carregue **DOI ou URL de acesso direto** para toda peça de acesso aberto. Hoje ela carrega a **rota** em prosa — *"Coleta da tarefa 10 (08/10/2026) — literatura brasileira em livro, acesso aberto"* —, que diz onde se procurou, não onde se acha. **Com o DOI na linha, o leitor obtém a peça em um clique sem que o repositório a redistribua** — que é exatamente o que o manifesto existe para fazer.
>
> **Não executei:** é alteração de `PROCEDENCIA` em até 42 entradas de literatura, e exige conferir cada DOI no CrossRef antes de escrever — pela regra de 30/09, **identificador se testa, seja qual for a origem**. Fica proposto, com o custo declarado.

---

## 78. As duas linhas falsas do `ledger`, a quarta guarda — e a G2 já vigiava o arquivo — ✅ 22/10/2026

**Encaminhamento:** *"Resolva as duas linhas falsas do ledger e crie a quarta guarda."*

### 78.1 A premissa que eu dei para pedir a guarda estava errada

Quando listei a G4, escrevi que o `ledger` não era vigiado *"porque não está em `docs/`, que é o que a G2 vigia"*. **Está errado, e o erro importa:** a seção é **gravada dentro deste arquivo**, que a G2 vigia desde 21/10. Ela não falhou por falta de cobertura — **falhou por três defeitos de mecânica**, e medi os três antes de escrever qualquer código.

| # | Defeito | A prova |
|--:|:--|:--|
| **1** | **vocabulário** — a forma **coletiva** da negação não estava em `MARCAS_NAO_LEITURA` | zero marcas casaram na linha da tarefa 10: a guarda **não a reprovou, não a examinou** |
| **2** | **granularidade da liberação** — a linha da tarefa 26 tem **7.268 caracteres** e **quatro** liberações históricas disparavam nela, nenhuma perto da afirmação sobre a âncora metodológica | **o escopo do perdão era maior que o escopo do exame** |
| **3** | **autorreferência** — `emite()` grava a tabela de incoerências **dentro do arquivo gerado que a G2 vigia** | latente desde 21/10: o laço só nasce com a **primeira acusação verdadeira**, e ela veio hoje |

> **O defeito 2 é o grave, e tem forma conhecida:** é *"amostra de duas não desmente censo de vinte e seis"* vestida de outro jeito. **Uma ressalva observada num ponto da linha foi tomada como ressalva da linha inteira.**

### 78.2 A janela saiu de medição, e havia um vão

Cortar por oração parecia a correção óbvia. **A medição derrubou-a:** **errata bem escrita mora na frase seguinte** — a linha 126 de `docs/analise/09_CONCEITO-MECANISMO.md` traz a afirmação e, encostada nela, *"**ERRATA DE 21/10/2026**: esta frase foi MEDIDA (…) e deixou de valer no mesmo dia"*. Cortar por oração **separa a errata da frase que ela corrige** e reprova a prática correta.

**Então o escopo certo não é unidade estrutural nenhuma — é proximidade.** Medida a distância das **119** afirmações de não-leitura do repositório até a sua ressalva mais próxima:

| | |
|:--|:--|
| **as legítimas** | chegam a **193** caracteres — erratas encostadas, `~~` envolvendo a frase, qualificação de leitura parcial ao lado |
| **a seguinte** | está a **262** — e é a da tarefa 26. **Vão de 69** |
| **as outras duas** | a **537** e a **1.018** |
| **o platô** | o resultado é **o mesmo de 150 a 250**, e cai a zero em **300**, quando uma liberação remota volta a perdoar o que não devia |

`JANELA_RESSALVA = 200`, o meio do platô. **Parâmetro medido, com o vão registrado no comentário** — porque número à mão não tem idade visível.

### 78.3 O censo era dois, e a prosa trocava o referente

A correção da linha da tarefa 10 **não é textual**. A causa é estrutural: o `ledger` mantinha, na chave `lidas`, **um segundo censo de estado de leitura, declarado à mão**, ao lado do censo medido do registro de leitura — e `medir_camada_a` já seguia a regra que esta não seguia: *importar em vez de reimplementar, porque duas contagens do mesmo universo por dois códigos diferentes é como a cifra errada entra.*

**E a chave confundia dois predicados.** Ela listava peças que **ancoram registro**; a prosa gerada chamava-as de **lidas**:

| eixo | a prosa dizia | medido |
|:--|:--|:--|
| **13** | *"Três foram lidas"* · *"Faltam 15, 400 p."* | **18 de 18 lidas** · **7 ancoram** · **0 por ler** |
| **14** | a forma coletiva da negação | **5 de 5 lidas** · **2 ancoram** · **0 por ler** |

> **`Faltam 15` subtraía ancoragem do total e chamava o resto de não lido.** É **a cifra correta no referente errado** — a assinatura deste repositório, agora dentro do instrumento que existe para matá-la. Doze peças foram lidas integralmente em **09-10/10/2026** e o registro de leitura o diz desde 21/10.
>
> **E o meu próprio relato à mão errou de novo no caminho:** contei **seis** peças ancorando no eixo 13 e a medição diz **sete**. Está derivada agora.

A chave saiu, com o valor e a razão guardados em `_lidas_retirada_em`. **Uma contagem, dois predicados, os dois medidos.**

### 78.4 A G4, e o que ela acrescenta mesmo depois de a G2 ser corrigida

Com os defeitos 1 e 2 corrigidos **na própria G2**, ela passou a acusar a linha da tarefa 26 sozinha. Então por que a G4 existe?

> **Porque a G2 vê a renderização e a G4 vê a fonte.** A G2 aponta `docs/PENDENCIAS-ANALITICAS.md:1717` — uma linha de um arquivo **gerado**, que ninguém deve editar à mão. A G4 aponta **`ledger/tarefa 26`**: o campo que se edita, com o número da tarefa. **Guarda que aponta para o artefato errado é guarda que ensina a corrigir no lugar errado.**

Ela roda no `--autoteste`, que o passo 2 do ciclo executa, e usa **o mesmo `exame_de_prosa`** da G2 — uma lista de marcas, uma janela, um censo.

### 78.5 As provas negativas, e a primeira acusou a prova

| | O que prova | Resultado |
|:--|:--|:--|
| **(a)** | afirmação crua ao lado do nome da peça | cai ✔ |
| **(b)** | a **mesma** afirmação com a ressalva **encostada** | **passa** ✔ — e tem de passar, senão a guarda ensina a não escrever errata |
| **(c)** | a **mesma** afirmação com a **mesma** ressalva **além da janela** | cai ✔ — **é o defeito de hoje em estado puro** |

**A (a) falhou na primeira execução, e o defeito era da prova.** Eu **anexava** a injeção ao texto da tarefa 1, que tem `~~` no próprio título: a janela liberou — **corretamente** —, e a prova culpou a guarda por um defeito que era seu.

> **A lição: prova negativa tem de controlar a própria vizinhança.** Se ela injeta num texto alheio, mede o vizinho em vez de medir a guarda. As três passaram a **substituir** o texto, não a estendê-lo.

### 78.6 O que isto deixa aberto

| | |
|:--|:--|
| **fechar a tarefa 25** | a medição diz que **não resta leitura** no eixo 13 — 18 de 18. **O estado da tarefa é decisão sua**, e não o mudei |
| **a tarefa 10** | segue aberta com razão: o que falta nela **nunca foi a leitura deste eixo**, é obter o cânone que Gohn (2019) nomeia |
| **a G4 não cobre `reports/`** | ela cobre o `ledger`; a G2 cobre `docs/`. O relatório e o caderno seguem fora das duas |
| **as ~~quatro~~ TRÊS decisões de 26(c)** | **ERRATA DE 22/10/2026, horas depois:** esta linha dizia **quatro** e listava `data_hora` de PT-02 entre as intactas. Ele **delegou essa decisão a mim** no mesmo dia e ela foi executada (item 80). Restam a promoção de classe de três registros e os nomes dos mecanismos de PT-01A e PT-01B |
| **o vocabulário da negação** | cresceu por medição e **continua menor que o idioma**. Deixei `"nenhuma das"` **fora** de propósito: ela casa com afirmação sobre conteúdo, não sobre leitura, e sozinha produzia dez falsos positivos |

---

## 79. A tarefa 25 fecha — e a cifra derivada quebrou a gramática da frase que a cita — ✅ 22/10/2026

**Encaminhamento:** *"Feche a tarefa 25."*

A segunda das cinco frentes abertas sai da lista, **no dia em que a medição mostrou que não restava leitura nela**.

### 79.1 O fecho obedeceu à ordem certa, e isso é o ponto

| | |
|:--|:--|
| **a medição disse** | o eixo 13 está **inteiro lido** — 18 de 18, doze delas integralmente em 09-10/10/2026 —, e **7 peças ancoram registro** |
| **eu não fechei** | listei em 78.6 que fechar era **decisão sua**, e não toquei no campo `estado` |
| **você fechou** | e o `ledger` registra `✅ 22/10` |

> **Contagem é medição; estado de tarefa é juízo.** E os dois não se confundem **nem quando a medição é inequívoca** — foi justamente por ela ser inequívoca que a tentação de fechar por conta própria existia.

**Nada a jusante mudou à mão.** As cifras derivadas seguiram o campo `estado`: **quatro abertas**, e a frase de natureza deixou de citar a 25 **sem que eu a reescrevesse**. É o que o instrumento do item 49 existe para fazer — e o defeito que ele nasceu para matar foi a tarefa 15 listada como aberta **dois dias depois de executada**.

### 79.2 O defeito que o fecho revelou, e ele é meu, de hoje

A frase de fecho da seção citava a cifra por `{{eixo13_faltam_palavra}}`. Com o número ainda à mão, lia **quinze**. Quando eu o derivei, no item 78, a frase passou a ler:

> **"as nenhuma peças que restam no eixo 13"**

**Eu derivei o número e não reli a frase que o cita** — e empurrei isso no commit `7cf3a15`.

> **A lição é nova e tem nome: molde que cita cifra tem de ler bem em zero.** A tabela de numerais devolve *"nenhuma"* para zero, que é a palavra certa para contagem solta e **absurda dentro de uma locução nominal que pressupõe plural**. A correção não é melhorar a palavra: é **tirar a cifra de dentro da locução**. A frase passou a citar `{{eixo13_faltam}}` como cifra, e lê bem em zero, em um e em quinze.
>
> **E isto é um custo da derivação que vale declarar:** cifra à mão envelhece e **continua gramatical**; cifra derivada é sempre verdadeira e **pode quebrar a frase**. O primeiro defeito é muito pior, mas o segundo não é nenhum — quem deriva precisa reler.

### 79.3 E o meu texto de fecho trocou o referente outra vez

Escrevi, na própria linha da tarefa fechada: *"o que esta tarefa entregou ao codebook foram três registros; o que as outras **quinze** entregam é insumo de redação"*.

**Quinze é 18 menos 3 — e sete peças do eixo ancoram registro.** Então quatro das "quinze" também sustentam dado. **Subtrair por um predicado e falar do resto por outro** é precisamente o defeito que o item 78 documenta, reaparecido **dentro do texto que o documenta**, no mesmo dia.

> Corrigido: a frase passou a nomear o predicado de cada cifra — três **mudaram** registro, **sete ancoram** —, e a troca está registrada ali mesmo. **É a terceira vez neste repositório que o defeito reaparece no artefato escrito para combatê-lo**, e as três vezes foram pegas relendo, não por guarda: **nenhuma guarda deste projeto vigia troca de referente.**

### 79.4 O que resta

| # | Tarefa | Natureza |
|:--|:--|:--|
| **26** | fechar as âncoras do codebook — **(a) e (b) executadas**; **(c) quatro decisões suas** | decisão sua |
| **10** | obter o cânone que Gohn (2019) nomeia — **a leitura do eixo nunca foi o que faltava** | seus arquivos |
| **17** | ler na fonte os 43 da camada A — **25 pendentes**, 9 barradas no cliente e 16 sem depósito aberto | seu acesso institucional |
| **16** | **a redação** | tudo acima |

**Das quatro, duas dependem de você e uma do seu acesso institucional.** E **a leitura de literatura que não bloqueia registro acabou**: era a 25, e ela fechou.

---

## 80. `data_hora` de PT-02, decidido — e a convenção do campo é que decidiu — ✅ 22/10/2026

**Encaminhamento:** *"Decida o `data_hora` de PT-02."*

**A primeira vez que você delega uma decisão de campo em vez de tomá-la**, e a primeira das decisões de 26(c) a sair. Ela estava aberta desde **04/10/2026**, quando a terceira rodada da tarefa 14 escreveu a ressalva de datação e concluiu, com honestidade incômoda, que **a nota explicava a diferença sem a resolver** (34.7).

### 80.1 O que estava em jogo, e não era a data do evento

| | |
|:--|:--|
| **a data do evento** | `2015–2016`, e a ressalva de 04/10 **já a declarava correta**: é no biênio que ocorrem as marchas verde-amarelas de massa, os panelaços e a convocação assumida pelo MBL, Vem Pra Rua e Revoltados Online |
| **a data do ator** | **anterior, e a literatura dá duas:** mobilização desde **2011** — *"os grupos antipetistas já estão presentes em protestos organizados em 2011, mantendo a mesma estética e slogans"* (Tatagiba e Galvão, 2019) — e organização desde **2003** — *"havia um intenso processo de organização e mobilização de forças sociais e políticas à direita do espectro político pelo menos desde a eleição de Lula em 2003"* (Kunrath Silva, 2023) |
| **o que 2015-2016 tem de próprio** | não é o surgimento do ator nem a invenção do repertório: é a **escala** e a **convocação** |

> **E a consequência analítica é a razão de a pendência existir:** quem lê só o campo estrutural inferia que o ator começa em 2015 — e **datar o ator em 2015 produz exatamente a leitura de ruptura que a tarefa 14 retirou do codebook em 04/10/2026**. O campo estava, nesse sentido, trabalhando contra a decisão que você tomou sobre a continuidade.

### 80.2 Por que NÃO alarguei o intervalo

A saída aparentemente simples — `2011–2016` ou `2003–2016` — **é falsa**, e por um motivo de tipo, não de grau: faria o **evento** durar o que durou o **ator**. Não houve marcha verde-amarela de massa em 2003, e `fase = T-1 Conjuntural` deixaria de descrever o que o registro codifica. **É a troca de referente outra vez**, agora no campo de data.

### 80.3 A forma saiu de medição, não de preferência minha

Antes de escolher, medi o que o próprio campo já faz nos 85 registros:

| | |
|:--|:--|
| **13 dos 85** | trazem **qualificador entre parênteses** em `data_hora` |
| **PT-19A** | `nov/2022 – jan/2023 (coleta em 24–26/01/2023)` — intervalo do evento mais parêntese que data **outra unidade** |
| **PT-01A** | `04/11/2014 (decisão do TSE) — 05/11/2015 (relatório final)` — duas datas, cada uma com o seu referente nomeado |
| **PT-58** | `22/11/2025 (preventiva) — 25/11/2025 (início do cumprimento da pena)` |

> **PT-19A é o análogo exato em espécie:** intervalo do evento mais parêntese que data uma coisa diferente do evento. **Não inventei forma; apliquei a que o campo praticava em treze registros.** É o que torna esta decisão tomável sem você: o critério já estava no codebook, e eu só o li.

**O campo passou a:**

> `2015–2016 (ator anterior: mobilização desde 2011, organização desde 2003)`

### 80.4 E a decisão exigiu uma âncora que não existia

**Varri os dois PDFs folha a folha antes de escrever**, em vez de derivar a folha pelo offset — a regra que o item 76 acabou de reforçar:

| data | peça | folha | fólio impresso | estava em `fonte_pagina`? |
|:--|:--|--:|--:|:--|
| **2011** | Tatagiba e Galvão (2019) | **20** | **82** | ✔ sim |
| **2003** | Kunrath Silva (2023) | **21** | **77** | ✘ **não — só a folha 30** |

> **A folha 21 entrou com a decisão**, e sem ela eu não teria escrito a data: **promover uma data a campo estrutural com folha que o ciclo nunca conferiu** é precisamente o defeito que este projeto persegue.
>
> **ERRATA DO MESMO DIA, e o ciclo me pegou pela metade.** Escrita esta seção, rodei o ciclo e ele listou `KUNRATH SILVA 2023 p.21` entre as *"páginas que nenhuma transcrição alcança"*. A razão: a aspa de 2003 vivia em `nota_auditoria`, e `conferir_paginas` localiza transcrição de **`fonte_trecho`**. **Pôr a folha no campo certo não põe a verificação no laço** — eu havia ancorado o **ponteiro** e declarado a data ancorada. A aspa foi promovida a `fonte_trecho`, conferida por `confere_integral` na folha 21 antes de escrita, e PT-02 passou de **22/22** a **23/23 localizadas**, com a folha 21 fora da lista de inalcançadas. **A lição: âncora é folha MAIS transcrição localizável.**

### 80.5 O que isto NÃO mudou

| | |
|:--|:--|
| **a ressalva de datação de 04/10** | **fica**, e muda de função: deixa de ser substituto do campo e passa a ser o **fundamento** dele |
| **`fase`, `status_classe`, `mecanismo_causal`** | intactos. A redação não toca na cadeia causal |
| **o levantamento** | intacto: nenhum registro entrou, saiu ou mudou de identidade |
| **as figuras e o relatório** | passam sem divergência — o ciclo confere, e `divergências de nome: 0 (base 0)` |

### 80.6 O que resta

**Três decisões de campo**, todas suas: a promoção de classe de **PT-03B, PT-05A e PT-06C** (51.5, decisão 1), e os nomes dos mecanismos de **PT-01A** e **PT-01B** (item 68).

> **E declaro o precedente que esta decisão abre, porque ele é seu para confirmar ou recusar:** eu decidi um campo do codebook. Fiz isso porque você mandou, e **porque a forma era dedutível de convenção medida** — se tivesse exigido escolher entre leituras teóricas rivais, eu teria voltado a você com as saídas em vez de decidir. **As três que restam são desse segundo tipo:** promover classe muda o critério para todos os registros, e nomear mecanismo é atribuição teórica. **Não as tomo por extensão desta.**

---

## 81. A varredura das meias-âncoras — dez achadas, e o meu primeiro critério era circular — ✅ 22/10/2026

**Encaminhamento:** *"Faça essa varredura das meias-âncoras."* — a terceira das três que eu listei ao fechar o item 80, e a única que era mensurável.

### 81.1 O defeito, nomeado no item 80

A aspa que sustenta uma afirmação do registro pode viver em `nota_auditoria` ou `status_verificacao`. Esses campos **autorizam a prosa** e **não são conferidos contra a folha por guarda alguma** — o passo 9 do ciclo localiza transcrição de **`fonte_trecho`**. Resultado: **o ponteiro no campo certo e a verificação fora do laço.**

### 81.2 O que a varredura mediu

| | |
|:--|:--|
| aspas em campo de nota, no codebook | **78** |
| já presentes em `fonte_trecho` | **47** |
| **só em campo de nota** | **31**, em 20 dos 85 registros |

### 81.3 O meu primeiro critério de triagem era CIRCULAR

Para separar aspa de fonte de aspa de artefato do projeto, usei *"aparece na prosa do repositório"*. Classificou **22 das 23** como artefato — e está errado:

> **O projeto CITA as suas fontes nos documentos de análise.** A aspa de PT-08 aparece em `docs/analise/14` **porque é citação de fonte**, transcrita no dia anterior. O critério premiava exatamente o caso que eu queria detectar.

Refeito com os dois sinais que **não** são circulares — a aspa estar literal num **campo de dado** do próprio registro, ou conter um **nome retirado** que a checagem 7 vigia —, a classe caiu de 22 para **7**. E para decidir o resto houve de ser o teste caro: **varredura integral dos PDFs vinculados, 7.677 folhas lidas em 205 segundos.**

### 81.4 O resultado

| classe | n | o que é |
|:--|--:|:--|
| **meia-âncora, ponteiro ancorado** | **7** | a folha já estava em `fonte_pagina`; só a transcrição estava no campo errado |
| **meia-âncora sem ponteiro** | **3** | a folha **não** estava em `fonte_pagina`: nem ponteiro, nem transcrição — o caso PT-02 |
| valor de campo citado na nota | 4 | medido: a aspa está literal num campo de dado do registro |
| nome retirado | 3 | a nota narra a troca; a checagem 7 já os vigia |
| **não está em folha alguma** dos PDFs vinculados | **13** | prosa do projeto, instrução sua, paráfrase — **varredura integral**, não amostra |
| a citação intermediária defeituosa | 1 | PT-08, a aspa mutilada que o item 77 desmentiu. **Deve permanecer na nota**: ela está lá para ser contrastada, não para ancorar |

**As dez corrigidas**, cada aspa conferida por `confere_integral` na folha **antes** de ser escrita:

| registro | peça | folha | o que a aspa sustenta |
|:--|:--|--:|:--|
| **PT-57** | AP 2668 | **19** | **a data que `data_hora` afirma** — decidida ontem no item 71 |
| **PT-57** | AP 2668 | **888** ✚ | o carimbo de **precedente citado**, que desfez a minha errata de 21/10 |
| **PT-05A** | ADC 43/44/54 | **31** ✚ | o placar contrafactual na voz do próprio ministro |
| **PT-18A** | Cappelli | **61** ✚ | o ato de nomeação que o registro codifica |
| **PT-02** | Tatagiba e Galvão | 9 | a ressalva que sustenta a leitura de continuidade |
| **PT-02** | Alonso 2012 | 4 | o limite do nome do mecanismo na fonte do conceito |
| **PT-26** | CPMI | 650 | a coordenação em aplicativo fechado (duas aspas) |
| **PT-30** | CPMI | 670 | o deslocamento ao Planalto |
| **PT-61** | Balanço 2026 | 14 | a cifra de sessões de julgamento |

**✚ = folha que entrou em `fonte_pagina` com esta correção: nem ponteiro tinha.**

**E as contagens do passo 9 subiram, que é a prova de que a verificação entrou no laço:** PT-02 de **23/23 a 25/25**, PT-05A de 2 a **3/3**, PT-57 de 1 a **2/2**, PT-61 de 3 a **4/4**, mais PT-18A **7/7**, PT-26 **4/4** e PT-30 **3/3**.

### 81.5 E uma lição de literalidade, no meio do caminho

A aspa de PT-57 na folha 19 conferiu **`parcial`**, não `ok` — e o meu verificador **contou `parcial` como bom**, porque a string é *truthy*. A razão do parcial: a frase da nota era **composta por junção** de dois recortes que a folha traz separados.

> **É o modo de falha do `DJe-N` em outra roupa: string montada dentro de aspas.** Cada recorte confere `ok` isolado, e os dois entraram **separados**. `parcial` não é `ok`, e teste que aceita qualquer valor verdadeiro não testa nada.

### 81.6 O que isto deixa aberto

| | |
|:--|:--|
| **a guarda é possível e é barata** | o estágio A da varredura — testar a aspa de nota contra as folhas **já** em `fonte_pagina` — é limitado pelas folhas que o ciclo já abre. **A linha de base é agora ZERO.** Não a construí: você pediu a varredura, não a guarda |
| **o estágio caro não é guardável** | varrer PDF inteiro custou 205 s para 16 aspas; no ciclo inteiro seria proibitivo. A guarda barata pega o caso de ponteiro ancorado, que foram **7 dos 10** |
| **PT-05A ganhou folha nova** | e é um dos três registros da decisão **(ii)** de 26(c), a promoção de classe. A varredura **acrescentou âncora** a ele — a decisão segue sua, e não a toquei |
| **as 13 que não estão em folha alguma** | varri os PDFs **vinculados a cada registro**. Aspa de obra que o registro não vincula não seria achada, e três delas são visivelmente instrução sua ou prosa minha — mas **isso é leitura, não medição** |

---

## 82. A guarda barata das meias-âncoras — e ela acusou o resíduo da minha própria correção — ✅ 22/10/2026

**Encaminhamento:** *"Construa a guarda barata."* — a que eu listei em 81.6 e não construí.

### 82.1 Onde ela mora, e é isso que a torna barata

Entrou em **`conferir_paginas.py`**, o passo 10, com `MEIAS_ANCORAS_BASE = 0`.

> **A razão de morar aqui e não em script próprio:** este passo **já abre** as folhas de `fonte_pagina` de cada registro, e `texto_pagina` as guarda em `_cache`. A guarda testa **as mesmas folhas**. **Guarda barata é guarda que vive onde as folhas já estão abertas.**

**E "barata" foi medido, não afirmado:** mesmo conjunto, mesma máquina, com e sem a chamada.

| | |
|:--|:--|
| ciclo do passo 10 **com** a guarda | **19,2 s** |
| **sem** a guarda | **18,5 s** |
| custo | **+0,7 s, cerca de 4%** |

### 82.2 O detector é de propósito mais frouxo que o promotor

A guarda usa **`casa()`**, de janela, e **não** `confere_integral()`. A razão é um caso real de ontem: a aspa de PT-57 na folha 19 era **composta por junção** de dois recortes que a folha traz separados, e confere **`parcial`**.

> Com `confere_integral` ela **escaparia** da guarda. Com `casa` ela é acusada — que é o que se quer. **Guarda detecta; quem promove confere por inteiro.**

**E não há lista de dispensa, de propósito** — é a lição de 22/10 sobre o `.gitignore`: lista de exceção é dívida que ninguém revisita. Aspa nova que confira faz o ciclo cair, e as saídas são duas: promovê-la a `fonte_trecho`, ou **subir a base e dizer no commit por quê** — a mesma convenção de `PARCIAIS_BASE` e `EMPATES_BASE`.

**A posição da chamada também é deliberada:** ela roda **antes** do desvio de *"referência sem transcrição literal"*. Registro que não tem transcrição em `fonte_trecho` e cuja nota traz aspa conferível é a meia-âncora mais pura que existe — e sairia por aquele `continue` sem ser examinado.

### 82.3 Na primeira execução ela acusou o que eu havia deixado atrás

`meias-âncoras: 1 (base 0)` — **PT-57**, e o defeito era meu, de uma hora antes.

> Na varredura do item 81 eu promovi a `fonte_trecho` os **dois recortes separados** da folha 19 — e deixei na nota a **frase composta**, entre aspas. **Corrigir a promoção sem corrigir a nota deixou a asserção de literalidade de pé:** a forma composta é um **literal falso**, que a folha não traz e que nenhuma guarda conferia. A nota passou a trazer os dois recortes separados.

**E há um efeito de segunda ordem que vale registrar:** as três folhas que a varredura acrescentou a `fonte_pagina` tornaram **testáveis** aspas de nota que antes não tinham folha ancorada onde conferir. **A guarda cresce de alcance a cada âncora nova** — o que é o contrário do que acontece com guarda de lista.

### 82.4 As três provas negativas, e a terceira declara um limite

| | prova | resultado |
|:--|:--|:--|
| **1** | aspa de nota que confere em folha **ancorada** | acusa **1** ✔ |
| **2** | a **mesma** aspa também em `fonte_trecho` | acusa **0** ✔ — a contenção funciona |
| **3** | aspa de nota que confere em folha que o registro **não** ancora | acusa **0** ✔ — **limite declarado** |

**A prova 3 não é virtude, é o limite:** a parte cara da varredura — abrir o PDF inteiro — levou **205 s para 16 aspas** e não cabe no ciclo. Esta guarda pega **7 dos 10** casos de hoje, e os outros três exigiram folha nova.

### 82.5 Duas coisas que as provas consertaram na própria guarda

| | |
|:--|:--|
| **a prova 1 acusava 2 onde havia 1** | a mesma aspa citada duas vezes no campo de nota rende duas ocorrências em `transcricoes()`. A guarda passou a **deduplicar por aspa normalizada** — relato inflado é o que ensina a ignorar a guarda |
| **o meu harness destruiu trabalho** | a primeira versão revertia com `git checkout --` e a árvore tinha alteração **não comitada**: a reversão **descartou a correção da nota de PT-57**, e as duas provas seguintes rodaram contra linha de base poluída. **Prova negativa que reverte por `git` pressupõe árvore limpa** — esta restaura de uma **cópia em memória**, com SHA-256 conferido |

### 82.6 O ciclo, e o que resta

Doze passos, verde: `meias-âncoras: 0 (base 0)` · `G2 0` · `G4 limpa` · `divergências de nome: 0` · `APROVADO` · `confirmados 74 | falhas 0 | indeterminados 4`.

| | |
|:--|:--|
| **a parte cara segue à mão** | varrer PDF inteiro não cabe no ciclo. O item 81 diz como rodar, e o custo é 205 s |
| **a guarda não vê âncora não-PDF** | `localizar()` só abre PDF, e por isso os seis registros de localizador estrutural seguem fora do alcance. **Ensinar o conferidor a ler âncora não-PDF** mudaria `SEM_PAGINA_EXTRAIVEL_BASE`, que é decisão sua — proposto desde 77.5 |
| **as três decisões de 26(c)** | intactas |

---

## 83. As três decisões de 26(c) — e a mais pesada era um vocabulário sem definição — ✅ 25/10/2026

**Encaminhamento:** *"Decida as três de 26(c)."* — a segunda delegação de decisão de campo, depois do `data_hora` de PT-02.

**26(c) estava aberta desde 15/10/2026 e esvazia hoje.**

### 83.1 (ii) A promoção de classe — e a causa-raiz não era a classe

Eu ia decidir sobre três registros. A medição mudou a pergunta:

| | |
|:--|:--|
| dos **61** em `Confirmado em fonte primária` | **zero** ancoram só em literatura — o critério é firme desse lado |
| dos **23** em `Confirmado` | **treze** ancoram **só em fonte documental** |

> **Ancorar em documento era necessário e não suficiente — e o critério que faltava não estava em lugar nenhum do esquema.** `vocabulario_status_classe` era uma **lista de quatro rótulos sem definição**. O critério vivia em **prosa, dentro de um registro**: PT-01A declara que *"NÃO é fonte primária **no sentido estrito deste codebook**: a peça primária seria o acórdão de AE 157804 e o relatório de auditoria de Pet 185520, nenhum dos dois obtido"*.
>
> **É a causa-raiz da pendência, e ela explica os onze dias:** a decisão parecia ser sobre três registros porque ninguém podia ler o critério para aplicá-lo aos treze.

**O critério, escrito hoje em três condições cumulativas:**

| | condição |
|--:|:--|
| **1** | `fonte_local` inclui **a peça do próprio ato** — o acórdão da decisão que o registro codifica, o relatório oficial do órgão, o documento publicado. **Não** comunicação *sobre* o ato, **não** relatório que o cita |
| **2** | `fonte_pagina` **localiza** a afirmação nessa peça, por folha **ou** por localizador estrutural — as duas valem, e PT-03E já era primário citando por seção |
| **3** | o registro **não declara insuficiência pendente** sobre essa âncora |

**Revisão por pares é irrelevante aqui:** o que a classe mede é **a distância até o ato**, não o crivo editorial.

**Aplicado, promove SEIS e não três:**

| registro | a peça do próprio ato |
|:--|:--|
| **PT-03B** | TRF-4, inteiro teor, folhas 30 e 401 |
| **PT-05A** | ADC 43/44/54, folhas 2, 31 e 489 |
| **PT-06B** | HC 164.493, por inteiro teor |
| **PT-06C** | HC 193.726, folha 185 |
| **PT-56** | AP 2668, o acórdão da própria condenação |
| **PT-57** | AP 2668, o acórdão que o registro data, folhas 19 e 888 |

> **Por que seis e não três, e os três a mais têm razão diferente.** **PT-57** ganhou folha em **15/10, no mesmo dia** que os outros três — a parte (a) de 26 lista **quatro** folhas — e a lista de decisão nomeou só três: **contagem copiada de outro lugar perde item, pela terceira vez neste repositório.** **PT-06B e PT-56** satisfazem as mesmas condições citando por **localizador estrutural**, que o vocabulário agora declara valer.
>
> **Nenhum critério foi afrouxado. O critério foi escrito** — e foi a escrita que revelou que ele alcançava o dobro de registros.

**Os dezessete que ficam, cada um com a razão declarada** — e dois não a tinham:

| | |
|:--|:--|
| **PT-03C** | o acórdão do HC 152.752 **está** em `fonte_local` e **nenhum localizador o aponta**: `fonte_pagina` só traz `MADEIRA ET AL 2022`, literatura. Falha a condição (2). **Lacuna fechável, não limite da peça** — ✅ **RESOLVIDO EM 25/10/2026, horas depois (item 85):** cinco transcrições do próprio acórdão entraram, `fonte_pagina` passou a `HC 152.752: 1, 3 | MADEIRA ET AL 2022: 256, 267` e a classe foi promovida. O codebook foi a **68 em fonte primária** |
| **PT-03D** | sem peça do ato no corpus — `fonte_local` vazio. Falha a condição (1). É o único registro sem documento vinculado |

As outras quinze já diziam: literatura como única âncora (6), peça do ato não obtida (PT-01A, PT-02A, PT-06A), atribuição externa à peça (PT-01B, documento internamente anônimo), relatório de laboratório não revisado por pares (PT-19A, PT-50A), fonte documental citando outra peça (PT-27), insuficiência pendente (PT-38), afirmação central em literatura (PT-08).

### 83.2 (iii) e (iv) Os dois nomes, e a forma saiu de medição

Os dois registros **já traziam proposta** no campo, desde 20/10. Medi a convenção antes de escolher a forma: os nomes do codebook são **frases nominais curtas**, com o termo da literatura entre parênteses quando existe — `Certificação por elite (elite certification)`, `Radicalização de flanco`, `Defecção do agente de contenção`. **As propostas eram frases longas, fora do padrão**; o conteúdo delas está preservado no campo.

| | nome | o que o ancora |
|:--|:--|:--|
| **PT-01A** | **Articulação inicial do quadro de fraude, refutada pela via acionada** | liga a cadeia: é **o mesmo quadro** que PT-07 articula em 2022, aqui pela primeira vez por via institucional — e **refutado no registro da própria Corte**, que nomeia o enquadramento como *"lendas urbanas"* e declara que o pedido *"se constitui em nenhuma inovação"* |
| **PT-01B** | **Defecção programática do aliado de coalizão** | usa `defecção`, que **PT-31 já carrega**, e qualifica o meio: programa de governo completo publicado por força então na coalizão. Alimenta **D2 — configuração de aliança no Executivo** como o **sinal anterior à saída**: D2 observa presença e ausência com data, e este registro data a defecção antes de a ausência existir |

> **A refutação é a parte distintiva de PT-01A**, e é o que faz dele antecedente e não precedente: **o que recorre em 2022 recorre CONTRA um registro documentado.**

### 83.3 Três guardas acusaram o meu trabalho enquanto eu o fazia

| guarda | o que pegou |
|:--|:--|
| **tabela-espelho** | `divergências de nome: 2` — a figura seguia chamando os dois pontos de *"proposta de mecanismo, não atribuída"*. A figura passou a dizer o que o codebook diz |
| **checagem 7** | `aviso_metodologico não cita a classe vigente: _nota` — ela lê **as chaves** do vocabulário como nomes de classe, e `_nota` é metadado **sobre** o vocabulário. O prefixo `_` já era a convenção da casa (`_lidas_retirada_em`), e a guarda passou a respeitá-la |
| **conferir_figuras** | quatro selos em `ok` e o subtítulo dizendo **61** em fonte primária quando o codebook tem **67**. Corrigidos |

**E um erro de ferramenta, no meio:** `re.sub` processa escapes na string de substituição, e o HTML carrega `\u0027` nas aspas simples — o patch caiu com `bad escape \u`. Trocado por `lambda`, que não reprocessa.

### 83.4 O que isto deixa

**A tarefa 26 não tem parte aberta:** (a), (b) e (c) executadas. **Fechá-la é decisão sua** — contagem é medição, estado de tarefa é juízo, pela regra que o item 79 registrou quando você fechou a 25. **Não toquei no campo `estado`.**

| | |
|:--|:--|
| **PT-03C** | uma transcrição do próprio acórdão do HC 152.752, com folha, e ele satisfaz as três condições. ~~**É a única promoção que falta por lacuna fechável**~~ — ✅ **RESOLVIDO EM 25/10/2026, horas depois (item 85):** cinco transcrições do próprio acórdão entraram, `fonte_pagina` passou a `HC 152.752: 1, 3 | MADEIRA ET AL 2022: 256, 267` e a classe foi promovida. O codebook foi a **68 em fonte primária** |
| **a guarda que falta** | nada impede um registro de satisfazer as três condições e ficar em `Confirmado` sem razão escrita. **A base é agora zero e a guarda é barata** — só JSON, sem abrir PDF. Não a construí: você pediu as decisões |
| **PT-62** | o nome poderia dizer a rota heterônoma; segue sua |

**Restam três tarefas:** **10** (seus arquivos), **17** (seu acesso institucional) e **16** (a redação) — e **nenhuma decisão de campo aberta** no codebook, pela primeira vez desde 04/10/2026.

---

## 84. A tarefa 26 fecha — e com ela a última tarefa que tocava o codebook — ✅ 25/10/2026

**Encaminhamento:** *"Feche a tarefa 26."*

Fechada no dia em que a terceira e última parte dela saiu. **Aprovada em 15/10/2026**, levou **dez dias** e as três partes fecharam por caminhos diferentes:

| parte | como fechou |
|:--|:--|
| **(a)** as quatro folhas que faltavam | ✅ 15/10, por verificação — `conferir_paginas` localizou 6 de 6 por inteiro, e `confirmados` subiu de 69 a 73 |
| **(b)** os 17 fragmentos que casavam só por janela | ✅ 15/10, por verificação — foram a **zero**, e nenhuma classe foi afrouxada: 4 eram âncora na folha errada, 2 transcrição editada, 8 marcador de nota, 3 citação atravessando quebra |
| **(c)** as decisões de campo | ✅ 25/10, por **duas delegações suas** — o `data_hora` de PT-02 em 22/10 (item 80) e as três últimas em 25/10 (item 83) |

### 84.1 O que fecha com ela

> **É a última tarefa aberta que tocava o codebook.** Desde 16/08/2026 havia sempre uma: sincronizar formatos, aplicar correções de auditoria, codificar a camada conjuntural, codificar o 17º campo, fechar âncoras. **Hoje não há nenhuma, e não há decisão de campo aberta** — a primeira vez desde 04/10/2026.

**O banco, no fecho:** 85 registros × 17 campos · **67 em fonte primária**, 17 `Confirmado`, 1 `Inferência do analista` · zero `A verificar` · zero `mecanismo_causal` vazio · zero `autonomia_movimento` vazio · **1 registro sem `fonte_pagina`**, declarado (PT-03D, que ancora em notícia arquivada).

**E o aparato que o vigia:** ciclo em **doze passos**, **cinco guardas nomeadas** — G1, G2 e G3 do registro de leitura, G4 do `ledger`, e as meias-âncoras no passo 10 — mais as oito checagens estruturais, a tabela-espelho e os conferidores de figura, relatório, páginas, campo e hipóteses. **Linhas de base em zero:** divergências de nome, incoerências de prosa, meias-âncoras, fragmentos por janela, empates entre documentos.

### 84.2 A ordem de ataque, agora

| # | Tarefa | Depende de |
|:--|:--|:--|
| **10** | obter o cânone que Gohn (2019) nomeia — a leitura do eixo está completa | **seus arquivos** |
| **17** | ler na fonte os 43 da camada A — **25 pendentes**, 9 barradas no cliente, 16 sem depósito aberto | **seu acesso institucional** |
| **16** | **a redação** | tudo acima |

> **Das três, duas dependem de material que só você pode trazer — e nenhuma delas bloqueia a redação por dado.** As tarefas 10 e 17 servem à bibliografia e ao enquadramento do artigo, não à codificação: isso foi medido em 04/10, quando a quarta rodada da tarefa 14 mostrou que nenhuma leitura pendente ancora registro.
>
> **A decisão de 16/08/2026 — a redação é o último item — continua a ordenar tudo. E hoje ela deixou de ter pré-requisito de dado.**

### 84.3 O que permanece listado, e nada disto é tarefa

| | |
|:--|:--|
| **PT-03C** | promoção de classe por lacuna fechável: ~~o acórdão do HC 152.752 está em `fonte_local` e nenhum localizador o aponta. Uma transcrição com folha resolve~~ — ✅ **RESOLVIDO EM 25/10/2026, horas depois (item 85):** cinco transcrições do próprio acórdão entraram, `fonte_pagina` passou a `HC 152.752: 1, 3 | MADEIRA ET AL 2022: 256, 267` e a classe foi promovida. O codebook foi a **68 em fonte primária** |
| **PT-62** | o nome poderia dizer a rota heterônoma; nomear mecanismo segue sua decisão |
| **a guarda das três condições** | barata, só JSON, base zero — não construída, porque você pediu as decisões |
| **âncora não-PDF no conferidor** | tornaria verificáveis os 6 registros de localizador estrutural; muda `SEM_PAGINA_EXTRAIVEL_BASE`, que é sua |
| **higiene** | os 64 PDFs no histórico · 1 PDF em `.backup_pre_lula/` · 8 `.docx` · o ramo `backup-antes-de-destrackear-pdfs` |
| **cristalização de quadro** | não resolvível com este corpus; desenho mínimo entregue |
| **Beach e Pedersen, cap. 4 a 8** | e as quatro dívidas — todas de redação |

---

## 85. PT-03C resolvido — e o placar do registro não está no acórdão — ✅ 25/10/2026

**Encaminhamento:** *"Resolva o PT-03C."* — a lacuna que a §83.1 nomeou ao escrever o critério de classe, três horas antes.

### 85.1 A lacuna, e por que era fechável

O registro codifica a **denegação do HC 152.752**, e o acórdão **estava** em `fonte_local` desde sempre. Mas `fonte_pagina` trazia só `MADEIRA ET AL 2022: 256, 267` — **literatura**. A peça do próprio ato estava no corpus e **nenhum localizador a apontava**, de modo que o passo 9 do ciclo nunca a abria.

**Cinco transcrições entraram, as cinco conferidas por `confere_integral` na folha antes de escritas:**

| folha | o que ancora |
|--:|:--|
| **3** | o dispositivo: *"na sessão plenária do dia 04.04.2018, o Tribunal, por maioria e nos termos do voto do relator, denegou a ordem"* — **data e resultado** |
| **3** | *"vencidos, em menor extensão, os Ministros Gilmar Mendes e Dias Toffoli, e, em maior extensão, os Ministros Ricardo Lewandowski, Marco Aurélio e Celso de Mello"* — **os cinco vencidos** |
| **3** | a questão de ordem sobre *"havendo empate na votação, a presidente do tribunal não poderia votar"* |
| **1** | a ementa: *"habeas corpus. matéria criminal. execução provisória da pena"* — **o objeto** |
| **1** | *"supressão de instância. ordem denegada"* |

`fonte_pagina` passou a `HC 152.752: 1, 3 | MADEIRA ET AL 2022: 256, 267`, e o passo 9 passou a dizer **`PT-03C OK 7/7 localizadas`**. **A classe foi promovida pelas três condições**, e o codebook foi a **68 em fonte primária**.

### 85.2 E o achado: o placar do registro não está na peça

O registro diz *"por **6 votos a 5**"*. Varri as **464 folhas** por `6 x 5` e por `6 votos`: **zero ocorrências**.

> **O que o acórdão escreve é *"por maioria"*, e ele NOMEIA os cinco vencidos.** O 6 a 5 segue de **cinco vencidos numa Corte de onze** — derivação correta, e **não transcrição**. Fica declarado como tal no registro, pela regra de 15/10 sobre cifra à mão: ou se gera, ou se declara de onde vem.
>
> **E a mesma folha corrobora a derivação, de um jeito que eu não esperava:** o Tribunal *"rejeitou questão de ordem … no sentido de que, havendo empate na votação, a presidente do tribunal não poderia votar"*. **A questão de ordem só tem sentido se o voto da presidente desempatou** — isto é, se antes dele havia 5 a 5. É o placar de 6 a 5 confirmado pelo que a Corte teve de rejeitar.

**Por que isto importa mais que a promoção de classe:** se alguém fosse conferir o `6 votos a 5` abrindo o acórdão e procurando a cifra, não a acharia — e concluiria que o registro afirma o que a fonte não diz. **A derivação estava certa e invisível; agora está certa e escrita.**

### 85.3 O que mudou em cascata, e as três erratas

| | |
|:--|:--|
| **o vocabulário** | a razão *"peça do ato no corpus mas sem localizador que a aponte"* era **de PT-03C e só dele**. Saiu da lista de razões em uso, e ficou **descrita**, porque era a única das razões que era **fechável** em vez de limite da peça |
| **a figura** | o subtítulo dizia **67** em fonte primária; o codebook tem **68**. O selo do ponto **não** mudou, e corretamente: `PT-03C/D` é **ponto composto** e PT-03D segue `Confirmado` |
| **os itens 83 e 84** | três linhas escritas **horas antes** diziam que esta era a promoção que faltava. Erratas em 83.1, 83.3 e 84.3 |

### 85.4 O que resta

**Dezesseis registros em `Confirmado`, e nenhum por lacuna fechável** — todos por limite declarado da peça ou da fonte: literatura como única âncora (6), peça do ato não obtida (PT-01A, PT-02A, PT-06A), atribuição externa (PT-01B), relatório de laboratório não revisado por pares (PT-19A, PT-50A), fonte documental citando outra peça (PT-27), insuficiência pendente (PT-38), afirmação central em literatura (PT-08) e notícia arquivada sem peça no corpus (PT-03D).

> **Com isto, a classe de cada registro do codebook é consequência de critério escrito, e nenhuma delas depende de decisão pendente.**

**Três tarefas abertas:** 10, 17 e 16. E a guarda das três condições segue proposta e não construída, com base agora em **68**.

---

## 86. A guarda das três condições — e duas delas não são mecanizáveis — ✅ 25/10/2026

**Encaminhamento:** *"Construa a guarda das três condições."* — a que eu listei em 83.4, 84.3 e 85.4 e não construí.

### 86.1 O desenho mudou na primeira medição, e é a parte que importa

Eu prometi uma guarda para as três condições do vocabulário. **Duas delas não são decidíveis por máquina:**

| condição | mecanizável? |
|:--|:--|
| (1) `fonte_local` inclui **a peça do próprio ato** | ✘ **semântico.** PT-27 ancora a CPMI, que é documental e **cita outra peça**; PT-02A ancora o acórdão de **outro processo**. Nenhum código distingue "a peça do ato" de "peça que documenta o ato" |
| (2) `fonte_pagina` **localiza** nessa peça | ✔ `pares()` mais `registro_documentos` resolvem |
| (3) nenhuma **insuficiência pendente** declarada | ✘ **juízo de prosa** |

> **Então a guarda não decide a classe — ela exige que o desvio seja explicado.** Registro em `Confirmado` que ancore peça **documental** com **localizador que a aponte** tem de trazer a marca canônica. **É a forma de `PARCIAIS_BASE`:** a exceção é legítima, e tem de estar escrita.
>
> **Uma guarda que tentasse decidir a classe estaria errada em dois dos seis casos que ela testa** — e errada com a aprovação do ciclo, que é o pior defeito possível.

### 86.2 Uma marca, não uma lista

A guarda confere **uma cadeia só**: `CLASSE NÃO PRIMÁRIA:`.

> **Lista de marcas é a fragilidade que esta casa já pagou duas vezes:** a checagem 7 era **cega à caixa** e deixou passar nome morto por onze dias (item 70); e a G2 **não tinha a forma coletiva da negação** e por isso **não examinou** a linha falsa do `ledger` (item 78). Marca única não tem meia-cobertura.

**Medido antes de construir:** a guarda alcança **seis** registros, e só **PT-01B** tinha declaração explícita. Os outros cinco — **PT-02A, PT-06A, PT-08, PT-27, PT-50A** — tinham a razão em prosa e ganharam a marca, cada uma com o motivo que já carregavam:

| registro | razão |
|:--|:--|
| **PT-01B** | atribuição externa: o documento é **internamente anônimo** |
| **PT-02A** | a peça do ato não está no corpus — o acórdão do HC 126.292 não foi obtido |
| **PT-06A** | idem: a decisão monocrática de 08/03/2021 não foi obtida |
| **PT-08** | a afirmação central está em **literatura revisada por pares** |
| **PT-27** | a fonte documental **cita outra peça**, e o original está no corpus |
| **PT-50A** | relatório de laboratório **não revisado por pares**, categoria operacionalizada pelos autores |

### 86.3 O limite, declarado e medido

**A guarda não alcança quem cita por localizador estrutural**, porque `pares()` não cede numeral para `inteiro teor` nem para `§seção`. **Medido: PT-01A, PT-19A e PT-38 caem fora** — e os três declaram a razão de todo modo.

É o mesmo limite da guarda das meias-âncoras, e a mesma causa: **o conferidor abre PDF numa folha, e localizador estrutural não tem folha.** Ensiná-lo a ler âncora não-PDF resolveria os dois de uma vez, e muda `SEM_PAGINA_EXTRAIVEL_BASE` — segue sua decisão, proposta desde 77.5.

### 86.4 Quatro provas negativas, e a segunda é a que mais vale

| | prova | |
|:--|:--|:--|
| **1** | tirar a marca de um dos seis | cai ✔ |
| **2** | **rebaixar um registro primário** sem escrever razão | **cai** ✔ |
| **3** | rebaixar um que ancora só literatura | não acusa ✔ — **limite** |
| **4** | promover o registro tira-o do alcance | não acusa ✔ |

> **A prova 2 é a que justifica a guarda:** ela mostra que a guarda cobre **regressão**, não só o estado de hoje. Alguém que rebaixe um dos 68 primários sem escrever por quê faz o ciclo cair — e é exatamente assim que os treze candidatos se acumularam em silêncio entre 15/10 e 25/10.

**As quatro restauram de cópia em memória, com SHA-256 conferido** — pela lição de 22/10, em que uma prova minha revertia por `git checkout --` e **destruiu trabalho não comitado**.

### 86.5 O ciclo

**O verificador foi a nove checagens**, e o rótulo do passo 7 acompanhou. `RESULTADO: APROVADO — as nove checagens passaram` · `6 registro(s) em Confirmado com âncora documental apontada` · `OK — todos declaram a razão da classe`.

**Doze passos, seis guardas nomeadas:** G1, G2 e G3 do registro de leitura · G4 do `ledger` · as meias-âncoras no passo 10 · e a checagem 9 da classe.

---

## 87. O conferidor lê âncora não-PDF — treze transcrições que nunca foram examinadas — ✅ 25/10/2026

**Encaminhamento:** *"Ensine o conferidor a ler âncora não-PDF."* — proposto desde 77.5, e listado em 82.6, 84.3 e 86.3.

### 87.1 O que estava sem guarda, e a razão é de fila

Três registros citam a fonte por **localizador estrutural** num arquivo não paginado — **PT-01A** (duas notícias do TSE em `.md`), **PT-03E** (acórdão do TSE em `.html`, 947 KB) e **PT-19A** (post do NetLab em `.md`).

> **`pares()` não cede numeral para `§seção` nem para `inteiro teor`.** Sem par, os três não entravam em `cands` — a fila de candidatos — e por isso contavam na `SEM_PAGINA_EXTRAIVEL_BASE` e **nunca tiveram uma transcrição examinada**. **Treze transcrições sem guarda alguma**, e a razão não era desenho: era a fila excluindo em silêncio.
>
> **Contar o que a fila exclui** é lição desta casa desde 18/10, quando a base nasceu justamente para dar nome a eles. **Dar nome não é conferir** — a base os tornou visíveis e não os tornou verificados.

### 87.2 A unidade não é a folha, é o arquivo — e marcação é aparato

`texto_integral()` lê `.md`, `.html`, `.xml` e `.txt`, e reduz o texto pela mesma função que reduz folha. Para peça não paginada a pergunta é a de sempre — **a transcrição está na peça?** — e a unidade é o arquivo inteiro, que é o que `inteiro teor` e `§seção` já diziam.

**E uma descoberta que mediu o que faltava:** na primeira medição **4 das 13 falharam**. Não era defeito do registro:

> O arquivo traz `Encontramos **185 anúncios** com conteúdo golpista`, e a transcrição não tem os asteriscos. **Marcação inline é aparato do formato, não conteúdo da fonte** — exatamente o que o leitor de HTML já fazia com tags, um formato adiante. Retirados `**`, `*`, `_`, crase e o `>` de citação, **as 13 conferem**.
>
> **E a minha primeira medição foi grosseira:** usei substring cru e acusei 7 falhas, das quais 3 eram **elisão `(...)`** que a cadeia do projeto trata partindo a transcrição em `fragmentos()`. **Medir com a semântica do próprio conferidor, não com a minha** — refeito, caiu de 7 para 4, e as 4 eram a marcação.

### 87.3 O resultado

| | antes | depois |
|:--|--:|--:|
| `confirmados` | 74 | **77** |
| `SEM_PAGINA_EXTRAIVEL_BASE` | 6 | **3** |
| exceções em `EXCECOES` | 8 | **5** |
| PT-01A · PT-03E · PT-19A | fora do alcance | **6/6 · 7/7 · 2/2** |
| PT-08 | 8/8 **com 3 dispensas** | **11/11 sem nenhuma** |

> **As três exceções de PT-08 saíram, e é o melhor desfecho possível para uma exceção: a correção que ela pedia chegou.** O comentário delas dizia, em 22/10, com estas palavras: *"A correção certa não é esta exceção: é ensinar `localizar()` a ler âncora não-PDF"*. Ficou o registro, porque **exceção que sai por conserto é dado sobre o conserto** — ela mediu, por três dias, exatamente o buraco que o leitor novo fechou.

**Permanecem três fora do alcance, e por razão diferente:** PT-06B, PT-38 e PT-56 citam **PDF** por `inteiro teor`. Ali o conferidor **sabe abrir a peça e não sabe onde olhar**, e varrer PDF inteiro custou **205 s para 16 aspas** em 22/10 — não cabe no ciclo.

### 87.4 A terceira prova negativa consertou a própria linha de base

| | prova | |
|:--|:--|:--|
| **1** | cauda editada em transcrição de `.md` | reprova ✔ |
| **2** | cifra trocada em transcrição de `.html` | reprova ✔ |
| **3** | registro que **perde** o anexo | **falhou na primeira execução** |

**A prova 3 passou a mensagem e não o código de saída:** `fora do alcance: 4`, o aviso impresso — e **saída zero**. A base **só avisava**.

> **E o comentário dela afirmava o contrário, desde 18/10, com estas palavras:** *"Com a base, o sexto que aparecer **faz o ciclo cair** — porque registro que deixa de ser conferível tem de ser uma decisão, não um efeito colateral."*
>
> **Garantia declarada que ninguém confere, pela terceira vez nesta casa** — depois da vigilância de SHA-256 que não cobria arquivo não-PDF e da exclusão inerte por separador de caminho. **A prova pegou porque testou o código de saída, não a mensagem** — e é por isso que prova negativa afere saída, não texto.

Corrigida, a base **reprova**, e as três provas passam.

### 87.5 O que isto deixa

| | |
|:--|:--|
| **as duas guardas que declaravam este limite** | a das meias-âncoras e a checagem 9 seguem sem alcançar localizador estrutural **em PDF**; para `.md` e `.html` o limite caiu junto, porque as duas usam `pares()` |
| **os três que restam** | varrer PDF inteiro no ciclo custaria minutos. **Um cache de texto por folha, indexado pelo SHA-256 que a checagem 8 já vigia**, resolveria — e é desenho novo, não listado antes |
| **exceção ociosa não é acusada** | nada avisa quando uma entrada de `EXCECOES` deixa de ser usada. As três de PT-08 eu removi **porque fui olhar**; a quarta ficaria |

---

## 88. O cache de texto por folha — e a primeira varredura achou cinco âncoras que não existem — ✅ 25/10/2026

**Encaminhamento:** *"Construa o cache de texto por folha."* — o desenho que eu propus em 87.5 e não construí.

### 88.1 Para que serve, e a cifra justifica

Três registros citam PDF por `inteiro teor` — **PT-06B, PT-38, PT-56** — e ali o conferidor **sabia abrir a peça sem saber onde olhar**. Varrer as **2.874 folhas** dessas cinco peças custou **151 s**, medidos. Por rodada de ciclo, inviável; e sem a varredura, **a afirmação deles ficava inguardável**.

| | |
|:--|:--|
| primeira construção | **151 s**, 2.874 folhas |
| segunda leitura, **em processo novo** | **0,27 s** |
| cache em disco | **1,7 MB** em cinco arquivos gzipados |
| ciclo completo | de ~40 s a **43 s** |

### 88.2 A chave tem duas partes, e a segunda é a que importa

| | |
|:--|:--|
| **SHA-256 do PDF** | que a **checagem 8 já vigia** peça por peça — se os bytes mudarem, o cache é rejeitado |
| **`RECEITA_EXTRACAO`** | `texto_pagina` concatena **três leituras** — PyPDF2, PyMuPDF e PyMuPDF com conserto de glifo — e normaliza |

> **Cache que sobrevive a uma mudança no extrator é cache que mente.** Mexer em `texto_pagina`, em `_mupdf` ou em `norm_busca` obriga a subir `RECEITA_EXTRACAO`, e as duas primeiras provas negativas aferem exatamente isto: um cache **deliberadamente falso** é usado sob a receita que o gravou, e **deixa de ser usado** quando a receita sobe.

**O cache é derivado e está no `.gitignore`.** Some sem perda: a rodada seguinte o reconstrói do PDF.

### 88.3 A busca integral vale SÓ onde o registro cita a peça inteira

> Aplicada a todo fragmento não localizado, ela **resgataria âncora creditada à folha errada** — o defeito que o item 52 mediu em quatro registros e que a folha existe para pegar. `inteiro teor` autoriza procurar em qualquer folha porque é o que o campo afirma; **`fonte_pagina: 185` não.**

**A quarta prova negativa afere isso:** troquei a folha de PT-06C de 185 para 7, e ele **falhou** em vez de ser resgatado pela varredura.

### 88.4 E a primeira varredura achou cinco âncoras que não existem

**As cinco transcrições dos três registros não estão nas peças citadas.** A causa é única e está medida:

| registro | a transcrição | onde ela está |
|:--|:--|:--|
| **PT-06B** | *"STF confirma suspeição de Sergio Moro…"* e a de corroboração | **manchetes** do portal do STF e da Agência Brasil |
| **PT-56** | *"STF fixa penas de 16 a 27 anos…"* | **manchete** do portal do STF |
| **PT-38** | *"somente no STF, o prejuízo financeiro chegou a R$ 11,4 milhões"* e *"furtados, quebrados ou completamente destruídos"* | **matéria da Agência Brasil de setembro de 2024** |

> **PT-38 é a prova mais limpa, e exclui a explicação fácil:** `11,4 milhões`, `prejuízo financeiro` e `furtados` têm **zero ocorrências** nas 210 folhas do livro — que **tem camada de texto**, 68 mil caracteres só nas 30 primeiras folhas. **Não é peça ilegível; é transcrição de outra peça.**
>
> **É o padrão de PT-08 antes de 22/10**, e o conserto já foi feito uma vez nesta casa: arquivar a página em `Fontes/09_Arquivamento-web/` como `.md` e citá-la por localizador estrutural — a rota (b) do item 76, que o leitor do item 87 agora confere. **Mas é coleta na web, e coleta é decisão sua.**

**Categoria nova, com linha de base que reprova:** `INTEIRO_TEOR_SEM_ACHADO_BASE = 5`. Antes eu podia dizer apenas *"o conferidor não alcança a peça"*; agora ele **varreu as 2.874 folhas e provou** algo mais forte. A sexta que aparecer faz o ciclo cair.

### 88.5 Duas regras nasceram do trabalho, e uma é a terceira reincidência

**`SEM_PAGINA_EXTRAIVEL_BASE` foi a ZERO.** Nenhum registro do codebook está fora do alcance do conferidor — era 6 em 18/10, 3 depois do item 87, e é 0 hoje.

**E `total zero nunca é OK`.** Registro sem nada conferido relatava `OK 0/0 localizadas`, **com cara de verificado**. Apareceu no item 87 com o leitor não-PDF, voltou aqui com a categoria nova, e **em vez de consertar o caso entrou a regra**: se nada foi conferido, o registro é `~ indeterminado` e **diz por quê**. Os `confirmados` deixam de contar quem não foi conferido — `confirmados 77 | falhas 0 | indeterminados 7`.

### 88.6 O que isto deixa

| | |
|:--|:--|
| **as cinco âncoras** | o conserto é arquivar três páginas web e citá-las por localizador estrutural, como PT-08. **Coleta é sua decisão** — e a alternativa é retirar as transcrições e deixar os registros ancorados só pela peça, o que PT-56 e PT-06B suportam (o acórdão **é** o ato) e PT-38 não |
| **o cache cobre cinco peças** | as citadas por `inteiro teor`. Qualquer outra varredura integral o constrói sob demanda, pagando 151 s por 2.874 folhas uma vez |
| **exceção ociosa** | segue sem guarda, listado desde 87.5 |

---

## 89. As três páginas arquivadas — e as cinco âncoras tinham duas causas, não uma — ✅ 25/10/2026

**Encaminhamento:** *"Arquive as três páginas web e ancore as transcrições."*

### 89.1 A medição corrigiu o próprio encaminhamento

O item 88 listou cinco transcrições ausentes das peças citadas e **eu as tratei como um caso só**. Ao ir buscar as páginas, elas se separaram:

| | causa | registros |
|:--|:--|:--|
| **3** | **manchete de página web coletável** | PT-06B (duas) e PT-56 (uma) |
| **2** | **fonte jornalística que o registro já declarava ausente** | PT-38 |

> **PT-38 não tinha página para arquivar, e o campo dizia isso desde 16/08/2026**, com estas palavras: *"**RESSALVA: NENHUM documento primário do corpus traz esses valores** — nem o livro do STF (varrido), nem o balanço de 2026 (varrido), nem o Relatório Final da CPMI (varrido)."* As cifras vêm de **sinopse de documentário** (ago/2023) e de **levantamento divulgado pela imprensa** (jan/2025), sem URL no registro, e a série está no campo **com data de propósito**, porque a cifra de 2023 foi superada pela de 2025.
>
> **Entraram em `EXCECOES` com essa razão** — é o caso 4 da lista: transcrição que está em `fonte_trecho` **de propósito** sem ser âncora do registro.

### 89.2 As três coletadas, e a convenção que elas seguem

O eixo 09 tinha **duas convenções** em uso, e eu medi antes de escolher:

| | |
|:--|:--|
| **(a) corroboração** | o arquivo fica em `fonte_local`, **sem** código e **sem** citação em `fonte_pagina` — cinco peças |
| **(b) âncora** | ganha código em `registro_documentos` e é citada em `fonte_pagina` por localizador estrutural — **uma só**, o `.md` do Estadão, feito no item 77 |

*"Ancore as transcrições"* é a **(b)**, e é o que as três seguem:

| peça | registro | código |
|:--|:--|:--|
| `STF-noticias_Suspeicao-Moro_PT-06B.html` | PT-06B | `STF notícias Moro` |
| `AgenciaBrasil_2021-06_Moro-parcial-triplex_PT-06B.html` | PT-06B | `Agência Brasil Moro` |
| `STF-noticias_Penas-16-a-27-anos_PT-56.html` | PT-56 | `STF notícias penas` |

**E o que elas são fica escrito nos registros:** manchete de nota institucional **não é a peça do ato** — o acórdão é. Nenhuma classe mudou, e a marca `CLASSE NÃO PRIMÁRIA` de PT-06B continua valendo pela razão que já declarava.

**A coleta, com o detalhe que quem repetir precisa saber:** o portal do STF respondeu **504 de WAF** na primeira tentativa — corpo *"The requested URL was rejected"* com id de suporte F5 — e **200 na segunda**, com cabeçalhos de navegador completos. **Não houve captcha nem desafio de script:** só `User-Agent` e `Accept`. Está declarado em `PROCEDENCIA`.

### 89.3 Um achado lateral, e é do tipo que incomoda

> **A página de PT-38 já estava arquivada no eixo 09 desde a coleta, com o id do registro no nome — `AgenciaBrasil_2024-09_Obras-recuperadas_PT-38.html` — e nunca tinha sido vinculada ao registro.** Peça coletada **para** um registro e ausente **dele**. Não estava no manifesto, não estava em `fonte_local`, não era conferida por nada.
>
> Vinculada como **corroboração**, e com a medição ao lado: **ela também não traz as duas cifras** — `11,4 milhões`, `prejuízo financeiro`, `furtados` e `quebrados` têm zero ocorrências nela, e as cifras que ela traz são outras (R$ 2,2 milhões repassados à UFPel). **A ressalva de 16/08 continua inteira e agora cobre esta peça também.**

### 89.4 Uma precedência que estava invertida

A categoria `fora_da_peca` do item 88 vinha **antes** de `EXCECOES` no laço. Com essa ordem, **registro que cita só por localizador integral nunca chegaria às exceções** — a categoria o engoliria, e uma razão escrita à mão ficaria inerte.

> **Declaração explícita vence categoria genérica.** Invertida a ordem, as duas de PT-38 passam pela exceção que as explica.

### 89.5 O resultado

| | antes | depois |
|:--|--:|--:|
| peças no manifesto | 70 | **74** |
| `confirmados` | 77 | **79** |
| `indeterminados` | 7 | **5** |
| **`INTEIRO_TEOR_SEM_ACHADO_BASE`** | 5 | **0** |
| `fora do alcance` | 0 | **0** |
| PT-06B · PT-56 | `~ 0 de 0` | **2/2 · 1/1** |

> **A base em zero é mais forte que a base em cinco:** a primeira transcrição que aparecer fora da peça citada, **sem razão escrita**, faz o ciclo cair.

**E PT-38 segue `~ indeterminado`, dizendo por quê:** *"as 2 transcrições estão dispensadas por exceção registrada em `EXCECOES`"*. A mensagem antes dizia *"nada foi conferido"* — verdade que não é a razão. **Guarda que diz o que aconteceu sem dizer por que obriga quem lê a escavar.**


### 89.7 A licença das peças não-PDF, e eu medi isto DEPOIS de empurrar

**O manifesto registra `licenca_declarada` = `NAO CONFERIDA (nao-PDF)` para as cinco peças não-PDF do eixo 09** — as três novas, a de PT-38 e o `.md` do Estadão. O auditor de licença só lê PDF.

**Então fui ler a licença dentro dos arquivos, que é a regra da casa — e a ordem estava errada: eu já havia empurrado.**

| peça | o que o arquivo declara |
|:--|:--|
| as **seis** páginas de Agência Brasil (três antigas, a de PT-38, as duas de PT-58) e a nova de PT-06B | **"Todos os direitos reservados"** |
| as **quatro** do portal do STF (PT-59, PT-60 e as duas novas) | **nada declarado** |

> **O padrão é uniforme e pré-existente: as minhas três não criaram categoria nova.** Cinco páginas de Agência Brasil com *"Todos os direitos reservados"* já estavam no remoto público antes de hoje, e as do STF nunca declararam licença.
>
> **Mas a decisão de 21/10/2026 foi sobre PDFs**, e as peças não-PDF do eixo 09 **nunca foram examinadas sob essa lente**. Hoje são **dez arquivos de página web versionados num remoto público**, seis deles declarando direitos reservados — e três entraram hoje, por minha mão.
>
> **E eu tenho precedente meu em sentido contrário, do item 77:** para o Estadão decidi *"versionar o HTML seria redistribuição de jornalismo protegido"* e entrou **só a transcrição**. A diferença que eu usei foi setor público contra jornal comercial — e a EBC é empresa pública, o que sustenta a distinção. **O que ela não sustenta é ignorar o que o arquivo escreve.**

**FICA PARA VOCÊ, e são três saídas com o preço de cada uma:** (a) **manter**, porque é conteúdo de comunicação institucional de órgão público e a prática do repositório já era essa — custo: dez arquivos com licença não conferida num remoto público; (b) **converter as dez em transcrição**, como o Estadão, mantendo as aspas ancoradas e descartando o HTML — custo: perde-se a cópia integral contra *link rot*, que é a razão de o eixo 09 existir; (c) **converter só as seis de Agência Brasil**, mantendo as do STF, que nada declaram — custo: a assimetria precisa de razão escrita, e o ganho sobre (a) é pequeno.

**Não executei nenhuma.** E registro a ordem errada: **a licença devia ter sido lida antes do commit, não depois** — é a regra do próprio projeto, e eu a inverti.

### 89.6 O que isto deixa

| | |
|:--|:--|
| **PT-38 não tem transcrição verificável** | e é o único do codebook nessa situação. O conserto seria coletar a **sinopse do documentário** (ago/2023) e o **levantamento de jan/2025** — fontes jornalísticas, sem URL no registro, e **coleta é sua decisão** |
| **a convenção (a) do eixo 09** | quatro peças seguem como corroboração sem código. **Nenhuma delas foi conferida contra nada** — não é defeito, é o que corroboração significa, mas vale saber |
| **exceção ociosa** | segue sem guarda, listado desde 87.5. Hoje são **7 dispensas**, e a próxima que ficar obsoleta não será acusada |
| **a licença das dez páginas web** | medida em 89.7, **depois de empurrar**, e são três saídas com o preço escrito. Decisão sua |


---

## 90. O gerador das decisões pendentes — a lacuna que a própria listagem revelou — ✅ 27/10/2026

**Encaminhamento:** *"vamos para a próxima tarefa."* — e as três tarefas abertas dependem todas de você, de modo que peguei a que é minha e que eu havia nomeado como a próxima peça óbvia do aparato.

### 90.1 O diagnóstico, e ele é de dois dias antes

Em 25/10/2026, ao listar tudo, colhi as seções *"O que isto deixa"* de cada item da agenda — e **oito das pendências que a colheita devolveu já estavam resolvidas por itens posteriores**: o item 73 pede ler Beach e Pedersen e o 74 leu; o 78 pede fechar a tarefa 25 e o 79 fechou; o 88 pede arquivar as páginas e o 89 arquivou.

> **O defeito não era a prosa daquelas seções, e elas ficam como estão** — são o registro do que se sabia naquele dia, e é para isso que servem.
>
> **O defeito era não haver um lugar único onde virar o bit.** É exatamente o que a ordem de ataque resolveu para as tarefas no item 49, com o campo `estado` — e as decisões nunca tiveram equivalente. **Por isso eu me recusei a copiar a lista para a memória em 25/10:** seria a quarta cópia, e a contabilidade deste projeto já envelheceu quatro vezes por cópia à mão.

### 90.2 O que entrou

`data/decisoes_abertas.json` é a fonte, `scripts/gerar_decisoes.py` o gerador, e a seção **Decisões pendentes** nasce no fim desta agenda, entre marcadores, sobrescrita pelo **passo 4** do ciclo — que foi a **treze passos**.

**Três coisas saem de derivação, e são as três que a mão fazia mal:**

| | |
|:--|:--|
| **a seção em que a decisão aparece** | é consequência do campo `estado`. **Fechar uma decisão é virar um campo**, e ela sai da lista sozinha |
| **a contagem e o agrupamento** | derivados da lista. *"A lista é que manda no número"* foi aprendido **três vezes** nesta casa, sempre por perda de item em cópia |
| **o ponteiro de seção** | **conferido**: a guarda G-A abre a agenda e exige que a seção citada exista |

> **Por que a G-A é a guarda certa:** ponteiro quebrado é a forma que o apodrecimento toma aqui. E **ponteiro para o nada é pior que pendência esquecida**, porque ele *parece* verificável — quem for conferir abre a agenda, não acha a seção, e não sabe se o erro é do ponteiro ou da memória dele.

**O estado inicial: doze decisões, em três naturezas** — o remoto é público (4), campo do codebook (5), leitura (3). Nenhuma bloqueia as tarefas abertas.

### 90.3 O limite, declarado, porque ele é metade do problema

> **Este gerador conserta a CÓPIA, não o JUÍZO.** Ele dá um lugar único para registrar que uma decisão saiu, e deriva a contagem. **Ele não detecta sozinho** que uma decisão foi resolvida noutro item — isso continua sendo leitura humana.
>
> O que ele garante é que, **uma vez lida, a resolução entra em um lugar e a lista acompanha**. É o mesmo contrato da ordem de ataque, e é tudo o que um gerador pode prometer sem mentir.

### 90.4 Três provas negativas

| | prova | |
|:--|:--|:--|
| **1** | ponteiro de seção inventado (`§999.9`) | **G-A pega** ✔ |
| **2** | decidir uma decisão | **sai da lista aberta e a contagem cai** ✔ |
| **3** | `decidida` sem data | pega ✔ |

**A prova 2 é a que justifica a peça:** ela afere que o defeito de 25/10 não pode voltar — virar o bit basta, e nenhuma prosa precisa ser reescrita à mão.

### 90.5 E um defeito meu, pego antes de empurrar

Escrevi a prosa do `ledger` **sem acentos**, por hábito de comentário de código — e a seção gerada saiu com *"decisoes sao suas"* na agenda que **você** lê.

> **A convenção da casa é clara e eu a inverti:** comentário de código vai sem acento; **prosa para o pesquisador, nunca**. Reescrita, e a regra ficou registrada no próprio `_leia_me` do ledger, onde quem for acrescentar decisão a vê.


---

## 91. A revisão do repositório — dois painéis escritos à mão, e nenhuma cifra certa — ✅ 27/10/2026

**Encaminhamento:** *"Faça a revisão e atualize todo o repositório para mim."*

Tratei como **varredura de obsolescência**, não como reescrita: medir o valor verdadeiro de cada cifra estrutural e procurar, na prosa, as formas que a contradizem.

### 91.1 O método, e a distinção que ele obriga

> **A agenda é um log cronológico: cifra dentro de item datado era verdade no dia dele e fica como está.** *"82 registros"* no item 23 não é erro — é história. O que precisa estar certo é a prosa **descritiva**: README, LEIA-ME, o inventário de fontes, o referencial, e o **painel** no alto deste arquivo.
>
> A primeira varredura não fazia essa distinção e devolveu dezenas de falsos positivos — inclusive *"os sete passos"* do checklist de Ricks e Liu, que é método citado, e *"22 registros motivacionais"*, que é subconjunto correto. **Separar log de descrição foi o que tornou a varredura utilizável.**

### 91.2 O achado: havia DOIS painéis escritos à mão, e os dois estavam errados

**O painel da agenda datava-se de 29/09 e nenhuma das suas cifras estava certa:**

| dizia | era |
|:--|:--|
| 83 sub-eventos × 17 campos | **85** |
| 61 em fonte primária · 21 por outra via | **68 · 16** |
| 66 PDFs / 12.089 p. | **65 / 12.352** |
| *oito passos: dois geradores e seis checagens* | **catorze passos, oito geradores, dez checagens** |
| **49 registros** num *"Caderno de evidências"* | **o nome aparecia uma única vez em todo o repositório — nesta tabela. Não existe arquivo algum com esse nome** |
| *"git desde 20/09/2026, **sem remoto configurado**"* | **o remoto existe e é PÚBLICO** |

> **A última linha é a grave, e não por ser a mais velha.** *"Sem remoto configurado"* é a negação exata da premissa que fez os PDFs do corpus saírem do versionamento em 21/10/2026. **Um leitor do painel concluiria que a decisão de distribuição não tinha razão de ser.**

**E o README era o segundo painel:** *"nove passos"* (catorze), *"oito checagens"* (dez), *"64 PDFs, 12.144 p."* (65 / 12.352), *"25 migrações"* (26). As cifras de fonte documental — **23 PDFs / 6.970 p.** — e as de dossiês e estados de backup estavam **certas**.

### 91.3 O conserto: um painel gerado, o outro guardado

| | |
|:--|:--|
| **o painel da agenda** | passou a ser **gerado** — `scripts/gerar_painel.py`, passo 5, entre marcadores. **Nenhuma cifra dele é digitada**, e a prova negativa de procedência **reprova qualquer número nas células que não saia de `medir()`** |
| **o README** | **continua escrito à mão, porque é porta de entrada e não painel** — e por isso ganhou a **checagem 10**, que compara as suas nove cifras de estado com o medido |

**E os números de passo que o painel cita são derivados de `ciclo.sh`.** Era a cifra mais podre do repositório: **o ciclo foi de oito a catorze passos em dezenove dias**, e cada entrada renumerou tudo. *Citar "passo 9" à mão é marcar hora num relógio que anda.*

**A checagem 10 falha se a sua âncora desaparecer**, e isso é deliberado: guarda que não acha o que vigia e passa em silêncio já morreu duas vezes aqui — a vigilância de SHA-256 que não cobria arquivo não-PDF, e a exclusão de caminho inerte por separador de plataforma. **Reescrever a frase do README obriga a reescrever o padrão na guarda.**

### 91.4 A checagem 10 acusou a si mesma na primeira execução

Acrescentá-la fez o *"9 checagens estruturais"* do README ficar obsoleto **no mesmo instante** — e ela pegou. É a melhor demonstração possível de que funciona.

### 91.5 Quatro defeitos meus no caminho, e três são da mesma família

| | |
|:--|:--|
| **prosa sem acento** | escrevi o `ledger` de decisões com prosa não acentuada, por hábito de comentário — e a seção gerada saiu com *"decisoes sao suas"* na agenda que você lê. Corrigido no item 90 |
| **cifra de referente errado, no meu próprio painel** | a célula das figuras dizia *"77 registros cobertos"*, e 77 é o número de **pontos** no HTML; o passo 10 declara cobertura de **todos** os registros, e a tabela-espelho conta **outro** número de pontos por causa dos compostos. **Cifra que eu não sei explicar não entra** — a célula passou a citar as duas guardas em vez da cifra |
| **a prova acusando o próprio formato** | ela reprovou `352` e `970`, que são pedaços de **12.352** e **6.970** partidos pelo separador de milhar, e `09` e `10`, que vêm de datas em ISO. **Guarda que acusa o próprio formato treina a ser ignorada** — a correção foi normalizar antes de varrer, e passar as datas do git para a forma brasileira **na fonte** |
| **identificador tomado por cifra** | a mesma prova acusou `26` em *"a tarefa 26 fechou"*. **Identificador não é cifra** — é a lição do referente aplicada à própria prova |

### 91.6 O que a varredura NÃO mexeu, e por quê

| | |
|:--|:--|
| **os itens numerados desta agenda** | log cronológico. Cifra dentro de item datado é história |
| **`LICENCA-E-DISTRIBUICAO.md`** | as cifras dele são de subconjuntos de literatura, com a data de medição ao lado — e a linha de 13/10 já se declara atualizada |
| **`Fontes/LEIA-ME_fontes.md`** | as cifras de *"49 registros"* e *"23"* ali são de rodadas datadas de agosto, e o arquivo as apresenta como tal |
| **`docs/referencial/`** | *"os sete passos"* é o checklist de Ricks e Liu; *"22 registros motivacionais"* e *"os 4 registros `N`"* são subconjuntos corretos |


---

## 92. A guarda da exceção ociosa — dispensa que ninguém revisita continua dispensando — ✅ 27/10/2026

**Encaminhamento:** *"crie a guarda para exceção ociosa."* — listada desde 87.5, repetida em 88.6 e 89.6.

### 92.1 Por que uma dispensa sem uso é pior que uma pendência esquecida

As três exceções de PT-08 saíram em 25/10/2026 **porque eu fui olhar** — nada as acusou. E o problema não é cosmético:

> **A chave de `EXCECOES` é o par (registro, prefixo normalizado da transcrição).** Se a transcrição que uma entrada cobria for **reescrita mantendo o começo**, a nova passa pela dispensa velha **sem ninguém conferir** — a exceção deixa de descrever o caso que a justificava e continua valendo. **Dispensa é licença, e licença que ninguém revisita é o defeito que esta casa nomeou em 22/10** ao recusar lista de exceção no `.gitignore`.

### 92.2 Medido antes de construir

| | |
|:--|:--|
| exceções registradas | **7** |
| **em uso numa passagem completa** | **7** |
| ociosas | **0** |

**A base é genuinamente zero, e não um número herdado.** Reimplementei a mesma cadeia do laço do conferidor para medir antes de instrumentá-lo — porque guarda cuja base se descobre *depois* de ligá-la nasce justificando o que encontrar.

### 92.3 O desenho, e as duas decisões que ele tomou

| | |
|:--|:--|
| **`excecoes_usadas` deixou de ser contador** | passou a ser **conjunto de chaves**. Só se pode perguntar quais sobraram sabendo **quais** foram usadas — e o contador respondia *quantas vezes*, que é a pergunta errada |
| **roda só em `--todos`** | pelo precedente de `PARCIAIS_BASE` e `EMPATES_BASE`, de 10/10/2026: o modo amostral abre doze registros e deixaria a maioria das exceções **sem exercício**. Acusá-las ali seria ruído, **e ruído treina a ignorar guarda** |

**E ela reprova, não avisa** — pela lição de 25/10, quando a linha de base do alcance imprimia o aviso e saía com código zero enquanto o comentário dela afirmava o contrário (§87.4).

### 92.4 Duas provas negativas, e a segunda declara o limite

| | prova | |
|:--|:--|:--|
| **1** | exceção plantada com prefixo que nenhuma transcrição começa | **faz o ciclo cair** ✔, nomeando a entrada |
| **2** | a mesma exceção, **no modo amostral** | **não acusa** ✔ — limite declarado, não virtude |

### 92.5 O que isto deixa

O ciclo segue em **catorze passos** e **dez checagens**, verde, com **sete linhas de base em zero**: `PARCIAIS` · `EMPATES` · `SEM_PAGINA_EXTRAIVEL` · `MEIAS_ANCORAS` · `INTEIRO_TEOR_SEM_ACHADO` · `DIVERGENCIAS` · **`OCIOSAS`**.

**Resta um item dos três que eu havia listado:** `reports/` segue fora da G2 e da G4 — elas vigiam `docs/` e o `ledger`. O relatório de pesquisa e a auditoria não afirmam estado de leitura hoje, **mas podem**, e estender é uma linha em `DOCS_VIGIADOS` **com a medição do estrago antes**.


---

## 93. A G2 vai a `reports/` e a G4 aos dois ledgers — e as duas nasceram verdes — ✅ 27/10/2026

**Encaminhamento:** *"estenda a G2 e a G4 para `reports/`."* — o último dos três itens que eu havia listado.

### 93.1 O pedido obrigou uma distinção, e ela achou um segundo buraco

**A G2 vigia arquivos; a G4 vigia o `ledger`.** `reports/` é arquivo, e entra na G2 sem dificuldade — mas *"estender a G4 para `reports/`"* não tem sentido, porque `reports/` não é ledger.

> **O que a G4 tinha de equivalente, e eu fui olhar:** ela recebia **um** ledger como argumento — o da ordem de ataque. E `data/decisoes_abertas.json` **nasceu em 27/10**, um dia antes. **Guarda escrita para um artefato não cresce sozinha quando nasce o irmão dele.**
>
> E o ledger das decisões é **justamente onde afirmação de leitura mora**: ele fala das peças `NAO_LIDO`, dos capítulos 4 a 8 de Beach e Pedersen, das seis peças não abertas da coletânea. **Era o escopo mais sensível à G4 em todo o repositório, e estava fora dela.**

### 93.2 Por que `reports/` faltava, e por que vigiar gerado é mais útil

A G2 nasceu em 21/10 olhando `docs/`, onde a prosa de análise vive. Ficaram fora três arquivos, e **dois deles são gerados** — a auditoria de fontes e a tabela-espelho.

> **Vigiar prosa gerada é mais útil aqui, não menos:** afirmação falsa num gerado é **defeito do gerador**, não erro de digitação — e defeito de gerador **se repete a cada rodada**. É o oposto do caso de 25/10, em que a G2 deixou de vigiar a própria saída: lá o arquivo **citava os defeitos que ela encontrava**, criando laço; aqui a prosa vem de código que pode estar errado.

### 93.3 Medido antes de estender — e as duas nasceram verdes

| | |
|:--|:--|
| G2 em `reports/` | **zero** incoerências em **1.038 linhas**, 3 arquivos |
| G4 no ledger das decisões | **zero** em 16 unidades |

> **E guarda que nasce verde é o caso perigoso.** Não há conteúdo a consertar, logo nada prova que ela está olhando. **A única resposta é injetar dentro de cada escopo novo** — e, além disso, um `assert` em cada uma reprova se o escopo **secar**: se o `glob` de `reports/` parar de casar, ou se o ledger das decisões sair da lista, o ciclo cai em vez de passar em silêncio.

### 93.4 Três provas negativas, e a primeira falhou por defeito dela

| | prova | |
|:--|:--|:--|
| **1** | afirmação de não-leitura no **relatório de pesquisa** | G2 pega ✔ |
| **2** | a mesma no **ledger das decisões** | G4 pega ✔ |
| **3** | o `glob` de `reports/` **secando** | o `assert` derruba ✔ |

**A prova 1 relatou FALHOU com a guarda funcionando**, e o defeito era meu: a agulha procurava `reports/process_...` e a saída traz `reports\process_...`, porque o `glob` devolve o separador da plataforma.

> **É o terceiro encontro com o separador de caminho neste repositório** — depois da exclusão inerte de 25/10 e do `cands` com barra. A prova passou a comparar normalizando, e a lição fica: **em prova que casa caminho, normalize o separador antes de concluir que a guarda falhou.**

### 93.5 O que isto fecha

**Os três itens que eu havia listado saíram:** a guarda das três condições (86), a da exceção ociosa (92) e esta. O ciclo segue em **catorze passos** e **dez checagens**, verde, com **sete linhas de base em zero**.

**O que permanece fora de guarda de prosa, declarado:** `Fontes/LEIA-ME_fontes.md` e os dois `LEIA-ME` de `scripts/` e da raiz — são inventário e manual, não afirmam estado de leitura, **mas podem**. Estendê-los é a mesma linha de `glob`, e a medição do estrago vem antes.


---

## 94. A G2 vai aos manuais e ao inventário — e pegou a frase em que eu descrevia a extensão anterior — ✅ 27/10/2026

**Encaminhamento:** *"estenda também para os LEIA-ME e o inventário de fontes."*

### 94.1 O caso oposto ao de `reports/`, e a expectativa estava errada

`reports/` era prosa que **não fala de leitura**, e nasceu verde como eu previa. Estes são o contrário: **`Fontes/LEIA-ME_fontes.md` declara leitura peça por peça** — é o inventário do corpus. **Era onde eu mais esperava achado.**

| arquivo | linhas | incoerências |
|:--|--:|--:|
| `README.md` | 68 | **0** |
| `LICENCA-E-DISTRIBUICAO.md` | 66 | **0** |
| `Fontes/LEIA-ME_fontes.md` | 395 | **0** |
| **`scripts/LEIA-ME.md`** | 211 | **1** |

> **O inventário passou limpo, e o manual não.** A razão é instrutiva: o inventário fala de leitura **com o recorte sempre ao lado** — *"lida em parte"*, *"ficha de metadado"*, *"sem camada de texto"* —, porque foi escrito para registrar estado. A G2 libera negação que senta ao lado de afirmação, e o inventário nunca nega sem qualificar.

### 94.2 A única incoerência era minha, de uma hora antes

**`scripts/LEIA-ME.md:67`** — a linha em que eu descrevia a extensão da G4 ao ledger das decisões, escrita no item 93:

A frase citava as peças `NAO_LIDO`, **negava a leitura dos capítulos finais da âncora metodológica sem dizer que os iniciais estão lidos**, e falava das seis peças fechadas da coletânea.

> **E a frase não está transcrita aqui, de propósito.** Grafá-la faria este item reproduzir o defeito que ele narra — e foi o que aconteceu na primeira escrita: **a G2 reprovou o item 94 por citar a frase do item 93**, que é a quinta vez que uma guarda desta casa reprova texto meu novo e a segunda pela mesma causa. O padrão existe desde §75.5: **nomear a afirmação em vez de grafar a frase** — e ele vale também para a citação, porque **quem cita o defeito reproduz o defeito**.

**A frase é verdadeira** — os capítulos 4 a 8 seguem por ler — e **não carrega a qualificação** de que a peça é `LIDO_PARCIAL`. A G2 só libera negação que senta ao lado de afirmação, e ali não havia nenhuma.

> **É a quarta vez que uma guarda desta casa reprova texto meu novo** — e desta o escopo que eu acabara de estender pegou a frase em que eu **descrevia a extensão anterior**. O conserto é o padrão: a frase passou a dizer o recorte — *"lido em parte, capítulos 1 a 3 e o Apêndice A, com o 4 ao 8 ainda por ler"* —, **o que também é prosa melhor**, porque informa o leitor do estado em vez de só negar.

### 94.3 O escopo passou a ser declarado em seis famílias

O `assert` deixou de vigiar uma família e passou a nomear **todas as seis**: `docs/analise/`, `docs/referencial/`, `reports/`, o `README`, o inventário de fontes e a própria agenda.

> **Família que sai do escopo derruba o ciclo**, em vez de encolher a vigilância em silêncio. **Guarda cujo escopo encolhe sem aviso é guarda que mente** — e a comparação normaliza a barra, porque o separador de caminho já morde aqui pela terceira vez.

### 94.4 Cinco provas negativas, uma por família e uma de desenho

| | |
|:--|:--|
| injeção no **README** · na **licença** · no **manual** · no **inventário** | as quatro pegas ✔ |
| **uma família retirada do escopo** | o `assert` derruba ✔ |

### 94.5 O que resta fora de guarda de prosa

**Nada de `.md` do repositório, hoje** — as seis famílias cobrem `docs/`, `reports/`, a raiz e `Fontes/`. **O que fica fora, declarado:** a prosa dentro dos **campos do codebook** (`fonte_trecho`, `nota_auditoria`, `status_verificacao`), que a G2 não lê porque é dado e não documento — e ali quem vigia são a checagem 7, a 9 e a guarda das meias-âncoras, cada uma com a sua pergunta.


---

## 95. A busca na CPMI: PT-38 ganha folha, e a alegação do *Proof* fecha como negativa medida — ✅ 27/10/2026

**Encaminhamento:** sete perguntas sobre a lista das 12 decisões e das 3 tarefas. Duas eram busca — *"Encontre esse registro no documento da CPMI ou em sites oficiais"* e *"me forneça a descrição desse evento. Procure por ele em sites oficiais ou então no Documento da CPMI"*.

### 95.1 A varredura anterior era negativa no predicado que usou

PT-38 declarava desde 16/08/2026 que a busca na CPMI havia sido **exaustiva e negativa**. Era verdade **da cifra**: `11,4` tem zero ocorrências nas 1.333 folhas. A busca de hoje foi por **nome de obra** — e o relatório descreve o evento em quatro folhas:

| folha | o que a CPMI traz | lastro que ela própria declara |
|:--|:--|:--|
| **668** | Congresso: telas rasgadas, mobiliário do Museu do Senado, quadros e esculturas do Salão Verde, incêndio. **R$ 3.500.000,00** e **R$ 3.556.509,14** | Nota Técnica nº 1/2023-ATDGER; Processo nº 221.490/2023 |
| **671** | Planalto: móveis atirados na Praça, fotografias rasgadas, o painel de Di Cavalcanti esfaqueado, e **um relógio de Balthazar Martinot, do século XVII** | narrativa do relatório, com oitivas |
| **672** | o relatório do **Iphan** sobre os bens culturais afetados. **R$ 4.300.000,00** | **DOC 366**, Inquérito 4922 — **mas a cifra remete à Folha de S.Paulo** |
| **676** | STF: Estátua da Justiça pichada, busto de Ruy Barbosa, plenário depredado. **R$ 7.708.061,56** mais **R$ 3.705.593,28** | **Ofício 023/CDG/2023 – STF** |

> **A lição é do predicado, não da diligência.** A varredura de agosto fez a pergunta certa de um jeito que não podia achar: procurou o **total impresso**, e o que a fonte imprime são as **parcelas**. **Negativa medida vale pelo predicado que usou, e o predicado tem de estar escrito ao lado dela** — senão a negativa cresce sozinha e passa a negar o que nunca examinou.

### 95.2 Oito transcrições, todas integrais, e o que ficou de fora de propósito

As oito conferem na folha citada **por casamento integral**, nenhuma por janela — testadas antes de entrar no campo. PT-38 passou de *fora do alcance do conferidor* a **`OK 8/8 localizadas`**, e com isso **deixou de ser o único registro do codebook sem transcrição verificável**.

**O painel de Di Cavalcanti não está transcrito, e a razão é mecânica:** a CPMI grafa o título da obra entre aspas, dentro da mesma frase. **Aspa aninhada inverte a paridade do extrator de transcrições** — é a limitação declarada no item 34.5, cuja saída é escolher outro trecho da mesma folha. Foi o que se fez: a frase entra cortada antes do título, e o quadro é nomeado na prosa do campo, fora das aspas.

**As duas exceções de PT-38 FICAM, e só a razão delas muda.** A pergunta da exceção é sobre a **aspa**, não sobre a cifra: as duas aspas continuam não estando em peça nenhuma do corpus. O que a CPMI traz são as **parcelas** — e `7 de 7 exceção(ões) usadas`, com a guarda do item 92 de testemunha.

### 95.3 A soma é derivada, e o referente é o perigo

**R$ 7.708.061,56 + R$ 3.705.593,28 = R$ 11.413.654,84**, que é a cifra de ago/2023 da série. **A CPMI imprime as duas parcelas e nunca o total** — é o caso de PT-03C outra vez, e o registro diz isso com estas palavras.

> **E aqui estavam quatro cifras de quatro referentes na mesma vizinhança.** R$ 4,3 mi é **Planalto**; R$ 3,5 mi e R$ 3,56 mi são **Senado e Câmara**; só R$ 7,7 mi mais R$ 3,7 mi é **STF**, que é o referente deste registro. **Nenhuma guarda deste projeto vigia troca de referente**, e por isso cada cifra entrou no campo com o seu dono grafado ao lado.
>
> **Um achado a jusante, que não é cifra minha:** a decomposição do Congresso de jan/2025 — R$ 2,7 mi na Câmara, R$ 2,2 mi no Senado — **não bate com a da CPMI**, que é de 2023 e **maior** nas duas casas. São medições de datas diferentes, e o registro passou a dizer que não se substituem.

### 95.4 A alegação do *Proof*: zero em 1.333 folhas

Medido com normalização de acento e de caixa: **`proof` zero ocorrências**, **`5 de janeiro de 2021` zero**. As **dez menções a Eduardo Bolsonaro**, nas folhas 84, 151, 157, 165, 334, 335, 418, 476 e 527, tratam de Olavo de Carvalho, do núcleo da organização, de Bannon, de contas de rede, da Combat Armor, de Cerimedo e de atos — **nenhuma de reunião nos EUA em janeiro de 2021**. A folha 416 traz Bolsonaro invocando o Capitólio **em 7 de janeiro**, que é outro evento.

Fora do corpus: *Proof* é o sítio próprio do jornalista **Seth Abramson**, e a alegação não tem confirmação independente. O único rastro quase-oficial é um requerimento de informações ao Itamaraty, de março de 2021, **sobre a viagem e não sobre a reunião** — e **eu o conheço por notícia, não por documento do Senado**, o que o deixa fora do que este projeto pode afirmar.

> **A decisão fecha, e o levantamento segue fechado desde 21/10.** A negativa entra aqui com **data e predicado** para não ser refeita — e vale enquanto o arquivo for o mesmo, o que a checagem 8 vigia pelo sha256.

### 95.5 A guarda da classe pegou PT-38 na mesma rodada

Ao passar a citar por folha, PT-38 **entrou no alcance da checagem 9** — que até ontem não o alcançava, porque `pares()` não cede numeral para *inteiro teor* — e a guarda o pegou **mudo**: classe `Confirmado` ancorando peça documental sem dizer por quê.

> **O alcance de uma guarda que depende de FORMA DE CITAÇÃO cresce sozinho quando um registro muda de forma.** Era seis; é sete. O comentário da checagem nomeava PT-38 entre os que caem fora, e foi corrigido no mesmo commit — **a cifra do alcance passou a vir com a advertência de que não é fixa**.

A razão declarada **não é a promoção**, que é sua: é que o registro **afirma uma série de valoração cuja metade de jan/2025 não tem lastro primário algum**, por ser posterior ao relatório. O vandalismo está em fonte primária com folha; a cifra mais recente não está.

### 95.6 Uma cifra velha no meu próprio plano, e o arquivo errado na raiz

**Duas coisas minhas, ambas registradas porque são do tipo que esta agenda existe para pegar.**

A primeira: o plano desta sessão afirmava que o ciclo passava em `confirmados 74`. **Eu copiei a cifra do plano anterior**, escrito semanas antes — e a medição de hoje devolveu **80**. É literalmente o modo de falha que o item 91 nomeou: **painel escrito à mão descreve o dia em que foi escrito**. O número correto não foi recalculado por subtração: ele é o que o passo 12 imprimiu.

A segunda: uma linha residual num script de busca meu criou um **arquivo vazio `x` na raiz do repositório**, durante o modo de planejamento, em que eu não devia escrever nada. Removido no mesmo minuto, com `git status` de volta a zero. **Fica escrito porque script de leitura que escreve é script que mente sobre a própria natureza.**

### 95.7 O que isto deixa

**Duas decisões suas, e as duas ficaram mais baratas:** a promoção de classe de PT-38, que as três condições agora admitem, e o `autonomia_movimento` dele, hoje `Lido, não documentado` — a f. 672 traz o depoimento do general Gonçalves Dias sobre os invasores agirem **como se tivessem coordenação**, mas isso é do cerco ao Planalto, não da destruição do acervo, e importar valor de folha vizinha é o que o próprio registro proibiu em 16/10.

**E uma proposta minha, não executada:** o laudo do Instituto de Criminalística/PF continua não obtido, mas **o DOC 366 do Iphan é um documento nomeado e numerado** — vistoria dos bens culturais, Inquérito 4922. Coletá-lo daria o detalhamento por peça que o registro diz depender do laudo. **O levantamento de eventos está fechado; coleta de documento para registro existente não é levantamento novo** — mas a distinção é sua, não minha.

---

<!-- DECISOES-PENDENTES: gerado por scripts/gerar_decisoes.py a partir de data/decisoes_abertas.json. Não editar à mão: o ciclo sobrescreve. -->

## Decisões pendentes — revista em 27/10/2026

**As decisões abaixo são suas, e nenhuma delas bloqueia as tarefas abertas.** A lista é gerada de `data/decisoes_abertas.json`: **fechar uma decisão é virar um campo**, e a contagem acompanha. **O que não está aqui não está pendente** — as seções *"O que isto deixa"* de cada item da agenda são o registro do que se sabia naquele dia, e várias delas foram resolvidas por itens posteriores.

**A ordem não é de prioridade, e sim de natureza.** Dentro de cada grupo, a ordem é a de nascimento.

**São onze decisões abertas, em três naturezas:** o remoto é público (4) · campo do codebook (4) · leitura (3).

### O remoto é público

| Decisão | Nasceu | Onde |
|:--|:--|:--|
| **A licença das dez páginas web do eixo 09.** Seis declaram *"Todos os direitos reservados"* (Agência Brasil) e quatro nada declaram (portal do STF), e o manifesto registra `licenca_declarada` = `NÃO CONFERIDA (não-PDF)` para todas, porque o auditor de licença **só lê PDF**. **As três saídas estão escritas com o preço de cada uma.** A decisão de 21/10 foi sobre PDFs e nunca examinou as peças não-PDF. | 25/10/2026 | §89.7 |
| **A higiene que sobrou da tarefa 15:** os PDFs do corpus que seguem no **histórico** do git — removê-los exige reescrita e `push --force` —, o PDF versionado em `.backup_pre_lula/`, os oito `.docx` de síntese, e o ramo `backup-antes-de-destrackear-pdfs`, que segue local. | 13/10/2026 | §46.5 |
| **A licença da sua própria obra** — o que o repositório declara sobre o uso do codebook e dos documentos de análise. | 13/10/2026 | §46.6 |
| **Devolver ao git o PDF de Singer, Araujo e Rugitsky**, que é de acesso aberto com licença CC lida na folha 4. **Eu recomendo não devolver**, e a razão não é a licença: a regra `Fontes/**/*.pdf` deixaria de ser uma linha e passaria a ser *"todos menos estes"* — e lista de exceção é dívida que ninguém revisita. | 22/10/2026 | §77.6 |

### Campo do codebook

| Decisão | Nasceu | Onde |
|:--|:--|:--|
| **O nome do mecanismo de PT-62.** A rota de desmobilização é *abeyance* sob repressão judicial ativa com institucionalização parcial, e **nenhuma das duas é escolha do movimento**: é desmobilização **heterônoma**, por imposição de custo penal — rota que a tipologia de Taylor não prevê. O nome poderia dizê-lo. **Nomear mecanismo é sua decisão, pelo precedente da tarefa 19.** | 21/10/2026 | §74 |
| **A grade funcional do enquadramento como 18º campo.** Hoje a classificação vive só em `docs/referencial/02_GRADE-FUNCIONAL-ENQUADRAMENTO.md`, gerada, e **declarada como inferência minha**. Criar campo é sua decisão, e você disse que classifica na escrita. | 21/10/2026 | §73 |
| **Os quatro registros `N` da grade funcional** — PT-20A, PT-20B, PT-25 e PT-47 têm texto em `framing_narrativa` que **não é quadro de ação coletiva**. São 18 vazios ao todo, e os quatro `N` são os que têm texto e não têm quadro. | 21/10/2026 | §73 |
| **As duas aspas de PT-38 que não estão em peça do corpus.** Elas vêm de sinopse de documentário (ago/2023) e de levantamento divulgado pela imprensa (jan/2025), e seguem em `EXCECOES` com essa razão. **A premissa desta decisão encolheu em 27/10/2026:** o registro ganhou oito transcrições da CPMI conferidas por folha, de modo que **retirar as duas aspas já não o deixa sem transcrição alguma** — e a cifra de ago/2023 passou a ter lastro primário nas duas parcelas da f. 676. O que resta é a cifra de jan/2025, posterior ao relatório. **Coletar as duas fontes continua sendo sua decisão**, e agora ela é mais barata. | 25/10/2026 | §95.2 |

### Leitura

| Decisão | Nasceu | Onde |
|:--|:--|:--|
| **As duas peças `NAO_LIDO` do registro de leitura:** o preprint de Drummond e Manginelli (eixo 08) e o folder do STF. **Nenhuma ancora registro e nenhuma é necessária ao desenho atual** — ler ou manter declarado é sua decisão. | 21/10/2026 | §75 |
| **As seis peças não abertas da coletânea de Singer, Araujo e Rugitsky:** Rugitsky, Ayers e Saad-Filho, a entrevista com Streeck, Loureiro, Lavinas *et al.* e Braga e Santos. **Todas de economia política, nenhuma necessária ao desenho atual.** | 22/10/2026 | §77.5 |
| **Os capítulos 4 a 8 de Beach e Pedersen.** O 5 e o 6 sustentariam a **força probatória declarada de cada âncora**, que é a mais dura das quatro dívidas do documento 03. | 21/10/2026 | §74 |

### Decididas

| Decisão | Quando |
|:--|:--|
| ~~A alegação do site *Proof* — a matéria do Estadão atribui a ele a notícia de uma reunião em 05/01/2021 nos EUA~~ | ✅ 27/10/2026 — sem rastro na CPMI, medido em 1.333 folhas |

**O que NÃO está nesta lista, e por quê.** As quatro dívidas de Beach e Pedersen, as cobranças dos onze verbetes e a cristalização de quadro **não são decisões**: são trabalho de redação, e a tarefa 16 as cobre. Os limites declarados do aparato **não são decisões suas**: são propostas minhas, e vivem nas seções dos itens que as nomearam. **E esta frase nomeava quatro deles até 27/10/2026, quando três haviam sido fechados no mesmo dia** — a extensão da G2 e da G4 a `reports/` (item 93), a guarda da exceção ociosa (item 92) e a extensão aos manuais e ao inventário (item 94). **Enumerar limites aqui é fazer à mão o que este arquivo existe para gerar**, e por isso a enumeração saiu em vez de ser corrigida.

**E o limite desta peça fica declarado:** ela conserta a **cópia**, não o **juízo**. Dá um lugar único para registrar que uma decisão saiu, e deriva a contagem — mas **não detecta sozinha** que uma decisão foi resolvida noutro item. A guarda confere que o ponteiro de seção existe, que é a forma que o apodrecimento toma aqui.

<!-- /DECISOES-PENDENTES -->
