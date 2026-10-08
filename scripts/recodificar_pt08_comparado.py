#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PT-08 sai de contextual, e com ele o ultimo contextual do codebook.

PT-08 era o unico registro que restava em `Contextual` depois que a tarefa 14
fechou a camada conjuntural brasileira em 04/10/2026. A lacuna dele nunca foi
brasileira: era literatura comparada sobre o 6 de janeiro norte-americano, que
nenhuma das dezoito pecas do eixo 13 cobria.

O pesquisador entregou as duas pecas em 08/10/2026, depois que a coleta
automatizada falhou nas duas -- a MDPI por um interstitial do Akamai Bot Manager
e a SAGE por nao ter o PDF em deposito algum.

  CASTANEDA E JENKS 2023 -- "January 6th and De-Democratization in the United
  States", Social Sciences 12(4):238, MDPI, CC-BY, 15 p. **SEM PAGINACAO
  IMPRESSA**: a MDPI pagina por numero de artigo, nao por intervalo no fasciculo,
  e o cabecalho corrente e "Soc. Sci. 2023, 12, 238". Cita-se pela pagina do PDF.

  CHEN, LUKITO E KOO 2023 -- "Comparing the #StopTheSteal Movement across
  Multiple Platforms", Social Media + Society 9(3):1-13, CC BY-NC, 13 p.
  Pagina impressa = PDF + 0, LIDO (a p. 2 imprime "2", a p. 13 imprime "13").
  **Tres autores**, e o CSV da camada A nomeava zero.

O QUE CADA UMA ANCORA, e a divisao e nitida:

  CHEN, LUKITO E KOO ancoram o EVENTO e o ENQUADRAMENTO. Comparam 675.336 posts
  de Facebook, Twitter e Parler entre 1/09/2020 e 1/02/2021 aplicando a
  tipologia de enquadramentos de acao coletiva de **Snow e Benford** --
  diagnostico, prognostico e motivacional, mais um dispositivo proprio, pistas
  de violencia. Snow e Benford sao marco teorico declarado deste projeto, de
  modo que a peca fala a lingua do codebook. Nao dizem uma palavra sobre o
  Brasil: zero ocorrencias de "Brazil", "Bolsonaro", "January 8".

  CASTANEDA E JENKS ancoram o MECANISMO, e e por isso que PT-08 fecha. A frase:
  "The attack on congress to contest an election has now become a contentious
  performance that was used by the equivalent actors in Brazil on January 8,
  2023" (PDF p. 10). E a afirmacao de difusao que o registro precisa -- e vem no
  vocabulario de Tilly, "performance contenciosa", com agente de transmissao
  nomeado: "Both events occurred with the encouragement of Steve Bannon and
  similar agents of chaos" (PDF p. 10).

UM ALERTA DE METODO QUE ESTA RODADA PRODUZIU. Para decidir se a peca servia, eu
contei termos no texto integral: "Bolsonaro" 0, "diffusion" 0, "emulation" 0,
"transnational" 0, "Brazil" 1. A medicao estava certa e a conclusao que ela
sugeria -- a peca nao serve -- estava ERRADA: a unica ocorrencia de "Brazil" e
exatamente a frase que o registro precisa. **Um autor pode afirmar a proposicao
inteira sem usar nenhuma das palavras com que voce a nomeia.** Decima quinta
ocorrencia do modo de falha do projeto.

O LIMITE QUE O REGISTRO PASSA A DECLARAR: a ligacao com o Brasil e feita em UMA
frase, de passagem, sem aparato de evidencia do lado brasileiro. Castaneda e
Jenks escrevem sobre os Estados Unidos; o Brasil aparece como comparacao. E
ressalva da mesma natureza que "um estado so, serie ate 2015" em Fernandes e
Silva (2021).

E A RESSALVA DO SRI LANKA NAO SO SOBREVIVE: FICA REFORCADA. O registro ja dizia
que o precedente invocado pelos organizadores como "Plano B" foi a revolta do
Sri Lanka, nao o Capitolio -- o Capitolio como referencia de REPERTORIO, o Sri
Lanka como referencia de EFICACIA (CPMI, p. 614). Castaneda e Jenks dizem
exatamente que o ataque ao Congresso se tornou uma *performance contenciosa*
usada no Brasil, o que e afirmacao de repertorio. As duas leituras se encaixam.

CONTAGEM ESPERADA: 61 primaria | 21 Confirmado | 0 Contextual | 1 Inferencia.
**Nao resta nenhum registro contextual no codebook.**

