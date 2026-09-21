# Dossiê de candidatura — PIPD/CAPES · PPG em Sociologia, IESP-UERJ

> ## ⚠️ Esta pasta não é corpus de pesquisa
>
> **`projeto-pos-doc/` funciona como um pull request sobre o repositório: lê dele, não escreve nele.**
>
> - Nenhum arquivo desta pasta ancora registro do codebook, consta do inventário `Fontes/LEIA-ME_fontes.md` ou do dicionário `PROCEDENCIA` em `scripts/gerar_codebook.py`.
> - Os scripts de verificação varrem apenas `Fontes/` — esta pasta **não** é lida por `verificar_integridade.py`, e não pode alterar o resultado da auditoria.
> - As figuras em `figuras/` são **cópias byte-idênticas** de artefatos da raiz, não artefatos novos. Os `sha1` estão registrados abaixo, para que a relação cópia→original seja verificável e ninguém confunda uma com a outra.
> - Os textos daqui são **documentos de candidatura**, não achados de pesquisa. Não devem ser citados como fonte.
>
> A única escrita feita no repositório fora desta pasta foi a incorporação da tese de doutorado em `Fontes/11_Tese-doutorado/` — que é adição de **fonte**, autorizada em 19/08/2026, e está declarada no inventário e em `PROCEDENCIA`, com a auditoria reexecutada e aprovada.

Pasta criada em **19/08/2026**, revista no mesmo dia. Reúne os documentos da candidatura à bolsa de pós-doutorado do PIPD/CAPES no PPGS do IESP-UERJ. Inscrições até **31/08/2026, 23h59**.

---

## Índice

| Arquivo | O que é | Estado |
|:--|:--|:--|
| [`edital/PIPD-Sociologia-2026-1.pdf`](edital/PIPD-Sociologia-2026-1.pdf) | A chamada pública, cópia do original | — |
| [`00_ESPECIFICACAO-ESTILO.md`](00_ESPECIFICACAO-ESTILO.md) | Os nove tracos de escrita adotados, do modelo FAPERJ | Documento de trabalho |
| [`01_PROJETO-PESQUISA.md`](01_PROJETO-PESQUISA.md) | Projeto de pesquisa — **item 2 do edital** | **2.442 palavras no corpo** (limite: 2.500; referencias fora) |
| [`01_PROJETO-PESQUISA_v1-compacto.md`](01_PROJETO-PESQUISA_v1-compacto.md) | Versao compacta congelada, anterior a reescrita | Fallback de conversao |
| [`02_PROPOSTA-DISCIPLINA.md`](02_PROPOSTA-DISCIPLINA.md) | Ementa e plano de curso — **item 3 do edital** | Pronto, 15 semanas |
| [`03_CARTA-RECOMENDACAO.md`](03_CARTA-RECOMENDACAO.md) | Minuta de carta de apoio, a assinar por Christiane Jalles de Paula | 22 marcadores a preencher |
| [`04_ROTEIRO-CV-LATTES.md`](04_ROTEIRO-CV-LATTES.md) | O que conferir no Lattes — **item 1 do edital** | Requer sua ação |
| [`05_CHECKLIST-SUBMISSAO.md`](05_CHECKLIST-SUBMISSAO.md) | Conferência dos quatro itens, calendário, entrevista | — |
| [`06_BIBLIOGRAFIA-DO-PROJETO.md`](06_BIBLIOGRAFIA-DO-PROJETO.md) | Aparato completo por camada, com status por item | 78 referências + núcleo teórico |
| [`figuras/`](figuras/) | Figura 1 (SVG) e cronologia navegável (HTML) | Cópias declaradas |

---

## O projeto, em uma página

**Título:** *Camadas de uma ruptura: estruturas de mobilização e oportunidades políticas e discursivas no 8 de Janeiro de 2023.*

**O objeto é o evento**, não o que veio depois. A pergunta é como se compõem as camadas estrutural, organizacional, discursiva e situacional para produzir aquele domingo — e o que se perde ao explicá-lo por uma só delas.

**O diagnóstico que abre o projeto é medido, não impressionista.** Das 50 referências confirmadas do levantamento, **17 tratam do desfecho institucional e apenas 10 da mobilização e execução**. A camada organizacional — acampamento, transporte, dinheiro, convocação — é a menos coberta da literatura e a mais bem documentada nas fontes primárias do repositório. É exatamente a lacuna que a pesquisa ocupa.

