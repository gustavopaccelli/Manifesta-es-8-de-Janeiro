#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
O campo multiorganizacional do 8 de Janeiro — sistemas de aliança e de conflito.

Tarefa 21 da "Ordem de ataque". Cobrança do verbete *Multiorganizational
fields* (KLANDERMANS, B. In: SNOW et al., 2013, `10.1002/9780470674871.wbespm139`),
lido na fonte em 30/09/2026: os atores estão no codebook, o campo não existia
como peça.

=============================================================================
POR QUE O CAMPO PRECISA DE UM ATOR FOCAL DECLARADO
=============================================================================

Klandermans define campo multiorganizacional como "the total possible number of
organizations with which **the movement organization** might establish specific
links", decomposto no **alliance system** — "groups and organizations that
support it" — e no **conflict system**, "groups and organizations that oppose
it". A definição é possessiva: **o campo é sempre de alguém.**

O codebook não é. Ele codifica o **episódio**, não um movimento: em T-1
Conjuntural o `ator_grupo` é majoritariamente tribunal — STF, TRF-4, TSE, a 13ª
Vara —, em T0 são manifestantes e batalhões da PMDF, em T+1 são STF, PF, PGR e
Congresso. Somar `ator_grupo` não produz um campo; produz a lista de quem agiu.

Por isso este script **declara o foco** — a coalizão bolsonarista desafiante — e
classifica cada entidade em relação a ele. Trocado o foco, o campo se inverte,
e é isso que o modelo prevê.

=============================================================================
O CRITÉRIO, QUE NÃO É DE OPINIÃO
=============================================================================

