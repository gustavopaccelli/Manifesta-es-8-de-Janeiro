# -*- coding: utf-8 -*-
"""Leitura das 15 pecas nao lidas do eixo 13 (09-10/10/2026): as ancoras que ela produziu.

ENCAMINHAMENTOS DO PESQUISADOR nesta rodada:
  - "Leia as 15 pecas nao lidas do eixo 13."
  - "Madeira et al. (p. 254) vai para PT-05 ou para o arco judicial? O que me
     sugere? Execute sua recomendacao."

O QUE ESTE SCRIPT FAZ, e o que NAO faz:
  FAZ  -- lanca ancoras com pagina conferida, fecha uma declaracao de PT-06 que
          era verdadeira em agosto e deixou de ser, e registra DOIS limites de
          atribuicao que a leitura descobriu.
  NAO  -- renomeia mecanismo nenhum. A nomenclatura da tarefa 19 e decisao do
          pesquisador, e esta proposta, com caracteristicas e relacoes, no
          documento 09.

A RECOMENDACAO SOBRE MADEIRA, EXECUTADA: a frase do general vai para **PT-03C**,
nao para PT-05. Tres razoes. (1) DATA: a declaracao e de inicio de abril de 2018
e PT-05 cobre 2019-2022. (2) REFERENTE: o general condiciona a reacao armada a uma
decisao do STF -- "se o Supremo Tribunal Federal deixasse o ex-presidente solto, e
permitisse que se candidatasse" --, e PT-03C E essa decisao, o HC 152.752 julgado
em 04/04/2018. (3) LACUNA: o arco judicial se apoia so em acordaos, isto e, em
fonte primaria sem literatura que a interprete; PT-05 ja tem duas pecas de
literatura para o mesmo mecanismo. A frase mede pressao militar SOBRE a decisao
judicial, que e exatamente o que o acordao nao pode registrar sobre si mesmo.

DOIS LIMITES DE ATRIBUICAO QUE A LEITURA DESCOBRIU, e os dois valem mais que uma
ancora nova:

1. **BASTOS E RECUERO (2023) NAO CORROBORA O SRI LANKA.** Eu quase registrei que
   corroborava. A peca diz que a estrategia insurrecional foi "ostensibly inspired
   by the coups in Sri Lanka and Thailand" (p. 4) -- mas a frase esta no paragrafo
   de REVISAO e e atribuida a Keulenaar et al. (2023), que a propria peca qualifica
   como *Unpublished report*. O estudo de Bastos e Recuero analisa as declaracoes
   de Bolsonaro na campanha e a penetracao do playbook entre parlamentares; o Sri
   Lanka nao e achado deles. A mesma cadeia vale para a divisao de plataformas
   ("expertly coordinated via Telegram while Facebook and Instagram were used for
   broadcasting", p. 4): tambem e de Keulenaar et al. **Citar isso como segunda
   fonte independente seria citar uma citacao -- o que este projeto proibiu em
   30/09.** O Sri Lanka continua ancorado SO na CPMI (p. 614).

2. **O "LIMIAR" DE CESARINO NAO E O LIMIAR DE GRANOVETTER.** Cesarino (2022) tem
   sete ocorrencias de "limiar", e nenhuma serve a PT-29: e "limiar
   transformacional", da antiestrutura de Turner e da formula canonica de
   Levi-Strauss. Contagem de termo alta e referente outro -- o modo de falha do
   projeto, agora com a palavra certa no conceito errado.
"""
import io
import json
import os

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
P = "process_tracing_8jan_eventos.json"
d = json.load(io.open(P, encoding="utf-8"))
EV = {e["id"]: e for e in d["eventos"]}
mudancas = []


def poe(pid, campo, novo):
    e = EV[pid]
    if e.get(campo) == novo:
        return
    e[campo] = novo
    mudancas.append((pid, campo))


