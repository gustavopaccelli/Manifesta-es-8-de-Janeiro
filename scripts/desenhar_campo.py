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


SVG_OUT = RAIZ / "reports/figures/figura_campo_multiorganizacional.svg"
HTML_OUT = RAIZ / "reports/figures/campo_multiorganizacional.html"


def carregar():
    with io.open(JSON_IN, encoding="utf-8") as f:
        regs = json.load(f)["eventos"]
    return {r["id"]: r for r in regs}, regs


# =============================================================================
# O DESENHO
# =============================================================================
# Sai do mesmo `ENTIDADES` que a planilha, e por isso não pode divergir dela:
# é a regra de 25/09/2026 aplicada a figura. Vive em `reports/figures/`, ao lado
# da cronologia — mas por razão oposta: aquela é conferida por
# `conferir_figuras.py` porque foi feita à mão, e esta dispensa conferência
# porque é gerada. A pasta passou a ter os dois regimes, e o cabeçalho de
# `conferir_figuras.py` diz qual peça está em qual.
#
# A composição é o argumento: em cima, a dicotomia do modelo — aliança à
# esquerda, conflito à direita, fronteira no meio. Embaixo, atravessando a
# fronteira, as cinco entidades que o modelo não acomoda. O desenho mostra a
# dicotomia e mostra onde ela não fecha.

def quebrar(texto, largura):
    """Quebra por contagem de caracteres; suficiente para rótulo curto."""
    linhas, atual = [], ""
    for p in texto.split():
        if len(atual) + len(p) + 1 <= largura:
            atual = (atual + " " + p).strip()
        else:
            linhas.append(atual)
            atual = p
    if atual:
        linhas.append(atual)
    return linhas


def caixa(x, y, w, rotulo, sub, cor, traco="", raio=6):
    """Devolve (svg, altura). A altura sai do texto — caixa fixa estourava o
    rótulo de duas linhas, que é o caso de metade das entidades."""
    linhas = quebrar(rotulo, int(w / 7.4))
    sublinhas = quebrar(sub, int(w / 5.6)) if sub else []
    h = 20 + 17 * len(linhas) + (15 * len(sublinhas) + 4 if sublinhas else 0)
    txt = ['<rect x="{}" y="{}" width="{}" height="{}" rx="{}" class="cx"'
           ' style="fill:var(--{}-f);stroke:var(--{}-s)"{}/>'.format(
               x, y, w, h, raio, cor, cor,
               ' stroke-dasharray="7 5"' if traco == "tracejada" else "")]
    yt = y + 19
    for l in linhas:
        txt.append('<text x="{}" y="{}" class="rot">{}</text>'.format(x + 14, yt, l))
        yt += 17
    yt += 2
    for l in sublinhas:
        txt.append('<text x="{}" y="{}" class="sub">{}</text>'.format(x + 14, yt, l))
        yt += 15
    return "\n".join(txt), h