**A continuidade com a tese não é retórica.** `Fontes/11_Tese-doutorado/` analisa três ciclos (1992, 2013, 2015) pelo par estruturas de mobilização × oportunidades políticas e discursivas, encerrando com a entrada dos movimentos de direita. O 8 de janeiro é onde aquele arco chega a um desfecho antissistêmico. E o instrumento teórico decisivo já estava lá: **Koopmans & Olzak (2004)**, sobre oportunidades discursivas e violência de extrema-direita, é citado na tese — o projeto o aplica ao caso que ela não alcançou.

**As figuras compõem a escrita.** A Figura 1 abre o projeto como arquitetura do processo, e suas cinco faixas — T−1 conjuntural, T−1 operacional, T0, T0 ampliado, T+1 — são as seções da argumentação. A cronologia navegável entra como produto de divulgação e material da disciplina, onde serve para discutir que **visualizar uma cadeia causal já é uma afirmação analítica**.

---

## Verificação executada

### Aparato do repositório — intacto

`python scripts/verificar_integridade.py` → **APROVADO, as seis checagens passaram**, depois da incorporação da tese. `gerar_codebook.py` regenera com **zero arquivos órfãos** (41 no inventário). Nada do dossiê tocou o codebook.

### Figuras — cópias conferidas por hash

| Original (raiz) | Cópia (`figuras/`) | sha1 |
|:--|:--|:--|
| `reports/figures/figura_cronologia_8jan.svg` | `figura-1_cronologia-causal.svg` | `35ea4fc963475fc2d4c1db934ddfda913fc4dbfd` |
| `reports/figures/cronologia_8jan_interativa.html` | `cronologia-interativa.html` | `183dc2e9c87547c4a1708083e66d5a0012088df5` |

### Números do projeto — rastreados até a fonte

| Afirmação | Conferência |
|:--|:--|
| 82 sub-eventos × 16 campos · 60 em fonte primária | Contagem direta no JSON: 60 primária · 14 confirmados · 7 contextuais · 1 inferência |
| 22 documentos / 6.928 páginas | **Medido com PyPDF**, não copiado do painel |
| 2.151 prisões em flagrante (8 e 9/1) | PT-52 · CPMI, p. 76 e 688 |
| 1.878 investigações · 1.335 ações penais · 1.402 responsabilizados | PT-53 · Balanço do Gabinete Moraes, 29/04/2026, p. 4–6 |
| 272 caminhões (MBVA/Abin) | PT-10A · CPMI, p. 884-887 |
| 185 anúncios pagos | PT-19A · NetLab-UFRJ |
| "Festa da Selma"; Sri Lanka como "Plano B" | PT-19 · CPMI, p. 614-625 e 614 |
| Financiamento: captação pulverizada com nós | PT-12A · CPMI, p. 577-578 e 880-884 |
| "manifestante" supera "terrorista" e "golpista" no dia 8 | PT-50A · Manchetômetro/DOXA-IESP-UERJ, p. 9 |
| 58 referências, 50 confirmadas; 17 em T+1, 10 em T0 | Contagem por status e por fase na aba `Levantamento_Organizado` |

A cifra de "mais de 1.600 ações penais" que ainda consta de `../reports/process_tracing_8jan_relatorio.md` §3.2 **não foi usada**: o JSON a corrigiu para 1.335 em 16/08/2026.

### Referências — verificadas no CrossRef em 19/08/2026

Confirmadas com volume e paginação conferidos: Koopmans & Olzak (2004) `10.1086/386271` · Giugni et al. (2005) `10.17813/maiq.10.1.n40611874k23l1v7` · Tatagiba & Galvão (2019) `10.1590/1807-0191201925163` · Alonso (2017) `10.25091/s01013300201700040006` · Gohn `10.17141/mundosplurales.1.2019.3925` · Beach & Pedersen (2019) `10.3998/mpub.10072208` · McAdam, Tarrow & Tilly (2001) `10.1017/cbo9780511805431` · McCarthy & Zald (1977) `10.1086/226464` · Benford & Snow (2000) `10.1146/annurev.soc.26.1.611` · Collier (2011), Hutter (2014), Tarrow (2005).

