# Scripts — pipeline de dados do process tracing

Criados em **16/08/2026**, quando o codebook passou a ter uma fonte única da verdade.

## A regra

**O JSON é a única fonte da verdade.** `process_tracing_8jan_eventos.json` é o
que se edita. CSV e XLSX são **gerados** e serão sobrescritos sem aviso na
próxima execução.

Antes de 16/08/2026 não era assim, e o resultado foi previsível: o CSV carregava
um campo `Fonte_Local` que o JSON não tinha, embora o próprio
`metadados.colunas_codebook` do JSON já o declarasse. Os formatos divergiram em
silêncio por quatro dias. O gerador único existe para que isso não se repita.

## O ciclo

Toda vez que uma fonte nova entra em `Fontes/`, ou que um registro muda:

```bash
# 1. edite o JSON (à mão, ou por script de migração)

# 2. declare a procedência do arquivo novo em PROCEDENCIA, dentro de gerar_codebook.py

# 3. regere os formatos derivados
python scripts/gerar_codebook.py

# 4. regere o relatório de auditoria
python scripts/gerar_auditoria.py

# 5. regere a seção "Ordem de ataque" da agenda
python scripts/gerar_ordem_de_ataque.py

# 6. verifique — falha se algo divergir
python scripts/verificar_integridade.py

# 7. confira as figuras de reports/figures/ contra o codebook
python scripts/conferir_figuras.py

# 8. confira o relatório de pesquisa contra o codebook
python scripts/conferir_relatorio.py

# 9. confira a amostra contra o texto dos PDFs
python scripts/conferir_paginas.py

# 10. confira o campo multiorganizacional contra o codebook
python scripts/desenhar_campo.py --autoteste

# 11. confira as citações do documento 11 contra o codebook
python scripts/conferir_hipoteses.py
```

Os passos 3 a 11 são o que `bash scripts/ciclo.sh` roda, nessa ordem — **doze
passos desde 21/10/2026**, quando a grade funcional do enquadramento entrou como
passo 5 e o registro de estado de leitura como passo 6; a tabela-espelho entrou como passo 4 em 20/10. Os passos 6 a 11 devolvem código de saída != 0 em caso
de falha, então servem em gancho de pré-commit. Os passos 3 a 5 **geram**: se a
árvore ficar suja depois do ciclo, foi peça derivada que estava atrasada.

## Os arquivos

