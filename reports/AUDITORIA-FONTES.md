# Auditoria de fontes — vínculo registro ↔ documento ↔ página

Gerado por `scripts/gerar_auditoria.py` em **25/09/2026**. Não editar à mão: rode o script de novo depois de cada rodada de coleta.

Esta peça responde a uma pergunta única e a responde para os 82 registros: **onde está, exatamente, o documento que sustenta esta afirmação, e em que página?** É o que um parecerista cobra quando desconfia de um ponto da cronologia, e é o que separa uma cronologia auditável de uma cronologia asserida.

## Painel

| Indicador | Valor |
|:--|--:|
| Sub-eventos no codebook | 82 |
| Com documento local vinculado | **74** |
| Com página atribuída ao documento | 68 |
| Sem âncora local, por natureza do registro | 7 |
| Sem âncora local, dependentes de coleta | **1** |
| Referências quebradas | 0 |
| Arquivos do corpus sem procedência declarada | 0 |

**Distribuição por classe de verificação**

| Classe | N |
|:--|--:|
| Confirmado em fonte primária | 60 |
| Confirmado | 14 |
| Contextual | 7 |
| Inferência do analista | 1 |

## O que esta auditoria alterou

Nenhum dado analítico foi tocado — nenhum fato, mecanismo causal ou enquadramento mudou. As alterações são todas de **vínculo** e de **status**, e cada uma está registrada no campo `nota_auditoria` do próprio registro.

