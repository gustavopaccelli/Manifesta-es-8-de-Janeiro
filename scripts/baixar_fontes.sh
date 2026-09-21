#!/usr/bin/env bash
#
# Coleta das fontes primárias que faltam ao corpus do 8 de Janeiro.
# Gerado em 16/08/2026 a partir de reports/AUDITORIA-FONTES.md.
#
# ============================================================================
# LEIA ANTES DE RODAR
# ============================================================================
#
# Este script NÃO baixa nada sozinho. Cada peça é um alvo separado, invocado
# por nome, para que você veja o que vai buscar antes de buscar:
#
#     bash scripts/baixar_fontes.sh listar        # o que falta e por quê
#     bash scripts/baixar_fontes.sh agencia       # arquivamento das matérias (sem bloqueio)
#     bash scripts/baixar_fontes.sh stf-noticias  # páginas de notícia do STF
#     bash scripts/baixar_fontes.sh stf-busca "prisão preventiva Bolsonaro"
#     bash scripts/baixar_fontes.sh stf-doc <docID> <nome-do-arquivo.pdf> <pasta>
#     bash scripts/baixar_fontes.sh tse           # instruções (exige pessoa)
#     bash scripts/baixar_fontes.sh conferir      # paginação e camada de texto do que chegou
#
# DUAS PROTEÇÕES ANTI-BOT, tratadas de formas diferentes:
#
#   STF  — AWS WAF com desafio JavaScript. Requisição sem execução de JS recebe
#          HTTP 202 com corpo vazio, o que se parece com bloqueio mas é o desafio
#          não resolvido. Solução: abrir qualquer página do STF num navegador real,
#          copiar o cookie `aws-waf-token` e exportá-lo antes de rodar:
#
#              export AWS_WAF_TOKEN='cole-o-valor-aqui'
#
#          O token expira em algumas horas. Se voltar 202, pegue outro.
#
#   TSE  — hCAPTCHA (não reCAPTCHA, como este script dizia até 16/08/2026).
#          Protege a API do buscador de jurisprudência, que sem token responde
#          {"mensagem":"Falha na verificação antirrobô."}. NÃO deve ser
#          contornado. Mas a Consulta Unificada PJe serve o inteiro teor por
#          caminho direto, SEM captcha — foi assim que PT-03E se resolveu.
#          Ver o alvo `tse`.
#
# ============================================================================

set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'
D01="Fontes/01_Arco-judicial_2017-2021"
D03="Fontes/03_T0_8-de-janeiro"
D04="Fontes/04_T+1_Resposta-institucional"
D08="Fontes/09_Arquivamento-web"

log()  { printf '\n\033[1m%s\033[0m\n' "$*"; }
ok()   { printf '  \033[32mOK\033[0m   %s\n' "$*"; }
warn() { printf '  \033[33m~\033[0m    %s\n' "$*"; }
err()  { printf '  \033[31mX\033[0m    %s\n' "$*"; }

# Baixa preservando o arquivo já existente. Nada é sobrescrito em silêncio.
baixar() {
  local url="$1" destino="$2"
  if [[ -s "$destino" ]]; then
    warn "já existe, preservado: $destino"
    return 0
  fi
  mkdir -p "$(dirname "$destino")"
  if curl -fsSL --retry 2 --max-time 180 -A "$UA" -o "$destino.parcial" "$url"; then
    mv "$destino.parcial" "$destino"
    ok "$destino  ($(du -h "$destino" | cut -f1))"
  else
    rm -f "$destino.parcial"
    err "falhou: $url"
    return 1
  fi
}