def svg(por_id, regs):
    sistemas = defaultdict(list)
    for nome, s, refs, rec, _n in ENTIDADES:
        ids = sorted({r for r, _, _ in refs})
        sistemas[s].append((nome, ids, rec))

    W, DIV = 1240, 620
    p = []
    p.append('<text x="30" y="46" class="t1">O campo multiorganizacional do 8 de Janeiro</text>')
    p.append('<text x="30" y="72" class="t2">Ator focal declarado: {}</text>'.format(FOCAL))
    p.append('<text x="30" y="94" class="t3">Sistemas de aliança e de conflito na acepção de '
             'Klandermans (2013). Gerado de scripts/desenhar_campo.py — '
             '{} entidades, todas com lastro em registro do codebook.</text>'.format(len(ENTIDADES)))

    # a fronteira atravessa o desenho inteiro, porque é ela que está em questão
    DIVISOR = len(p)
    p.append('')  # a linha da fronteira entra no fim, com a altura real
    p.append('<text x="{}" y="124" class="eixo">fronteira do campo</text>'.format(DIV - 62))

    p.append('<text x="30" y="160" class="cab al">SISTEMA DE ALIANÇA</text>')
    p.append('<text x="30" y="178" class="glosa">provê recurso ou oportunidade ao foco</text>')
    p.append('<text x="910" y="160" class="cab co">SISTEMA DE CONFLITO</text>')
    p.append('<text x="910" y="178" class="glosa">drena recurso ou restringe oportunidade</text>')

    ya = yc = 196
    for nome, ids, rec in sistemas["ALIANÇA"]:
        s, h = caixa(30, ya, 300, nome, "{} · {}".format(" ".join(ids[:3]), rec), "al")
        p.append(s)
        ya += h + 9
    for nome, ids, rec in sistemas["CONFLITO"]:
        s, h = caixa(910, yc, 300, nome, " ".join(ids[:4]), "co")
        p.append(s)
        yc += h + 9

    p.append('<text x="392" y="238" class="cab ind">INDIFERENTES</text>')
    p.append('<text x="392" y="256" class="glosa">infraestrutura ou informação,</text>')
    p.append('<text x="392" y="272" class="glosa">sem tomar partido</text>')
    yi = 292
    for nome, ids, rec in sistemas["INDIFERENTE"]:
        s, h = caixa(392, yi, 200, nome, " ".join(ids), "ind")
        p.append(s)
        yi += h + 10

    # a faixa de baixo: o que o modelo não acomoda, atravessando a fronteira
    y = max(ya, yc, yi) + 62
    p.append('<text x="30" y="{}" class="cab qb">O QUE O MODELO NÃO ACOMODA</text>'.format(y - 26))
    p.append('<text x="30" y="{}" class="glosa">a unidade de análise de Klandermans é a organização — '
             'aqui ela se divide por escalão e por data</text>'.format(y - 8))
    for nome, ids, rec in sistemas["CINDIDA"]:
        s, h = caixa(150, y, 940, "CINDIDA — " + nome,
                     "nos dois sistemas ao mesmo tempo · " + " ".join(ids), "cin")
        p.append(s)
        y += h + 10
    for nome, ids, rec in sistemas["MIGRANTE"]:
        s, h = caixa(150, y, 940, "MIGRANTE — " + nome,
                     "aliança → conflito, com data · " + " ".join(ids), "mig")
        p.append(s)
        p.append('<path d="M {} {} l 26 9 l -26 9 z" class="seta"/>'.format(
            DIV - 13, y + h - 26))
        y += h + 10
    for nome, ids, rec in sistemas["CONTESTADA"]:
        s, h = caixa(150, y, 940, "CONTESTADA — " + nome,
                     "a classificação é o objeto da disputa do artigo · " + " ".join(ids),
                     "con", traco="tracejada")
        p.append(s)
        y += h + 10

    # o perfil por fase, que é onde a proposição do modelo não se confirma
    porfase = defaultdict(set)
    for nome, s, refs, _r, _n in ENTIDADES:
        for rid, _c, _f in refs:
            porfase[fase_larga(por_id[rid]["fase"])].add((nome, s))
    y += 34
    p.append('<text x="30" y="{}" class="cab">PRESENÇA POR FASE — e a proposição do ciclo '
             'não se confirma</text>'.format(y))
    p.append('<text x="30" y="{}" class="glosa">Klandermans prevê expansão no pico e '
             'desligamento na queda. O pico do campo é T-1 Operacional, e o lado da '
             'aliança desaparece em T0.</text>'.format(y + 18))
    y += 44
    for i, f in enumerate(ORDEM_FASE):
        ativas = porfase[f]
        al = sum(1 for _n, s in ativas if s == "ALIANÇA")
        est = len(ativas) - al
        x = 30 + i * 300
        p.append('<text x="{}" y="{}" class="fase">{}</text>'.format(x, y, f))
        p.append('<rect x="{}" y="{}" width="{}" height="20" class="bar al"'
                 ' style="fill:var(--al-s)"/>'.format(x, y + 10, max(al * 16, 2)))
        p.append('<rect x="{}" y="{}" width="{}" height="20" class="bar co"'
                 ' style="fill:var(--co-s)"/>'.format(x, y + 34, max(est * 16, 2)))
        p.append('<text x="{}" y="{}" class="num">{} de aliança</text>'.format(
            x + max(al * 16, 2) + 8, y + 25, al))
        p.append('<text x="{}" y="{}" class="num">{} do lado estatal</text>'.format(
            x + max(est * 16, 2) + 8, y + 49, est))
    H = y + 90
    p[DIVISOR] = ('<line x1="{0}" y1="130" x2="{0}" y2="{1}" class="div"/>'
                  .format(DIV, H - 150))

    estilo = """
  :root{--bg:#fbfbf9;--tx:#1a1a17;--tx2:#55524c;--ln:#c9c5bd;
    --al-f:#eef4ec;--al-s:#4a7a52;--co-f:#f6eeec;--co-s:#9c4f3f;
    --ind-f:#f2f1ed;--ind-s:#8a857b;--cin-f:#f2eff7;--cin-s:#6a5a8c;
    --mig-f:#fdf3e6;--mig-s:#a8762c;--con-f:#fbf0f4;--con-s:#8d3c5c}
  @media (prefers-color-scheme:dark){:root{--bg:#16161a;--tx:#ecebe7;--tx2:#a8a49c;--ln:#3b3a38;
    --al-f:#1d2a20;--al-s:#79ab80;--co-f:#2c1d1a;--co-s:#d08976;
    --ind-f:#232320;--ind-s:#9b968c;--cin-f:#231f2e;--cin-s:#a695c9;
    --mig-f:#2b2116;--mig-s:#d7a css;--con-f:#2a1a22;--con-s:#cf7f9f}}
  text{font-family:ui-sans-serif,-apple-system,"Segoe UI",Roboto,sans-serif}
  .t1{font-size:25px;font-weight:700;fill:var(--tx)}
  .t2{font-size:14px;fill:var(--tx2)}
  .t3{font-size:12.5px;fill:var(--tx2)}
  .cab{font-size:13px;font-weight:700;letter-spacing:.06em;fill:var(--tx)}
  .cab.al{fill:var(--al-s)} .cab.co{fill:var(--co-s)} .cab.ind{fill:var(--ind-s)}
  .cab.qb{fill:var(--cin-s)}
  .glosa{font-size:11.5px;fill:var(--tx2)}
  .eixo{font-size:11px;fill:var(--tx2);font-style:italic}
  .rot{font-size:13px;fill:var(--tx)}
  .sub{font-size:10.5px;fill:var(--tx2)}
  .cx{stroke-width:1.6}
  .div{stroke:var(--ln);stroke-width:2;stroke-dasharray:3 6}
  .seta{fill:var(--mig-s)}
  .fase{font-size:12px;font-weight:600;fill:var(--tx)}
  .num{font-size:11px;fill:var(--tx2)}
""".replace("#d7a css", "#d7a45e")

    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            'width="{w}" height="{h}" role="img" '
            'aria-label="Campo multiorganizacional do 8 de Janeiro">\n'
            '<style>{e}</style>\n'
            '<rect width="{w}" height="{h}" fill="var(--bg)"/>\n{c}\n</svg>\n'
            ).format(w=W, h=H, e=estilo, c="\n".join(p))


