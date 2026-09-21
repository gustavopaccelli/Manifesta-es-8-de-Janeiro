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

`Livro_Process tracing.pdf` (104 p.) · `process-tracing-research-designs-a-practical-guide.pdf` (5 p.) · `LEIA-ME_status_downloads.md` (status do levantamento bibliográfico)

**Sete sínteses de literatura** (`*_LeapSpace.docx`), cobrindo os conceitos do referencial teórico — ~31,6 mil palavras e **410 DOIs distintos**. Cinco entraram em 13/08/2026; **duas foram acrescentadas em 01/09/2026** (assinaladas com ✚), na mesma data em que as cinco anteriores foram substituídas por reemissões:

| Arquivo | DOIs | Cobre |
|:--|--:|:--|
| `Process_tracing_LeapSpace.docx` | 77 | método, padrões evidenciais, reconstrução de mecanismos |
| `Causal_mechanisms_in_social_science_LeapSpace.docx` | 89 | mecanismo vs. variável; explicação mecanística em sociologia histórica |
| `Political_Process_by_Charles_Tilly_LeapSpace.docx` | 82 | repertórios, formação do Estado, democratização |
| `Mobilization_structures_LeapSpace.docx` | 76 | recrutamento, liderança, participação |
| ✚ `Political_and_discursive_opportunities_LeapSpace.docx` | 46 | oportunidades políticas e discursivas; estrutura de oportunidade de mediação |
| ✚ `Framing_process_and_alignment_LeapSpace.docx` | 44 | enquadramento, alinhamento de quadros, quadros-mestres, narrativa |
| `Protest_cycle_LeapSpace.docx` | 24 | início e agrupamento de ciclos; limiares de mobilização |

> **Sobre a substituição de 01/09/2026.** As cinco reemissões são **substantivamente idênticas** às versões de 13/08: a comparação do texto extraído acusou diferença de uma única linha — o carimbo de geração, que passou de `Generated by LeapSpace` para `Generated by LeapSpace, Fri Aug 14 2026`. Em `Protest_cycle` nem isso mudou (só `docProps/core.xml`). A troca foi feita para fixar a data de geração no próprio documento; **nada do conteúdo, das contagens ou dos DOIs foi alterado por ela**. A contagem de DOIs de `Causal_mechanisms` passou de 90 para 89 por recontagem no arquivo (DOIs distintos), não por mudança de conteúdo.

⚠️ **Não são fonte citável.** São sínteses geradas por sistema automatizado (LeapSpace), sem revisão por pares e sem autoria identificável. Servem como **mapa de leitura** e como lista de DOIs para busca — a citação vai sempre para o trabalho original, lido na fonte. Os DOIs precisam de verificação no CrossRef antes de qualquer incorporação: o levantamento original deste projeto já trouxe um DOI fabricado, corrigido em `../LEIA-ME_metodologia_verificacao.md`. Encaminhamento detalhado no item 11.3 de `../PENDENCIAS-ANALITICAS.md`.

**Primeira leva de verificação executada em 01/09/2026 — 10 itens, dos quais 4 divergentes.** A suspeita registrada acima confirmou-se: as listas de referências destas sínteses contêm erros de metadados demonstráveis. Achados que valem para todo o acervo:

- `10.3998/mpub.2556282`, atribuído a "Beach & Pedersen (2019)", é a **1ª edição, de 2013**. O DOI da 2ª edição, já usado no projeto, é `10.3998/mpub.10072208`.
- `10.1007/9781139858472`, atribuído a Bennett & Checkel, **não existe** (HTTP 404). O correto é `10.1017/CBO9781139858472` — o prefixo 10.1007 é da Springer, não da Cambridge. E os dois são **organizadores**, não autores.
- Escribà-Folch (2008), em *Dados*, é indexado pelo título em inglês, mas **o artigo foi publicado em português**: "Participação arriscada: manifestações e tumultos em regimes ditatoriais".
- McCammon (2013), "Discursive Opportunity Structure", tem **duas versões com DOIs distintos**: a de 2013 e a `.pub2`, de 27/09/2022.
- Há ainda ruído grosseiro nas listas: um item datado de **2099**; um registro reduzido a link do Scopus sem citação; itens de migração, clima de negócios e deslizamentos de terra sem relação com o tema; entradas duplicadas; e ao menos uma **colisão de homônimos** (Beach, D., de *The Lancet Global Health*, que não é Derek Beach).

Ficha completa da verificação em `../../projeto-pos-doc/08_BIBLIOGRAFIA-METODOLOGICA.md`. **A regra do projeto permanece: nenhum item destas sínteses entra em texto sem conferência item a item na fonte.**

