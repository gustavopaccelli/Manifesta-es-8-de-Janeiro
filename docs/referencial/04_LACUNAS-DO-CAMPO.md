# As lacunas que a literatura declara — e o que este material responde

**21/10/2026.** Encaminhamento do pesquisador sobre as três que eu havia listado como exigindo trabalho novo: *"resolva essa tarefa"*.

**O que foi feito, e a distinção importa:** **duas das três se resolvem com o que o repositório já tem** — e estão resolvidas abaixo, como inferência declarada. **A terceira não se resolve, e a razão é medida, não de opinião:** o corpus não contém o dado que ela exige. O que se entrega para ela é o **desenho mínimo** que a tornaria resolvível.

---

## 1. Cristalização de quadro ao longo do tempo — **NÃO resolvível com este corpus**

**A lacuna, na voz da fonte.** Snow, Vliegenthart e Ketelaars (2019, p. 400 impressa): *"there has been **little comparable research on the factors that account for the crystallization of some frames and the corresponding decline of other frames over time**"*. O precedente empírico é do próprio coautor: nos motins franceses de 2005, ao longo de três semanas, o diagnóstico por categorias sociais declinou e o estrutural cresceu.

**Por que eu dizia que o corpus a respondia, e por que estava errado.** `docs/analise/10` afirma que *"o eixo 08 do corpus é cobertura de imprensa, e `gerar_catalogo_imprensa.py` já o cataloga"*. **Medido em 21/10/2026:**

| O que se mediu | Resultado |
|:--|:--|
| peças em `Fontes/08_Imprensa-enquadramento/` | **uma** — um preprint do SciELO sobre editoriais (Drummond e Manginelli, 2023), 24 folhas |
| o relatório do Manchetômetro (`Doxa-IESP-UERJ`, 16 folhas), que ancora PT-50A | é **análise de volume em redes sociais** — publicações e interações por dia e por tipo de página. Ocorrências de `enquadr`: **zero**. De `frame`: **zero**. De `semana`: **zero** |
| o que `gerar_catalogo_imprensa.py` cataloga | **atribuições de número de manifestantes na imprensa** — e o próprio cabeçalho declara-se instrumento separado do codebook |

> **Não há no corpus uma série temporal codificável de quadros.** O que há é: um recorte de **48 horas** em PT-50A, dois dias de volume de redes no Manchetômetro, e um estudo de editoriais. **Medir cristalização exige codificar quadro por peça ao longo de semanas, e isso é coleta nova.**

### O desenho mínimo que a tornaria resolvível

| | |
|:--|:--|
| **unidade** | a peça jornalística (editorial, notícia, coluna), não o dia |
| **janela** | de 08/01/2023 a, no mínimo, 31/01/2023 — três semanas, que é a janela do precedente de 2005 |
| **grade de codificação** | ela **já existe** e é a deste repositório: as três tarefas centrais de enquadramento, em [`02_GRADE-FUNCIONAL-ENQUADRAMENTO.md`](02_GRADE-FUNCIONAL-ENQUADRAMENTO.md), mais os quadros concorrentes nomeados — *"atos golpistas"*, *"manifestação"*, *"terrorismo"*, *"infiltrados"*, *"o governo sabia"* |
| **o que mediria cristalização** | a proporção de peças por quadro, por semana. Cristalização é a **ascensão de um quadro sobre os competidores**; o que o projeto tem hoje é o ponto de partida (PT-50A, a contraofensiva em 48 horas) e o ponto de chegada (PT-53, PT-56: o quadro penal vence), **sem a curva entre os dois** |
| **o custo** | é coleta e codificação, não leitura — e fica **fora** do levantamento de eventos, que o pesquisador fechou em 21/10/2026 |

**O que o projeto PODE afirmar hoje, sem a série:** que houve **disputa** de quadro, documentada nos dois extremos; e que a recaptura em cerca de 48 horas é **volatilidade de oportunidade discursiva** (McCammon *et al.* 2007, no verbete de DOS). **Não pode afirmar cristalização**, que é uma afirmação sobre curva.

---

## 2. A clivagem social do campo multiorganizacional — **RESOLVIDA, como inferência declarada**

**A lacuna, na voz da fonte.** Klandermans (2013, p. 407-408 impressa): *"The composition of a movement's organizational field is **not random, but relates to existing cleavages in a society**."*

**O que o repositório já tem:** `data/processed/campo_multiorganizacional.csv`, gerado por `scripts/desenhar_campo.py`, com **22 entidades** classificadas por sistema (aliança, conflito, indiferente, cindida, migrante, contestada) e por tipo de recurso, cada uma com os registros que a ancoram. **O que faltava era ler o campo contra a clivagem** — e é isto:

### 2.1 As quatro clivagens que organizam o campo

> **É inferência do analista**, de 21/10/2026, sobre as 22 entidades do CSV. O critério está escrito em cada linha; o leitor pode discordar de uma atribuição sem rediscutir o método.