| Script | O que faz |
|:--|:--|
| `gerar_codebook.py` | JSON → `data/processed/`: CSV (UTF-8 com BOM) + XLSX de quatro abas. Guarda `PROCEDENCIA` (procedência de cada arquivo do corpus) e `PENDENCIAS` (fila de coleta). |
| `gerar_auditoria.py` | JSON → `reports/AUDITORIA-FONTES.md`. A narrativa vive no script; as tabelas saem dos dados. **E em 18/10/2026 descobriu-se que um bloco da narrativa trazia cifra DIGITADA e errada** — dizia 58 registros com página em PDF (são 77), 5 sem transcrição literal (são 4) e nomeava PT-08 entre eles, que não é um deles. Aquele bloco passou a importar `pares` e `transcricoes` de `conferir_paginas.py` e a medir; o que só o passo 7 sabe deixou de ser repetido aqui. Ver item 64. |
| `gerar_painel.py` | **Passo 5 do ciclo, desde 27/10/2026 (item 91).** O **Painel de estado** no alto de `../docs/PENDENCIAS-ANALITICAS.md`, entre marcadores. **A razão tem data:** o painel era escrito à mão, datava-se de **29/09**, e a revisão do repositório mediu que **nenhuma das suas cifras estava certa** — dizia 83 sub-eventos (85), 61 em fonte primária (68), 66 PDFs (65), *oito passos* (catorze), e **49 registros num "Caderno de evidências" que não existe como arquivo algum**. E uma linha era falsa em sentido perigoso: *"sem remoto configurado"*, quando o remoto é **público** — que é a premissa de toda a decisão de distribuição de 21/10. **Nenhuma cifra dele é digitada, e os números de passo que ele cita são lidos de `ciclo.sh`** — número de passo é a cifra que mais apodrece aqui, de oito a catorze em dezenove dias. Duas provas negativas, e a primeira é de procedência: **cifra que não sai de `medir()` não entra nas células**, e ela pegou uma `4242` plantada. Não repete as listas de tarefas e decisões: aponta para as seções irmãs. |
| `gerar_decisoes.py` | **Passo 4 do ciclo, desde 27/10/2026 (item 90).** `data/decisoes_abertas.json` → a seção **Decisões pendentes** de `../docs/PENDENCIAS-ANALITICAS.md`, entre marcadores HTML. **Irmão do passo 3:** um gera as TAREFAS abertas a partir do campo `estado`, este gera as DECISÕES do mesmo jeito. **A razão tem data:** em 25/10/2026 a colheita das seções *"O que isto deixa"* de cada item devolveu **oito pendências já resolvidas por itens posteriores** — aquelas seções são **instantâneos datados**, e o defeito não era a prosa delas, era **não haver um lugar único onde virar o bit**. Fechar uma decisão passou a ser virar um campo, e a contagem e a frase de natureza acompanham. **Guarda G-A:** o ponteiro de seção de cada decisão tem de **existir** na agenda — ponteiro quebrado é a forma que o apodrecimento toma aqui, e ponteiro para o nada é pior que pendência esquecida, porque parece verificável. Três provas negativas. **Limite declarado:** conserta a cópia, não o juízo — não detecta sozinho que uma decisão foi resolvida noutro item. |
| `gerar_ordem_de_ataque.py` | `data/ordem_de_ataque.json` → a seção **Ordem de ataque** de `../docs/PENDENCIAS-ANALITICAS.md`, entre marcadores HTML. Escreve **só** dentro do bloco e prova por `assert` que o resto do arquivo não mudou. A seção em que cada tarefa aparece sai do campo `estado`, e as cifras saem de medição: as da camada A pela função `estado()` de `localizar_camada_a.py` — importada, não reimplementada —, as de corpus do `MANIFESTO-CORPUS.csv`. Cifra que exigiria rede fica em `medidos_a_mao`, e o bloco **imprime a data em que foi medida**. `--chaves` lista o que se pode citar como `{{chave}}`; `--autoteste` roda **seis** provas negativas. **Nasceu porque aquela tabela envelheceu três vezes em dezesseis dias** — ver `../docs/PENDENCIAS-ANALITICAS.md`, item 49. **E envelheceu a quarta vez em 22/10/2026, por onde o gerador não media:** a prosa de cada linha de tarefa era texto declarado, e duas linhas ficaram falsas por catorze dias. Daí vieram duas mudanças (item 78). **(i) O censo é único:** `medir_corpus` deixou de ler a chave `lidas` do ledger — um segundo censo de estado de leitura, declarado à mão — e passou a derivar de `gerar_registro_leitura.censo()`, **importado e não reimplementado**, medindo dois predicados em vez de um, porque a chave antiga chamava de *lidas* as peças que listava por *ancorarem registro*. **(ii) G4:** nenhum texto do ledger pode afirmar não-leitura de peça cujo estado é de leitura — mesmo `exame_de_prosa` da G2, e ela aponta `ledger/tarefa N`, a **fonte** que se edita, em vez de um número de linha do arquivo gerado. **A G4 PASSOU A VIGIAR OS DOIS LEDGERS em 27/10/2026 (item 93).** Ela recebia só o ledger das tarefas como argumento, e `data/decisoes_abertas.json` nasceu um dia antes: **guarda escrita para um artefato não cresce sozinha quando nasce o irmão dele.** E o ledger das decisões é justamente onde afirmação de leitura mora — ele fala das peças `NAO_LIDO`, de Beach e Pedersen — **lido em parte**, capítulos 1 a 3 e o Apêndice A, com o 4 ao 8 ainda por ler — e das seis peças da coletânea que seguem fechadas. Com `assert` contra escopo vazio. |
| `verificar_integridade.py` | **Oito** checagens **estruturais** — eram seis até 08/10/2026; a 7 pega nome de mecanismo retirado e a 8 confere corpus × manifesto por SHA-256. Desde 16/10/2026 a **1** também confere se `metadados.colunas_codebook` declara o mesmo esquema que o gerador usa, e a **4** cobre `autonomia_movimento`: valor fora do vocabulário derruba, e **valor afirmativo sem `fonte_pagina` derruba** — codificação sem folha é a âncora que parece âncora. Desde 16/10/2026 a **5** também **resolve** o localizador estrutural: todo `§Seção` citado em `fonte_pagina` tem de existir como cabeçalho no arquivo não-PDF vinculado, porque `conferir_paginas.py` abre PDF e seção com nome errado passaria para sempre; e a **8** passou a cobrir as âncoras não-PDF, importando do gerador do manifesto a regra de quais são. Ver a ressalva abaixo. **CHECAGEM 9, desde 25/10/2026 (item 86) — classe inferior com âncora documental diz por quê:** nasceu do que o item 83 revelou, que o critério de `Confirmado em fonte primária` vivia em prosa dentro de PT-01A e nunca tinha sido escrito no vocabulário; escrito, promoveu **seis** registros, o dobro do que a pendência nomeava. **A guarda não decide a classe** — duas das três condições não são decidíveis por máquina: *"a peça do próprio ato"* é semântico (PT-27 ancora a CPMI, que **cita** outra peça) e *"insuficiência pendente"* é juízo de prosa. Ela exige que o **desvio seja explicado**: registro em `Confirmado` que ancore peça documental com localizador que a aponte traz a marca `CLASSE NÃO PRIMÁRIA:`. **Uma marca, não uma lista** — lista de marcas é o que deixou a checagem 7 cega à caixa e a G2 sem a forma coletiva da negação. **Limite declarado:** não alcança quem cita por localizador estrutural, porque `pares()` não cede numeral para `inteiro teor` nem para `§seção` — PT-01A, PT-19A e PT-38 caem fora, e os três declaram de todo modo. Alcance medido: **seis** registros. |
| `gerar_registro_leitura.py` | **Passo 6 do ciclo, desde 21/10/2026, a pedido do pesquisador, e a razão tem data:** horas antes eu havia relatado seis verbetes como *"lidos-a-ler"* quando os seis estavam **lidos**, por copiar uma lista de 30/09 do documento que **pedia** a leitura em vez do que a **registrava**. Emite `../docs/referencial/05_REGISTRO-DE-LEITURA.md`. **A maior parte do estado é MEDIDA, não declarada:** das 69 peças do manifesto, 43 ancoram registro com `fonte_pagina` e o passo 9 confere a transcrição contra a folha — leitura parcial demonstrável. As 26 que não ancoram têm o estado em `../data/estado_de_leitura.json`, que é **dado e não prosa**. Três guardas: **G1** cobertura nos dois sentidos — e ela pegou quatro caminhos que eu errei na própria declaração; **G2** coerência de prosa — nenhum documento de `docs/` afirma não-leitura de peça lida, e **ela pegou duas asserções que eu escrevi na mesma sessão e que a leitura tornou falsas horas depois**; **G3** procedência — peça declarada lida diz onde a leitura está registrada, e o arquivo existe. Ver item 75. **REVISTA EM 22/10/2026 (item 78), em três pontos, e os três por medição.** (i) `MARCAS_NAO_LEITURA` ganhou a **forma coletiva** da negação: *"nenhuma lida"* não estava na lista, e por isso uma linha que a G2 vigiava não foi reprovada — **não foi examinada**. (ii) A liberação passou a ser por **proximidade** (`JANELA_RESSALVA`, **200 caracteres medidos**) em vez de por linha: numa linha de 7.268 caracteres, um `~~` remoto dava anistia ao parágrafo inteiro. A janela saiu de medir as 119 afirmações de não-leitura do repositório — as legítimas chegam a 193 caracteres da sua ressalva e a seguinte está a 262. (iii) A G2 **deixou de vigiar a própria saída**: `emite()` grava a tabela de incoerências dentro dela, e a primeira acusação verdadeira fez a rodada seguinte acusar o relatório. O censo virou `censo()`, importável, e a ordem de ataque passou a usá-lo. **A G2 PASSOU A VIGIAR `reports/` em 27/10/2026 (item 93).** Ela nasceu em 21/10 olhando `docs/`, e o relatório de pesquisa, a auditoria de fontes e a tabela-espelho ficavam fora — **dois dos três são GERADOS, e isso torna a vigilância mais útil, não menos:** afirmação falsa ali é defeito do gerador, e defeito de gerador se repete a cada rodada. Medido antes de estender: **zero incoerências em 1.038 linhas** — de modo que o risco não era conserto de conteúdo, era **guarda inerte**, e há `assert` que reprova se o glob secar. **E AOS MANUAIS E AO INVENTÁRIO em 27/10/2026 (item 94).** O escopo da G2 passou a seis famílias nomeadas num `assert`, de modo que **família que sai do escopo derruba o ciclo** em vez de encolher a vigilância em silêncio. Medido antes: zero no README, zero na licença, **zero no inventário de fontes — que era onde eu mais esperava achado, porque ele declara leitura peça por peça** — e **uma no manual dos scripts, que era texto meu de uma hora antes**: a frase que descrevia a extensão anterior desta guarda dizia *"os capítulos não lidos de Beach e Pedersen"* sem a qualificação de que a peça é `LIDO_PARCIAL`. Corrigida pelo padrão da casa — a frase passou a dizer o recorte. **Cinco provas negativas, uma por família e uma de desenho.** |
| `gerar_grade_enquadramento.py` | **Passo 5 do ciclo, desde 21/10/2026, a pedido do pesquisador.** Emite `../docs/referencial/02_GRADE-FUNCIONAL-ENQUADRAMENTO.md`: a classificação dos 85 campos `framing_narrativa` nas três tarefas centrais de enquadramento de Snow, Vliegenthart e Ketelaars (2019, p. 396-397 impressas), mais contraquadro e *não-é-quadro*. **A classificação é INFERÊNCIA declarada**, registro por registro, e vive no dicionário `G` do script — versionada e auditável; **as contagens saem dela**, nunca da cabeça. Nada disto entra no codebook: criar campo é decisão do pesquisador. Está no ciclo pelas **três guardas internas** — todo id classificado, `0` casando com campo realmente vazio nos dois sentidos, e a soma por ator fechando com o total que tem quadro. A terceira pegou um defeito meu na primeira execução. Ver item 74. |
| `gerar_tabela_espelho.py` | **Passo 4 do ciclo, desde 20/10/2026, a pedido do pesquisador.** Emite `../reports/TABELA-ESPELHO-EVENTOS.md` (scanável) e `../data/processed/tabela_espelho_eventos.csv` (completa, 32 colunas): cada registro do codebook ao lado do que a cronologia interativa exibe dele, com o **estado do espelho** campo por campo. Responde o que o ciclo não respondia — *as figuras ainda dizem o que o codebook diz?* `BLOCO`, `campo`, `CLASSE` e `COMPOSTOS` são **importados** de `conferir_figuras.py`, não reimplementados. **Não cobra igualdade de prosa**, porque `mec` difere em 100% por desenho — a figura precisa de frase legível e o campo carrega a prosa de auditoria; cobra o **NOME** do mecanismo, recortado até o primeiro `:`, travessão ou ponto. Em ponto **composto** a cobrança é de **continência**, não de prefixo: o nome de cada registro tem de aparecer no rótulo, porque o rótulo enumera um mecanismo por registro (decisão do pesquisador, 21/10/2026). `DIVERGENCIAS_BASE` era **17** em 20/10 e é **0** desde 21/10, frente F10: deixou de ser tolerância e passou a ser **proibição** — qualquer nome de mecanismo que a figura escreva diferente do codebook derruba o ciclo, sem lista a manter. Ver itens 69 e 70. |
| `gerar_diades.py` | **Passo 7 do ciclo, desde 29/10/2026, por encaminhamento do pesquisador.** Emite `../reports/TABELA-DIADES.md`: um par de registros por seção, com data, fase, ator, repertório e enquadramento dos dois lados, lidos do codebook sem intermediação. **A única afirmação nova é o PAR**, e ela vive no marcador `DÍADE: PT-XX` de `mecanismo_causal` — **não há campo novo no esquema**, e a razão é medição: em 29/10, 58 dos 87 registros já remetiam a outro, com 226 remissões em quatro campos, de modo que o que faltava era **tipo e reciprocidade**, não um campo. **A guarda pergunta duas coisas, e a segunda é a que importa:** o id existe, e **a declaração é recíproca** — se A declara díade com B, B tem de declarar com A. Ponteiro confere existência; **reciprocidade confere que a relação foi pensada dos dois lados**, e é a diferença entre *vide também* e uma afirmação sobre a estrutura do conflito. **Três provas negativas:** id inexistente, declaração de um lado só, e díade consigo mesmo. **DOIS SENTIDOS DE `DÍADE` NO APARATO, e eles não se confundem:** a desta tabela é **inter-registro**; a da grade funcional é **intra-registro** — um registro cujo `framing_narrativa` carrega dois quadros em disputa, como PT-03D, que por isso **não** entra aqui. A teoria é o verbete *Movement/countermovement dynamics* (Dillard, 2013, f. 391-393), lido no mesmo dia. Ver o item 104. |
| `conferir_figuras.py` | As duas peças de `reports/figures/` contra o codebook: cobertura dos registros, selo de status, procedência e cifras já retiradas. Ver a segunda ressalva. |
| `conferir_relatorio.py` | `reports/process_tracing_8jan_relatorio.md` contra o codebook: cobertura da tabela da Etapa 2, páginas citadas × `fonte_pagina`, cifras retiradas e caminhos citados. Ver a segunda ressalva. |
| `conferir_paginas.py` | Abre o PDF na página citada e procura a transcrição. Desde 18/10/2026 **segmento que localiza por estrutura interna não cede numeral** — `ementa itens 2-4` eram lidos como as folhas 2, 3 e 4 —, e os registros que citam por `inteiro teor`, `peça integral` ou seção passaram a ser **nomeados e contados** em vez de desaparecer da saída: `SEM_PAGINA_EXTRAIVEL_BASE` é 5, e o sexto derruba. Ver item 64. **A única checagem que lê a fonte.** Casa por janela de 90, 60 ou 40 caracteres, porque hifenização e ligadura quebram o casamento literal — e **classifica a causa de cada divergência** em vez de afrouxar: pontuação terminal, interpolação entre colchetes, quebra de página (com ou sem o aparato da folha no meio) e marcador de nota de rodapé. **O resíduo sem causa classificada tem linha de base ZERO** (`PARCIAIS_BASE`), e o ciclo cai se subir. Desde 15/10/2026 o localizador **prefere a folha que confere por inteiro**: antes creditava a âncora ao primeiro documento com qualquer janela de 40 caracteres, e as peças do corpus se citam entre si — ver `../docs/PENDENCIAS-ANALITICAS.md`, item 52. E porque preferência só decide quando há diferença, ele devolve também **os documentos empatados na classe vencedora**: com `EMPATES_BASE = 0`, o primeiro fragmento cuja âncora for escolhida pela **ordem de `fonte_pagina`**, e não pelo texto, derruba o ciclo. Medido em 234 fragmentos, item 53. **GUARDA NOVA EM 22/10/2026 — as meias-âncoras (`MEIAS_ANCORAS_BASE = 0`, item 82):** a aspa que sustenta uma afirmação do registro pode viver em `nota_auditoria` ou `status_verificacao`, campos que autorizam a prosa e que **nenhuma guarda conferia contra a folha**, porque este passo localiza transcrição de `fonte_trecho`. A guarda testa a aspa de nota contra as folhas que o registro **já** ancora — as mesmas que este passo abre, em `_cache` —, e por isso custa **+0,7 s em 19 s, cerca de 4%**. O detector usa `casa()` e não `confere_integral()`, de propósito: aspa **composta por junção** confere `parcial` e escaparia do segundo. **Guarda detecta; quem promove confere por inteiro.** Deduplica por aspa, porque a prova negativa acusou 2 onde havia 1. **Não há lista de dispensa:** aspa nova que confira faz o ciclo cair, e as saídas são promovê-la ou subir a base dizendo por quê. Três provas negativas, e a terceira **declara o limite**: folha que o registro não ancora não é alcançada — essa é a parte cara da varredura, 205 s para 16 aspas, e não cabe no ciclo. **LÊ ÂNCORA NÃO-PDF desde 25/10/2026 (item 87).** Três registros citavam a fonte por localizador estrutural num `.md` ou `.html` — PT-01A, PT-03E e PT-19A — e **nunca foram conferidos**: `pares()` não cede numeral para `§seção`, então eles não entravam na fila e contavam na `SEM_PAGINA_EXTRAIVEL_BASE`. **Treze transcrições sem guarda alguma.** `texto_integral()` lê `.md`, `.html`, `.xml` e `.txt`; a unidade ali não é a folha, é o arquivo. **E marcação é aparato do formato, não conteúdo da fonte:** 4 das 13 só passaram a conferir quando a marcação inline do Markdown saiu, porque o arquivo traz `**185 anúncios**` no meio da frase — é o mesmo que o leitor de HTML já fazia com tags, um formato adiante. **Resultado:** `confirmados` de 74 a **77**, `SEM_PAGINA_EXTRAIVEL_BASE` de 6 a **3**, e as **três exceções de PT-08 saíram** — o comentário delas pedia exatamente esta correção. **Permanecem 3 fora do alcance por outra razão:** PT-06B, PT-38 e PT-56 citam PDF por `inteiro teor`, e varrer PDF inteiro custa 205 s para 16 aspas. Três provas negativas, e a terceira consertou a própria base: ela **só avisava**, com código de saída zero, enquanto o comentário dela afirmava que o sexto faria o ciclo cair. **CACHE DE TEXTO POR FOLHA desde 25/10/2026 (item 88).** Três registros citam PDF por `inteiro teor` e o conferidor sabia abrir a peça **sem saber onde olhar**; varrer as 2.874 folhas custou **151 s** medidos — por rodada, inviável, e sem varredura a afirmação deles ficava inguardável. `folhas_da_peca()` guarda o texto reduzido de cada folha em `../data/cache/folhas/`, gzipado, **1,7 MB** nas cinco peças: segunda leitura em processo novo em **0,27 s**, e o ciclo passou de ~40 s a **43 s**. **A chave tem duas partes, e a segunda é a que importa:** o SHA-256 do PDF, que a checagem 8 já vigia, **e `RECEITA_EXTRACAO`** — `texto_pagina` concatena três leituras e normaliza, e **cache que sobrevive a uma mudança no extrator é cache que mente**; mexer em `texto_pagina`, `_mupdf` ou `norm_busca` obriga a subir o número. **A busca integral vale SÓ onde o registro cita a peça inteira** — aplicada a todo fragmento perdido, resgataria âncora creditada à folha errada, que é o defeito do item 52. O cache é derivado e está no `.gitignore`: some sem perda. Quatro provas negativas, e duas nasceram daí — `INTEIRO_TEOR_SEM_ACHADO_BASE = 5` e a regra **total zero nunca é OK**. **GUARDA DA EXCEÇÃO OCIOSA desde 27/10/2026 (`OCIOSAS_BASE = 0`, item 92).** Listada desde 87.5: nada avisava quando uma entrada de `EXCECOES` deixava de ser usada — as três de PT-08 saíram em 25/10 **porque eu fui olhar**. **E exceção obsoleta é pior que pendência esquecida, porque ela continua dispensando:** a chave é (registro, prefixo), e se a transcrição que ela cobria for reescrita mantendo o começo, **a nova passa pela dispensa velha sem ninguém conferir**. `excecoes_usadas` deixou de ser contador e passou a ser **conjunto de chaves** — só se pode perguntar quais sobraram sabendo quais foram usadas. **Roda só em `--todos`**, pelo precedente de `PARCIAIS_BASE` e `EMPATES_BASE`: o modo amostral abre doze registros e deixaria a maioria sem exercício, e acusá-las ali seria ruído. Medido antes de construir: **as sete estão em uso**, e a base é genuinamente zero. Duas provas negativas, a segunda sobre o limite. **E ELE PASSOU A HOSPEDAR A CLASSIFICAÇÃO DOS CAMPOS em 29/10/2026 (item 106)**, que é o conserto de um padrão que cegou duas guardas em três dias. `NAO_PROSA` traz os oito campos que não são prosa **com a razão de cada exclusão**; `CAMPO_BASE` é `fonte_trecho`, que não é exclusão e sim o campo conferido; e `CAMPOS_DE_PROSA` é **derivado** — a lista deixou de existir. **O `assert` é o coração:** `confere_esquema()` compara a classificação contra as chaves do **próprio registro no JSON**, e roda nos 87 registros no passo 9 e no 13 — de modo que **o esquema não pode crescer em silêncio** e a guarda seguinte não pode nascer cega. **Não deriva de `CABECALHOS`** porque aquele constante vive em `gerar_codebook.py`, que importa `openpyxl`, e acoplar um conferidor a biblioteca de planilha seria pior que o problema. Consomem a classificação: a guarda das meias-âncoras aqui, a checagem 6 da integridade, o marcador de díade e o varredor de `fonte_pagina`. |
| `desenhar_campo.py` | O campo multiorganizacional do episódio: sistemas de aliança e de conflito em relação a um **ator focal declarado**, porque campo é sempre de alguém e o codebook é neutro quanto ao ator. Emite `data/processed/campo_multiorganizacional.csv` e, do mesmo `ENTIDADES`, o desenho em `reports/figures/figura_campo_multiorganizacional.svg` e a página `reports/figures/campo_multiorganizacional.html`. **A figura sai do gerador, não da mão** — é por isso que ela não pode divergir da planilha, e é por isso que `conferir_figuras.py` não a confere: aquele script existe para as duas peças da cronologia, que são feitas à mão. A pasta passou a ter os dois regimes. Cada entidade declara os registros e o campo do codebook que a sustentam, e `--autoteste` exige que o fragmento ocorra literalmente ali — com prova negativa por injeção de defeito. **É o passo 8/9 do ciclo.** |
| `conferir_hipoteses.py` | `../docs/analise/11_HIPOTESES-RIVAIS-PT-28.md` contra o codebook: cada linha de tabela que cita um registro tem de citar página que aquele registro ancora, **e no documento-fonte certo** — "Cappelli: 679" é reprovado quando a página é do CPMI. Não abre PDF; a pergunta é anterior. **Passo 9/9 do ciclo.** |
| `gerar_manifesto_corpus.py` | **Fora do ciclo** — regere `Fontes/MANIFESTO-CORPUS.csv`, que a checagem 8 confere: caminho, **SHA-256**, páginas, bytes, classe de licença lida no arquivo e rota de obtenção. É o que mantém a pesquisa verificável sem ser redistribuível, e **65 peças desde 16/10/2026** — 63 PDFs por varredura e as **âncoras não-PDF lidas do `fonte_local` do codebook**, não de lista à mão. Rode-o depois de mexer no corpus ou em `fonte_local`; o ciclo não o roda. |
| `auditar_licencas.py` | **Fora do ciclo** (tarefa 15) — lê o que **cada arquivo declara sobre a própria redistribuição**, nas seis primeiras e três últimas folhas, que é onde a licença vive. Devolve `CC` (com a variante), `ABERTA`, `RESERVADA` ou `SEM` — e **`SEM` não é livre**: é desconhecido, e desconhecido conta como reservado por omissão. Não infere licença do editor nem do registro de acesso aberto, e a razão está no cabeçalho: o OpenAlex declarava Rich (2021) como OURO e a peça está à venda em livraria. É de onde `gerar_manifesto_corpus.py` importa `classifica` e `FORA_DA_DOCUMENTAL` — a linha de corte da contagem documental não é reimplementada em lugar nenhum. |
| `exportar_aparato.py` | **Fora do ciclo, e não publica** (tarefa 15). Monta num diretório à parte um repositório **sem histórico** com só texto e código, e **se recusa a terminar** se qualquer peça não redistribuível tiver escapado — segurança por construção, conferida contra o manifesto, não por cuidado de quem executa. A regra é **inclusão por autorização**, não exclusão por caminho: a primeira versão excluía `Fontes/**/*.pdf` e vazou um PDF de 24,7 MB que estava em `.backup_pre_lula/`. **Não cria remoto, não faz commit e não publica** — publicar é irreversível e é ato do pesquisador. |
| `gerar_catalogo_imprensa.py` | **Fora do ciclo, e instrumento SEPARADO do codebook** — não alimenta o process tracing nem a cronologia. Cataloga as **atribuições de número de manifestantes na imprensa**, e serve a duas coisas: aparato de conferência e material para analisar como os veículos disputam o processo político **pela via do número**. O codebook mantém apenas os números do documento legal. Emite `data/processed/CATALOGO-IMPRENSA-MULTIDAO-8JAN.xlsx`. |
| `rotas_camada_a.py` | **Fora do ciclo** (tarefa 17) — **não baixa nada**: responde só, para cada pendente da camada A, **quais depósitos existem**. Existe porque `localizar_camada_a.py` guardava apenas o `best_oa_location` do OpenAlex, e foi o campo `locations` — **todos** os depósitos, não o melhor — que revelou Mayntz (2004) integral no MPG.PuRe depois de a peça ter sido dada como sem arquivo. Emite `scripts/locais.jsonl`. |
| `baixar_fontes.sh` | Comandos de coleta do que falta. Não baixa nada sozinho: cada peça é um alvo nomeado. |
| `historico/migrar_esquema16.py` | Rodada única de 16/08/2026 (12 → 16 campos + correções de auditoria). Idempotente. Mantido como registro da decisão, não faz parte do ciclo. |
| `historico/migrar_esquema17.py` | Rodada única de 16/10/2026 (16 → 17 campos: entra `autonomia_movimento`, por decisão do pesquisador). Idempotente — reexecutar não duplica campo nem revisão. Codificou **um** registro, PT-06, cujo lastro já estava conferido; os outros 82 entraram vazios de propósito, e o vazio é contado no passo 4. |
| `varrer_fonte_pagina.py` | **Triagem, fora do ciclo.** Compara as páginas citadas na prosa dos registros (`fonte_trecho`, `mecanismo_causal`, `status_verificacao`, `nota_auditoria`) com o campo estruturado `fonte_pagina`, e imprime o trecho em volta de cada divergência. Nem todo achado é lacuna — ver a terceira ressalva. |
| `verificar_dois_sinteses.py` | **Triagem, fora do ciclo.** Os DOIs das sínteses LeapSpace no CrossRef e, em 404, na DataCite. Emite `data/processed/dois_sinteses_leapspace.csv` com metadados, e confere se o título registrado casa com o que a síntese declara. **Imprime a contagem por arquivo e cobra as duas contagens escritas à mão** — a de `PROCEDENCIA` e a do inventário de fontes —, saindo com código 1 se divergirem. Ver a quarta ressalva. |
| `triar_dois.py` | **Triagem, fora do ciclo.** Classifica os DOIs verificados em três camadas contra os mecanismos que o codebook afirma, e emite `data/processed/triagem_dois.csv` com o uso declarado item por item. A chave é fragmento de título com número de correspondências esperado — aborta se divergir, para nenhuma referência ser inventada por engano de digitação. |
| `historico/recodificar_*.py` · `historico/inserir_*.py` · `historico/migrar_*.py` | **As 25 migrações de uso único**, uma por rodada, cada uma com o achado que a motivou no cabeçalho. Registro do que foi feito, fora do ciclo. **Mudaram de lugar em 14/10/2026**: estavam misturadas aos scripts vivos nesta pasta, e quem abria `scripts/` não distinguia o que roda do que já rodou. **Não se reexecutam** — cada uma afirma por `assert` um estado anterior que já não existe, e é isso que as torna seguras de guardar. |

