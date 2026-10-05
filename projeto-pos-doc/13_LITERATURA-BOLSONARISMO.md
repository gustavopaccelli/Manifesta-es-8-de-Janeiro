# A literatura do bolsonarismo como fenômeno de mobilização — coleta da tarefa 25

**04/10/2026.** A tarefa 25 nasceu de madrugada, na primeira rodada da tarefa 14, com a seguinte formulação: *"a literatura do bolsonarismo (2018-2022) — Cesarino, Campos Mello, Abranches, Avritzer. É o que falta para PT-04, PT-05 e PT-06 saírem de contextuais, e não está em nenhuma das duas coleções já varridas."*

O pesquisador especificou o recorte: **o bolsonarismo enquanto fenômeno de mobilização social e política**, com foco nas dinâmicas de mobilização, manifestação e protesto, e em particular nas **formas de repertório específicas do campo das direitas**. Este documento registra a coleta feita sob esse recorte.

> **ATUALIZADO EM 04/10/2026, ao fim do mesmo dia: o eixo passou de catorze a DEZOITO peças, e a declaração de abertura deixou de valer para todas.** **TRÊS** foram lidas na fonte, por encaminhamento do pesquisador, e **ancoram registro com página**: `ARAUJO E SALES 2022`, `FERNANDES E SILVA 2021` e `VON BÜLOW E ABERS 2024` — esta na quarta rodada, e foi ela que **fechou PT-06**, o último contextual da camada brasileira. Quatro entraram porque o pesquisador **entregou as peças barradas**, e uma dessas quatro é justamente a que fechou PT-06. **As quinze restantes continuam coletadas e não lidas.**
>
> **A DECLARAÇÃO, AGORA COM A DISTINÇÃO QUE ELA PRECISA: das dezoito peças, três foram lidas e ancoram registro; quinze não foram lidas e não ancoram nada.** As quinze estão em `Fontes/13_Bolsonarismo-mobilizacao/` como **fila de leitura**, com proveniência declarada em `PROCEDENCIA` — que é o que `verificar_integridade.py` exige de todo arquivo que não ancora registro. Um arquivo dentro de `Fontes/` parece lastro, e estas quinze não são: quem for ancorar registro em qualquer uma delas precisa abrir, ler e pôr página, como se fez com as sete peças do eixo 12 e com as duas lidas aqui. **`PROCEDENCIA` declara o eixo 13 em três blocos de ORIGEM — doze coletadas, duas lidas que ancoram, quatro entregues — justamente para que a distinção não dependa deste documento. E note-se que origem e leitura são eixos independentes: a terceira peça lida vem do bloco das ENTREGUES, de modo que a contagem de lidas (três) não bate com nenhum bloco isolado.**

---

## 1. Como se buscou

**OpenAlex**, por consulta programática em `scripts`-de-rodada (`oa_busca.py`, mantido no diretório de trabalho da sessão). A escolha repete a de 29/09: **o OpenAlex responde sem identificação**, e nenhuma consulta deste projeto carrega o e-mail do pesquisador.

Dezessete consultas, em português e em inglês, recortadas em 2016-2026, cruzando quatro eixos: *bolsonarismo*, *extrema-direita / campo das direitas*, *mobilização / protesto / manifestação* e *repertório de ação coletiva*. Mais nove consultas por autor, com os nomes que a literatura brasileira já consagrou no tema — Cesarino, Messenberg, Camila Rocha, Esther Solano, Pinheiro-Machado, Tatagiba.

**345 obras distintas** na união das duas rodadas de busca — 151 na primeira, 214 na segunda, com **apenas 20 em comum**, o que diz que as duas estratégias de consulta varriam regiões diferentes da literatura e que nenhuma delas sozinha bastaria. A triagem dos títulos foi feita a olho, e dela saíram dezoito peças escolhidas por aderência direta ao recorte do pesquisador. **Catorze chegaram.**

> *A primeira versão deste parágrafo dizia "365 obras distintas", que é a soma de 151 e 214 — e as duas listas se sobrepõem em 20. A união é 345. A soma de duas buscas não é a união delas, e somar sem conferir a interseção é a forma aritmética do defeito que este projeto persegue desde agosto: o número certo medindo a coisa errada.*

