# -*- coding: utf-8 -*-
"""TAREFA 17 — a peca lida hoje entra no codebook, e o residuo do vocabulario sai.

TRES MUDANCAS, e a ordem das guardas vem ANTES do write: em 09/10 um script
deste tipo poe o assert depois da escrita e exigiu restore de backup.

1. PT-07 ganha ancora de literatura e a QUALIFICACAO do nome do mecanismo. O
   padrao e o de PT-62: registra-se a divergencia entre o nome que o registro usa
   e o que a fonte define, e NAO se renomeia -- nomear mecanismo e decisao do
   pesquisador (precedente da tarefa 19, 10/10/2026).
2. `registro_documentos` ganha o codigo da peca (sem hifen, que e a regra do
   conferidor).
3. `aviso_metodologico` para de ensinar `Contextual` como valor vigente. A classe
   saiu do vocabulario em 08/10/2026 e a propria nota metodologica do JSON
   continuava listando-a -- e omitindo `Confirmado em fonte primaria`, que existe.
   A checagem 7 vigia nome aposentado nos artefatos de mao; ninguem vigiava a
   prosa do proprio JSON.

NENHUMA ASPA fora das transcricoes reais no fonte_trecho: aspa em volta de nome
de mecanismo promove o nome a transcricao e manda o conferidor procura-lo no PDF
(foi o que PT-62 fez em 09/10). As cinco transcricoes abaixo foram testadas com
confere_integral ANTES desta escrita: cinco OK, nenhuma parcial.
"""
import io
import json
import os
import shutil
import sys
import time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.chdir(r"D:/Projetos/Manifestações 8 de Janeiro")

JSON = "process_tracing_8jan_eventos.json"
DOC = ("Fontes/05_Bibliografia-teorica/SNOW-VLIEGENTHART-KETELAARS_"
       "The-framing-perspective-on-social-movements_Wiley-Blackwell-Companion-2ed_2019.pdf")
CODIGO = "SNOW VLIEGENTHART E KETELAARS 2019"

ACRESCIMO = (
    " || ACRÉSCIMO DE 13/10/2026 — TAREFA 17, e esta é a peça que dá ao marco "
    "teórico declarado do codebook a sua primeira leitura na fonte. A peça: SNOW, "
    "VLIEGENTHART e KETELAARS (2019), capítulo 22 de The Wiley Blackwell Companion "
    "to Social Movements, 2ª ed., pp. 392-410, lida integral; página impressa = PDF "
    "+ 390. O codebook declara Framing (Snow e Benford, 2000) no campo marco_teorico, "
    "e esse balanço de 2000 nunca foi lido — continua FECHADO na camada A. Este "
    "capítulo é o balanço posterior, do mesmo autor principal, e é o que está lido. "
    "O QUE A FONTE DEFINE: “Frame alignment processes encompass the strategic efforts "
    "of social movement actors and organizations to link their interests and goals "
    "with those of prospective adherents and resource providers” (p. 400 impressa — "
    "PDF p. 10), em quatro processos que o capítulo atribui a Snow et al. (1986) — "
    "bridging, amplification, extension e transformation. E separa disso os mecanismos "
    "discursivos pelos quais um quadro é gerado e modificado: “Frame articulation "
    "involves the connection, or splicing together, and coordination of issues” (p. 397 "
    "— PDF p. 7) e “frame elaboration involves accenting and highlighting some events” "
    "(p. 398 — PDF p. 8); e define a tarefa de enquadramento que a narrativa de fraude "
    "cumpre, o diagnóstico, que inclui “the attribution of blame or responsibility for "
    "the problematized state of affairs” (p. 396 — PDF p. 6). A QUALIFICAÇÃO IMPORTA "
    "PARA O NOME DO MECANISMO DESTE REGISTRO, e é o motivo de ela estar aqui: o que a "
    "denúncia documenta em 22/03/2021 é o núcleo deliberando e passando a disseminar um "
    "diagnóstico — articulação e elaboração de quadro, na distinção do capítulo. "
    "Alinhamento é a ligação estratégica a um público, e o tipo que corresponderia é o "
    "bridging, “the linkage of a movement organization with an unmobilized sentiment "
    "pool” (p. 400 — PDF p. 10), que é o que PT-06 documenta em 2020-2021, não o que "
    "este registro documenta. O nome atual nomeia a família, não o processo. NÃO "
    "RENOMEEI: nomear mecanismo é decisão do pesquisador, pelo precedente da tarefa 19, "
    "e a proposta está no item 47 de docs/PENDENCIAS-ANALITICAS.md. LIMITE DA LEITURA, "
    "declarado: ter lido este capítulo não autoriza citar Benford e Snow (2000) nem "
    "Snow et al. (1986) — citar cifra ou tese conferida apenas na citação de terceiro é "
    "o modo de falha que este projeto nomeia. O que a leitura autoriza é citar o capítulo."
)

