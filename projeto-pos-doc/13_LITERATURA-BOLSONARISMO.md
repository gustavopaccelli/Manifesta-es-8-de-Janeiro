# A literatura do bolsonarismo como fenômeno de mobilização — coleta da tarefa 25

**04/10/2026.** A tarefa 25 nasceu de madrugada, na primeira rodada da tarefa 14, com a seguinte formulação: *"a literatura do bolsonarismo (2018-2022) — Cesarino, Campos Mello, Abranches, Avritzer. É o que falta para PT-04, PT-05 e PT-06 saírem de contextuais, e não está em nenhuma das duas coleções já varridas."*

O pesquisador especificou o recorte: **o bolsonarismo enquanto fenômeno de mobilização social e política**, com foco nas dinâmicas de mobilização, manifestação e protesto, e em particular nas **formas de repertório específicas do campo das direitas**. Este documento registra a coleta feita sob esse recorte.

> **A DECLARAÇÃO QUE VEM PRIMEIRO, E VALE PARA TODO O DOCUMENTO: nenhuma das catorze peças coletadas foi lida, e nenhuma ancora registro algum do codebook.** Elas estão em `Fontes/13_Bolsonarismo-mobilizacao/` como **fila de leitura**, com proveniência declarada em `PROCEDENCIA` — que é o que `verificar_integridade.py` exige de todo arquivo que não ancora registro. Um arquivo dentro de `Fontes/` parece lastro, e estes catorze não são: quem for ancorar registro em qualquer um deles precisa abrir, ler e pôr página, como se fez com as sete peças do eixo 12.

---

## 1. Como se buscou

**OpenAlex**, por consulta programática em `scripts`-de-rodada (`oa_busca.py`, mantido no diretório de trabalho da sessão). A escolha repete a de 29/09: **o OpenAlex responde sem identificação**, e nenhuma consulta deste projeto carrega o e-mail do pesquisador.

Dezessete consultas, em português e em inglês, recortadas em 2016-2026, cruzando quatro eixos: *bolsonarismo*, *extrema-direita / campo das direitas*, *mobilização / protesto / manifestação* e *repertório de ação coletiva*. Mais nove consultas por autor, com os nomes que a literatura brasileira já consagrou no tema — Cesarino, Messenberg, Camila Rocha, Esther Solano, Pinheiro-Machado, Tatagiba.

**345 obras distintas** na união das duas rodadas de busca — 151 na primeira, 214 na segunda, com **apenas 20 em comum**, o que diz que as duas estratégias de consulta varriam regiões diferentes da literatura e que nenhuma delas sozinha bastaria. A triagem dos títulos foi feita a olho, e dela saíram dezoito peças escolhidas por aderência direta ao recorte do pesquisador. **Catorze chegaram.**

> *A primeira versão deste parágrafo dizia "365 obras distintas", que é a soma de 151 e 214 — e as duas listas se sobrepõem em 20. A união é 345. A soma de duas buscas não é a união delas, e somar sem conferir a interseção é a forma aritmética do defeito que este projeto persegue desde agosto: o número certo medindo a coisa errada.*

**Cada peça foi conferida nos dois eixos da regra de 29/09** — *existir não é estar bem atribuído*. O DOI resolve **e** o título que a fonte devolve casa com o título esperado. Divergências de título: **zero em catorze**. E cada arquivo baixado foi conferido byte a byte: começa com `%PDF`, abre no PyPDF2, e a primeira página devolve texto. **Nenhuma peça do eixo 13 tem o problema do eixo 12** — todas têm camada de texto legível.

Uma peça precisou ser descartada depois de baixada: a tentativa na Cambridge devolveu **HTTP 429** com uma página de erro de 1,3 KB, que o `curl` gravou com extensão `.pdf`. Um HTML de erro guardado como PDF é exatamente o tipo de defeito silencioso que este projeto caça — foi apagado, e a peça está na lista de pendentes abaixo.

---

## 2. O que entrou — catorze peças, 378 páginas

A coluna **serve a** diz qual registro a peça tem condições de ancorar **depois de lida**. É mapa de leitura, não âncora.

| Peça | Referência | p. | Serve a |
|:--|:--|--:|:--|
| MESSENBERG 2017 | "A direita que saiu do armário: a cosmovisão dos formadores de opinião dos manifestantes de direita". *Sociedade e Estado*, 32(3) | 27 | **PT-02** |
| ROCHA 2019 | "'Imposto é Roubo!' A Formação de um Contrapúblico Ultraliberal e os Protestos Pró-Impeachment de Dilma Rousseff". *Dados*, 62(3) | 42 | **PT-02, PT-03** |
| TATAGIBA 2018 | "Entre as ruas e as instituições: os protestos e o impeachment de Dilma Rousseff". *Lusotopie*, 17(1):112-135 | 20 | **PT-02, PT-03** |
| FERNANDES E SILVA 2021 | "Dinâmicas do controle à ação coletiva: o policiamento a protestos no Rio Grande do Sul". *Mediações*, 26(3) | 17 | **PT-02** |
| SANTOS E TANSCHEIT 2019 | "Quando velhos atores saem de cena: a ascensão da nova direita política no Brasil". *Colombia Internacional*, 99 | 37 | **PT-04** |
| CESARINO 2019 | "Identidade e representação no bolsonarismo". *Revista de Antropologia*, 62(3) | 28 | **PT-04** |
| KAYSEL E BIANCHI 2025 | "Bolsonarismo como coalizão discursiva de extrema-direita". *Caderno CRH*, 38 | 14 | **PT-04** |
| CARVALHO E TATAGIBA 2025 | "Quando o conflito eleitoral extravasa para as ruas: protestos e eleições presidenciais no Brasil". *Lua Nova*, 124 | 46 | **PT-04**, T₋₁ operacional |
| ARAUJO E SALES 2022 | "Atuação política das Forças Armadas e o fenômeno bolsonarista no Brasil (2013-2022)". *Cadernos do Tempo Presente*, 13(1) | 17 | **PT-05, PT-12** |
| MENDONÇA E DOMINGUES 2021 | "Protestos contemporâneos e a crise da democracia". *RBCP*, 37 | 36 | **PT-05** |
| CESARINO 2022 | "Bolsonarismo sem Bolsonaro? Públicos antiestruturais na nova fronteira cibernética". *Revista do IEB*, 82 | 27 | **PT-06** |
| NUNES 2024 | "A palavra e a coisa: bolsonarismo como convergência, horizonte, infraestrutura, ecologia". *Lua Nova*, 122 | 20 | **PT-06** |
| MENDONÇA E FREITAS 2022 | "Fake News e o Repertório Contemporâneo de Ação Política". *Dados*, 66(2) | 33 | **PT-06** |
| CHAGAS E CARREIRO 2022 | "Far-Right Digital Activism in Polarized Contexts". *Media and Communication*, 10(4) | 14 | **PT-06** |

