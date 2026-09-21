# Eixo bibliográfico — Lava Jato, judicialização da política e lawfare

## Por que esta pasta existe

Quando o arco judicial de 2016–2021 entrou no process tracing (registros **PT-02A** e **PT-03A a PT-06C**), abriu-se uma lacuna: o levantamento bibliográfico original, de 48 referências, **não cobria nenhum** desses temas. Ele fora montado para bolsonarismo, ativismo digital, política contestatória e resposta institucional. Nada sobre Lava Jato, judicialização ou *lawfare*.

Sem esse eixo, o artigo afirmaria que a arena judicial reconfigurou a competição eleitoral **sem literatura que sustente o conceito**. É a diferença entre uma tese e uma opinião.

## O que há aqui

| Arquivo | Conteúdo |
|:--|:--|
| `bibliografia_eixo_lava-jato.csv` | 20 referências, 9 colunas, legível por máquina |
| `bibliografia_comentada.md` | As mesmas, agrupadas por subeixo, com nota sobre o que cada uma serve no projeto |

Protocolo de verificação: consulta à **API do CrossRef** por título, comparando o ano retornado com o da busca original — o mesmo protocolo usado no levantamento de 2026-08 (ver `../../docs/LEIA-ME_metodologia_verificacao.md` na raiz).

**18 das 20 têm DOI confirmado.** Duas ressalvas anotadas na coluna de status:

- **Sieder (2020)** — a consulta retornou obra distinta da mesma autora, de 2005. O DOI foi **removido** em vez de registrado errado. Confirmar na página da *Latin American Research Review*.
- **Coelho** — o CrossRef registra 2024; a busca indicava 2021. Conferir na página do periódico *Passagens*.

---

## Advertência sobre o desequilíbrio da literatura

**A distribuição de posições não é equilibrada, e isso não é falha do levantamento.**

Contagem por posição: 3 críticas diretas à operação, 4 de *lawfare* (todas críticas em maior ou menor grau), 1 crítica em chave de teoria política, 2 favoráveis, e o restante analítico ou clássico.

Busquei deliberadamente trabalhos favoráveis à operação — a busca *"anticorruption enforcement effectiveness Brazil Car Wash deterrence positive assessment"* foi feita justamente para isso. O resultado foi magro: **Castro & Ansari (2017)** e, em chave indireta, **Mohallem (2021)**. A explicação mais provável é temporal: a literatura revisada por pares sobre a Lava Jato **adensa-se depois de 2019**, isto é, depois da Vaza Jato, e reflete esse deslocamento. A defesa da operação existe sobretudo em escrita de operadores — artigos e livros de Sergio Moro e Deltan Dallagnol —, que **não é literatura acadêmica** e deve entrar no texto como *objeto de análise*, não como referência de autoridade.

**Como lidar com isso no artigo.** Não simular equilíbrio inexistente, e não deixar a assimetria implícita. A formulação defensável é declarar o estado do campo: *"a literatura revisada por pares posterior a 2019 é majoritariamente crítica à operação; as defesas mais articuladas encontram-se em escrita de operadores, tratada aqui como fonte primária e não como bibliografia"*. Isso é mais forte do que fingir simetria, e é verdadeiro.

## Advertência sobre uma referência específica

**Dias, B. L. C. V. et al. (2024)** sustenta que o *lawfare* é instrumento de guerra geopolítica conduzida pelos EUA para apropriação de recursos naturais. O periódico tem baixo fator de impacto e **o argumento excede o que a evidência apresentada sustenta**. Foi incluído por representar uma posição efetivamente presente no debate latino-americano — mas usá-lo como sustentação, e não como objeto, comprometeria o artigo. O mesmo vale, em grau menor, para Zaffaroni, Caamaño & Vegh Weis (2023).

O item **metodologicamente mais sólido** do subeixo *lawfare* é **Vegh Weis (2022)**, em *Punishment & Society*.

---

## As três referências que fazem trabalho direto no codebook

| Referência | Registro |
|:--|:--|
| **Rodrigues & Arantes (2020)** | **PT-02A e PT-05A** — analisa exatamente a virada do STF sobre execução provisória e a reversão de 2019 |
| **Silva (2020)** | **PT-03A a PT-04** — conecta Lava Jato e ascensão de Bolsonaro, que é o argumento do arco judicial |
| **Meszaros (2020)** | **PT-05A** — fundamenta o mecanismo de deslegitimação recíproca do Judiciário |

## O que falta

Nenhuma destas obras foi **lida na íntegra**. As anotações derivam de resumos e da posição declarada de cada texto. Antes de citar como sustentação teórica — e não apenas como referência de existência —, a leitura é necessária, pela mesma razão registrada no LEIA-ME do levantamento original.

Falta também a literatura **clássica brasileira** sobre judicialização, que é de livro e por isso não aparece em busca por DOI: Werneck Vianna et al., *A judicialização da política e das relações sociais no Brasil* (1999); Rogério Arantes, *Ministério Público e política no Brasil* (2002); Kerche & Marona, *A política no banco dos réus* (2022). Devem ser incorporadas manualmente.