| Clivagem | Sistema de aliança | Sistema de conflito | O que a clivagem explica |
|:--|:--|:--|:--|
| **C1. Agrário-exportadora × regulação federal** | MBVA/Aprosoja (material), caminhoneiros (humano), caravanas e seus financiadores (material) | — | **a capacidade material**: frota, combustível, logística interestadual. É a clivagem que explica por que a mobilização tinha meios próprios e não dependia de arrecadação difusa |
| **C2. Digital-plataformizada × imprensa e arbitragem institucional** | perfis e canais bolsonaristas, anunciantes não identificados | Plataformas da Meta (**indiferente**, não aliada) | **a capacidade de convocação**: alcance sem intermediário. E a posição *indiferente* da Meta é analiticamente relevante — a plataforma não é aliada do campo, é infraestrutura que não o barrou |
| **C3. Militar-corporativa × ordem constitucional civil** | Forças Armadas (**CINDIDA**), PMDF (**CINDIDA**) | Forças Armadas, PMDF | **a clivagem decisiva, e a única que atravessa entidades em vez de separá-las.** As duas corporações aparecem nos dois sistemas: é o que o CSV chama de *cindida*, e é o que explica PT-31 (PMs sinalizam para prosseguir) ao lado de PT-43 (reforço do CMP retoma o palácio) |
| **C4. Executivo eleito × árbitros do jogo** | Presidência até 31/12/2022 (moral), Coligação Pelo Bem do Brasil (moral) | STF, Congresso, TSE, PF, PGR, governo federal a partir de 01/01/2023 | **a legitimidade**: o recurso que o campo de aliança perde e o de conflito ganha na virada do ano |

### 2.2 Os três achados que a leitura por clivagem produz

**(a) O campo não é simétrico em tipo de recurso, e a assimetria é a sua estrutura.** O sistema de **aliança** reúne entidades classificadas por **material**, **humano**, **moral** e **social-organizacional** — isto é, recursos que se **acumulam**. O sistema de **conflito** reúne, sem exceção, entidades cujo recurso o CSV registra como `—`: são **instituições**, cujo poder não é recurso acumulável, é **autoridade**. **A disputa não é entre dois estoques de recursos; é entre estoque e autoridade** — e essa é a leitura que a clivagem C4 dá.

**(b) A migração acontece em entidades do Estado, não do movimento.** As duas entidades **MIGRANTE** do CSV são **Anderson Torres / MJ / PRF** e **Ibaneis Rocha / GDF** — as duas estatais. Nenhuma entidade do campo desafiante migra. **O que o verbete prevê como dinâmica esperada do campo** — *"former allies can become opponents"* — **realiza-se aqui dentro do aparato estatal**, não entre organizações de movimento. É uma precisão que o verbete não antecipa e que o caso oferece.

**(c) E a entidade CONTESTADA é uma só, e é onde a causalidade do dia se decide.** A *cúpula da segurança pública do DF* (SSP-DF, SOI, GSI) ancora PT-18, PT-19B, PT-20A e PT-20B — quatro registros de **informação que não se converteu em ação**. O CSV a classifica como contestada porque é exatamente o ponto em que as hipóteses rivais de PT-28 se separam: seletividade estrutural (Rival 1) ou sobrecarga analítica (Rival 2), ambas de della Porta e Reiter.

### 2.3 O que esta resolução NÃO faz

Não mede a clivagem contra dados de estrutura social brasileira — renda, setor, região — porque esses dados **não estão no corpus**. As quatro clivagens são lidas **das entidades que o codebook ancora**, e é isso que as torna verificáveis: cada atribuição aponta para registros com fonte.

---

## 3. A rota de desmobilização de PT-62 — **RESOLVIDA, como inferência declarada**

**A lacuna, na voz da fonte.** Fillieule (2013, p. 177-180 impressa): *"at the meso-sociological level, we still **lack a reliable typology** of the diversity of routes chosen by social movement organizations that are undergoing a process of demobilization"* — as rotas identificáveis, a partir de Taylor (1989), sendo **burocratização**, **institucionalização**, **assimilação pelo Estado**, **radicalização** e ***abeyance***.

**O que PT-62 afirma hoje:** *"Desmobilização por repressão seletiva, seguida de migração de arena"* — dois mecanismos, nome atribuído em 10/10/2026, com `status_classe` = **Inferência do analista**, o único registro do codebook nessa classe.

### 3.1 PT-62 contra as cinco rotas