**Cada peça foi conferida nos dois eixos da regra de 29/09** — *existir não é estar bem atribuído*. O DOI resolve **e** o título que a fonte devolve casa com o título esperado. Divergências de título: **zero em catorze**. E cada arquivo baixado foi conferido byte a byte: começa com `%PDF`, abre no PyPDF2, e a primeira página devolve texto. **Nenhuma peça do eixo 13 tem o problema do eixo 12** — todas têm camada de texto legível.

Uma peça precisou ser descartada depois de baixada: a tentativa na Cambridge devolveu **HTTP 429** com uma página de erro de 1,3 KB, que o `curl` gravou com extensão `.pdf`. Um HTML de erro guardado como PDF é exatamente o tipo de defeito silencioso que este projeto caça — foi apagado, e a peça está na lista de pendentes abaixo.

---

## 2. O que entrou — dezoito peças, 453 páginas

A coluna **serve a** diz qual registro a peça tem condições de ancorar **depois de lida**. É mapa de leitura, não âncora — exceto nas duas primeiras linhas, marcadas **LIDA**, onde já é âncora conferida pelo ciclo.

### 2.1 As três lidas, que ancoram registro

| Peça | Referência | p. | Offset | Ancora |
|:--|:--|--:|:--|:--|
| **ARAUJO E SALES 2022** — *LIDA* | "Atuação política das Forças Armadas e o fenômeno bolsonarista no Brasil (2013-2022)". *Cadernos do Tempo Presente*, 13(1):26-42 | 17 | impressa = PDF + 25, **derivado** | **PT-02** (genealogia do frame), **PT-04** (expressão antissistêmica), **PT-05** (cadeia causal — saiu de contextual), **PT-06** (repertório e enquadramento), **PT-12** (genealogia) |
| **FERNANDES E SILVA 2021** — *LIDA* | "Dinâmicas do controle à ação coletiva: o policiamento a protestos no Rio Grande do Sul". *Mediações*, 26(3):485-502 | 17 | impressa = PDF + 484, **lido** | **PT-02** — e **tirou do campo** a "tolerância policial", que contradisse |
| **VON BÜLOW E ABERS 2024** — *LIDA* | "Denialism and Populism: Two Sides of a Coin in Jair Bolsonaro's Brazil". *Government and Opposition*, 59:998-1016 | 19 | impressa = PDF + 997, **lido** | **PT-06** — **fechou o registro** e **retificou o mecanismo**: a infraestrutura informacional antecede a pandemia. Também **PT-05**, em corroboração dupla |

**O que a leitura dessas três produziu está no documento 12, §4 e §5.** Em duas linhas: uma afirmação de dez anos saiu do codebook porque a leitura a contradisse; e dois registros deixaram de ser contextuais, o segundo deles com o mecanismo **retificado** — a pandemia carrega uma infraestrutura anterior, em vez de consolidá-la.

**E um achado que não é de registro nenhum.** Von Bülow e Abers sustentam que o bolsonarismo é **movimento social com autonomia relativa**, um processo que *precedes his rise to power* e que o líder *does not fully control* (p. 1000 e 1009 impressas). Nenhum dos 16 campos do esquema codifica grau de autonomia, e por isso entrou como achado em `fonte_trecho`. É material de argumento para a redação, e está anotado como pendência de decisão no documento 12, §8, item 10.

### 2.2 As quinze não lidas

