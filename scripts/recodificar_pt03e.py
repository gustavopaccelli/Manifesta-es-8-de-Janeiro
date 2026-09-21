#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Resolução de PT-03E — o acórdão do TSE, obtido SEM captcha.

Rodada de 16/08/2026. Era a última peça do arco judicial e estava classificada
como bloqueada por captcha desde a abertura do eixo.

COMO FOI OBTIDO. O buscador de jurisprudência do TSE (jurisprudencia.tse.jus.br)
é uma SPA Angular cuja API — sjur-pesquisa-api.tse.jus.br — exige verificação
antirrobô: um POST em /public/pesquisa sem token responde
{"mensagem":"Falha na verificação antirrobô."}. NÃO foi feita nenhuma tentativa
de contornar essa verificação.

A rota que funcionou é outra e é pública: o endpoint de documento da Consulta
Unificada PJe, em consultaunificadapje.tse.jus.br, serve o inteiro teor por
caminho direto, sem captcha. O caminho do acórdão foi localizado por busca web.

DUAS CORREÇÕES DE DOCUMENTAÇÃO que esta rodada produziu:
  1. O captcha do TSE é hCAPTCHA, não reCAPTCHA. Todo o material do projeto
     dizia reCAPTCHA. Verificado no bundle: o buscador carrega
     js.hcaptcha.com/1/api.js e não há nenhuma referência a recaptcha.
  2. O acórdão NÃO É PDF. O endpoint serve HTML e ignora o parâmetro
     extensaoArquivo — pedir application/pdf devolve o mesmo HTML, só muda o
     Content-Type. O arquivo entra no corpus como .html, e a citação é por
     estrutura interna (ementa, itens, dispositivo), não por página.