## Três ressalvas que importam

### 1. O estrutural não pega vínculo errado

`verificar_integridade.py` **não pega vínculo apontando para o documento errado.**
Ele deriva o código do documento a partir do próprio vínculo, então um registro
que aponta para a peça errada passa como coerente — está consistente consigo
mesmo, e errado.

Foi exatamente o que aconteceu com **PT-28**: o texto citava "Relatório Final da
CPMI, p. 657" e o vínculo apontava para o acórdão da AP 2668. A frase está na
CPMI p. 657 e é ausente das 1.991 páginas do acórdão. Só `conferir_paginas.py`
revelou o descasamento.

**Consequência prática: rode os dois.** O estrutural é barato e roda em segundos;
o amostral é lento e cobre 12 registros por vez. Nenhum substitui o outro.

Desde **25/09/2026** o amostral é estrito: toda transcrição do registro precisa
ser localizada em alguma página listada, e não basta uma casar. Ele também passou
a listar as **páginas que nenhuma transcrição alcança** — aviso, não falha, e o
primeiro lugar a olhar quando uma âncora estiver sob suspeita. Duas ressalvas de
leitura estão no cabeçalho do próprio script, e uma delas retifica um diagnóstico
que este projeto vinha repetindo sobre PT-59.

### 2. Três peças não são geradas, e envelhecem em silêncio