| Registro | Alteração |
|:--|:--|
| **PT-02A** | PT-02A — busca de melhor esforço em 16/08/2026 (Tier 2), sem mudança de status. Localizado um mirror em luisrobertobarroso.com.br — mas é APENAS o voto do min. Barroso (28 p.), não o acórdão completo do HC 126.292 com todos os votos. Não resolve a lacuna declarada ('o acórdão do próprio HC 126.292 não foi baixado'). Arquivo NÃO baixado para Fontes/ — decisão sobre incorporá-lo como material suplementar fica pendente para o pesquisador (ver lista de pendências). |
| **PT-03A** | PT-03A — busca de melhor esforço em 16/08/2026 (Tier 2), sem mudança de status. Localizados apenas comentários sobre a sentença (ex.: artigo de 6 p. de Mário Montanha Teixeira Filho), não o inteiro teor. O e-proc da JFPR não foi consultado diretamente — provavelmente exige login. Permanece baixa prioridade: o dispositivo já está transcrito no acórdão do TRF-4, p. 395. |
| **PT-03E** | PT-03E RESOLVIDO em 16/08/2026 — última peça do arco judicial. O inteiro teor foi obtido SEM captcha, por rota pública distinta do buscador de jurisprudência: o endpoint de documento da Consulta Unificada PJe. A API do buscador (sjur-pesquisa-api) exige verificação antirrobô e responde 'Falha na verificação antirrobô' sem token; nenhuma tentativa de contorná-la foi feita. DUAS CORREÇÕES DE DOCUMENTAÇÃO: o captcha do TSE é hCAPTCHA e não reCAPTCHA, como o projeto vinha registrando; e o acórdão é servido em HTML, não em PDF. ACHADO SUBSTANTIVO: a Súmula 41/TSE, invocada na ementa, mostra que o efeito eleitoral da condenação opera por automatismo — a Justiça Eleitoral se declara incompetente para rever o mérito —, o que explica por que as anulações posteriores do STF (PT-06A e PT-06B) não puderam desfazer a exclusão de 2018. |
| **PT-06B** | vínculo corrigido em 16/08/2026 — O Plenário confirmou a suspeição em 23/06/2021 no segundo AgR do HC 193.726 (7x4); o registro cita as duas decisões mas só apontava a primeira. |
| **PT-08** | vínculo corrigido em 16/08/2026 — O achado do Sri Lanka como precedente invocado está na CPMI p. 614 e é citado na tabela do relatório, mas fonte_local estava vazio. |
| **PT-12** | PT-12 RESOLVIDO em 16/08/2026, mesmo padrão do PT-34. Cifra de 'mais de 100 acampamentos' retirada — busca exaustiva em todo o PDF da CPMI e no Cappelli não a localizou; provinha de retrospectiva da Agência Brasil sem órgão nomeado. Substituída pela caracterização geográfica que a CPMI sustenta com página: 'em todos os Estados' (p. 510). |
| **PT-13** | vínculo corrigido em 16/08/2026 — Denúncia da PGR como peça integral, corroborada pela CPMI p. 230 e 566. |
| **PT-15** | ACRESCENTADO EM 25/09/2026: a p. 274, que o status_verificacao já nomeava, entrou no fonte_pagina. Divergência achada por scripts/varrer_fonte_pagina.py. |
| **PT-17** | PT-17 RESOLVIDO em 16/08/2026. Busca exaustiva em todo o PDF da CPMI (985 páginas além da seção já checada) localizou a confirmação da data de saída de Bolsonaro para os EUA em p. 612, no texto analítico da comissão sobre a 'estratégia do caos'. Reclassificado de 'A verificar' para 'Confirmado em fonte primária'. |
| **PT-18** | vínculo corrigido em 16/08/2026 — CPMI p. 646 e 711; corroboração e agravamento em Cappelli, conclusões D e H. |
| **PT-21** | Acrescentada em 16/08/2026 a contagem de transporte da ANTT difundida pela Abin (105 ônibus, ~3.900 passageiros), que estava ausente do codebook e sustenta a faixa de magnitude de PT-34. |
| **PT-27** | vínculo corrigido em 16/08/2026 — CPMI p. 651 cita textualmente o relatório do interventor, hoje disponível em local. |
| **PT-28** | vínculo corrigido em 16/08/2026 — fonte_trecho cita 'Relatório Final da CPMI, p. 657' e o texto foi localizado nessa página, mas fonte_local apontava para o acórdão da AP 2668. Erro anterior a esta rodada, corrigido em 16/08/2026. ANCORAS ACRESCENTADAS EM 25/09/2026: o registro citava por extenso o Relatório do Interventor Federal (conclusão G, p. 57) e o acórdão da AP 2668 (p. 495 e 497) sem vincular nenhum dos dois. As três páginas foram lidas antes da correção. O vínculo da AP 2668 sumira na própria correção de 16/08/2026, que trocou o arquivo errado pelo certo em vez de somar os dois. Achado por scripts/varrer_fonte_pagina.py. |
| **PT-34** | PT-34 RESOLVIDO em 16/08/2026, após busca em veículos de escala nacional. Retirada a cifra pontual de 'cerca de 4 mil pessoas na Praça às 15h26': sem lastro primário e sem corroboração independente — fonte única (Agência Brasil, jan/2024, 'policiais' sem órgão nomeado), ausente das cronologias contemporâneas, e aplicada a referente diverso pela Wikipédia. Substituída por faixa de 3.000 a 5.500 no conjunto mobilizado, ancorada em duas medições oficiais independentes (ANTT/Abin: 105 ônibus e ~3.900 passageiros; SSP/DF: 3.000 de público às 9h) mais a caracterização da CPMI ('poucos milhares'). Ver o dossiê em ESTIMATIVA-MULTIDAO-8JAN.md. |
| **PT-38** | PT-38, 16/08/2026: (a) repontado para a cópia consolidada do livro em 10_Democracia-Inabalada/, após a remoção da duplicata byte-idêntica que estava em 03_T0_8-de-janeiro/; (b) acrescentada a valoração do dano como série datada. O valor de R$ 11,4 mi, que vinha da sinopse do documentário, NÃO foi adotado como cifra final — foi superado pelo levantamento de ~R$ 12 mi. Nenhum documento primário do corpus carrega esses números; a busca no livro, no balanço e na CPMI foi exaustiva e negativa. |
| **PT-39** | vínculo corrigido em 16/08/2026 — CPMI p. 677 mais o acréscimo da AP 2668 p. 496 sobre o silêncio no grupo Difusão. |
| **PT-50A** | PT-50A CRIADO em 16/08/2026, resolvendo o último arquivo órfão do corpus. O relatório do Manchetômetro estava em Fontes/07_NetLab-UFRJ/ desde a auditoria sem vincular-se a registro nenhum. Decidido que VIRA REGISTRO, e não contexto declarado, por três razões: traz achado datável ausente do codebook (a contraofensiva narrativa dos 'infiltrados', às 17h40 de 8/1); tem precedente direto em PT-19A, que entrou a partir de fonte de mesma natureza; e ancora empiricamente o primeiro passo da inferência de PT-62. Contra-argumento considerado e rejeitado: o eixo 08 trata cobertura jornalística como objeto de análise, mas o Manchetômetro mede circulação em plataforma, não interpreta cobertura — é fonte, da mesma família do NetLab. |
| **PT-52** | PT-52 RESOLVIDO em 16/08/2026, encerrando a última pendência de proveniência. Adotado 2.151 (CPMI, primária) como número principal, em lugar de '~1.200 em 40 ônibus' (imprensa, contagem parcial de meio de manhã). ACHADO NO PROCESSO: a CPMI se contradiz sobre o escopo — p. 76 diz 'no próprio domingo ou no dia seguinte' e p. 688 diz 'no ato de desocupação'. Adotada a p. 76, e o texto do registro passou a dizer '8 e 9 de janeiro', porque citar 2.151 como prisões da desocupação superestima o dia 9. Acrescentado o funil da responsabilização (2.151 flagrantes → ~1.400 no processo), cruzando CPMI e balanço de 2026. |
| **PT-53** | PT-53 RESOLVIDO em 16/08/2026 com o documento primário, e CORRIGIDO no mesmo dia: a cifra de 'mais de 1.600 ações penais' foi retirada por estar errada — o total é 1.335. O 1.618 pertence a audiências de custódia. A leitura dos gráficos vetoriais exigiu renderização da página; a camada de texto não os entrega. Corrigida também a fonte_url, que apontava para um balanço diferente. |
| **PT-56** | vínculo corrigido em 16/08/2026 — A questão de ordem preliminar de 14/05/2025 integra o julgamento e estava órfã. |
| **PT-58** | PT-58 elevado a fonte primária em 16/08/2026, com as decisões obtidas. CORREÇÃO DE FATO: a prisão preventiva de 22/11/2025 foi decretada na PETIÇÃO 14.129 — por coação no curso do processo, obstrução e art. 359-L —, convertendo cautelares de 17/7/2025, e NÃO na execução da AP 2668. São dois atos distintos: a preventiva contém risco de fuga em 22/11; o cumprimento da pena começa em 25/11. O registro anterior os tratava como um só. PÁGINAS CORRIGIDAS em 11/09/2026: o vínculo anterior ('Pet 14.129: 1 \| EP 169-Transferência: 1') apontava para a capa e a assinatura da peça; as transcrições foram localizadas página a página e o campo passou a 'Pet 14.129: 1, 7, 8, 10, 14, 16 \| EP 169-Transferência: 1'. |
| **PT-59** | PT-59 elevado a fonte primária em 16/08/2026. A decisão traz precisão que o registro não tinha: a transferência é para SALA DE ESTADO MAIOR no 19º BPM, dentro da Papuda — prerrogativa preservada, não equiparação ao regime comum. A mesma decisão ordena a junta médica que dois meses depois fundamenta a domiciliar de PT-60. PÁGINAS CORRIGIDAS em 11/09/2026: o vínculo anterior ('EP 169-Transferência: 1, 36') apontava para a capa e a assinatura da peça; as transcrições foram localizadas página a página e o campo passou a 'EP 169-Transferência: 1, 33, 35, 36'. |
| **PT-60** | PT-60 elevado a fonte primária em 16/08/2026. Duas precisões: a data é 24/03/2026, e a menção a 'prorrog. 03/07/2026' que constava do registro NÃO tem lastro no corpus — foi retirada do campo de data e marcada como não verificada. Acrescentado o antecedente relevante: o mesmo pedido fora INDEFERIDO em 2/3/2026 após perícia oficial, o que sustenta ler a concessão como modulação técnica e não como recuo. PÁGINAS CORRIGIDAS em 11/09/2026: o vínculo anterior ('EP 169-Domiciliar: 1, 40') apontava para a capa e a assinatura da peça; as transcrições foram localizadas página a página e o campo passou a 'EP 169-Domiciliar: 1, 35, 36, 37, 38, 40'. |
| **PT-61** | PT-61 RESOLVIDO em 16/08/2026 com a chegada do documento primário, fornecido pelo pesquisador. Percorreu três estados no mesmo dia: 'Confirmado' (jornalístico) → rebaixado a 'A verificar' pela auditoria → 'Confirmado' por corroboração jornalística dupla → agora 'Confirmado em fonte primária'. A cifra de 1.402 pode ser citada como dado oficial, com página. |