# ---------------------------------------------------------------------------
listar() {
  cat <<'FIM'

FILA DE COLETA — 16/08/2026
===========================

✅ RESOLVIDOS NESTA DATA
  [PT-03E] Acórdão do TSE — obtido SEM captcha, via Consulta Unificada PJe.
           Ver o alvo `tse`: traz a rota e duas correções de documentação.
  [PT-53]  Balanço "Democracia Inabalada" — obtido no bucket S3 oficial do STF.
  [PT-61]  Mesma peça; 1.402 réus agora citável como dado oficial, com página.
  [PT-58]  Prisão preventiva — corroboração jornalística dupla (Agência Brasil).
  [PT-52]  Detidos na desocupação — adotadas as 2.151 prisões em flagrante.
  [PT-12]  "Mais de 100 acampamentos" — cifra retirada, sem lastro.
  [PT-17]  Saída de Bolsonaro do país — confirmada na CPMI, p. 612.
  [PT-34]  Os "4 mil" na Praça — cifra retirada, substituída por faixa.
  [—]      Manchetômetro (Doxa/IESP-UERJ) — virou o registro PT-50A.

AINDA ABERTOS
  [PT-59]  Decisão de transferência para a Papuda (15/01/2026)   — STF, WAF
  [PT-60]  Prisão domiciliar humanitária, Exec. Penal 169        — STF, WAF
           Ambos apoiados em notícia do portal do STF, não na decisão.
  [vários] Arquivamento em PDF das matérias da Agência Brasil    — sem bloqueio
           Contra link rot: hoje esses registros existem só como URL viva.

BAIXA PRIORIDADE — declarar como limite, não perseguir
  [PT-38]  Laudos do Instituto de Criminalística/PF  — restrição confirmada
           O livro oficial do STF já cobre o essencial.
  [PT-03A] Sentença de Moro, inteiro teor            — JFPR/e-proc, exige login
           O dispositivo já está transcrito no acórdão do TRF-4, p. 395.
  [PT-02A] Acórdão completo do HC 126.292            — só o voto de Barroso
           foi localizado (28 p., mirror). Já documentado via ADC 43/44/54.

FIM
}

# ---------------------------------------------------------------------------
# Arquivamento das matérias jornalísticas. Sem bloqueio algum.
# Preserva o HTML; a evidência deixa de depender de a URL continuar viva.
agencia() {
  log "ARQUIVAMENTO WEB — matérias hoje ancoradas só por URL"
  mkdir -p "$D08"
  baixar "https://agenciabrasil.ebc.com.br/politica/noticia/2017-07/ex-presidente-lula-e-condenado-nove-anos-e-seis-meses-de-prisao" \
         "$D08/AgenciaBrasil_2017-07-12_Condenacao-Lula_PT-03A.html"
  baixar "https://agenciabrasil.ebc.com.br/politica/noticia/2018-04/lula-chega-policia-federal-em-curitiba-para-comecar-cumprir-pena" \
         "$D08/AgenciaBrasil_2018-04-07_Prisao-Curitiba_PT-03D.html"
  baixar "https://agenciabrasil.ebc.com.br/geral/noticia/2024-09/democracia-restaurada-obras-vandalizadas-no-81-sao-recuperadas-0" \
         "$D08/AgenciaBrasil_2024-09_Obras-recuperadas_PT-38.html"
  baixar "https://www.tse.jus.br/comunicacao/noticias/2018/Setembro/tse-indefere-pedido-de-registro-de-candidatura-de-lula-a-presidencia-da-republica" \
         "$D08/TSE_2018-09-01_Indeferimento-registro_PT-03E.html"
  warn "HTML não é fonte primária: serve como evidência de que a notícia existiu"
  warn "e do que ela dizia. O acórdão do TSE segue pendente (alvo: tse)."
}

# ---------------------------------------------------------------------------
stf_noticias() {
  log "PÁGINAS DE NOTÍCIA DO STF — PT-53, PT-59, PT-60"
  mkdir -p "$D08"
  baixar "https://noticias.stf.jus.br/postsnoticias/em-dois-anos-stf-responsabilizou-898-pessoas-por-atos-antidemocraticos-de-8-de-janeiro/" \
         "$D08/STF-noticias_Responsabilizacao-2anos_PT-53.html"
  baixar "https://noticias.stf.jus.br/postsnoticias/stf-determina-transferencia-do-ex-presidente-bolsonaro-para-unidade-da-pm-df-no-complexo-penitenciario-da-papuda/" \
         "$D08/STF-noticias_Transferencia-Papuda_PT-59.html"
  baixar "https://noticias.stf.jus.br/postsnoticias/stf-concede-prisao-domiciliar-temporaria-ao-ex-presidente-jair-bolsonaro/" \
         "$D08/STF-noticias_Prisao-domiciliar_PT-60.html"
  warn "Notícia institucional NÃO é a decisão. Para o inteiro teor use stf-busca."
}