As duas figuras de `reports/figures/` e o relatório de pesquisa reproduzem
números do codebook **à mão**. A cronologia interativa carrega uma cópia dos 82
registros dentro do `<script>`; o SVG é rótulo por rótulo em coordenadas
absolutas; o relatório traz a tabela da Etapa 2 e a cifra em prosa. Editar o
JSON não atualiza nenhum dos três.

O custo apareceu duas vezes, do mesmo jeito. Em **11/09/2026** o relatório
carregava "mais de 1.600 ações penais" e "1.402 condenados", quase um mês
depois de o codebook ter corrigido os dois. Em **25/09/2026** as figuras
traziam treze divergências, seis delas cifras retiradas — e a correção de
11/09, que alcançara a §3.2 do relatório, tinha deixado a §2.1 com a marcha de
"9 km". Nos três casos o JSON estava certo e a peça derivada, errada.

`conferir_figuras.py` e `conferir_relatorio.py` existem para que a próxima
defasagem apareça no ciclo, e não num parecer.

**O que os dois fazem é comparar o que a peça declara** — ids, páginas citadas,
selo de status, cifras já retiradas, caminhos — contra o codebook. **O que não
fazem é ler a prosa:** uma cifra nova e errada passa, e uma afirmação causal sem
lastro passa. Eles pegam regressão declarada, não erro de interpretação, e a
correção continua manual nas três peças.