### Os três achados que motivaram as correções

**1. Cinco arquivos estavam no corpus sem vínculo com registro nenhum.** Quatro deles já tinham atribuição declarada em `Fontes/LEIA-ME_fontes.md` que nunca chegou ao codebook — o inventário de fontes e o codebook divergiam silenciosamente. O caso mais grave era o livro oficial do STF sobre o vandalismo, atribuído a PT-38 no inventário e ausente do registro.

**2. PT-08 afirmava fonte primária sem apontar arquivo.** O status dizia que *"o modelo efetivamente invocado pelos organizadores está confirmado em fonte primária"* e a tabela do relatório citava CPMI p. 614 — mas o vínculo local estava vazio. É o achado do **Sri Lanka, e não do Capitólio**, como precedente invocado: a contribuição teórica própria do projeto estava sem âncora rastreável.

**3. Dois registros declaravam mais confiança do que a evidência sustenta.** PT-53 e PT-61 estavam como `Confirmado` apoiados no balanço "Democracia Inabalada" de 29/04/2026 — documento **que não foi obtido**, por não estar indexado como PDF. Ambos foram rebaixados a `A verificar`. A cifra de 1.402 condenados está hoje apenas em fonte jornalística e não deve ser citada como dado oficial até a peça chegar.

**4. Um registro apontava para o documento errado.** PT-28 — o subdimensionamento crítico, *"apenas 20 policiais militares"* guarnecendo o Congresso às 14h45, que o codebook trata como **hoop test** — citava no texto "Relatório Final da CPMI, p. 657" e vinculava o acórdão da AP 2668. A frase foi localizada na CPMI p. 657 e é **ausente das 1.991 páginas do acórdão**. Erro anterior a esta rodada, corrigido.

