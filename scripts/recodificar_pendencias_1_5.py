# -*- coding: utf-8 -*-
"""Pendencias 1 e 5, resolvidas em 10/10/2026 por delegacao do pesquisador.

ENCAMINHAMENTO: "Resolva as pendencias 1 e 5."

PENDENCIA 1 — CESARINO (2019) ENTRA EM PT-29?  **NAO.** Tres razoes.
  (a) A RENOMEACAO RETIROU A NECESSIDADE. Cesarino era resgate do nome VELHO:
      "transposicao do limiar" tinha uma tensao interna com PT-19 (limiar
      pressupoe acao sem coordenacao; PT-19 afirma coordenacao), e o contagio
      nao-deliberado dela dissolvia essa tensao. "Demonstracao de viabilidade"
      nao tem contagio nenhum: e efeito de demonstracao entre quem ja esta no
      lugar. **Nao ha mais o que resgatar.**
  (b) REFERENTE DIFERENTE, e esta e a razao dura. O contagio de Cesarino e
      circulacao de CONTEUDO em WhatsApp e YouTube na campanha de 2018; PT-29 e
      imitacao de uma ACAO FISICA por uma multidao co-presente em 08/01/2023.
      Mesma palavra, referentes distintos — e importa-la seria a 17a ocorrencia
      do modo de falha da casa, cometida por mim e com a peca lida.
  (c) REDUNDANTE ONDE ELA CABERIA. O lugar em que a tese dela serve e PT-06 — a
      circulacao, nao a consistencia, sustentando a mobilizacao —, e PT-06 ja
      esta ancorado em Cesarino (2022), da mesma autora e com pagina conferida.

PENDENCIA 5 — PARTIR PT-62 EM DOIS REGISTROS?  **NAO, e por uma razao melhor do
que as duas que eu havia oferecido.** Eu propus escolher entre partir o registro
e manter um campo com dois mecanismos, e justifiquei a segunda pelo custo de
mexer na contagem de 83 sub-eventos. **O custo nao era o argumento certo.** Ao
olhar a camada T+1 inteira, o mecanismo (1) de PT-62 — desmobilizacao por
repressao do Estado — **ja esta documentado em fonte primaria por QUATRO outros
registros**:

  PT-49  decisao de Moraes determinando a desocupacao total dos acampamentos
  PT-52  desmonte do acampamento do SMU pela Policia do Exercito e PMDF, com
         2.151 prisoes em flagrante no 8 e 9 de janeiro — e o mecanismo de PT-52
         JA SE CHAMA "destruicao da infraestrutura de mobilizacao"
  PT-53  inqueritos 4921 e 4922
  PT-61  1.402 reus responsabilizados ate abr/2026

Partir PT-62 criaria um registro novo que **duplica esses quatro**, com evidencia
pior do que a deles. E manter os dois mecanismos como afirmacao PROPRIA de PT-62
e o defeito oposto: o registro e classe `Inferencia do analista`, e estava
afirmando por conta propria uma coisa que outros quatro registros provam em fonte
primaria.

**A saida e de-duplicar, nao partir.** O mecanismo (1) passa a ser REMISSAO aos
registros que o documentam; o que PT-62 afirma por conta propria e o mecanismo
(2), a migracao de arena — e e so isso que a classe `Inferencia do analista`
precisa cobrir. Com a remissao, a classe volta a ser honesta.

NOTA: PT-52 ja havia pensado a distincao. O proprio campo dele diz que "a
diferenca e o que separa a desmobilizacao do repertorio da punicao de seus
agentes". O projeto tinha a distincao e PT-62 a estava reafirmando sem ver.
"""
import io
import json
import os

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
P = "process_tracing_8jan_eventos.json"
d = json.load(io.open(P, encoding="utf-8"))
EV = {e["id"]: e for e in d["eventos"]}
mudou = []

# ====================================================== PENDENCIA 1 — PT-29 ===
V29 = ("O QUE ESTE CAMPO NÃO DECIDE: se Cesarino (2019) entra como âncora conceitual "
       "deste registro continua em aberto na agenda — o argumento dela, de que o "
       "contágio opera em plano não necessariamente consciente para os atores, "
       "dissolveria a tensão também no plano teórico, e lançá-la aqui seria decidir o "
       "que está em aberto")
