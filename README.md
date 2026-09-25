# Manifestações 8 de Janeiro

Reconstrução cronológico-causal do 8 de janeiro de 2023 por *process tracing*, com marco na Teoria do Processo Político (McAdam, Tarrow, Tilly). O produto central é um codebook de **82 sub-eventos × 16 campos**, ancorado documento a documento e página a página em um corpus de fontes primárias — relatório da CPMI, relatório do interventor federal, denúncia da PGR, acórdãos do STF, TRF-4 e TSE, decisões de execução penal e o balanço do Gabinete do Min. Moraes.

O artigo ainda não foi escrito: por decisão de 16/08/2026, a redação é o último item da fila.

## Como verificar que está tudo de pé

```bash
pip install -r requirements.txt
bash scripts/ciclo.sh
```

O ciclo regenera os formatos derivados, refaz a auditoria e roda as três checagens: a estrutural, a das figuras e a amostral contra o texto dos PDFs. Ele falha — com código de saída diferente de zero — se qualquer coisa divergir. Rode-o depois de **toda** alteração no JSON ou no corpus.

## As regras que sustentam o aparato

1. **O JSON é a única fonte da verdade.** `process_tracing_8jan_eventos.json` é o que se edita. CSV e XLSX são gerados e sobrescritos sem aviso.
2. **Toda fonte nova entra com procedência declarada** no dicionário `PROCEDENCIA`, em `scripts/gerar_codebook.py`, e no inventário `Fontes/LEIA-ME_fontes.md`. A terceira checagem falha se um arquivo ficar sem declaração.
3. **Todo número é conferido contra a fonte, nunca contra outra citação dela.** O modo de falha recorrente do projeto é a cifra correta aplicada ao referente errado — aconteceu cinco vezes, e cada caso está registrado em `docs/PENDENCIAS-ANALITICAS.md`.
4. **Nada se afirma sem ter sido lido.** Quando a leitura não foi possível, a peça entra como catalogação de metadados, com a limitação escrita.
5. **Alteração que exige julgamento não se executa por conta própria** — vai para a agenda de pendências e espera decisão do pesquisador.

## Mapa do diretório

A estrutura segue os princípios do padrão *Cookiecutter Data Science* — dado bruto imutável, derivados gerados por script, fluxo em um sentido só. Os diretórios derivados adotam os nomes do padrão; `Fontes/` e `scripts/` mantêm os nomes em português, já citados por 290 referências no JSON, nos scripts e nos documentos, e renomeá-los custaria mais do que a nomenclatura vale.

| Aqui | Papel | Equivalente CCDS |
|:--|:--|:--|
| `Fontes/` | Corpus documental, **imutável**. 22 PDFs, 6.928 p., mais HTML, arquivamento web e sínteses. Inventário em `Fontes/LEIA-ME_fontes.md` | `data/raw` |
| `process_tracing_8jan_eventos.json` | Codebook — a fonte única da verdade. Fica na raiz porque é a porta de entrada dos dados e o que todo script lê | `data/interim` (curado à mão) |
| `data/processed/` | Derivados, **gerados**: o CSV e o XLSX do codebook e o catálogo da imprensa. Não editar — a próxima execução sobrescreve | `data/processed` |
| `Caderno-de-evidencias/` | Transcrições literais com página, por registro | `references` |
| `scripts/` | Geradores, verificadores e as migrações já executadas. Ver `scripts/LEIA-ME.md` | `src` |
| `reports/` | `AUDITORIA-FONTES.md`, a auditoria de vínculos, **gerada** | `reports` |
| `reports/figures/` | Figura da cadeia causal (SVG) e cronologia navegável (HTML). **Escritas à mão** — editar o JSON não as atualiza; `scripts/conferir_figuras.py` acusa a defasagem | `reports/figures` |
| `reports/process_tracing_8jan_relatorio.md` | Relatório de pesquisa, escrito à mão | `reports` |
| `docs/Pesquisa-sobre-Mobilizações-de-8-de-Janeiro.md` | Documento-base do projeto, anterior ao process tracing | `docs` |
| `docs/PENDENCIAS-ANALITICAS.md` | **A agenda.** O que está aberto e o que espera decisão sua | `docs` |
| `docs/ESTIMATIVA-MULTIDAO-8JAN.md`, `docs/LEIA-ME_metodologia_verificacao.md` | Dossiês de método e de decisão sobre cifras | `docs` |
| `data/external/levantamento_8_de_janeiro_*` | Levantamento bibliográfico original, coletado à mão | `data/external` |
| `projeto-pos-doc/` | Dossiê de candidatura ao PIPD/CAPES. Lê do repositório, não escreve nele | `reports` |
| `.backup_pre_lula/` | Cópias manuais anteriores ao controle de versão. Redundantes desde que o histórico do git existe | — |

Uma migração antiga, `scripts/migrar_esquema16.py`, ainda aponta para o CSV na raiz. É registro do que foi executado em 16/08/2026, não parte do ciclo, e por isso não foi reescrita.

## Por onde começar a ler

1. `docs/PENDENCIAS-ANALITICAS.md` — o painel de estado e a ordem de ataque.
2. `reports/AUDITORIA-FONTES.md` — onde está o documento que sustenta cada afirmação, e em que página.
3. `scripts/LEIA-ME.md` — o ciclo, os scripts e as duas ressalvas que importam: a checagem estrutural não pega vínculo que aponta para o documento errado, e as figuras não são geradas a partir do JSON.

## Limites declarados do corpus

Laudos periciais do Instituto de Criminalística (acesso restrito), o inteiro teor da sentença de primeira instância de Moro (suprido pela transcrição no acórdão do TRF-4, p. 395) e o acórdão completo do HC 126.292 (documentado via ADC 43/44/54). Nenhum deles bloqueia a redação.

## Fontes de terceiros

O corpus reúne documentos públicos de órgãos oficiais e peças de imprensa arquivadas contra *link rot*, cada um com origem e termos declarados no inventário. São reproduzidos aqui para fins de pesquisa; os direitos permanecem de seus titulares.