> **Por que só a conferência contra o PDF pegou isso.** As checagens estruturais derivam o código do documento a partir do próprio vínculo — validam como coerente um vínculo que aponta para a peça errada. Só abrir o arquivo na página e procurar o texto revela o descasamento. Por isso `scripts/conferir_paginas.py` passa a ser parte da rotina, e não um extra: **é a única checagem que lê a fonte.**

### Conferência integral contra o texto dos PDFs

Rodada sobre os **58 registros com página estruturada em documento PDF**, abrindo cada arquivo na página citada e procurando a transcrição literal:

| Resultado | N |
|:--|--:|
| Transcrição localizada na página citada | **53** |
| Divergência | **0** |
| Sem transcrição literal para conferir | 5 |

Os cinco indeterminados — PT-08, PT-13, PT-23, PT-33 e PT-55 — não são falhas: seu `fonte_trecho` traz referência de página sem citação entre aspas, então não há o que casar contra o PDF. São candidatos naturais a ganhar transcrição literal na próxima passagem pelo `Caderno-de-evidencias/`.

> **Dois falsos positivos do próprio verificador, corrigidos e registrados.** PT-31 falhou porque o casamento estava ancorado no início da citação, e hifenização no PDF costuma atingir justamente as primeiras palavras — passou a procurar janelas ao longo do texto. PT-16 falhou porque seu `fonte_trecho` usa aspas simples para **títulos de seção** (*'A radicalização do movimento'*) e não só para transcrições; a extração casava o intervalo entre dois títulos, que é aparato de referência. Ambos conferidos manualmente contra o PDF e **corretos no codebook**. Fica o registro de que a falha era do instrumento, não do dado.