| Peça | Referência | p. | Serve a |
|:--|:--|--:|:--|
| MESSENBERG 2017 | "A direita que saiu do armário: a cosmovisão dos formadores de opinião dos manifestantes de direita". *Sociedade e Estado*, 32(3) | 27 | **PT-02** |
| ROCHA 2019 | "'Imposto é Roubo!' A Formação de um Contrapúblico Ultraliberal e os Protestos Pró-Impeachment de Dilma Rousseff". *Dados*, 62(3) | 42 | **PT-02, PT-03** |
| TATAGIBA 2018 | "Entre as ruas e as instituições: os protestos e o impeachment de Dilma Rousseff". *Lusotopie*, 17(1):112-135 | 20 | **PT-02, PT-03** |
| SANTOS E TANSCHEIT 2019 | "Quando velhos atores saem de cena: a ascensão da nova direita política no Brasil". *Colombia Internacional*, 99 | 37 | **PT-04** |
| CESARINO 2019 | "Identidade e representação no bolsonarismo". *Revista de Antropologia*, 62(3) | 28 | **PT-04** |
| KAYSEL E BIANCHI 2025 | "Bolsonarismo como coalizão discursiva de extrema-direita". *Caderno CRH*, 38 | 14 | **PT-04** |
| CARVALHO E TATAGIBA 2025 | "Quando o conflito eleitoral extravasa para as ruas: protestos e eleições presidenciais no Brasil". *Lua Nova*, 124 | 46 | **PT-04**, T₋₁ operacional |
| MENDONÇA E DOMINGUES 2021 | "Protestos contemporâneos e a crise da democracia". *RBCP*, 37 | 36 | **PT-05** |
| CESARINO 2022 | "Bolsonarismo sem Bolsonaro? Públicos antiestruturais na nova fronteira cibernética". *Revista do IEB*, 82 | 27 | **PT-06** |
| NUNES 2024 | "A palavra e a coisa: bolsonarismo como convergência, horizonte, infraestrutura, ecologia". *Lua Nova*, 122 | 20 | **PT-06** |
| MENDONÇA E FREITAS 2022 | "Fake News e o Repertório Contemporâneo de Ação Política". *Dados*, 66(2) | 33 | **PT-06** |
| CHAGAS E CARREIRO 2022 | "Far-Right Digital Activism in Polarized Contexts". *Media and Communication*, 10(4) | 14 | **PT-06** |
| **GOHN 2019** — *entregue* | "Ciclos de protestos no Brasil: 1970-2019". *mundosplurales*, 6(1):93-119 | 27 | **PT-01 a PT-04**, e a **tarefa 10** |
| **BASTOS E RECUERO 2023** — *entregue* | "The Insurrectionist Playbook: Jair Bolsonaro and the National Congress of Brazil". *Social Media + Society*, p. 1-16 | 16 | **PT-06** e T₋₁ operacional — a mais próxima do objeto central |
| **FARIAS, CASARÕES E MAGALHÃES 2022** — *entregue* | "Radical Right Populism and the Politics of Cruelty: The Case of COVID-19 in Brazil Under President Bolsonaro". *Global Studies Quarterly*, 2:1-13 | 13 | **PT-05, PT-06** |

### Observações que a coleta produziu — e as três que a leitura já respondeu

**A obra que PT-04 citava sem ter, agora está.** O registro declarava, desde agosto, "Cesarino (2022)". Entraram **duas** Cesarino — a de 2019, sobre identidade e representação, e a de 2022, sobre públicos antiestruturais. Qual das duas o registro queria é coisa que só a leitura dirá, e o `fonte_trecho` de PT-04 continua declarando que a obra citada não foi lida.

**~~Há uma peça que cobre exatamente o arco que o projeto mais precisa.~~ CONFIRMADO PELA LEITURA.** Araujo e Sales (2022) tratam da atuação política das Forças Armadas e do fenômeno bolsonarista **entre 2013 e 2022** — a junta entre T₋₁ conjuntural e T₋₁ operacional. Lida em 04/10/2026, **tirou PT-05 de contextual** e deu página a PT-02, PT-04, PT-06 e PT-12. A previsão da coluna "serve a" dizia PT-05 e PT-12; a leitura entregou cinco registros.

**~~Há uma peça para a afirmação órfã de PT-02.~~ LIDA, E REFUTOU.** "Tolerância policial" era a única afirmação de PT-02 que nenhuma das sete peças do eixo 12 sustentava. Fernandes e Silva (2021) estudam 45 anos de policiamento a protestos no Rio Grande do Sul, e das três possibilidades que este documento previa em 04/10 pela manhã — *"pode confirmar, pode refutar, pode não falar do período"* — ocorreu a segunda: documentam *"o uso prevalente de táticas de repressão física, pouco tolerantes"* (rev. p. 492). O campo passou a dizer **seletividade**, com dois limites declarados: um estado, série até 2015. Ver documento 12, §4.2.

**~~Nada do que entrou cobre PT-08.~~ A peça chegou, e não foi lida.** Nenhuma das catorze da coleta tratava de 6 de janeiro de 2021 nos Estados Unidos. Bastos e Recuero (2023), *The Insurrectionist Playbook*, estava barrada pela SAGE e **o pesquisador a entregou no mesmo dia**. Trata do 8 de janeiro e do Congresso brasileiro, não do Capitólio — de modo que PT-08, cuja lacuna é literatura comparada sobre os Estados Unidos, **continua sem peça**, e o que ganhou peça foi o T₋₁ operacional.

**E uma observação nova, da leitura: a previsão da coluna "serve a" errou por baixo, não por cima.** As duas peças lidas ancoraram mais registros do que a coleta previa — cinco em vez de dois, e um deles mudou de classe. Isso é argumento para ler, não para confiar no mapa: o mapa foi feito de título e resumo.

