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

# 5. verifique — falha se algo divergir
python scripts/verificar_integridade.py

# 6. confira as figuras de reports/figures/ contra o codebook
python scripts/conferir_figuras.py

# 7. confira o relatório de pesquisa contra o codebook
python scripts/conferir_relatorio.py

# 8. confira a amostra contra o texto dos PDFs
python scripts/conferir_paginas.py
```

Os passos 3 a 8 são o que `bash scripts/ciclo.sh` roda, nessa ordem. Os passos
5 a 8 devolvem código de saída != 0 em caso de falha, então servem em gancho
de pré-commit.

## Os arquivos

| Script | O que faz |
|:--|:--|
| `gerar_codebook.py` | JSON → `data/processed/`: CSV (UTF-8 com BOM) + XLSX de quatro abas. Guarda `PROCEDENCIA` (procedência de cada arquivo do corpus) e `PENDENCIAS` (fila de coleta). |
| `gerar_auditoria.py` | JSON → `reports/AUDITORIA-FONTES.md`. A narrativa vive no script; as tabelas saem dos dados. |
| `verificar_integridade.py` | Seis checagens **estruturais**. Ver a ressalva abaixo. |
| `conferir_figuras.py` | As duas peças de `reports/figures/` contra o codebook: cobertura dos registros, selo de status, procedência e cifras já retiradas. Ver a segunda ressalva. |
| `conferir_relatorio.py` | `reports/process_tracing_8jan_relatorio.md` contra o codebook: cobertura da tabela da Etapa 2, páginas citadas × `fonte_pagina`, cifras retiradas e caminhos citados. Ver a segunda ressalva. |
| `conferir_paginas.py` | Abre o PDF na página citada e procura a transcrição. **A única checagem que lê a fonte.** |
| `baixar_fontes.sh` | Comandos de coleta do que falta. Não baixa nada sozinho: cada peça é um alvo nomeado. |
| `migrar_esquema16.py` | Rodada única de 16/08/2026 (12 → 16 campos + correções de auditoria). Idempotente. Mantido como registro da decisão, não faz parte do ciclo. |
| `varrer_fonte_pagina.py` | **Triagem, fora do ciclo.** Compara as páginas citadas na prosa dos registros (`fonte_trecho`, `mecanismo_causal`, `status_verificacao`, `nota_auditoria`) com o campo estruturado `fonte_pagina`, e imprime o trecho em volta de cada divergência. Nem todo achado é lacuna — ver a terceira ressalva. |
| `recodificar_*.py` | Migrações já executadas, uma por rodada, cada uma idempotente e com o achado que a motivou no cabeçalho. Registro do que foi feito, fora do ciclo. |

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

## Dependências

```bash
pip install openpyxl PyPDF2
```

Testado em Python 3.14 no Windows. `curl` e `bash` para o script de coleta —
o Git Bash resolve.

**Nunca use `pdfinfo` para contar páginas destes PDFs**: ele subconta
grosseiramente (relatou 84 páginas para um arquivo de 464). Use `PyPDF2`, como
todos os scripts aqui fazem.
