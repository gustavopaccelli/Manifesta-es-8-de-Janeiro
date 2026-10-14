#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tarefa 14 — codificar a camada T-1 conjuntural sobre literatura lida na fonte.

Os sete registros contextuais (PT-01 a PT-06 e PT-08) foram escritos em 08/2026
apoiados em uma lista de nomes — "Literatura: Alonso (2017); Tatagiba (2014)" —
sem que nenhuma dessas obras estivesse no corpus ou tivesse sido lida. Este
script substitui a lista de nomes por ancoragem com página, onde a leitura na
fonte existe, e **declara a lacuna onde ela não existe**.

O QUE ENTROU NO CORPUS, e de onde. Quatro artigos da pasta de textos de ação
coletiva anexada à sessão, copiados para `Fontes/12_Camada-T-1_Literatura/`:

  TATAGIBA 2014       1984, 1992 e 2013. Sobre ciclos de protestos e democracia
                      no Brasil. Política & Sociedade, 13(28):35-62.  28 p.
                      **SEM CAMADA DE TEXTO** — lido por renderização.
  TATAGIBA E GALVAO   Os protestos no Brasil em tempos de crise (2011-2016).
          2019        Opinião Pública, 25(1):63-96.  34 p.
  PINTO 2017          A trajetória discursiva das manifestações de rua no
                      Brasil (2013-2015). Lua Nova, 100:119-153.  37 p.
  ALONSO 2012         Repertório, segundo Charles Tilly: história de um
                      conceito. Sociologia & Antropologia, 2(3):21-41.  21 p.

PÁGINA DO PDF, NÃO DA REVISTA. `fonte_pagina` é lido por `conferir_paginas.py`
como índice de página do PDF, e nestes quatro a numeração da revista não
coincide com a do arquivo. O campo guarda a página do PDF; `fonte_trecho` traz
a da revista entre parênteses, que é a citável. Os deslocamentos estão
declarados em PROCEDENCIA, em gerar_codebook.py.

TRÊS ACHADOS QUE A LEITURA PRODUZIU, e que mudam registro:

  1. **PT-01 atribuía ao ator o enquadramento do adversário.** O campo dizia
     «'Não é só por 20 centavos' — antipolítica». Tatagiba (2014, p. 40)
     sustenta o contrário — "desde o começo, foi sim uma luta por 0,20
     centavos" — e Pinto (2017, p. 131) traz a militante do MPL dizendo que
     "interessava para vários setores dizer que a luta não era somente pelos
     R$ 0,20. [...] Para nós do movimento, era, sim, pelos R$ 0,20". A leitura
     ampliada não era o quadro do MPL: era o quadro que terceiros, de direita e
     de esquerda, lhe impuseram. É a quarta variante do modo de falha do
     projeto — depois da cifra, do termo técnico e da frase própria, **o
     enquadramento do adversário posto na boca do ator**.

  2. **A obra citada nos dois registros nunca esteve no corpus.** "Alonso
     (2017)" não está na pasta nem foi lida. O que há é ALONSO (2012), outro
     texto — história do conceito de repertório —, e ele cobra do codebook algo
     diferente: "Tilly não detalha o processo de apropriação do repertório pelos
     atores" (p. 24). O mecanismo que PT-02 chama de apropriação não tem, na
     fonte do conceito, o detalhamento que o nome sugere. Decisão de nome é da
     tarefa 19.

  3. **A intervenção militar já estava nas ruas em março de 2015.** Pinto
     (2017, p. 150) documenta faixas pedindo intervenção militar e o movimento
     "SOS Forças Armadas", que "atualizava o espaço político das Forças
     Armadas". É o mesmo apelo que o codebook trata em T-1 operacional (PT-12),
     oito anos antes. Fica registrado em PT-02; se vira registro próprio, é
     decisão sua.

O QUE NÃO FOI CODIFICADO, E POR QUÊ. PT-04 (2018), PT-05 (2019-2022), PT-06
(2020-2021) e PT-08 (Capitólio) seguem **Contextual**. A varredura de conteúdo
nos 145 arquivos da pasta anexada devolveu **zero ocorrências de "Bolsonaro"**,
zero de "pandemia" e nenhuma ocorrência de "Capitol" posterior a 2021 — todas
as que há são de obras anteriores, sobre história norte-americana. A literatura
desses quatro registros (Cesarino, Campos Mello, Abranches, Avritzer, Levitsky &
Ziblatt, Norris & Inglehart) não está em lugar algum ao alcance. O status deixa
de dizer "requer fonte primária" e passa a dizer o que foi varrido e não achado.

