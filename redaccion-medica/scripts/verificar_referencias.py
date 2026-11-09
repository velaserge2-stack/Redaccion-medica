#!/usr/bin/env python3
"""Verifica DOI y PMID de una lista de referencias contra Crossref y PubMed.

Uso:
    python3 verificar_referencias.py referencias.txt
    python3 verificar_referencias.py --doi 10.1136/bmj-2024-081123 --pmid 40228833

Requisitos: Python 3.8+, solo biblioteca estándar, acceso a internet a
api.crossref.org y eutils.ncbi.nlm.nih.gov. Si la sesión no tiene acceso,
cada referencia sale como "No verificable" (nunca como verificada).

Qué hace:
  - Extrae DOI (10.xxxx/...) y PMID ("PMID: 12345678") del texto.
  - Consulta Crossref (DOI) y PubMed E-utilities (PMID).
  - Devuelve una tabla Markdown con: identificador, estado, título, revista,
    año, primer autor y alertas (p. ej., publicación retractada en PubMed).

Qué NO hace:
  - No confirma que la referencia respalde la frase donde se cita: eso exige
    leer el artículo.
  - No corrige la referencia del usuario: solo muestra lo que dice la fuente
    para que el autor compare.
"""
import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

USER_AGENT = "redaccion-medica-skill/0.4 (verificacion de referencias)"
DOI_RE = re.compile(r"\b(10\.\d{4,9}/[^\s\"<>]+)", re.IGNORECASE)
PMID_RE = re.compile(r"PMID\s*:?\s*(\d{1,9})", re.IGNORECASE)


def fetch_json(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def clean_doi(doi):
    return doi.rstrip(".,;)]}")


def extract_ids(text):
    dois = []
    for m in DOI_RE.finditer(text):
        d = clean_doi(m.group(1))
        if d.lower() not in [x.lower() for x in dois]:
            dois.append(d)
    pmids = []
    for m in PMID_RE.finditer(text):
        if m.group(1) not in pmids:
            pmids.append(m.group(1))
    return dois, pmids


def check_doi(doi, fetch=fetch_json):
    row = {"id": "DOI " + doi, "estado": "", "titulo": "", "revista": "",
           "anio": "", "autor": "", "alertas": []}
    if doi.startswith("10.5555/"):
        row["alertas"].append("prefijo 10.5555 es de pruebas de Crossref")
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/")
    try:
        msg = fetch(url)["message"]
    except urllib.error.HTTPError as e:
        row["estado"] = "No encontrado (HTTP %s)" % e.code if e.code == 404 else "No verificable (HTTP %s)" % e.code
        return row
    except Exception as e:  # red bloqueada, tiempo agotado, JSON inválido
        row["estado"] = "No verificable (%s)" % type(e).__name__
        return row
    row["estado"] = "Existe en Crossref"
    row["titulo"] = (msg.get("title") or [""])[0]
    row["revista"] = (msg.get("container-title") or [""])[0]
    parts = (msg.get("issued") or {}).get("date-parts") or [[None]]
    row["anio"] = str(parts[0][0] or "")
    authors = msg.get("author") or []
    if authors:
        a = authors[0]
        row["autor"] = (a.get("family") or a.get("name") or "") + (" " + a["given"][0] if a.get("given") else "")
    for upd in msg.get("update-to") or []:
        row["alertas"].append("actualización registrada: %s" % upd.get("type", "?"))
    if msg.get("type") == "retraction":
        row["alertas"].append("el DOI corresponde a un aviso de retractación")
    return row


def check_pmid(pmid, fetch=fetch_json):
    row = {"id": "PMID " + pmid, "estado": "", "titulo": "", "revista": "",
           "anio": "", "autor": "", "alertas": []}
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id="
           + pmid)
    try:
        data = fetch(url)
    except Exception as e:
        row["estado"] = "No verificable (%s)" % type(e).__name__
        return row
    rec = (data.get("result") or {}).get(pmid)
    if not rec or "error" in rec:
        row["estado"] = "No encontrado en PubMed"
        return row
    row["estado"] = "Existe en PubMed"
    row["titulo"] = rec.get("title", "")
    row["revista"] = rec.get("source", "")
    row["anio"] = (rec.get("pubdate") or "")[:4]
    authors = rec.get("authors") or []
    if authors:
        row["autor"] = authors[0].get("name", "")
    pubtypes = rec.get("pubtype") or []
    if "Retracted Publication" in pubtypes:
        row["alertas"].append("PUBLICACIÓN RETRACTADA")
    if "Retraction of Publication" in pubtypes:
        row["alertas"].append("es un aviso de retractación")
    for aid in rec.get("articleids") or []:
        if aid.get("idtype") == "doi":
            row["alertas"].append("DOI en PubMed: " + aid.get("value", ""))
    return row


def to_markdown(rows):
    out = ["| Identificador | Estado | Primer autor | Año | Revista | Título | Alertas |",
           "|---|---|---|---|---|---|---|"]
    for r in rows:
        cells = [r["id"], r["estado"], r["autor"], r["anio"], r["revista"],
                 r["titulo"], "; ".join(r["alertas"])]
        out.append("| " + " | ".join(c.replace("|", "/") for c in cells) + " |")
    out.append("")
    out.append("Compare cada fila con la referencia del manuscrito. Una referencia "
               "'No verificable' no se da por buena: se marca [VERIFICAR].")
    return "\n".join(out)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("archivo", nargs="?", help="Archivo de texto con las referencias")
    p.add_argument("--doi", action="append", default=[])
    p.add_argument("--pmid", action="append", default=[])
    args = p.parse_args(argv)
    dois, pmids = list(args.doi), list(args.pmid)
    if args.archivo:
        with open(args.archivo, encoding="utf-8") as f:
            d, pm = extract_ids(f.read())
        dois += d
        pmids += pm
    if not dois and not pmids:
        print("No se encontraron DOI ni PMID. Las referencias sin identificador "
              "deben buscarse por título en PubMed o Crossref.", file=sys.stderr)
        return 1
    rows = [check_doi(d) for d in dois] + [check_pmid(x) for x in pmids]
    print(to_markdown(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
