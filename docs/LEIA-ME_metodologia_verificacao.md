# Nota metodológica — verificação do levantamento bibliográfico sobre o 8 de Janeiro de 2023

## O que foi feito

Você pediu para eu verificar e organizar em tabela a lista de ~58 referências que o OpenScience gerou, sinalizando o que fosse duvidoso (sem descartar nada) e aplicando as categorias de Process Tracing/PEA do projeto. É isso que está no arquivo `data/external/levantamento_8_de_janeiro_verificado.csv`.

Cada referência foi checada individualmente:
- **Com DOI**: consultei diretamente a API do CrossRef (api.crossref.org), que é a base oficial de metadados de publicações acadêmicas. Trouxe título, autores, periódico e resumo (quando o CrossRef o disponibiliza — muitas revistas não registram o abstract ali).
- **Sem DOI**: fiz busca na web por título e autor, e só considerei "confirmada" uma referência quando encontrei a página oficial do periódico, repositório institucional ou biblioteca digital de teses correspondente.

## Resultado

Das 58 referências do levantamento original (após remover duplicatas explícitas), a esmagadora maioria (48) foi confirmada como existente, com link de acesso real. Seis itens **não puderam ser localizados** com o autor/título informados (marcados como "Não localizado" na coluna de status) — isso não significa necessariamente que sejam inventados, apenas que não encontrei uma fonte correspondente nas buscas realizadas. Recomendo que você confirme esses itens diretamente antes de citá-los:

- Moreira (2025) — tese sobre lei antiterrorismo
- Rodrigues (2024) — fake news e ensino de história (encontrei um trabalho de tema muito próximo, mas de autoria não confirmada)
- Soares (2025) — crimes contra instituições democráticas
- Machuy (2023?) — título aparentemente incompleto/impreciso
- Silva et al. (2023) — "Crisis, Moderating Power, COVID-19..."
- do Vale (2026) — "Digital Constitutionalism in Brazil..."

## Um problema encontrado no levantamento original

O item de Amaral (2024), "Brazil as a Laboratory for Fascist Uprising", vinha com o DOI `10.1215/00382876-12345678`, já sinalizado no seu levantamento como "(approximate)". Esse padrão de números sequenciais (12345678) é uma marca típica de DOI fabricado por IA. Confirmei que o artigo **existe de fato** (South Atlantic Quarterly, Duke University Press), mas com o DOI real `10.1215/00382876-11086627`. Corrigi isso na planilha.

## Limitações importantes (leia antes de usar a tabela para a pesquisa)

1. **Resumos**: só incluí o texto do abstract quando ele estava genuinamente disponível via CrossRef ou na página do periódico — não escrevi resumos "de memória" nem inferi conteúdo que não estava explícito. Vários itens (sobretudo capítulos de livro e teses/dissertações) estão marcados como "não obtido nesta consulta — recomenda-se leitura do texto completo".
2. **Categorias de Process Tracing/PEA** (fase do processo, relevância ao 8/1): são classificações **preliminares**, baseadas apenas no resumo disponível — não na leitura integral dos textos. O projeto pede rastreabilidade estrita a partir dos documentos-fonte; para uma codificação definitiva segundo seu codebook, essas obras precisam ser lidas na íntegra.
3. **Relevância ao tema**: alguns itens (Messari sobre o G20, de Souza sobre COVID-19, de Oliveira & Rached sobre governança global) parecem só tangencialmente relacionados ao 8 de Janeiro — provavelmente entraram no levantamento original por aparecerem em buscas amplas sobre "democracia no Brasil". Sinalizei isso para você decidir se ficam no corpus.
4. **Não baixei os PDFs** — por decisão sua, a tabela traz os links de acesso (muitos são open access; alguns exigem acesso institucional).

## Arquivo

`data/external/levantamento_8_de_janeiro_verificado.csv` — abre em Excel, Google Sheets ou LibreOffice Calc. Colunas: Nº, Autor(es), Título, Periódico/Fonte, DOI, Link, Status de verificação, Resumo, Metodologia, Relevância ao 8/1, Fase do processo, Observações.

---

## Adendo de 12/08/2026 — lacuna bibliográfica aberta pela revisão do process tracing

Nesta data foi incorporado ao process tracing o arco judicial Lava Jato / prisão de Lula (2017–2021): registros **PT-03A a PT-03E, PT-05A e PT-06A a PT-06C** em `data/processed/process_tracing_8jan_eventos.csv`. Ver a nota de revisão no topo de `../reports/process_tracing_8jan_relatorio.md`.

**Consequência para o levantamento bibliográfico: este corpus não cobre o novo eixo.** As 48 referências verificadas tratam de bolsonarismo, ativismo digital, política contestatória e resposta institucional ao 8/1 — nenhuma trata de Lava Jato, judicialização da política ou *lawfare*, que agora se tornaram necessárias ao referencial teórico da camada $T_{-1}$ conjuntural.

Recomendo abrir um **quinto eixo** na Seção 1 do inventário de corpus, com três cuidados:

1. **Equilíbrio de posições.** O debate acadêmico sobre a Lava Jato é litigioso e polarizado. Um levantamento que só recolha trabalhos de um dos lados comprometerá a defesa do artigo em banca ou parecer. Inclua deliberadamente autores que sustentam leituras opostas sobre a legitimidade da operação.
2. **Separar as duas perguntas.** Uma coisa é a literatura sobre o *mérito* das decisões judiciais; outra é a literatura sobre *efeitos da judicialização na competição política*. É a segunda que a pesquisa precisa — a primeira só interessa como objeto de disputa a ser reportado, não como fundamento.
3. **Verificação.** Aplicar o mesmo protocolo já usado aqui (CrossRef para itens com DOI; confirmação em página oficial de periódico ou repositório para os demais) antes de incorporar qualquer item ao corpus.

As fontes primárias do arco judicial **já foram obtidas** e estão em `Fontes/01_Arco-judicial_2017-2021/` — inclusive o acórdão do TSE, obtido em 16/08/2026 pela Consulta Unificada PJe, sem captcha. Inventário completo, pendências e nota técnica de acesso em [`Fontes/LEIA-ME_fontes.md`](../Fontes/LEIA-ME_fontes.md).

A antiga pasta `Referências/` foi consolidada em `Fontes/05_Bibliografia-teorica/`.
