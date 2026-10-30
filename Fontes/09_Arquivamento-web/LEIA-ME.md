# 09 — Arquivamento web

Eixo aberto em **16/08/2026**. Guarda **matéria e notícia arquivadas que ancoram registro do codebook** — a cópia local existe contra *link rot*, que é o risco que faz uma âncora de URL apodrecer sem avisar.

A distinção que organiza o material jornalístico do projeto está no `LEIA-ME.md` da pasta `08`: **matéria arquivada que ancora registro é fonte de dado e vem para cá; literatura sobre como a imprensa enquadrou o evento é objeto de análise e fica na 08.**

---

## A licença destas peças — ✅ DECIDIDO EM 30/10/2026

**Decisão: manter as páginas arquivadas, com a razão escrita.** É a saída (a) das três que o item 89.7 da agenda deixou precificadas, e esta seção é a razão que faltava — a decisão de 21/10/2026, que tirou os PDFs do versionamento, **foi sobre PDF e nunca examinou as peças não-PDF deste eixo**.

### O que cada arquivo declara sobre si — lido em 30/10/2026

| Origem | Arquivos | O que o arquivo declara |
|:--|--:|:--|
| **Agência Brasil** (EBC) | **6** `.html` | **"Todos os direitos reservados"**, nos seis |
| **Portal de notícias do STF** | **4** `.html` | **nada declarado** — e nenhuma menção a Creative Commons |
| **Estadão** | **1** `.md` | é **transcrição**, não cópia da página: o HTML não entrou, por decisão do item 77 |

### A razão de manter

**Três coisas sustentam a decisão, e a terceira é o limite dela.**

1. **O conteúdo é comunicação institucional de órgão público.** A **EBC é empresa pública federal** e o **STF é tribunal**; o que está arquivado é o noticiário oficial de cada um sobre atos processuais próprios. É material produzido para difusão pública, e a cópia local não compete com nenhuma exploração comercial dele.
2. **O precedente do projeto é coerente, e a distinção que ele usou é esta.** No item 77 o HTML do **Estadão** NÃO entrou — *"versionar o HTML seria redistribuição de jornalismo protegido"* —, e entrou **só a transcrição**. A diferença aplicada foi **setor público contra jornal comercial**, e ela se sustenta: a EBC é empresa pública, o Estadão não.
3. **E o preço fica escrito, porque ele é real:** são **dez páginas web num remoto público**, seis delas **declarando direitos reservados no próprio arquivo**. A decisão é de manter sabendo disso, não por não ter lido. **Se os titulares pedirem a retirada, retira-se** — e nada do aparato se perde: o que ancora registro é a transcrição literal em `fonte_trecho`, que já está no codebook com folha ou seção declarada.

> **A ordem foi errada uma vez, e isto fica registrado.** As três páginas de 25/10/2026 entraram no remoto **antes** de a licença ser lida, e a regra da casa é o inverso — a licença se lê dentro do arquivo, antes de empurrar. O item 89.7 registra a inversão.

---

## Cinco destes arquivos ancoram registro; seis não — e o nome não diz isso

**Medido em 30/10/2026:** dos **11** arquivos rastreados, **5 estão em `Fontes/MANIFESTO-CORPUS.csv`** e **6 estão fora**.

| | Arquivos | Vigilância |
|:--|:--|:--|
| **no manifesto** | Agência Brasil de **PT-06B** e **PT-38**, STF de **PT-56** e **PT-06B**, e a transcrição do Estadão de **PT-08** | SHA-256 no manifesto, e a **checagem 8** do ciclo acusa byte mudado, peça removida e peça intrusa |
| **fora do manifesto** | Agência Brasil de **PT-03A**, **PT-03D** e duas de **PT-58**; STF de **PT-59** e **PT-60** | **nenhuma** |

**A regra que produz isso é declarada e deliberada:** `ancoras_nao_pdf()`, em `scripts/gerar_manifesto_corpus.py`, recolhe peça não-PDF a partir de `fonte_local` — *"porque é o que define âncora"* —, e nasceu em 16/10/2026 justamente para fechar um buraco deste tipo. **Para peça que não ancora registro, o manifesto não tem o que dizer.**