Uso:
    python scripts/recodificar_pt08_comparado.py --dry-run
    python scripts/recodificar_pt08_comparado.py
"""

import io
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

COMP = "Fontes/15_Comparado-6-de-janeiro/"
CJ23 = COMP + "CASTANEDA-JENKS_January-6th-and-de-democratization_Social-Sciences-12-4_2023.pdf"
CLK23 = (COMP + "CHEN-LUKITO-KOO_Comparing-the-StopTheSteal-movement-across-platforms_"
         "Social-Media-and-Society-9-3_2023.pdf")
CPMI = "Fontes/04_T+1_Resposta-institucional/CPMI-8-de-Janeiro_Relatorio-Final_2023-10-17.pdf"

DOCS_NOVOS = {
    "CASTANEDA E JENKS 2023": CJ23,
    "CHEN LUKITO E KOO 2023": CLK23,
}

MUDANCAS = {
    "PT-08": {
        "ator_grupo": (
            "Apoiadores de Donald Trump (EUA) — o movimento “Stop the Steal”, organizado "
            "através de plataformas digitais e não por estrutura partidária"
        ),
        "resposta_estatal": (
            "Resposta judicial nos EUA; e a comissão especial da Câmara, cujo relatório é "
            "citado pela literatura lida"
        ),
        "fonte_trecho": (
            "RECODIFICADO EM 08/10/2026 — o registro deixa de ser contextual, e com ele sai "
            "o último contextual do codebook. Duas peças entregues pelo pesquisador depois "
            "que a coleta automatizada falhou nas duas. "
            "SOBRE O EVENTO E O ENQUADRAMENTO, em Chen, Lukito e Koo (2023), que comparam "
            "675.336 posts de Facebook, Twitter e Parler entre 1/09/2020 e 1/02/2021: os "
            "esforços para reverter o resultado “culminated in the storming of Capitol Hill "
            "on 6 January 2021, endangering the democratic process” (PDF p. 1). O desenho: "
            "“we compared posts about #StopTheSteal from three social media platforms after "
            "the 2020 US Presidential election and preceding the January 6 Capitol Riot” "
            "(PDF p. 1). E o que a peça sustenta sobre a infraestrutura da mobilização: "
            "“this study highlights their use of different social media platforms to "
            "disseminate election-related disinformation, mobilize supporters” (PDF p. 1). "
            "A transcrição para aí de propósito: a frase da fonte prossegue falando em "
            "reforçar as identidades políticas e o nacionalismo do grupo, e o apóstrofo de "
            "posse que ela usa seria lido como aspa de fechamento por transcricoes(). A "
            "peça aplica a tipologia de enquadramentos de ação coletiva de SNOW E BENFORD — "
            "diagnóstico, prognóstico e motivacional, mais um dispositivo próprio, pistas de "
            "violência —, que é marco teórico declarado deste projeto. "
            "SOBRE O MECANISMO, e é a âncora que fecha o registro, em Castañeda e Jenks "
            "(2023): “The attack on congress to contest an election has now become a "
            "contentious performance that was used by the equivalent actors in Brazil on "
            "January 8, 2023” (PDF p. 10). Com agente de transmissão nomeado: “Both events "
            "occurred with the encouragement of Steve Bannon and similar agents of chaos” "
            "(PDF p. 10). E com o escopo que os autores dão ao processo: “De-democratization "
            "is not unique to the United States and has been happening in many countries for "
            "years” (PDF p. 10). "
            "SOBRE A LEITURA DO 6 DE JANEIRO QUE A PEÇA PROPÕE, e que é a razão de ela estar "
            "no corpus: “we argue that January 6th was not an individual event in a vacuum "
            "nor purely the result of Trump’s ego” (PDF p. 4), e “Trump’s rise to power and "
            "the riots on January 6th were symptoms of a longer process of "
            "de-democratization” (PDF p. 4). O quadro é o de Charles Tilly — democratização "
            "e desdemocratização como processo, não como estado. "
            "MANTIDO, E É O QUE O PROJETO TEM DE PRÓPRIO AQUI: a CPMI (p. 614) mostra que o "
            "precedente efetivamente invocado pelos organizadores como Plano B não foi o "
            "Capitólio, e sim a revolta do Sri Lanka de julho de 2022. Ver PT-19. "
            "AS OBRAS DECLARADAS NO REGISTRO ORIGINAL — Levitsky e Ziblatt; Norris e "
            "Inglehart — CONTINUAM FORA DO CORPUS e não foram lidas."
        ),
        "fonte_local": CPMI + "; " + CJ23 + "; " + CLK23,
        "fonte_pagina": ("CPMI: 614 | CASTANEDA E JENKS 2023: 4, 10 | "
                         "CHEN LUKITO E KOO 2023: 1"),
        "status_verificacao": (
            "Confirmado em literatura revisada por pares, lida na fonte com página — "
            "Castañeda e Jenks (2023, PDF p. 4 e 10) e Chen, Lukito e Koo (2023, PDF p. 1) "
            "—, e o modelo efetivamente invocado pelos organizadores continua confirmado em "
            "FONTE PRIMÁRIA: CPMI, p. 614 (ver PT-19). O registro passou de Contextual a "
            "Confirmado em 08/10/2026, pelo mesmo critério que promoveu PT-04, PT-05 e "
            "PT-06: a cadeia causal que ele afirma está ancorada. **Com ele, o codebook "
            "deixa de ter registro contextual.** "
            "DOIS LIMITES DECLARADOS, e o primeiro é sério. (1) A ligação com o Brasil é "
            "feita por Castañeda e Jenks em UMA FRASE, DE PASSAGEM, sem aparato de evidência "
            "do lado brasileiro: o artigo é sobre os Estados Unidos e o Brasil entra como "
            "comparação. A frase é explícita e usa o vocabulário de Tilly — performance "
            "contenciosa usada pelos atores equivalentes no Brasil —, mas é uma frase, e o "
            "registro não finge que é um estudo comparado. (2) Chen, Lukito e Koo NÃO "
            "tratam do Brasil: zero ocorrências de “Brazil”, “Bolsonaro” e “January 8”. "
            "Ancoram o evento norte-americano e o enquadramento, não a difusão. "
            "O QUE O REGISTRO NÃO REIVINDICA: nenhuma das duas peças documenta o lado "
            "brasileiro da emulação. Esse lado está em PT-19 e nos registros de T-1 "
            "operacional, em fonte primária. "
            "NOTA DE PAGINAÇÃO: Castañeda e Jenks NÃO TEM PAGINAÇÃO IMPRESSA — a MDPI pagina "
            "por número de artigo (12(4):238), não por intervalo no fascículo, e o cabeçalho "
            "corrente é Soc. Sci. 2023, 12, 238. As páginas citadas são do PDF. Chen, "
            "Lukito e Koo tem impressa = PDF + 0, lido no rótulo da própria página."
        ),
        "status_classe": "Confirmado",
        "+nota_auditoria": (
            " | RECODIFICADO EM 08/10/2026 — PASSOU DE CONTEXTUAL A CONFIRMADO, e era o "
            "ÚLTIMO contextual do codebook. A lacuna nunca foi brasileira: era literatura "
            "comparada sobre o 6 de janeiro norte-americano, que nenhuma das dezoito peças "
            "do eixo 13 cobria — nem Bastos e Recuero (2023), que trata do Congresso "
            "brasileiro e não do Capitólio. As duas peças vieram do eixo 15, aberto no mesmo "
            "dia, e foram entregues pelo pesquisador depois que a coleta automatizada falhou "
            "nas duas. "
            "UM ALERTA DE MÉTODO QUE ESTA RODADA PRODUZIU, e é mais útil que a âncora: para "
            "decidir se Castañeda e Jenks servia, contei termos no texto integral — "
            "“Bolsonaro” 0 ocorrências, “diffusion” 0, “emulation” 0, “transnational” 0, "
            "“Brazil” 1. A medição estava certa e a conclusão que ela sugeria, a de que a "
            "peça não servia, estava ERRADA: a única ocorrência de “Brazil” é exatamente a "
            "frase que o registro precisava, dita no vocabulário de Tilly em vez das "
            "palavras com que eu a nomeio. **Um autor pode afirmar a proposição inteira sem "
            "usar nenhuma das palavras com que você a nomeia** — contagem de termo é medida "
            "de palavra, não de proposição. É a irmã semântica da armadilha da ligadura ﬁ, e "
            "por pouco não produziu um descarte confiante e falso. "
            "A RESSALVA DO SRI LANKA FICA REFORÇADA, não contrariada: o Capitólio é "
            "referência de REPERTÓRIO e o Sri Lanka é referência de EFICÁCIA, e dizer que o "
            "ataque ao Congresso “se tornou uma performance contenciosa usada pelos atores "
            "equivalentes no Brasil” é precisamente uma afirmação de repertório."
        ),
    },
}

NOTA_REVISAO = (
    "2026-10-08 — PT-08 sai de contextual, e com ele o ÚLTIMO contextual do codebook: as "
    "classes passam a 61 em fonte primária, 21 confirmados, ZERO contextuais e 1 inferência "
    "declarada. Duas peças entregues pelo pesquisador e lidas na fonte, no eixo 15 "
    "(Comparado 6 de janeiro), aberto no mesmo dia: Castañeda e Jenks (2023, Social "
    "Sciences 12(4):238) e Chen, Lukito e Koo (2023, Social Media + Society 9(3):1-13). "
    "Chen, Lukito e Koo ancoram o evento e o enquadramento, aplicando a tipologia de Snow e "
    "Benford, que é marco teórico declarado do projeto — e não dizem nada sobre o Brasil. "
    "Castañeda e Jenks ancoram o MECANISMO, com a frase que o registro precisava: o ataque "
    "ao Congresso “has now become a contentious performance that was used by the equivalent "
    "actors in Brazil on January 8, 2023”, com Steve Bannon nomeado como agente de "
    "transmissão. DOIS LIMITES DECLARADOS: a ligação com o Brasil é uma frase de passagem, "
    "sem aparato do lado brasileiro; e Chen, Lukito e Koo não tratam do Brasil. A ressalva "
    "do Sri Lanka (CPMI, p. 614) fica REFORÇADA: Capitólio é referência de repertório, Sri "
    "Lanka é referência de eficácia. ALERTA DE MÉTODO REGISTRADO: a contagem de termos no "
    "texto integral de Castañeda e Jenks deu zero para “diffusion”, “emulation”, "
    "“transnational” e “Bolsonaro” e um para “Brazil” — medição certa que levaria à "
    "conclusão errada, porque a única ocorrência é a frase decisiva. Contagem de termo é "
    "medida de palavra, não de proposição. Corpus: 59 -> 66 PDFs, 10.774 -> 12.089 páginas, "
    "com o eixo 14 indo a 12 peças (tarefa 10) e o eixo 15 nascendo com 2; a contagem "
    "documental continua em 22 PDFs e 6.951 páginas."
)


def aplicar(dados, seco):
    tocados = 0
    for rid, campos in MUDANCAS.items():
        ev = next((e for e in dados["eventos"] if e["id"] == rid), None)
        if ev is None:
            raise SystemExit("registro ausente: " + rid)
        for campo, valor in campos.items():
            if campo.startswith("+"):
                nome = campo[1:]
                antes = ev.get(nome) or ""
                depois = antes + valor
            else:
                nome, antes, depois = campo, ev.get(campo), valor
            if antes == depois:
                continue
            print("  {:<7} {:<20} {} -> {} car.".format(
                rid, nome, len(antes or ""), len(depois)))
            if not seco:
                ev[nome] = depois
            tocados += 1
    reg = dados["metadados"]["registro_documentos"]
    for cod, caminho in DOCS_NOVOS.items():
        if reg.get(cod) == caminho:
            continue
        print("  metadados registro_documentos += {}".format(cod))
        if not seco:
            reg[cod] = caminho
        tocados += 1
    if NOTA_REVISAO not in dados["metadados"]["revisoes"]:
        print("  metadados revisoes += nota de 08/10")
        if not seco:
            dados["metadados"]["revisoes"].append(NOTA_REVISAO)
        tocados += 1
    return tocados


def main():
    seco = "--dry-run" in sys.argv
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    print("RECODIFICAÇÃO — PT-08, o último contextual{}".format(
        "  (SECO)" if seco else ""))
    print("=" * 78)
    n = aplicar(dados, seco)
    print("-" * 78)
    print("{} alteração(ões)".format(n))
    if not seco and n:
        # newline="\n" é obrigatório: o .gitattributes traz `* -text`.
        with io.open(JSON_P, "w", encoding="utf-8", newline="\n") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print("gravado: {}".format(JSON_P.name))
        classes = {}
        for e in dados["eventos"]:
            classes[e.get("status_classe")] = classes.get(e.get("status_classe"), 0) + 1
        print("classes: " + " | ".join(
            "{} {}".format(v, k) for k, v in sorted(classes.items(), key=lambda x: -x[1])))


if __name__ == "__main__":
    main()