### Quatro observações que a coleta produziu, e que valem antes da leitura

**A obra que PT-04 citava sem ter, agora está.** O registro declarava, desde agosto, "Cesarino (2022)". Entraram **duas** Cesarino — a de 2019, sobre identidade e representação, e a de 2022, sobre públicos antiestruturais. Qual das duas o registro queria é coisa que só a leitura dirá, e o `fonte_trecho` de PT-04 continua declarando que a obra citada não foi lida.

**Há uma peça que cobre exactamente o arco que o projeto mais precisa.** Araujo e Sales (2022) tratam da atuação política das Forças Armadas e do fenômeno bolsonarista **entre 2013 e 2022** — isto é, a junta entre T₋₁ conjuntural e T₋₁ operacional, que é a lacuna que a primeira rodada da tarefa 14 chamou de "a mais cara".

**Há uma peça para a afirmação órfã de PT-02.** "Tolerância policial" é a única afirmação de PT-02 que nenhuma das sete peças do eixo 12 sustenta. Fernandes e Silva (2021) estudam o policiamento a protestos no Rio Grande do Sul — é a literatura mais próxima que a busca achou. Pode confirmar, pode refutar, pode não falar do período: **nada disso se sabe antes de ler.**

**Nada do que entrou cobre PT-08.** Nenhuma das catorze trata de 6 de janeiro de 2021 nos Estados Unidos. A peça que o faria — Bastos e Recuero (2023), *The Insurrectionist Playbook* — está na lista de pendentes, barrada pela SAGE.

---

## 3. O que não entrou, e por quê

Quatro peças escolhidas não chegaram. **Três das quatro são de editora comercial grande, e as catorze que chegaram são todas de plataformas latino-americanas ou de acesso aberto diamante.** Isso não é coincidência e já é um resultado: *a literatura do bolsonarismo que está efetivamente ao alcance deste projeto é a brasileira publicada em acesso aberto diamante.*

| Peça | Via | O que aconteceu |
|:--|:--|:--|
| GOHN 2020, "Ciclos de protestos no Brasil: 1970-2019", *Mundos Plurales* | FLACSO Andes (OJS) | **HTTP 403** no PDF **e na página do artigo**. Declarada diamante pelo OpenAlex; o servidor recusa requisição automatizada, com ou sem `Referer` |
| VON BÜLOW E ABERS 2022, "Denialism and Populism", *Government and Opposition* | Cambridge | **HTTP 429** nas duas tentativas. A memória do projeto registra que a Cambridge passa — e passou em 29/09. Hoje limitou. **É a mais promissora de retentar** |
| BASTOS E RECUERO 2023, *The Insurrectionist Playbook*, *Social Media + Society* | SAGE | **HTTP 403**. Ouro no OpenAlex, barrada pela SAGE — exatamente o que a memória do projeto já registrava sobre a SAGE. É a única peça da lista que trata do 8 de janeiro e do Congresso |
| FARIAS E CASARÕES 2022, "Radical Right Populism and the Politics of Cruelty", *Global Studies Quarterly* | Oxford, e repositório UNSW | **HTTP 403** na Oxford, **timeout** no repositório australiano. Também consistente com a memória: a Oxford barra |

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

1. **Não leu nada.** O próximo passo da tarefa 25 é leitura, e leitura com página — o padrão que o eixo 12 estabeleceu hoje. Catorze peças, 378 páginas.
2. **Não mudou nenhum registro.** PT-05, PT-06 e PT-08 continuam `Contextual`, e seus `status_verificacao` continuam dizendo que a literatura não foi lida — o que é verdade, e o que seria falso se a coleta tivesse sido confundida com leitura.
3. **Não escolheu a ordem de leitura.** A coluna "serve a" propõe um mapa; qual registro atacar primeiro é juízo. A sugestão, se vale: **Araujo e Sales (2022)**, por cobrir 2013-2022 e tocar a junta da cadeia; e **Fernandes e Silva (2021)**, por ser a única candidata à afirmação órfã de PT-02.
4. **Não retentou as quatro barradas.** A de Cambridge é a mais promissora — foi 429, não 403.
5. **O eixo 13 entrou em `FORA_DA_DOCUMENTAL`**, como o 05 e o 12. Corpus: **48 PDFs / 10.132 páginas**, dos quais **22 / 6.951 documentais, inalterados**. O corpus cresceu 741 páginas hoje sem que um único documento oficial entrasse.
