# Etapa 1: inventário do repositório "Manifestações 8 de Janeiro"

Leitura feita em 25/09/2026. O terminal no computador do pesquisador não iniciou, então os arquivos foram listados e trazidos para esta sessão pela ponte de arquivos. A seção 6 separa o que foi lido integralmente, o que foi apenas catalogado e o que não foi aberto.

---

## 1. Estrutura de pastas

```
Manifestações 8 de Janeiro/
├── README.md                         mapa, regras do aparato, por onde começar
├── process_tracing_8jan_eventos.json FONTE ÚNICA DA VERDADE: codebook, 82 sub-eventos × 16 campos
├── requirements.txt, .gitignore, .gitattributes, .git/ (versionado)
├── Caderno-de-evidencias/            transcrições literais da CPMI com página (49 registros)
├── data/
│   ├── external/                     levantamento bibliográfico original (58 refs)
│   └── processed/                    derivados GERADOS: CSV e XLSX do codebook, catálogo da imprensa
├── docs/                             agenda de pendências, dossiês de método, documento-base
├── Fontes/                           corpus IMUTÁVEL: 22 PDFs / 6.928 p. + HTML + sínteses
│   ├── 01_Arco-judicial_2017-2021/   7 acórdãos (STF, TRF-4) + acórdão TSE em HTML
│   ├── 02_T-1_Articulacao/           Denúncia PGR, Pet 12.100, Núcleo 1 (272 p.)
│   ├── 03_T0_8-de-janeiro/           Relatório do Interventor Cappelli (62 p.)
│   ├── 04_T+1_Resposta-institucional/ CPMI (1.333 p.), AP 2668 (1.991 p.), QO, Pet 14.129, EP 169 (×2)
│   ├── 05_Bibliografia-teorica/      2 PDFs de process tracing + 7 sínteses LeapSpace (não citáveis)
│   ├── 06_Lava-Jato-.../             20 referências (18 com DOI)
│   ├── 07_NetLab-UFRJ/               NetLab (Meta Ads) + Manchetômetro/Doxa-IESP-UERJ
│   ├── 08_Imprensa-enquadramento/    preprint Drummond & Manginelli (SciELO Preprints)
│   ├── 09_Arquivamento-web/          7 matérias HTML arquivadas contra link rot
│   ├── 10_Democracia-Inabalada/      livro do STF (2023), folder, balanço do Gabinete Moraes (2026)
│   └── 11_Tese-doutorado/            PACCELLI, tese UFJF 2024 (.docx, ~89 mil palavras)
├── projeto-pos-doc/                  dossiê PIPD/CAPES (lê do repositório, não escreve nele)
├── reports/                          relatório de process tracing, auditoria de fontes, figuras
├── scripts/                          geradores e verificadores (ciclo.sh, gerar_codebook.py, etc.)
└── .backup_pre_lula/                 cópias anteriores ao git, redundantes
```

---

## 2. O que cada arquivo contém (arquivos de trabalho)