> **O que o sufixo do nome significa, e esta é a convenção — declarada aqui em 30/10/2026 para não ficar sendo inferida do nome do arquivo.** O `_PT-XX` do fim do nome diz **para qual registro a página foi coletada**, e **não** que o registro a declare como âncora. **A página arquivada é seguro contra `link rot`, não a âncora.** Quem lê o nome como declaração de âncora lê o arquivo dizendo algo que o codebook não diz.

Os **seis arquivos de fora** são de **cinco registros**, e quatro deles estão ancorados em PDF: **PT-03A** no acórdão do TRF-4 (f. 348 e 395), **PT-58** em duas decisões do STF, **PT-59** e **PT-60** em decisões do EP 169.

### A exceção, e ela é a mais interessante do eixo: PT-03D

**`AgenciaBrasil_2018-04-07_Prisao-Curitiba_PT-03D.html` é a cópia arquivada da fonte do único registro do codebook SEM ARQUIVO VINCULADO.** Medido em 30/10/2026: PT-03D tem `fonte_local` **vazio** e `fonte_pagina` **vazio** — é o registro que o painel declara como exceção, e é classe `Confirmado`, não fonte primária. **A cópia da fonte dele está nesta pasta, versionada, e o registro não a cita.**

**Citá-la em `fonte_local` faria três coisas de uma vez:** daria arquivo ao único registro sem arquivo, levaria a ancoragem documental de 86 para 87 de 87, e traria o arquivo para dentro do manifesto e da vigilância de SHA-256 — **pela regra que já existe, sem exceção nenhuma**.

> **Não foi executado, e a razão é a regra da casa:** acrescentar âncora é **codificação** — exige ler a página, decidir o que ela sustenta e transcrever literal —, e codificação é decisão do pesquisador. O precedente para a forma existe e é desta mesma pasta: **PT-06B, PT-38 e PT-56** ancoram página web arquivada, e **PT-08** ancora transcrição de matéria.

**As saídas que isto deixa, e as três são dele:** **citar** as páginas em `fonte_local`, uma a uma — o caso de PT-03D é o que mais rende; **destrackear** as seis, mantendo a cópia local e tirando do remoto o que registro nenhum cita; ou **manter como está**, que é seguro declarado e fora de vigilância.

---

## Acervo

### Agência Brasil (EBC) — 6 arquivos

| Arquivo | Para qual registro | No manifesto |
|:--|:--|:--|
| `AgenciaBrasil_2017-07-12_Condenacao-Lula_PT-03A.html` | PT-03A | não |
| `AgenciaBrasil_2018-04-07_Prisao-Curitiba_PT-03D.html` | PT-03D | não |
| `AgenciaBrasil_2021-06_Moro-parcial-triplex_PT-06B.html` | **PT-06B** | **sim** |
| `AgenciaBrasil_2024-09_Obras-recuperadas_PT-38.html` | **PT-38** | **sim** |
| `AgenciaBrasil_2025-11-22_Prisao-preventiva_PT-58.html` | PT-58 | não |
| `AgenciaBrasil_2025-11-25_Cumprimento-pena_PT-58.html` | PT-58 | não |

### Portal do STF — 4 arquivos

| Arquivo | Para qual registro | No manifesto |
|:--|:--|:--|
| `STF-noticias_Penas-16-a-27-anos_PT-56.html` | **PT-56** | **sim** |
| `STF-noticias_Prisao-domiciliar_PT-60.html` | PT-60 | não |
| `STF-noticias_Suspeicao-Moro_PT-06B.html` | **PT-06B** | **sim** |
| `STF-noticias_Transferencia-Papuda_PT-59.html` | PT-59 | não |

### Estadão — 1 arquivo, e é transcrição

`Estadao_2021-03-08_Eduardo-Bolsonaro-nega-atuacao-Capitolio.md` — ancora **PT-08**, e está no manifesto. **O HTML não entrou**, por decisão do item 77: jornalismo comercial protegido não se redistribui, e a transcrição com atribuição basta para a âncora.

---

*A licença da obra do pesquisador — que não alcança estas peças — está em `../../LICENSE`. O raciocínio de distribuição do corpus está em `../../LICENCA-E-DISTRIBUICAO.md`, e a decisão desta pasta no item 107 de `../../docs/PENDENCIAS-ANALITICAS.md`.*
