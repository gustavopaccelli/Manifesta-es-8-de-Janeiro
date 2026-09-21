#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Resolução do Manchetômetro: VIRA REGISTRO — PT-50A.

Rodada de 16/08/2026. O relatório do Doxa/IESP-UERJ estava no corpus desde a
auditoria sem vínculo com registro nenhum, como último órfão declarado.

DECISÃO: vira registro. Três razões.

  1. TEM ACHADO DATÁVEL QUE O CODEBOOK NÃO COBRE. O relatório documenta a
     emergência da narrativa dos "infiltrados da esquerda" às 17h40 do dia 8 e
     sua consolidação em 9-10/01. O codebook não tem NADA sobre a contraofensiva
     discursiva imediata — PT-50 cobre só a nota de Bolsonaro, e PT-62 é
     inferência sobre o longo prazo.

  2. HÁ PRECEDENTE DIRETO. PT-19A entrou no codebook a partir do NetLab, também
     relatório de laboratório universitário não revisado por pares, com as
     ressalvas declaradas. O Manchetômetro é a peça companheira: PT-19 cobre a
     circulação orgânica no WhatsApp, PT-19A a paga na Meta, e faltava a
     orgânica pública no Facebook.

  3. ANCORA EMPIRICAMENTE O PRIMEIRO PASSO DE PT-62. A inferência sobre migração
     da contestação para outras arenas era leitura do analista sem lastro. A
     recaptura do enquadramento em 48 horas é o primeiro elo observável dela.

CONTRA-ARGUMENTO CONSIDERADO E REJEITADO: o projeto decidiu tratar cobertura de
imprensa como OBJETO de análise (eixo 08), não fonte de evento. Mas o
Manchetômetro não é análise de enquadramento jornalístico — é medição
quantitativa de circulação em plataforma, da mesma natureza do NetLab. A
distinção que vale é entre medir circulação (fonte) e interpretar cobertura
(objeto), não entre acadêmico e jornalístico.

POSIÇÃO NA CRONOLOGIA: PT-50A entra depois de PT-50 por afinidade temática — os
dois são T+1 Enquadramento. Registre-se a sobreposição: a emergência às 17h40
PRECEDE a nota de Bolsonaro das 21h17 (PT-50), mas a consolidação do fenômeno é
posterior. Está declarado no próprio registro.

