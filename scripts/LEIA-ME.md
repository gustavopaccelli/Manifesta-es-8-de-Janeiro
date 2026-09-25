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

# 7. confira a amostra contra o texto dos PDFs
python scripts/conferir_paginas.py
```

Os passos 3 a 7 são o que `bash scripts/ciclo.sh` roda, nessa ordem. Os passos
5, 6 e 7 devolvem código de saída != 0 em caso de falha, então servem em gancho
de pré-commit.

## Os arquivos

| Script | O que faz |
|:--|:--|
| `gerar_codebook.py` | JSON → `data/processed/`: CSV (UTF-8 com BOM) + XLSX de quatro abas. Guarda `PROCEDENCIA` (procedência de cada arquivo do corpus) e `PENDENCIAS` (fila de coleta). |
| `gerar_auditoria.py` | JSON → `reports/AUDITORIA-FONTES.md`. A narrativa vive no script; as tabelas saem dos dados. |
| `verificar_integridade.py` | Seis checagens **estruturais**. Ver a ressalva abaixo. |
| `conferir_figuras.py` | As duas peças de `reports/figures/` contra o codebook: cobertura dos registros, selo de status, procedência e cifras já retiradas. **A única parte do aparato que não é gerada** — ver a segunda ressalva. |
| `conferir_paginas.py` | Abre o PDF na página citada e procura a transcrição. **A única checagem que lê a fonte.** |
| `baixar_fontes.sh` | Comandos de coleta do que falta. Não baixa nada sozinho: cada peça é um alvo nomeado. |
| `migrar_esquema16.py` | Rodada única de 16/08/2026 (12 → 16 campos + correções de auditoria). Idempotente. Mantido como registro da decisão, não faz parte do ciclo. |

## Duas ressalvas que importam

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

### 2. As figuras não são geradas

`reports/figures/` é a única parte do aparato escrita à mão: a cronologia
interativa carrega uma cópia dos 82 registros dentro do `<script>`, e o SVG é
rótulo por rótulo em coordenadas absolutas. Editar o JSON não as atualiza.

Em 25/09/2026 descobriu-se o custo disso: as duas peças ainda traziam sete
cifras retiradas em 16/08 e 11/09 — "+1.600 ações penais", "1.402 condenados",
"~4 mil na Praça", "9 km", "+100 acampamentos", "~1.200 presos" e a prorrogação
de 03/07/2026. Ficaram seis semanas publicadas numa figura que se apresenta como
a codificação completa.

`conferir_figuras.py` existe para que a próxima defasagem apareça no ciclo, e
não num parecer. Ele compara o que as figuras **declaram** — ids, selo de
status, procedência, cifras mortas —, não o conteúdo dos rótulos: uma cifra
nova e errada passa por ele. A correção continua sendo manual, nos dois
arquivos.

## Dependências

```bash
pip install openpyxl PyPDF2
```

Testado em Python 3.14 no Windows. `curl` e `bash` para o script de coleta —
o Git Bash resolve.

**Nunca use `pdfinfo` para contar páginas destes PDFs**: ele subconta
grosseiramente (relatou 84 páginas para um arquivo de 464). Use `PyPDF2`, como
todos os scripts aqui fazem.