Um detalhe do `conferir_relatorio.py` que vale conhecer antes de editar o
relatório: a busca por cifra morta **absolve a linha que também traz a cifra
correta**. É o que permite ao texto narrar a própria história — "1.335, não
'mais de 1.600'" — sem disparar alarme. Se você escrever a cifra antiga longe
da nova, ele reclama, e está certo em reclamar.

### 3. `fonte_pagina` e a prosa podem divergir

O campo `fonte_pagina` é o que as ferramentas leem. A prosa dos registros —
`fonte_trecho`, `mecanismo_causal`, `status_verificacao`, `nota_auditoria` —
também cita páginas, e nada no ciclo compara as duas. Em 25/09/2026 divergiram: PT-10 ancorava "CPMI:
999, 1023" e a própria prosa dizia "p. 999, 1021 e 1023". A p. 1021 sustenta a
cifra dos bloqueios e tinha sumido do campo estruturado.

Aquilo apareceu de raspão, porque o relatório citava a página a mais. Onde
nenhuma peça derivada cita, ninguém vê. `varrer_fonte_pagina.py` olha os 82 de
uma vez, e na estreia achou mais duas lacunas: a p. 274 da CPMI em PT-15, e dois
documentos inteiros em PT-28 — o Cappelli e o acórdão da AP 2668 — que o
`mecanismo_causal` do registro citava por extenso sem ancorar.