Cada entidade entra com os registros que a sustentam e o **campo do codebook**
em que ela aparece. A regra de leitura é a do próprio Klandermans:

  ALIANÇA   aparece em `ator_grupo` provendo recurso ou oportunidade ao foco
            ("alliance systems provide resources and create political
            opportunities")
  CONFLITO  aparece em `target_alvo` do foco, ou em `ator_grupo` de registro
            cujo alvo é o foco ("conflict systems drain resources and restrict
            opportunities")
  INDIFERENTE  presta infraestrutura ou informação sem tomar partido
  CINDIDA   está nos dois sistemas ao mesmo tempo — ver abaixo

`verificar()` exige que o fragmento declarado **ocorra literalmente** no campo
declarado do registro declarado. Digitar a classificação sem lastro aborta a
execução. É o mesmo mecanismo de `triar_dois.py`, e existe pela mesma razão: o
modo de falha deste projeto é a cifra correta no referente errado, e aqui o
risco equivalente é a entidade certa no sistema errado.

=============================================================================
O QUE O CASO FAZ COM O MODELO — E É O ACHADO
=============================================================================

Klandermans prevê fronteira fluida: "organizations that try to keep aloof from
the controversy may choose **or be forced** to take sides. **Coalitions can fall
apart and former allies can become opponents.**" O caso tem isso, e tem mais.

**A PMDF está nos dois sistemas no mesmo dia, cindida por escalão.** O comando
produz o dispositivo deliberadamente inferior (PT-18, PT-19B); os pelotões de
choque são a linha de contenção invadida (PT-28, PT-31, PT-32) e depois quem
dispersa (PT-41) e desmonta o acampamento (PT-52). O mesmo vale para as Forças
Armadas: destinatárias do apelo (PT-12), presentes na certificação (PT-13),
anfitriãs do acampamento no SMU (PT-20), reforço tático contra a invasão
(PT-43) e executoras da desmobilização (PT-52).

**Isso não é fronteira fluida: é a unidade de análise que não se sustenta.** O
modelo toma a organização como unidade, e aqui a organização se divide
internamente por escalão e por hora do dia. É uma cobrança do caso ao modelo, e
está registrada como tal — não corrigida no silêncio.

=============================================================================
O QUE ESTE SCRIPT NÃO FAZ
=============================================================================

1. **Não decide o caso contestado.** A cúpula da segurança do DF entra como
   `CONTESTADA`, com as duas leituras escritas na própria linha: omissão
   deliberada, que é o que o codebook afirma, e seletividade estrutural do
   policiamento, que é a hipótese rival lida na fonte em *Policing protest*
   (tarefa 20). Escolher é juízo do pesquisador.
2. **Não inclui os apoiadores de Trump (PT-08).** Campo é relação; PT-08 é
   difusão por laço indireto, sem vínculo organizacional demonstrado. Fica fora
   por definição, e a ausência é declarada.
3. **Não pontua nem pesa.** Não há índice de centralidade: o codebook registra
   presença em registro, não intensidade de vínculo.

Uso:  python scripts/desenhar_campo.py [--autoteste]
"""
import csv
import io
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parent.parent
JSON_IN = RAIZ / "process_tracing_8jan_eventos.json"
SAIDA = RAIZ / "data/processed/campo_multiorganizacional.csv"

FOCAL = "coalizão bolsonarista desafiante (os acampamentos e a rede de convocação)"

# Tipos de recurso: os cinco de EDWARDS & GILLHAM (2013), verbete de RMT,
# `10.1002/9780470674871.wbespm447`, lido na fonte em 30/09/2026.
# (nome, sistema, [(registro, campo, fragmento)], recurso, nota)
ENTIDADES = [
    # ---------------------------------------------------------------- ALIANÇA
    ("Presidência da República / Jair Bolsonaro", "ALIANÇA",
     [("PT-05", "ator_grupo", "Presidência da República"),
      ("PT-11", "ator_grupo", "Jair Bolsonaro"),
      ("PT-13", "ator_grupo", "Presidência da República"),
      ("PT-17", "ator_grupo", "Jair Bolsonaro")],
     "moral",
     "Topo do sistema de aliança: é a autoridade externa cuja validação PT-13 "
     "registra. Migra — ver CINDIDAS E MIGRANTES."),

    ("Movimento Brasil Verde e Amarelo (MBVA) / Aprosoja", "ALIANÇA",
     [("PT-10A", "ator_grupo", "Movimento Brasil Verde e Amarelo")],
     "material",
     "Empresariado do agronegócio; o STF bloqueou contas por suspeita de "
     "financiamento (Pet. 10.685), o que é o sistema de conflito drenando "
     "recurso do de aliança."),

    ("Caminhoneiros", "ALIANÇA",
     [("PT-10", "ator_grupo", "Caminhoneiros")],
     "humano",
     "Repertório de bloqueio; recurso humano e de perturbação."),

    ("Rede de doadores e nós centralizadores (USA Brasil Informática)", "ALIANÇA",
     [("PT-12A", "ator_grupo", "USA Brasil Informática")],
     "material",
     "As quatro vias de acesso a recurso de RMT aparecem aqui: agregação de "
     "doação dispersa, patrocínio empresarial e fornecimento in natura."),

    ("Caravanas de ônibus e seus financiadores", "ALIANÇA",
     [("PT-21", "ator_grupo", "Caravanas de ônibus"),
      ("PT-21", "ator_grupo", "financiadores")],
     "material",
     "Nenhuma interdição registrada — o recurso circulou sem obstáculo estatal."),

    ("Coligação Pelo Bem do Brasil (PL, Republicanos, Progressistas)", "ALIANÇA",
     [("PT-14", "ator_grupo", "Coligação Pelo Bem do Brasil")],
     "moral",
     "O aliado partidário na arena institucional — e a ação foi negada pela "
     "presidência do TSE. Aliança que não converteu em oportunidade."),

    ("Perfis e canais bolsonaristas (Telegram, WhatsApp, Instagram)", "ALIANÇA",
     [("PT-04", "ator_grupo", "redes digitais (WhatsApp)"),
      ("PT-19", "ator_grupo", "Perfis e canais bolsonaristas")],
     "social-organizacional",
     "A infraestrutura de convocação; em PT-06 é o ecossistema paralelo que "
     "serve de base."),

    ("Anunciantes não identificados", "ALIANÇA",
     [("PT-19A", "ator_grupo", "Anunciantes não identificados")],
     "material",
     "Anúncio pago é recurso material convertido em alcance. Os anunciantes "
     "não foram identificados no levantamento — o nó do campo existe e não "
     "tem nome."),

    # ------------------------------------------------------------ INDIFERENTE
    ("Plataformas da Meta", "INDIFERENTE",
     [("PT-19A", "ator_grupo", "plataformas da Meta como veículo")],
     "social-organizacional",
     "Veículo, não parte. É a 'infrastructure' de RMT — recurso "
     "não-proprietário. A moderação própria mostrou-se insuficiente, e nenhuma "
     "medida estatal foi registrada no período."),

    ("Abin", "INDIFERENTE",
     [("PT-22", "ator_grupo", "Abin (produtor de alerta)"),
      ("PT-23", "ator_grupo", "Abin")],
     "—",
     "Produziu alerta e não integrou nenhum dos dois sistemas em ação: a "
     "informação circulou sem medida proporcional. É o caso que *Policing "
     "protest* nomeia como sobrecarga analítica."),

    # --------------------------------------------------------------- CONFLITO
    ("STF", "CONFLITO",
     [("PT-05", "target_alvo", "STF"),
      ("PT-19", "target_alvo", "Palácio do Planalto, Congresso Nacional e STF"),
      ("PT-35", "target_alvo", "STF (Poder Judiciário)"),
      ("PT-49", "ator_grupo", "Ministro Alexandre de Moraes (STF)"),
      ("PT-53", "ator_grupo", "STF"),
      ("PT-56", "ator_grupo", "Primeira Turma do STF"),
      ("PT-57", "ator_grupo", "STF"),
      ("PT-58", "ator_grupo", "Min. Alexandre de Moraes (STF)")],
     "—",
     "Alvo simbólico em T-1 e T0, e o principal agente do sistema de conflito "
     "em T+1. É a entidade com mais registros nos dois papéis."),

    ("TSE", "CONFLITO",
     [("PT-05", "target_alvo", "TSE"),
      ("PT-14", "target_alvo", "TSE"),
      ("PT-08B", "ator_grupo", "Ministro Alexandre de Moraes, na presidência do TSE")],
     "—",
     "Alvo da ação da coligação e emissor da ordem que contrariou a PRF na "
     "véspera do pleito."),

    ("Congresso Nacional", "CONFLITO",
     [("PT-29", "target_alvo", "Congresso Nacional (Poder Legislativo)"),
      ("PT-37", "target_alvo", "Congresso Nacional"),
      ("PT-46", "target_alvo", "Congresso Nacional"),
      ("PT-54", "ator_grupo", "Congresso Nacional — CPMI do 8 de Janeiro"),
      ("PT-55", "ator_grupo", "CPMI do 8 de Janeiro")],
     "—",
     "Alvo físico em T0 e instância de apuração em T+1. Em T-2 (PT-03) o "
     "Congresso integrava a coalizão pró-impeachment — outro episódio, outro "
     "campo."),

    ("Polícia Federal", "CONFLITO",
     [("PT-15", "target_alvo", "Polícia Federal"),
      ("PT-53", "ator_grupo", "Polícia Federal"),
      ("PT-58", "ator_grupo", "Polícia Federal")],
     "—",
     "E há defecção interna do aparelho a registrar: em PT-08A a cúpula da PF "
     "na Bahia RECUSOU o pedido de operação conjunta. O sistema de conflito se "
     "forma por recusa, não só por ação."),

    ("PGR", "CONFLITO",
     [("PT-53", "ator_grupo", "PGR"),
      ("PT-58", "ator_grupo", "PGR"),
      ("PT-60", "ator_grupo", "PGR (parecer favorável)")],
     "—", "Titular da ação penal em T+1."),

    ("Governo federal a partir de 01/01/2023 (Lula)", "CONFLITO",
     [("PT-45", "ator_grupo", "Presidente Luiz Inácio Lula da Silva"),
      ("PT-51", "ator_grupo", "Lula")],
     "—",
     "A mudança de configuração de poder tem data: o aliado deixou o governo "
     "sete dias antes de T0."),

    ("Ricardo Cappelli (intervenção federal)", "CONFLITO",
     [("PT-48", "ator_grupo", "Ricardo Cappelli (interventor federal)")],
     "—", "Executor da desmobilização do acampamento do QG."),

    # ----------------------------------------------------- CINDIDAS E MIGRANTES
    ("Forças Armadas", "CINDIDA",
     [("PT-12", "target_alvo", "Forças Armadas (destinatário do apelo)"),
      ("PT-13", "ator_grupo", "comandantes das Forças"),
      ("PT-20", "ator_grupo", "Acampados no Setor Militar Urbano"),
      ("PT-43", "ator_grupo", "Comando Militar do Planalto"),
      ("PT-52", "ator_grupo", "Polícia do Exército")],
     "moral e social-organizacional",
     "Cinco posições em cinco registros: destinatária do apelo, presente na "
     "certificação, anfitriã do acampamento, reforço tático contra a invasão e "
     "executora da desmobilização."),

    ("PMDF", "CINDIDA",
     [("PT-18", "ator_grupo", "Comando da PMDF"),
      ("PT-19B", "ator_grupo", "Coronel Jorge Henrique da Silva Pinto (PMDF)"),
      ("PT-28", "ator_grupo", "PMDF — 1º Batalhão de Policiamento de Choque"),
      ("PT-31", "ator_grupo", "PMDF — 2º Pelotão de Policiamento de Choque"),
      ("PT-32", "ator_grupo", "1º Pelotão de Choque da PMDF"),
      ("PT-41", "ator_grupo", "Batalhão de Choque da PMDF"),
      ("PT-52", "ator_grupo", "PMDF")],
     "—",
     "Cindida por escalão no mesmo dia: o comando planeja o dispositivo "
     "inferior, os pelotões são a linha invadida, e a corporação desmonta o "
     "acampamento em 09/01."),

    ("Anderson Torres, MJ e PRF (Silvinei Vasques)", "MIGRANTE",
     [("PT-08A", "ator_grupo", "Anderson Torres (ministro da Justiça)"),
      ("PT-08A", "ator_grupo", "Silvinei Vasques (diretor-geral da PRF)"),
      ("PT-08C", "ator_grupo", "Polícia Rodoviária Federal"),
      ("PT-42", "target_alvo", "Anderson Torres")],
     "—",
     "Aparelho de Estado operando a favor da causa do foco em PT-08A e PT-08C, "
     "e alvo em PT-42 (demissão), com prisão de Vasques em 09/08/2023. "
     "Aliança → conflito, com data."),

    ("Ibaneis Rocha / Governo do Distrito Federal", "MIGRANTE",
     [("PT-42", "ator_grupo", "Ibaneis Rocha (governador do DF)"),
      ("PT-45", "target_alvo", "Governo do Distrito Federal"),
      ("PT-47", "ator_grupo", "Ibaneis Rocha")],
     "—",
     "Demite o aliado (PT-42), torna-se alvo da intervenção federal (PT-45) e "
     "pede desculpas publicamente (PT-47). É o 'forced to take sides' de "
     "Klandermans em três registros."),

    # -------------------------------------------------------------- CONTESTADA
    ("Cúpula da segurança pública do DF (SSP-DF, SOI, GSI)", "CONTESTADA",
     [("PT-18", "ator_grupo", "SOI/SSP-DF"),
      ("PT-19B", "ator_grupo", "Fernando de Sousa Oliveira"),
      ("PT-20A", "ator_grupo", "coordenador de segurança do GSI"),
      ("PT-20B", "ator_grupo", "Subsecretaria de Inteligência da SSP-DF")],
     "—",
     "DUAS LEITURAS, e o script não escolhe. (a) omissão deliberada, que é o "
     "que o codebook afirma — dispositivo inferior ao da posse em regime e em "
     "planejamento, e nenhuma elevação após os alertas. (b) seletividade "
     "estrutural: della Porta & Reiter registram que a repressão recai menos "
     "sobre grupos ricos em recurso e em conexão política, o que prediz "
     "policiamento brando sem conivência. Ver tarefa 20."),
]

# Entidade declarada fora do campo, com a razão. Ver item 2 do cabeçalho.
FORA = [
    ("Apoiadores de Donald Trump (EUA)", "PT-08",
     "Campo é vínculo organizacional; PT-08 é difusão por laço indireto, e o "
     "laço direto (Bannon) não está demonstrado em nenhuma fonte lida."),
]

SISTEMAS = ["ALIANÇA", "INDIFERENTE", "CONFLITO", "CINDIDA", "MIGRANTE", "CONTESTADA"]


def carregar():
    with io.open(JSON_IN, encoding="utf-8") as f:
        regs = json.load(f)["eventos"]
    return {r["id"]: r for r in regs}, regs


def verificar(por_id):
    """Todo fragmento declarado tem de ocorrer no campo declarado do registro.

    Devolve a lista de falhas; vazia quando o campo inteiro tem lastro."""
    falhas = []
    for nome, sistema, refs, _rec, _nota in ENTIDADES:
        if sistema not in SISTEMAS:
            falhas.append("{}: sistema desconhecido '{}'".format(nome, sistema))
        for rid, campo, frag in refs:
            r = por_id.get(rid)
            if r is None:
                falhas.append("{}: registro {} nao existe".format(nome, rid))
                continue
            if campo not in r:
                falhas.append("{}: campo '{}' nao existe em {}".format(nome, campo, rid))
                continue
            if frag.lower() not in (r.get(campo) or "").lower():
                falhas.append("{}: '{}' ausente de {}.{}".format(nome, frag, rid, campo))
    for nome, rid, _ in FORA:
        if rid not in por_id:
            falhas.append("FORA {}: registro {} nao existe".format(nome, rid))
    return falhas


def fase_larga(f):
    """Agrupa as 15 fases do codebook nas quatro do desenho em camadas."""
    if f.startswith("T-1 Conjuntural"):
        return "T-1 Conjuntural"
    if f.startswith("T-1 Operacional"):
        return "T-1 Operacional"
    if f.startswith("T0"):
        return "T0"
    return "T+1"


ORDEM_FASE = ["T-1 Conjuntural", "T-1 Operacional", "T0", "T+1"]


def autoteste():
    por_id, regs = carregar()
    assert len(regs) == 82, "o codebook tem 82 registros; achei {}".format(len(regs))

    falhas = verificar(por_id)
    assert not falhas, "declaracoes sem lastro:\n  " + "\n  ".join(falhas)

    # Negativa por injeção de defeito: um fragmento falso tem de ser pego.
    global ENTIDADES
    guardado = ENTIDADES
    try:
        ENTIDADES = [("Falso", "ALIANÇA",
                      [("PT-13", "ator_grupo", "Confederação Nacional dos Metalúrgicos")],
                      "—", "injetado pelo autoteste")]
        assert verificar(por_id), "a checagem deixou passar fragmento inexistente"
    finally:
        ENTIDADES = guardado

    # O foco tem de estar declarado, e os quatro casos que o modelo não prevê.
    assert FOCAL and "bolsonarista" in FOCAL
    for s in ("CINDIDA", "MIGRANTE", "CONTESTADA"):
        assert any(e[1] == s for e in ENTIDADES), "nenhuma entidade em " + s
    assert fase_larga("T0/T+1 Resposta institucional") == "T0"
    assert fase_larga("T+1 Resposta judicial") == "T+1"
    print("autoteste OK — 82 registros, {} entidades com lastro, prova negativa".format(
        len(ENTIDADES)))


def main():
    if "--autoteste" in sys.argv:
        autoteste()
        return 0

    por_id, regs = carregar()
    falhas = verificar(por_id)
    if falhas:
        print("ABORTA — declaracoes sem lastro no codebook:")
        for f in falhas:
            print("  " + f)
        return 1

    linhas = []
    for nome, sistema, refs, recurso, nota in ENTIDADES:
        fases = sorted({fase_larga(por_id[r]["fase"]) for r, _, _ in refs},
                       key=ORDEM_FASE.index)
        linhas.append({
            "sistema": sistema,
            "entidade": nome,
            "recurso": recurso,
            "registros": " ".join(sorted({r for r, _, _ in refs})),
            "n_registros": len({r for r, _, _ in refs}),
            "fases": " ".join(fases),
            "papel_alvo": sum(1 for _, c, _ in refs if c == "target_alvo"),
            "papel_ator": sum(1 for _, c, _ in refs if c == "ator_grupo"),
            "nota": nota,
        })
    linhas.sort(key=lambda d: (SISTEMAS.index(d["sistema"]), -d["n_registros"]))
    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    with io.open(SAIDA, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0].keys()))
        w.writeheader()
        w.writerows(linhas)

    print("Ator focal declarado: **{}**".format(FOCAL))
    print()
    cont = Counter(d["sistema"] for d in linhas)
    print("| Sistema | Entidades | O que é |")
    print("|:--|--:|:--|")
    glosa = {
        "ALIANÇA": "provê recurso ou oportunidade ao foco",
        "INDIFERENTE": "presta infraestrutura ou informação sem tomar partido",
        "CONFLITO": "drena recurso ou restringe oportunidade",
        "CINDIDA": "nos dois sistemas ao mesmo tempo — o modelo não prevê",
        "MIGRANTE": "mudou de sistema, com data",
        "CONTESTADA": "a classificação é o objeto da disputa",
    }
    for s in SISTEMAS:
        if cont[s]:
            print("| {} | {} | {} |".format(s, cont[s], glosa[s]))
    print("| **Total** | **{}** | |".format(len(linhas)))

    print()
    print("### Presença por fase — a proposição de Klandermans, testada")
    print()
    print("Klandermans: *\"a proporção do campo engajada em um dos dois sistemas "
          "expande ou contrai conforme os ciclos de protesto. No **pico**, "
          "organizações inicialmente indiferentes tomam partido; na **queda**, "
          "organizações se desligam.\"*")
    print()
    porfase = defaultdict(Counter)
    for nome, sistema, refs, _r, _n in ENTIDADES:
        for rid, _c, _f in refs:
            porfase[fase_larga(por_id[rid]["fase"])][nome] = 1
    # Quebra por sistema, porque o total esconde o achado: o lado do foco
    # desaparece em T0 enquanto o do Estado se individua em batalhões.
    sist = {nome: s for nome, s, _r, _rc, _n in ENTIDADES}
    do_foco = {"ALIANÇA"}
    do_estado = {"CONFLITO", "CINDIDA", "MIGRANTE", "CONTESTADA"}
    nreg = Counter(fase_larga(r["fase"]) for r in regs)
    print("| Fase | Entidades ativas | do sistema de ALIANÇA | do lado estatal | Registros |")
    print("|:--|--:|--:|--:|--:|")
    for f in ORDEM_FASE:
        ativas = list(porfase[f])
        a = sum(1 for n in ativas if sist[n] in do_foco)
        e = sum(1 for n in ativas if sist[n] in do_estado)
        print("| {} | {} | {} | {} | {} |".format(f, len(ativas), a, e, nreg[f]))
    print()
    print("**A proposição não se confirma como enunciada.** O pico de engajamento "
          "do campo é **T-1 Operacional**, não T0. E a quebra por sistema mostra "
          "por quê: em T0 o lado do foco **desaparece como organização** — o "
          "codebook registra ali multidão, marcha e manifestantes radicalizados —, "
          "enquanto o lado estatal se **individua em batalhões e pelotões**. "
          "Se isso é propriedade do episódio ou da codificação de T0 é pergunta "
          "aberta, e está registrada como tal.")

    print()
    print("### As entidades que o modelo não acomoda")
    print()
    for d in linhas:
        if d["sistema"] in ("CINDIDA", "MIGRANTE", "CONTESTADA"):
            print("- **{}** ({}) — {} registros: {}".format(
                d["entidade"], d["sistema"], d["n_registros"], d["registros"]))

    print()
    print("### Declarado fora do campo")
    for nome, rid, razao in FORA:
        print("- **{}** ({}): {}".format(nome, rid, razao))

    print()
    print("Planilha: {}".format(SAIDA.relative_to(RAIZ)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
