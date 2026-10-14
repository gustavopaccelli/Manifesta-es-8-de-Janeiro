# -*- coding: utf-8 -*-
"""Pendencia 2: a expressao "guerra cultural" de PT-06 ganha ancora. 10/10/2026.

ENCAMINHAMENTO: "Resolva as tres pendencias restantes."

A pendencia era: entra no corpus a dissertacao do deposita/434, cujo titulo e
"'Agentes do caos': 'guerra cultural', redes sociais e 'novas direitas'"?

**NAO ENTRA, E NAO PRECISA.** Varrido o corpus JA LIDO, a expressao esta em
pecas que o projeto leu e cujas paginas estao conferidas: Cesarino (2019) com
tres ocorrencias de "guerra cultural" e Cesarino (2022) com uma. A dissertacao
seria duas vezes inadequada: e dissertacao de mestrado, e o corpus so admitiu
artigo revisado por pares, livro de editora e fonte primaria; e o recorte dela e
2014-2018, enquanto PT-06 cobre 2020-2021.

**E A LEITURA DA PECA MUDA O QUE SE PODE AFIRMAR.** Cesarino nao apenas usa a
expressao: ela ARGUMENTA CONTRA reduzir o bolsonarismo a ela. As duas ancoras
abaixo entram juntas de proposito -- a que sustenta o frame e a que o limita --,
porque lancar a primeira sem a segunda seria usar a autora contra o argumento
dela.

NOTA DE APARATO: a frase de Cesarino (2022, p. 174) que tematiza as guerras
culturais tem ASPAS CURVAS DENTRO ("guerras culturais"), e por isso NAO foi
transcrita: aspa aninhada inverte a paridade de transcricoes() e foi o que
deixou cinco ancoras de PT-08 sem conferencia em 08/10. A peca e citada por
pagina, sem transcricao. As duas transcricoes usadas sao de Cesarino (2019), que
nao tem aspas internas -- e as duas casam POR TEXTO INTEGRAL, nao por janela.
"""
import io
import json
import os

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
P = "process_tracing_8jan_eventos.json"
d = json.load(io.open(P, encoding="utf-8"))
EV = {e["id"]: e for e in d["eventos"]}

CES19 = ("Fontes/13_Bolsonarismo-mobilizacao/CESARINO_Identidade-e-representacao-no-"
         "bolsonarismo_Revista-de-Antropologia-62-3_2019.pdf")
assert os.path.exists(CES19), CES19
assert "-" not in "CESARINO 2019"
d["metadados"]["registro_documentos"]["CESARINO 2019"] = CES19

# ------------------------------------------------------------------ framing ---
V = ("A expressão 'guerra cultural' permanece sem âncora nas peças lidas")
N = ("A expressão guerra cultural GANHOU ÂNCORA EM 10/10/2026, e a âncora vem com o "
     "seu limite. Cesarino (2019) documenta a PROVENIÊNCIA do termo: “Como o próprio "
     "termo guerra cultural, outros como marxismo cultural e globalismo foram tomados "
     "diretamente de empréstimo da alt-right americana” (p. 540 impressa — PDF p. 11). "
     "E a MESMA AUTORA PÕE O LIMITE, que entra junto porque lançar um sem o outro seria "
     "usá-la contra o argumento dela: “Longe de se resumir a uma guerra cultural no "
     "campo das políticas de identidade, o bolsonarismo tem como pilar constitutivo um "
     "eixo neoliberal que é normalmente obscurecido pelo eixo populista-conservador” "
     "(p. 539 impressa — PDF p. 10). Cesarino (2022, p. 174 impressa) cobre a janela "
     "deste registro e trata as guerras culturais como a via conservadora pela qual o "
     "inimigo comum é tematizado, dizendo que o que une os segmentos é antes uma defesa "
     "intransigente da liberdade — citada por página e SEM transcrição, porque a frase "
     "traz aspas curvas internas e aspa aninhada já custou a este projeto cinco âncoras "
     "sem conferência em PT-08. LIMITE DE PERÍODO DECLARADO: Cesarino (2019) trata da "
     "campanha de 2018, de modo que ancora a existência e a proveniência do "
     "enquadramento, não o seu uso em 2020-2021")
assert V in EV["PT-06"]["framing_narrativa"], "PT-06: a declaracao de lacuna mudou"
EV["PT-06"]["framing_narrativa"] = EV["PT-06"]["framing_narrativa"].replace(V, N)

EV["PT-06"]["fonte_local"] += "; " + CES19
EV["PT-06"]["fonte_pagina"] += " | CESARINO 2019: 10, 11"
EV["PT-06"]["nota_auditoria"] = (EV["PT-06"].get("nota_auditoria") or "") + (
    " 10/10/2026 — a última expressão sem âncora deste registro, guerra cultural, "
    "ganhou lastro, e NÃO foi preciso ampliar o corpus: a expressão estava em peças já "
    "lidas. A dissertação de mestrado que a busca no IBICT havia encontrado ficou fora, "
    "por padrão de evidência e por recorte de período. As duas âncoras entram em par — "
    "a que sustenta o frame e a que o limita —, porque Cesarino argumenta contra reduzir "
    "o bolsonarismo à guerra cultural.")

d["metadados"]["revisoes"].append(
    "2026-10-10 — PT-06: a expressão guerra cultural ganhou âncora em Cesarino (2019), "
    "peça já lida, com a ressalva da própria autora contra reduzir o bolsonarismo a "
    "ela. A dissertação do deposita/434 ficou fora do corpus: dissertação de mestrado e "
    "recorte 2014-2018 contra os 2020-2021 do registro. Nenhuma outra expressão de "
    "PT-06 segue sem âncora.")

# ------------------------------------------------------------------- guarda ---
assert len(d["eventos"]) == 83
from collections import Counter   # noqa: E402
cl = Counter(e["status_classe"] for e in d["eventos"])
assert dict(cl) == {"Confirmado em fonte primária": 61, "Confirmado": 21,
                    "Inferência do analista": 1}, dict(cl)
assert "GANHOU ÂNCORA EM 10/10/2026" in EV["PT-06"]["framing_narrativa"]
assert "CESARINO 2019: 10, 11" in EV["PT-06"]["fonte_pagina"]

io.open(P, "w", encoding="utf-8", newline="\n").write(
    json.dumps(d, ensure_ascii=False, indent=2) + "\n")
print("PT-06: guerra cultural ancorada em Cesarino (2019), p. 539 e 540 impressas")
print("83 sub-eventos | " + " | ".join("%d %s" % (v, k) for k, v in cl.most_common()))