AVISO_VELHO = (
    "O campo 'status_verificacao' distingue: 'Confirmado' (fonte localizada e "
    "citada), 'A verificar' (fato amplamente noticiado, sem fonte primária "
    "consultada nesta rodada), 'Contextual' (item de enquadramento histórico que "
    "depende da bibliografia teórica, não de fonte primária) e 'Inferência do "
    "analista'."
)
AVISO_NOVO = (
    "O campo 'status_verificacao' narra a verificação em prosa; a classe controlada "
    "é 'status_classe', e os valores vigentes estão em 'vocabulario_status_classe': "
    "'Confirmado em fonte primária' (documento oficial ou peça de literatura lida, "
    "com página conferida), 'Confirmado' (fonte localizada e citada), 'A verificar' "
    "(fato amplamente noticiado, sem fonte primária consultada nesta rodada) e "
    "'Inferência do analista' (leitura do analista, declarada como tal). ATENÇÃO AO "
    "HISTÓRICO: 'Contextual' SAIU do vocabulário em 08/10/2026 (ver 'revisoes'), e "
    "esta nota continuou listando-a como valor vigente — e omitindo 'Confirmado em "
    "fonte primária', que existe — até 13/10/2026. As ocorrências de 'Contextual' "
    "nos campos de prosa dos registros são narração datada de recodificação e ficam."
)

REVISAO = (
    "2026-10-13 — TAREFA 17, leitura na fonte da camada A: a rodada rendeu UMA peça "
    "das 26 pendentes, e o número é o resultado. O campo `locations` da API do "
    "OpenAlex — todos os depósitos, não só o melhor — nunca havia sido consultado "
    "para os pendentes, e foi essa consulta que achou SNOW, VLIEGENTHART e KETELAARS "
    "(2019) integral no UvA-DARE. Os outros quatro com rota declarada devolveram 403 "
    "(Oxford, SAGE duas vezes, Wiley) e 22 não têm depósito aberto em lugar algum; "
    "EUI Cadmus e ricerca.sns.it, que são repositórios e não editores, também barram "
    "cliente automatizado, e Cambridge e a Wayback Machine devolveram 429 em três "
    "tentativas. A peça entrou no corpus, ancora PT-07 e qualifica o nome do "
    "mecanismo desse registro, sem renomeá-lo. Na mesma rodada, 'aviso_metodologico' "
    "parou de ensinar 'Contextual' como valor vigente do vocabulário."
)


def main():
    d = json.load(io.open(JSON, encoding="utf-8"))
    md, evs = d["metadados"], d["eventos"]

    # ------------------------------------------------------- GUARDAS, antes de escrever
    assert os.path.exists(DOC), "o PDF não está no corpus"
    assert CODIGO not in md["registro_documentos"], "código já registrado"
    assert "-" not in CODIGO, "código com hífen quebra o conferidor"
    assert md["aviso_metodologico"].count(AVISO_VELHO) == 1, "o aviso mudou de forma"
    pt07 = [e for e in evs if e["id"] == "PT-07"]
    assert len(pt07) == 1, "PT-07 não é único"
    pt07 = pt07[0]
    assert "TAREFA 17" not in (pt07["fonte_trecho"] or ""), "acréscimo já aplicado"
    classes_antes = {}
    for e in evs:
        classes_antes[e["status_classe"]] = classes_antes.get(e["status_classe"], 0) + 1
    assert classes_antes.get("Confirmado em fonte primária") == 61, classes_antes
    assert len(evs) == 83, len(evs)

    # ------------------------------------------------------------------ as mudanças
    pt07["fonte_trecho"] = (pt07["fonte_trecho"] or "") + ACRESCIMO
    pt07["fonte_local"] = (pt07["fonte_local"] or "") + "; " + DOC
    pt07["fonte_pagina"] = (pt07["fonte_pagina"] or "") + " | %s: 6, 7, 8, 10" % CODIGO
    md["registro_documentos"][CODIGO] = DOC
    md["aviso_metodologico"] = md["aviso_metodologico"].replace(AVISO_VELHO, AVISO_NOVO)
    md["revisoes"].append(REVISAO)

    # Classe não muda: PT-07 já estava confirmado em fonte primária pela denúncia.
    depois = {}
    for e in evs:
        depois[e["status_classe"]] = depois.get(e["status_classe"], 0) + 1
    assert depois == classes_antes, (depois, classes_antes)

    backup = ".backup_pre_lula/eventos_pre_tarefa17_%s.json" % time.strftime("%Y%m%d-%H%M")
    os.makedirs(os.path.dirname(backup), exist_ok=True)
    shutil.copyfile(JSON, backup)
    io.open(JSON, "w", encoding="utf-8", newline="\n").write(
        json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print("JSON reescrito. backup: %s" % backup)
    print("classes: %s" % depois)
    print("documentos no registro: %d" % len(md["registro_documentos"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
