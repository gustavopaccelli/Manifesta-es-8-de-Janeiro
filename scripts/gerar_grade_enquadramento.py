#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A GRADE FUNCIONAL DE `framing_narrativa` — inferencia declarada, gerada.

Emite: docs/referencial/02_GRADE-FUNCIONAL-ENQUADRAMENTO.md

POR QUE ESTE SCRIPT EXISTE, e nao um arquivo escrito a mao. A classificacao
funcional dos 85 campos e JUIZO do analista, registro por registro -- mas as
CONTAGENS que ela produz nao podem ser contadas de cabeca, e o documento nao
pode envelhecer em silencio se o codebook mudar. Entao o juizo vive no
dicionario `G` abaixo, versionado e auditavel, e tudo o que e cifra sai dele.

AS TRES GUARDAS, e cada uma ja pegou algo:
  1. todo id do codebook tem de estar em `G`, e nenhum id de `G` pode faltar no
     codebook -- pega registro novo ou removido;
  2. a classificacao "0" (campo vazio) tem de casar com campo REALMENTE vazio no
     codebook, nos dois sentidos -- pega campo que deixou de ser vazio;
  3. desafiante + estatal + misto tem de somar os que TEM quadro -- e esta pegou
     um defeito meu na primeira execucao, que imprimia "28 dos 62" com 28 que
     nao era subconjunto de 62, porque incluia os 4 `N` e dois rotulos de ator
     tinham caido fora das listas.

O ENCAMINHAMENTO QUE O AUTORIZA, do pesquisador em 21/10/2026: "Classificarei
essa funcao na escrita. Por enquanto, pode inferir as possiveis funcoes que
julgar importantes analiticamente." E, no mesmo dia: "resolva isso criando um
documento proprio. Nao interfira no levantamento dos eventos." Logo NADA disto
entra no codebook -- criar campo e decisao dele.