**Ele é triagem, não gate, e por isso fica fora do ciclo.** Boa parte do que
levanta é legítima: página citada para refutar, remissão a outro registro,
menção de passagem a documento que o registro não precisa ancorar. Ele imprime
o trecho em volta de cada achado justamente para que a triagem leve segundos, e
sai com código 0 por padrão — `--estrito` sai com 1 havendo achados, se um dia
você quiser prendê-lo a um gancho.

O limite é de leitura, não de implementação: ele atribui cada "p. N" ao
documento nomeado mais perto, antes dela, e erra quando a prosa volta a um
documento anterior sem renomeá-lo. Duas salvaguardas reduzem o estrago —
páginas já ancoradas sob outro documento do mesmo registro são silenciadas
(`--tudo` mostra quais), e o trecho impresso deixa o engano visível.

### 4. DOI que responde não é DOI bem atribuído

As sínteses de `Fontes/05_Bibliografia-teorica/` são geradas por sistema
automatizado e **não são citáveis** — valem pelos DOIs. Em 29/09/2026 os 411
foram verificados: 408 existem, 3 não.

O achado que interessa é outro. Numa das sínteses, dois capítulos vizinhos do
mesmo manual têm os DOIs deslocados: o que ela atribui a Vaughan
(`10.4324/9780203856949-40`) é o capítulo de O'Halloran, e o que ela atribui a
O'Halloran não existe. **O primeiro responde 200 e passaria como confirmado.** Os identificadores corretos dos
três DOIs quebrados e do par deslocado estão nos dicionários `NAO_EXISTEM` e
`VIZINHOS_TROCADOS` do próprio script, e nas fichas de
`../docs/analise/08_BIBLIOGRAFIA-METODOLOGICA.md`.