# ===================================================== registro_documentos ====
D13 = "Fontes/13_Bolsonarismo-mobilizacao/"
NOVOS = {
    "CESARINO 2022": D13 + "CESARINO_Bolsonarismo-sem-Bolsonaro-publicos-antiestruturais_"
                            "Revista-do-IEB-82_2022.pdf",
    "NUNES 2024": D13 + "NUNES_A-palavra-e-a-coisa-bolsonarismo-como-infraestrutura_"
                        "Lua-Nova-122_2024.pdf",
    "CARVALHO E TATAGIBA 2025": D13 + "CARVALHO-TATAGIBA_Quando-o-conflito-eleitoral-"
                                      "extravasa-para-as-ruas_Lua-Nova-124_2025.pdf",
    "MADEIRA ET AL 2022": "Fontes/14_Livros-brasileiros/MADEIRA-MARONA-DEL-RIO_"
                          "Democracia-e-justica-na-America-Latina_EdUERJ_2022.pdf",
}
for cod, cam in NOVOS.items():
    assert "-" not in cod, cod          # o regex de CITACAO nao aceita hifen no codigo
    assert os.path.exists(cam), cam
    if d["metadados"]["registro_documentos"].get(cod) != cam:
        d["metadados"]["registro_documentos"][cod] = cam
        mudancas.append(("metadados", "registro_documentos:" + cod))

# ==================================================================== PT-06 ===
# A declaracao que caiu: o registro dizia que Cesarino (2022) continuava nao lida.
_pt06 = EV["PT-06"]["fonte_trecho"]
VELHO06 = ("CESARINO (2022), declarada no registro original, ENTROU no corpus em "
           "04/10/2026 e CONTINUA NÃO LIDA.")
assert VELHO06 in _pt06, "PT-06: a declaracao sobre Cesarino mudou de forma"
NOVO06 = (
    "CESARINO (2022) FOI LIDA EM 09/10/2026, e com isso se fecha uma declaração que "
    "o registro carregava desde agosto: a peça era citada sem ter sido lida, entrou "
    "no corpus em 04/10 e continuava não lida. A leitura CORROBORA o mecanismo "
    "retificado, de literatura independente — antropologia e cibernética, não ciência "
    "política — e com a tese de que o que sustenta a mobilização não é o conteúdo: "
    "“o bolsonarismo se define menos por um conteúdo ou base social fixa do que por "
    "uma dinâmica sociotécnica de mobilização contínua e performativa de demandas "
    "latentes, num fluxo de causalidade circular entre influenciadores e influenciados "
    "orientado por métricas em tempo real” (p. 164 impressa — PDF p. 3). "
    "E A MESMA PEÇA FECHA A PENDÊNCIA DO TELEGRAM E DO WHATSAPP, que estavam nomeados "
    "no campo sem verificação de primeira mão desde agosto: Cesarino descreve um "
    "“ecossistema em camadas múltiplas – que hoje inclui desde grandes plataformas do "
    "mainstream como YouTube e Facebook até aplicativos de mensagens fechados como "
    "Telegram e WhatsApp” (p. 181 impressa — PDF p. 20). A distinção que ela faz é "
    "FUNCIONAL — plataforma aberta de massa contra aplicativo de mensagem fechado —, "
    "e é isso, não a lista de nomes, que o registro precisava.")
poe("PT-06", "fonte_trecho", _pt06.replace(VELHO06, NOVO06))
poe("PT-06", "fonte_local", EV["PT-06"]["fonte_local"] + "; " + NOVOS["CESARINO 2022"])
poe("PT-06", "fonte_pagina", EV["PT-06"]["fonte_pagina"] + " | CESARINO 2022: 3, 20")
poe("PT-06", "nota_auditoria", (EV["PT-06"].get("nota_auditoria") or "") +
    " QUINTA RODADA, 09/10/2026 — Cesarino (2022) lida, por ordem do pesquisador de "
    "ler as quinze peças não lidas do eixo 13. Duas âncoras novas, e nenhuma muda "
    "campo: a primeira corrobora o mecanismo retificado em 04/10 de literatura "
    "independente; a segunda tira Telegram e WhatsApp da condição de nomes sem "
    "verificação, que era item de decisão desde 08/10. O registro não mudou de classe "
    "e nenhum campo foi reescrito.")

