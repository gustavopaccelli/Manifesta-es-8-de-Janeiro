#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Quarta rodada da tarefa 14: PT-06 fecha, e o mecanismo que ele afirmava estava datado errado.

A terceira rodada deixou PT-06 contextual DE PROPOSITO. Repertorio e
enquadramento tinham ganhado pagina em Araujo e Sales (2022), mas o MECANISMO --
"radicalizacao de bases e consolidacao de ecossistema informacional paralelo
(Telegram/WhatsApp)" -- seguia sem leitura, e o critetio fixado por PT-04 e a
cadeia causal ancorada, nao o repertorio. Ficou como item de julgamento, com a
observacao de que a peca que o fecharia estava no corpus e nao havia sido lida.

O pesquisador mandou ler. Esta rodada le:

  VON BULOW E ABERS 2024 -- "Denialism and Populism: Two Sides of a Coin in Jair
  Bolsonaro's Brazil", Government and Opposition 59:998-1016. Pagina impressa =
  PDF + 997. Cobre marco/2020 a outubro/2021 -- a janela exata de PT-06.

O MECANISMO FECHA, E A LEITURA O RETIFICA. Tres achados, em ordem de custo:

  (1) A INFRAESTRUTURA ANTECEDE A PANDEMIA, e o campo dizia o contrario. O
      codebook afirmava "consolidacao de ecossistema informacional paralelo",
      isto e, que a pandemia construiu a infraestrutura. As autoras documentam
      que "the online radical right-wing networks that had grown exponentially
      since the beginning of the 2000s became sounding boards for informational
      chaos during the pandemic" (p. 1006 impressa). A pandemia CARREGA uma
      infraestrutura que encontra pronta; nao a constroi. E a mesma forma da
      ressalva de datacao de PT-02, aplicada a outro objeto: o que o registro
      codifica e o evento, e o meio do evento e anterior a ele.

  (2) O MECANISMO QUE ELAS NOMEIAM E "CAOS INFORMACIONAL", E NAO E ECOSSISTEMA
      COERENTE. A cacofonia e constitutiva: "The fact that some of these ideas
      -- such as the massive global conspiracy theory -- seemed to contradict
      others -- such as that the disease was not really that deadly -- was not an
      issue" (p. 1006). O efeito e o que importa para a cadeia: "the circulation
      of these frames kept Bolsonaro's populist radical-right constituency in a
      state of constant mobilization" (p. 1006). Mobilizacao permanente, nao
      ecossistema.

  (3) A RADICALIZACAO TEM PAGINA, E TEM DATA. "As Bolsonaro's popularity
      plummeted in the first months of 2021, his supporters became even more
      active. They also became more extreme" (p. 1010), com a campanha "eu
      autorizo" de maio de 2021 -- autorizar o presidente a dar um golpe militar
      -- culminando no 7 de setembro de 2021. E, na conclusao, "both the
      president and bolsonaristas radicalized their rhetoric by openly calling
      for authoritarian solutions", de modo que "they blurred the boundaries
      between what Mudde (2007) called the radical right and the extreme right"
      (p. 1011).

UM ACHADO QUE NAO E DE PT-06 E VALE MAIS QUE ELE. As autoras sustentam que o
bolsonarismo e MOVIMENTO SOCIAL com autonomia relativa em relacao ao lider: o
presidente "depends on a well-organized grassroots mobilization process that
pre-dates his emergence as a populist radical-right leader and which he does not
fully control" (p. 1000), e o bolsonarismo "is part of a process of right-wing
mobilization that is larger than the leader himself, and precedes his rise to
power" (p. 1009). Isso toca a pergunta central desta pesquisa sobre o 8 de
janeiro -- mobilizacao de cima para baixo ou com autonomia -- e entra no
registro como achado, nao como campo.

