#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A prosa do registro cita páginas que o `fonte_pagina` não ancora?

`fonte_pagina` é o campo estruturado — o que as ferramentas leem, o que a
auditoria publica, o que o `conferir_paginas.py` abre no PDF. A prosa dos
campos `fonte_trecho`, `mecanismo_causal`, `status_verificacao` e
`nota_auditoria` também cita páginas, em linguagem corrida, e as duas coisas podem divergir sem que nada
reclame: nenhuma checagem do ciclo compara uma com a outra.

Divergiram. Em 25/09/2026, PT-10 ancorava "CPMI: 999, 1023" enquanto a própria
prosa do registro dizia "p. 999, 1021 e 1023" — a p. 1021 sustenta a cifra dos
bloqueios e tinha sumido do campo estruturado. Foi achado de raspão, porque o
relatório citava a página a mais. Onde nenhuma peça derivada cita, ninguém vê.
Este varredor existe para olhar os 82 de uma vez.

COMO LER O RESULTADO. Isto é triagem, não veredito: ele levanta candidatos e
imprime o trecho em volta de cada um para que a decisão leve segundos. Boa
parte do que aparece é legítima — página citada para REFUTAR ("na CPMI, '4 mil'
aparece em p. 532, referente diverso"), remissão a outro registro, ou menção a
documento que o registro não precisa ancorar. Por isso o padrão é sair com
código 0. Use `--estrito` para sair com 1 havendo achados.

O QUE ELE NÃO FAZ. Não abre PDF — quem confere se a página sustenta a
afirmação é o `conferir_paginas.py`. E não entende a frase: atribui cada "p. N"
ao documento nomeado mais perto, antes dela, o que erra quando a prosa volta a
um documento anterior sem renomeá-lo. Duas salvaguardas reduzem isso: páginas
já ancoradas sob OUTRO documento do mesmo registro são silenciadas, e o trecho
impresso deixa o engano visível.

Uso:  python scripts/varrer_fonte_pagina.py [--estrito] [--tudo]
      --tudo  também lista o que foi silenciado, para conferir as salvaguardas
"""

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
JSON_P = RAIZ / "process_tracing_8jan_eventos.json"

# `mecanismo_causal` entrou em 25/09/2026: é onde PT-28 citava dois documentos
# sem ancorar nenhum, e a varredura sem ele não via. Custo em ruído: zero.
CAMPOS = ("fonte_trecho", "mecanismo_causal", "status_verificacao", "nota_auditoria")

# Como os documentos aparecem escritos na prosa, além do código curto que o
# próprio JSON registra em metadados.registro_documentos.
ALIAS_EXTRA = {
    "relatório final da cpmi": "CPMI",
    "relatório do interventor federal": "Cappelli",
    "denúncia da pgr": "PGR",
    "pet 12.100": "PGR",
    "acórdão do trf-4": "TRF-4",
    "relatório do gabinete do min. alexandre de moraes": "Balanço 2026",
    "livro oficial do stf": "Livro STF 2023",
    "livro do stf": "Livro STF 2023",
}

# Quão perto o nome do documento precisa estar, antes do "p.", para valer como
# atribuição explícita. Além disso, herda-se o documento corrente do campo.
JANELA = 70

# "p. 1023" | "p. 25, 53 e 274" | "p. 577-578" | "p. 34–35". O grupo 1 captura
# o til de aproximação: "p. ~800-980" é estimativa de capítulo, não citação.
CITACAO = re.compile(r'(~\s*)?\bp\.\s*(~?\s*\d+(?:\s*[-–—]\s*\d+)?'
                     r'(?:\s*(?:,|e)\s*\d+)*)')


def paginas(trecho):
    """'25, 53 e 274' -> {25, 53, 274}; de um intervalo, só as pontas."""
    saida = set()
    for item in re.split(r'\s*(?:,|\be\b)\s*', trecho.strip()):
        nums = re.findall(r'\d+', item)
        if nums:
            saida.add(int(nums[0]))
            saida.add(int(nums[-1]))
    return saida


def ancoras(registro, reg_docs):
    """O que o registro ancora, indexado pelo CAMINHO do arquivo.

    Pelo caminho, e não pelo rótulo, porque dois códigos podem apontar para a
    mesma peça — 'Doxa' e 'Manchetômetro' são o mesmo PDF, e a prosa alterna
    entre os dois."""
    saida = {}
    for parte in (registro.get("fonte_pagina") or "").split("|"):
        if ":" not in parte:
            continue
        rotulo, nums = parte.split(":", 1)
        rotulo = rotulo.strip()
        numeros = {int(n) for n in re.findall(r'\d+', nums)}
        if numeros:
            saida[reg_docs.get(rotulo, rotulo)] = (rotulo, numeros)
    return saida


def trecho_em_volta(texto, pos, antes=110, depois=55):
    recorte = texto[max(0, pos - antes):pos + depois].strip()
    return re.sub(r'\s+', " ", recorte)


def main():
    estrito = "--estrito" in sys.argv
    tudo = "--tudo" in sys.argv

    dados = json.loads(JSON_P.read_text(encoding="utf-8"))
    reg_docs = dados["metadados"]["registro_documentos"]

    alias = dict(ALIAS_EXTRA)
    for codigo in reg_docs:
        alias.setdefault(codigo.lower(), codigo)
    termos = sorted(alias, key=len, reverse=True)   # o rótulo mais longo vence

    nao_ancorado, fora_do_campo, silenciados = [], [], []
    vistas = herdadas = orfas = aproximadas = 0

    for e in dados["eventos"]:
        anc = ancoras(e, reg_docs)
        for campo in CAMPOS:
            texto = e.get(campo) or ""
            minusculo = texto.lower()
            corrente = None
            for m in CITACAO.finditer(texto):
                if m.group(1) or "~" in m.group(2):
                    aproximadas += 1
                    continue
                pgs = paginas(m.group(2))
                if not pgs:
                    continue
                vistas += 1

                codigo, pos = None, -1
                for termo in termos:
                    achado = minusculo.rfind(termo, max(0, m.start() - JANELA), m.start())
                    if achado > pos:
                        codigo, pos = alias[termo], achado
                explicito = codigo is not None
                if not explicito:
                    if corrente is None:
                        orfas += 1
                        continue
                    codigo = corrente
                    herdadas += 1
                else:
                    corrente = codigo

                caminho = reg_docs.get(codigo, codigo)
                item = (e["id"], campo, codigo, sorted(pgs), explicito,
                        trecho_em_volta(texto, m.start()))

                if caminho not in anc:
                    nao_ancorado.append(item)
                    continue
                rotulo, numeros = anc[caminho]
                sobrando = pgs - numeros
                if not sobrando:
                    continue
                # Salvaguarda: se a página já está ancorada sob OUTRO documento
                # deste registro, o mais provável é que a atribuição do varredor
                # esteja errada, não que falte âncora.
                alhures = [r for c, (r, n) in anc.items()
                           if c != caminho and sobrando <= n]
                if alhures:
                    silenciados.append(item + (rotulo, alhures[0]))
                    continue
                fora_do_campo.append((e["id"], campo, rotulo, sorted(sobrando),
                                      sorted(numeros), explicito,
                                      trecho_em_volta(texto, m.start())))

    print("VARREDURA: prosa do registro x fonte_pagina")
    print("=" * 78)
    print("  {} citações de página na prosa dos {} registros".format(
        vistas, len(dados["eventos"])))
    print("  {} com documento nomeado ao lado · {} herdadas do contexto · "
          "{} sem documento identificável".format(
              vistas - herdadas - orfas, herdadas, orfas))
    print("  {} intervalo(s) aproximado(s) (~) ignorado(s) · "
          "{} silenciada(s) pela salvaguarda".format(aproximadas, len(silenciados)))

    def bloco(titulo, itens, formato):
        print()
        print("-" * 78)
        print("{} — {}".format(titulo, len(itens)))
        print("-" * 78)
        if not itens:
            print("  (nenhum)")
        for it in itens:
            for linha in formato(it):
                print(linha)

    bloco("A. Documento citado com página e NAO ancorado no registro", nao_ancorado,
          lambda it: ["  {} [{}] {}, p. {}{}".format(
              it[0], it[1], it[2], ", ".join(str(n) for n in it[3]),
              "" if it[4] else "   (documento herdado do contexto)"),
              "      ...{}...".format(it[5])])

    bloco("B. Página do MESMO documento, fora do fonte_pagina", fora_do_campo,
          lambda it: ["  {} [{}] «{}» p. {} — ancoradas: {}{}".format(
              it[0], it[1], it[2], ", ".join(str(n) for n in it[3]),
              ", ".join(str(n) for n in it[4]),
              "" if it[5] else "   (documento herdado do contexto)"),
              "      ...{}...".format(it[6])])

    if tudo:
        bloco("C. Silenciadas — página já ancorada sob outro documento do registro",
              silenciados,
              lambda it: ["  {} [{}] atribuída a «{}», mas p. {} está em «{}»".format(
                  it[0], it[1], it[6], ", ".join(str(n) for n in it[3]), it[7]),
                  "      ...{}...".format(it[5])])

    achados = len(nao_ancorado) + len(fora_do_campo)
    print()
    print("=" * 78)
    if achados:
        print("{} candidato(s) para triagem. Página citada na prosa não é, por si, "
              "página que".format(achados))
        print("falta: pode ser refutação, remissão a outro registro ou menção de passagem.")
        print("Leia o trecho, e só então decida. Correção de fonte_pagina vai por script")
        print("de migração — veja scripts/historico/recodificar_pagina_pt10.py como modelo.")
    else:
        print("OK — nenhuma página citada na prosa ficou fora do fonte_pagina")
    return 1 if (achados and estrito) else 0


if __name__ == "__main__":
    sys.exit(main())