| Arquivo | Conteúdo | Papel para o Artigo 1 |
|:--|:--|:--|
| `README.md` | Mapa, 5 regras do aparato (JSON como fonte única; toda cifra conferida contra a fonte; nada afirmado sem leitura) | Regras de rastreabilidade já compatíveis com as suas |
| `process_tracing_8jan_eventos.json` | `metadados` (fases, vocabulário, histórico de revisões) + `eventos` (82 registros; campos: id, data_hora, fase, ator_grupo, repertorio_acao, target_alvo, framing_narrativa, resposta_estatal, mecanismo_causal, fonte_trecho, fonte_url, fonte_local, fonte_pagina, status_verificacao, status_classe, nota_auditoria) | **Espinha empírica do artigo** |
| `docs/PENDENCIAS-ANALITICAS.md` | Agenda com 18 itens; painel de estado de 16/08/2026 | Itens 3, 4, 5 e 6 são exatamente o núcleo do mecanismo (c) |
| `docs/ESTIMATIVA-MULTIDAO-8JAN.md` | Dossiê que retira o "4 mil" e adota faixa de 3.000 a 5.500 (ANTT/Abin; SSP-DF; CPMI p. 374, 637, 643, 695) | Números de T0 |
| `docs/LEIA-ME_metodologia_verificacao.md` | Protocolo CrossRef do levantamento; DOI fabricado corrigido (Amaral 2024) | Protocolo para a Etapa 5 |
| `docs/Pesquisa-sobre-Mobilizações-...md` | Registro de conversa com Gemini que desenhou o projeto. Metodológico, sem dado empírico | Não citável |
| `reports/process_tracing_8jan_relatorio.md` | Relatório de 15,7 mil palavras: reconstrução T-1/T0/T+1, síntese da cadeia causal, "três mecanismos fazem o trabalho causal pesado". Revisão parcial em 11/09/2026 | Base do argumento; a seção de próximos passos está desatualizada (14/08) |
| `reports/AUDITORIA-FONTES.md` | Vínculo registro ↔ documento ↔ página; 74 registros ancorados; 53 transcrições conferidas na página citada, 0 divergências | Rastreabilidade das citações |
| `Caderno-de-evidencias/caderno_CPMI_verbatim.md/.csv` | 49 registros com trecho literal e página da CPMI; o mecanismo atribuído aparece separado ("leitura do analista") | **Fonte direta das citações de T-1 operacional e T0** |
| `data/processed/process_tracing_8jan_codebook.xlsx` | 4 abas: Codebook (82×16), Dicionario, Inventario_Fontes (43 arquivos), Pendencias_Coleta | Derivado do JSON |
| `data/processed/process_tracing_8jan_eventos.csv` | Mesmo conteúdo do JSON, UTF-8 com BOM | Derivado |
| `data/processed/CATALOGO-IMPRENSA-MULTIDAO-8JAN.xlsx` | Cifras de multidão atribuídas pela imprensa, 12 linhas; por decisão sua, fora do codebook | Material do Artigo 3 |
| `data/external/levantamento_8_de_janeiro_*` | 58 referências, 15 colunas, com fase e relevância preliminares; a 2ª aba do XLSX é importação corrompida | Bibliografia sobre o 8/1 |
| `projeto-pos-doc/00_ESPECIFICACAO-ESTILO.md` | Nove traços de escrita e regras negativas, tomados de um modelo FAPERJ | Relevante para a Etapa 2, mas **não é o estilo da tese** |
| `projeto-pos-doc/01_PROJETO-PESQUISA.md` | Projeto "Camadas de uma ruptura", 2.442 palavras | Enquadramento teórico já redigido |
| `projeto-pos-doc/06_BIBLIOGRAFIA-DO-PROJETO.md` | 78 referências por camada + núcleo teórico (a única parte lida na íntegra) | Base da Etapa 4 |
| `projeto-pos-doc/08_BIBLIOGRAFIA-METODOLOGICA.md` | Verificação de 10 itens das sínteses LeapSpace (4 divergentes); testes de process tracing; "ameaça, e não só oportunidade" | Base metodológica |
| `projeto-pos-doc/02, 03, 04, 05, 07` | Disciplina, carta, Lattes, checklist, registro de revisão | Fora do escopo |
| `Fontes/LEIA-ME_fontes.md` | Inventário do corpus, páginas, procedência, nota técnica de acesso | Nota de fontes do artigo |
| `Fontes/05/*_LeapSpace.docx` (7) | Sínteses automáticas, ~31,6 mil palavras, 410 DOIs; com erros de metadados demonstrados | Só como mapa de busca |
| `Fontes/07/NetLab...md` | Transcrição: 185 anúncios golpistas na biblioteca de anúncios da Meta (07/02/2023) | PT-19A |
| `Fontes/11/PACCELLI_Tese...docx` | Tese; capítulos: Introdução · Eventos precipitantes e EOP · Estruturas de mobilização · Considerações finais | Etapa 2 (estilo) e antecedente teórico |
| `scripts/` (17 arquivos) | Geradores e verificadores Python/bash | Não lidos: são infraestrutura, sem conteúdo analítico |

---

## 3. Estado dos dados