# ==================================================================== PT-03C ==
# A recomendacao sobre Madeira, executada. Ver o cabecalho deste arquivo.
poe("PT-03C", "fonte_trecho", EV["PT-03C"]["fonte_trecho"] +
    " || ACRÉSCIMO DE 09/10/2026 — PRIMEIRA LITERATURA A INTERPRETAR O ARCO JUDICIAL, "
    "que até aqui se apoiava só em acórdãos. Madeira, Marona e Del Río (2022), no "
    "capítulo 8, de Andrés del Río e André Rodrigues, documentam a PRESSÃO MILITAR "
    "SOBRE ESTE JULGAMENTO — que é precisamente o que um acórdão não pode registrar "
    "sobre si mesmo. O enquadramento geral: “Uma característica presente nesse "
    "processo de reconfigurar os sentidos da memória da democracia foi a participação "
    "ativa do âmbito militar no cenário político, violentando os sentidos da "
    "Constituição” (p. 254 impressa — PDF p. 256). E a condicional explícita, de um "
    "general de exército da reserva em início de abril de 2018, segundo a qual se o "
    "STF deixasse Lula solto e elegível então “só restará o recurso à reação armada. "
    "Aí é dever da Força Armada restaurar a ordem. Mas não creio que chegaremos lá” "
    "(p. 254 impressa — PDF p. 256). Na véspera do julgamento, o comandante do "
    "Exército — nomeado na mesma página 254 como o general Eduardo Villas Bôas — "
    "publicou em redes sociais: “Asseguro à Nação que o Exército Brasileiro julga "
    "compartilhar o anseio de todos os cidadãos de bem de repúdio à impunidade e de "
    "respeito à Constituição, à paz social e à Democracia, bem como se mantém atento "
    "às suas missões institucionais” (p. 265 impressa — PDF p. 267). "
    "LIMITES DECLARADOS: (a) os autores caracterizam as declarações como “ameaças de "
    "golpe”, e isso é avaliação deles, não do analista; (b) a peça é de junho de 2022 "
    "e não menciona 8 de janeiro — zero ocorrências em busca normalizada —, de modo "
    "que entra no arco pela montante, não pelo evento; (c) a identificação do "
    "comandante do Exército na página 265 é feita pela página 254 do mesmo capítulo, "
    "e não pela página citada.")
poe("PT-03C", "fonte_local", EV["PT-03C"]["fonte_local"] + "; " + NOVOS["MADEIRA ET AL 2022"])
poe("PT-03C", "fonte_pagina", "MADEIRA ET AL 2022: 256, 267")
poe("PT-03C", "nota_auditoria",
    "acrescentado em 09/10/2026, por encaminhamento do pesquisador — ele perguntou se "
    "a frase do general ia para PT-05 ou para o arco judicial e mandou executar a "
    "recomendação. VEIO PARA CÁ, por data, por referente e por lacuna: a declaração é "
    "de abril de 2018 e PT-05 cobre 2019-2022; o general condiciona a reação armada a "
    "uma decisão do STF, e esta é a decisão; e o arco judicial não tinha literatura "
    "nenhuma, só acórdãos. O campo mecanismo_causal NÃO mudou: ele já dizia que a "
    "margem de um voto alimentaria “nos dois campos, a leitura do STF como ator "
    "político”, e o que a literatura acrescenta é o lado militar dessa pressão, não "
    "uma cadeia causal nova. Este registro tinha fonte_pagina nulo até hoje.")

# ==================================================================== PT-19 ====
# Nenhuma ancora nova: um limite de atribuicao, que e resultado de leitura.
poe("PT-19", "fonte_trecho", EV["PT-19"]["fonte_trecho"] +
    " || LIMITE DE ATRIBUIÇÃO REGISTRADO EM 09/10/2026, e é resultado negativo da "
    "leitura das quinze peças do eixo 13. Bastos e Recuero (2023) parecia corroborar "
    "a referência ao Sri Lanka com literatura revisada por pares, e NÃO CORROBORA. A "
    "peça diz que a estratégia insurrecional foi “ostensibly inspired by the coups in "
    "Sri Lanka and Thailand that similarly bypassed the press altogether” (p. 4), mas "
    "a frase está no parágrafo de revisão e é atribuída a Keulenaar et al. (2023), que "
    "a própria peça qualifica como relatório NÃO PUBLICADO. O estudo dos autores "
    "analisa as declarações de Bolsonaro na campanha e a penetração do playbook entre "
    "parlamentares; o Sri Lanka não é achado deles. Tomar isso como segunda fonte "
    "independente seria citar uma citação. A REFERÊNCIA AO SRI LANKA CONTINUA "
    "ANCORADA SÓ NA CPMI (p. 614). A mesma cadeia desqualifica, para efeito de "
    "âncora, a divisão de plataformas que a mesma página afirma — coordenação via "
    "Telegram e difusão via Facebook e Instagram —, também de Keulenaar et al.")