As 58 do levantamento e as 20 do eixo Lava Jato entraram no `06_` **com o status já registrado na origem**, copiadas da coluna de referência formatada — não retranscritas.

> ⚠️ **Limite que vale para todo o aparato:** salvo o núcleo teórico, **estas obras não foram lidas na íntegra**. O status confirma que a referência existe, não que o conteúdo foi examinado. O projeto as cita como posições no campo, e a leitura integral é a atividade do 1º semestre do cronograma. Está declarado no próprio `06_`.

---

## Três divergências encontradas — e não resolvidas por conta própria

**1. 48 ou 50 referências confirmadas?** `../docs/LEIA-ME_metodologia_verificacao.md` diz 48; a contagem por status na planilha dá **50 confirmadas, 6 não localizadas, 2 só em autoarquivamento** (soma 58, que fecha). Usei 50. As duas de autoarquivamento são a explicação provável da diferença — decisão sua.

**2. Metadados divergentes em Alonso (2017) e Gohn.** A tese registra Alonso em número "Especial"; o CrossRef dá **v. 37**. A tese data Gohn em 2019; o CrossRef registra 2020, com DOI e volume de 2019. Mantive o dado do CrossRef, que é verificável.

**3. Tatagiba & Galvão (2019) tem errata publicada** (`10.1590/1807-01912019252472`), não consultada. Verificar antes de citar dados numéricos do artigo.

**Além disso, um defeito de arquivo:** a segunda aba de `../data/external/levantamento_8_de_janeiro_organizado.xlsx` (`levantamento_8_de_janeiro_verif`) é uma importação malformada — cabeçalho todo em uma célula, acentuação corrompida. Só a primeira aba é utilizável. Não a removi.

---

## O que depende de você

1. **Validação do título** do projeto.
2. **Periódicos-alvo.** O projeto ainda diz "estrato superior" sem nomear. O modelo FAPERJ que serviu de espelho nomeia revista por artigo, e é o único traço de escrita que ficou por aplicar.
3. **A citação em bloco.** A seção 2 traz um marcador explícito no lugar da passagem de Koopmans e Olzak (2004). O AJS está fechado, o abstract foi elidido pela editora e a tese cita os autores sem transcrever. Ou você fornece a passagem, ou o marcador sai e o trecho segue sem citação em bloco.
4. **A cifra remanescente no relatório.** `../reports/process_tracing_8jan_relatorio.md` §3.2 ainda traz "mais de 1.600 ações penais", corrigida no JSON para 1.335 em 16/08. Não alterei o aparato auditado — mexer nele é decisão sua.
5. **Bibliografia nacional da semana 11 da disciplina**, deixada em aberto para diálogo com a linha de Sociologia Política do IESP.
6. **Conversão para PDF.** A reescrita introduziu notas de rodapé em Markdown, que contam para o teto e podem não sobreviver ao conversor. Confira também que a Figura 1 em SVG atravessa, e reconfira a contagem no PDF final.

### Resolvido em 28/08/2026

- **Item 4 do edital**, com duas peças distintas: PAULA e PACCELLI, *Diretas Já*, Revista Estudos Políticos, v. 16, n. 32, p. 397-421, 2025 (`10.22409/rep.v16i32.63410`), na vaga do artigo em periódico, por tratar de ciclo excluído do escopo da tese; e PACCELLI e PAULA, *As juventudes de direita redescobrem as ruas*, Revista Agenda Política, v. 13, n. 2, p. 17-40, 2026 (`10.14244/agenda.2025.2.1`), na vaga da publicação derivada da tese.
- **Carta de apoio:** Christiane Jalles de Paula, orientadora.
- **Supervisão pretendida no pós-doc:** Breno Bringel. Não citado no corpo do projeto, por depender de conversa prévia.
- **Registro de escrita:** projeto reescrito em prosa desenvolvida, sem negrito, segundo `00_ESPECIFICACAO-ESTILO.md`.

## Regras herdadas do projeto, aplicadas aqui

Todo número conferido contra a fonte e não contra outra citação dela; nada afirmado que não tenha sido lido — daí a advertência explícita sobre a leitura integral pendente; e nenhuma decisão de julgamento tomada por inferência: as sete acima estão listadas, não executadas.
