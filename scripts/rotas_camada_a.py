# -*- coding: utf-8 -*-
"""TAREFA 17 — todas as rotas de deposito dos 26 pendentes da camada A.

POR QUE ISTO E NOVO. `localizar_camada_a.py` guardou do OpenAlex apenas o
`best_oa_location` (campos pdf_url/landing/licenca do cache). A memoria do
projeto registra que foi o campo `locations` -- TODOS os depositos, nao o
melhor -- que revelou Mayntz (2004) integral no MPG.PuRe depois de ele ter sido
dado como sem arquivo. Para os 26 pendentes esse campo nunca foi consultado.

Nao baixa nada. Responde so: para cada pendente, quais depositos existem.
"""
import csv
import io
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = r"D:/Projetos/Manifestações 8 de Janeiro"
ENTRADA = os.path.join(RAIZ, "data/processed/camada_a_acesso.csv")
AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(AQUI, "locais.jsonl")

UA = "verificador-bibliografico-8jan/1.0 (pesquisa academica; python-urllib)"
API = "https://api.openalex.org/works/doi:"


def pendentes():
    with io.open(ENTRADA, encoding="utf-8-sig", newline="") as fh:
        return [r for r in csv.DictReader(fh) if r["estado"] == "PENDENTE"]


def consultar(doi):
    req = urllib.request.Request(API + urllib.parse.quote(doi, safe="/:."),
                                 headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        return {"_erro": "HTTP %s" % e.code}
    except Exception as e:                                   # noqa: BLE001
        return {"_erro": type(e).__name__}


def local(loc):
    fonte = (loc.get("source") or {})
    return {
        "is_oa": bool(loc.get("is_oa")),
        "pdf": loc.get("pdf_url"),
        "landing": loc.get("landing_page_url"),
        "licenca": loc.get("license"),
        "versao": loc.get("version"),
        "fonte": fonte.get("display_name"),
        "hospeda": fonte.get("host_organization_name"),
        "tipo_fonte": fonte.get("type"),
    }


def main():
    itens = pendentes()
    print("pendentes na planilha: %d" % len(itens))
    cache = {}
    if os.path.exists(SAIDA):
        for linha in io.open(SAIDA, encoding="utf-8"):
            linha = linha.strip()
            if linha:
                reg = json.loads(linha)
                cache[reg["doi"]] = reg

    novos = 0
    with io.open(SAIDA, "a", encoding="utf-8", newline="\n") as fh:
        for it in itens:
            doi = it["doi"]
            if doi in cache:
                continue
            w = consultar(doi)
            reg = {"doi": doi, "titulo": it["titulo"], "veiculo": it["veiculo"]}
            if "_erro" in w:
                reg["erro"] = w["_erro"]
                reg["locais"] = []
            else:
                reg["erro"] = None
                reg["locais"] = [local(x) for x in (w.get("locations") or [])]
                reg["oa_status"] = (w.get("open_access") or {}).get("oa_status")
            fh.write(json.dumps(reg, ensure_ascii=False) + "\n")
            cache[doi] = reg
            novos += 1
            time.sleep(0.4)
    print("consultados agora: %d (cache: %d)" % (novos, len(cache)))

    # ------------------------------------------------- o que o campo revelou
    com_rota, sem_rota = [], []
    for doi in [i["doi"] for i in itens]:
        reg = cache[doi]
        oa = [l for l in reg["locais"] if l["is_oa"] and (l["pdf"] or l["landing"])]
        (com_rota if oa else sem_rota).append((reg, oa))

    print()
    print("=" * 78)
    print("COM pelo menos um deposito ABERTO no campo `locations`: %d" % len(com_rota))
    print("=" * 78)
    for reg, oa in com_rota:
        print()
        print("%s  %s" % (reg["doi"], (reg["titulo"] or "")[:58]))
        print("   %s | oa_status=%s | %d local(is), %d aberto(s)"
              % ((reg["veiculo"] or "")[:40], reg.get("oa_status"),
                 len(reg["locais"]), len(oa)))
        for l in oa:
            print("   - %-10s %-9s %s" % (l["versao"] or "-", l["licenca"] or "-",
                                          (l["fonte"] or "-")[:46]))
            if l["pdf"]:
                print("     PDF  %s" % l["pdf"])
            elif l["landing"]:
                print("     PAG  %s" % l["landing"])

    print()
    print("=" * 78)
    print("SEM nenhum deposito aberto: %d" % len(sem_rota))
    print("=" * 78)
    for reg, _ in sem_rota:
        print("  %-42s %-34s %s" % (reg["doi"], (reg["veiculo"] or "")[:34],
                                    reg.get("erro") or ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
