# Fontes — corpus documental do projeto

Pasta criada em **12/08/2026**. Reúne as fontes primárias e a bibliografia teórica do projeto sobre as mobilizações de 8 de janeiro de 2023. Os produtos da análise (relatório, CSV, JSON, figuras) permanecem na raiz do projeto — aqui ficam apenas os **insumos**.

## Organização

```
Fontes/
├── 01_Arco-judicial_2017-2021/      T−1 conjuntural — Lava Jato, prisão e elegibilidade
├── 02_T-1_Articulacao/              articulação logística (30/10/2022 – 08/01/2023)
├── 03_T0_8-de-janeiro/              o evento
├── 04_T+1_Resposta-institucional/   resposta institucional (2023–2026)
├── 05_Bibliografia-teorica/         método e referencial teórico
├── 06_Lava-Jato-judicializacao-lawfare/   eixo bibliográfico aberto pelo arco judicial
└── 07_NetLab-UFRJ/                  relatórios de laboratórios sobre redes digitais
```

---

## Acervo obtido — 19 PDFs (6.835 páginas), 1 acórdão em HTML, 5 sínteses e artefatos textuais

*Atualizado em 16/08/2026.* Camada de texto conferida com **PyPDF2**, amostrando cinco pontos ao longo de cada documento — nunca só a página 1, que costuma ser capa sem texto e produz falso alarme de "precisa de OCR". Duas peças **não têm** camada de texto e estão declaradas: o folder da campanha e o relatório do Manchetômetro (parcial).

> **Nunca use `pdfinfo` para contar páginas destes PDFs**: ele subcontou grosseiramente (84 para um arquivo de 464). Use PyPDF2, como fazem todos os scripts do projeto.

### 01 — Arco judicial (2017–2021) · registros PT-03A a PT-06C

| Arquivo | Pág. | Registro | Origem |
|:--|--:|:--|:--|
| `TRF4_Revista-97_Acordao-ACr-5046512-94_2018-01-24.pdf` | 657 | PT-03B | Revista do TRF-4 nº 97 (30/08/2018) — traz o **inteiro teor da ementa, do relatório e dos votos** da Apelação Criminal 5046512-94.2016.4.04.7000 |
| `STF_HC-152752_Acordao_2018-04-04.pdf` | 464 | PT-03C | Acórdão que denegou o HC por 6×5 e viabilizou a execução provisória |
| `STF_ADC-43-44-54_Acordao_2019-11-07.pdf` | 489 | PT-05A | Julgamento conjunto; constitucionalidade do art. 283 do CPP |
| `STF_HC-164493_Acordao_Suspeicao-Moro_2021-03-23.pdf` | 441 | PT-06B | 2ª Turma reconhece a suspeição do ex-juiz Sergio Moro |
| `STF_HC-193726-AgR_Acordao_2021-04-15.pdf` | 264 | PT-06C | Plenário confirma a anulação por incompetência (8×3) — **elegibilidade restaurada** |
| `STF_HC-193726-AgR-segundo_Acordao_2021-06-23.pdf` | 182 | PT-06B | Plenário mantém o entendimento (7×4) |
| `STF_ADC-43-MC_Acordao_2016-10-05.pdf` | 250 | PT-02A | Medida cautelar de 2016 — precedente da execução provisória |
| `TSE_RCand-0600903-50_Acordao_2018-09-01.html` | — | **PT-03E** | **Acórdão do TSE** que indeferiu o registro de candidatura de Lula, rel. min. Barroso, 1º/09/2018. Obtido em **16/08/2026 SEM captcha**, pelo endpoint de documento da Consulta Unificada PJe (`consultaunificadapje.tse.jus.br`). ⚠️ **Servido em HTML, não em PDF** — o parâmetro `extensaoArquivo` só muda o Content-Type. Citar por estrutura interna (item da ementa, dispositivo), não por página |

### 03 — T0, o evento

| Arquivo | Pág. | Registro | Origem |
|:--|--:|:--|:--|
| *(o livro do STF migrou para `10_Democracia-Inabalada/`)* | — | PT-38 | Havia duas cópias byte-idênticas no corpus. Consolidadas em 16/08/2026: mantida a do eixo 10, removida esta (backup em `.backup_pre_lula/`) |

### 04 — T+1, resposta institucional

| Arquivo | Pág. | Registro | Origem |
|:--|--:|:--|:--|
| `CPMI-8-de-Janeiro_Relatorio-Final_2023-10-17.pdf` | 1.333 | PT-55 e cronologia de T0 | **Relatório Final da CPMI.** Espinha dorsal da reconstrução de $T_0$. **49 registros do codebook já foram recodificados sobre ela, com página** |
| `STF_AP-2668_Acordao_Condenacao_2025-09-11.pdf` | 1.991 | PT-56, PT-57 | **Acórdão da condenação do núcleo crucial.** Inteiro teor completo, com todos os votos |
| `STF_AP-2668-QO_Acordao_2025-05-14.pdf` | 50 | PT-56 | Questão de ordem preliminar |

### 02 e 03 — obtidos na segunda rodada de coleta

| Arquivo | Pág. | Registros | Procedência |
|:--|--:|:--|:--|
| `02_T-1_Articulacao/PGR_Denuncia_PET-12100_Nucleo-1_2025-02-18.pdf` | 272 | PT-06A, PT-07, PT-13 | **Denúncia da PGR contra o Núcleo 1**, assinada digitalmente pelo procurador-geral Paulo Gustavo Gonet Branco em 18/02/2025, com chave de validação verificável em `transparencia.mpf.mp.br/validacaodocumento`. Hospedada pela Agência Brasil (EBC) |
| `03_T0_8-de-janeiro/GDF-SSP_Relatorio-Interventor-Federal_Cappelli_2023-01-27.pdf` | 62 | PT-18, PT-20B, PT-27, PT-52 | **Relatório do Interventor Federal**, GDF/SSP, Gabinete do Interventor, elaborado por Ricardo Cappelli sob o Decreto nº 11.377/2023. Obtido em espelho jornalístico (Poder360) — o documento traz cabeçalho e identificação oficiais, mas **não foi localizado em domínio oficial**. **Integridade conferida em 16/08/2026** contra o espelho público `https://static.poder360.com.br/2023/01/1-RELATORIO-FINAL.pdf`: byte-idêntico, SHA-1 `78adf23746d11ee1…`, 7.074.810 bytes. A ausência de domínio oficial permanece e deve constar da nota de fontes do artigo; o que se ganhou é conferência repetível por terceiros |

Estrutura do relatório Cappelli: 1. Introdução (p. 2) · 2. Contexto situacional (p. 2) · 3. Sistema de segurança do DF (p. 3) · 4. Eventos relevantes (p. 17) · 5. Atos de vandalismo (p. 37) · **6. Conclusões (p. 53-60)** · Anexos (p. 61). As conclusões A a H são a parte mais citável.

**A sentença de 1ª instância de Moro deixou de ser pendência crítica.** Seu dispositivo está **transcrito no acórdão do TRF-4** (Revista nº 97, p. 395 do PDF), incluindo a fixação da pena e do regime. O inteiro teor segue não obtido, mas a parte operativa e a fundamentação essencial estão reproduzidas na peça recursal, o que basta para citação.