| Rota, na tipologia | Definição | O caso é dela? |
|:--|:--|:--|
| **burocratização** | profissionalização da organização, com quadros pagos e rotina administrativa | ❌ não há organização formal a burocratizar: o campo era rede |
| **institucionalização** | conversão do repertório de rua em participação em arenas instituídas | 🔶 **parcialmente** — a migração para a arena eleitoral e para o debate de anistia no Congresso é isso. Mas institucionalização, na tipologia, é escolha **do movimento**; aqui a rua cessa por **operação do Estado** |
| **assimilação pelo Estado** | cooptação, com o movimento absorvido pela estrutura que contestava | ❌ é o inverso do que ocorreu: a estrutura estatal **processou penalmente** o campo |
| **radicalização** | deslocamento para formas mais confrontativas por uma fração | ❌ não como desfecho: a radicalização é **anterior** (PT-15, PT-16) e culmina no próprio 8/1 |
| ***abeyance*** | estruturas de sobrevivência que mantêm identidade e rede em período hostil, sem ação pública | 🔶 **parcialmente** — *"perseguição política"* e *"anistia"* são os quadros de uma rede que persiste sem repertório de rua |

> ### A resposta, e ela é uma contribuição à tipologia, não um encaixe nela
>
> **PT-62 não é nenhuma das cinco rotas, e é a combinação de duas sob uma condição que a tipologia não prevê.** A rota do caso é:
>
> **`abeyance` sob repressão judicial ativa, com institucionalização parcial da pauta.**
>
> Isto é: a rede **sobrevive** (abeyance) e parte da pauta **entra em arena instituída** (institucionalização, pela via da anistia e do pleito), **mas nenhuma das duas é escolha do movimento** — ambas são o que resta depois de o repertório de rua ser removido por operação estatal com data e decisão judicial (PT-52) e de a liderança ser encarcerada (PT-58, PT-59).
>
> **O que a tipologia de Taylor não prevê, e o caso exige:** as cinco rotas são **escolhas organizacionais** diante de contexto adverso. Aqui a desmobilização é **heterônoma** — o custo foi imposto, não calculado. **A rota que falta na tipologia é a desmobilização por imposição de custo penal**, em que a organização não escolhe entre sobreviver e institucionalizar-se: faz as duas porque as outras três lhe foram fechadas.
>
> **E isto fecha com a segunda lacuna do mesmo verbete** — *"explore the effects across time and space of the **failure** of a movement"* —, porque é precisamente um caso de fracasso com desfecho medido: 1.402 responsabilizados (PT-61).

### 3.2 O que isto cobrou do codebook — **adotado em 27/10/2026**

A proposta era que o nome de PT-62 passasse a dizer a rota, e o pesquisador **a adotou em 27/10/2026**: o mecanismo chama-se hoje **desmobilização heterônoma por custo penal: abeyance sob repressão ativa com institucionalização parcial da pauta**, e a §3.1 acima é o fundamento dele.

**A proposta ficou escrita e não executada por seis dias**, porque nomear mecanismo é decisão do pesquisador pelo precedente da tarefa 19 — e é esse o desenho: a §3.1 mede, a §3.2 propõe, e o campo só muda com a palavra dele.

**O que mudou junto, e por quê.** O nome retirado — *desmobilização por repressão seletiva, seguida de migração de arena* — entrou no registro de nomes retirados da checagem 7, e **a entrada que havia sido criada em 10/10 foi atualizada no mesmo movimento**, porque o nome que ela apontava como vigente era justamente o que saiu. Os dois rótulos internos do campo também mudaram: eles eram as duas metades do nome retirado, e deixá-los repetiria a lição do item 66 — **nome retirado de um registro não retira o conceito** se ele segue vivo como rótulo dentro do próprio registro.

**O que NÃO mudou:** o campo continua nomeando dois componentes, a classe continua `Inferência do analista`, e a âncora de Carvalho e Tatagiba (2025, f. 35) continua cobrindo 2023 e não a janela inteira. **Nenhum fato foi tocado.**

---

## 4. O balanço das oito lacunas declaradas pelo campo

| Lacuna | Fonte | Estado |
|:--|:--|:--|
| mecanismos que governam o **declínio** de movimentos | *Demobilization* | ✅ T+1 inteira, 20 registros datados |
| efeitos do **fracasso** de um movimento no tempo e no espaço | *Demobilization* | ✅ PT-62 e PT-61 |
| **desmobilização de recursos** não é o inverso da mobilização | *Resource mobilization theory* | ✅ PT-52 — remoção coercitiva com data e decisão judicial |
| como a **oportunidade de um nível impele o scale shift** | *Diffusion and scale shift* | ✅ barrado na urna e no quartel, desloca-se para a sede dos três poderes |
| **erros de enquadramento** como impedimento de mobilização | cap. 22 (2019) | ✅ um quadro **falso** que produziu mobilização de massa |
| **tipologia de rotas** de desmobilização | *Demobilization* | ✅ **resolvida nesta rodada** — §3, com uma rota que a tipologia não tem |
| **clivagem social** do campo organizacional | *Multiorganizational fields* | ✅ **resolvida nesta rodada** — §2, quatro clivagens |
| **cristalização** de quadro ao longo do tempo | cap. 22 (2019) | 🔶 **não resolvível com este corpus** — §1, com o desenho mínimo declarado |

**Sete das oito respondidas; uma com o desenho da coleta que falta.**