Uso:  python scripts/recodificar_pt03e.py [--dry-run]
"""

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"
TSE = "Fontes/01_Arco-judicial_2017-2021/TSE_RCand-0600903-50_Acordao_2018-09-01.html"

PT03E = {
    "repertorio_acao":
        "Indeferimento do registro de candidatura de Lula à Presidência, por maioria, com "
        "declaração de inelegibilidade pelo art. 1º, I, 'e', itens 1 e 6, da LC 64/1990 (Lei da "
        "Ficha Limpa); faculta substituição em 10 dias, veda atos de campanha e propaganda "
        "eleitoral no rádio e na TV, e determina a retirada do nome da programação da urna "
        "eletrônica",

    "mecanismo_causal":
        "Exclusão institucional do favorito — e, agora que o inteiro teor está no corpus, com a "
        "cadeia causal explicitada pelo próprio tribunal. O acórdão liga formalmente a condenação "
        "colegiada do TRF-4 (PT-03B) à inelegibilidade: 'O candidato requerente foi condenado "
        "criminalmente por órgão colegiado do Tribunal Regional Federal da 4ª Região (...) "
        "Incide, portanto, a causa de inelegibilidade'. O que torna o registro analiticamente "
        "forte é a SÚMULA 41/TSE, invocada no item 4 da ementa: a Justiça Eleitoral declara não "
        "ter competência para examinar 'o acerto ou desacerto das decisões proferidas por outros "
        "órgãos do Judiciário'. Ou seja, o efeito eleitoral da condenação opera por AUTOMATISMO "
        "INSTITUCIONAL — basta a decisão colegiada existir. Isso é decisivo para a leitura do "
        "arco judicial: quando o STF vier a anular os atos por incompetência (PT-06A) e a "
        "reconhecer a suspeição do julgador (PT-06B), o efeito eleitoral de 2018 já se consumara "
        "e era irreversível. A remoção do competidor não dependeu de a condenação ser boa; "
        "dependeu apenas de ela ser colegiada e existir a tempo.",

    "fonte_trecho":
        "Acórdão do TSE, Registro de Candidatura nº 0600903-50.2018.6.00.0000, rel. min. Luís "
        "Roberto Barroso, Brasília, 1º de setembro de 2018. "
        "EMENTA, item 2: a LC 64/1990, com redação da LC 135/2010 ('Lei da Ficha Limpa'), torna "
        "inelegíveis 'os que forem condenados, em decisão transitada em julgado ou proferida por "
        "órgão judicial colegiado, desde a condenação até o transcurso do prazo de 8 (oito) anos "
        "após o cumprimento da pena' pelos crimes que arrola (art. 1º, I, 'e', itens 1 e 6). "
        "Item 3: 'O candidato requerente foi condenado criminalmente por órgão colegiado do "
        "Tribunal Regional Federal da 4ª Região, pelos crimes de corrupção passiva (art. 317 do "
        "Código Penal) e lavagem de dinheiro (art. 1º, caput e V, da Lei nº 9.613/1998). Incide, "
        "portanto, a causa de inelegibilidade prevista no art. 1º, I, alínea e, itens 1 e 6, da "
        "LC nº 64/1990.' "
        "Item 4, SÚMULA 41/TSE: 'A Justiça Eleitoral não tem competência para analisar se a "
        "decisão criminal condenatória está correta ou equivocada. (...) não cabe à Justiça "
        "Eleitoral decidir sobre o acerto ou desacerto das decisões proferidas por outros órgãos "
        "do Judiciário ou dos tribunais de contas que configurem causa de inelegibilidade'. "
        "Item 12, efeitos: '(i) faculta-se à coligação substituir o candidato, no prazo de 10 "
        "(dez) dias; (ii) fica vedada a prática de atos de campanha presidencial pelo candidato "
        "cujo registro vem de ser indeferido; e (iii) determina-se a retirada do nome do "
        "candidato da programação da urna eletrônica'. "
        "DISPOSITIVO: 'Acordam os ministros do Tribunal Superior Eleitoral, por maioria, em "
        "julgar procedentes as impugnações (...), declarar a inelegibilidade de Luiz Inácio Lula "
        "da Silva, com base no artigo 1º, inciso I, alínea e, itens 1 e 6, da Lei Complementar nº "
        "64/1990, e indeferir o pedido de registro de candidatura ao cargo de Presidente da "
        "República.' Datado de 1º de setembro de 2018. "
        "IMPUGNANTES arrolados no acórdão, entre outros: Ministério Público Eleitoral, Partido "
        "Novo, Kim Patroca Kataguiri, a coligação 'Brasil Acima de Tudo, Deus Acima de Todos' e "
        "Jair Messias Bolsonaro — este último, adversário direto no pleito, figura formalmente "
        "como impugnante.",

    "fonte_url":
        "https://consultaunificadapje.tse.jus.br/consulta-publica-unificada/documento"
        "?extensaoArquivo=text/html&path=tse/2018/10/15/16/"
        "27d7840a9d81d321d006c4131443ab64a984b9e1",

    "fonte_local": TSE,
    "fonte_pagina": "TSE RCand: ementa itens 2-4 e 12; dispositivo",

    "status_verificacao":
        "Confirmado em fonte primária — inteiro teor do acórdão obtido em 16/08/2026 no endpoint "
        "público de documentos da Consulta Unificada PJe do TSE, domínio oficial "
        "consultaunificadapje.tse.jus.br, SEM captcha. 947.206 bytes, cerca de 476 mil caracteres "
        "de texto útil, SHA-256 80288ca9fe52586955bf76e17f523a05… "
        "RESSALVA DE FORMATO: o TSE serve este documento como HTML, não como PDF — o parâmetro "
        "extensaoArquivo altera só o Content-Type, e pedir application/pdf devolve o mesmo HTML. "
        "Por isso a citação é por estrutura interna do acórdão (item da ementa, dispositivo) e "
        "não por página, e o arquivo não entra na contagem de PDFs do corpus.",

    "status_classe": "Confirmado em fonte primária",

    "nota_auditoria":
        "PT-03E RESOLVIDO em 16/08/2026 — última peça do arco judicial. O inteiro teor foi obtido "
        "SEM captcha, por rota pública distinta do buscador de jurisprudência: o endpoint de "
        "documento da Consulta Unificada PJe. A API do buscador (sjur-pesquisa-api) exige "
        "verificação antirrobô e responde 'Falha na verificação antirrobô' sem token; nenhuma "
        "tentativa de contorná-la foi feita. DUAS CORREÇÕES DE DOCUMENTAÇÃO: o captcha do TSE é "
        "hCAPTCHA e não reCAPTCHA, como o projeto vinha registrando; e o acórdão é servido em "
        "HTML, não em PDF. ACHADO SUBSTANTIVO: a Súmula 41/TSE, invocada na ementa, mostra que o "
        "efeito eleitoral da condenação opera por automatismo — a Justiça Eleitoral se declara "
        "incompetente para rever o mérito —, o que explica por que as anulações posteriores do "
        "STF (PT-06A e PT-06B) não puderam desfazer a exclusão de 2018.",
}


def main():
    dry = "--dry-run" in sys.argv
    if not (RAIZ / TSE).exists():
        raise SystemExit("ERRO: acórdão não encontrado em " + TSE)

    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    for ev in dados["eventos"]:
        if ev["id"] == "PT-03E":
            print("=== PT-03E — antes ===")
            print("  classe:", ev["status_classe"], "| local:", ev.get("fonte_local") or "(vazio)")
            ev.update(PT03E)
            print("=== PT-03E — depois ===")
            print("  classe:", ev["status_classe"])
            print("  local :", ev["fonte_local"])

    dados["metadados"].setdefault("registro_documentos", {})["TSE RCand"] = TSE

    dados["metadados"]["revisoes"] = [
        r for r in dados["metadados"]["revisoes"] if not r.startswith("2026-08-16 (PT-03E)")
    ]
    dados["metadados"]["revisoes"].append(
        "2026-08-16 (PT-03E) — obtido o inteiro teor do acórdão do TSE que indeferiu o registro "
        "de candidatura de Lula (RCand 0600903-50.2018.6.00.0000, rel. min. Barroso, 1º/09/2018), "
        "fechando o arco judicial 2016-2021. Conseguido SEM captcha, por rota pública distinta do "
        "buscador de jurisprudência: o endpoint de documento da Consulta Unificada PJe. A API do "
        "buscador exige verificação antirrobô e nenhuma tentativa de contorná-la foi feita. "
        "Corrigem-se duas informações que o projeto vinha repetindo: o captcha do TSE é hCAPTCHA, "
        "não reCAPTCHA, e o acórdão é servido em HTML, não em PDF. ACHADO: a ementa invoca a "
        "Súmula 41/TSE — a Justiça Eleitoral não examina 'o acerto ou desacerto' da condenação —, "
        "de modo que o efeito eleitoral opera por automatismo institucional. Isso explica por que "
        "a anulação por incompetência (PT-06A) e o reconhecimento da suspeição de Moro (PT-06B), "
        "ambos posteriores, não puderam desfazer a exclusão consumada em 2018."
    )

    if dry:
        print("\nDRY RUN — nada gravado")
    else:
        JSON_P.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("\nJSON reescrito.")


if __name__ == "__main__":
    main()