A mesma rodada fechou uma **terceira cópia manual de cifra** do projeto, depois
das figuras e do relatório: a contagem de DOIs por síntese estava digitada em
`PROCEDENCIA` e no inventário de fontes, e em 01/09 uma recontagem mudou um dos
dois e não o outro — um DOI de diferença, quatro semanas de pé. O script agora
**imprime a tabela e cobra as duas declarações**, com código de saída 1 quando
divergem. Provado por injeção: 89 posto de volta no inventário reprova, dizendo
qual arquivo e qual número.

Por isso o verificador tem dois eixos, e o segundo procura o título registrado
na janela de texto que antecede o DOI na síntese. Das 444 menções, 435 casam e
9 vão para leitura — oito delas são título traduzido, absolvidas em segundos
pelo trecho que ele imprime. **Nenhum DOI destas sínteses entra na bibliografia
sem os dois eixos**, e a leitura é sempre na fonte, nunca na síntese.

## Dependências

```bash
pip install openpyxl PyPDF2
```

Testado em Python 3.14 no Windows. `curl` e `bash` para o script de coleta —
o Git Bash resolve.

**Nunca use `pdfinfo` para contar páginas destes PDFs**: ele subconta
grosseiramente (relatou 84 páginas para um arquivo de 464). Use `PyPDF2`, como
todos os scripts aqui fazem.