**Codebook.** 82 sub-eventos × 16 campos. Status: 60 em fonte primária, 14 confirmados por outra via, 7 contextuais, 1 inferência declarada (PT-62), 0 a verificar. Por fase: T-1 Conjuntural 18 · **T-1 Operacional 24** · **T0 Mobilização 5** · **T0 Execução 11** · T0 Resposta tática 5 · T+1 (várias subfases) 19.

**Recorte do Artigo 1 no codebook:** PT-08A a PT-28 (T-1 Operacional) e PT-24 a PT-38 (T0 Mobilização e Execução), cerca de 40 registros. Quase todos estão ancorados na CPMI com página e transcrição no caderno; há corroboração dupla com Cappelli em PT-18 e PT-20B e com o acórdão da AP 2668 em PT-19B e PT-39.

**Como os três mecanismos aparecem no codebook:**

| Mecanismo do Artigo 1 | Registros | Situação |
|:--|:--|:--|
| (a) Escalada de radicalização | PT-10 → PT-12 (conversão de repertório) → PT-15 (12/12, "ensaio geral sem custo") → PT-16 (24/12, radicalização de flanco) → PT-19/19B ("Tomada de Poder") → PT-29 a PT-37 | Bem documentado; o rótulo "escalada" já está no codebook |
| (b) Alinhamento de quadros "fraude" ↔ "intervenção" | PT-07 (PGR: fraude pré-construída em 2021), PT-10, PT-10A ("Eu autorizo, Presidente!"), PT-12 ("SOS Forças Armadas"), PT-14, PT-16, PT-19A, PT-20, PT-29, PT-36 | **O mais frágil.** O campo `framing_narrativa` guarda rótulos curtos, não textos de convocação, faixas ou manifestos transcritos |
| (c) Falhas de contenção | PT-11, PT-13 (aval da elite), PT-18 (sobreaviso), PT-19B/PT-39 (grupo "Difusão"), PT-20A, PT-20B, PT-22, PT-23, PT-25 a PT-28, PT-31, PT-32 | **O mais forte**; pendências 3, 4 e 5 já preparam as respostas a pareceristas |

**Matrizes de process tracing.** Não há matriz formal de testes (hoop, smoking gun, doubly decisive). Os testes aparecem apenas nomeados dentro dos registros (PT-28 como hoop test; o smoking gun deslocado de PT-41 para PT-18). O relatório lista "testar os mecanismos" como item **aberto**.

**Notas sobre a CPMI.**
- O caderno traz 49 registros literais, e a paginação do PDF coincide com a impressa.
- A crítica da fonte já foi iniciada: a CPMI se contradiz sobre os 2.151 presos (p. 76 × p. 688); a mensagem das 14h56 é achado exclusivo da CPMI, sem validação judicial; a advertência "a CPMI é peça de investigação parlamentar, com posição política própria e votos em separado" está registrada.
- **Não verifiquei se o PDF de 1.333 p. inclui os votos em separado.**

**Bibliografia já reunida.**
- 58 do levantamento: 50 confirmadas, 6 não localizadas, 2 só em autoarquivamento. **Nenhuma foi lida na íntegra**, segundo o próprio aparato. Por fase: 11 conjunturais, 9 discursivas, 10 de T0 (majoritariamente mídia e discurso), 18 institucionais.
- 20 do eixo Lava Jato.
- Núcleo teórico reverificado no CrossRef: McAdam, Tarrow e Tilly (2001), Benford e Snow (2000), Koopmans e Olzak (2004), Giugni et al. (2005), McCarthy e Zald (1977), Beach e Pedersen (2019), Collier (2011), Alonso (2017), Tatagiba e Galvão (2019) e outros.

---

## 4. HTML da cronologia

- **`reports/figures/cronologia_8jan_interativa.html`** (original, 96 KB). É idêntico byte a byte a `projeto-pos-doc/figuras/cronologia-interativa.html`.
  - Título: "Cronologia causal do 8 de Janeiro — Process Tracing".
  - Traz um array JS `E` com 77 pontos, 4 faixas de cor (conjuntural, operacional, T0, T+1), data, rótulo, fase, repertório e mecanismo.