Uso:  python scripts/inserir_pt50a.py [--dry-run]
"""

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"
MANCH = "Fontes/07_NetLab-UFRJ/Doxa-IESP-UERJ_Manchetometro_Atos-golpistas-8-jan_2023-03.pdf"

PT50A = {
    "id": "PT-50A",
    "data_hora": "08/01/2023, a partir das 17h40 — 10/01/2023",
    "fase": "T+1 Enquadramento",

    "ator_grupo":
        "Segmento bolsonarista em páginas do Facebook — políticos (Capitão Contar, cel. "
        "Aginaldo, Carla Zambelli), influenciadores e mídia alinhada (Jornal da Cidade Online, "
        "Jovem Pan News)",

    "repertorio_acao":
        "Contraofensiva narrativa em rede: atribuição dos atos a 'infiltrados da esquerda' e, "
        "em seguida, deslocamento do debate de 'quem foi responsável' para 'o governo sabia'",

    "target_alvo":
        "A atribuição pública de responsabilidade pelos atos; o enquadramento dominante nas "
        "redes",

    "framing_narrativa":
        "'Infiltrados da esquerda' e black blocs, sobre o argumento de que 'manifestações da "
        "direita teriam sido sempre pacíficas'; e 'o governo sabia' — a partir da notícia dos "
        "alertas da Abin, usada para sugerir complacência deliberada do governo para "
        "criminalizar a direita",

    "resposta_estatal":
        "Nenhuma no plano discursivo. A resposta estatal foi judicial (PT-53) e policial "
        "(PT-52), não comunicacional",

    "mecanismo_causal":
        "RECAPTURA DO ENQUADRAMENTO. Derrotado na rua e também na disputa narrativa do próprio "
        "dia 8 — quando, nos termos do relatório, 'a esquerda e o governo dominaram a narrativa "
        "nas redes' e a acusação de infiltrados saiu 'ainda sem sucesso' —, o campo bolsonarista "
        "reconstrói o debate em seus próprios termos em cerca de 48 horas, deslocando a pergunta "
        "de quem foi responsável para se o governo sabia. É desmobilização de rua COM preservação "
        "da capacidade discursiva: o repertório de ocupação se encerra materialmente com a "
        "desocupação do acampamento (PT-52), mas a infraestrutura de circulação permanece intacta "
        "e opera de imediato em modo defensivo. Note-se a inversão de sinal no próprio dia 8: o "
        "campo suprime as transmissões ao vivo que até a véspera serviam de convocação para o QG "
        "e passa a acusar; no dia 9 volta a produzir os posts de maior engajamento do período. "
        "IMPORTÂNCIA PARA O ARGUMENTO: este é o primeiro elo OBSERVÁVEL da inferência de PT-62 — "
        "migração da contestação da rua para outras arenas —, que até aqui era leitura do "
        "analista sem lastro empírico. Não a converte em achado, mas lhe dá um ponto de partida "
        "datado.",

    "fonte_trecho":
        "Manchetômetro / Doxa-IESP-UERJ, 'Os atos golpistas de 8 de janeiro de 2023 — relatório "
        "temático' (mar/2023, 16 p.). Corpus: publicações de páginas do Facebook coletadas por "
        "termos na plataforma CrowdTangle entre 6 e 10 de janeiro de 2023 (p. 2). Escala, p. 3 e 4: "
        "314 tipos de página na amostra, cujos 20 maiores produziram 56.679 publicações (86,5% do total) e 13,3 "
        "milhões de interações (90,2% do total); 1.155 lives no período. "
        "EMERGÊNCIA DA NARRATIVA, p. 10: os atos são atribuídos a 'infiltrados da esquerda' — "
        "'narrativa que já aparece na rede no final da tarde, a partir das 17:40' do dia 8. "
        "CONSOLIDAÇÃO, p. 14: 'o segmento bolsonarista na rede continuou no esforço de afirmar "
        "que as ações teriam sido realizadas por grupos infiltrados da esquerda, como os black "
        "blocs (...), a partir do argumento de que manifestações da direita teriam sido sempre "
        "pacíficas'; e, na mesma página, 'O governo sabia': 'a partir da notícia de que a "
        "Agência Brasileira de Inteligência (Abin) teria alertado o governo sobre o risco de "
        "violência antes dos atos, especialmente figuras de políticos e mídia alinhados ao "
        "bolsonarismo utilizaram-se do fato para questionar se o governo teria sido complacente "
        "com o ocorrido para criminalizar a direita'. "
        "CONCLUSÃO DO RELATÓRIO, p. 15: 'a extrema-direita reconstruiu o debate nos seus termos "
        "e desvirtuou a narrativa para discutir não mais sobre quem eram os responsáveis, mas "
        "sobre se o governo sabia ou não dos atos e se haviam vândalos pagos para destruir os "
        "atos. E a esquerda, por fim, não conseguiu retomar o protagonismo no debate que tivera "
        "no dia dos atos.' "
        "MÉTRICAS DE APOIO: no dia 8, o post de maior interação é de Lula (17h54, 345.660 "
        "interações); no dia 9, o de Capitão Contar (21h37, 222.176 interações e 128.489 "
        "compartilhamentos), atribuindo os atos a infiltrados. "
        "DISPUTA DE NOMEAÇÃO, p. 9 — na nuvem de palavras do dia 8, 'manifestante' (4.000 "
        "menções) supera 'terrorista' (3.227) e 'golpista' (2.356): a designação do evento ainda "
        "estava em aberto no próprio dia. "
        "SOBREPOSIÇÃO CRONOLÓGICA DECLARADA: a emergência às 17h40 precede a nota de Bolsonaro "
        "das 21h17 (PT-50); a consolidação do fenômeno é posterior. O registro entra depois de "
        "PT-50 por afinidade de fase, não por estrita ordem de início.",

    "fonte_url": None,
    "fonte_local": MANCH,
    "fonte_pagina": "Manchetômetro: 3, 4, 9, 10, 13, 14, 15",

    "status_verificacao":
        "Confirmado quanto à existência, à datação e ao teor das narrativas, em relatório de "
        "laboratório universitário — Manchetômetro/Doxa-IESP-UERJ, mar/2023. NÃO REVISADO POR "
        "PARES: mesma qualificação de PT-19A (NetLab), e citável só como relatório técnico. "
        "QUATRO RESSALVAS DE MÉTODO, todas a declarar ao citar: (a) a coleta usou o CrowdTangle, "
        "DESCONTINUADO pela Meta em 14/08/2024 — os dados não são reproduzíveis por terceiros; "
        "(b) o universo é apenas o Facebook, não cobrindo WhatsApp (PT-19), Telegram nem X; (c) "
        "'interações' é métrica de plataforma, não medida de alcance nem de persuasão; (d) a "
        "seleção dos cinco posts de maior interação por período é critério dos próprios autores. "
        "PENDÊNCIA: a URL de origem do relatório não foi registrada quando o PDF entrou no "
        "corpus e precisa ser recuperada para citação formal.",

    "status_classe": "Confirmado",

    "nota_auditoria":
        "PT-50A CRIADO em 16/08/2026, resolvendo o último arquivo órfão do corpus. O relatório "
        "do Manchetômetro estava em Fontes/07_NetLab-UFRJ/ desde a auditoria sem vincular-se a "
        "registro nenhum. Decidido que VIRA REGISTRO, e não contexto declarado, por três razões: "
        "traz achado datável ausente do codebook (a contraofensiva narrativa dos 'infiltrados', "
        "às 17h40 de 8/1); tem precedente direto em PT-19A, que entrou a partir de fonte de "
        "mesma natureza; e ancora empiricamente o primeiro passo da inferência de PT-62. "
        "Contra-argumento considerado e rejeitado: o eixo 08 trata cobertura jornalística como "
        "objeto de análise, mas o Manchetômetro mede circulação em plataforma, não interpreta "
        "cobertura — é fonte, da mesma família do NetLab.",
}


def main():
    dry = "--dry-run" in sys.argv
    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    eventos = dados["eventos"]

    if any(e["id"] == "PT-50A" for e in eventos):
        print("PT-50A já existe — nada a fazer.")
        return

    campos = list(eventos[0].keys())
    novo = {c: PT50A.get(c) for c in campos}

    idx = next(i for i, e in enumerate(eventos) if e["id"] == "PT-50")
    eventos.insert(idx + 1, novo)

    dados["metadados"].setdefault("registro_documentos", {})["Manchetômetro"] = MANCH

    dados["metadados"]["revisoes"] = [
        r for r in dados["metadados"]["revisoes"] if not r.startswith("2026-08-16 (PT-50A)")
    ]
    dados["metadados"]["revisoes"].append(
        "2026-08-16 (PT-50A) — criado o registro PT-50A a partir do relatório do "
        "Manchetômetro/Doxa-IESP-UERJ, que era o último arquivo órfão do corpus. Documenta a "
        "CONTRAOFENSIVA NARRATIVA do campo bolsonarista: a atribuição dos atos a 'infiltrados da "
        "esquerda' emerge às 17h40 do próprio dia 8 e, em 9-10/01, desloca o debate para 'o "
        "governo sabia'. O codebook não cobria a disputa discursiva imediata do pós-evento. O "
        "registro ancora empiricamente o primeiro passo da inferência de PT-62 sobre migração da "
        "contestação para outras arenas. Classificado como 'Confirmado', não 'em fonte "
        "primária', pela mesma razão de PT-19A: relatório de laboratório universitário, não "
        "revisado por pares. Quatro ressalvas de método ficam declaradas no status, entre elas a "
        "descontinuação do CrowdTangle pela Meta em 14/08/2024, que torna a coleta não "
        "reproduzível. O codebook passa de 81 para 82 sub-eventos."
    )

    if dry:
        print("DRY RUN — nada gravado")
    else:
        JSON_P.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("JSON reescrito.")

    print("\nPT-50A inserido após PT-50 (posição {} de {})".format(idx + 2, len(eventos)))
    print("  data  :", novo["data_hora"])
    print("  fase  :", novo["fase"])
    print("  classe:", novo["status_classe"])
    print("  pagina:", novo["fonte_pagina"])


if __name__ == "__main__":
    main()
