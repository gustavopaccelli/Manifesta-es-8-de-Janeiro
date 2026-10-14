# -*- coding: utf-8 -*-
"""TAREFA 19: os quatro nomes de mecanismo, atribuidos pelo pesquisador em 10/10/2026.

ENCAMINHAMENTO: "Aprovo as quatro propostas de nomenclatura, execute."

As propostas, com definicao, estao em projeto-pos-doc/09_CONCEITO-MECANISMO.md
secoes 9.2 a 9.5. Este script as aplica ao JSON, que e a fonte da verdade, e
escreve DENTRO de cada registro a razao da troca -- porque a regra da casa e que
mudanca de nome de mecanismo se explica no proprio registro, nao so no documento.

UMA DECISAO DE IMPLEMENTACAO, DECLARADA: a proposta (a) de PT-62 admitia duas
formas -- partir o registro em dois, ou o campo passar a nomear dois mecanismos.
Foi pela SEGUNDA. Partir em dois mudaria a contagem de 83 sub-eventos, que e
conferida por verificar_integridade, pelas duas figuras e pela tabela do
relatorio; isso e mudanca estrutural, e o encaminhamento aprovou nomenclatura.
Se preferir dois registros, e uma linha de pedido.

O QUE NAO FOI TOCADO, de proposito:
  - A ATRIBUICAO DOS QUATRO TESTES (quinta cobranca da tarefa 19, documento 09
    secao 9.6). Nao e nome de mecanismo e nao estava entre "as quatro propostas
    de nomenclatura": muda um documento de projeto, nao o codebook.
  - CESARINO (2019) EM PT-29. A pergunta de se ela entra como ancora continua
    aberta na agenda, item 41.5. O argumento dela dissolve a tensao entre PT-29 e
    PT-19 no plano conceitual, e isso esta dito abaixo sem que a peca seja
    lancada como ancora -- lancar seria decidir o que esta em aberto.
"""
import io
import json
import os

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
P = "process_tracing_8jan_eventos.json"
d = json.load(io.open(P, encoding="utf-8"))
EV = {e["id"]: e for e in d["eventos"]}

ATRIB = ("NOME ATRIBUÍDO PELO PESQUISADOR EM 10/10/2026, em substituição a ")

# =========================================================== PT-29 ============
VELHO29 = ("Transposição do limiar: a primeira invasão bem-sucedida funciona como "
           "sinal de viabilidade e dispara o contágio para os demais alvos")
assert EV["PT-29"]["mecanismo_causal"] == VELHO29, EV["PT-29"]["mecanismo_causal"]
EV["PT-29"]["mecanismo_causal"] = (
    "Demonstração de viabilidade: a primeira transposição bem-sucedida converte uma "
    "ação de desfecho incerto em ação demonstradamente possível, e com isso reduz o "
    "custo percebido da imitação para atores JÁ REUNIDOS E JÁ CONVOCADOS — sem exigir "
    "que os imitadores partilhem plano com os primeiros. "
    + ATRIB + "“transposição do limiar”. "
    "A RAZÃO DA TROCA, que era cobrança da tarefa 19 aberta desde 30/09: o modelo de "
    "limiar de Granovetter pressupõe ação que NÃO vem de coordenação e planejamento, e "
    "PT-19 afirma coordenação por criptolinguagem — a tensão era interna ao codebook, "
    "não entre codebook e fonte. O nome novo guarda o que a evidência mostra, que é a "
    "sequência das três invasões e o sinal de viabilidade, e descarta o que o codebook "
    "nunca mediu, que são limiares individuais e a sua distribuição. E é compatível com "
    "a coordenação a montante, porque situa o efeito entre quem já está no lugar. "
    "O QUE ESTE CAMPO NÃO DECIDE: se Cesarino (2019) entra como âncora conceitual deste "
    "registro continua em aberto na agenda — o argumento dela, de que o contágio opera "
    "em plano não necessariamente consciente para os atores, dissolveria a tensão "
    "também no plano teórico, e lançá-la aqui seria decidir o que está em aberto")