poe("PT-19", "nota_auditoria", (EV["PT-19"].get("nota_auditoria") or "") +
    " QUINTA RODADA, 09/10/2026 — nenhum campo mudou. Entrou um limite de atribuição "
    "que a leitura descobriu e que, se não ficasse escrito, voltaria a parecer âncora "
    "na próxima vez que alguém abrisse a peça.")

# ==================================================================== PT-12A ===
poe("PT-12A", "fonte_trecho", EV["PT-12A"]["fonte_trecho"] +
    " || CORROBORAÇÃO DE LITERATURA, 09/10/2026, e é a primeira que este registro tem: "
    "até aqui a arquitetura de duas camadas era achado meu sobre os dados do COAF, sem "
    "literatura que a nomeasse. Nunes (2024) descreve a extrema direita brasileira "
    "organizada em torno de “empreendedores políticos” e atribui a essas ecologias "
    "“um edifício de várias camadas em que cada camada descendente preside sobre um "
    "público menor” (p. 11 impressa — PDF p. 11), comparando a estrutura à dos "
    "sistemas de marketing multinível. E liga essa estrutura ao evento: “Um ponto que "
    "me parece essencial para compreender o ocorrido nessa ocasião é justamente a "
    "estrutura multinível que acabamos de discutir” (p. 13 impressa — PDF p. 13). "
    "O ENCAIXE COM O ACHADO DO COAF É DIRETO: captação pulverizada na base, execução "
    "concentrada nos nós — é a mesma forma que Nunes descreve a partir de material "
    "inteiramente outro. LIMITE: Nunes não analisa o financiamento dos acampamentos "
    "nem cita o COAF; a convergência é de forma organizacional, não de evidência "
    "sobre o mesmo dado.")
poe("PT-12A", "fonte_local", EV["PT-12A"]["fonte_local"] + "; " + NOVOS["NUNES 2024"])
poe("PT-12A", "fonte_pagina", EV["PT-12A"]["fonte_pagina"] + " | NUNES 2024: 11, 13")
poe("PT-12A", "nota_auditoria", (EV["PT-12A"].get("nota_auditoria") or "") +
    " QUINTA RODADA, 09/10/2026 — primeira corroboração de literatura, por Nunes "
    "(2024). O mecanismo NÃO foi renomeado: a tipificação que a tarefa 19 cobra deste "
    "registro continua aberta, e a proposta está no documento 09.")

# ==================================================================== PT-62 ====
poe("PT-62", "fonte_trecho", (EV["PT-62"].get("fonte_trecho") or "") +
    " || ACRÉSCIMO DE 09/10/2026 — primeira literatura sobre o desfecho dos "
    "acampamentos, e ela QUALIFICA o mecanismo deste registro. Carvalho e Tatagiba "
    "(2025) registram que “O acampamento de Brasília foi a base para a manifestação na "
    "Esplanada dos Ministérios que, em 8 de janeiro, terminou com a invasão e "
    "destruição das sedes dos três poderes” (p. 35 impressa — PDF p. 35), e que depois "
    "do episódio os acampamentos perderam volume até serem desmobilizados em operações "
    "do exército — com a palavra desmobilizados entre aspas no original, que é a "
    "ressalva das autoras. A QUALIFICAÇÃO IMPORTA PARA O NOME DO MECANISMO: este "
    "registro chama o processo de desarticulação do repertório de rua com "
    "deslocamento, o que sugere movimento endógeno; as autoras documentam "
    "desmobilização por OPERAÇÃO ESTATAL. Deslocamento e desmobilização forçada não "
    "são o mesmo mecanismo. NOTA DE APARATO: o nome do mecanismo aparece acima SEM "
    "ASPAS de propósito. Na primeira execução deste script ele estava entre aspas "
    "curvas, e transcricoes() o promoveu a transcrição e foi procurá-lo no PDF de "
    "Carvalho e Tatagiba, onde evidentemente não está — a mesma armadilha que PT-08 "
    "expôs em 08/10, agora com o analista citando o próprio codebook. Aspas curvas em "
    "fonte_trecho são reservadas ao que está na fonte. "
    "LIMITE: a peça cobre 2023 e este registro projeta até "
    "2026, de modo que a âncora alcança o início da janela, não toda ela — e a classe "
    "do registro continua Inferência do analista.")