Uso:  python scripts/recodificar_camada_t1.py [--dry-run]
"""
import io
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

BASE = "Fontes/12_Camada-T-1_Literatura/"
DOCS = {
    "TATAGIBA 2014":
        BASE + "TATAGIBA_Ciclos-de-protestos-e-democracia_Politica-e-Sociedade-28_2014.pdf",
    "TATAGIBA E GALVAO 2019":
        BASE + "TATAGIBA-GALVAO_Protestos-no-Brasil-em-tempos-de-crise_Opiniao-Publica-25-1_2019.pdf",
    "PINTO 2017":
        BASE + "PINTO_Trajetoria-discursiva-das-manifestacoes-de-rua_Lua-Nova-100_2017.pdf",
    "ALONSO 2012":
        BASE + "ALONSO_Repertorio-segundo-Charles-Tilly_Sociologia-e-Antropologia-2-3_2012.pdf",
}

# Varredura de 04/10/2026 na pasta anexada à sessão: 145 arquivos, busca de
# conteúdo com normalização NFKC. O texto abaixo entra nos registros que
# continuam contextuais, para que a lacuna seja datada e reproduzível.
VARREDURA = ("Contextual — varredura de conteúdo em 04/10/2026 nos 145 arquivos da pasta "
             "de textos de ação coletiva não localizou literatura sobre o período: zero "
             "ocorrências de 'Bolsonaro', zero de 'pandemia', e as de 'Capitol' são todas "
             "de obras anteriores a 2021, sobre história norte-americana. As obras citadas "
             "não estão no corpus e não foram lidas.")

MUDANCAS = {

    # ------------------------------------------------------------------ PT-01
    "PT-01": {
        "framing_narrativa":
            "Sem quadro unificador — a literatura lida registra que nenhum enquadramento "
            "deu unidade à diversidade para além do estopim tarifário. O que se documenta "
            "é antipartidarismo, com hostilidade inédita a partidos e militantes nos atos; "
            "e a leitura ampliada dos 20 centavos é atribuída pelo próprio MPL a terceiros, "
            "de direita e de esquerda, não ao movimento",
        "fonte_trecho":
            "TATAGIBA (2014, p. 36, 38, 40, 47) e PINTO (2017, p. 128-131); séries de "
            "protesto em TATAGIBA E GALVÃO (2019, p. 70-74). Sobre a resposta estatal: "
            "“foram nacionalizados a partir da forte repressão policial contra os "
            "manifestantes na cidade de São Paulo. Os protestos provocaram redução das "
            "tarifas em várias cidades” (Tatagiba, 2014, p. 36). Sobre o quadro: "
            "“não houve a conformação de um frame capaz de conferir unidade a essa "
            "diversidade para além do estopim: contra o aumento da tarifa do transporte "
            "público” (p. 40). Sobre os 20 centavos, a militante do MPL Nina Cappello: "
            "“Interessava para vários setores dizer que a luta não era somente pelos "
            "R$ 0,20. Colocam um monte de coisas no mesmo saco e não se conquista nada. "
            "Para nós do movimento, era, sim, pelos R$ 0,20” (Pinto, 2017, p. 131). "
            "Sobre a oportunidade: “Junho de 2013 representa o ápice desse processo e "
            "constitui uma extraordinária oportunidade para os setores oposicionistas, à "
            "esquerda e à direita do espectro político, expressarem seu descontentamento "
            "com as políticas do governo” (Tatagiba e Galvão, 2019, p. 74). Sobre o "
            "ator: “Grupos autonomistas, que defendem a horizontalidade contra a "
            "hierarquia de partidos e sindicatos, emergem especialmente nesse segmento, "
            "como o Movimento Passe Livre (MPL), que deflagrou as Jornadas de 2013” "
            "(p. 72).",
        "fonte_local": "; ".join([DOCS["TATAGIBA 2014"], DOCS["PINTO 2017"],
                                  DOCS["TATAGIBA E GALVAO 2019"]]),
        # páginas do PDF: Tatagiba 2014 = revista - 34; Pinto = revista - 118;
        # Tatagiba e Galvão = revista - 62
        "fonte_pagina": "TATAGIBA 2014: 2, 4, 6, 13 | PINTO 2017: 10, 11, 12, 13 | "
                        "TATAGIBA E GALVAO 2019: 8, 10, 12",
        "status_verificacao":
            "Confirmado em literatura revisada por pares, lida na fonte com página. Não há "
            "fonte primária de 2013 no corpus, e o registro não a reivindica.",
        "status_classe": "Confirmado",
        "nota_auditoria":
            "recodificado em 04/10/2026, tarefa 14 — o campo framing_narrativa dizia "
            "“'Não é só por 20 centavos' — antipolítica”. As duas obras lidas "
            "contradizem a atribuição: Tatagiba (2014, p. 40) afirma que “desde o "
            "começo, foi sim uma luta por 0,20 centavos” e que nenhum frame unificou o "
            "ciclo; Pinto (2017, p. 131) mostra a leitura ampliada como quadro imposto ao "
            "MPL por terceiros. “Antipolítica” também muda de referente: em Pinto "
            "(p. 131) o discurso antipolítico é o que emerge DEPOIS da retirada do MPL e "
            "está “claramente à direita”. O termo documentado para 2013 é "
            "antipartidarismo (Tatagiba, 2014, p. 47; Pinto, 2017, p. 149). Quarta variante "
            "do modo de falha do projeto: o enquadramento do adversário atribuído ao ator. "
            "Alonso (2017), citada no campo anterior, nunca esteve no corpus nem foi lida.",
    },

    # ------------------------------------------------------------------ PT-02
    "PT-02": {
        "fonte_trecho":
            "PINTO (2017, p. 143-152) e TATAGIBA E GALVÃO (2019, p. 81-82). Sobre o marco "
            "inicial: a vaia à presidenta na abertura da Copa, em 12/06/2014, “foi o "
            "momento inaugural do discurso conservador, fundamentalmente antipetista, que "
            "tomou fôlego a partir de então, dando sentido às manifestações por seu "
            "impeachment em março de 2015” (Pinto, 2017, p. 143). Sobre a base social: "
            "“esse discurso com apelo popular não foi levado a efeito pelas classes "
            "populares indignadas, mas por setores da alta classe média” (p. 144). "
            "Sobre o deslocamento do quadro: “Se, em 2013, poderia ser identificado um "
            "antipartidarismo, mesmo em grupos identificados com posições à esquerda, como "
            "o Movimento Passe Livre, que se declarava antipartidário, em 2015 o cenário "
            "foi distinto, centralizando-se no discurso anti-PT” (p. 149). Sobre os "
            "convocantes: “A convocação dos protestos foi assumida por organizações "
            "como o MBL, Vem Pra Rua, Revoltados Online, Nas Ruas, Movimento Contra a "
            "Corrupção, entre outras organizações menores, a partir de um forte uso das "
            "redes sociais” (Tatagiba e Galvão, 2019, p. 82) — e, no mesmo parágrafo, "
            "a ressalva de que “os grupos antipetistas já estão presentes em protestos "
            "organizados em 2011, mantendo a mesma estética e slogans”. ACHADO QUE O "
            "CODEBOOK NÃO REGISTRA: já em março de 2015 havia “faixas pedindo "
            "intervenção militar”, algumas em inglês, e um movimento “SOS Forças "
            "Armadas” que, pouco expressivo em número, “atualizava o espaço "
            "político das Forças Armadas” (Pinto, 2017, p. 150).",
        "fonte_local": "; ".join([DOCS["PINTO 2017"], DOCS["TATAGIBA E GALVAO 2019"],
                                  DOCS["ALONSO 2012"]]),
        "fonte_pagina": "PINTO 2017: 25, 26, 31, 32, 34 | TATAGIBA E GALVAO 2019: 9, 19, 20 | "
                        "ALONSO 2012: 4, 10",
        "status_verificacao":
            "Confirmado em literatura revisada por pares, lida na fonte com página. Uma "
            "afirmação do registro segue sem âncora: “tolerância policial” não foi "
            "localizada em nenhuma das obras lidas. O enquadramento midiático favorável está "
            "em Pinto (2017, p. 130, nota 11).",
        "status_classe": "Confirmado",
        "nota_auditoria":
            "recodificado em 04/10/2026, tarefa 14 — atores, repertório e enquadramento "
            "passam a ter página. Três ressalvas que a leitura impõe e que o registro não "
            "resolve sozinho: (1) Tatagiba e Galvão (2019, p. 71, 91) sustentam que “não "
            "observamos uma descontinuidade entre 2013 e os protestos posteriores”, o "
            "que enfraquece a leitura de spin-off como ruptura e a converte em difusão "
            "dentro de um mesmo ciclo; (2) os grupos antipetistas já protestavam em 2011 "
            "(p. 82), de modo que a apropriação do repertório é de escala, não de origem; "
            "(3) Alonso (2012, p. 24) registra que “Tilly não detalha o processo de "
            "apropriação do repertório pelos atores” — o nome do mecanismo não tem, na "
            "fonte do conceito, o conteúdo que sugere. O nome é decisão da tarefa 19. "
            "“Tolerância policial” permanece sem âncora.",
    },

    # ------------------------------------------------------------------ PT-03
    "PT-03": {
        "fonte_trecho":
            "TATAGIBA E GALVÃO (2019, p. 65, 69, 91). A data: o banco cobre até "
            "“31/8/2016, quando ela é definitivamente afastada pelo Senado” "
            "(p. 69). A cadeia: “o pico das mobilizações em 2013 cria oportunidades "
            "políticas inéditas para os setores oposicionistas, à direita e à esquerda do "
            "PT, conformando um cenário de crise política que, associado à crise econômica, "
            "abre caminho para o impeachment” (p. 91). As autoras tratam 2016 como o "
            "“ano do golpe jurídico-parlamentar que levou à sua destituição e "
            "substituição por seu vice, Michel Temer” (p. 65) — caracterização delas, "
            "oposta à do campo pró-impeachment que o registro codifica.",
        "fonte_local": DOCS["TATAGIBA E GALVAO 2019"],
        "fonte_pagina": "TATAGIBA E GALVAO 2019: 3, 7, 29",
        "status_verificacao":
            "Confirmado quanto à data e ao encadeamento com o ciclo de protestos, em "
            "literatura revisada por pares lida na fonte. O enquadramento "
            "“legalidade constitucional” é o do campo pró-impeachment e não foi "
            "localizado nas obras lidas, que adotam a caracterização oposta.",
        "status_classe": "Confirmado",
        "nota_auditoria":
            "recodificado em 04/10/2026, tarefa 14. O rótulo do mecanismo continua pendente "
            "desde 30/09: “certificação de eficácia” não satisfaz a definição de "
            "Dynamics of Contention, que exige validação por autoridade externa, e o "
            "enunciado não nomeia autoridade alguma (agenda, item 24.6). A leitura desta "
            "rodada não resolve — reforça, porque a literatura lida descreve o impeachment "
            "como desfecho de uma crise política, não como validação de uma via. Decisão da "
            "tarefa 19. O campo framing_narrativa foi mantido, porque codifica o quadro do "
            "ator e não a avaliação da literatura; a divergência fica declarada no status.",
    },

    # --------------------------------------------------- PT-04, PT-05, PT-06
    "PT-04": {
        "fonte_trecho":
            "Literatura declarada no registro original — Campos Mello (2020); Cesarino "
            "(2022) — NÃO ESTÁ NO CORPUS e não foi lida. Item contextual.",
        "status_verificacao": VARREDURA,
        "nota_auditoria":
            "revisado em 04/10/2026, tarefa 14 — permanece contextual. A pasta de literatura "
            "anexada à sessão cobre densamente o ciclo 2013-2016 e não cobre o período "
            "2018-2022: é a mesma lacuna que a triagem de 29/09 encontrou nos 411 DOIs das "
            "sínteses (agenda, item 23.2), agora confirmada por varredura de conteúdo numa "
            "segunda coleção independente.",
    },
    "PT-05": {
        "fonte_trecho":
            "Literatura declarada no registro original — Abranches; Avritzer — NÃO ESTÁ NO "
            "CORPUS e não foi lida. Item contextual.",
        "status_verificacao": VARREDURA,
        "nota_auditoria":
            "revisado em 04/10/2026, tarefa 14 — permanece contextual, pela mesma varredura "
            "que fechou PT-04. Observação de ancoragem, não de leitura: o atrito "
            "institucional de 2019-2022 que este registro descreve tem, no próprio codebook, "
            "registros vizinhos já ancorados em fonte primária (PT-05A, PT-06A a PT-06C, do "
            "arco judicial). O que falta aqui é a literatura que interpreta o período, não a "
            "documentação dele.",
    },
    "PT-06": {
        "fonte_trecho":
            "Literatura declarada no registro original — Cesarino (2022) — NÃO ESTÁ NO "
            "CORPUS e não foi lida. Item contextual.",
        "status_verificacao": VARREDURA,
        "nota_auditoria":
            "revisado em 04/10/2026, tarefa 14 — permanece contextual, pela mesma varredura "
            "que fechou PT-04. É o registro de maior custo entre os quatro: o mecanismo que "
            "ele afirma — consolidação do ecossistema informacional paralelo — é o que liga "
            "T-1 conjuntural a T-1 operacional, e segue sem leitura.",
    },

    # ------------------------------------------------------------------ PT-08
    "PT-08": {
        "status_verificacao":
            "Contextual quanto ao evento; o modelo efetivamente invocado pelos organizadores "
            "está confirmado em fonte primária — CPMI, p. 614 (ver PT-19). A varredura de "
            "conteúdo de 04/10/2026 nos 145 arquivos da pasta anexada não localizou "
            "literatura sobre 6 de janeiro de 2021: todas as ocorrências de 'Capitol' são de "
            "obras anteriores a 2021, sobre história norte-americana. Levitsky & Ziblatt e "
            "Norris & Inglehart não estão no corpus e não foram lidos.",
        "nota_auditoria":
            "vínculo corrigido em 16/08/2026 — O achado do Sri Lanka como precedente "
            "invocado está na CPMI p. 614 e é citado na tabela do relatório, mas fonte_local "
            "estava vazio. | revisado em 04/10/2026, tarefa 14 — a comparação com o "
            "Capitólio continua sem literatura comparada lida na fonte, e a ressalva do "
            "registro (Sri Lanka, não Capitólio) continua sendo o que o projeto tem de "
            "próprio aqui.",
    },
}


def main():
    seco = "--dry-run" in sys.argv
    with io.open(JSON_P, encoding="utf-8") as f:
        dados = json.load(f)

    por_id = {e["id"]: e for e in dados["eventos"]}
    for rid in MUDANCAS:
        assert rid in por_id, "registro inexistente: {}".format(rid)

    n_campos = 0
    for rid, campos in sorted(MUDANCAS.items()):
        ev = por_id[rid]
        print("\n{}  ({})".format(rid, ev.get("data_hora")))
        for campo, novo in sorted(campos.items()):
            velho = ev.get(campo)
            if velho == novo:
                print("   = {} (sem mudanca)".format(campo))
                continue
            print("   - {}: {}".format(campo, (velho or "")[:88]))
            print("   + {}: {}".format(campo, novo[:88]))
            if not seco:
                ev[campo] = novo
            n_campos += 1

    # Os quatro artigos entram no registro de documentos, sem o qual a checagem 5
    # de verificar_integridade.py acusa pagina citada fora de documento vinculado.
    reg = dados["metadados"].setdefault("registro_documentos", {})
    for cod, caminho in sorted(DOCS.items()):
        if reg.get(cod) != caminho:
            print("\nregistro_documentos += {}".format(cod))
            if not seco:
                reg[cod] = caminho
            n_campos += 1

    nota = ("2026-10-04 (tarefa 14) — camada T-1 conjuntural codificada sobre literatura "
            "lida na fonte. Entram no corpus quatro artigos revisados por pares, em "
            "Fontes/12_Camada-T-1_Literatura/: Tatagiba (2014), Tatagiba e Galvão (2019), "
            "Pinto (2017) e Alonso (2012). PT-01, PT-02 e PT-03 passam de Contextual a "
            "Confirmado, com página. PT-04, PT-05, PT-06 e PT-08 permanecem contextuais, "
            "agora com a lacuna datada e a varredura declarada. Três achados: o "
            "enquadramento de PT-01 era o do adversário, não o do ator; Alonso (2017), "
            "citada em dois registros, nunca esteve no corpus; e o apelo à intervenção "
            "militar está documentado nas ruas em março de 2015, oito anos antes de PT-12. "
            "Contagem de contextuais: 7 -> 4.")
    if nota not in dados["metadados"].get("revisoes", []):
        print("\nrevisoes += nota da rodada")
        if not seco:
            dados["metadados"].setdefault("revisoes", []).append(nota)
        n_campos += 1

    print("\n{} alteracao(oes){}".format(
        n_campos, " — DRY RUN, nada gravado" if seco else ""))
    if not seco and n_campos:
        # newline="\n" é obrigatório: o .gitattributes do projeto traz `* -text`,
        # isto é, nenhuma conversão. Sem isso, o Python no Windows grava CRLF e o
        # git mostra as 1.600 linhas do codebook como alteradas — diferença
        # fantasma que esconde as 30 linhas que de fato mudaram.
        with io.open(JSON_P, "w", encoding="utf-8", newline="\n") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print("gravado em {}".format(JSON_P.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