def html(desenho, por_id):
    ncab = Counter(s for _n, s, _r, _rc, _nt in ENTIDADES)
    linhas = []
    for nome, s, refs, rec, nota in ENTIDADES:
        ids = " ".join(sorted({r for r, _, _ in refs}))
        linhas.append("<tr><td class=s>{}</td><td><b>{}</b></td><td class=r>{}</td>"
                      "<td>{}</td><td class=n>{}</td></tr>".format(s, nome, ids, rec, nota))
    return """<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Campo multiorganizacional — 8 de Janeiro</title>
<style>
:root{{--bg:#fbfbf9;--tx:#1a1a17;--tx2:#55524c;--ln:#e2ded6;--cd:#fff}}
@media (prefers-color-scheme:dark){{:root{{--bg:#16161a;--tx:#ecebe7;--tx2:#a8a49c;
  --ln:#32312f;--cd:#1d1d21}}}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--tx);
  font:15px/1.6 ui-sans-serif,-apple-system,"Segoe UI",Roboto,sans-serif}}
main{{max-width:1300px;margin:0 auto;padding:32px 16px 72px}}
h1{{font-size:26px;margin:0 0 4px;line-height:1.25}}
.meta{{color:var(--tx2);font-size:13.5px;margin:0 0 28px}}
figure{{margin:0 0 36px;background:var(--cd);border:1px solid var(--ln);
  border-radius:10px;padding:8px;overflow-x:auto}}
svg{{display:block;min-width:900px;width:100%;height:auto}}
table{{width:100%;border-collapse:collapse;font-size:13.5px}}
th,td{{text-align:left;padding:9px 10px;border-bottom:1px solid var(--ln);
  vertical-align:top}}
th{{font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--tx2)}}
td.s{{font-size:11px;letter-spacing:.04em;white-space:nowrap;color:var(--tx2)}}
td.r{{font-family:ui-monospace,SFMono-Regular,Consolas,monospace;font-size:11.5px;
  white-space:nowrap;color:var(--tx2)}}
td.n{{color:var(--tx2);font-size:12.5px;max-width:34em}}
.av{{border-left:3px solid #a8762c;background:var(--cd);padding:12px 16px;
  border-radius:0 8px 8px 0;margin:0 0 28px;font-size:13.5px}}
h2{{font-size:17px;margin:34px 0 10px}}
code{{font-family:ui-monospace,Consolas,monospace;font-size:.92em}}
</style></head><body><main>
<h1>O campo multiorganizacional do 8 de Janeiro</h1>
<p class="meta">Ator focal declarado: <b>{focal}</b> · {n} entidades ·
gerado por <code>scripts/desenhar_campo.py</code> a partir de
<code>process_tracing_8jan_eventos.json</code></p>

<p class="av"><b>Campo é sempre de alguém.</b> Klandermans define campo como o das
organizações com que <i>a organização do movimento</i> pode estabelecer vínculo — a
definição é possessiva, e o codebook não é: ele codifica o episódio. Por isso o ator
focal é declarado, e trocá-lo inverte o campo. As {aliados} entidades de aliança, as
{opostos} de conflito e as {amb} que o modelo não acomoda estão todas ancoradas em
registro, e <code>--autoteste</code> aborta se um fragmento deixar de ocorrer no
campo declarado.</p>

<figure>{svg}</figure>

<h2>As {n} entidades</h2>
<table><thead><tr><th>Sistema</th><th>Entidade</th><th>Registros</th>
<th>Recurso</th><th>Nota</th></tr></thead><tbody>
{linhas}
</tbody></table>
</main></body></html>
""".format(focal=FOCAL, n=len(ENTIDADES), svg=desenho, linhas="\n".join(linhas),
           aliados=ncab["ALIANÇA"], opostos=ncab["CONFLITO"],
           amb=ncab["CINDIDA"] + ncab["MIGRANTE"] + ncab["CONTESTADA"])


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
    # Piso, não igualdade: o codebook cresce, e prender o número aqui obrigaria
    # a editar este script a cada registro novo — a brittleness que o projeto
    # combate. Quem garante a aderência ao codebook é verificar(), que exige
    # que cada fragmento declarado ocorra no campo declarado do registro.
    assert len(regs) >= 82, "o codebook encolheu: {} registros".format(len(regs))

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

    desenho = svg(por_id, regs)
    io.open(SVG_OUT, "w", encoding="utf-8", newline="\n").write(desenho)
    io.open(HTML_OUT, "w", encoding="utf-8", newline="\n").write(html(desenho, por_id))

    print()
    print("Planilha: {}".format(SAIDA.relative_to(RAIZ)))
    print("Desenho:  {}".format(SVG_OUT.relative_to(RAIZ)))
    print("Página:   {}".format(HTML_OUT.relative_to(RAIZ)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