---

## 3. O que não entrou — e as quatro que, barradas aqui, você entregou

Quatro peças escolhidas não chegaram **pela via automatizada**, e o pesquisador entregou as quatro no mesmo dia, depois do encaminhamento 4. Isso **confirma** o resultado que a tabela abaixo registrava e **corrige a sua formulação**.

O que a coleta mostrou: três das quatro são de editora comercial grande, e as catorze que chegaram são todas de plataformas latino-americanas ou de acesso aberto diamante. **O enunciado correto do achado é sobre o ALCANCE AUTOMATIZADO, não sobre a literatura:** *a literatura do bolsonarismo que está ao alcance de coleta automatizada neste projeto é a brasileira publicada em acesso aberto diamante.* As quatro barradas estavam ao alcance de um navegador com um ser humano atrás — e é a mesma lição que PT-04 já havia ensinado nesta mesma tarefa, em outra forma: **uma varredura prova a lacuna do que varreu.** Aqui, a lacuna era do método de coleta.

**Duas das quatro vinham mal atribuídas nesta lista, e abrir o arquivo corrigiu.** Gohn é de **2019**, não 2020 — o próprio DOI traz `.1.2019.`. E von Bülow e Abers são do fascículo de **2024**, v. 59, p. 998-1016: o slug `gov.2022.14` é o ano da publicação on-line, não o do fascículo. Farias e Casarões são **três** autores, com David Magalhães. **O ano do DOI não é o ano de publicação** — armadilha de citação que vale guardar.

| Peça | Via | O que aconteceu, e como terminou |
|:--|:--|:--|
| GOHN **2019**, "Ciclos de protestos no Brasil: 1970-2019", *mundosplurales* | FLACSO Andes (OJS) | **HTTP 403** no PDF **e na página do artigo**. Declarada diamante pelo OpenAlex; o servidor recusa requisição automatizada, com ou sem `Referer`. **ENTREGUE pelo pesquisador em 04/10/2026** |
| VON BÜLOW E ABERS **2024**, "Denialism and Populism", *Government and Opposition* | Cambridge | **HTTP 429** nas duas tentativas — limite de taxa, não recusa. **ENTREGUE em 04/10/2026**, e é a mais valiosa das quatro: sustenta que o bolsonarismo é **movimento social** e cobre março/2020 a outubro/2021, o período exato de PT-06 |
| BASTOS E RECUERO 2023, *The Insurrectionist Playbook*, *Social Media + Society* | SAGE | **HTTP 403**. Ouro no OpenAlex, barrada pela SAGE. **ENTREGUE em 04/10/2026**, e o PDF traz licença **CC BY** impressa na primeira página — isto é, a obra era livre e o **acesso** não era. É a única peça da lista que trata do 8 de janeiro e do Congresso |
| FARIAS, CASARÕES **E MAGALHÃES** 2022, "Radical Right Populism and the Politics of Cruelty", *Global Studies Quarterly* | Oxford, e repositório UNSW | **HTTP 403** na Oxford, **timeout** no repositório australiano. **ENTREGUE em 04/10/2026.** O texto usa ligadura ﬁ — buscar "defined" sem normalizar NFKC não acha, armadilha que o projeto já conhecia |

**Candidatas identificadas e não coletadas**, por serem obra longa ou por estarem fora do recorte imediato:

- **ROCHA, Camila. *'Menos Marx, mais Mises': uma gênese da nova direita brasileira (2006-2018)***. Tese, USP, 2019 (`10.11606/t.8.2019.tde-19092019-174426`, ouro). É a genealogia da nova direita, e é a obra de onde sai o artigo de 2019 já coletado.
- **SOUZA, Rafael de. *Cenários de protesto: mobilização e espacialidade no ciclo de confronto de junho de 2013***. Tese, USP, 2019 (`10.11606/t.8.2019.tde-12032019-123654`, ouro).
- **VENÂNCIO e FERREIRA 2024**, "Unraveling User Coordination on Telegram", ICWSM (`10.1609/icwsm.v18i1.31408`) — infraestrutura de coordenação, serve a PT-06.
- **MAYKA e SMITH 2021**, "The Grassroots Right in Latin America", *LAPS* (`10.1017/lap.2021.20`) — Cambridge, híbrida.
- **ESCOFFIER e PAYNE 2026**, "Mapping the Right against Rights in Latin America: A Database of Right-wing Mobilization" — é **base de dados**, não artigo, e pode ser mais útil que qualquer um dos textos acima.
- **CAMASSA 2026**, "A nova direita jurídica brasileira: um contrapúblico alinhado ao bolsonarismo", *Novos Estudos CEBRAP* — toca o arco judicial, que no codebook é PT-05A e PT-06A a PT-06C.