Além disso, **sete registros citavam dois documentos e declaravam apenas um**. A corroboração dupla — que é uma força do aparato, não um detalhe — estava invisível. PT-18 é o caso exemplar: o regime de sobreaviso está na CPMI **e** nas conclusões D e H do relatório Cappelli, dois documentos independentes que convergem.

> **Falso positivo registrado.** A varredura automática apontou PT-45 e PT-48 como registros de fonte dupla. São falsos positivos: ali "Capelli" aparece como o nome do interventor designado, não como citação do relatório dele. Conferidos e mantidos com fonte única.

## Cobertura por documento

| Documento | Registros que ancora | Páginas | Natureza |
|:--|--:|--:|:--|
| CPMI | 52 | 1333 | oficial |
| Cappelli | 5 | 62 | espelho |
| AP 2668 | 5 | 1991 | oficial |
| PGR | 3 | 272 | oficial |
| Balanço 2026 | 3 | 15 | oficial |
| ADC 43/44/54 | 2 | 489 | oficial |
| TRF-4 | 2 | 657 | oficial |
| EP 169-Transferência | 2 | 36 | oficial |
| ADC 43-MC | 1 | 250 | oficial |
| HC 152.752 | 1 | 464 | oficial |
| TSE RCand | 1 |  | oficial |
| HC 164.493 | 1 | 441 | oficial |
| HC 193.726-2 | 1 | 182 | oficial |
| HC 193.726 | 1 | 264 | oficial |
| NetLab | 1 |  | transcrição |
| Livro STF 2023 | 1 | 210 | oficial |
| Manchetômetro | 1 | 16 | laboratório |
| AP 2668-QO | 1 | 50 | oficial |
| Pet 14.129 | 1 | 17 | oficial |
| EP 169-Domiciliar | 1 | 40 | oficial |

O Relatório Final da CPMI ancora sozinho **52 dos 74 registros vinculados**. Isso é uma dependência a declarar no artigo: a espinha dorsal de $T_0$ vem de uma peça de investigação parlamentar, com posição política própria e votos em separado. Que a CPMI afirme algo não é o mesmo que o fato estar estabelecido — advertência que já consta do `Caderno-de-evidencias/LEIA-ME.md` e que o artigo precisa repetir.

## Lista 1 — Registros ancorados (74)

Cada um aponta arquivo e página. A numeração impressa do relatório da CPMI coincide com a paginação do PDF, então a conferência é direta: abrir o arquivo na página indicada.

