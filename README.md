# Manifestações 8 de Janeiro

Reconstrução cronológico-causal do 8 de janeiro de 2023 por *process tracing*, com marco na Teoria do Processo Político (McAdam, Tarrow, Tilly). O produto central é um codebook de **82 sub-eventos × 16 campos**, ancorado documento a documento e página a página em um corpus de fontes primárias — relatório da CPMI, relatório do interventor federal, denúncia da PGR, acórdãos do STF, TRF-4 e TSE, decisões de execução penal e o balanço do Gabinete do Min. Moraes.

O artigo ainda não foi escrito: por decisão de 16/08/2026, a redação é o último item da fila.

## Como verificar que está tudo de pé

```bash
pip install -r requirements.txt
bash scripts/ciclo.sh
```

O ciclo regenera os formatos derivados, refaz a auditoria e roda as quatro checagens: a estrutural, a das figuras, a do relatório e a amostral contra o texto dos PDFs. Ele falha — com código de saída diferente de zero — se qualquer coisa divergir. Rode-o depois de **toda** alteração no JSON ou no corpus.

## As regras que sustentam o aparato

1. **O JSON é a única fonte da verdade.** `process_tracing_8jan_eventos.json` é o que se edita. CSV e XLSX são gerados e sobrescritos sem aviso.
2. **Toda fonte nova entra com procedência declarada** no dicionário `PROCEDENCIA`, em `scripts/gerar_codebook.py`, e no inventário `Fontes/LEIA-ME_fontes.md`. A terceira checagem falha se um arquivo ficar sem declaração.
3. **Todo número é conferido contra a fonte, nunca contra outra citação dela.** O modo de falha recorrente do projeto é a cifra correta aplicada ao referente errado — aconteceu **dezesseis vezes numeradas** na agenda, e duas vezes mais em 13 e 14/10/2026 — o auditor de licença que leu uma frase contrafactual como declaração (item 47.4) e a identidade por `sha1` que as cópias das figuras declaravam e já não tinham (item 48). Cada caso está registrado em `docs/PENDENCIAS-ANALITICAS.md`.
4. **Nada se afirma sem ter sido lido.** Quando a leitura não foi possível, a peça entra como catalogação de metadados, com a limitação escrita.
5. **Alteração que exige julgamento não se executa por conta própria** — vai para a agenda de pendências e espera decisão do pesquisador.

## Mapa do diretório

A estrutura segue os princípios do padrão *Cookiecutter Data Science* — dado bruto imutável, derivados gerados por script, fluxo em um sentido só. Os diretórios derivados adotam os nomes do padrão; `Fontes/` e `scripts/` mantêm os nomes em português, já citados por 290 referências no JSON, nos scripts e nos documentos, e renomeá-los custaria mais do que a nomenclatura vale.