# =========================================================== PT-34 ============
m34 = EV["PT-34"]["mecanismo_causal"]
VELHO34 = "Massa crítica atingida no ponto de máxima densidade simbólica."
assert m34.startswith(VELHO34), m34[:90]
EV["PT-34"]["mecanismo_causal"] = (
    "Concentração simultânea no conjunto simbólico: por serem CONTÍGUAS as três sedes, "
    "uma única concentração alcança os três alvos sem redeslocamento — de modo que o "
    "conjunto simbólico se torna atingível por UMA concentração, e não por três "
    "operações sucessivas. "
    + ATRIB + "“massa crítica atingida no ponto de máxima densidade simbólica”. "
    "A RAZÃO DA TROCA: em Marwell e Oliver a massa crítica são os ORGANIZADORES e não a "
    "multidão, e Oliver classifica o uso para o grupo inicial de manifestantes como "
    "metafórico e frouxo. A varredura das quinze peças do eixo 13, lidas em 09-10/10, "
    "devolveu ZERO ocorrências de massa crítica: não há no corpus literatura que "
    "sustente o termo para este caso. O nome velho afirmava uma quantidade-limite que o "
    "codebook não mediu; o novo usa a contiguidade das sedes, que é dado primário. "
    + m34[len(VELHO34):].strip())

# =========================================================== PT-12A ===========
m12a = EV["PT-12A"]["mecanismo_causal"]
VELHO12A = ("Mobilização de recursos em rede distribuída com nós centralizadores — e é "
            "aqui que está o achado teórico.")
assert m12a.startswith(VELHO12A), m12a[:110]
EV["PT-12A"]["mecanismo_causal"] = (
    "Agregação na base e intermediação concentrada: recursos são reunidos de muitas "
    "unidades sem vínculo entre si e sem comando central — AGREGAÇÃO —, e convertidos "
    "em suprimento por um número pequeno de nós que concentram e redistribuem — "
    "INTERMEDIAÇÃO. Dispersão na captação e concentração na execução não se contradizem "
    "porque operam em camadas distintas. "
    + ATRIB + "“mobilização de recursos em rede distribuída com nós centralizadores”. "
    "A RAZÃO DA TROCA: o nome velho DESCREVIA e não TIPIFICAVA, e a cobrança da tarefa "
    "19 era exatamente tipificar nos termos de Edwards e Gillham (2013). O novo o faz, e "
    "parte do ganho está no que ele EXCLUI: não é PATROCÍNIO, porque o nó não financia, "
    "redistribui; e não é COOPTAÇÃO, porque nenhuma organização preexistente foi "
    "capturada. E é aqui que está o achado teórico. "
    + m12a[len(VELHO12A):].strip())

# =========================================================== PT-62 ============
VELHO62 = ("Desarticulação do repertório de rua com deslocamento (não extinção) da "
           "contestação para arenas institucionais e discursivas")
assert EV["PT-62"]["mecanismo_causal"] == VELHO62, EV["PT-62"]["mecanismo_causal"]
EV["PT-62"]["mecanismo_causal"] = (
    "Desmobilização por repressão seletiva, seguida de migração de arena — e o campo "
    "passa a nomear DOIS mecanismos, não um. "
    "(1) DESMOBILIZAÇÃO POR REPRESSÃO SELETIVA: o repertório de rua cessa por ação do "
    "Estado — desocupação dos acampamentos e persecução penal —, e não por exaustão do "
    "ator. "
    "(2) MIGRAÇÃO DE ARENA: a contestação persiste deslocando-se para arenas em que o "
    "custo de repressão é menor, as eleitorais e as digitais. "
    + ATRIB + "“desarticulação do repertório de rua com deslocamento (não extinção)”, "
    "pela saída (a) das duas apresentadas no documento 09, §9.5. "
    "DUAS RAZÕES, e a segunda é nova. A primeira é de critério: no critério de Tarrow o "
    "nome velho era PROCESSO e não mecanismo, porque continha uma sequência — era a "
    "cobrança da tarefa 19. A segunda é EMPÍRICA e apareceu na leitura de 09/10: "
    "Carvalho e Tatagiba (2025, p. 35 impressa) documentam que os acampamentos perderam "
    "volume até serem desmobilizados em operações do exército, com centenas de prisões. "
    "O nome velho afirmava DESLOCAMENTO, isto é, agência do ator, onde a fonte mostra "
    "OPERAÇÃO DO ESTADO. "
    "IMPLEMENTAÇÃO DECLARADA: a proposta (a) admitia partir o registro em dois ou fazer "
    "o campo nomear dois mecanismos; foi pela segunda, porque partir mudaria a contagem "
    "de 83 sub-eventos, que é conferida pela integridade, pelas duas figuras e pela "
    "tabela do relatório. "
    "LIMITE INALTERADO: a classe continua Inferência do analista, porque a âncora de "
    "Carvalho e Tatagiba cobre 2023 e o registro projeta até 2026")

