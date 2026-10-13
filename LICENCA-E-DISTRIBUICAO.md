# Licença e distribuição

*Tarefa 15, executada em 13/10/2026. Este documento registra **fatos apurados**, não escolhas de licença: a licença da obra do pesquisador é decisão dele, e está em aberto no fim deste arquivo.*

---

## 1. A decisão, e ela é forçada pela evidência

**Este repositório não vai a remoto público.**

Não é preferência de cautela. A auditoria de licença — `python scripts/auditar_licencas.py`, que lê o que **cada arquivo declara sobre si**, e não o que o editor ou o registro de acesso aberto dizem — encontrou isto:

| | Arquivos | |
|:--|--:|:--|
| **Documental** | **22** | 21 atos oficiais + 1 CC |
| **Literatura** | **40** | 13 CC · **2 com todos os direitos reservados impressos** · 25 sem declaração |

**27 das 40 peças de literatura não podem ser redistribuídas** — 56 MB. Entre elas:

- **KUNRATH SILVA (2018)** e **TATAGIBA (2018)**, as duas pela *Lusotopie*, que declaram **todos os direitos reservados no próprio arquivo**. A primeira **ancora PT-01, PT-02, PT-04 e PT-05**;
- **TARROW**, *O poder em movimento*, Vozes;
- **McADAM, TARROW e TILLY**, *Dynamics of Contention*, Cambridge;
- a **Wiley-Blackwell Encyclopedia of Social and Political Movements**, 1.638 páginas;
- **ALONSO**, *Treze*, Companhia das Letras.

> **E "sem declaração" não significa livre:** significa desconhecido, e desconhecido conta como reservado por omissão. A regra tem um caso que a justifica: **Rich (2021)**, que o OpenAlex declarava **ouro** e que está à venda em livraria. **Registro de acesso aberto pode estar errado sobre a licença; o arquivo é o que vale.**

**Já o documental é outra coisa**, e misturar os dois produzia uma cifra errada. A ausência de declaração num acórdão ou num relatório de CPMI não é lacuna: a **Lei 9.610/98, art. 8º, IV**, põe atos oficiais fora do direito autoral.

## 2. Parar de versionar o corpus agora não resolveria

Os PDFs estão **no histórico**. O `.git` tem **250 MB** por causa deles, contra **8 MB** de texto e código. Um remoto público deste repositório distribuiria os arquivos **mesmo que a árvore de trabalho ficasse limpa**.

> Logo a pergunta "tirar o corpus do versionamento antes de criar o remoto?" tem resposta **não**, por duas razões: não bastaria, e o versionamento é o que garante os bytes exatos de nove peças que o pesquisador obteve pessoalmente e que não se recuperam. **O corpus continua versionado, e o repositório continua privado.**

## 3. Como a pesquisa fica verificável sem ser redistribuída

Pelo **manifesto**: `Fontes/MANIFESTO-CORPUS.csv`, gerado por `scripts/gerar_manifesto_corpus.py`. Para cada uma das 62 peças: caminho, **SHA-256**, páginas, bytes, classe de licença lida no arquivo e **rota de obtenção**. Toda peça tem rota declarada — conferido.

Quem quiser checar uma âncora obtém a peça pela rota, compara o SHA-256 e abre a página. **A verificabilidade não depende da redistribuição.**

E o manifesto serve a um segundo propósito que vale por si: a **checagem 8** de `verificar_integridade.py` compara corpus e manifesto peça por peça. Um PDF que mude de bytes sem mudar de nome quebraria toda âncora que dependa dele, e até 13/10/2026 **nada acusava**. Prova negativa: um bit virado no meio de um PDF, uma peça removida e uma peça intrusa — **3 de 3 pegas**.

## 4. Se um dia houver publicação, ela é de um repositório NOVO

`python scripts/exportar_aparato.py` monta a árvore publicável num diretório à parte: **131 arquivos de texto e código, 8 MB**, contra 294 MB de binário excluído.

**A segurança é por construção, não por cuidado de quem executa:**

- o filtro **inclui por autorização** — texto e código entram, binário só entra por lista. A primeira versão excluía `Fontes/**/*.pdf`, regra de *caminho*, e **vazou um PDF de 24,7 MB que estava em `.backup_pre_lula/`**. Regra de caminho falha no caminho que ninguém lembrou;
- antes de terminar, o script **confere o resultado contra o manifesto** e **apaga o destino** se qualquer peça `RESERVADA`, `SEM` ou `ILEGÍVEL` tiver escapado;
- e ele **não cria remoto, não faz commit e não publica nada**. Publicar é irreversível, e é ato do pesquisador.

## 5. Duas pendências de higiene, relatadas e não executadas

1. **`.backup_pre_lula/` está versionado**: 27 arquivos, **27 MB**, incluindo um PDF de 24,7 MB. É diretório de backup dentro do controle de versão. Não foi removido porque são os estados anteriores do JSON, que são a sua rede de segurança — **tirar backup do versionamento é decisão sua**. A exportação já o exclui por construção.
2. **`STF_Democracia-Inabalada_Folder.pdf`: 37,4 MB em 6 páginas** — 6,23 MB por página, o pior índice do corpus. Recomprimir seria seguro quanto à licença, porque é ato oficial, mas **mudaria os bytes** e com isso o SHA-256 do manifesto e o lastro de qualquer âncora que dependa da peça. **Não se toca em bytes de peça do corpus sem decisão explícita.**

## 6. O que continua em aberto, e é jurídico

**Sob que licença sai a obra do pesquisador** — o codebook, os scripts, os documentos de análise. Não escolhi por você: licença é decisão jurídica, e a de quem assina a obra.

Os arquivos que a exportação exclui por serem binários **e que são seus** estão listados pelo próprio script quando ele roda: a tese de doutorado, o projeto de pesquisa, as planilhas e os sete `.docx` de fichamento do eixo 05. Publicá-los é decisão sua, e é por isso que o script os **lista em vez de decidir**.