**Autores que o item 25 nomeava e a busca não trouxe em formato coletável:** Campos Mello, Abranches e Avritzer publicam sobre o tema **em livro**, não em artigo de acesso aberto. Continuam fora do alcance pela mesma razão que a literatura clássica brasileira da tarefa 10: **são livros, e livro não se baixa de repositório.** Se o pesquisador tiver os arquivos, entram como Alonso (2023) entrou.

---

## 4. O que a coleta não fez, e é decisão sua

1. **Leu três das dezoito, e as três por encaminhamento seu.** **Restam quinze peças, 400 páginas.** E a natureza do que falta mudou: **nenhuma das quinze bloqueia mais registro algum do codebook.** A camada conjuntural brasileira está fechada, e o único contextual que resta — PT-08 — pede literatura comparada sobre o Capitólio, que nenhuma das quinze cobre. **A leitura restante passou a servir à redação, não à codificação**, e por isso deixa de ter ordem de prioridade imposta pela cadeia causal.
2. **A coleta não mudou registro; a leitura mudou — dois registros.** **PT-05 saiu** de contextual com Araujo e Sales (2022) e **PT-06 saiu** com von Bülow e Abers (2024). Resta `Contextual` apenas **PT-08**. Os `status_verificacao` das quinze não lidas continuam dizendo que a literatura não foi lida — o que é verdade, e o que seria falso se a coleta tivesse sido confundida com leitura. **Cesarino (2022), que PT-06 citava desde agosto sem ter, está no corpus e continua não lida**, e o registro diz isso.
3. ~~**Não escolheu a ordem de leitura.**~~ **VOCÊ ESCOLHEU, em 04/10/2026**, e as duas sugestões foram as lidas, nessa ordem: Araujo e Sales (2022) e depois Fernandes e Silva (2021). A ordem importou — ver documento 12, §4.1.
4. ~~**Não retentou as quatro barradas.**~~ **DESNECESSÁRIO: você entregou as quatro.** Estão no eixo 13, coletadas e não lidas, com procedência declarada.
5. **O eixo 13 entrou em `FORA_DA_DOCUMENTAL`**, como o 05 e o 12. Corpus: **52 PDFs / 10.207 páginas**, dos quais **22 / 6.951 documentais, inalterados**. O corpus cresceu **816 páginas** hoje, em três rodadas, sem que um único documento oficial entrasse.
6. **NOVO — três das dezoito peças são de editora comercial grande**, e entraram porque você as entregou. Duas declaram licença Creative Commons na própria peça; a terceira não traz declaração visível no PDF. **Se o repositório ganhar remoto público (tarefa 15), isso precisa ser decidido antes, não depois** — é o mesmo ponto que `ALONSO 2023` abriu no eixo 12.
7. **Gohn (2019) pode servir à tarefa 10, e não só à 25.** É levantamento de cinco décadas de estudos brasileiros de protesto, com o quinto ciclo definido como "pós junho de 2013". É a única peça do corpus que faz o **balanço da própria literatura brasileira** — exatamente a lacuna que a tarefa 10 registra como "as sínteses têm zero referências sobre o Brasil". Se ela conta como fechamento parcial da 10, é decisão sua.
8. **NOVO — duas plataformas continuam nomeadas no codebook sem verificação.** O `mecanismo_causal` de PT-06 nomeia Telegram e WhatsApp. Von Bülow e Abers as nomeiam também, mas **por citação de segunda mão** — as 802 mensagens de WhatsApp são de Soares et al. (2021) e as 867 de Telegram são de Nascimento et al. (2020), nenhum dos dois no corpus. A regra deste projeto proíbe lastrear cifra conferida apenas contra outra citação dela, e por isso as duas estão **declaradas como não verificadas** no status do registro. **Se quiser âncora de primeira mão para as plataformas, as peças a ler são Chagas e Carreiro (2022) e Mendonça e Freitas (2022)**, já no corpus. Caso contrário, a saída honesta é tirar as duas do campo.