N29 = ("DECIDIDO EM 10/10/2026, por delegação do pesquisador: CESARINO (2019) NÃO ENTRA "
       "NESTE REGISTRO. Três razões. (a) A renomeação retirou a necessidade: Cesarino "
       "era resgate do nome VELHO, porque o contágio não-deliberado dela dissolvia a "
       "tensão entre limiar e coordenação; demonstração de viabilidade não tem contágio "
       "nenhum, e não há mais o que resgatar. (b) E a razão dura é de REFERENTE: o "
       "contágio dela é circulação de CONTEÚDO em WhatsApp e YouTube na campanha de "
       "2018, e este registro é imitação de uma AÇÃO FÍSICA por multidão co-presente em "
       "08/01/2023 — mesma palavra, referentes distintos, e importá-la seria o modo de "
       "falha deste projeto cometido com a peça já lida. (c) Onde a tese dela serve é "
       "PT-06, a circulação e não a consistência sustentando a mobilização, e PT-06 já "
       "está ancorado em Cesarino (2022), da mesma autora e com página conferida")
assert V29 in EV["PT-29"]["mecanismo_causal"], "PT-29: a declaracao de abertura mudou"
EV["PT-29"]["mecanismo_causal"] = EV["PT-29"]["mecanismo_causal"].replace(V29, N29)
EV["PT-29"]["nota_auditoria"] = (EV["PT-29"].get("nota_auditoria") or "") + (
    " 10/10/2026 — pendência resolvida por delegação: Cesarino (2019) não entra. A razão "
    "que decide não é de mérito da peça, é de referente: contágio de conteúdo não é "
    "imitação de ação física por multidão co-presente. Nenhum campo mudou além desta "
    "declaração, que antes dizia que a questão estava aberta.")
mudou += ["PT-29/mecanismo_causal", "PT-29/nota_auditoria"]

# ====================================================== PENDENCIA 5 — PT-62 ===
V62 = ("(1) DESMOBILIZAÇÃO POR REPRESSÃO SELETIVA: o repertório de rua cessa por ação "
       "do Estado — desocupação dos acampamentos e persecução penal —, e não por "
       "exaustão do ator.")
N62 = ("(1) DESMOBILIZAÇÃO POR REPRESSÃO SELETIVA: o repertório de rua cessa por ação do "
       "Estado — desocupação dos acampamentos e persecução penal —, e não por exaustão "
       "do ator. **ESTE MECANISMO NÃO É AFIRMAÇÃO PRÓPRIA DESTE REGISTRO: é REMISSÃO aos "
       "quatro que o documentam em fonte primária** — PT-49 (decisão de Moraes "
       "determinando a desocupação total), PT-52 (desmonte do acampamento do SMU pela "
       "Polícia do Exército e PMDF, com 2.151 prisões em flagrante no 8 e 9 de janeiro, "
       "e cujo mecanismo já se chama destruição da infraestrutura de mobilização), PT-53 "
       "(inquéritos 4921 e 4922) e PT-61 (1.402 réus responsabilizados até abr/2026).")
assert V62 in EV["PT-62"]["mecanismo_causal"], "PT-62: o mecanismo (1) mudou de forma"
m62 = EV["PT-62"]["mecanismo_causal"].replace(V62, N62)

V62B = ("(2) MIGRAÇÃO DE ARENA: a contestação persiste deslocando-se para arenas em que "
        "o custo de repressão é menor, as eleitorais e as digitais.")
N62B = ("(2) MIGRAÇÃO DE ARENA: a contestação persiste deslocando-se para arenas em que o "
        "custo de repressão é menor, as eleitorais e as digitais. **ESTE É O QUE PT-62 "
        "AFIRMA POR CONTA PRÓPRIA, e é só ele que a classe Inferência do analista "
        "precisa cobrir.**")
assert V62B in m62
m62 = m62.replace(V62B, N62B)

