# Registro de estado de leitura do corpus

> **Peça gerada por `scripts/gerar_registro_leitura.py`. Não edite à mão.** É a resposta a um defeito com data: em 21/10/2026 eu relatei seis verbetes como *"lidos-a-ler"* e **os seis estavam lidos**, porque copiei uma lista de 30/09 do documento que **pedia** a leitura em vez de abrir o que a **registrava**. O estado de leitura vivia em prosa espalhada por sete documentos, e nada no ciclo conferia.

**70 peças no corpus. 45 com estado MEDIDO, 25 com estado DECLARADO.**

## 1. Como o estado é estabelecido — e a maior parte não é declarada

| Origem | Quantas | Como |
|:--|--:|:--|
| **MEDIDO** | 45 | a peça **ancora registro** com `fonte_pagina`, e o passo 9 do ciclo confere a transcrição contra a folha do PDF. Leitura parcial **demonstrável**, não afirmada |
| **DECLARADO** | 25 | a peça **não ancora registro**: informa o desenho sem sustentar dado. O estado vive em `data/estado_de_leitura.json`, que é dado e não prosa |

| Estado | Peças |
|:--|--:|
| `ILEGIVEL` | 1 |
| `LIDO_INTEGRAL` | 13 |
| `LIDO_PARCIAL` | 54 |
| `NAO_LIDO` | 2 |

**Vocabulário.** `LIDO_INTEGRAL` · `LIDO_PARCIAL`, com o que foi lido · `NAO_LIDO` · `ILEGIVEL`, no corpus e sem camada de texto · `NAO_DECLARADO`, quando **nenhum documento do repositório registra o estado** — é confissão, não suposição.

## 2. As três guardas, e a segunda é a que faltava

| | O que confere | O que pega |
|:--|:--|:--|
| **G1** cobertura | toda peça do manifesto está medida ou declarada, e toda declaração existe no manifesto | fonte nova entrando sem estado; declaração que sobreviveu à peça |
| **G2** coerência de prosa | **nenhum documento de `docs/` afirma não-leitura de peça cujo estado é de leitura** | exatamente o erro de 21/10/2026. Menção histórica datada fica livre pela marca de errata, pelo mesmo critério da checagem 7 do ciclo |
| **G3** procedência da leitura | peça declarada lida diz **onde** a leitura está registrada, e o arquivo existe | leitura afirmada sem lugar onde conferi-la |

**G2 hoje: 0 incoerência(s).**

## 3. O registro, peça por peça