Rodado como passo do ciclo desde 21/10/2026. Uso: python scripts/gerar_grade_enquadramento.py
"""
import io
import json
import os
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

# id -> (ator do quadro, funcoes, observacao)
#   D = diagnostico (problematizacao + atribuicao de culpa)
#   P = prognostico (a solucao proposta)
#   M = motivacional (razao para agir)
#   C = contraquadro / disputa de quadro
#   0 = campo vazio no codebook
#   N = nao e quadro de acao coletiva
G = {
    "PT-01":  ("desafiante", "", "ausência MEDIDA, não vazio: a literatura lida registra que nenhum quadro unificou o ciclo"),
    "PT-01A": ("partido derrotado", "DP", "dúvida sobre a urna é diagnóstico; voto impresso é o remédio, e aparece só no relatório de 2015"),
    "PT-01B": ("partido da base", "DP", "a crise como 'grave risco' é diagnóstico; as reformas estruturais são o prognóstico"),
    "PT-02":  ("contramovimento", "DPM", "'SOS Forças Armadas' já em março de 2015 é FRAME DE RECRUTAMENTO, não demanda do ciclo"),
    "PT-02A": ("tribunal", "C", "díade: 'efetividade da jurisdição' × 'presunção de inocência'"),
    "PT-03":  ("coalizão parlamentar", "P", "'legalidade constitucional' legitima a via adotada"),
    "PT-03A": ("Judiciário/MPF", "D", "'combate à corrupção' nomeia o problema e o culpado"),
    "PT-03B": ("tribunal", "DC", "'confirmação da Justiça' com o contraquadro 'lawfare' no mesmo campo"),
    "PT-03C": ("tribunal", "C", "díade, e a decisão foi 6×5"),
    "PT-03D": ("campos opostos", "C", "'ninguém está acima da lei' × 'preso político'"),
    "PT-03E": ("tribunal eleitoral", "C", "'Ficha Limpa' × 'cassação da soberania popular'"),
    "PT-04":  ("movimento no governo", "DP", "'anti-sistema' é diagnóstico; 'nova política' é prognóstico"),
    "PT-05":  ("Executivo/base", "D", "'STF ditador' atribui culpa a instituição nomeada"),
    "PT-05A": ("tribunal", "C", "'presunção de inocência' × 'impunidade'"),
    "PT-06":  ("Executivo/base", "DP", "'liberdade' é diagnóstico; 'tratamento precoce' é prognóstico explícito"),
    "PT-06A": ("tribunal/campo", "C", "'vício de competência' × 'anulação por tecnicalidade, não inocência'"),
    "PT-06B": ("tribunal/campo", "C", "díade"),
    "PT-06C": ("tribunal/campo", "C", "díade"),
    "PT-07":  ("núcleo político", "D", "'fraude nas urnas' é O quadro diagnóstico do caso — e a PGR o declara FALSO"),
    # OS DOIS DA CONTRAMOBILIZACAO, 29/10/2026 (item 102). Sao `C` por
    # definicao do capitulo: contraquadro e o quadro que DISPUTA outro, e os
    # dois disputam o de PT-07.
    #
    # E OS ROTULOS DE ATOR SAO OS QUE O CONJUNTO JA TINHA -- `partido` e
    # `setor economico`. Eu havia escrito dois rotulos novos e o `assert`
    # derrubou o ciclo, que e o comportamento certo: a taxonomia ja tem casa
    # para ator coletivo nao estatal, e inventar rotulo seria crescer o
    # vocabulario sem necessidade.
    #
    # LIMITE QUE VALE ESCRITO: o conjunto se chama DESAFIANTE e **estes dois
    # sao do campo OPOSTO ao desafiante**. O nome do conjunto e mais estreito
    # do que o que ele guarda -- ele ja abrigava `contramovimento`, `campo
    # derrotado` e `movimento estrangeiro` --, e a prosa gerada diz
    # "desafiante OU DO CAMPO", que e a formula que cobre isso. O conjunto
    # separa ator ESTATAL de ator NAO ESTATAL, nao um campo do outro.
    "PT-07A": ("partido", "C",
               "disputa o quadro de fraude de PT-07, no dia seguinte à ameaça"),
    "PT-07B": ("setor econômico", "C",
               "disputa o mesmo quadro, e a folha atribui o motivo a interesse ameaçado"),
    "PT-08":  ("movimento estrangeiro", "DM", "'Stop the Steal' diagnostica e convoca na mesma frase"),
    "PT-08A": ("Estado", "D", "'combate à compra de votos' — diagnóstico PRETEXTUAL, recusado pela própria PF na Bahia"),
    "PT-08B": ("tribunal eleitoral", "P", "'garantia do exercício do voto' é o remédio que a ordem impõe"),
    "PT-08C": ("Estado", "P", "'fiscalização de rotina' justifica o ato; a mensagem interna desmente o quadro"),
    "PT-09":  ("—", "0", ""),
    "PT-10":  ("desafiante", "D", "'fraude eleitoral' e recusa do resultado"),
    "PT-10A": ("setor econômico", "DPM", "contestação da lisura, apoio à intervenção, e 'Eu autorizo, Presidente!' nos caminhões"),
    "PT-11":  ("liderança", "M", "agradecimento SEM reconhecimento da derrota: licencia a continuação por omissão"),
    "PT-12":  ("desafiante", "PM", "'intervenção militar' é o prognóstico; 'SOS Forças Armadas' convoca"),
    "PT-12A": ("rede de doadores", "M", "'permanência patriótica' sustenta a base acampada"),
    "PT-13":  ("Presidência", "M", "'manifestação legítima' é certificação por elite: reduz o custo de agir"),
    "PT-14":  ("partido", "D", "'fraude nas urnas eletrônicas' levado à arena institucional"),
    "PT-15":  ("desafiante", "D", "a diplomação como agravo imediato"),
    "PT-16":  ("flanco radical", "PM", "'provocar comoção para precipitar intervenção' é meio-fim explícito"),
    "PT-17":  ("—", "0", ""),
    "PT-18":  ("—", "0", ""),
    "PT-18A": ("—", "0", ""),
    "PT-19":  ("desafiante", "PM", "criptolinguagem convoca; o Sri Lanka é o modelo, isto é, o meio"),
    "PT-19A": ("desafiante", "DPM", "as três tarefas num anúncio pago — o caso mais completo do codebook"),
    "PT-19B": ("desafiante", "PM", "'Tomada de Poder' nomeia o fim e convoca"),
    "PT-20":  ("desafiante", "P", "'intervenção militar'"),
    "PT-20A": ("órgão estatal", "N", "avaliação interna de risco: não é quadro de ação coletiva"),
    "PT-20B": ("órgão estatal", "N", "relato de inteligência: não é quadro de ação coletiva"),
    "PT-21":  ("desafiante", "M", "'Festa da Selma' é convocação cifrada"),
    "PT-22":  ("—", "0", ""),
    "PT-23":  ("desafiante", "M", "convocações e incitações, com deliberação sobre a hora de marchar"),
    "PT-24":  ("desafiante", "M", "'marcha patriótica'"),
    "PT-25":  ("órgão estatal", "N", "'manifestação sob controle' é avaliação, não quadro"),
    "PT-26":  ("desafiante", "M", "'o povo no poder'"),
    "PT-27":  ("—", "0", ""),
    "PT-28":  ("—", "0", ""),
    "PT-29":  ("desafiante", "M", "'retomada do poder pelo povo'"),
    "PT-30":  ("desafiante", "M", "'casa do povo' ressignifica o alvo como próprio"),
    "PT-31":  ("—", "0", ""),
    "PT-32":  ("—", "0", ""),
    "PT-33":  ("desafiante", "M", "'ocupação do Poder Central'"),
    "PT-34":  ("desafiante", "M", "'praça do povo'"),
    "PT-35":  ("desafiante", "D", "'STF ditador' no momento da invasão do alvo que ele nomeia"),
    "PT-36":  ("desafiante", "M", "'tomada do poder'"),
    "PT-37":  ("—", "0", ""),
    "PT-38":  ("desafiante", "D", "a ordem de 1988 como o problema, atacada na sua forma material"),
    "PT-39":  ("—", "0", ""),
    "PT-40":  ("—", "0", ""),
    "PT-41":  ("—", "0", ""),
    "PT-42":  ("Executivo local", "P", "'responsabilização individual' é o remédio oferecido sob pressão"),
    "PT-43":  ("—", "0", ""),
    "PT-44":  ("—", "0", ""),
    "PT-45":  ("Estado", "P", "'defesa do Estado Democrático de Direito'"),
    "PT-46":  ("desafiante", "M", "manutenção do confronto após a perda do território"),
    "PT-47":  ("Executivo local", "N", "contrição não é nenhuma das três tarefas: é reparação reputacional"),
    "PT-48":  ("Estado", "P", "'restabelecimento da ordem'"),
    "PT-49":  ("Judiciário", "D", "o enquadramento penal É atribuição de responsabilidade"),
    "PT-50":  ("liderança", "C", "distanciamento e negação de vínculo: contraquadro do próprio líder"),
    "PT-50A": ("campo derrotado", "DC", "'infiltrados' re-atribui a culpa; 'o governo sabia' inverte o acusado"),
    "PT-51":  ("Estado", "P", "'unidade dos Poderes'"),
    "PT-52":  ("Estado", "P", "'cumprimento de ordem judicial'"),
    "PT-53":  ("Judiciário", "D", "os tipos penais nomeiam o problema e os responsáveis"),
    "PT-54":  ("Legislativo", "P", "'apuração de responsabilidades' é o procedimento proposto"),
    "PT-55":  ("Legislativo", "D", "os indiciamentos atribuem responsabilidade nominal"),
    "PT-56":  ("Judiciário", "D", "os cinco tipos da condenação"),
    "PT-57":  ("—", "0", ""),
    "PT-58":  ("—", "0", ""),
    "PT-59":  ("—", "0", ""),
    "PT-60":  ("Judiciário", "P", "'prisão domiciliar humanitária' é a medida, com fundamento clínico"),
    "PT-61":  ("Estado", "M", "'Democracia Inabalada' é motivacional INVERTIDO: dissuasão dirigida a ciclos futuros"),
    "PT-62":  ("campo derrotado", "DP", "'perseguição política' diagnostica; 'anistia' é o prognóstico"),
}

dados = json.loads(io.open("process_tracing_8jan_eventos.json",
                           encoding="utf-8").read())
ids = [e["id"] for e in dados["eventos"]]
J = {e["id"]: e for e in dados["eventos"]}

faltam = [i for i in ids if i not in G]
sobram = [i for i in G if i not in ids]
assert not faltam, "sem classificação: %s" % faltam
assert not sobram, "id inexistente: %s" % sobram

# conferir que o "0" casa com campo vazio ou "—" no codebook, e so com ele
VAZIO = {"", "—", "-"}
for i in ids:
    campo = (J[i].get("framing_narrativa") or "").strip()
    zero = G[i][1] == "0"
    if zero != (campo in VAZIO):
        raise AssertionError(
            "%s: classifiquei %r e o campo é %r" % (i, G[i][1], campo[:40]))

cont = Counter()
for _, f, _ in G.values():
    if f == "0":
        cont["0"] += 1
    elif f == "N":
        cont["N"] += 1
    elif f == "":
        cont["ausencia"] += 1
    else:
        for c in f:
            cont[c] += 1

com_quadro = sum(1 for _, f, _ in G.values() if f not in ("0", "N", ""))
multi = sum(1 for _, f, _ in G.values()
            if f not in ("0", "N", "") and len(f) > 1)
# O recorte de ATOR tem de ser subconjunto dos que TEM quadro, e nenhum rotulo
# pode cair fora da classificacao -- a primeira versao desta conta somava os 4
# `N` dentro do total de estatais e deixava dois rotulos sem casa, produzindo
# "28 dos 62" com 28 que nao era subconjunto de 62. A cifra no referente errado,
# dentro do proprio script que a emite.
DESAFIANTE = {"desafiante", "contramovimento", "setor econômico",
              "rede de doadores", "flanco radical", "partido", "liderança",
              "núcleo político", "movimento no governo", "Executivo/base",
              "campo derrotado", "movimento estrangeiro",
              "coalizão parlamentar", "partido da base", "partido derrotado"}
ESTATAL = {"Estado", "órgão estatal", "Judiciário", "tribunal",
           "tribunal eleitoral", "Legislativo", "Presidência",
           "Executivo local", "tribunal/campo", "Judiciário/MPF"}
MISTO = {"campos opostos"}
SEM = {"—"}
for a, _, _ in G.values():
    assert a in DESAFIANTE | ESTATAL | MISTO | SEM, "ator sem casa: %r" % a

tem_quadro = [(a, f) for a, f, _ in G.values() if f not in ("0", "N", "")]
desafiante = sum(1 for a, _ in tem_quadro if a in DESAFIANTE)
estatal = sum(1 for a, _ in tem_quadro if a in ESTATAL)
misto = sum(1 for a, _ in tem_quadro if a in MISTO)
assert desafiante + estatal + misto == com_quadro, (
    desafiante, estatal, misto, com_quadro)

print("TOTAL de registros classificados: %d" % len(G))
print("  com quadro de ação coletiva  : %d  (dos quais %d acumulam função)"
      % (com_quadro, multi))
print("  campo vazio no codebook      : %d" % cont["0"])
print("  não é quadro de ação coletiva: %d" % cont["N"])
print("  ausência MEDIDA              : %d" % cont["ausencia"])
print()
print("  diagnóstico  D : %d" % cont["D"])
print("  prognóstico  P : %d" % cont["P"])
print("  motivacional M : %d" % cont["M"])
print("  contraquadro C : %d" % cont["C"])
print()
print("  COM QUADRO, por ator: desafiante/campo %d | estatal %d | misto %d"
      % (desafiante, estatal, misto))

# ----------------------------------------------------------------- a secao
L = []
w = L.append
w("# A grade funcional de `framing_narrativa` — **inferência do analista**")
w("")
w("**Encaminhamento:** *\"Classificarei essa função na escrita. Por enquanto, "
  "pode inferir as possíveis funções que julgar importantes "
  "analiticamente.\"*")
w("")
w("> **ISTO É INFERÊNCIA, E A MARCA NÃO É FORMALIDADE.** A classificação "
  "abaixo é **juízo meu**, registro por registro, e **não entrou no "
  "codebook**: criar campo é decisão sua, e você disse que classifica na "
  "escrita. O que está aqui é insumo para essa decisão — e o critério está "
  "escrito, para que você possa discordar de casos sem discutir o método.")
w("")
w("## 1. O critério, e ele vem da peça lida")
w("")
w("As três **tarefas centrais de enquadramento** do capítulo de Snow, "
  "Vliegenthart e Ketelaars (2019, p. 396-397 impressas, lido integral):")
w("")
w("| Sigla | Tarefa | Definição na fonte |")
w("|:--|:--|:--|")
w("| **D** | diagnóstico | problematização **mais** *\"the attribution of "
  "blame or responsibility\"* (p. 396) |")
w("| **P** | prognóstico | o que fazer — a solução proposta (p. 396-397) |")
w("| **M** | motivacional | a razão para agir, o *call to arms* (p. 397) |")
w("")
w("E duas categorias que a própria peça obriga a acrescentar, porque o campo "
  "do codebook as contém:")
w("")
w("| Sigla | Categoria | De onde vem |")
w("|:--|:--|:--|")
w("| **C** | contraquadro / disputa de quadro | o capítulo lista "
  "**contramobilização** entre as três funções de mobilização (p. 395) e "
  "**disputas de quadro** entre os quatro riscos de enquadramento (p. 403-404) |")
w("| **N** | não é quadro de ação coletiva | o capítulo define as três "
  "tarefas para **quadros de movimento**; avaliação interna de órgão e "
  "contrição reputacional não são nenhuma das três |")
w("")
w("> **A extensão, e ela DEIXOU DE SER ANALOGIA MINHA EM 28/10/2026:** as "
  "três tarefas foram formuladas para quadros **de movimento**, e dos {} "
  "registros com quadro **{} são de desafiante ou do campo, {} são de ator "
  "estatal** — tribunal, Judiciário, Legislativo, Executivo — e {} é díade "
  "entre campos opostos. Até 28/10 eu declarava isto como **extensão por "
  "analogia**, mantida porque a simetria é analiticamente útil — um tipo "
  "penal *é* atribuição de responsabilidade, que é a definição de "
  "diagnóstico. **A leitura de Kriesi, Hutter e Bojár (2019) deu a ela "
  "autorização por citação:** a `Contentious Episode Analysis` existe, "
  "entre outras razões, para ir além do foco estreito nas ações de "
  "protesto dos desafiantes, e define o episódio pela **interação "
  "diádica** entre governo e desafiantes mais terceiros (f. 4, impressa "
  "254). Incorporar o ator estatal à análise de um episódio contencioso é "
  "o que aquela peça foi escrita para fazer. **O que continua sendo meu é "
  "o recorte mais estreito**: CEA autoriza analisar o ato estatal; "
  "aplicar-lhe a grade de TAREFAS DE ENQUADRAMENTO de Snow é um passo a "
  "mais, que a peça não dá e eu dou. **O ponto frágil mudou de lugar, e "
  "encolheu.**".format(com_quadro, desafiante, estatal, misto))
w("")
w("## 2. O que a grade mostra, e as cifras são geradas deste documento")
w("")
w("| | |")
w("|:--|--:|")
w("| registros classificados | **{}** |".format(len(G)))
w("| com quadro de ação coletiva | **{}** |".format(com_quadro))
w("| dos quais **acumulam mais de uma função** | **{}** |".format(multi))
w("| campo vazio no codebook (`—`) | **{}** |".format(cont["0"]))
w("| não é quadro de ação coletiva | **{}** |".format(cont["N"]))
w("| **ausência MEDIDA**, distinta de vazio | **{}** — PT-01 |".format(
    cont["ausencia"]))
w("")
w("| Função | Registros |")
w("|:--|--:|")
w("| **D** diagnóstico | **{}** |".format(cont["D"]))
w("| **P** prognóstico | **{}** |".format(cont["P"]))
w("| **M** motivacional | **{}** |".format(cont["M"]))
w("| **C** contraquadro / disputa | **{}** |".format(cont["C"]))
w("")
w("**Três leituras que a contagem autoriza, e nenhuma delas estava visível no "
  "campo em prosa:**")
w("")
w("1. **O motivacional concentra-se no dia.** Dos {} registros motivacionais, "
  "a maioria está em T−1 operacional e T0 — *'festa da Selma'*, *'marcha "
  "patriótica'*, *'o povo no poder'*, *'casa do povo'*, *'praça do povo'*, "
  "*'tomada do poder'*. **O diagnóstico é de anos; a convocação é de "
  "semanas.**".format(cont["M"]))
w("2. **O contraquadro é quase todo judicial.** Das {} ocorrências de **C**, a "
  "maior parte é **díade de arena** — *'presunção de inocência'* × "
  "*'efetividade da jurisdição'* e variantes —, e só três são contraquadro de "
  "ator político: PT-03B (*lawfare*), PT-50 (negação de vínculo) e PT-50A "
  "(*'infiltrados'*). **A disputa de enquadramento deste caso corre, em boa "
  "medida, dentro do Judiciário.**".format(cont["C"]))
w("3. **E o prognóstico tem dois donos opostos.** *'Intervenção militar'* e "
  "*'anistia'* de um lado; *'defesa do Estado Democrático de Direito'*, "
  "*'restabelecimento da ordem'*, *'apuração de responsabilidades'* e "
  "*'cumprimento de ordem judicial'* do outro. **O campo `framing_narrativa` "
  "guarda, sem distinguir, os dois programas que disputaram o desfecho.**")
w("")
w("## 3. Registro por registro")
w("")
w("| id | de quem é o quadro | função inferida | base, no texto do campo |")
w("|:--|:--|:--|:--|")
ROT = {"D": "**D**", "P": "**P**", "M": "**M**", "C": "**C**"}
for i in ids:
    ator, f, obs = G[i]
    if f == "0":
        rot = "— *campo vazio*"
    elif f == "N":
        rot = "**N** *(não é quadro)*"
    elif f == "":
        rot = "**∅** *(ausência medida)*"
    else:
        rot = " + ".join(ROT[c] for c in f)
    w("| `{}` | {} | {} | {} |".format(i, ator, rot, obs or "—"))
w("")
w("## 4. O que isto deixa para você")
w("")
w("| | |")
w("|:--|:--|")
w("| **a grade entra no esquema?** | criar um 18º campo é **decisão sua**. "
  "Hoje a classificação vive **só aqui**, e é inferência declarada |")
w("| **a extensão a ator estatal** | **{} dos {}** quadros são de ator "
  "estatal — contra {} de desafiante e {} de díade entre campos. **Desde "
  "28/10/2026 a extensão cita Kriesi, Hutter e Bojár (2019)**, que "
  "incorporam o ator estatal à análise do episódio por construção. O que "
  "resta de escolha minha é aplicar a eles a grade de TAREFAS, que "
  "aquela peça não aplica |".format(estatal, com_quadro, desafiante,
                                   misto))
w("| **os {} registros `N`** | PT-20A, PT-20B, PT-25 e PT-47 têm texto no "
  "campo que **não é quadro de ação coletiva**. Se a grade entrar, eles "
  "precisam de valor próprio, ou o campo precisa de outro nome |".format(
      cont["N"]))
w("| **os {} vazios** | são vazio de **ato sem enquadramento declarado** — "
  "retirada de barreira, chegada de tropa, decisão administrativa. Distintos "
  "de PT-01, que é **ausência medida na literatura** |".format(cont["0"]))

D = "docs/referencial/02_GRADE-FUNCIONAL-ENQUADRAMENTO.md"
io.open(D, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
print()
print("OK  escrito: " + D)
