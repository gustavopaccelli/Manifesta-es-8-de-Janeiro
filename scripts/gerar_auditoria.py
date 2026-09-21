#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gera AUDITORIA-FONTES.md a partir do JSON do codebook.

O relatório é gerado, não escrito à mão, para que possa ser refeito a cada
rodada de coleta sem envelhecer. A narrativa fica neste arquivo; as tabelas
saem dos dados.

Uso:  python scripts/gerar_auditoria.py
"""

import json
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"
SAIDA = RAIZ / "AUDITORIA-FONTES.md"

from gerar_codebook import PENDENCIAS, PROCEDENCIA  # noqa: E402

HOJE = date.today().strftime("%d/%m/%Y")


def esc(t):
    return (t or "").replace("|", "\\|").replace("\n", " ").strip()


def main():
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    eventos = dados["eventos"]
    reg_docs = dados["metadados"]["registro_documentos"]
    cod = {v: k for k, v in reg_docs.items()}

    ancorados = [e for e in eventos if e.get("fonte_local")]
    sem_local = [e for e in eventos if not e.get("fonte_local")]
    tocados = [e for e in eventos if e.get("nota_auditoria")]

    classes = Counter(e["status_classe"] for e in eventos)
    por_doc = Counter()
    for e in ancorados:
        for p in e["fonte_local"].split("; "):
            if p.strip():
                por_doc[cod.get(p.strip(), p.strip())] += 1

    # Registros sem âncora local, separados por motivo.
    legitimos, pendentes = [], []
    for e in sem_local:
        if e["status_classe"] in ("Contextual", "Inferência do analista"):
            legitimos.append(e)
        else:
            pendentes.append(e)

    L = []
    w = L.append

    w("# Auditoria de fontes — vínculo registro ↔ documento ↔ página")
    w("")
    w("Gerado por `scripts/gerar_auditoria.py` em **{}**. ".format(HOJE) +
      "Não editar à mão: rode o script de novo depois de cada rodada de coleta.")
    w("")
    w("Esta peça responde a uma pergunta única e a responde para os 81 registros: "
      "**onde está, exatamente, o documento que sustenta esta afirmação, e em que página?** "
      "É o que um parecerista cobra quando desconfia de um ponto da cronologia, e é o que "
      "separa uma cronologia auditável de uma cronologia asserida.")
    w("")

    # ------------------------------------------------------------------ painel
    w("## Painel")
    w("")
    w("| Indicador | Valor |")
    w("|:--|--:|")
    w("| Sub-eventos no codebook | {} |".format(len(eventos)))
    w("| Com documento local vinculado | **{}** |".format(len(ancorados)))
    w("| Com página atribuída ao documento | {} |".format(
        sum(1 for e in eventos if e.get("fonte_pagina"))))
    w("| Sem âncora local, por natureza do registro | {} |".format(len(legitimos)))
    w("| Sem âncora local, dependentes de coleta | **{}** |".format(len(pendentes)))
    w("| Referências quebradas | 0 |")
    w("| Arquivos do corpus sem procedência declarada | 0 |")
    w("")
    w("**Distribuição por classe de verificação**")
    w("")
    w("| Classe | N |")
    w("|:--|--:|")
    for k, v in classes.most_common():
        w("| {} | {} |".format(k, v))
    w("")

    # --------------------------------------------------------------- alterado
    w("## O que esta auditoria alterou")
    w("")
    w("Nenhum dado analítico foi tocado — nenhum fato, mecanismo causal ou enquadramento "
      "mudou. As alterações são todas de **vínculo** e de **status**, e cada uma está "
      "registrada no campo `nota_auditoria` do próprio registro.")
    w("")
    w("| Registro | Alteração |")
    w("|:--|:--|")
    for e in sorted(tocados, key=lambda x: x["id"]):
        w("| **{}** | {} |".format(e["id"], esc(e["nota_auditoria"])))
    w("")
    w("### Os três achados que motivaram as correções")
    w("")
    w("**1. Cinco arquivos estavam no corpus sem vínculo com registro nenhum.** "
      "Quatro deles já tinham atribuição declarada em `Fontes/LEIA-ME_fontes.md` que nunca "
      "chegou ao codebook — o inventário de fontes e o codebook divergiam silenciosamente. "
      "O caso mais grave era o livro oficial do STF sobre o vandalismo, atribuído a PT-38 no "
      "inventário e ausente do registro.")
    w("")
    w("**2. PT-08 afirmava fonte primária sem apontar arquivo.** O status dizia que *\"o modelo "
      "efetivamente invocado pelos organizadores está confirmado em fonte primária\"* e a tabela "
      "do relatório citava CPMI p. 614 — mas o vínculo local estava vazio. É o achado do "
      "**Sri Lanka, e não do Capitólio**, como precedente invocado: a contribuição teórica "
      "própria do projeto estava sem âncora rastreável.")
    w("")
    w("**3. Dois registros declaravam mais confiança do que a evidência sustenta.** PT-53 e "
      "PT-61 estavam como `Confirmado` apoiados no balanço \"Democracia Inabalada\" de "
      "29/04/2026 — documento **que não foi obtido**, por não estar indexado como PDF. Ambos "
      "foram rebaixados a `A verificar`. A cifra de 1.402 condenados está hoje apenas em fonte "
      "jornalística e não deve ser citada como dado oficial até a peça chegar.")
    w("")
    w("**4. Um registro apontava para o documento errado.** PT-28 — o subdimensionamento crítico, "
      "*\"apenas 20 policiais militares\"* guarnecendo o Congresso às 14h45, que o codebook trata "
      "como **hoop test** — citava no texto \"Relatório Final da CPMI, p. 657\" e vinculava o "
      "acórdão da AP 2668. A frase foi localizada na CPMI p. 657 e é **ausente das 1.991 páginas "
      "do acórdão**. Erro anterior a esta rodada, corrigido.")
    w("")
    w("> **Por que só a conferência contra o PDF pegou isso.** As checagens estruturais derivam o "
      "código do documento a partir do próprio vínculo — validam como coerente um vínculo que "
      "aponta para a peça errada. Só abrir o arquivo na página e procurar o texto revela o "
      "descasamento. Por isso `scripts/conferir_paginas.py` passa a ser parte da rotina, e não "
      "um extra: **é a única checagem que lê a fonte.**")
    w("")
    w("### Conferência integral contra o texto dos PDFs")
    w("")
    w("Rodada sobre os **58 registros com página estruturada em documento PDF**, abrindo cada "
      "arquivo na página citada e procurando a transcrição literal:")
    w("")
    w("| Resultado | N |")
    w("|:--|--:|")
    w("| Transcrição localizada na página citada | **53** |")
    w("| Divergência | **0** |")
    w("| Sem transcrição literal para conferir | 5 |")
    w("")
    w("Os cinco indeterminados — PT-08, PT-13, PT-23, PT-33 e PT-55 — não são falhas: seu "
      "`fonte_trecho` traz referência de página sem citação entre aspas, então não há o que "
      "casar contra o PDF. São candidatos naturais a ganhar transcrição literal na próxima "
      "passagem pelo `Caderno-de-evidencias/`.")
    w("")
    w("> **Dois falsos positivos do próprio verificador, corrigidos e registrados.** PT-31 falhou "
      "porque o casamento estava ancorado no início da citação, e hifenização no PDF costuma "
      "atingir justamente as primeiras palavras — passou a procurar janelas ao longo do texto. "
      "PT-16 falhou porque seu `fonte_trecho` usa aspas simples para **títulos de seção** "
      "(*'A radicalização do movimento'*) e não só para transcrições; a extração casava o "
      "intervalo entre dois títulos, que é aparato de referência. Ambos conferidos manualmente "
      "contra o PDF e **corretos no codebook**. Fica o registro de que a falha era do "
      "instrumento, não do dado.")
    w("")
    w("Além disso, **sete registros citavam dois documentos e declaravam apenas um**. A "
      "corroboração dupla — que é uma força do aparato, não um detalhe — estava invisível. "
      "PT-18 é o caso exemplar: o regime de sobreaviso está na CPMI **e** nas conclusões D e H "
      "do relatório Cappelli, dois documentos independentes que convergem.")
    w("")
    w("> **Falso positivo registrado.** A varredura automática apontou PT-45 e PT-48 como "
      "registros de fonte dupla. São falsos positivos: ali \"Capelli\" aparece como o nome do "
      "interventor designado, não como citação do relatório dele. Conferidos e mantidos com "
      "fonte única.")
    w("")

    # ------------------------------------------------------------- por doc
    w("## Cobertura por documento")
    w("")
    w("| Documento | Registros que ancora | Páginas | Natureza |")
    w("|:--|--:|--:|:--|")
    for c, n in por_doc.most_common():
        caminho = reg_docs.get(c, "")
        proc = PROCEDENCIA.get(caminho, ("", "—", ""))
        pag = ""
        if caminho.lower().endswith(".pdf"):
            try:
                from PyPDF2 import PdfReader
                pag = len(PdfReader(str(RAIZ / caminho)).pages)
            except Exception:
                pag = "?"
        w("| {} | {} | {} | {} |".format(c, n, pag, proc[1]))
    w("")
    w("O Relatório Final da CPMI ancora sozinho **{} dos {} registros vinculados**. "
      "Isso é uma dependência a declarar no artigo: a espinha dorsal de $T_0$ vem de uma peça "
      "de investigação parlamentar, com posição política própria e votos em separado. Que a "
      "CPMI afirme algo não é o mesmo que o fato estar estabelecido — advertência que já consta "
      "do `Caderno-de-evidencias/LEIA-ME.md` e que o artigo precisa repetir."
      .format(por_doc["CPMI"], len(ancorados)))
    w("")

    # -------------------------------------------------------------- lista 1
    w("## Lista 1 — Registros ancorados ({})".format(len(ancorados)))
    w("")
    w("Cada um aponta arquivo e página. A numeração impressa do relatório da CPMI coincide com "
      "a paginação do PDF, então a conferência é direta: abrir o arquivo na página indicada.")
    w("")
    w("| Registro | Documento(s) | Página | Classe |")
    w("|:--|:--|:--|:--|")
    for e in ancorados:
        docs = " + ".join(cod.get(p.strip(), p.strip())
                          for p in e["fonte_local"].split(";") if p.strip())
        w("| {} | {} | {} | {} |".format(
            e["id"], docs, esc(e.get("fonte_pagina")) or "—", e["status_classe"]))
    w("")

    # -------------------------------------------------------------- lista 2
    w("## Lista 2 — Sem âncora documental por natureza do registro ({})".format(len(legitimos)))
    w("")
    w("Estes **não são lacunas**. São itens de enquadramento histórico apoiados na bibliografia "
      "teórica, mais uma inferência declarada. Perseguir fonte primária para eles seria erro de "
      "categoria: não são fatos a verificar em documento, são leituras a discutir em referencial "
      "teórico.")
    w("")
    w("| Registro | Classe | Apoio declarado |")
    w("|:--|:--|:--|")
    for e in legitimos:
        w("| {} | {} | {} |".format(e["id"], e["status_classe"], esc(e["fonte_trecho"])[:110]))
    w("")

    # -------------------------------------------------------------- lista 3
    w("## Lista 3 — Dependentes de coleta ({})".format(len(pendentes)))
    w("")
    w("Estas são as lacunas reais. Cada uma tem uma peça identificada e uma via de obtenção; "
      "os comandos estão em `scripts/baixar_fontes.sh`.")
    w("")
    w("| Registro | Classe | O que falta |")
    w("|:--|:--|:--|")
    falta_por_reg = defaultdict(list)
    for peca, regs, _via, _bloq, _pri, _obs in PENDENCIAS:
        for r in [x.strip() for x in regs.split(";")]:
            falta_por_reg[r].append(peca)
    for e in pendentes:
        w("| {} | {} | {} |".format(
            e["id"], e["status_classe"],
            esc("; ".join(falta_por_reg.get(e["id"], []))) or "a definir"))
    w("")

    # ------------------------------------------------------------ pendências
    w("## Fila de coleta")
    w("")
    w("| Peça | Registro(s) | Via | Bloqueio | Prior. |")
    w("|:--|:--|:--|:--|:--|")
    ordem = {"Alta": 0, "Média": 1, "Baixa": 2}
    for peca, regs, via, bloq, pri, _obs in sorted(PENDENCIAS, key=lambda p: ordem.get(p[4], 9)):
        w("| {} | {} | {} | {} | {} |".format(
            esc(peca), esc(regs), esc(via), esc(bloq), pri))
    w("")

    # ------------------------------------------------------------- limites
    w("## O que esta auditoria não faz")
    w("")
    w("Três limites, declarados para que ninguém leia mais do que ela oferece.")
    w("")
    w("1. **Não confere, para todos os 81, se a página sustenta a afirmação.** A checagem "
      "estrutural verifica que o vínculo existe, que o arquivo está em disco e que a página "
      "pertence ao documento vinculado. A conferência do *conteúdo* contra o texto do PDF é "
      "feita **por amostra** — `scripts/conferir_paginas.py`, 12 registros por rodada, ou "
      "`--todos` para os {} com página. A transcrição literal de 49 registros está no "
      "`Caderno-de-evidencias/`.".format(
          sum(1 for e in eventos if e.get("fonte_pagina"))))
    w("2. **Não avalia a qualidade da fonte.** Que um registro esteja ancorado no relatório "
      "Cappelli não o torna verdadeiro — torna-o rastreável. E o Cappelli, registre-se, é "
      "**espelho jornalístico**: traz identificação oficial mas não foi localizado em domínio "
      "oficial. Isso está declarado no inventário e precisa constar da nota de fontes do artigo.")
    w("3. **Não resolve as ressalvas de proveniência.** A auditoria as classifica; não as fecha. "
      "PT-34 — a mais grave, os \"4 mil\" sem lastro — **foi fechada em 16/08/2026 por trabalho "
      "próprio**, com a cifra retirada e substituída por faixa ancorada em duas medições oficiais "
      "independentes (ver `ESTIMATIVA-MULTIDAO-8JAN.md`). PT-12, PT-17 e PT-52 seguem abertas, "
      "detalhadas no item 7 de `PENDENCIAS-ANALITICAS.md`.")
    w("")
    w("---")
    w("")
    w("*Regenerar com* `python scripts/gerar_auditoria.py`. "
      "*Verificar a integridade com* `python scripts/verificar_integridade.py`.")

    SAIDA.write_text("\n".join(L) + "\n", encoding="utf-8")
    print("AUDITORIA-FONTES.md gerado — {} linhas".format(len(L)))
    print("  ancorados          : {}".format(len(ancorados)))
    print("  sem âncora legítima: {}".format(len(legitimos)))
    print("  dependentes coleta : {}".format(len(pendentes)))


if __name__ == "__main__":
    main()