- **SVG existente:** `reports/figures/figura_cronologia_8jan.svg`, idêntico a `projeto-pos-doc/figuras/figura-1_cronologia-causal.svg`. Há ainda uma versão mais antiga em `.backup_pre_lula/`.

**Problema:** as duas figuras ficaram para trás depois das correções de 16/08/2026.
- O SVG ainda diz **"acampamentos em quartéis (+100)"**, cifra retirada, e **"bloqueios (>1.000 pontos)"**, quando o codebook registra 1.300 (CPMI).
- O HTML ainda mostra **"+1.600 ações penais"** em T+1, quando o correto é 1.335. Isso fica fora do recorte do Artigo 1, mas vale corrigir.

Por isso a Figura 1 **deve ser construída a partir do JSON**, e não copiada do SVG atual.

---

## 5. Lacunas para o Artigo 1

1. **A referência central do mecanismo (b) não está no repositório.** Snow, Rochford, Worden e Benford (1986) não aparece em nenhum arquivo (busca por "Rochford" e "Worden": zero ocorrências). A tese cita Benford e Snow (2000) e Snow e Benford (1988). Precisa ser verificada e incluída na Etapa 5.
2. **Faltam fontes textuais para o alinhamento de quadros.** Hoje as provas são rótulos codificados e poucas transcrições (PT-10A, PT-19B). Para sustentar a ponte entre "fraude" e "intervenção militar" com rastreabilidade, é preciso extrair do PDF da CPMI (e da denúncia da PGR) os trechos literais de convocações, faixas e mensagens. É trabalho de leitura dirigida, ainda não feito.
3. **Não há literatura sobre escalada e radicalização em contentious politics** (nenhuma ocorrência de della Porta sobre radicalização, de Alimi, Bosi e outros). Também não há literatura sobre **policiamento de protesto**, necessária para o mecanismo (c).
4. **Não há literatura sobre militares, forças de segurança e política no Brasil**, e o eixo secundário do artigo é justamente esse. O único item próximo é Koonings e Kruijt (2025), sobre golpes e autogolpes.
5. **Há pouca literatura brasileira sobre a dinâmica de mobilização dos acampamentos.** Das 10 referências de T0, a maioria trata de mídia e discurso. O próprio projeto de pós-doc diagnostica isso: a camada organizacional é "a menos coberta da literatura".
6. **Não há matriz formal de testes de process tracing.** Ela é necessária para a seção de método e para a análise, e pode ser montada a partir do codebook.
7. **A figura da cronologia está desatualizada** (ver seção 4).
8. **A tese está em .docx, sem paginação estável.** O LEIA-ME recomenda citá-la por seção. Na Etapa 2, os exemplos de estilo terão **localização por capítulo e seção, e não por página**, a menos que você tenha um PDF paginado da versão final.
9. **As normas da revista ainda não foram verificadas.** Isso fica para a Etapa 3.
10. **Votos em separado da CPMI:** não sei se estão no PDF do corpus. Eles são relevantes para o tratamento crítico da fonte.
11. **Divergência de estilo a decidir:** `00_ESPECIFICACAO-ESTILO.md` descreve o registro adotado no projeto de pós-doc (modelo FAPERJ). Você pediu o estilo **da tese**. A Etapa 2 vai tomar a tese como referência, salvo instrução contrária.

---

## 6. Limites desta leitura

- **Lidos integralmente:** README, todos os LEIA-ME, `PENDENCIAS-ANALITICAS.md`, `06_BIBLIOGRAFIA-DO-PROJETO.md` e o JSON inteiro (processado por script, com os 82 registros listados).
- **Lidos por estrutura e seções-chave:** relatório de process tracing (notas de revisão, síntese causal, próximos passos), caderno de evidências (estrutura), sínteses LeapSpace (busca dirigida), tese (sumário e busca dirigida), HTML e SVG da cronologia.
- **Catalogados sem leitura nesta etapa:** os 22 PDFs de fonte primária (6.928 p.). Uso as descrições do inventário e os trechos já transcritos no caderno. Os scripts e a pasta `.git` também não foram lidos.
- **Não abertos:** `.backup_pre_lula/` (redundante, segundo o README) e `.claude/settings.local.json`.
