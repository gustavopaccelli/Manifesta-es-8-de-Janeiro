# Tabela-espelho dos eventos — figuras × codebook

> **Peça gerada por `scripts/gerar_tabela_espelho.py`. Não edite à mão.** Ela existe para responder uma pergunta que o ciclo não respondia: *as figuras ainda dizem o que o codebook diz?* `conferir_figuras.py` confere cobertura, selo, procedência e cifras retiradas — **não o texto do mecanismo** (item 42.3, lacuna aberta desde 10/10/2026).

**85 registros no codebook · 80 pontos na cronologia interativa · 3 deles compostos.**

## 1. O que a comparação mede, e o que ela não pode cobrar

| campo da figura | idêntico | contido | parafraseado | ausente na figura |
|:--|--:|--:|--:|--:|
| `ator` → `ator_grupo` | 52 | 7 | 26 | 0 |
| `rep` → `repertorio_acao` | 45 | 4 | 36 | 0 |
| `tgt` → `target_alvo` | 70 | 2 | 13 | 0 |
| `frm` → `framing_narrativa` | 54 | 3 | 28 | 0 |
| `res` → `resposta_estatal` | 60 | 4 | 21 | 0 |
| `mec` → `mecanismo_causal` | 0 | 0 | 85 | 0 |

> **`mec` parafraseado em toda parte é desenho, não defeito.** A figura precisa de uma frase legível; `mecanismo_causal` carrega a prosa de auditoria. **O que é conferível é o NOME** — a frase até o primeiro `:` —, e é só isso que a coluna `espelho_nome_mecanismo` cobra.

## 2. Nome do mecanismo: onde a figura e o codebook discordam

**0 divergências**, contra a linha de base de **0** medida em 20/10/2026.

Nenhuma. A figura e o codebook nomeiam o mesmo mecanismo em todos os registros.

## 3. A tabela, registro por registro

A versão completa — com os seis campos da figura ao lado dos seis do codebook e o estado do espelho de cada um — está em `data/processed/tabela_espelho_eventos.csv`. Abaixo, a forma scanável.