| Aqui | Papel | Equivalente CCDS |
|:--|:--|:--|
| `Fontes/` | Corpus, **imutável**. **63 PDFs, 12.125 p.** — dos quais **22 PDFs / 6.951 p. são fonte documental**, e o resto é bibliografia teórica e literatura —, mais HTML, arquivamento web e sínteses. Inventário em `Fontes/LEIA-ME_fontes.md`, manifesto gerado em `Fontes/MANIFESTO-CORPUS.csv`. **Estes dois números são a linha de base de 13/10/2026 da checagem 6**, que avisa quando o corpus se move | `data/raw` |
| `process_tracing_8jan_eventos.json` | Codebook — a fonte única da verdade. Fica na raiz porque é a porta de entrada dos dados e o que todo script lê | `data/interim` (curado à mão) |
| `data/processed/` | Derivados, **gerados**: o CSV e o XLSX do codebook, o catálogo da imprensa, a planilha dos 411 DOIs das sínteses e a triagem deles por pertinência. Não editar — a próxima execução sobrescreve | `data/processed` |
| `Caderno-de-evidencias/` | Transcrições literais com página, por registro | `references` |
| `scripts/` | **Só o que roda hoje**: 17 geradores e verificadores. Ver `scripts/LEIA-ME.md` | `src` |
| `scripts/historico/` | As **24 migrações de uso único** já executadas — `recodificar_*`, `inserir_*`, `migrar_*`. Não são parte do ciclo e **não se reexecutam**: cada uma afirma, por `assert`, o estado anterior que já não existe. Ficam como registro de o que mudou o codebook, e quando | `src` |
| `reports/` | `AUDITORIA-FONTES.md`, a auditoria de vínculos, **gerada** | `reports` |
| `reports/figures/` | **O único lugar das figuras**: cadeia causal e campo multiorganizacional, em SVG e HTML. As da cronologia são **escritas à mão** — editar o JSON não as atualiza, e `scripts/conferir_figuras.py` acusa a defasagem; as do campo são geradas por `desenhar_campo.py`. Até 14/10/2026 havia uma cópia em `projeto-pos-doc/figuras/`, declarada byte-idêntica e que **não era** — ver `docs/PENDENCIAS-ANALITICAS.md`, item 48 | `reports/figures` |
| `reports/process_tracing_8jan_relatorio.md` | Relatório de pesquisa, **escrito à mão** — como as figuras, reproduz números do codebook e já ficou para trás duas vezes; `scripts/conferir_relatorio.py` acusa a defasagem | `reports` |
| `docs/Pesquisa-sobre-Mobilizações-de-8-de-Janeiro.md` | Documento-base do projeto, anterior ao process tracing | `docs` |
| `docs/PENDENCIAS-ANALITICAS.md` | **A agenda.** O que está aberto e o que espera decisão sua | `docs` |
| `docs/ESTIMATIVA-MULTIDAO-8JAN.md`, `docs/LEIA-ME_metodologia_verificacao.md` | Dossiês de método e de decisão sobre cifras | `docs` |
| `docs/analise/` | **Os nove dossiês de análise da pesquisa** — bibliografia do projeto e metodológica, o conceito de mecanismo, os verbetes, as hipóteses rivais de PT-28, a camada $T_{-1}$, o bolsonarismo, os livros brasileiros e o comparado do 6 de janeiro. **Estavam em `projeto-pos-doc/` até 14/10/2026**, e não é onde pertenciam: são o caderno de leitura desta pesquisa, não peça de candidatura. Dois deles, `11_` e `12_`, são lidos pelo ciclo — `conferir_hipoteses.py` exige que toda página citada neles seja ancorada por registro | `docs` |
| `docs/historico/` | Relatórios de sessão datados, que descrevem estados **anteriores** do repositório. Não se atualizam: reescrevê-los falsificaria o registro | `docs` |
| `data/external/levantamento_8_de_janeiro_*` | Levantamento bibliográfico original, coletado à mão | `data/external` |
| `data/external/crossref_cache.jsonl` | O que o CrossRef e a DataCite responderam sobre cada DOI, em 29/09/2026. Cache e, ao mesmo tempo, registro da consulta | `data/external` |
| `projeto-pos-doc/` | **Só o dossiê de candidatura ao PIPD/CAPES**: projeto, proposta de disciplina, carta, roteiro de Lattes, checklist, registro de revisão, o edital e os dois arquivos de submissão. Lê do repositório, não escreve nele. **Era também onde estavam os nove dossiês de análise e uma cópia das figuras**, e deixou de ser em 14/10/2026 | `reports` |
| `.backup_pre_lula/` | Cópias manuais anteriores ao controle de versão — **19 estados do JSON** e os derivados de cada um. Redundantes desde que o histórico do git existe, e tirá-las do controle de versão é decisão do pesquisador | — |

Uma migração antiga, `scripts/historico/migrar_esquema16.py`, ainda aponta para o CSV na raiz. É registro do que foi executado em 16/08/2026, não parte do ciclo, e por isso não foi reescrita.

## Por onde começar a ler

1. `docs/PENDENCIAS-ANALITICAS.md` — o painel de estado e a ordem de ataque.
2. `reports/AUDITORIA-FONTES.md` — onde está o documento que sustenta cada afirmação, e em que página.
3. `scripts/LEIA-ME.md` — o ciclo, os scripts e as duas ressalvas que importam: a checagem estrutural não pega vínculo que aponta para o documento errado, e três peças (as duas figuras e o relatório) não são geradas a partir do JSON.

## Limites declarados do corpus

Laudos periciais do Instituto de Criminalística (acesso restrito), o inteiro teor da sentença de primeira instância de Moro (suprido pela transcrição no acórdão do TRF-4, p. 395) e o acórdão completo do HC 126.292 (documentado via ADC 43/44/54). Nenhum deles bloqueia a redação.

## Fontes de terceiros

O corpus reúne documentos públicos de órgãos oficiais e peças de imprensa arquivadas contra *link rot*, cada um com origem e termos declarados no inventário. São reproduzidos aqui para fins de pesquisa; os direitos permanecem de seus titulares.
