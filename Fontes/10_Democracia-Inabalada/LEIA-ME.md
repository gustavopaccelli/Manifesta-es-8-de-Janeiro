# 10 — Democracia Inabalada

Pasta criada em **16/08/2026** para reunir as peças da campanha institucional do STF e o relatório de balanço do Gabinete do Min. Alexandre de Moraes.

## A distinção que precisa ficar clara antes de tudo

**São dois documentos diferentes, com o mesmo nome de campanha, separados por quase três anos.** Confundi-los foi a origem de uma ressalva que ficou aberta no projeto por dias.

| Peça | Data | O que é |
|:--|:--|:--|
| **Livro / ebook** `8.1.2023: Democracia Inabalada` | ago/2023 | Obra fotográfica e narrativa sobre o vandalismo e a restauração do edifício-sede. **Não traz estatística de responsabilização.** |
| **Relatório do Gabinete do Min. Alexandre de Moraes** | **29/04/2026** | Balanço estatístico do ciclo judicial: 1.402 réus responsabilizados, sanções, prisões, núcleos. **É este que ancora PT-53 e PT-61.** |

## Acervo

### `STF_Gabinete-Moraes_Balanco-8-de-Janeiro_2026-04-29.pdf` — fonte primária

15 p. · SHA-1 `8089338fd4051ea521ab345807a4e16d77f0bd92` · 3.243.181 B
Origem: bucket oficial do STF em S3 (`noticias-stf-wp-prd.s3.sa-east-1.amazonaws.com`), fornecido pelo pesquisador em 16/08/2026.
**Ancora PT-53** (p. 4) **e PT-61** (p. 6, 7, 8, 10, 11, 13, 14).

Dados conferidos na camada de texto:

| Seção | Conteúdo |
|:--|:--|
| I — Dados gerais (p. 4) | 1.878 investigações instauradas; denúncias por inquérito: 628 executores (INQ 4922), 1.160 incitadores (INQ 4921), 31 núcleos principais; 177 em andamento; 67 em fase de recebimento; 144 arquivamentos por ausência de justa causa |
| II — Réus responsabilizados (p. 6) | **1.402** = 29 núcleos principais + 402 crimes graves + 419 crimes menos graves + 552 ANPPs |
| III — Sanções (p. 7) | 431 penas privativas de liberdade + multa + R$ 30 mi de danos morais coletivos (30,7%); 419 convertidas em restritivas de direito + R$ 5 mi (29,9%); 552 ANPPs (39,4%) |
| IV — Penas (p. 8) | Tabela demonstrativa. Máxima: 27 anos e 3 meses (1 réu, 0,07%). Maior contingente: 404 réus com 1 ano (28,82%); 213 com 14 anos (15,19%) |
| V — Prisões (p. 10-11) | **190 presos** (10,12% dos réus): 169 definitivas (9%) e 21 processuais (1,12%) |
| VI — Núcleos (p. 13-14) | 29 condenações nas APs 2668, 2693, 2694 e 2696. 21 sessões de julgamento (set–dez); 31 réus: 25 condenações integrais, 2 parciais, 2 desclassificações, 2 absolvições; 127 advogadas e advogados; 154 testemunhas (8 de acusação, 146 de defesa). Núcleos: 1-Crucial, 2-Estratégico, 3-Executores, 4-Desinformação |

### Os dois gráficos vetoriais — lidos por renderização em 16/08/2026

Os valores das p. 5 e 6 **não saem na camada de texto**: são vetoriais. Foram lidos renderizando as páginas com PyMuPDF. O resultado **corrigiu um erro do codebook**.

**AÇÕES PENAIS (p. 6)** — por situação e por classe de crime:

| Situação | Crimes Menos Graves | Crimes Graves e Núcleos | **Total** |
|:--|--:|--:|--:|
| Condenações | 419 | 431 | **850** |
| Absolvições | 8 | 8 | **16** |
| Instrução em andamento | 192 | 267 | **459** |
| Extinções de punibilidade (art. 107, I) | 5 | 5 | **10** |
| **TOTAL DE AÇÕES PENAIS** | | | **1.335** |