| id | data | evento na figura | fase | classe | nome do mecanismo | ponto | espelho |
|:--|:--|:--|:--|:--|:--|:--|:--|
| `PT-01` | jun/2013 | Jornadas de Junho | T-1 Conjuntural | Confirmado | janela de oportunidades politicas aberta no ciclo de 2013, … | — | ✅ |
| `PT-01A` | 04/11/2014 (decisão do TSE) — 05/11/2015 (relatório final) | PSDB pede auditoria ao TSE | T-1 Conjuntural | Confirmado | proposta de mecanismo, nao atribuida | — | ✅ |
| `PT-01B` | 29/10/2015 | Uma Ponte para o Futuro | T-1 Conjuntural | Confirmado | proposta de mecanismo, nao atribuida | — | ✅ |
| `PT-02` | 2015–2016 | Marchas pró-impeachment | T-1 Conjuntural | Confirmado | apropriacao parcial do repertorio de protesto por contramov… | — | ✅ |
| `PT-02A` | 17/02/2016 | STF admite prisão em 2ª instância | T-1 Conjuntural | Confirmado | precondicao jurisprudencial do arco judicial | — | ✅ |
| `PT-03` | 31/08/2016 | Impeachment consumado | T-1 Conjuntural | Confirmado | ressignificacao do protesto | — | ✅ |
| `PT-03A` | 12/07/2017 | Moro condena Lula (triplex) | T-1 Conjuntural | Confirmado em fonte primária | certificacao judicial do frame anticorrupcao | — | ✅ |
| `PT-03B` | 24/01/2018 | TRF-4 confirma e amplia a pena | T-1 Conjuntural | Confirmado | acionamento do gatilho de inelegibilidade | — | ✅ |
| `PT-03C` | 04/04/2018 | STF nega HC; prisão em Curitiba | T-1 Conjuntural | Confirmado | fechamento da via recursal | PT-03C/D | ✅ |
| `PT-03D` | 07/04/2018 | STF nega HC; prisão em Curitiba | T-1 Conjuntural | Confirmado | remocao do competidor e reconfiguracao da estrutura de opor… | PT-03C/D | ✅ |
| `PT-03E` | 31/08–01/09/2018 | TSE barra a candidatura | T-1 Conjuntural | Confirmado em fonte primária | exclusao institucional do favorito | — | ✅ |
| `PT-04` | 28/10/2018 | Eleição de Bolsonaro | T-1 Conjuntural | Confirmado | incorporacao do movimento ao estado | — | ✅ |
| `PT-05` | 2019–2022 | Atrito com STF e Congresso | T-1 Conjuntural | Confirmado | erosao do consenso institucional | — | ✅ |
| `PT-05A` | 07–08/11/2019 | Fim da prisão em 2ª instância; Lula é s… | T-1 Conjuntural | Confirmado | reversao jurisprudencial e reabertura parcial da oportunida… | — | ✅ |
| `PT-06` | 2020–2021 | Pandemia e radicalização | T-1 Conjuntural | Confirmado | mobilizacao permanente da base por circulacao de enquadrame… | — | ✅ |
| `PT-06A` | 08/03/2021 | Anulação; elegibilidade restaurada | T-1 Conjuntural | Confirmado | anulacao por vicio de competencia | PT-06A/B/C | ✅ |
| `PT-06B` | 23/03/2021 (Plenário confirma em 23/06/2021) | Anulação; elegibilidade restaurada | T-1 Conjuntural | Confirmado | descertificacao do agente judicial | PT-06A/B/C | ✅ |
| `PT-06C` | 15/04/2021 | Anulação; elegibilidade restaurada | T-1 Conjuntural | Confirmado | reabertura da estrutura de oportunidade eleitoral | PT-06A/B/C | ✅ |
| `PT-07` | 22/03/2021 (primeira deliberação datada pela denúncia) | Primeira deliberação do grupo | T-1 Conjuntural | Confirmado em fonte primária | deliberacao de ruptura e articulacao do quadro de fraude | — | ✅ |
| `PT-08` | 06/01/2021 | Capitólio (EUA) | T-1 Conjuntural | Confirmado | difusao transnacional / emulacao | — | ✅ |
| `PT-08A` | out/2022 (05–26/10/2022) | TRÊS MECANISMOS, UM POR REGISTRO. (PT-0… | T-1 Operacional | Confirmado em fonte primária | captura de aparato estatal para fim eleitoral | PT-08A / PT-08B / PT-08C | ✅ |
| `PT-08B` | 29/10/2022 | TRÊS MECANISMOS, UM POR REGISTRO. (PT-0… | T-1 Operacional | Confirmado em fonte primária | tentativa de contencao institucional preventiva | PT-08A / PT-08B / PT-08C | ✅ |
| `PT-08C` | 30/10/2022 (dia do segundo turno) | TRÊS MECANISMOS, UM POR REGISTRO. (PT-0… | T-1 Operacional | Confirmado em fonte primária | supressao seletiva de participacao eleitoral | PT-08A / PT-08B / PT-08C | ✅ |
| `PT-09` | 30/10/2022 | Derrota eleitoral (e o silêncio) | T-1 Operacional | Confirmado em fonte primária | gatilho | — | ✅ |
| `PT-10` | 30/10–06/11/2022 | Bloqueios: 1.300 pontos | T-1 Operacional | Confirmado em fonte primária | ativacao imediata e teste de capacidade de contencao estatal | — | ✅ |
| `PT-10A` | nov/2022 (comboios a partir de 04/11) | MBVA: 272 caminhões do agro | T-1 Operacional | Confirmado em fonte primária | mobilizacao de recursos por setor economico organizado | — | ✅ |
| `PT-11` | 01/11/2022 | “Fiquem à vontade” | T-1 Operacional | Confirmado em fonte primária | sinalizacao ambigua da lideranca | — | ✅ |
| `PT-12` | nov/2022 em diante | Acampamentos em quartéis (todos os Esta… | T-1 Operacional | Confirmado em fonte primária | conversao de repertorio | — | ✅ |
| `PT-12A` | nov/2022 – jan/2023 | A rede de financiamento | T-1 Operacional | Confirmado em fonte primária | agregacao na base e intermediacao concentrada | — | ✅ |
| `PT-13` | nov/2022 | Aval presidencial aos acampamentos | T-1 Operacional | Confirmado em fonte primária | certificacao por elite (elite certification) | — | ✅ |
| `PT-14` | 22/11/2022 | PL pede anulação de 280 mil urnas | T-1 Operacional | Confirmado em fonte primária | fechamento da via institucional | — | ✅ |
| `PT-15` | 12/12/2022 (noite) | Diplomação: tentativa de invadir a PF | T-1 Operacional | Confirmado em fonte primária | escalada de radicalizacao e teste de repertorio violento | — | ✅ |
| `PT-16` | 24/12/2022 | Bomba no aeroporto | T-1 Operacional | Confirmado em fonte primária | radicalizacao de flanco (flank radicalization) | — | ✅ |
| `PT-17` | 30/12/2022 | Bolsonaro admite buscar alternativas e … | T-1 Operacional | Confirmado em fonte primária | desincorporacao da lideranca | — | ✅ |
| `PT-18` | 01/01/2023 (e o rebaixamento do dispositivo para 08/01) | Posse com POI; dia 8 em sobreaviso | T-1 Operacional | Confirmado em fonte primária | rebaixamento deliberado do dispositivo por comparacao com a… | — | ✅ |
| `PT-18A` | 02–03/01/2023 | Troca do escalão de planejamento da SSP… | T-1 Operacional | Confirmado em fonte primária | descontinuidade administrativa do escalao de planejamento | — | ✅ |
| `PT-19` | dez/2022–jan/2023 | Código “Festa da Selma” | T-1 Operacional | Confirmado em fonte primária | coordenacao distribuida por criptolinguagem | — | ✅ |
| `PT-19A` | nov/2022 – jan/2023 (coleta em 24–26/01/2023) | 185 anúncios pagos na Meta | T-1 Operacional | Confirmado | circulacao paga | — | ✅ |
| `PT-19B` | 04–05/01/2023 | Grupo “Difusão”: alerta e silêncio | T-1 Operacional | Confirmado em fonte primária | canal dedicado de alerta, criado e silenciado | — | ✅ |
| `PT-20` | 05/01/2023 | Acampamento: 300 pessoas | T-1 Operacional | Confirmado em fonte primária | linha de base do afluxo | — | ✅ |
| `PT-20A` | 06/01/2023 17h30 | GSI dispensa reforço no Planalto | T-1 Operacional | Confirmado em fonte primária | desmobilizacao preventiva do dispositivo | — | ✅ |
| `PT-20B` | 06/01/2023 | SSP-DF: inteligência própria alerta | T-1 Operacional | Confirmado em fonte primária | falha de conversao de inteligencia em acao | — | ✅ |
| `PT-21` | 06–07/01/2023 | Caravanas: salto para 5.500 | T-1 Operacional | Confirmado em fonte primária | concentracao de contingente no acampamento | — | ✅ |
| `PT-22` | 08/01/2023 08h53 e 09h00 (dados apurados até 08h20) | Abin: 101 ônibus; 3.000 pessoas | T-1 Operacional | Confirmado em fonte primária | falha de conversao de inteligencia em acao | — | ✅ |
| `PT-23` | 08/01/2023 10h00 | Alerta explícito às 10h | T-1 Operacional | Confirmado em fonte primária | segunda falha de conversao | — | ✅ |
| `PT-24` | 08/01/2023 13h00 | Marcha deixa o QG | T0 Mobilização | Confirmado em fonte primária | deslocamento espacial como escalada | — | ✅ |
| `PT-25` | 08/01/2023 13h23 | Áudio tranquiliza o governador | T0 Mobilização | Confirmado em fonte primária | neutralizacao da percepcao de ameaca no topo da cadeia poli… | — | ✅ |
| `PT-26` | 08/01/2023 14h30 | 1ª barreira (Via N1) | T0 Mobilização | Confirmado em fonte primária | teste sequencial de contencao | — | ✅ |
| `PT-27` | 08/01/2023 14h43 | Gradis da Av. das Bandeiras | T0 Mobilização | Confirmado | ruptura de barreira fisica | — | ✅ |
| `PT-28` | 08/01/2023 14h45 | Apenas 20 PMs no Congresso | T0 Mobilização | Confirmado em fonte primária | subdimensionamento critico do dispositivo | — | ✅ |
| `PT-29` | 08/01/2023 15h00 | Invasão do Congresso | T0 Execução | Confirmado em fonte primária | demonstracao de viabilidade | — | ✅ |
| `PT-30` | 08/01/2023 15h10 | Fundos do Planalto | T0 Execução | Confirmado em fonte primária | contagio e difusao simultanea de alvos (multiplicacao de fr… | — | ✅ |
| `PT-31` | 08/01/2023 15h15 | PMs sinalizam para prosseguir | T0 Execução | Confirmado em fonte primária | defeccao do agente de contencao | — | ✅ |
| `PT-32` | 08/01/2023 15h16 | Retirada libera acesso ao STF | T0 Execução | Confirmado em fonte primária | abertura de corredor | — | ✅ |
| `PT-33` | 08/01/2023 15h20 | Grades e vidros do Planalto | T0 Execução | Confirmado em fonte primária | escalada de repertorio | — | ✅ |
| `PT-34` | 08/01/2023 15h26 | Ocupação da Praça | T0 Execução | Confirmado em fonte primária | concentracao simultanea no conjunto simbolico | — | ✅ |
| `PT-35` | 08/01/2023 15h37 | Invasão do STF | T0 Execução | Confirmado em fonte primária | fechamento do ciclo de alvos em 37 minutos | — | ✅ |
| `PT-36` | 08/01/2023 15h45 | 3º andar do Planalto | T0 Execução | Confirmado em fonte primária | penetracao do nucleo simbolico | — | ✅ |
| `PT-37` | 08/01/2023 15h53 | PMs abandonam o Congresso | T0 Execução | Confirmado em fonte primária | colapso da contencao e inversao da relacao de forca | — | ✅ |
| `PT-38` | 08/01/2023 ~15h–16h30 | Violência simbólica dirigida. O alvo nã… | T0 Execução | Confirmado | violencia simbolica dirigida | — | ✅ |
| `PT-39` | 08/01/2023 16h25 | Início da expulsão | T0 Resposta tática | Confirmado em fonte primária | inflexao tardia da contencao | — | ✅ |
| `PT-40` | 08/01/2023 16h40 | Guarda Presidencial no Planalto | T0 Resposta tática | Confirmado em fonte primária | substituicao do agente de contencao | — | ✅ |
| `PT-41` | 08/01/2023 17h00 | Choque chega 2h após ser pedido | T0 Resposta tática | Confirmado em fonte primária | latencia de resposta | — | ✅ |
| `PT-42` | 08/01/2023 17h08 | Ibaneis demite Anderson Torres | T0 Resposta política | Confirmado em fonte primária | deslocamento de responsabilidade (blame shifting) sob press… | — | ✅ |
| `PT-43` | 08/01/2023 17h15 | Reforço do CMP no palácio | T0 Resposta tática | Confirmado em fonte primária | consolidacao da retomada por escalonamento de forcas | — | ✅ |
| `PT-44` | 08/01/2023 17h30 | Prédios majoritariamente livres | T0 Resposta tática | Confirmado em fonte primária | retomada assimetrica | — | ✅ |
| `PT-45` | 08/01/2023 17h50 | Intervenção federal decretada | T0/T+1 Resposta institucional | Confirmado em fonte primária | federalizacao da resposta | — | ✅ |
| `PT-46` | 08/01/2023 18h20 | Fogo no gramado do Congresso | T0 Execução | Confirmado em fonte primária | repertorio residual de confronto apos a perda do territorio… | — | ✅ |
| `PT-47` | 08/01/2023 19h00 | Ibaneis pede desculpas | T+1 Resposta política | Confirmado em fonte primária | tentativa de contencao reputacional diante da iminente resp… | — | ✅ |
| `PT-48` | 08/01/2023 20h00 | Cappelli convoca todo o efetivo | T+1 Resposta institucional | Confirmado em fonte primária | reversao do mecanismo de falha de contencao pela unificacao… | — | ✅ |
| `PT-49` | 08/01/2023 (noite) | Moraes: desocupar em 24h | T+1 Resposta judicial | Confirmado em fonte primária | gatilho juridico que destrava a desmobilizacao | — | ✅ |
| `PT-50` | 08/01/2023 21h17 | Nota de Bolsonaro, 6h depois | T+1 Enquadramento | Confirmado em fonte primária | descertificacao tardia (cerca de 6 horas apos o inicio) | — | ✅ |
| `PT-50A` | 08/01/2023, a partir das 17h40 — 10/01/2023 | Contraofensiva narrativa: “infiltrados” | T+1 Enquadramento | Confirmado | recaptura do enquadramento | — | ✅ |
| `PT-51` | 08/01/2023 22h00 | Lula e ministros vistoriam | T+1 Resposta institucional | Confirmado em fonte primária | ritual de recertificacao da ordem | — | ✅ |
| `PT-52` | 09/01/2023 (manhã) | Desmonte do acampamento: 2.151 prisões | T+1 Desarticulação | Confirmado em fonte primária | destruicao da infraestrutura de mobilizacao | — | ✅ |
| `PT-53` | jan/2023 em diante | Inquéritos e 1.335 ações penais | T+1 Resposta judicial | Confirmado em fonte primária | repressao juridica seletiva e escalonada por nucleos (execu… | — | ✅ |
| `PT-54` | 2023 | Instalação da CPMI | T+1 Resposta legislativa | Confirmado em fonte primária | abertura de arena institucional de atribuicao de responsabi… | — | ✅ |
| `PT-55` | 17–18/10/2023 | Relatório da CPMI: 61 indiciamentos | T+1 Resposta legislativa | Confirmado em fonte primária | certificacao parlamentar da cadeia causal | — | ✅ |
| `PT-56` | 11/09/2025 | Condenação do núcleo crucial | T+1 Resposta judicial | Confirmado | fechamento causal "de cima" | — | ✅ |
| `PT-57` | 22/10/2025 | Acórdão da AP 2668 | T+1 Resposta judicial | Confirmado | consolidacao documental da narrativa causal oficial | — | ✅ |
| `PT-58` | 22/11/2025 (preventiva) — 25/11/2025 (início do cumprimento da pena) | Prisão de Bolsonaro | T+1 Resposta judicial | Confirmado em fonte primária | responsabilizacao do topo da cadeia | — | ✅ |
| `PT-59` | 15/01/2026 | Sala de Estado Maior na Papuda | T+1 Resposta judicial | Confirmado em fonte primária | normalizacao da execucao penal do ex-chefe do executivo | — | ✅ |
| `PT-60` | 24/03/2026 | Prisão domiciliar humanitária | T+1 Resposta judicial | Confirmado em fonte primária | modulacao humanitaria da sancao | — | ✅ |
| `PT-61` | 29/04/2026 | Balanço: 1.402 responsabilizados | T+1 Balanço institucional | Confirmado em fonte primária | encerramento formal do ciclo repressivo-judicial | — | ✅ |
| `PT-62` | 2023–2026 | Desmobilização por repressão seletiva, … | T+1 Efeito de processo | Inferência do analista | desmobilizacao por repressao seletiva, seguida de migracao … | — | ✅ |