O QUE CONTINUA SEM ANCORA EM PT-06, e o registro declara:

  - "guerra cultural" como rotulo. As autoras documentam a ameaca aos valores
    tradicionais e a identificacao da esquerda como inimigo, nao a expressao.
  - TELEGRAM E WHATSAPP como plataformas nomeadas. As autoras as nomeiam, mas
    por CITACAO DE SEGUNDA MAO: os 802 mensagens de WhatsApp sao de Soares et
    al. (2021) e as 867 de Telegram sao de Nascimento et al. (2020). A regra
    deste projeto proibe lastrear cifra conferida apenas contra outra citacao
    dela, e por isso nenhuma das duas entra no codebook como verificada. O que
    entra e a afirmacao propria das autoras sobre as redes e o caos.

PT-05 tambem ganha ancora, de tabela: "Since Bolsonaro took office in January of
2019, his government has promoted a state of permanent conflict with the
legislature and the judiciary" (p. 1003) -- o mecanismo de PT-05 e exatamente
isso, e a frase cobre o inicio da janela 2019-2022.

DOIS BURACOS DO HARNESS, FECHADOS ANTES DESTA RODADA (ver conferir_paginas.py):

  - APOSTROFO INTRAPALAVRA era tomado por delimitador de aspa. ASPAS_FECHA
    contem U+2019, o apostrofo de todo texto em ingles. Qualquer transcricao com
    "Bolsonaro's" era descartada EM SILENCIO. Auditado o codebook: as 57
    transcricoes entao existentes nao eram afetadas, por serem em portugues --
    nada retroativo mudou --, mas a primeira peca em ingles a ancorar registro
    caiu no buraco.
  - HIFENIZACAO DE QUEBRA DE LINHA nao era unida. norm_busca apagava o hifen e
    deixava o espaco: o PDF "mobiliza-\\ntion" normalizava para "mobiliza tion"
    e nao casava com "mobilization". Duas ancoras desta peca apareciam como nao
    localizadas tendo a frase na pagina citada.

Os dois consertos foram provados invariantes: 66 ancoras anteriores identicas,
57 de 57 transcricoes ainda vistas.

CONTAGEM ESPERADA: 61 primaria | 20 Confirmado | 1 Contextual | 1 Inferencia.
Contextuais: 7 -> 4 -> 3 -> 2 -> 1, e o que resta e PT-08, o item comparado.

Uso:
    python scripts/recodificar_pt06_bolsonarismo_movimento.py --dry-run
    python scripts/recodificar_pt06_bolsonarismo_movimento.py