# ---------------------------------------------------------------------------
# Busca na API de jurisprudência do STF. Devolve o idDocumento que o alvo
# stf-doc consome. Exige AWS_WAF_TOKEN exportado.
stf_busca() {
  local termo="${1:-}"
  [[ -z "$termo" ]] && { err 'uso: baixar_fontes.sh stf-busca "termo de busca"'; return 1; }
  if [[ -z "${AWS_WAF_TOKEN:-}" ]]; then
    err "AWS_WAF_TOKEN não está definido."
    cat <<'FIM'
       Como obter:
         1. abra https://portal.stf.jus.br num navegador real
         2. deixe a página carregar por inteiro (o WAF emite o cookie)
         3. DevTools > Application > Cookies > copie o valor de `aws-waf-token`
         4. export AWS_WAF_TOKEN='valor'
       O token expira em algumas horas.
FIM
    return 1
  fi
  log "BUSCA NO STF: $termo"
  curl -sS -X POST "https://jurisprudencia.stf.jus.br/api/search/search" \
    -H "Content-Type: application/json" \
    -H "Cookie: aws-waf-token=${AWS_WAF_TOKEN}" \
    -A "$UA" \
    -d "{\"query\":\"${termo}\",\"size\":10,\"from\":0}" \
    | python -X utf8 -c '
import json,sys
try:
    d=json.load(sys.stdin)
except Exception:
    print("  resposta não-JSON: WAF provavelmente rejeitou o token"); sys.exit(1)
hits=d.get("result",{}).get("hits",{}).get("hits",[])
if not hits:
    print("  nenhum resultado"); sys.exit(0)
for h in hits:
    s=h.get("_source",{})
    print("  ---")
    print("  titulo :",str(s.get("titulo",""))[:100])
    print("  classe :",s.get("classe",""),s.get("numero",""))
    print("  data   :",s.get("dataPublicacao",""))
    print("  docID  :",s.get("inteiro_teor_url","") or s.get("idDocumento",""))
'
  warn "pegue o docID e rode: baixar_fontes.sh stf-doc <docID> <nome.pdf> <pasta>"
}

# ---------------------------------------------------------------------------
stf_doc() {
  local docid="${1:-}" nome="${2:-}" pasta="${3:-$D04}"
  [[ -z "$docid" || -z "$nome" ]] && {
    err 'uso: baixar_fontes.sh stf-doc <docID> <nome-do-arquivo.pdf> [pasta]'
    warn "exemplo: stf-doc 812345678 STF_AP-2668_Preventiva_2025-11-22.pdf $D04"
    return 1
  }
  if [[ -z "${AWS_WAF_TOKEN:-}" ]]; then
    err "AWS_WAF_TOKEN não está definido — veja o alvo stf-busca."
    return 1
  fi
  log "INTEIRO TEOR STF — docID $docid"
  mkdir -p "$pasta"
  local destino="$pasta/$nome"
  if [[ -s "$destino" ]]; then warn "já existe, preservado: $destino"; return 0; fi
  curl -fsSL --max-time 300 -A "$UA" \
    -H "Cookie: aws-waf-token=${AWS_WAF_TOKEN}" \
    -o "$destino.parcial" \
    "https://redir.stf.jus.br/paginadorpub/paginador.jsp?docTP=TP&docID=${docid}" || {
      rm -f "$destino.parcial"; err "download falhou"; return 1; }
  if [[ $(stat -c%s "$destino.parcial" 2>/dev/null || echo 0) -lt 10000 ]]; then
    err "arquivo pequeno demais — o WAF devolveu 202 vazio. Renove o token."
    rm -f "$destino.parcial"; return 1
  fi
  mv "$destino.parcial" "$destino"
  ok "$destino  ($(du -h "$destino" | cut -f1))"
  warn "depois: rode 'conferir' e registre a peça em scripts/gerar_codebook.py"
}