| Registro | Documento(s) | Página | Classe |
|:--|:--|:--|:--|
| PT-02A | ADC 43/44/54 + ADC 43-MC | ADC 43/44/54: 3, 9 | Confirmado |
| PT-03A | TRF-4 | TRF-4: 395 | Confirmado em fonte primária |
| PT-03B | TRF-4 | — | Confirmado |
| PT-03C | HC 152.752 | — | Confirmado |
| PT-03E | TSE RCand | TSE RCand: ementa itens 2-4 e 12; dispositivo | Confirmado em fonte primária |
| PT-05A | ADC 43/44/54 | — | Confirmado |
| PT-06A | PGR | PGR: 8 | Confirmado |
| PT-06B | HC 164.493 + HC 193.726-2 | HC 164.493: inteiro teor | Confirmado |
| PT-06C | HC 193.726 | — | Confirmado |
| PT-07 | PGR | PGR: 8, 249 | Confirmado em fonte primária |
| PT-08 | CPMI | CPMI: 614 | Contextual |
| PT-08A | CPMI | CPMI: 465-468, 466, 467, 468 | Confirmado em fonte primária |
| PT-08B | CPMI | CPMI: 468-469 | Confirmado em fonte primária |
| PT-08C | CPMI | CPMI: 469, 470 | Confirmado em fonte primária |
| PT-09 | CPMI | CPMI: 472 | Confirmado em fonte primária |
| PT-10 | CPMI | CPMI: 999, 1021, 1023 | Confirmado em fonte primária |
| PT-10A | CPMI | CPMI: 884-887, 887-890 | Confirmado em fonte primária |
| PT-11 | CPMI | CPMI: 515 | Confirmado em fonte primária |
| PT-12 | CPMI | CPMI: 524, 529, 531, 532, 510, 577 | Confirmado em fonte primária |
| PT-12A | CPMI | CPMI: 577-578, 880-884 | Confirmado em fonte primária |
| PT-13 | PGR + CPMI | PGR: peça integral \| CPMI: 230, 566 | Confirmado em fonte primária |
| PT-14 | CPMI | CPMI: 481, 16 | Confirmado em fonte primária |
| PT-15 | CPMI | CPMI: 25, 53, 274 | Confirmado em fonte primária |
| PT-16 | CPMI | CPMI: 584, 269, 1031, 599 | Confirmado em fonte primária |
| PT-17 | CPMI | CPMI: 507, 612 | Confirmado em fonte primária |
| PT-18 | CPMI + Cappelli | CPMI: 646, 711 \| Cappelli: 55, 57 | Confirmado em fonte primária |
| PT-19 | CPMI | CPMI: 614-625, 614, 620 | Confirmado em fonte primária |
| PT-19A | NetLab | — | Confirmado |
| PT-19B | AP 2668 | AP 2668: 495-496 | Confirmado em fonte primária |
| PT-20 | CPMI | CPMI: 576 | Confirmado em fonte primária |
| PT-20A | CPMI | CPMI: 635, 842 | Confirmado em fonte primária |
| PT-20B | Cappelli | Cappelli: 54 | Confirmado em fonte primária |
| PT-21 | CPMI | CPMI: 576, 374, 637, 643 | Confirmado em fonte primária |
| PT-22 | CPMI | CPMI: 643 | Confirmado em fonte primária |
| PT-23 | CPMI | CPMI: 376, 374-375 | Confirmado em fonte primária |
| PT-24 | CPMI | CPMI: 645, 648 | Confirmado em fonte primária |
| PT-25 | CPMI | CPMI: 648 | Confirmado em fonte primária |
| PT-26 | CPMI | CPMI: 650, 649 | Confirmado em fonte primária |
| PT-27 | CPMI + Cappelli | CPMI: 651 | Confirmado |
| PT-28 | CPMI + Cappelli + AP 2668 | CPMI: 657 \| Cappelli: 57 \| AP 2668: 495, 497 | Confirmado em fonte primária |
| PT-29 | CPMI | CPMI: 657 | Confirmado em fonte primária |
| PT-30 | CPMI | CPMI: 670 | Confirmado em fonte primária |
| PT-31 | CPMI | CPMI: 667 | Confirmado em fonte primária |
| PT-32 | CPMI | CPMI: 674, 658 | Confirmado em fonte primária |
| PT-33 | CPMI | CPMI: 670-671 | Confirmado em fonte primária |
| PT-34 | CPMI | CPMI: 674, 695, 643, 637, 374, 576, 688 | Confirmado em fonte primária |
| PT-35 | CPMI | CPMI: 673 | Confirmado em fonte primária |
| PT-36 | CPMI | CPMI: 671 | Confirmado em fonte primária |
| PT-37 | CPMI | CPMI: 667 | Confirmado em fonte primária |
| PT-38 | Livro STF 2023 | Livro STF 2023: inteiro teor | Confirmado |
| PT-39 | CPMI + AP 2668 | CPMI: 677 \| AP 2668: 496 | Confirmado em fonte primária |
| PT-40 | CPMI | CPMI: 678 | Confirmado em fonte primária |
| PT-41 | CPMI | CPMI: 679 | Confirmado em fonte primária |
| PT-42 | CPMI | CPMI: 680 | Confirmado em fonte primária |
| PT-43 | CPMI | CPMI: 678 | Confirmado em fonte primária |
| PT-44 | CPMI | CPMI: 680 | Confirmado em fonte primária |
| PT-45 | CPMI | CPMI: 680 | Confirmado em fonte primária |
| PT-46 | CPMI | CPMI: 681 | Confirmado em fonte primária |
| PT-47 | CPMI | CPMI: 681 | Confirmado em fonte primária |
| PT-48 | CPMI | CPMI: 681 | Confirmado em fonte primária |
| PT-49 | CPMI | CPMI: 687 | Confirmado em fonte primária |
| PT-50 | CPMI | CPMI: 685 | Confirmado em fonte primária |
| PT-50A | Manchetômetro | Manchetômetro: 3, 4, 9, 10, 13, 14, 15 | Confirmado |
| PT-51 | CPMI | CPMI: 686 | Confirmado em fonte primária |
| PT-52 | CPMI + Cappelli + Balanço 2026 | CPMI: 576, 687, 688, 76 \| Cappelli: 53 \| Balanço 2026: 4, 5, 6 | Confirmado em fonte primária |
| PT-53 | Balanço 2026 | Balanço 2026: 4, 5, 6 | Confirmado em fonte primária |
| PT-54 | CPMI | CPMI: 21 | Confirmado em fonte primária |
| PT-55 | CPMI | CPMI: 831, 835, 836 | Confirmado em fonte primária |
| PT-56 | AP 2668 + AP 2668-QO | AP 2668: inteiro teor | Confirmado |
| PT-57 | AP 2668 | — | Confirmado |
| PT-58 | Pet 14.129 + EP 169-Transferência | Pet 14.129: 1, 7, 8, 10, 14, 16 \| EP 169-Transferência: 1 | Confirmado em fonte primária |
| PT-59 | EP 169-Transferência | EP 169-Transferência: 1, 33, 35, 36 | Confirmado em fonte primária |
| PT-60 | EP 169-Domiciliar | EP 169-Domiciliar: 1, 35, 36, 37, 38, 40 | Confirmado em fonte primária |
| PT-61 | Balanço 2026 | Balanço 2026: 6, 7, 8, 10, 11, 13, 14 | Confirmado em fonte primária |