| Peça | Folhas | Estado | Origem | O que foi lido | Onde está registrado |
|:--|--:|:--|:--|:--|:--|
| `STF_ADC-43-44-54_Acordao_2019-11-07.pdf` | 489 | **LIDO_PARCIAL** | MEDIDO | ancora 2 registro(s) com 8 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `STF_ADC-43-MC_Acordao_2016-10-05.pdf` | 250 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 5 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `STF_HC-152752_Acordao_2018-04-04.pdf` | 464 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 7 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `STF_HC-164493_Acordao_Suspeicao-Moro_2021-03-23.pdf` | 441 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 2 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `STF_HC-193726-AgR-segundo_Acordao_2021-06-23.pdf` | 182 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 2 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `STF_HC-193726-AgR_Acordao_2021-04-15.pdf` | 264 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 3 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `TRF4_Revista-97_Acordao-ACr-5046512-94_2018-01-24.pdf` | 657 | **LIDO_PARCIAL** | MEDIDO | ancora 2 registro(s) com 5 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `TSE_RCand-0600903-50_Acordao_2018-09-01.html` | 0 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 3 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `DODF-001_Decreto-01-01-2023_Nomeacao-Torres-SSPDF_2023-01-02.pdf` | 66 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 8 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `DODF-003_Decreto-03-01-2023_Ajudancia-de-Ordens-SSPDF_2023-01-04.pdf` | 66 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 8 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `PGR_Denuncia_PET-12100_Nucleo-1_2025-02-18.pdf` | 272 | **LIDO_PARCIAL** | MEDIDO | ancora 3 registro(s) com 8 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `GDF-SSP_Relatorio-Interventor-Federal_Cappelli_2023-01-27.pdf` | 62 | **LIDO_PARCIAL** | MEDIDO | ancora 6 registro(s) com 27 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `CPMI-8-de-Janeiro_Relatorio-Final_2023-10-17.pdf` | 1333 | **LIDO_PARCIAL** | MEDIDO | ancora 53 registro(s) com 103 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `STF_AP-2668-QO_Acordao_2025-05-14.pdf` | 50 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 1 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `STF_AP-2668_Acordao_Condenacao_2025-09-11.pdf` | 1991 | **LIDO_PARCIAL** | MEDIDO | ancora 5 registro(s) com 9 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `STF_EP-169_Decisao-Prisao-Domiciliar_2026-03-24.pdf` | 40 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 7 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `STF_EP-169_Decisao-Transferencia-Papuda_2026-01-15.pdf` | 36 | **LIDO_PARCIAL** | MEDIDO | ancora 2 registro(s) com 11 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `STF_Pet-14129_Decisao-Prisao-Preventiva_2025-11-22.pdf` | 17 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 8 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `BEACH-PEDERSEN_Process-Tracing-Methods_Michigan-2013.pdf` | 208 | **LIDO_PARCIAL** | DECLARADO | capítulos 1 a 3 (p. 1-44 impressas) e Apêndice A (p. 163-170); offset impressa = PDF − 8 | docs/referencial/03_ADAPTACAO-METODOLOGICA.md |
| `COLLIER_Understanding-process-tracing_PS-44-4_2011.pdf` | 8 | **LIDO_INTEGRAL** | DECLARADO | integral, 8 folhas; offset impressa = PDF + 822 | docs/analise/09_CONCEITO-MECANISMO.md |
| `GONZALEZ-BAILON-BORGE-HOLTHOEFER-RIVERO-MORENO_Dynamics-of-protest-recruitment-through-an-online-network_Scientific-Reports-1_2011.pdf` | 7 | **LIDO_PARCIAL** | DECLARADO | achados centrais, na ficha 13: os participantes iniciais não têm posição topológica típica; só os disseminadores de cascata são mais centrais | docs/analise/08_BIBLIOGRAFIA-METODOLOGICA.md |
| `Livro_Process tracing.pdf` | 104 | **LIDO_PARCIAL** | DECLARADO | trechos conceituais com página — condição necessária e suficiente, p. 92 e 97 | docs/analise/09_CONCEITO-MECANISMO.md |
| `MAYNTZ_Mechanisms-in-the-analysis-of-social-macro-phenomena_PSS-34-2_2004.pdf` | 23 | **LIDO_INTEGRAL** | DECLARADO | integral, 23 folhas | docs/analise/09_CONCEITO-MECANISMO.md |
| `McADAM-TARROW-TILLY_Dynamics-of-Contention_Cambridge-2001.pdf` | 411 | **LIDO_PARCIAL** | DECLARADO | trechos definidores citados por folha impressa: brokerage 26, certification 145 e 158, mobilizing structures 45, threshold 307, scale shift 332, difusão 333; offset impressa = PDF − 24 | docs/referencial/01_QUADRO-TEORICO-METODOLOGICO.md |
| `SNOW-DELLA-PORTA-KLANDERMANS-McADAM_Wiley-Blackwell-Encyclopedia-of-Social-and-Political-Movements_2013.pdf` | 1638 | **LIDO_PARCIAL** | DECLARADO | ONZE verbetes lidos integrais: Mechanisms (Tarrow) · Protest cycles and waves · Political opportunity · Repertoires of contention · Policing protest (della Porta e Reiter) · Diffusion and scale shift (Soule) · Demobilization (Fillieule) · Discursive opportunity structure (McCammon) · Multiorganizational fields (Klandermans) · Resource mobilization theory (Edwards e Gillham) · Critical mass theory (Oliver). OS NOMES DOS ONZE VERBETES ESTÃO EM `termos`, e a razão é uma prova negativa que falhou em 21/10/2026: a peça do corpus é o volume, mas a unidade de leitura — e a unidade sobre a qual eu errei — é o VERBETE. Guarda que vigia só o nome do continente não pega afirmação sobre o conteúdo | docs/analise/10_VERBETES-ENCICLOPEDIA.md |
| `SNOW-VLIEGENTHART-KETELAARS_The-framing-perspective-on-social-movements_Wiley-Blackwell-Companion-2ed_2019.pdf` | 20 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 6 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `TARROW_O-poder-em-movimento_Vozes-2009.pdf` | 162 | **ILEGIVEL** | DECLARADO | no corpus e SEM camada de texto: digitalização em duas páginas por folha. Não se faz OCR porque a paginação resultante erraria o que uma ficha precisa ancorar | docs/referencial/01_QUADRO-TEORICO-METODOLOGICO.md |
| `process-tracing-research-designs-a-practical-guide.pdf` | 5 | **LIDO_INTEGRAL** | DECLARADO | integral, 5 folhas; offset impressa = PDF + 841. Lida em 21/10/2026 | docs/referencial/01_QUADRO-TEORICO-METODOLOGICO.md |
| `Doxa-IESP-UERJ_Manchetometro_Atos-golpistas-8-jan_2023-03.pdf` | 16 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 7 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `NetLab-UFRJ_Anuncios-golpistas-Meta-Ads_2023-02-07.md` | 0 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 0 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `SciELO-Preprints_Drummond-Manginelli_Editoriais-8-jan_2023-10-09.pdf` | 24 | **NAO_LIDO** | DECLARADO | catalogada no LEIA-ME do eixo 08 como OBJETO DE ANÁLISE, não como fonte de dado. Nenhum documento registra leitura | — |
| `Estadao_2021-03-08_Eduardo-Bolsonaro-nega-atuacao-Capitolio.md` | 0 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 7 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `STF_Democracia-Inabalada_Ebook_28x28cm.pdf` | 210 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 1 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `STF_Democracia-Inabalada_Folder.pdf` | 6 | **NAO_LIDO** | DECLARADO | folder de 6 páginas e 37,4 MB — o pior índice de bytes por página do corpus (item 46.5 da agenda). O conteúdo lido do mesmo título está no Ebook, que ancora registro | — |
| `STF_Gabinete-Moraes_Balanco-8-de-Janeiro_2026-04-29.pdf` | 15 | **LIDO_PARCIAL** | MEDIDO | ancora 3 registro(s) com 15 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `ALONSO_Repertorio-segundo-Charles-Tilly_Sociologia-e-Antropologia-2-3_2012.pdf` | 21 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 28 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `ALONSO_Treze-a-politica-de-rua-de-Lula-a-Dilma_Companhia-das-Letras_2023.pdf` | 309 | **LIDO_PARCIAL** | MEDIDO | ancora 4 registro(s) com 40 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `KUNRATH-SILVA_Apropriacao-conservadora-do-ciclo-de-protestos_Lusotopie-17-1_2018.pdf` | 20 | **LIDO_PARCIAL** | MEDIDO | ancora 2 registro(s) com 34 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `KUNRATH-SILVA_Ciclo-de-protestos-de-2013-objeto-de-disputa_Desigualdade-e-Diversidade-23_2023.pdf` | 34 | **LIDO_PARCIAL** | MEDIDO | ancora 4 registro(s) com 40 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `PINTO_Trajetoria-discursiva-das-manifestacoes-de-rua_Lua-Nova-100_2017.pdf` | 37 | **LIDO_PARCIAL** | MEDIDO | ancora 2 registro(s) com 34 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `TATAGIBA-GALVAO_Protestos-no-Brasil-em-tempos-de-crise_Opiniao-Publica-25-1_2019.pdf` | 34 | **LIDO_PARCIAL** | MEDIDO | ancora 3 registro(s) com 39 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `TATAGIBA_Ciclos-de-protestos-e-democracia_Politica-e-Sociedade-28_2014.pdf` | 28 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 16 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `ARAUJO-SALES_Atuacao-politica-das-Forcas-Armadas-e-bolsonarismo_Cadernos-do-Tempo-Presente-13-1_2022.pdf` | 17 | **LIDO_PARCIAL** | MEDIDO | ancora 5 registro(s) com 42 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `BASTOS-RECUERO_The-insurrectionist-playbook_Social-Media-and-Society-out-dez_2023.pdf` | 16 | **LIDO_INTEGRAL** | DECLARADO | lida em 09-10/10/2026. Produziu um LIMITE e não uma âncora: não corrobora o Sri Lanka | docs/analise/13_LITERATURA-BOLSONARISMO.md |
| `CARVALHO-TATAGIBA_Quando-o-conflito-eleitoral-extravasa-para-as-ruas_Lua-Nova-124_2025.pdf` | 46 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 2 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `CESARINO_Bolsonarismo-sem-Bolsonaro-publicos-antiestruturais_Revista-do-IEB-82_2022.pdf` | 27 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 14 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `CESARINO_Identidade-e-representacao-no-bolsonarismo_Revista-de-Antropologia-62-3_2019.pdf` | 28 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 14 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `CHAGAS-CARREIRO_Far-right-digital-activism-in-polarized-contexts_Media-and-Communication-10-4_2022.pdf` | 14 | **LIDO_INTEGRAL** | DECLARADO | lida em 09-10/10/2026; não ancora registro | docs/analise/13_LITERATURA-BOLSONARISMO.md |
| `FARIAS-CASAROES-MAGALHAES_Radical-right-populism-and-the-politics-of-cruelty_Global-Studies-Quarterly-2_2022.pdf` | 13 | **LIDO_INTEGRAL** | DECLARADO | lida em 09-10/10/2026; não ancora registro | docs/analise/13_LITERATURA-BOLSONARISMO.md |
| `FERNANDES-SILVA_Dinamicas-do-controle-a-acao-coletiva-policiamento_Mediacoes-26-3_2021.pdf` | 17 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 28 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `GOHN_Ciclos-de-protestos-no-Brasil-1970-2019_Mundos-Plurales-6-1_2019.pdf` | 27 | **LIDO_PARCIAL** | DECLARADO | lida em parte em 08/10/2026, para o mapa bibliográfico | docs/analise/13_LITERATURA-BOLSONARISMO.md |
| `KAYSEL-BIANCHI_Bolsonarismo-como-coalizao-discursiva-de-extrema-direita_Caderno-CRH-38_2025.pdf` | 14 | **LIDO_INTEGRAL** | DECLARADO | lida em 09-10/10/2026. Não ancora registro; recusa 'populismo' por amplo e normativo e propõe conceito espacial e relacional | docs/analise/13_LITERATURA-BOLSONARISMO.md |
| `MENDONCA-DOMINGUES_Protestos-contemporaneos-e-a-crise-da-democracia_RBCP-37_2021.pdf` | 36 | **LIDO_INTEGRAL** | DECLARADO | lida em 09-10/10/2026; não ancora registro | docs/analise/13_LITERATURA-BOLSONARISMO.md |
| `MENDONCA-FREITAS_Fake-news-e-o-repertorio-contemporaneo-de-acao-politica_Dados-66-2_2022.pdf` | 33 | **LIDO_INTEGRAL** | DECLARADO | lida em 09-10/10/2026; não ancora registro | docs/analise/13_LITERATURA-BOLSONARISMO.md |
| `MESSENBERG_A-direita-que-saiu-do-armario_Sociedade-e-Estado-32-3_2017.pdf` | 27 | **LIDO_INTEGRAL** | DECLARADO | lida em 09-10/10/2026; não ancora registro | docs/analise/13_LITERATURA-BOLSONARISMO.md |
| `NUNES_A-palavra-e-a-coisa-bolsonarismo-como-infraestrutura_Lua-Nova-122_2024.pdf` | 20 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 7 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `ROCHA_Imposto-e-roubo-contrapublico-ultraliberal_Dados-62-3_2019.pdf` | 42 | **LIDO_INTEGRAL** | DECLARADO | lida em 09-10/10/2026; não ancora registro | docs/analise/13_LITERATURA-BOLSONARISMO.md |
| `SANTOS-TANSCHEIT_Quando-velhos-atores-saem-de-cena-nova-direita_Colombia-Internacional-99_2019.pdf` | 37 | **LIDO_INTEGRAL** | DECLARADO | lida em 09-10/10/2026; não ancora registro | docs/analise/13_LITERATURA-BOLSONARISMO.md |
| `TATAGIBA_Entre-as-ruas-e-as-instituicoes-impeachment_Lusotopie-17-1_2018.pdf` | 20 | **LIDO_INTEGRAL** | DECLARADO | lida em 09-10/10/2026; não ancora registro. A camada de texto foi diagnosticada como cifrada por mim, e o diagnóstico estava errado — ver §8.6 do documento 13 | docs/analise/13_LITERATURA-BOLSONARISMO.md |
| `VON-BULOW-ABERS_Denialism-and-populism-two-sides-of-a-coin_Government-and-Opposition-59_2024.pdf` | 19 | **LIDO_PARCIAL** | MEDIDO | ancora 2 registro(s) com 15 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `ABERS_Ativismo-institucional-criatividade-e-luta-na-burocracia_Editora-UnB_2021.pdf` | 359 | **LIDO_PARCIAL** | DECLARADO | lido em parte em 08/10/2026; offset medido impressa = PDF − 2 | docs/analise/14_LIVROS-BRASILEIROS.md |
| `FARIA-MARQUES_Giros-a-direita-volume-integral_SertaoCult_2020.pdf` | 258 | **LIDO_PARCIAL** | DECLARADO | capítulo de Marques, p. 241-255, identificado na leitura de 08/10/2026. O volume substituiu os oito offprints, e nenhum registro aponta para ele | docs/analise/14_LIVROS-BRASILEIROS.md |
| `LAVALLE-CARLOS-DOWBOR-SZWAKO_Movimentos-sociais-e-institucionalizacao_EdUERJ_2018.pdf` | 414 | **LIDO_PARCIAL** | DECLARADO | lido em parte em 08/10/2026; offset medido impressa = PDF − 2. Traz a crítica ao marco teórico declarado do projeto | docs/analise/14_LIVROS-BRASILEIROS.md |
| `MADEIRA-MARONA-DEL-RIO_Democracia-e-justica-na-America-Latina_EdUERJ_2022.pdf` | 427 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 7 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `SINGER-ARAUJO-RUGITSKY_O-Brasil-no-inferno-global_FFLCH-USP_2022.pdf` | 374 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 28 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `CASTANEDA-JENKS_January-6th-and-de-democratization_Social-Sciences-12-4_2023.pdf` | 15 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 7 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `CHEN-LUKITO-KOO_Comparing-the-StopTheSteal-movement-across-platforms_Social-Media-and-Society-9-3_2023.pdf` | 13 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 7 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `PMDB-FUG_Uma-Ponte-para-o-Futuro_2015-10-29.pdf` | 19 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 5 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `TSE-noticias_2014-11-04_Auditoria-PSDB-Eleicoes-2014.md` | 0 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 2 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |
| `TSE-noticias_2015-11-05_PSDB-nao-encontra-fraude.md` | 0 | **LIDO_PARCIAL** | MEDIDO | ancora 1 registro(s) com 2 folha(s) citada(s); o passo 9 do ciclo confere a transcrição contra a folha | o próprio codebook (`fonte_pagina`) |

## 4. Peças que os documentos discutem e que NÃO estão no corpus

**A afirmação de não-leitura sobre estas é legítima**, e é por estarem declaradas aqui que a guarda G2 não as confunde com peça lida.

| Peça | Situação |
|:--|:--|
| **BENFORD e SNOW (2000)** | PENDENTE e closed na camada A, sem depósito em repositório algum. Era o que `marco_teorico` declarava até 21/10/2026; hoje é referência de genealogia |
| **SNOW et al. (1986)** | a fonte dos quatro tipos de alinhamento de quadros, atribuídos pelo capítulo de 2019. Citá-los como de 1986 seria asserção sem leitura |
| **TILLY e TARROW (2007)** | o vocabulário que PT-03D atribuía até 21/10/2026. Não está no corpus |
| **BEACH e PEDERSEN (2016)** | a 2. ed.; o corpus tem a de 2013 |
| **WALDNER (2015)** | editor barrado; ficha 9, metadado só |
| **TARROW, verbete Mechanisms .pub2 (2022)** | revisão que não está no volume de 2013 do corpus |