"""

import io
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

BOLSO = "Fontes/13_Bolsonarismo-mobilizacao/"
AS22 = BOLSO + "ARAUJO-SALES_Atuacao-politica-das-Forcas-Armadas-e-bolsonarismo_Cadernos-do-Tempo-Presente-13-1_2022.pdf"
VB24 = BOLSO + "VON-BULOW-ABERS_Denialism-and-populism-two-sides-of-a-coin_Government-and-Opposition-59_2024.pdf"

DOCS_NOVOS = {"VON BULOW E ABERS 2024": VB24}

MUDANCAS = {
    # ------------------------------------------------------------------ PT-06
    "PT-06": {
        "mecanismo_causal": (
            "Mobilização permanente da base por circulação de enquadramentos "
            "negacionistas, e radicalização dessa base quando a popularidade do "
            "presidente desaba em 2021 — é essa base mobilizada e radicalizada que serve "
            "de reserva de contingente em T-1 Operacional. RETIFICAÇÃO DE 04/10/2026, "
            "quarta rodada da tarefa 14: o campo dizia “consolidação de ecossistema "
            "informacional paralelo (Telegram/WhatsApp)”, e a peça que agora o ancora "
            "mostra que a infraestrutura ANTECEDE a pandemia — as redes digitais da "
            "direita radical cresciam exponencialmente desde o início dos anos 2000, e a "
            "pandemia as converteu em caixa de ressonância em vez de construí-las. A "
            "pandemia carrega uma infraestrutura que encontra pronta. E o mecanismo que a "
            "literatura nomeia é CAOS INFORMACIONAL, não ecossistema coerente: a "
            "contradição entre os próprios enquadramentos é tolerada, e é a circulação "
            "deles, não a sua consistência, que mantém a base em mobilização constante"
        ),
        "framing_narrativa": (
            "'Liberdade', 'tratamento precoce', 'guerra cultural' — e, com página desde "
            "04/10/2026, a forma concreta do frame da liberdade: governos subnacionais "
            "que impuseram restrições são acusados de atacar liberdades básicas, de modo "
            "que o discurso autoritário vem embrulhado em defesa da democracia e dos "
            "direitos individuais. A expressão 'guerra cultural' permanece sem âncora nas "
            "peças lidas"
        ),
        "resposta_estatal": (
            "CPI da Pandemia (maio a outubro de 2021), cujo relatório final incluiu o "
            "presidente numa lista de 78 indiciáveis, entre eles 13 médicos e um biólogo"
        ),
        "fonte_trecho": (
            "RECODIFICADO EM 04/10/2026, QUARTA RODADA DA TAREFA 14 — o registro deixa de "
            "ser contextual, e o mecanismo que ele afirmava sai retificado. A peça: von "
            "Bülow e Abers (2024), Government and Opposition 59:998-1016, lida integral, "
            "cobrindo março de 2020 a outubro de 2021 — a janela exata deste registro. "
            "Página impressa = PDF + 997. "
            "SOBRE O MECANISMO, e é aqui que a leitura corrige o codebook: a "
            "infraestrutura informacional é ANTERIOR à pandemia — “the online radical "
            "right-wing networks that had grown exponentially since the beginning of the "
            "2000s became sounding boards for informational chaos during the pandemic” "
            "(p. 1006 impressa — PDF p. 9). O que a pandemia produz é o estado de "
            "mobilização: “the circulation of these frames kept Bolsonaro’s populist "
            "radical-right constituency in a state of constant mobilization” (p. 1006 — "
            "PDF p. 9), sustentado por “A mix of denialism, disinformation and antagonism "
            "sustained the variety of interpretations of the nature of the crisis” "
            "(p. 1006 — PDF p. 9). "
            "SOBRE A RADICALIZAÇÃO, com data: “As Bolsonaro’s popularity plummeted in the "
            "first months of 2021, his supporters became even more active. They also "
            "became more extreme” (p. 1010 impressa — PDF p. 13). A forma que ela toma é "
            "a campanha de maio de 2021: “The words refer to authorizing the president to "
            "carry out a military coup to force subnational governments to end shutdown "
            "policies” (p. 1010 — PDF p. 13). E, na conclusão, “both the president and "
            "bolsonaristas radicalized their rhetoric by openly calling for authoritarian "
            "solutions” (p. 1011 impressa — PDF p. 14), de modo que “they blurred the "
            "boundaries between what Mudde (2007) called the radical right and the "
            "extreme right” (p. 1011 — PDF p. 14). "
            "SOBRE O REPERTÓRIO: “Disinformation campaigns were coupled with traditional "
            "social movement routines, such as street protests” (p. 1010 — PDF p. 13), e "
            "“During much of 2020 and parts of 2021, weekly demonstrations were held in "
            "front of Congress in support of the president” (p. 1010 — PDF p. 13). O "
            "fechamento do arco com o apelo militar: “Authoritarian references to military "
            "intervention and populist identification of the left as the enemy thus joined "
            "up with denialism on the streets” (p. 1010 — PDF p. 13), e “Protests "
            "organized by government supporters called for the military to intervene in "
            "support of the president and against the legislature and the judiciary” "
            "(p. 1003 impressa — PDF p. 6). "
            "SOBRE O ENQUADRAMENTO DA LIBERDADE: “Bolsonaro and the radical right accused "
            "subnational governments that imposed COVID restrictions of attacking basic "
            "freedoms” (p. 1000 impressa — PDF p. 3), e “the odd combination of "
            "authoritarianism and a discourse of freedom appeared in the frequent "
            "mobilizations in favour of Bolsonaro during the pandemic” (p. 1003 — PDF "
            "p. 6). "
            "SOBRE A RESPOSTA ESTATAL: “the final report of a Senate inquiry into the "
            "government’s handling of the pandemic included the president in a list of 78 "
            "individuals who should be indicted” (p. 998 impressa — PDF p. 1), e “Meeting "
            "from May to October 2021, the inquiry broadly publicized accusations of "
            "corruption and inefficiency in the acquisition and distribution of vaccines” "
            "(p. 1008 impressa — PDF p. 11). "
            "ACHADO QUE EXCEDE ESTE REGISTRO E VALE PARA A PESQUISA INTEIRA: o "
            "bolsonarismo é tratado como MOVIMENTO SOCIAL com autonomia relativa em "
            "relação ao líder. O presidente “depends on a well-organized grassroots "
            "mobilization process that pre-dates his emergence as a populist "
            "radical-right leader and which he does not fully control” (p. 1000 impressa "
            "— PDF p. 3), e “bolsonarismo is part of a process of right-wing mobilization "
            "that is larger than the leader himself, and precedes his rise to power” "
            "(p. 1009 impressa — PDF p. 12). "
            "MANTIDO DA TERCEIRA RODADA, e continua ancorando repertório e enquadramento: "
            "“diversos atos e motociatas ocorreram com o intuito de legitimar as "
            "hostilidades do mandatário em relação aos membros dos outros poderes "
            "constitucionais” (Araujo e Sales, 2022, p. 33 impressa — PDF p. 8); "
            "“A multiplicidade de pautas políticas postuladas nos atos do sete de setembro "
            "destacou-se” e “os pleitos da liberdade de expressão e do voto impresso "
            "auditável” (p. 33 impressa — PDF p. 8). A mesma página registra a "
            "reivindicação do tratamento precoce e do kit Covid — hidroxicloroquina, "
            "azitromicina e ivermectina —, sem aspas aqui de propósito, porque na fonte a "
            "expressão já vem aspada. "
            "CESARINO (2022), declarada no registro original, ENTROU no corpus em "
            "04/10/2026 e CONTINUA NÃO LIDA."
        ),
        "fonte_local": AS22 + "; " + VB24,
        "fonte_pagina": ("ARAUJO E SALES 2022: 8 | VON BULOW E ABERS 2024: 1, 3, 6, 9, "
                         "11, 12, 13, 14"),
        "status_verificacao": (
            "Confirmado em literatura revisada por pares, lida na fonte com página: von "
            "Bülow e Abers (2024, p. 998, 1000, 1003, 1006, 1008, 1009, 1010 e 1011 "
            "impressas) e Araujo e Sales (2022, p. 33 impressa). O registro passou de "
            "Contextual a Confirmado em 04/10/2026, na quarta rodada, pelo mesmo critério "
            "que promoveu PT-04 e PT-05: a CADEIA CAUSAL que ele afirma está ancorada. A "
            "terceira rodada o havia mantido contextual justamente por esse critério, "
            "quando só repertório e enquadramento tinham página — e a peça que faltava era "
            "esta. "
            "O MECANISMO FOI RETIFICADO PELA LEITURA, não apenas ancorado: o campo "
            "afirmava consolidação do ecossistema informacional durante a pandemia, e as "
            "autoras documentam que as redes cresciam desde o início dos anos 2000. A "
            "pandemia carrega infraestrutura anterior; o que ela produz é mobilização "
            "constante. "
            "O QUE CONTINUA SEM ÂNCORA, e são duas coisas nomeadas. (1) A expressão "
            "“guerra cultural”: as autoras documentam a ameaça aos valores tradicionais e "
            "a identificação da esquerda como inimigo, não o rótulo. (2) TELEGRAM E "
            "WHATSAPP como plataformas medidas: as autoras as nomeiam, mas por CITAÇÃO DE "
            "SEGUNDA MÃO — as 802 mensagens de WhatsApp são de Soares et al. (2021) e as "
            "867 de Telegram são de Nascimento et al. (2020), nenhum dos dois no corpus. A "
            "regra deste projeto proíbe lastrear cifra conferida apenas contra outra "
            "citação dela, e por isso nenhuma das duas entra como verificada. O que entra "
            "é a afirmação própria das autoras sobre as redes e o caos informacional. "
            "LIMITE DE PERÍODO DECLARADO: a peça termina em outubro de 2021. A ponte para "
            "os acampamentos de novembro de 2022 (PT-12) não é feita por ela; o que ela "
            "entrega é a base mobilizada e radicalizada que chega a 2022."
        ),
        "status_classe": "Confirmado",
        "+nota_auditoria": (
            " QUARTA RODADA, 04/10/2026 — PASSOU DE CONTEXTUAL A CONFIRMADO, e a nota da "
            "terceira rodada previa exatamente este caminho: ela declarou que a peça que "
            "fecharia o registro estava no corpus e não havia sido lida, e nomeou qual. O "
            "pesquisador mandou lê-la. Von Bülow e Abers (2024) cobrem março de 2020 a "
            "outubro de 2021 — a janela exata do registro — e ancoram a cadeia causal, que "
            "é o critério. "
            "MAS A LEITURA NÃO SÓ ANCOROU: RETIFICOU. O mecanismo afirmava “consolidação "
            "de ecossistema informacional paralelo (Telegram/WhatsApp)”, e as autoras "
            "documentam que as redes da direita radical online cresciam exponencialmente "
            "desde o início dos anos 2000 e que a pandemia as converteu em caixa de "
            "ressonância. **A infraestrutura é anterior ao evento que o registro "
            "codifica** — mesma forma da ressalva de datação de PT-02, aplicada a outro "
            "objeto, e pela segunda vez na mesma tarefa. Se a retificação não fosse feita, "
            "o registro teria ganhado página para uma afirmação que a página contradiz, "
            "que é o modo de falha deste projeto na sua forma mais difícil de ver: a "
            "âncora certa sustentando o enunciado errado. "
            "E o nome do mecanismo mudou de natureza: “caos informacional” é o que as "
            "autoras nomeiam, e não é ecossistema coerente — a cacofonia é constitutiva, "
            "porque a contradição entre os enquadramentos é tolerada. "
            "DUAS COISAS SEGUEM DECLARADAS SEM ÂNCORA: o rótulo “guerra cultural”, e as "
            "plataformas Telegram e WhatsApp como medidas — estas porque a peça as reporta "
            "por citação de segunda mão, e a regra do projeto não admite lastro nessa "
            "forma. CESARINO (2022) continua no corpus e não lida."
        ),
    },
    # ------------------------------------------------------------------ PT-05
    "PT-05": {
        "+fonte_trecho": (
            " ACRÉSCIMO DE 04/10/2026, QUARTA RODADA — von Bülow e Abers (2024) dão ao "
            "mecanismo deste registro a frase mais direta que o corpus tem, e ela cobre o "
            "início da janela: “Since Bolsonaro took office in January of 2019, his "
            "government has promoted a state of permanent conflict with the legislature "
            "and the judiciary” (p. 1003 impressa — PDF p. 6). Sobre o conteúdo do "
            "enquadramento antijudicial, que o registro rotula sem âncora: “such Supreme "
            "Court decisions fuelled pro-government arguments that the president was being "
            "usurped of his powers by the political establishment” (p. 1005 impressa — PDF "
            "p. 8) — é o conteúdo, não o rótulo."
        ),
        "+fonte_local": "; " + VB24,
        "+fonte_pagina": " | VON BULOW E ABERS 2024: 6, 8",
        "+status_verificacao": (
            " ACRÉSCIMO DE 04/10/2026, quarta rodada: o mecanismo ganhou segunda âncora, "
            "em peça que cobre todo o período — von Bülow e Abers (2024, p. 1003 "
            "impressa) descrevem “permanent conflict with the legislature and the "
            "judiciary” desde janeiro de 2019. Os dois rótulos de framing_narrativa "
            "CONTINUAM sem âncora: a peça documenta o argumento de que o presidente era "
            "usurpado de seus poderes pelo establishment político (p. 1005 impressa), que "
            "é o conteúdo do enquadramento, não as expressões “STF ditador” e “ativismo "
            "judicial”."
        ),
        "+nota_auditoria": (
            " QUARTA RODADA, 04/10/2026 — segunda âncora para o mecanismo, de peça que "
            "cobre 2019-2022 por inteiro, e que entrou no corpus para fechar PT-06. "
            "Corroboração dupla: Araujo e Sales (2022) e von Bülow e Abers (2024) "
            "descrevem o mesmo atrito deliberado com os outros poderes, de fontes e "
            "literaturas distintas. Os dois rótulos de enquadramento seguem declarados "
            "sem âncora, e isso não mudou."
        ),
    },
}

NOTA_REVISAO = (
    "2026-10-04 (tarefa 14, QUARTA rodada) — PT-06 fecha, e o mecanismo que ele afirmava "
    "sai RETIFICADO. Lida von Bülow e Abers (2024, Government and Opposition 59:998-1016), "
    "por encaminhamento do pesquisador: é a peça que a terceira rodada havia nomeado como "
    "a que fecharia o registro, e cobre março/2020 a outubro/2021, a janela exata de "
    "PT-06. O campo afirmava “consolidação de ecossistema informacional paralelo "
    "(Telegram/WhatsApp)”; as autoras documentam que as redes da direita radical online "
    "cresciam exponencialmente DESDE O INÍCIO DOS ANOS 2000 e que a pandemia as converteu "
    "em caixa de ressonância — a infraestrutura é anterior ao evento codificado, mesma "
    "forma da ressalva de datação de PT-02. O mecanismo passou a ser mobilização "
    "permanente e radicalização da base, com o nome que a literatura dá ao meio: caos "
    "informacional, que é cacofonia e não ecossistema coerente. PT-06: Contextual -> "
    "Confirmado, pelo critério de PT-04 e PT-05 — cadeia causal ancorada. Declarados sem "
    "âncora: o rótulo “guerra cultural” e as plataformas Telegram e WhatsApp como medidas, "
    "estas porque a peça as reporta por citação de segunda mão (Soares et al. 2021; "
    "Nascimento et al. 2020), e a regra do projeto não admite lastro nessa forma. PT-05 "
    "ganhou segunda âncora para o mesmo mecanismo, em corroboração dupla. Achado que "
    "excede os dois registros: as autoras sustentam que o bolsonarismo é MOVIMENTO SOCIAL "
    "com autonomia relativa, um processo que “precedes his rise to power” e que o líder "
    "“does not fully control” — o que toca diretamente a pergunta desta pesquisa sobre "
    "mobilização de cima para baixo. Contagem de contextuais: 2 -> 1, e o que resta é "
    "PT-08, o item comparado. Corpus inalterado em 52 PDFs / 10.207 páginas; documental em "
    "22 / 6.951. Dois buracos do harness fechados antes desta rodada, com invariância "
    "provada: apóstrofo intrapalavra deixou de ser delimitador de aspa, e a hifenização de "
    "quebra de linha passou a ser unida em norm_busca."
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
        print("  metadados revisoes += nota da quarta rodada")
        if not seco:
            dados["metadados"]["revisoes"].append(NOTA_REVISAO)
        tocados += 1
    return tocados


def main():
    seco = "--dry-run" in sys.argv
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    print("RECODIFICAÇÃO — quarta rodada, PT-06 e o mecanismo retificado{}".format(
        "  (SECO)" if seco else ""))
    print("=" * 78)
    n = aplicar(dados, seco)
    print("-" * 78)
    print("{} alteração(ões)".format(n))
    if not seco and n:
        # newline="\n" é obrigatório: o .gitattributes traz `* -text`, isto é,
        # nenhuma conversão. Sem isso o Python no Windows grava CRLF e o git
        # mostra as ~1.600 linhas do codebook como alteradas.
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
