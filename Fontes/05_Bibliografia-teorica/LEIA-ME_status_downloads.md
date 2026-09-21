# Bibliografia teórica — download dos PDFs mapeados

> **Nota de 12/08/2026.** Esta pasta era `Referências/` na raiz do projeto e foi movida para `Fontes/05_Bibliografia-teorica/` na consolidação do corpus. O texto abaixo é o registro original; a limitação técnica de sandbox nele mencionada **já não se aplica** — o download por rede voltou a funcionar, como comprova o acervo obtido em `Fontes/`. Ver `Fontes/LEIA-ME_fontes.md`.


## Dois limites que preciso deixar claros antes de prosseguir

**1) Direitos autorais.** Boa parte dos itens do levantamento está em periódicos comerciais fechados (SAGE, Routledge/Taylor & Francis, Springer, Cambridge University Press, Duke University Press). Baixar e armazenar em massa os PDFs desses artigos violaria os termos de acesso/copyright — não é diferente de você baixar um artigo pago sem ter assinatura. Por isso, para esses itens vou apenas deixar o link direto na tabela, para você baixar com seu acesso institucional (Periódicos CAPES costuma dar acesso a várias dessas revistas).

Para os itens que são **legitimamente de acesso aberto** — periódicos brasileiros em plataforma OJS (a grande maioria do levantamento), SciELO, SciELO Preprints, Redalyc, repositórios institucionais de teses/dissertações (UNESP, UFS, UCS, UNIOESTE, UFOP), SCIRP, e capítulos/artigos que os próprios autores disponibilizaram abertamente — o download é legítimo e vou trazer o PDF para esta pasta.

**2) Limitação técnica no momento.** O ambiente de execução (sandbox) que uso para baixar arquivos da web está indisponível nesta sessão (erro de infraestrutura, não relacionado ao seu pedido). Assim que ele voltar, retomo os downloads automaticamente. Esta pasta e este arquivo já estão criados para não perder o trabalho.

## Como vou prosseguir

1. Baixar os PDFs de acesso aberto (~40 itens) para esta pasta, nomeados como `NN_SobrenomeAutor_Ano.pdf`.
2. Deixar uma lista dos itens pagos (SAGE não-OA, Routledge, Springer, Cambridge, Duke) com o link direto, para download manual com seu acesso institucional.
3. Não tentar baixar os 6 itens que não foram localizados na verificação anterior (Moreira 2025, Rodrigues 2024, Soares 2025, Machuy, Silva et al. 2023, do Vale 2026).

Vou atualizar este arquivo com o resultado final assim que os downloads forem concluídos.

---

## Adendo de 12/08/2026 — peças processuais do arco judicial (2017–2021)

A revisão do process tracing desta data incorporou o arco Lava Jato / prisão de Lula. As peças abaixo são **fontes primárias de acesso público e gratuito** — não há restrição de copyright a baixá-las — e devem entrar nesta pasta quando obtidas:

| Peça | Órgão | Data | Observação de acesso |
|:--|:--|:--|:--|
| Sentença da AP 5046512-94.2016.4.04.7000 (triplex) | 13ª Vara Federal de Curitiba | 12/07/2017 | Consulta processual da JFPR / acervo do TRF-4 |
| Acórdão da ACr 5046512-94.2016.404.7000 | 8ª Turma do TRF-4 | 24/01/2018 | Portal do TRF-4 |
| Acórdão do HC 152.752 | Plenário do STF | 04/04/2018 | Busca de inteiro teor no STF |
| Acórdão do Registro de Candidatura (indeferimento) | Plenário do TSE | 01/09/2018 | Portal do TSE |
| Acórdãos das ADCs 43, 44 e 54 | Plenário do STF | 07/11/2019 | Publicados em nov/2020 |
| Decisão de anulação por incompetência (Rcl/HC) | Min. Edson Fachin, STF | 08/03/2021 | Confirmada pelo Plenário em 15/04/2021 |
| Acórdão do HC 164.493 (suspeição de Moro) | 2ª Turma do STF | 23/03/2021 | Plenário manteve em 23/06/2021 |

**Duas dificuldades de acesso registradas na sessão de 12/08/2026:** o `portal.stf.jus.br` retornou erro de certificado TLS e o `noticias.stf.jus.br` bloqueia acesso automatizado (HTTP 403). Ambos funcionam normalmente em navegador — a coleta terá de ser manual.

Enquanto os inteiros teores não forem obtidos, os nove registros novos do codebook apoiam-se em comunicados oficiais (TRF-4, TSE, STF) e na Agência Brasil/EBC, com o status de verificação anotado em cada linha.

---

## Adendo de 14/08/2026 — situação real da coleta

**A tabela acima está cumprida, com uma exceção.** Seis das sete peças foram obtidas e estão em `../01_Arco-judicial_2017-2021/` (mais o acórdão da ADC 43-MC de 2016, que entrou como precedente). Faltam:

- **Acórdão do TSE** (registro de candidatura, 01/09/2018) — buscador com reCAPTCHA, exige coleta por pessoa. Instruções em `../LEIA-ME_fontes.md`.
- **Sentença de 1ª instância** (12/07/2017), inteiro teor — deixou de ser pendência crítica: o dispositivo está transcrito no acórdão do TRF-4 (Revista 97, p. 395).

**A dificuldade de acesso ao STF foi diagnosticada e resolvida.** Não era certificado nem bloqueio: é AWS WAF com desafio JavaScript. A receita reproduzível está na nota técnica de `../LEIA-ME_fontes.md`.

**Sobre os downloads da bibliografia (itens 1 a 3 de "Como vou prosseguir"):** não foram retomados, e a prioridade mudou. O eixo bibliográfico que a pesquisa passou a precisar — Lava Jato, judicialização e *lawfare* — foi construído em `../06_Lava-Jato-judicializacao-lawfare/`, com 20 referências e 18 DOIs confirmados. Chegaram também, em 13/08/2026, cinco sínteses de literatura sobre os conceitos do referencial teórico, com 325 DOIs a verificar — ver `../LEIA-ME_fontes.md`, seção 05, e o item 11.3 de `../../docs/PENDENCIAS-ANALITICAS.md`.
