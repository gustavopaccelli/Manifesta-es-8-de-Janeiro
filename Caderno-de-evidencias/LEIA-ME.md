# Caderno de Evidências — natureza e uso

## O que é esta pasta

Um **repositório de evidência verificada**, não um produto de análise e não um corpus de artigo.

Reúne os **49 registros do codebook que estão ancorados diretamente no Relatório Final da CPMI do 8 de Janeiro**, cada um com número de página e transcrição literal do trecho que o sustenta. Foi gerado em 12/08/2026 a partir de `process_tracing_8jan_eventos.json`, ao término da recodificação integral da camada $T_0$ sobre fonte primária.

## Por que existe separadamente

O projeto tem três tipos de material, e misturá-los gera confusão:

| Pasta | Natureza | Papel |
|:--|:--|:--|
| `Fontes/` | **Insumo** — documentos oficiais originais | O que foi lido |
| `Caderno-de-evidencias/` | **Evidência verificada** — trechos literais com página | O que os documentos dizem |
| Raiz do projeto | **Análise** — codebook, relatório, figuras | O que o pesquisador conclui |

A separação existe porque **a maior parte deste conteúdo não vai para o artigo**. Dos 49 registros, talvez uma dúzia seja citada. Os demais foram verificados mesmo assim, por três razões:

1. **Verificar é diferente de usar.** Um registro conferido e descartado é um registro sobre o qual se sabe algo. Um registro nunca conferido é um risco silencioso.
2. **A pesquisa continua depois do artigo.** Este material sustenta desdobramentos — capítulo, apresentação, réplica a parecerista — sem exigir nova ida ao PDF de 1.333 páginas.
3. **Auditabilidade.** Um parecerista que questione qualquer afirmação da cronologia encontra aqui a página e o texto literal, sem depender de o autor lembrar onde leu.

## Como está organizado

- **`caderno_CPMI_verbatim.md`** — leitura humana. Agrupado por fase do process tracing, com transcrição, status de verificação e, recolhido em `<details>`, o mecanismo causal atribuído. O mecanismo aparece separado de propósito: **é leitura do analista, não conteúdo da fonte.**
- **`caderno_CPMI_verbatim.csv`** — leitura por máquina, 8 colunas, para filtrar, cruzar ou reimportar.

## Como citar a partir daqui

A numeração impressa do relatório da CPMI **coincide com a paginação do PDF** em `Fontes/04_T+1_Resposta-institucional/`. Uma citação como *(CPMI, p. 679)* é verificável abrindo o PDF nessa página, sem conversão nem ambiguidade.

## Advertências

**Não confunda transcrição com achado.** O campo de trecho literal reproduz o que a CPMI afirma. O relatório da CPMI é peça de investigação parlamentar, com posição política própria e votos em separado. Que o documento afirme algo não é o mesmo que o fato estar estabelecido.

**Os mecanismos causais são atribuições do pesquisador.** Estão aqui apenas para vincular cada evidência à sua função no argumento. Nenhum deles é citação da fonte.

**Há problemas de proveniência conhecidos** (a lista completa está ao final). O mais grave deles — a cifra de "cerca de 4 mil pessoas" na Praça dos Três Poderes às 15h26, em PT-34 — foi **resolvido em 16/08/2026: o número foi retirado**. Não tinha lastro em fonte primária nem corroboração jornalística independente; na própria CPMI, "4 mil" refere-se ao pico do acampamento em 15/11/2022 (p. 532) e ao depoimento do gen. Augusto Heleno (p. 1324). Em seu lugar entrou uma faixa de 3.000 a 5.500 no conjunto mobilizado, sustentada por duas medições oficiais independentes. Dossiê em [`../docs/ESTIMATIVA-MULTIDAO-8JAN.md`](../docs/ESTIMATIVA-MULTIDAO-8JAN.md).

## O que ainda não está aqui

**A recodificação sobre a CPMI está encerrada.** Não resta nenhum registro que o relatório cubra e que siga apoiado em fonte secundária.

Os 27 registros restantes do codebook não vêm da CPMI porque a CPMI não é a fonte pertinente para eles:

- **Camada contextual** (PT-01 a PT-07): itens de enquadramento histórico apoiados na literatura teórica do projeto — Alonso, Nobre, Cesarino, Abranches, Avritzer. Não são fatos a verificar em documento, são leituras a discutir em referencial teórico.
- **Arco judicial** (PT-02A, PT-03A a PT-03E, PT-05A, PT-06A a PT-06C): têm fonte primária própria — os acórdãos do STF e do TRF-4 em `Fontes/01_Arco-judicial_2017-2021/`.
- **Resposta institucional tardia** (PT-53, PT-56 a PT-61): posteriores ao relatório da CPMI, de out/2023; a fonte é o STF.
- **PT-38** (vandalismo): o detalhamento por peça exige o laudo pericial do Instituto de Criminalística da PF, não obtido.
- **PT-62**: inferência analítica declarada, não fato a verificar.

## Ressalvas de proveniência — três resolvidas, uma esclarecida

Todas sinalizadas no campo de status do codebook. Revisão de 16/08/2026: busca exaustiva no corpus inteiro (não só as seções já checadas) resolveu três das quatro.

1. ~~**PT-34** — "cerca de 4 mil pessoas" na Praça às 15h26~~ ✅ **RESOLVIDA em 16/08/2026: cifra retirada** (detalhado acima).
2. ~~**PT-12** — "mais de 100 acampamentos" no país~~ ✅ **RESOLVIDA em 16/08/2026: cifra retirada, mesmo padrão do PT-34.** Sem lastro na CPMI nem no Cappelli; substituída pela caracterização geográfica ancorada "em todos os Estados" (CPMI, p. 510).
3. ~~**PT-17** — a saída de Bolsonaro do país em 30/12~~ ✅ **RESOLVIDA em 16/08/2026: achado.** CPMI, p. 612, confirma a partida para os EUA em 30/12/2022, no texto analítico da própria comissão.
4. **PT-52** — **esclarecida, não substituída.** "~1.200 em 40 ônibus" (imprensa, atribuído ao então ministro Flávio Dino) e "2.151 presas" (CPMI, p. 688) medem universos diferentes — triagem progressiva ao longo da manhã x total de prisões ao fim da operação. Mantidas as duas cifras lado a lado; **a escolha de qual liderar no texto é decisão do pesquisador**.