> ⚠️ **O total é 1.335, não "mais de 1.600".** A afirmação anterior de PT-53 estava errada e foi retirada. O número **1.618** que circulava pertence a **audiências de custódia** (p. 5) — quarto caso no projeto de cifra correta aplicada ao referente errado, depois de PT-34, PT-12 e PT-28.

**ATOS PROCESSUAIS (p. 5)** — por ano:

| Ato | 2023 | 2024 | 2025 | 2026 | **Total** |
|:--|--:|--:|--:|--:|--:|
| Audiências de custódia | 1.397 | 137 | 51 | 33 | **1.618** |
| Audiências de instrução | 232 | 860 | 187 | 50 | **1.329** |
| Oitivas de testemunhas de acusação | 719 | 1.660 | 143 | 51 | **2.573** |
| Oitivas de testemunhas de defesa | 386 | 980 | 287 | 90 | **1.743** |
| Interrogatórios judiciais dos réus | 232 | 860 | 187 | 50 | **1.329** |

**Coerência interna, conferida e fechada:** 850 condenações + 552 ANPPs = **1.402 réus responsabilizados**; e 431 (crimes graves e núcleos) = 29 núcleos + 402 crimes graves. Os dois caminhos batem.

⚠️ **Uma ressalva remanescente, da própria peça.** A aritmética das denúncias não fecha: 628 + 1.160 + 31 = 1.819, e o total impresso é 1.878 — diferença de 59, não explicada. O rótulo do total é "investigações instauradas", não "denúncias". **Não force a soma ao citar.**

### `STF_Democracia-Inabalada_Ebook_28x28cm.pdf` — cópia canônica do livro

210 p. · SHA-256 `6082d29dfec7af13…` · 24.739.308 B · **ancora PT-38**

**Consolidado em 16/08/2026.** Havia duas cópias byte-idênticas no corpus — esta e uma em `03_T0_8-de-janeiro/`. Conferido o SHA-256 de ambas, a segunda foi removida (backup em `.backup_pre_lula/`) e PT-38 foi repontado para cá. Esta é a cópia baixada do domínio oficial do STF, e a única que resta.

### `STF_Democracia-Inabalada_Folder.pdf` — peça de divulgação

6 p. · **sem camada de texto** (peça gráfica pura). Conteúdo lido por extração das imagens embutidas:

| Página | Conteúdo |
|:--|:--|
| 1 | Capa: `#democraciainabalada` sobre fundo azul-escuro |
| 2 | Citação da **min. Rosa Weber**, então presidente do STF: *"Estarmos reunidos neste Plenário três semanas após os ataques criminosos contra a democracia constitucional é a demonstração de que este Supremo Tribunal Federal e seus ministros jamais serão intimidados na missão precípua da guarda da Constituição. Lembraremos sempre do 8/1/2023 para que ele jamais se repita e para que todos saibam que o STF e sua atuação em defesa do estado democrático de direito são inabaláveis."* |
| 3 | Plenário íntegro — legenda **"dezembro de 2022"** |
| 4 | Plenário destruído, em preto e branco, com dois detalhes do mobiliário quebrado — legenda **"janeiro de 2023"** |
| 5 | Plenário restaurado — legenda **"fevereiro de 2023"** |
| 6 | Assinatura institucional do STF |

O folder é **material de comunicação, não fonte de evento**. Seu valor analítico é ser um artefato do próprio enquadramento institucional: a estrutura de três tempos (íntegro → destruído → restaurado) é a tese visual da campanha condensada em três páginas.

## Documentos correlatos nesta pasta

- `DOCUMENTARIO-catalogacao.md` — ficha do documentário. **Leia a advertência no topo:** é catalogação de metadados, **não** resumo de quem assistiu.
- `PAGINA-CAMPANHA-catalogacao.md` — inventário completo da página oficial da campanha, com todas as peças e URLs.

## Termos de uso declarados pelo STF

Da página da campanha: *"É permitida a publicação dos arquivos disponibilizados nesta página. Porém, são vedadas quaisquer alterações de conteúdo, sejam de texto, imagem, som ou mesmo de formato, salvo autorização expressa da Secretaria de Comunicação do STF."*

Reprodução de trechos em trabalho acadêmico, com atribuição, está coberta; **reedição ou alteração das peças, não**.
