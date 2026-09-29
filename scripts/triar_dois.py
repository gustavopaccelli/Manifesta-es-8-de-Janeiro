#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Triagem por pertinência dos DOIs verificados das sínteses LeapSpace.

Passo 2 do encaminhamento do item 11.3 da agenda, depois de `verificar_dois_sinteses.py`
ter fechado o passo 1 (existência e atribuição). Emite
`data/processed/triagem_dois.csv`, com os 411 classificados em três camadas.

O CRITÉRIO, E ELE NÃO É DE GOSTO. Pertinência aqui significa **uma coisa só**:
sustentar um mecanismo que o codebook efetivamente afirma. O vocabulário causal
foi extraído dos 82 campos `mecanismo_causal` do JSON, não de uma ideia geral do
que seja literatura de movimentos sociais. É este:

  certificação e descertificação (PT-03, PT-13, PT-50, PT-06B)
  apropriação e mudança de repertório, spin-off (PT-01, PT-02, PT-12, PT-33, PT-38)
  difusão e emulação transnacional (PT-08)
  alinhamento de quadros e recaptura do enquadramento (PT-07, PT-50A)
  estrutura de oportunidade política e eleitoral, e sua reversão (PT-02A, PT-03D, PT-05A, PT-06C)
  estruturas de mobilização, recursos e rede com nós (PT-10A, PT-12A, PT-19, PT-21, PT-52)
  policing do protesto, defecção do agente de contenção, falha de conversão (PT-20A, PT-22, PT-28, PT-31, PT-32)
  limiar, massa crítica e contágio (PT-29, PT-30, PT-34)
  radicalização de flanco e escalada (PT-15, PT-16, PT-24, PT-33)
  repressão seletiva e escalonada, custo penal (PT-53, PT-61)
  ciclo de protesto e desmobilização (PT-52, PT-62)
  método: process tracing, teste hoop e smoking gun, mecanismo causal (o desenho todo)

AS TRÊS CAMADAS

  A  Sustenta um mecanismo afirmado, ou é a referência canônica do conceito que o
     codebook usa pelo nome. Vai para a bibliografia do projeto — **depois de lida
     na fonte**, que é o passo 3 e não está feito.
  B  Leitura útil, decisão na escrita: teoria geral do campo, caso empírico
     comparável, verbete de enciclopédia, ou instrumento metodológico adjacente.
  C  Fora. Não é juízo de qualidade: é ausência de relação com o argumento.

O BURACO, QUE É O ACHADO PRINCIPAL. As sínteses **não contêm** `Dynamics of
Contention` (McAdam, Tarrow & Tilly, 2001) nem `Power in Movement` — zero
ocorrências — e nenhum dos 411 títulos traz *certification*, *brokerage*, *blame*,
*threshold* ou *critical mass*. São cinco famílias de mecanismo que o codebook
afirma **pelo nome**, e PT-03D diz literalmente "em vocabulário de Tilly e
Tarrow". A camada A nomeia 25 dos 82 registros; para os outros 57 a literatura
precisa ser acrescentada à mão, como os clássicos brasileiros do item 11.4. Uma
lista de DOIs gerada por sistema é densa onde a produção recente é densa —
enquadramento, ativismo digital, formação do Estado em Tilly — e rala onde estão
os clássicos que o desenho usa. Isso não se descobre contando DOIs: descobre-se
procurando, no corpus, cada mecanismo que o codebook afirma.

O QUE ESTA TRIAGEM NÃO É. Ela lê **título, veículo, ano, autoria e assunto** — o
que a agência registra. Não lê as obras. Nenhum item de A é citável antes do
passo 3, e a regra do projeto continua valendo: nada entra em texto sem
conferência na fonte. Ver `projeto-pos-doc/08_BIBLIOGRAFIA-METODOLOGICA.md`,
onde as dez primeiras fichas mostram quanto a metadado sobrevive à leitura.

POR QUE A CHAVE É O TÍTULO, E NÃO O DOI. Digitar 100 DOIs à mão é convidar o
defeito que este projeto persegue desde agosto. Cada linha da triagem traz um
fragmento de título — ou o título inteiro, prefixado por `=`, quando ele é
subcadeia de outros — e **quantas** correspondências espera; o script resolve os
DOIs e aborta se achar número diferente. Uma referência inventada por engano não
sobrevive à execução.