# =========================================================== notas ============
NOTA = (" TAREFA 19, 10/10/2026 — nome do mecanismo atribuído pelo pesquisador, sobre a "
        "proposta do documento 09. A mudança NÃO é de campo nem de classe: é de NOME, e "
        "a razão está escrita no próprio mecanismo_causal para que a redação não a trate "
        "como troca cosmética.")
for pid in ("PT-29", "PT-34", "PT-12A", "PT-62"):
    EV[pid]["nota_auditoria"] = (EV[pid].get("nota_auditoria") or "") + NOTA

d["metadados"]["revisoes"].append(
    "2026-10-10 — TAREFA 19: os quatro nomes de mecanismo sob cobrança foram "
    "atribuídos pelo pesquisador. PT-29 passa de transposição do limiar a DEMONSTRAÇÃO "
    "DE VIABILIDADE; PT-34, de massa crítica a CONCENTRAÇÃO SIMULTÂNEA NO CONJUNTO "
    "SIMBÓLICO; PT-12A, de rede distribuída com nós centralizadores a AGREGAÇÃO NA BASE "
    "E INTERMEDIAÇÃO CONCENTRADA; PT-62, de desarticulação com deslocamento a "
    "DESMOBILIZAÇÃO POR REPRESSÃO SELETIVA seguida de MIGRAÇÃO DE ARENA, que são dois "
    "mecanismos e o campo passa a nomear os dois. Nenhum campo além de mecanismo_causal "
    "e nota_auditoria mudou, e nenhuma classe mudou. Restam da tarefa 19 a atribuição "
    "dos quatro testes, que é bibliográfica, e a decisão sobre Cesarino (2019) em "
    "PT-29.")

# =========================================================== guarda ===========
# A guarda vem ANTES da escrita. Ver o motivo em recodificar_eixo13_leitura.py.
for pid, inicio in (("PT-29", "Demonstração de viabilidade"),
                    ("PT-34", "Concentração simultânea no conjunto simbólico"),
                    ("PT-12A", "Agregação na base e intermediação concentrada"),
                    ("PT-62", "Desmobilização por repressão seletiva")):
    assert EV[pid]["mecanismo_causal"].startswith(inicio), pid
    assert "NOME ATRIBUÍDO PELO PESQUISADOR EM 10/10/2026" in EV[pid]["mecanismo_causal"], pid
assert len(d["eventos"]) == 83, "a contagem de sub-eventos nao pode mudar aqui"

from collections import Counter   # noqa: E402
classes = Counter(e["status_classe"] for e in d["eventos"])
assert dict(classes) == {"Confirmado em fonte primária": 61, "Confirmado": 21,
                         "Inferência do analista": 1}, dict(classes)

io.open(P, "w", encoding="utf-8", newline="\n").write(
    json.dumps(d, ensure_ascii=False, indent=2) + "\n")

print("TAREFA 19 — quatro nomes atribuídos:")
for pid in ("PT-29", "PT-34", "PT-12A", "PT-62"):
    print("  %-7s %s" % (pid, EV[pid]["mecanismo_causal"].split(":")[0][:72]))
print("\n83 sub-eventos | " + " | ".join("%d %s" % (v, k) for k, v in classes.most_common()))