## Lista 2 — Sem âncora documental por natureza do registro (7)

Estes **não são lacunas**. São itens de enquadramento histórico apoiados na bibliografia teórica, mais uma inferência declarada. Perseguir fonte primária para eles seria erro de categoria: não são fatos a verificar em documento, são leituras a discutir em referencial teórico.

| Registro | Classe | Apoio declarado |
|:--|:--|:--|
| PT-01 | Contextual | Literatura: Alonso (2017); Tatagiba (2014) — item contextual, sem fonte primária consultada |
| PT-02 | Contextual | Literatura: Alonso (2017); Meneguello; Rocha de Barros — item contextual |
| PT-03 | Contextual | Literatura: Nobre (2020) — item contextual |
| PT-04 | Contextual | Literatura: Campos Mello (2020); Cesarino (2022) — item contextual |
| PT-05 | Contextual | Literatura: Abranches; Avritzer — item contextual |
| PT-06 | Contextual | Literatura: Cesarino (2022) — item contextual |
| PT-62 | Inferência do analista | Inferência analítica a partir do conjunto das fontes — requer verificação empírica dedicada |

## Lista 3 — Dependentes de coleta (1)

Estas são as lacunas reais. Cada uma tem uma peça identificada e uma via de obtenção; os comandos estão em `scripts/baixar_fontes.sh`.