# ---------------------------------------------------------------------------
tse() {
  cat <<'FIM'

ACÓRDÃO DO TSE — PT-03E  ·  ✅ RESOLVIDO EM 16/08/2026, SEM CAPTCHA
==================================================================

RCand 0600903-50.2018.6.00.0000 — indeferimento do registro de candidatura
de Lula, rel. min. Luís Roberto Barroso, acórdão de 1º/09/2018.

Arquivo: Fontes/01_Arco-judicial_2017-2021/TSE_RCand-0600903-50_Acordao_2018-09-01.html

COMO FOI OBTIDO — a rota que funciona é o endpoint de documento da Consulta
Unificada PJe, que NÃO exige captcha:

  https://consultaunificadapje.tse.jus.br/consulta-publica-unificada/documento
    ?extensaoArquivo=text/html
    &path=tse/2018/10/15/16/27d7840a9d81d321d006c4131443ab64a984b9e1

DUAS CORREÇÕES ao que este script dizia antes:

  1. O captcha do TSE é hCAPTCHA, não reCAPTCHA. O buscador de jurisprudência
     carrega js.hcaptcha.com/1/api.js; não há reCAPTCHA em lugar nenhum.

  2. O documento é servido em HTML, não em PDF. O parâmetro extensaoArquivo
     muda só o Content-Type: pedir application/pdf devolve o mesmo HTML.

PARA OUTROS PROCESSOS DO TSE, o caminho é:

  a) descobrir o `path` do documento. O buscador jurisprudencia.tse.jus.br
     serve isso, mas a API dele (sjur-pesquisa-api.tse.jus.br) exige o token
     antirrobô — sem ele responde {"mensagem":"Falha na verificação antirrobô."}.
     NÃO tente contornar. Duas alternativas honestas:
       - resolver o hCaptcha no navegador e copiar o link do documento; ou
       - achar o `path` por busca web, que foi o que funcionou aqui.

  b) com o `path` em mãos, baixar direto:
       curl -sSL -A "Mozilla/5.0" -o saida.html          "https://consultaunificadapje.tse.jus.br/consulta-publica-unificada/documento?extensaoArquivo=text/html&path=<PATH>"

SE PRECISAR MESMO PASSAR PELO BUSCADOR (passo a passo manual):
  1. abra https://jurisprudencia.tse.jus.br/
  2. digite o número do processo no campo de pesquisa
  3. resolva o hCaptcha quando ele aparecer — é você quem resolve, não o script
  4. abra o resultado e clique em "Inteiro teor"
  5. copie o endereço do documento (tem o parâmetro `path=`) e use no curl acima,
     ou salve direto pelo navegador

FIM
}

# ---------------------------------------------------------------------------
# Confere o que chegou: paginação real e presença de camada de texto.
# pdfinfo subconta grosseiramente estes PDFs (relatou 84 para um de 464);
# por isso a contagem é feita com PyPDF2.
conferir() {
  log "CONFERÊNCIA DO CORPUS"
  python -X utf8 - <<'PY'
from pathlib import Path
try:
    from PyPDF2 import PdfReader
except ImportError:
    raise SystemExit("  PyPDF2 ausente:  pip install PyPDF2")
tot = n = 0
for p in sorted(Path("Fontes").rglob("*.pdf")):
    try:
        r = PdfReader(str(p)); pg = len(r.pages)
        # Amostra ao longo do documento, nunca só a página 1: capa costuma ser
        # imagem sem texto e produz falso alarme de "precisa de OCR".
        amostra = sorted({int(pg * f) for f in (0.05, 0.25, 0.5, 0.75, 0.95)} & set(range(pg)))
        com = sum(1 for i in amostra
                  if len((r.pages[i].extract_text() or "").strip()) > 40)
        marca = "texto ({}/{})".format(com, len(amostra)) if com else "SEM TEXTO — precisa de OCR"
        print("  {:>5} p.  {:<28}  {}".format(pg, marca, p.as_posix()))
        tot += pg; n += 1
    except Exception as e:
        print("  ERRO  {}: {}".format(p.name, str(e)[:60]))
print("\n  {} PDFs, {} páginas".format(n, tot))
print("  inventário de 16/08/2026: 22 PDFs, 6928 páginas")
PY
}

# ---------------------------------------------------------------------------
case "${1:-listar}" in
  listar|"")      listar ;;
  agencia)        agencia ;;
  stf-noticias)   stf_noticias ;;
  stf-busca)      shift; stf_busca "$@" ;;
  stf-doc)        shift; stf_doc "$@" ;;
  tse)            tse ;;
  conferir)       conferir ;;
  *)              err "alvo desconhecido: $1"; listar; exit 1 ;;
esac