### 11 — Tese de doutorado do pesquisador

*Eixo aberto em 19/08/2026.*

| Arquivo | Registro | Origem |
|:--|:--|:--|
| `PACCELLI_Tese-doutorado_UFJF_2024.docx` | — (não ancora registro) | PACCELLI, Gustavo. **"Estruturas de mobilização e Oportunidades Políticas: análise dos ciclos de protestos no Brasil contemporâneo"**. Tese de doutorado, Programa de Pós-Graduação em Ciências Sociais, Universidade Federal de Juiz de Fora, 2024. Orientação: Christiane Jalles de Paula. ~70 mil palavras, **302 referências** |

**Por que entra no corpus.** É o **antecedente teórico** de que este projeto parte. A tese analisa três ciclos de protesto no Brasil — Fora Collor (1992), junho de 2013 e as manifestações de 2015 — pela interação entre **estruturas de mobilização** e **oportunidades políticas e discursivas**, e sua última seção substantiva ("Dos coletivos progressistas aos movimentos de direita") encerra exatamente onde o 8 de Janeiro começa. O par analítico que organiza este projeto vem dela, e não é importado de fora: a tese já mobiliza **Koopmans & Olzak (2004)** e **Giugni, Koopmans, Passy & Statham (2005)** sobre oportunidades discursivas e violência de extrema-direita — o instrumento teórico para explicar a virada violenta já estava construído.

**O que ela não é.** Não é fonte de evento e **não ancora registro nenhum do codebook**. Declarada em `PROCEDENCIA` (`scripts/gerar_codebook.py`) com o tipo `bibliografia`, pela mesma razão das sínteses do eixo 05: é insumo de leitura e referencial, não evidência empírica sobre o 8 de janeiro. Formato `.docx`, sem paginação estável — citar por seção, não por página.

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

**Nem o acórdão nem a denúncia da PGR mencionam a mensagem, o horário 15h16 ou o tenente.** O STF adotou uma terceira moldura — **omissão dolosa** da cúpula civil da SSP-DF (art. 359-M) —, sob a qual uma ordem isolada é irrelevante: imputa-se o conjunto do não agir. Consequência prática para a citação: a mensagem das 14h56 é **achado exclusivo da CPMI, sem validação judicial**. Registro completo no item 2 de `../PENDENCIAS-ANALITICAS.md`.

*(Atenção a um falso positivo encontrado nessa busca: o "Rafael Martins de Oliveira" que aparece na denúncia não é o tenente da PMDF, e sim um militar do grupo "Kids Pretos".)*

## O que ainda falta coletar

Uma peça depende de coleta manual (acórdão do TSE, seção Pendências acima) e três não foram localizadas em fonte oficial. A agenda consolidada está no item 11 de `../PENDENCIAS-ANALITICAS.md`, e os comandos de coleta em `../scripts/baixar_fontes.sh` (`bash scripts/baixar_fontes.sh listar`).

---

## Auditoria de 16/08/2026 — este inventário divergia do codebook

**Leia [`../reports/AUDITORIA-FONTES.md`](../reports/AUDITORIA-FONTES.md): ele, e não este arquivo, é a peça autoritativa sobre o vínculo registro ↔ documento ↔ página.**

A auditoria encontrou que atribuições declaradas *aqui* nunca haviam chegado ao codebook. Cinco arquivos desta pasta estavam sem vínculo com registro nenhum, entre eles o livro oficial do STF (atribuído a PT-38 neste LEIA-ME, ausente do registro), a questão de ordem da AP 2668 (PT-56) e o segundo AgR do HC 193.726 (PT-06B). Todos foram vinculados.

Duas consequências que este inventário precisa registrar:

1. **PT-53 e PT-61 foram rebaixados** de `Confirmado` para `A verificar`. Ambos se apoiam no balanço "Democracia Inabalada" de 29/04/2026, que consta da seção "Ainda não localizados" acima. A cifra de 1.402 condenados **não deve ser citada como dado oficial** até a peça chegar.
2. **A camada de texto foi reconferida com PyPDF2**, amostrando cinco pontos ao longo de cada documento em vez da primeira página. Os 16 PDFs e as 6.790 páginas se confirmam, e nenhum precisa de OCR — a página 1 de três deles é capa sem texto, o que produz falso alarme em conferências que só olham o início.

**Regra que passa a valer:** um arquivo novo nesta pasta só está incorporado quando (a) tem procedência declarada em `PROCEDENCIA`, dentro de `../scripts/gerar_codebook.py`, e (b) está vinculado a um registro no JSON ou declarado como bibliografia. `../scripts/verificar_integridade.py` falha enquanto isso não for verdade.