V62C = ("IMPLEMENTAÇÃO DECLARADA: a proposta (a) admitia partir o registro em dois ou "
        "fazer o campo nomear dois mecanismos; foi pela segunda, porque partir mudaria a "
        "contagem de 83 sub-eventos, que é conferida pela integridade, pelas duas "
        "figuras e pela tabela do relatório.")
N62C = ("PENDÊNCIA DA PARTIÇÃO, RESOLVIDA EM 10/10/2026 POR DELEGAÇÃO — e a razão certa "
        "não era a que eu havia dado. Em 10/10 pela manhã mantive um campo com dois "
        "mecanismos alegando o CUSTO de mexer na contagem de 83 sub-eventos. O custo não "
        "era o argumento: olhando a camada T+1 inteira, o mecanismo (1) já está "
        "documentado em fonte primária por QUATRO registros, de modo que partir criaria "
        "um registro novo que os DUPLICA, com evidência pior que a deles. E manter os "
        "dois como afirmação própria era o defeito oposto: um registro de classe "
        "Inferência afirmando por conta própria o que outros quatro provam. **A saída é "
        "de-duplicar, não partir**, e é o que a remissão acima faz. PT-52 já havia "
        "pensado a distinção: o campo dele diz que a diferença é o que separa a "
        "desmobilização do repertório da punição de seus agentes.")
assert V62C in m62
m62 = m62.replace(V62C, N62C)

EV["PT-62"]["mecanismo_causal"] = m62
EV["PT-62"]["nota_auditoria"] = (EV["PT-62"].get("nota_auditoria") or "") + (
    " 10/10/2026 — pendência da partição resolvida por delegação: PT-62 CONTINUA UM "
    "registro, e o mecanismo (1) passou a ser remissão a PT-49, PT-52, PT-53 e PT-61 em "
    "vez de afirmação própria. Com isso a classe Inferência do analista volta a cobrir "
    "só o que o registro afirma por conta própria, que é a migração de arena. A âncora "
    "de Carvalho e Tatagiba (2025) PERMANECE, porque é a literatura que corrigiu o nome "
    "do mecanismo, não a que sustenta a migração.")
mudou += ["PT-62/mecanismo_causal", "PT-62/nota_auditoria"]

d["metadados"]["revisoes"].append(
    "2026-10-10 — pendências 1 e 5 resolvidas por delegação do pesquisador. (1) "
    "Cesarino (2019) NÃO entra em PT-29: a renomeação retirou a necessidade, e o "
    "referente é outro — contágio de conteúdo em plataforma não é imitação de ação "
    "física por multidão co-presente. (5) PT-62 NÃO se parte em dois: o mecanismo de "
    "desmobilização por repressão já está em fonte primária em PT-49, PT-52, PT-53 e "
    "PT-61, e partir criaria duplicata com evidência pior. O mecanismo (1) passou a ser "
    "remissão a esses quatro, de modo que a classe Inferência do analista cobre apenas "
    "a migração de arena, que é o que PT-62 afirma por conta própria. Nenhum registro "
    "criado, nenhuma classe alterada, 83 sub-eventos.")

# ------------------------------------------------------------------ guarda ----
assert len(d["eventos"]) == 83
from collections import Counter   # noqa: E402
cl = Counter(e["status_classe"] for e in d["eventos"])
assert dict(cl) == {"Confirmado em fonte primária": 61, "Confirmado": 21,
                    "Inferência do analista": 1}, dict(cl)
assert "NÃO ENTRA NESTE REGISTRO" in EV["PT-29"]["mecanismo_causal"]
assert "é REMISSÃO aos" in EV["PT-62"]["mecanismo_causal"]
assert len(mudou) == 4, mudou

io.open(P, "w", encoding="utf-8", newline="\n").write(
    json.dumps(d, ensure_ascii=False, indent=2) + "\n")

print("pendências 1 e 5 resolvidas — %d campos:" % len(mudou))
for m in mudou:
    print("   " + m)
print("\n83 sub-eventos | " + " | ".join("%d %s" % (v, k) for k, v in cl.most_common()))