poe("PT-62", "fonte_local", (EV["PT-62"].get("fonte_local") or "") and
    (EV["PT-62"]["fonte_local"] + "; " + NOVOS["CARVALHO E TATAGIBA 2025"])
    or NOVOS["CARVALHO E TATAGIBA 2025"])
poe("PT-62", "fonte_pagina", "CARVALHO E TATAGIBA 2025: 35")
poe("PT-62", "nota_auditoria", (EV["PT-62"].get("nota_auditoria") or "") +
    " QUINTA RODADA, 09/10/2026 — primeira âncora de literatura num registro que era "
    "inferência pura. A CLASSE NÃO MUDOU, de propósito: a âncora cobre 2023 e o "
    "registro projeta até 2026. E a leitura levanta uma dúvida de nome que é da tarefa "
    "19: deslocamento endógeno não é desmobilização por operação do exército.")

# ==================================================================== revisao ==
d["metadados"]["revisoes"].append(
    "2026-10-09/10 — leitura das quinze peças não lidas do eixo 13, por ordem do "
    "pesquisador. Cinco registros ganharam conteúdo e NENHUM mudou de classe ou de "
    "nome de mecanismo: PT-06 (Cesarino 2022 lida — fecha a declaração de agosto e a "
    "pendência de Telegram/WhatsApp), PT-03C (Madeira et al. 2022 — primeira "
    "literatura do arco judicial, e primeira fonte_pagina deste registro), PT-19 "
    "(limite de atribuição: Bastos e Recuero NÃO corrobora o Sri Lanka, porque a "
    "frase é de Keulenaar et al. 2023, relatório não publicado), PT-12A (Nunes 2024 "
    "— primeira corroboração de literatura da arquitetura de duas camadas) e PT-62 "
    "(Carvalho e Tatagiba 2025 — e a peça QUALIFICA o nome do mecanismo: "
    "desmobilização por operação do exército não é deslocamento endógeno).")

# ==================================================================== escrita ==
# A GUARDA VEM ANTES DA ESCRITA. Na primeira execucao deste script o assert
# estava DEPOIS do write: a contagem esperada falhou, o JSON ja havia sido
# gravado, e foi preciso restaurar do backup. Guarda que dispara depois do
# efeito nao e guarda, e aviso.
print("%d alteração(ões) em %d registro(s):"
      % (len(mudancas), len({m[0] for m in mudancas})))
for pid, campo in mudancas:
    print("   %-10s %s" % (pid, campo))
ESPERADO = 22   # 4 em metadados + 4 PT-06 + 4 PT-03C + 2 PT-19 + 4 PT-12A + 4 PT-62
assert len(mudancas) == ESPERADO, "esperava %d mudancas, houve %d" % (ESPERADO, len(mudancas))

io.open(P, "w", encoding="utf-8", newline="\n").write(
    json.dumps(d, ensure_ascii=False, indent=2) + "\n")
print("\nCONTAGEM DE CLASSES (nao deve mudar): 61 primaria | 21 Confirmado | 1 Inferencia")
from collections import Counter
for k, v in Counter(e["status_classe"] for e in d["eventos"]).most_common():
    print("   %3d  %s" % (v, k))