| Registro | Classe | O que falta |
|:--|:--|:--|
| PT-03D | Confirmado | Arquivamento em PDF das matérias da Agência Brasil |

## Fila de coleta

| Peça | Registro(s) | Via | Bloqueio | Prior. |
|:--|:--|:--|:--|:--|
| Decisão da prisão preventiva (22-25/11/2025) | PT-58 | STF — busca de jurisprudência | AWS WAF (cookie aws-waf-token) | Alta |
| Balanço "Democracia Inabalada" (29/04/2026) | PT-53; PT-61 | Assessoria de imprensa do STF | Não indexado como PDF | Alta |
| Decisão de transferência para a Papuda (15/01/2026) | PT-59 | STF | AWS WAF (cookie aws-waf-token) | Média |
| Decisão de transferência para a Papuda (15/01/2026) | PT-59 | STF | AWS WAF (cookie aws-waf-token) | Média |
| Prisão domiciliar humanitária — Execução Penal 169 | PT-60 | STF | AWS WAF (cookie aws-waf-token) | Média |
| Arquivamento em PDF das matérias da Agência Brasil | PT-03D; PT-38; PT-12 | agenciabrasil.ebc.com.br | Nenhum | Média |
| Decisão sobre o Manchetômetro (Doxa/IESP-UERJ) | — | — | Decisão do pesquisador | Média |
| Laudos periciais do Instituto de Criminalística/PF | PT-38 | Polícia Federal | Provável restrição de acesso | Baixa |
| Sentença de 1ª instância de Moro (12/07/2017), inteiro teor | PT-03A | JFPR / e-proc | Consulta processual | Baixa |

## O que esta auditoria não faz

Três limites, declarados para que ninguém leia mais do que ela oferece.

1. **Não confere, para todos os 82, se a página sustenta a afirmação.** A checagem estrutural verifica que o vínculo existe, que o arquivo está em disco e que a página pertence ao documento vinculado. A conferência do *conteúdo* contra o texto do PDF é feita **por amostra** — `scripts/conferir_paginas.py`, 12 registros por rodada, ou `--todos` para os 68 com página. A transcrição literal de 49 registros está no `Caderno-de-evidencias/`.
2. **Não avalia a qualidade da fonte.** Que um registro esteja ancorado no relatório Cappelli não o torna verdadeiro — torna-o rastreável. E o Cappelli, registre-se, é **espelho jornalístico**: traz identificação oficial mas não foi localizado em domínio oficial. Isso está declarado no inventário e precisa constar da nota de fontes do artigo.
3. **Não resolve as ressalvas de proveniência.** A auditoria as classifica; não as fecha — quem as fecha é a rodada de conferência. As quatro que existiam foram fechadas em 16/08/2026: PT-34, a mais grave, com os "4 mil" retirados e substituídos por faixa ancorada em duas medições oficiais independentes (ver `docs/ESTIMATIVA-MULTIDAO-8JAN.md`); PT-12, com a cifra de "mais de 100 acampamentos" retirada; PT-17, com a data de saída localizada na CPMI, p. 612; e PT-52, com as 2.151 prisões em flagrante adotadas no lugar dos ~1.200 de imprensa. Cada fechamento está no `nota_auditoria` do próprio registro.

---

*Regenerar com* `python scripts/gerar_auditoria.py`. *Verificar a integridade com* `python scripts/verificar_integridade.py`.