### 06 — Eixo bibliográfico: Lava Jato, judicialização e lawfare

**20 referências**, 18 com DOI confirmado no CrossRef, em `bibliografia_eixo_lava-jato.csv` e `bibliografia_comentada.md`. Supre a lacuna aberta quando o arco judicial entrou no process tracing. **Leia o `LEIA-ME.md` da pasta** — a literatura revisada por pares posterior a 2019 é majoritariamente crítica à operação, e o LEIA-ME explica como tratar esse desequilíbrio sem simular simetria inexistente.

### 07 — Relatórios de laboratórios sobre redes digitais

`NetLab-UFRJ_Anuncios-golpistas-Meta-Ads_2023-02-07.md` (transcrição de publicação web: 185 anúncios golpistas na biblioteca do Meta Ads) e `Doxa-IESP-UERJ_Manchetometro_Atos-golpistas-8-jan_2023-03.pdf` (16 p., **ancora PT-50A** desde 16/08/2026). **São dois laboratórios distintos** — o LEIA-ME da pasta explica por que ambos estão ali e como não confundi-los. Nenhum é revisado por pares; o do Manchetômetro usou o CrowdTangle, descontinuado pela Meta em 14/08/2024, o que torna a coleta não reproduzível.

### 10 — Democracia Inabalada

Pasta criada em 16/08/2026. **Leia o `LEIA-ME.md` dela** — ele desfaz uma confusão que custou dias ao projeto: *"Democracia Inabalada"* nomeia **duas peças distintas**, o livro fotográfico de ago/2023 e o **balanço estatístico do Gabinete do Min. Alexandre de Moraes de 29/04/2026**.

| Arquivo | Pág. | Registro | Observação |
|:--|--:|:--|:--|
| `STF_Gabinete-Moraes_Balanco-8-de-Janeiro_2026-04-29.pdf` | 15 | **PT-53, PT-61** | **Fonte primária.** Bucket oficial do STF (S3). 1.402 réus responsabilizados, 190 presos. Peça gráfica: dois gráficos vetoriais não extraem valores |
| `STF_Democracia-Inabalada_Ebook_28x28cm.pdf` | 210 | **PT-38** | Livro oficial do STF (ago/2023, ISBN 978-85-54223-50-2). **Cópia canônica** desde a consolidação de 16/08/2026 |
| `STF_Democracia-Inabalada_Folder.pdf` | 6 | — | Peça de divulgação, **sem camada de texto**. Lida por extração de imagem |

Mais `PAGINA-CAMPANHA-catalogacao.md` e `DOCUMENTARIO-catalogacao.md` — catalogação da campanha como objeto de enquadramento.

### 08 — Imprensa: cobertura e enquadramento

Eixo aberto em 16/08/2026. **Leia o `LEIA-ME.md` da pasta** — ele fixa a distinção que organiza o tratamento de material jornalístico no projeto: matéria arquivada que ancora registro é *fonte de dado* e vai para `09_Arquivamento-web/`; literatura sobre como a imprensa enquadrou o evento é *objeto de análise* e fica na 08.

`SciELO-Preprints_Drummond-Manginelli_Editoriais-8-jan_2023-10-09.pdf` (24 p., CC-BY 4.0, DOI 10.1590/SciELOPreprints.7040, SHA-1 `f983f619…`) — análise temática e de enquadramento de 105 editoriais de Folha, O Globo e Estadão entre 1 e 18/01/2023. ⚠️ **Preprint, não revisado por pares**, e **não traz números de manifestantes** (conferido).

### 05 — Bibliografia teórica

**O cânone de mecanismos, acrescentado à mão em 29/09/2026.** A triagem dos DOIs das sínteses (item 23 da agenda) mostrou que as obras de que o codebook toma o vocabulário — certificação, difusão, apropriação de repertório, limiar — **não estavam no corpus**, e nenhuma lista de DOIs gerada as traria. Entraram pelo pesquisador, e os dados abaixo foram lidos das próprias folhas de rosto:

| Arquivo | Referência | Observação |
|:--|:--|:--|
| `McADAM-TARROW-TILLY_Dynamics-of-Contention_Cambridge-2001.pdf` (411 p.) | McADAM, D.; TARROW, S.; TILLY, C. **Dynamics of Contention**. Cambridge: Cambridge University Press, 2001. ISBN 0-521-80588-0 (cart.), 0-521-01187-6 (brochura), 0-511-02877-6 (eBook). Série *Cambridge Studies in Contentious Politics*. DOI `10.1017/CBO9780511805431` | Com camada de texto. PDF de 2004, distribuído pela Cambridge |
| `TARROW_O-poder-em-movimento_Vozes-2009.pdf` (162 p.) | TARROW, S. **O poder em movimento: movimentos sociais e confronto político**. Trad. Ana Maria Sallum. Petrópolis: Vozes, 2009. Coleção Sociologia. ISBN 978-85-326-3828-1. Original: *Power in movement* | **Sem camada de texto** e em **duas páginas do livro por folha** — 162 folhas para ~324 páginas. `conferir_paginas.py` não o lê; a conferência foi por renderização. A folha de rosto **não declara a edição inglesa**; o sumário, em três partes e onze capítulos, corresponde à 2ª (1998), `10.1017/CBO9780511813245` |

Nenhum dos dois **ancora registro algum** do codebook, e nem deve: são o referencial, não a evidência. Os capítulos 5 e 8 do Tarrow — *Oportunidades e restrições políticas* e *Estruturas de mobilização e confronto político* — são os dois conceitos que dão nome à tese de doutorado do pesquisador, no eixo 11.

**A enciclopédia, acrescentada pelo pesquisador em 30/09/2026.** `SNOW-DELLA-PORTA-KLANDERMANS-McADAM_Wiley-Blackwell-Encyclopedia-of-Social-and-Political-Movements_2013.pdf` (1.638 p., com camada de texto) — SNOW, D. A.; DELLA PORTA, D.; KLANDERMANS, B.; McADAM, D. (Orgs.). **The Wiley-Blackwell Encyclopedia of Social and Political Movements**. Oxford: Blackwell, 2013.

**É a obra-contêiner de boa parte dos 411 DOIs das sínteses**: traz **434 verbetes com DOI próprio impresso no rodapé**, e por isso resolve de uma vez o problema de acesso que travava a leitura na fonte da camada A — sete verbetes pertinentes deixam de depender de assinatura de editor. Lidos integralmente em 30/09: *Mechanisms* (Tarrow), *Protest cycles and waves* (della Porta), *Resource mobilization theory* (Edwards & Gillham) e *Critical mass theory* (Oliver); ver [`projeto-pos-doc/09_CONCEITO-MECANISMO.md`](../projeto-pos-doc/09_CONCEITO-MECANISMO.md).

> ⚠️ **O DOI impresso no rodapé não existe.** A enciclopédia imprime `10.1002/9781405198431.wbespmNNN`, prefixo do ISBN impresso, e os quatro testados retornam **404 no CrossRef**. O registrado é o do ISBN eletrônico, `10.1002/9780470674871.wbespmNNN` — que é o que as sínteses declaram. **Primeira vez em que a fonte impressa erra o identificador e a síntese automatizada acerta.** Não copie do rodapé.