Uso:  python scripts/triar_dois.py
"""

import csv
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parent.parent
CSV_IN = RAIZ / "data/processed/dois_sinteses_leapspace.csv"
CSV_OUT = RAIZ / "data/processed/triagem_dois.csv"
CACHE = RAIZ / "data/external/crossref_cache.jsonl"

# As 21 entradas que a síntese cita por LINK DO SCOPUS, sem DOI, ficaram fora do
# universo dos 411 — e duas delas eram centrais. Busca por título no CrossRef
# recuperou 8 identificadores distintos, com casamento de título exato; os
# metadados vieram da agência para o cache, nada foi digitado aqui além do DOI, e
# `main` aborta se algum não estiver confirmado no cache.
RECUPERADOS = {
    "10.17813/maiq.19.1.x74278226830m69l": ("A", "PT-07: o balanço de 25 anos do alinhamento de quadros, "
        "pelos próprios autores da formulação — e a síntese o citava sem DOI"),
    "10.17813/maiq.14.3.kx87723664558jm4": ("A", "PT-07 e PT-50A: oportunidades discursivas e regras de "
        "sentimento; é o Bröer & Duyvendak que 08_BIBLIOGRAFIA-METODOLOGICA já apontava como de interesse"),
    "10.17813/maiq.17.1.u7rw348t8200174h": ("A", "PT-06, PT-15 e PT-16: dinâmica relacional da "
        "radicalização — o mecanismo da radicalização de flanco, em quadro comparativo"),
    "10.17813/maiq.14.2.u210745765568737": ("B", "oportunidade política em contexto altamente repressivo"),
    "10.17813/maiq.16.3.t5578801065mx5w0": ("B", "contexto político e engajamento organizacional, em série de países"),
    "10.17813/maiq.13.3.px4848183v2t073w": ("B", "oportunidade política e mobilização de desempregados"),
    "10.5153/sro.1856": ("B", "crítica à leitura estrutural da mobilização — antecipação de crítica"),
    "10.4324/9781315063362-34": ("C", "desenvolvimento capitalista e democracia; o codebook não afirma "
        "mecanismo estrutural de democratização"),
}

# (fragmento do título, correspondências esperadas, camada, uso no argumento)
TRIAGEM = [
    # ---------------------------------------------------------------- MÉTODO (A)
    ("Understanding Process Tracing", 1, "A", "método: os quatro testes; o codebook usa 'hoop test' pelo nome em PT-28"),
    ("The Logic of Process Tracing Tests", 1, "A", "método: formalização dos testes de process tracing"),
    ("Process-Tracing Methods", 1, "A", "método: manual de referência — ATENÇÃO, é a 1ª ed. (2013); o projeto cita a 2ª (2019), 10.3998/mpub.10072208"),
    ("Process Tracing and Qualitative Causal Inference", 1, "A", "método: o que a inferência de mecanismo pode e não pode afirmar"),
    ("=Case Study Research", 1, "A", "método: desenho de estudo de caso único, que é o desenho deste projeto"),
    ("Thinking about Mechanisms", 1, "A", "método: a definição de mecanismo de que o codebook depende em 82 campos"),
    ("Mechanisms in the Analysis of Social Macro-Phenomena", 1, "A", "método: mecanismo ligando micro-ato e desfecho macro — o problema deste caso"),
    ("Context and Causal Mechanisms in Political Analysis", 1, "A", "método: mecanismo é sempre situado em contexto; sustenta a camada T-1 conjuntural"),
    ("CONTENTIOUS EPISODE ANALYSIS", 1, "A", "método: a unidade 'episódio contencioso' é a unidade deste codebook"),
    ("Event Catalogs as Theories", 1, "A", "método: catálogo de eventos como teoria — é o que o codebook de 82 sub-eventos é"),
    ("Focusing on Focusing Events", 1, "A", "método: seleção de evento e viés de cobertura — a ressalva central do PEA, que este corpus enfrenta"),
    ("Strategies of Causal Inference in Small-N", 1, "B", "método: inferência em N pequeno; alternativa ao desenho adotado"),
    ("STRATEGIES OF CAUSAL ASSESSMENT IN COMPARATIVE HISTORICAL", 1, "B", "método: avaliação causal em análise histórica comparada"),
    ("The comparative sequential method", 1, "B", "método: sequência como evidência — útil para a ordenação T-1 / T0 / T+1"),
    ("ALIGNING ONTOLOGY AND METHODOLOGY", 1, "B", "método: coerência entre ontologia e desenho; antecipação de crítica"),
    ("Counterfactuals and Causal Inference", 1, "B", "método por contraste: o desenho NÃO é contrafactual de larga escala, e convém dizer por quê"),
    ("Process Tracing: a Bayesian Perspective", 1, "B", "método: leitura bayesiana do peso da evidência"),
    ("Understanding Bayesianism: Fundamentals for Process Tracers", 1, "B", "método: bayesianismo aplicado, em versão introdutória"),
    ("Updating Bayesian(s)", 1, "B", "método: crítica ao process tracing bayesiano — o outro lado do debate"),
    ("Mechanisms, Bayesianism, and process tracing", 1, "B", "método: mecanismo e bayesianismo, debate"),
    ("It's all about mechanisms", 1, "B", "método: o que um estudo de caso de process tracing deve demonstrar"),
    ("Explaining Social Processes", 1, "B", "método: explicação processual, formulação geral"),
    ("Mechanism-Based Causal Analysis", 1, "B", "método: verbete de enciclopédia sobre análise causal por mecanismo"),
    ("Causal Social Mechanisms; from the what to the why", 1, "B", "método: do que para o por quê, em mecanismo social"),
    ("Troubles with Mechanisms", 1, "B", "método: crítica ao 'giro mecanístico' — antecipação de crítica"),
    ("Single case studies and theory-testing", 1, "B", "método: caso único como teste de teoria"),
    ("=Comparative Process Tracing", 1, "B", "método: process tracing comparado, se o Capitólio entrar como caso"),
    ("=Mechanisms", 2, "A", "TARROW sobre mecanismo: o enunciado mais curto do vocabulário de Dynamics of Contention, e o mais próximo que este corpus chega dessa obra, que não está nele (duas versões, v1 e .pub2)"),

    # ------------------------------------------- ENQUADRAMENTO E OPORTUNIDADE (A)
    ("Framing Processes and Social Movements", 1, "A", "PT-07 e PT-50A: a referência canônica de enquadramento e alinhamento de quadros"),
    ("The Framing Perspective on Social Movements", 1, "A", "PT-07: balanço da perspectiva de enquadramento, posterior ao de 2000"),
    ("Linking Mobilization Frames and Political Opportunities", 1, "A", "PT-07 com PT-03D: quadro de mobilização acoplado à oportunidade política"),
    ("Protest logics and the mediation opportunity structure", 1, "A", "PT-50A: estrutura de oportunidade de mediação — o mecanismo da recaptura do enquadramento"),
    ("Transnational Discursive Opportunities", 1, "A", "PT-07 e PT-50A: oportunidade discursiva e quadro de risco; ficha 5 já conferida"),
    ("The Missing Link Between Structure and Agency", 1, "A", "PT-01 e PT-05A: o elo entre estrutura de oportunidade e ação; ficha 6 já conferida"),
    ("Opportunity Organizations and Threat", 1, "A", "PT-09 e PT-12: contenção induzida por ameaça e onda de protesto; ficha 4 já conferida"),
    ("Linking consensus to action", 1, "A", "PT-07: alinhamento de quadros entre simpatizantes e passagem à ação"),
    ("Discursive Opportunity Structure", 2, "B", "verbete de oportunidade discursiva (v1 de 2013 e .pub2 de 2022); ficha 7 já conferida"),
    ("=Master Frame", 2, "B", "verbete de quadro-mestre, que é o nível em que opera o frame anticorrupção de PT-03A"),
    ("=Frame alignment", 1, "B", "verbete de alinhamento de quadros, em enciclopédia de 2025"),
    ("Measuring collective action frames", 1, "B", "instrumento: medição linguística de quadros — útil se a criptolinguagem de PT-19 for codificada"),
    ("Analyzing frame analysis", 1, "B", "balanço crítico da análise de enquadramento; CONFERIR a autoria, que o CrossRef devolve como van Dijk"),
    ("Corn, Klansmen, and Coolidge", 1, "B", "enquadramento de movimento de direita radical, em chave estrutural"),
    ("Attention and counter-framing", 1, "B", "contra-enquadramento em plataforma — comparável à disputa narrativa de PT-50A"),
    ("Narrative and Frame Alignment in Social Movements", 1, "B", "narrativa e alinhamento de quadros"),
    ("FRAME-CONTRACTION", 1, "B", "contração de quadro — o movimento inverso do alinhamento"),
    ("Degrees of frame alignment: Comparing", 1, "B", "graus de alinhamento entre organizadores e participantes"),
    ("Opportunity Structures in the EU Multi-Level System", 1, "C", "oportunidade política em sistema multinível da UE, sem relação com o caso"),

    # ------------------------------------------------- REPERTÓRIO E DIFUSÃO (A)
    ("=Contentious Performances", 1, "A", "PT-01, PT-02, PT-12 e PT-33: a formulação de repertório de que o codebook se serve 20 vezes"),
    ("The Diffusion of Revolution", 1, "A", "PT-08: difusão e emulação entre países, com a América Latina no caso"),
    ("Networks, Diffusion, and Cycles of Collective Action", 1, "A", "PT-29 e PT-30: difusão em rede, contágio e ciclo"),
    ("Mechanisms of Maidan", 1, "A", "modelo do gênero: explicação por mecanismos de um único episódio contencioso, com contingência"),
    ("=Repertoires of Contention", 1, "B", "verbete de repertório de contenção"),
    ("Repertoires of Strategies", 1, "B", "verbete de repertório de estratégias"),
    ("Modular Protest Forms", 1, "B", "modularidade do repertório — o que permite a apropriação de PT-02"),
    ("Adding time to social movement diffusion", 1, "B", "temporalidade da difusão"),
    ("Protest Diffusion and Cultural Resonance", 1, "B", "difusão e ressonância cultural na onda de 2011"),
    ("Repertoires of Contention and Tactical Choice in Latin America", 1, "B", "repertório e escolha tática na América Latina, 1981-1995"),
    ("Repertoires of Contention across Latin America", 1, "B", "panorama de repertórios na América Latina"),
    ("The Spatial Diffusion of Rural Protest", 1, "C", "difusão espacial de protesto rural no século XIX; fora do escopo"),

    # --------------------------------- ESTRUTURAS DE MOBILIZAÇÃO E REDES (A/B)
    ("The Dynamics of Protest Recruitment through an Online Network", 1, "A", "PT-19 e PT-12A: recrutamento em rede online, com nós centralizadores"),
    ("Social Movement Organizations: Growth, Decay and Change", 1, "A", "PT-52: crescimento e decadência de organização — a destruição da infraestrutura de mobilização"),
    ("Anti-refugee Mobilization in Social Media", 1, "A", "PT-06: mobilização de extrema-direita em mídia social; 08_BIBLIOGRAFIA a listava como não verificada"),
    ("E-extremism", 1, "A", "PT-06: quadro conceitual para extrema-direita online, que é o ecossistema paralelo do registro"),
    ("Resource Mobilization: An Analysis of Conflicting", 1, "B", "mobilização de recursos, revisão das variantes teóricas"),
    ("Leadership and Membership in the Nuclear Freeze", 1, "B", "PT-12A: liderança e adesão como especificação da teoria de recursos"),
    ("The small-world network of global protests", 1, "B", "topologia de rede de protestos"),
    ("Anatomy of an urban mobilization network", 1, "B", "anatomia de rede de mobilização urbana"),
    ("Scaling Social Movements Through Social Media", 1, "B", "escala por mídia social, caso BLM"),
    ("Social media and social movements: Facebook", 1, "B", "mídia social e mobilização, caso guatemalteco"),
    ("Digitally Mediated Protest", 1, "B", "protesto mediado digitalmente e identidade coletiva"),
    ("The contentious sovereignties of the camp", 1, "B", "PT-12 e PT-21: o acampamento como forma territorial de contenção, não só como protesto"),
    ("Social Movement Organziations: Classic Views", 1, "B", "balanço sobre organizações de movimento"),
    ("A theoretical framework for comparisons of social movement participation", 1, "B", "participação em movimento, quadro comparativo"),
    ("Beyond Structural Analysis", 1, "B", "para além da análise estrutural: relação e processo em movimentos"),

    # ---------------------------- POLICING, REPRESSÃO E DEFECÇÃO DO AGENTE (A)
    ("The Impacts of Repression", 1, "A", "PT-27, PT-31 e PT-32: presença e ação policial como variável do desfecho do protesto"),
    ("Subnational State Capacity and the Repression of Protest", 1, "A", "PT-28: capacidade estatal subnacional e dispositivo — o subdimensionamento do DF"),
    ("DETERRENCE OR DEFIANCE", 1, "A", "PT-53 e PT-61: severidade e seletividade da repressão, que é exatamente a repressão escalonada por núcleos"),
    ("THE UNINTENDED CONSEQUENCES OF ESCALATED REPRESSION", 1, "A", "PT-53 e PT-62: consequências não pretendidas da repressão escalada — o deslocamento da contestação"),
    ("The Repression-Dissent Nexus in High-Threat", 1, "B", "nexo repressão-dissidência em ambiente de alta ameaça"),
    ("When Does Repression Trigger Mass Protest", 1, "B", "repressão como gatilho, caso Gezi"),
    ("The Gezi Park Protests and the Escalation", 1, "B", "PT-15 e PT-39: escalada e desescalada de confronto num episódio único"),
    ("Movement escalation and mobilization for resistance", 1, "B", "escalada de movimento em contexto de golpe"),
    ("How to Measure Dictatorship, Dissent, and Political Repression", 1, "B", "mensuração de repressão; instrumento, não teoria"),
    ("Participação arriscada", 1, "B", "participação de alto risco em regime ditatorial; publicado em português na Dados"),
    ("Mathematical model of repressive response", 1, "C", "modelo matemático de resposta repressiva; formalização fora do desenho"),
    ("Coercion and revolution", 1, "C", "modelo predador-presa de coerção; formalização fora do desenho"),

    # ------------------------------------- CICLO, ONDA E DESMOBILIZAÇÃO (A/B)
    ("The Sequencing of Social Movements", 1, "B", "sequenciamento de movimentos — a ordenação que o codebook faz em três tempos"),
    ("When Waves Collide", 1, "B", "PT-62: colisão de ondas e ciclo de protesto"),
    ("Master Frames, Cycles of Protest", 1, "B", "quadro-mestre e ciclo de protesto"),
    ("Protest Wave or Protest Spike", 1, "B", "onda ou pico: a distinção importa para classificar o 8/1"),
    ("Protest Waves in Latin America", 1, "B", "ondas de protesto na América Latina"),
    ("Was it Worth the Effort", 1, "B", "resultados e consequências de movimentos — a pergunta do T+1"),

    # --------------------- CONTESTAÇÃO DE RESULTADO ELEITORAL E O CAPITÓLIO (A)
    ("January 6th and De-Democratization", 1, "A", "PT-08: o caso de que o 8/1 é emulação, lido como episódio de desdemocratização"),
    ("Comparing the #StopTheSteal Movement", 1, "A", "PT-08 e PT-19: a mobilização do 6/1 por plataforma — o modelo que circulou"),
    ("Competitive authoritarianism and popular protest", 1, "B", "autoritarismo competitivo e protesto; comparação de regime"),
    ("Toward a Fourth Generation of Revolutionary Theory", 1, "B", "teoria da revolução, quarta geração; enquadra o caso na literatura maior"),
    ("Sources of Rebellion in Western Societies", 1, "B", "fontes de rebelião, formulação clássica de 1970"),
    ("Violence during democratization", 1, "C", "violência e qualidade institucional em painel de países; desenho incompatível"),
    ("=Democracy", 1, "B", "PT-50 e PT-06B: democratização e descertificação, na formulação de Tilly"),

    # ------- PROMOVIDOS PELA VARREDURA DE FALSO-NEGATIVO EM C (29/09/2026)
    # A camada C foi varrida por termo forte do codebook. Seis itens têm termo
    # no título; três mereciam B, e estão aqui. Os outros três ficaram em C com
    # razão: motim colonial do século XIX, difusão de protesto rural, e
    # governança de inteligência criminal em Ontário.
    ("anti-coup protests", 1, "B", "PT-12 e PT-33: mistura de repertório antigo e novo, em contexto de golpe"),
    ("Ukrainian radical right mobilized", 1, "B", "PT-06: mobilização territorial da direita radical"),
    ("Leninist beneficiaries", 1, "B", "PT-06: legado e direita radical em contexto comparado"),

    # ------------------------------------------------------------ FORA (C)
    ("Immigration and Categorical Inequality", 1, "C", "desigualdade categórica e migração; é o DOI de livro que duas entradas da síntese compartilham"),
    ("How to use corpus linguistics in the study of media discourse", 1, "C", "linguística de corpus para discurso midiático; o par trocado de 22.3, sem uso no argumento"),
    ("Basics of Bayesian Methods", 1, "C", "bayesianismo em biologia molecular — a medida do ruído que as sínteses arrastam"),
    ("the propensity score", 1, "C", "escore de propensão em estudo observacional; tradição contrafactual de N grande"),
    ("Estimating causal effects of treatments", 1, "C", "efeitos de tratamento; tradição contrafactual de N grande"),
    ("Birds of a Feather", 1, "C", "homofilia em redes sociais; teoria de rede sem vínculo com o argumento"),
    ("Does War Make States?", 1, "C", "paradigma bellicista de formação do Estado; o codebook não afirma mecanismo de state-building"),
    ("=War and State Formation", 1, "C", "formação do Estado pela guerra; mesma razão"),
    ("Integration of landslide hazard", 1, "C", "risco de deslizamento em planejamento urbano; ruído da síntese"),
    ("Global surgical care", 1, "C", "cirurgia global — a colisão de homônimos com Derek Beach, já registrada na ficha de 01/09"),
]


def carregar():
    with CSV_IN.open(encoding="utf-8-sig", newline="") as fh:
        return [r for r in csv.DictReader(fh)]


def resolver(rows):
    """Casa cada fragmento com os títulos verificados. Aborta se o número divergir."""
    decidido = {}
    for frag, quantos, camada, uso in TRIAGEM:
        exato = frag.startswith("=")          # título curto que é subcadeia de outros
        alvo = frag[1:].lower() if exato else frag.lower()
        achados = [r for r in rows if r["situacao"].startswith("CONFIRMADO")
                   and (r["titulo"].lower() == alvo if exato else alvo in r["titulo"].lower())]
        assert len(achados) == quantos, (
            "fragmento {!r}: esperava {} correspondência(s), achei {} — {}".format(
                frag, quantos, len(achados), [a["titulo"][:50] for a in achados]))
        for r in achados:
            anterior = decidido.get(r["doi"])
            assert anterior is None or anterior[0] == camada, (
                "{} classificado duas vezes, em camadas diferentes: {} e {}".format(
                    r["doi"], anterior[0] if anterior else "?", camada))
            decidido[r["doi"]] = (camada, uso)
    return decidido


def main():
    rows = carregar()
    decidido = resolver(rows)

    COLS = ["camada", "uso", "origem", "doi", "ano", "titulo", "veiculo", "autores",
            "citado_por", "eixos", "sinteses", "situacao"]
    ordem = {"A": 0, "B": 1, "C": 2}
    saida = []
    for r in rows:
        camada, uso = decidido.get(r["doi"], ("C", ""))
        if not uso and camada == "C":
            uso = {"": "sem termo do referencial no título nem nos assuntos"}.get(
                r["eixos"], "tema do campo, sem vínculo com mecanismo afirmado no codebook")
        if not r["situacao"].startswith("CONFIRMADO"):
            camada, uso = "—", "DOI inexistente; ver NAO_EXISTEM em verificar_dois_sinteses.py"
        saida.append(dict(r, camada=camada, uso=uso, origem="DOI impresso na síntese"))

    cache = {reg["doi"]: reg for reg in (json.loads(l) for l in
             CACHE.read_text(encoding="utf-8").splitlines() if l.strip())}
    for doi, (camada, uso) in RECUPERADOS.items():
        reg = cache.get(doi)
        assert reg and reg["situacao"].startswith("CONFIRMADO"), (
            "{} nao esta confirmado no cache - rode verificar_dois_sinteses.py".format(doi))
        reg = {k: ("" if v is None else str(v)) for k, v in reg.items()}   # o cache traz int
        saida.append(dict(reg, camada=camada, uso=uso, eixos="", sinteses="",
                          origem="sem DOI na síntese; achado por busca de título"))
    saida.sort(key=lambda r: (ordem.get(r["camada"], 3), -int(r["citado_por"] or 0)))

    CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
    with CSV_OUT.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS, extrasaction="ignore")
        w.writeheader()
        for r in saida:
            w.writerow(r)

    conta = {}
    for r in saida:
        conta[r["camada"]] = conta.get(r["camada"], 0) + 1
    print("TRIAGEM POR PERTINÊNCIA — {} DOIs ({} impressos + {} recuperados)".format(
        len(saida), len(rows), len(RECUPERADOS)))
    print("=" * 78)
    for c in ("A", "B", "C", "—"):
        if c in conta:
            print("  camada {:<2} {:>3}".format(c, conta[c]))
    print("=" * 78)
    for r in saida:
        if r["camada"] == "A":
            print("  {} | {} | {}".format(r["ano"][:4], r["titulo"][:62], r["uso"][:60]))
    print("\nplanilha: {}".format(CSV_OUT.relative_to(RAIZ)))
    print("Nada da camada A é citável antes do passo 3 — a leitura na fonte.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