Também no eixo: `Livro_Process tracing.pdf` (104 p.) — **CUNHA, Eleonora Schettini Martins; ARAÚJO, Carmem E. Leitão. *Process tracing nas Ciências Sociais: fundamentos e aplicabilidade*. Brasília: Enap, 2018. 103 p. ISBN 978-85-256-0090-5.** É a referência metodológica em português, e traz o esquema `X [A → B → C] → Y` e a definição de condição necessária que PT-28 usa · `process-tracing-research-designs-a-practical-guide.pdf` (5 p.) — **RICKS, J. I.; LIU, A. H. Process-tracing research designs: a practical guide. *PS: Political Science & Politics*, out. 2018, p. 842 ss. DOI `10.1017/S1049096518000975`**, seção *The Teacher*, a mesma de Collier (2011) · `LEIA-ME_status_downloads.md` (status do levantamento bibliográfico)

**Sete sínteses de literatura** (`*_LeapSpace.docx`), cobrindo os conceitos do referencial teórico — ~31,6 mil palavras e **411 DOIs distintos em 444 menções**. Cinco entraram em 13/08/2026; **duas foram acrescentadas em 01/09/2026** (assinaladas com ✚), na mesma data em que as cinco anteriores foram substituídas por reemissões:

| Arquivo | DOIs | Cobre |
|:--|--:|:--|
| `Process_tracing_LeapSpace.docx` | 77 | método, padrões evidenciais, reconstrução de mecanismos |
| `Causal_mechanisms_in_social_science_LeapSpace.docx` | 90 | mecanismo vs. variável; explicação mecanística em sociologia histórica |
| `Political_Process_by_Charles_Tilly_LeapSpace.docx` | 82 | repertórios, formação do Estado, democratização |
| `Mobilization_structures_LeapSpace.docx` | 76 | recrutamento, liderança, participação |
| ✚ `Political_and_discursive_opportunities_LeapSpace.docx` | 46 | oportunidades políticas e discursivas; estrutura de oportunidade de mediação |
| ✚ `Framing_process_and_alignment_LeapSpace.docx` | 44 | enquadramento, alinhamento de quadros, quadros-mestres, narrativa |
| `Protest_cycle_LeapSpace.docx` | 24 | início e agrupamento de ciclos; limiares de mobilização |

**Esta tabela não é digitada.** Ela é impressa por `../scripts/verificar_dois_sinteses.py` a cada execução, com menções e DOIs distintos por arquivo, e foi conferida contra a saída dele em 29/09/2026. O critério de contagem está no cabeçalho do script.

> **Sobre a substituição de 01/09/2026.** As cinco reemissões são **substantivamente idênticas** às versões de 13/08: a comparação do texto extraído acusou diferença de uma única linha — o carimbo de geração, que passou de `Generated by LeapSpace` para `Generated by LeapSpace, Fri Aug 14 2026`. Em `Protest_cycle` nem isso mudou (só `docProps/core.xml`). A troca foi feita para fixar a data de geração no próprio documento; **nada do conteúdo, das contagens ou dos DOIs foi alterado por ela**. A contagem de DOIs de `Causal_mechanisms` passou de 90 para 89 por recontagem no arquivo, não por mudança de conteúdo — **e essa recontagem estava errada: voltou a 90 em 29/09/2026, com critério declarado e gerado por script.** Ver o último achado da segunda leva, abaixo.

⚠️ **Não são fonte citável.** São sínteses geradas por sistema automatizado (LeapSpace), sem revisão por pares e sem autoria identificável. Servem como **mapa de leitura** e como lista de DOIs para busca — a citação vai sempre para o trabalho original, lido na fonte. Os DOIs precisam de verificação no CrossRef antes de qualquer incorporação: o levantamento original deste projeto já trouxe um DOI fabricado, corrigido em `../docs/LEIA-ME_metodologia_verificacao.md`. Encaminhamento detalhado no item 11.3 de `../docs/PENDENCIAS-ANALITICAS.md`.

**Primeira leva de verificação executada em 01/09/2026 — 10 itens, dos quais 4 divergentes.** A suspeita registrada acima confirmou-se: as listas de referências destas sínteses contêm erros de metadados demonstráveis. Achados que valem para todo o acervo:

- `10.3998/mpub.2556282`, atribuído a "Beach & Pedersen (2019)", é a **1ª edição, de 2013**. O DOI da 2ª edição, já usado no projeto, é `10.3998/mpub.10072208`.
- `10.1007/9781139858472`, atribuído a Bennett & Checkel, **não existe** (HTTP 404). O correto é `10.1017/CBO9781139858472` — o prefixo 10.1007 é da Springer, não da Cambridge. E os dois são **organizadores**, não autores.
- Escribà-Folch (2008), em *Dados*, é indexado pelo título em inglês, mas **o artigo foi publicado em português**: "Participação arriscada: manifestações e tumultos em regimes ditatoriais".
- McCammon (2013), "Discursive Opportunity Structure", tem **duas versões com DOIs distintos**: a de 2013 e a `.pub2`, de 27/09/2022.
- Há ainda ruído grosseiro nas listas: um item datado de **2099**; um registro reduzido a link do Scopus sem citação; itens de migração, clima de negócios e deslizamentos de terra sem relação com o tema; entradas duplicadas; e ao menos uma **colisão de homônimos** (Beach, D., de *The Lancet Global Health*, que não é Derek Beach).

**Segunda leva de verificação, em 29/09/2026 — os 411 DOIs de uma vez, por `../scripts/verificar_dois_sinteses.py`.** Consulta o CrossRef e, em 404, a DataCite. **408 existem; 3 não.** Os três já têm DOI correto identificado e confirmado:

| Declarado na síntese | Correto |
|:--|:--|
| `10.1007/9781139858472` (Bennett & Checkel) | `10.1017/CBO9781139858472` — **já corrigido na primeira leva** |
| `10.4324/9780203856949-48` (O'Halloran) | `10.4324/9780203856949-40` |
| `10.4324/9781315731377-34` (Chenoweth) | `10.4324/9781315731377-28` |

- **Quatro DOIs só existem na DataCite**, não no CrossRef — dois da *Partecipazione e Conflitto* e dois da *European Papers*. Verificar numa agência só os condenaria como inexistentes.
- **Um quinto modo de falha, e é o mais perigoso: DOIs de vizinhos trocados.** Em `Framing_process_and_alignment`, o `-40` atribuído a Vaughan é o capítulo de O'Halloran, e o de Vaughan é o `-34`. **O `-40` resolve e passaria por verificado.** Só comparar o título registrado com o título declarado revela — das 444 menções, 435 casam, 8 divergem por título traduzido e 1 é este par.
- **Sufixo de capítulo inexistente não significa capítulo não depositado.** Os dois casos da Routledge só apareceram por busca bibliográfica pelo título; testar o DOI do livro, que responde, induz à conclusão errada.
- **Divergência de contagem resolvida em 29/09/2026: são 90 em `Causal_mechanisms`, e 411 no total.** Este inventário trazia 89 e 410, de uma recontagem à mão de 01/09 cuja regra não ficou registrada — e o git começa em 20/09, depois dela, então o histórico não a recupera. **Nenhum critério a reproduz:** o arquivo tem **91 menções e 90 DOIs distintos** (duas entradas, de capítulos diferentes, recebem o mesmo DOI de livro — `10.4324/9781315100371`); seriam **88** colapsando as duas versões `.pub2` com as suas v1, e **95** se a conta fosse de entradas da lista, quatro das quais não têm DOI. **Critério adotado:** DOI distinto é a cadeia normalizada — minúscula, pontuação final removida — achada em `word/document.xml`. Repetição de DOI dentro do mesmo arquivo não é anomalia deste: ocorre em cinco das sete sínteses.

Ficha completa da verificação em `../../projeto-pos-doc/08_BIBLIOGRAFIA-METODOLOGICA.md`. **A regra do projeto permanece: nenhum item destas sínteses entra em texto sem conferência item a item na fonte.**

### 11 — Tese de doutorado do pesquisador

*Eixo aberto em 19/08/2026.*

| Arquivo | Registro | Origem |
|:--|:--|:--|
| `PACCELLI_Tese-doutorado_UFJF_2024.docx` | — (não ancora registro) | PACCELLI, Gustavo. **"Estruturas de mobilização e Oportunidades Políticas: análise dos ciclos de protestos no Brasil contemporâneo"**. Tese de doutorado, Programa de Pós-Graduação em Ciências Sociais, Universidade Federal de Juiz de Fora, 2024. Orientação: Christiane Jalles de Paula. ~70 mil palavras, **302 referências** |

**Por que entra no corpus.** É o **antecedente teórico** de que este projeto parte. A tese analisa três ciclos de protesto no Brasil — Fora Collor (1992), junho de 2013 e as manifestações de 2015 — pela interação entre **estruturas de mobilização** e **oportunidades políticas e discursivas**, e sua última seção substantiva ("Dos coletivos progressistas aos movimentos de direita") encerra exatamente onde o 8 de Janeiro começa. O par analítico que organiza este projeto vem dela, e não é importado de fora: a tese já mobiliza **Koopmans & Olzak (2004)** e **Giugni, Koopmans, Passy & Statham (2005)** sobre oportunidades discursivas e violência de extrema-direita — o instrumento teórico para explicar a virada violenta já estava construído.

**O que ela não é.** Não é fonte de evento e **não ancora registro nenhum do codebook**. Declarada em `PROCEDENCIA` (`scripts/gerar_codebook.py`) com o tipo `bibliografia`, pela mesma razão das sínteses do eixo 05: é insumo de leitura e referencial, não evidência empírica sobre o 8 de janeiro. Formato `.docx`, sem paginação estável — citar por seção, não por página.

### 12 — Literatura da camada $T_{-1}$ conjuntural

*Eixo aberto em 04/10/2026, pela tarefa 14, em duas rodadas no mesmo dia.* **Sete peças** — seis artigos revisados por pares e um livro acadêmico. Até aqui, quem ancorava registro era documento oficial, e a teoria do eixo 05 não ancorava nada; **este é o primeiro eixo de literatura secundária que ancora registro**, e é por isso que ele ficou **fora da contagem documental** em `verificar_integridade.py`: a cifra de "documentos oficiais" não pode crescer porque entrou artigo de revista. O eixo tem **483 páginas** e levou o corpus de 31 para 34 PDFs e de 9.391 para 9.754 páginas, **sem mexer na documental** (22 PDFs / 6.951 p.).

| Arquivo | Registros | Referência | Páginas |
|:--|:--|:--|:--|
| `TATAGIBA_Ciclos-de-protestos-e-democracia_Politica-e-Sociedade-28_2014.pdf` | PT-01 | TATAGIBA, L. "1984, 1992 e 2013. Sobre ciclos de protestos e democracia no Brasil". *Política & Sociedade*, 13(28):35-62, 2014. DOI 10.5007/2175-7984.2014v13n28p35 | 28 |
| `TATAGIBA-GALVAO_Protestos-no-Brasil-em-tempos-de-crise_Opiniao-Publica-25-1_2019.pdf` | PT-01, PT-02, PT-03 | TATAGIBA, L.; GALVÃO, A. "Os protestos no Brasil em tempos de crise (2011-2016)". *Opinião Pública*, 25(1):63-96, 2019. DOI 10.1590/1807-0191201925163 | 34 |
| `PINTO_Trajetoria-discursiva-das-manifestacoes-de-rua_Lua-Nova-100_2017.pdf` | PT-01, PT-02 | PINTO, C. R. J. "A trajetória discursiva das manifestações de rua no Brasil (2013-2015)". *Lua Nova*, 100:119-153, 2017. DOI 10.1590/0102-119153/100 | 37 |
| `ALONSO_Repertorio-segundo-Charles-Tilly_Sociologia-e-Antropologia-2-3_2012.pdf` | PT-02 | ALONSO, A. "Repertório, segundo Charles Tilly: história de um conceito". *Sociologia & Antropologia*, 2(3):21-41, 2012 | 21 |
| `KUNRATH-SILVA_Apropriacao-conservadora-do-ciclo-de-protestos_Lusotopie-17-1_2018.pdf` | PT-01, PT-02 | SILVA, M. K. "A apropriação conservadora do ciclo de protestos de 2013: rumo aos protestos anti-Dilma?". *Lusotopie*, 17(1):88-111, 2018. DOI 10.1163/17683084-12341713 | 20 |
| `KUNRATH-SILVA_Ciclo-de-protestos-de-2013-objeto-de-disputa_Desigualdade-e-Diversidade-23_2023.pdf` | PT-01, PT-03, PT-04 | SILVA, M. K. "Ciclo de protestos de 2013: contribuições do campo de estudos de movimentos sociais e protesto para a análise de um objeto de disputa". *Desigualdade & Diversidade*, 23:57-90, 2023. DOI 10.17771/PUCRio.DDCIS.64184 | 34 |
| `ALONSO_Treze-a-politica-de-rua-de-Lula-a-Dilma_Companhia-das-Letras_2023.pdf` | PT-01, PT-02, PT-03, PT-04 | ALONSO, A. *Treze: a política de rua de Lula a Dilma*. São Paulo: Companhia das Letras, 2023 | 309 |

**De onde veio cada peça.** As quatro primeiras, da pasta de textos de ação coletiva do pesquisador. Kunrath Silva (2018), da OpenEdition (`journals.openedition.org/lusotopie/2568`), acesso aberto. Kunrath Silva (2023), do Maxwell PUC-Rio (`maxwell.vrac.puc-rio.br/64184`), acesso aberto. Alonso (2023), exemplar fornecido pelo pesquisador — **é o único livro de editora comercial do eixo**, e entrou pelo precedente do eixo 05, que já traz dois livros de método.

**Quatro armadilhas declaradas, e todas já custaram caro a este projeto em outras formas.**

1. **A numeração da revista não coincide com a do PDF em nenhum dos cinco artigos.** `fonte_pagina` guarda a **página do PDF**, que é a que `conferir_paginas.py` abre; a da revista, citável, está em `fonte_trecho` e em `PROCEDENCIA`, com o deslocamento de cada peça — 34, 62, 118, 20 e 56. Confundi-las produziria a cifra correta no referente errado.
2. **Duas peças não têm paginação impressa, por motivos diferentes.** Kunrath Silva (2018) é a edição eletrônica da OpenEdition, que não reproduz as páginas 88-111 do impresso: a unidade citável é o **parágrafo (§)**. Alonso (2023) é **edição digital, sem número de página de papel e sem rótulo de página no PDF**: "p. 224" é a página *deste arquivo*, e quem conferir no livro em papel não vai encontrar o mesmo número.
3. **Tatagiba (2014) é digitalização SEM CAMADA DE TEXTO.** PyPDF2 devolve string vazia nas 28 páginas. Foi lida por **renderização a 170 dpi**, a mesma técnica usada nos gráficos vetoriais do balanço do STF, e suas duas transcrições estão em `EXCECOES`, no alto de `conferir_paginas.py`, com o motivo. É a **quarta** peça do corpus sem camada de texto.
4. **Kunrath Silva (2018) tem camada de texto PRESENTE E ERRADA**, e isto é pior que a ausência. A fonte `Gentium-Book-Basic` vem subconjuntada com CMap defeituoso: o código de cada glifo é o ASCII menos 29. PyPDF2 e PyMuPDF devolvem os dois a mesma sopa de letras, e uma busca por qualquer frase do artigo "prova" com alta confiança que ele não a contém. `conferir_paginas.py` desfaz o deslocamento **span por span** — as outras fontes do mesmo arquivo saem corretas, e consertar a página inteira estragaria o que estava bom.

**No mesmo movimento, um defeito que estava lá desde o início do projeto e só apareceu agora:** **PyPDF2 injeta espaço DENTRO das palavras** em alguns PDFs ("destaca -se", "empac amentos"), e por isso nenhuma das 26 âncoras que entraram na segunda rodada casava, embora todas as frases estivessem nas páginas certas. A conferência passou a tentar PyMuPDF quando PyPDF2 não acha — **acréscimo, não troca**.

**ATENÇÃO — são duas Alonso e dois Kunrath Silva, e nenhum par é a mesma coisa.** Alonso (2012) é a história do conceito de repertório; Alonso (2023) é *Treze*, sobre a política de rua. E **nenhuma das duas é a "Alonso (2017)"** que PT-01 e PT-02 citavam desde agosto: essa obra nunca esteve no corpus e não foi lida. Kunrath Silva (2018) é o artigo da *Lusotopie* sobre a apropriação conservadora; Kunrath Silva (2023) é o da *Desigualdade & Diversidade*, sobre o ciclo como objeto de disputa.

---

### 13 — Literatura do bolsonarismo como mobilização

*Eixo aberto em 04/10/2026, pela tarefa 25, e ampliado no mesmo dia pela terceira rodada da tarefa 14.* **Dezoito peças, 453 páginas**, sob o recorte dado pelo pesquisador: o bolsonarismo como fenômeno de mobilização social e política, com foco nas dinâmicas de manifestação e protesto e nos repertórios próprios do campo das direitas. Como o 05 e o 12, está **fora da contagem documental**.

**As dezoito têm TRÊS procedências, e `PROCEDENCIA` as declara separadamente — a distinção é o que impede que um arquivo seja tomado por lastro:**

| Bloco | Quantas | Origem | Lida? |
|:--|--:|:--|:--|
| (a) | 12 | coleta via OpenAlex, DOI resolvido e título conferido | **não**, e não ancoram nada |
| (b) | 2 | mesma coleta, **lidas na fonte** por encaminhamento do pesquisador | **sim** — `ARAUJO E SALES 2022` e `FERNANDES E SILVA 2021` **ancoram registro com página** |
| (c) | 4 | **entregues pelo pesquisador**: as que a coleta automatizada não alcançou | **uma sim, três não** — `VON BÜLOW E ABERS 2024` foi lida na quarta rodada e **ancora PT-06 e PT-05** |

**Origem e leitura são eixos independentes, e a tabela acima é de origem.** Das dezoito peças, **três foram lidas** — duas do bloco (b) e uma do bloco (c) —, de modo que a contagem de lidas não bate com nenhum bloco isolado. É a distinção que `PROCEDENCIA` guarda peça por peça.


> **QUINZE DAS DEZOITO NÃO FORAM LIDAS E NÃO ANCORAM REGISTRO.** São fila de leitura, 400 páginas, e estão declaradas assim em `PROCEDENCIA`, peça por peça. Um arquivo dentro de `Fontes/` parece lastro; estas quinze não são. Quem for ancorar registro em qualquer uma delas precisa abrir, ler e pôr página — o padrão que o eixo 12 estabeleceu no mesmo dia, e que as três lidas seguiram. **Nenhuma das quinze bloqueia registro algum:** a camada conjuntural brasileira fechou em 04/10/2026, e o único contextual que resta, PT-08, pede literatura comparada sobre o Capitólio, que nenhuma delas cobre.
>
> **AS TRÊS LIDAS DECLARAM OFFSET, como as do eixo 12.** `FERNANDES E SILVA 2021`: impressa = PDF + 484, **lido** na p. 1 do PDF, que imprime *485*. `VON BÜLOW E ABERS 2024`: impressa = PDF + 997, **lido** no cabeçalho da p. 1, que traz *59, 998-1016*. `ARAUJO E SALES 2022`: impressa = PDF + 25, e este é **derivado, não lido** — nenhuma página deste PDF imprime número; o cabeçalho corrente traz o intervalo do artigo, *"p. 26-42"*, e o PDF tem exatamente 17 páginas. **Quarta variante de armadilha de numeração do corpus**, ao lado das três do eixo 12.

A lista completa, com a referência de cada peça e o registro a que ela pode servir **depois de lida**, está em [`projeto-pos-doc/13_LITERATURA-BOLSONARISMO.md`](../projeto-pos-doc/13_LITERATURA-BOLSONARISMO.md). Em resumo: Messenberg (2017), Rocha (2019) e Tatagiba (2018) para **PT-02**; Santos e Tanscheit (2019), Cesarino (2019), Kaysel e Bianchi (2025) e Carvalho e Tatagiba (2025) para **PT-04**; Mendonça e Domingues (2021), von Bülow e Abers (2024) e Farias, Casarões e Magalhães (2022) para **PT-05**; Cesarino (2022), Nunes (2024), Mendonça e Freitas (2022), Chagas e Carreiro (2022) e Bastos e Recuero (2023) para **PT-06**; e Gohn (2019) para a camada conjuntural inteira **e para a tarefa 10**, por ser o único balanço da literatura brasileira de protesto no corpus.

**O que as três lidas ancoram, e é âncora conferida pelo ciclo, não previsão:** `ARAUJO E SALES 2022` ancora **PT-02** (genealogia do apelo militar depois de junho de 2013), **PT-04** (a expressão política antissistêmica), **PT-05** — que **saiu de contextual** por ela —, **PT-06** (repertório e enquadramento) e **PT-12** (genealogia do frame). `FERNANDES E SILVA 2021` ancora **PT-02**, e fez mais que ancorar: **tirou do campo a "tolerância policial"**, que o codebook afirmava sem fonte desde agosto e que a peça contradiz. `VON BÜLOW E ABERS 2024` ancora **PT-06** — **fechou o registro**, o último contextual da camada brasileira — e **PT-05**, em corroboração dupla; e também **retificou** o mecanismo de PT-06: o campo atribuía à pandemia a consolidação do ecossistema informacional, e as autoras documentam redes que cresciam desde o início dos anos 2000. **A pandemia carrega uma infraestrutura que encontra pronta.**

**Uma ressalva de lastro que vale no eixo inteiro.** O `mecanismo_causal` de PT-06 nomeia Telegram e WhatsApp. Von Bülow e Abers as nomeiam, mas **por citação de segunda mão** — os estudos de plataforma são de Soares et al. (2021) e Nascimento et al. (2020), nenhum dos dois no corpus. A regra do projeto proíbe lastrear cifra conferida só contra outra citação dela, e por isso as duas plataformas estão **declaradas como não verificadas** no status do registro.

**O que a coleta mostrou sobre acesso, e o que a entrega corrigiu no enunciado.** Das dezoito peças escolhidas, **as catorze que chegaram por coleta automatizada são todas de plataformas latino-americanas ou de acesso aberto diamante** — SciELO, portais de universidade, OpenEdition, Cogitatio. As quatro que não chegaram são de editora comercial grande: Cambridge (429), SAGE (403), Oxford (403) e um portal OJS equatoriano que recusa requisição automatizada até na página do artigo (403). Três delas são declaradas **ouro ou híbrida** pelo OpenAlex.

**O pesquisador entregou as quatro no mesmo dia, e isso muda o enunciado do achado.** O correto é: *a literatura do bolsonarismo ao alcance de COLETA AUTOMATIZADA neste projeto é a brasileira em acesso aberto diamante* — e não que a outra esteja fora do alcance do projeto. O PDF de Bastos e Recuero traz licença **CC BY impressa na primeira página**: a obra era livre, o acesso não era. É a mesma lição que a tarefa 14 aprendeu no mesmo dia em outra forma: **uma varredura prova a lacuna do que varreu** — aqui, do método de coleta.

**Duas atribuições vinham erradas na lista do projeto, e abrir o arquivo corrigiu.** Gohn é de **2019**, não 2020 (o DOI traz `.1.2019.`). Von Bülow e Abers são do fascículo de **2024**, v. 59, p. 998-1016 — o slug `gov.2022.14` é o ano da publicação on-line, não o do fascículo. E Farias, Casarões **e Magalhães** são três autores, não dois. **O ano do DOI não é o ano de publicação.**

**Um descarte que vale registro.** A tentativa na Cambridge devolveu uma página de erro de 1,3 KB que o `curl` gravou com extensão `.pdf`. Foi apagada. HTML de erro guardado como PDF é defeito silencioso do tipo exato que este projeto caça: todo arquivo desta coleta foi conferido para começar com `%PDF`, abrir no PyPDF2 e devolver texto na primeira página — e as quatro entregues passaram pela mesma conferência.

**E TRÊS armadilhas de transcrição que nasceram neste eixo.** `conferir_paginas.py` extrai transcrição fatiando `fonte_trecho` em todo caractere de aspa e ficando com os índices ímpares — e isso tem três consequências, duas já consertadas.

1. **Aspa dentro de aspa** inverte a paridade e o pedaço restante é descartado **em silêncio**: foi o que aconteceu com *"A reivindicação do tratamento precoce e do "kit Covid""*, de Araujo e Sales, em PT-06, e o registro teria entrado no ciclo com uma transcrição conferida em vez de três. Achado pela prova negativa, corrigido **na transcrição**, não no script: **esta continua sem conserto, de propósito**, e a saída é escolher outro trecho da mesma página.
2. **Apóstrofo dentro de palavra** era tomado por delimitador, porque `ASPAS_FECHA` contém U+2019 — o apóstrofo de todo texto em inglês, *"Bolsonaro's"*. **Consertado em 04/10/2026**, quando a primeira peça em inglês foi ancorar registro: o apóstrofo intrapalavra é mascarado antes de fatiar. Auditado o codebook no dia, as 57 transcrições então existentes não eram afetadas, por serem em português.
3. **Hifenização de quebra de linha** não era unida: `norm_busca` apagava o hífen e deixava o espaço, de modo que o PDF *"mobiliza-\ntion"* não casava com *"mobilization"*. **Consertado no mesmo dia.** Os dois consertos foram provados invariantes sobre as 66 âncoras anteriores.

> **A regra que as três deixam: o silêncio do ciclo não distingue *conferida-e-OK* de *nunca-conferida*.** É por isso que a prova negativa por injeção de defeito não é cerimônia.

---

### 14 — Literatura brasileira em livro

*Eixo aberto em 08/10/2026, pela tarefa 10, e ampliado no mesmo dia.* **Doze peças, 1.854 páginas** — seis capítulos do volume *Giros à direita: análises e perspectivas sobre o campo líbero-conservador* (Sobral, Editora SertãoCult, 2020) e o livro *O Brasil no inferno global: capitalismo e democracia fora dos trilhos* (São Paulo, FFLCH/USP, 2022). Como os eixos 05, 12 e 13, está **fora da contagem documental**.

> **NENHUMA DAS DOZE FOI LIDA, E NENHUMA ANCORA REGISTRO.** Fila de leitura, declarada peça por peça em `PROCEDENCIA`. Um arquivo dentro de `Fontes/` parece lastro; estas doze não são.
>
> **Três livros entraram entregues pelo pesquisador** — Gurza Lavalle, Carlos, Dowbor e Szwako (2018, EdUERJ), Abers (2021, Editora UnB) e Madeira, Marona e Del Río (2022, EdUERJ) —, os mesmos que o Bunny Shield barrava. **Os três têm OFFSET A DETERMINAR:** a ficha catalográfica anuncia menos páginas impressas do que o PDF tem (411/414, 356/359, 423/427), de modo que não se pode assumir PDF = impressa. **E dois capítulos a mais de *Giros à direita*** entraram por encaminhamento: Ramírez (offset **+7**) e Faria (offset **+109**), os dois começando na PDF p. 13 como os outros seis.
>
> **O volume inteiro de *Giros à direita* está depositado no IBICT** (`deposita/166`, "Faria & Marques - Giros à Direita.pdf"), o que tornaria os oito offprints redundantes e retiraria a armadilha de offset por capítulo. **Não foi trocado: é decisão do pesquisador.** E o quarto livro da lista de barrados, Rich (2021), saiu por outra razão — **não é de acesso aberto, apesar de o OpenAlex o declarar ouro**: está à venda em livraria.

**O que a coleta mostrou, e é resultado antes de qualquer leitura.** O cânone brasileiro de movimentos sociais **não está em acesso aberto como livro**: busca nominal por dezenove autores, exigindo autoria casada, devolveu **zero** para Gohn, Sader, Scherer-Warren, Avritzer, Doimo, Telles, Abranches, Nobre, Solano e Messenberg. São livros de editora comercial e seguem dependendo dos arquivos do pesquisador, como Alonso (2023) dependeu. Detalhe em [`projeto-pos-doc/14_LIVROS-BRASILEIROS.md`](../projeto-pos-doc/14_LIVROS-BRASILEIROS.md).

> **QUINTA VARIANTE DE ARMADILHA DE NUMERAÇÃO, e é a mais perigosa do corpus.** Os seis capítulos de *Giros à direita* são **offprints**: cada PDF traz as **mesmas 12 páginas de pré-textuais do volume** — capa sem camada de texto, biografias de todos os colaboradores, folha de rosto, ficha, sumário, apresentação — e o capítulo só começa na **PDF p. 13**. Logo o deslocamento é **diferente em cada arquivo**: Löwy +0, Montenegro +33, Hoeveler +58, Lerner +77, Cazetta +161, Gentile +209.
>
> **A mesma página de PDF significa páginas impressas diferentes em arquivos distintos do mesmo volume.** E citar PDF p. 1-12 em qualquer um deles é citar o pré-textual do volume **através do arquivo errado** — as doze páginas são idênticas nos seis, de modo que a conferência de transcrição casaria e o vínculo estaria errado. **Regra operacional: no eixo 14, só cite PDF p. ≥ 13, e sempre pelo arquivo do capítulo.**
>
> O offset de `SINGER, ARAUJO E RUGITSKY 2022` **não está declarado de propósito**: é livro inteiro, 374 páginas de PDF, e a paginação impressa precisa ser conferida na leitura. Não assumir PDF = impressa antes de abrir.

**Duas peças que valem destaque.** `HOEVELER 2020`, sobre fóruns e redes organizativas da extrema direita latino-americana, é a peça do corpus **mais próxima do mecanismo que PT-08 afirma** — difusão transnacional — e pelo lado brasileiro, que faltava. `LERNER 2020`, sobre a rede conservadora no Facebook, é candidata a dar **âncora de primeira mão** à infraestrutura digital que PT-06 nomeia e que von Bülow e Abers (2024) só reportam por citação de segunda mão; muda a plataforma, não fecha a ressalva.

**Um defeito de verificação que vale como armadilha registrada.** A conferência de dois eixos reprovou os seis capítulos na primeira passagem, porque amostrava as **quatro primeiras páginas** — e nos offprints as duas primeiras são capa sem texto e biografias do volume. Os seis são arquivos distintos (SHA-256 distintos, 30 a 88 mil caracteres cada) e cada um contém o próprio autor e título. **Verificação de dois eixos amostrada nas primeiras páginas falha em offprint com pré-textual comum:** conferir no texto inteiro. Reconferidos: 6 de 6.

**O que ficou barrado, e é o padrão já conhecido.** Quatro livros identificados e de acesso aberto estão no **SciELO Livros**, cujo host `books.scielo.org` está atrás do **Bunny Shield**, desafio JavaScript de detecção de bot: HTTP 403 ao curl e ao `urllib`, com ou sem cabeçalhos completos. Nenhum tem cópia em outro depósito — conferido no OpenAlex, no DOAB e nos repositórios da UnB e da UFRGS. São Gurza Lavalle et al. (2018), Abers (2021), Rich (2021) e Madeira, Marona e Del Río (2022). **O limite é da coleta automatizada, não do projeto:** abrem num navegador comum, e os DOIs estão no documento 14.

---

## Pendências

### Exigem coleta manual

**Acórdão do TSE — indeferimento do registro de candidatura (PT-03E), RCand 0600903-50.2018.6.00.0000.**
O buscador de jurisprudência do TSE (`jurisprudencia.tse.jus.br`) é protegido por **hCaptcha**, que não deve ser contornado por automação. A coleta precisa ser feita por pessoa, no navegador:
1. Acessar https://jurisprudencia.tse.jus.br/
2. Resolver o captcha e pesquisar por `0600903-50.2018.6.00.0000`
3. Baixar o inteiro teor em `01_Arco-judicial_2017-2021/`, nomeando `TSE_RCand-0600903-50_Acordao_2018-09-01.pdf`

Alternativa: Consulta Unificada PJe do TSE (`consultaunificadapje.tse.jus.br`), que responde sem captcha mas exige navegar até o documento certo.

### Ainda não localizados em fonte oficial

| Documento | Fase | Observação |
|:--|:--|:--|
| Sentença de 1ª instância (Moro, 12/07/2017) — inteiro teor | PT-03A | Consulta processual da JFPR/e-proc. **Baixa prioridade:** o dispositivo já está transcrito no acórdão do TRF-4 |
| Balanço "Democracia Inabalada" (29/04/2026, 1.402 condenados) | PT-61 | Documento distinto do livro de 2023. **Não indexado como PDF** — divulgado pelo gabinete do min. Moraes, aparentemente como apresentação à imprensa. Solicitar à assessoria do STF |
| Laudos periciais do Instituto de Criminalística/PF | PT-38 | Provavelmente sob restrição de acesso |


---

## Nota técnica de acesso

Registrada para quem repetir a coleta.

**O erro relatado antes ("STF inacessível") era de ferramenta, não do site.** O que ocorre:

- O `portal.stf.jus.br` e o `redir.stf.jus.br` estão atrás de **AWS WAF com desafio JavaScript**. Requisições sem execução de JS recebem `HTTP 202` com corpo vazio — o que se parece com bloqueio, mas é o desafio não resolvido.
- A solução usada: abrir qualquer página do STF num navegador real, deixar o WAF emitir o cookie `aws-waf-token`, e reaproveitar esse cookie nas requisições de download. O token expira em algumas horas.
- Os inteiros teores ficam em `https://redir.stf.jus.br/paginadorpub/paginador.jsp?docTP=TP&docID=<ID>`, onde `<ID>` é o mesmo `idDocumento` devolvido pelo campo `inteiro_teor_url` da API de busca (`POST https://jurisprudencia.stf.jus.br/api/search/search`).
- **TRF-4 e TSE não bloqueiam** consultas automatizadas; foram consultados diretamente. O acórdão do TRF-4 está em `https://www.trf4.jus.br/trf4/revistatrf4/arquivos/Rev97.pdf`.

**Cuidado ao conferir contagem de páginas:** `file` e `pdfinfo` subcontaram grosseiramente estes PDFs (relataram 84 páginas para um arquivo de 464). Use `PyPDF2` ou conte os marcadores "Página N de M" do rodapé do STF.

---

## Uso já feito destas fontes — situação em 14/08/2026

**A recodificação sobre fonte primária está concluída.** Foram seis rodadas, entre 12 e 14/08/2026, e o resultado é que **49 registros do codebook têm citação por página** do Relatório Final da CPMI, com transcrição literal arquivada em `../Caderno-de-evidencias/`. A numeração impressa do relatório **coincide com a do PDF**, o que torna a citação inequívoca.

No conjunto dos 81 sub-eventos: **51 ancorados em fonte primária**, 19 confirmados por outra via, 7 contextuais, 3 a verificar e 1 inferência declarada.

**Registros novos extraídos das fontes primárias:** PT-08A a PT-08C (operação da PRF no segundo turno, CPMI p. 465-470), PT-10A (MBVA, 272 caminhões, p. 884-887), PT-12A (rede de financiamento, p. 577-578 e 880-884), PT-19B (grupo "Difusão", AP 2668 p. 495-496), PT-20A e PT-20B (dispensa de reforço pelo GSI e Relatório de Inteligência nº 006/2023).

**A previsão de que os registros restantes eram dispensáveis estava errada, e o registro fica.** Ela constava aqui em 12/08: os 23 registros de $T_0$ que citavam a CPMI por via secundária descreveriam "fatos incontroversos". Recodificados a pedido do pesquisador, produziram três dos achados mais fortes do projeto — o regime de sobreaviso que explica mecanicamente a latência do Batalhão de Choque, o "Fiquem à vontade" de 01/11 como certificação por elite, e o Sri Lanka (não o Capitólio) como precedente invocado. Detalhes na seção 2.6 do relatório.

## O acórdão da AP 2668 foi aberto — resultado negativo e informativo

Feito em 12/08/2026. O acórdão (1.991 p.) era a única fonte capaz de arbitrar a contradição de PT-32: às 14h56 o secretário de Segurança do DF ordena "Não deixem chegar ao Supremo"; às 15h16 o comandante em campo libera justamente esse acesso, "sem justificativa".

**Nem o acórdão nem a denúncia da PGR mencionam a mensagem, o horário 15h16 ou o tenente.** O STF adotou uma terceira moldura — **omissão dolosa** da cúpula civil da SSP-DF (art. 359-M) —, sob a qual uma ordem isolada é irrelevante: imputa-se o conjunto do não agir. Consequência prática para a citação: a mensagem das 14h56 é **achado exclusivo da CPMI, sem validação judicial**. Registro completo no item 2 de `../docs/PENDENCIAS-ANALITICAS.md`.

*(Atenção a um falso positivo encontrado nessa busca: o "Rafael Martins de Oliveira" que aparece na denúncia não é o tenente da PMDF, e sim um militar do grupo "Kids Pretos".)*

## O que ainda falta coletar

Uma peça depende de coleta manual (acórdão do TSE, seção Pendências acima) e três não foram localizadas em fonte oficial. A agenda consolidada está no item 11 de `../docs/PENDENCIAS-ANALITICAS.md`, e os comandos de coleta em `../scripts/baixar_fontes.sh` (`bash scripts/baixar_fontes.sh listar`).

---

## Auditoria de 16/08/2026 — este inventário divergia do codebook

**Leia [`../reports/AUDITORIA-FONTES.md`](../reports/AUDITORIA-FONTES.md): ele, e não este arquivo, é a peça autoritativa sobre o vínculo registro ↔ documento ↔ página.**

A auditoria encontrou que atribuições declaradas *aqui* nunca haviam chegado ao codebook. Cinco arquivos desta pasta estavam sem vínculo com registro nenhum, entre eles o livro oficial do STF (atribuído a PT-38 neste LEIA-ME, ausente do registro), a questão de ordem da AP 2668 (PT-56) e o segundo AgR do HC 193.726 (PT-06B). Todos foram vinculados.

Duas consequências que este inventário precisa registrar:

1. **PT-53 e PT-61 foram rebaixados** de `Confirmado` para `A verificar`. Ambos se apoiam no balanço "Democracia Inabalada" de 29/04/2026, que consta da seção "Ainda não localizados" acima. A cifra de 1.402 condenados **não deve ser citada como dado oficial** até a peça chegar.
2. **A camada de texto foi reconferida com PyPDF2**, amostrando cinco pontos ao longo de cada documento em vez da primeira página. Os 16 PDFs e as 6.790 páginas se confirmam, e nenhum precisa de OCR — a página 1 de três deles é capa sem texto, o que produz falso alarme em conferências que só olham o início.

**Regra que passa a valer:** um arquivo novo nesta pasta só está incorporado quando (a) tem procedência declarada em `PROCEDENCIA`, dentro de `../scripts/gerar_codebook.py`, e (b) está vinculado a um registro no JSON ou declarado como bibliografia. `../scripts/verificar_integridade.py` falha enquanto isso não for verdade.
---

### 15 — Literatura comparada sobre o 6 de janeiro

*Eixo aberto em 08/10/2026.* **Duas peças, 28 páginas — as duas LIDAS e as duas ANCORANDO PT-08**, que era o último registro contextual do codebook e deixou de ser. Como os eixos 05, 12, 13 e 14, está **fora da contagem documental**.

O eixo nasce porque a lacuna de PT-08 nunca foi brasileira: era literatura comparada sobre os Estados Unidos, e nenhuma das dezoito peças do eixo 13 a cobria — nem Bastos e Recuero (2023), que trata do Congresso brasileiro e não do Capitólio.

| Peça | Referência | p. | Paginação | Ancora |
|:--|:--|--:|:--|:--|
| **CASTAÑEDA E JENKS 2023** | "January 6th and De-Democratization in the United States". *Social Sciences*, 12(4), art. 238 | 15 | **sem paginação impressa** | o **mecanismo** de PT-08 |
| **CHEN, LUKITO E KOO 2023** | "Comparing the #StopTheSteal Movement across Multiple Platforms". *Social Media + Society*, 9(3):1-13 | 13 | impressa = PDF + 0, **lido** | o **evento** e o **enquadramento** |

> **SEXTA VARIANTE DE ARMADILHA DE NUMERAÇÃO, e a causa é nova.** Castañeda e Jenks não tem paginação impressa — e não por ser edição digital nem por a plataforma numerar parágrafos. É porque **a MDPI pagina por NÚMERO DE ARTIGO**: a referência é 12(4):238, onde 238 é o artigo, e o cabeçalho corrente de toda página é "Soc. Sci. 2023, 12, 238". Quem procurar intervalo de páginas no fascículo não encontra nenhum. As páginas citadas são do PDF.

**Chen, Lukito e Koo aplicam a tipologia de SNOW E BENFORD** — diagnóstico, prognóstico e motivacional, mais um dispositivo próprio, pistas de violência —, que é marco teórico declarado deste projeto, sobre 675.336 posts de Facebook, Twitter e Parler. **E não dizem uma palavra sobre o Brasil:** zero ocorrências de "Brazil", "Bolsonaro" e "January 8".

**Castañeda e Jenks ancoram o mecanismo**, com a frase que o registro precisava e no vocabulário de Tilly: o ataque ao Congresso *"has now become a contentious performance that was used by the equivalent actors in Brazil on January 8, 2023"* (PDF p. 10), com Steve Bannon nomeado como agente de transmissão. **LIMITE DECLARADO NO REGISTRO:** é **uma** frase, de passagem, sem aparato de evidência do lado brasileiro.

> **UM ALERTA DE MÉTODO QUE ESTE EIXO PRODUZIU, e vale mais que as âncoras.** Para decidir se a peça servia, contei termos no texto integral: **"Bolsonaro" 0, "diffusion" 0, "emulation" 0, "transnational" 0, "Brazil" 1.** A medição estava certa e a conclusão que ela sugeria — *a peça não serve* — estava **errada**: a única ocorrência de "Brazil" é exatamente a frase decisiva. **Um autor pode afirmar a proposição inteira sem usar nenhuma das palavras com que você a nomeia.** Contagem de termo é medida de palavra, não de proposição — irmã semântica da armadilha da ligadura ﬁ. A saída prática é ler o contexto de cada ocorrência, não o histograma.

**A ressalva do Sri Lanka fica reforçada, não contrariada.** O Capitólio é referência de **repertório** e o Sri Lanka é referência de **eficácia** (CPMI, p. 614), e dizer que o ataque ao Congresso se tornou uma *performance contenciosa* usada no Brasil é precisamente uma afirmação de repertório.

