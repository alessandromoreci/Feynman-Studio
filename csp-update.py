#!/usr/bin/env python3
"""Aggiorna la Content-Security-Policy di feynman_studio.html.

La pagina permette l'esecuzione dei soli script che contiene, riconosciuti dalla loro impronta (sha256).
Dopo OGNI modifica a un blocco <script> della pagina bisogna rieseguire questo programma, altrimenti il
browser rifiuta lo script modificato e l'app non parte:

    python3 csp-update.py            # aggiorna feynman_studio.html
    python3 csp-update.py --check    # controlla soltanto (codice di uscita 1 se non è aggiornata)
"""
import base64, hashlib, re, sys
from pathlib import Path

FILE = Path(__file__).with_name("feynman_studio.html")
HOSTS = "https://api.anthropic.com https://generativelanguage.googleapis.com https://api.openai.com"
MARK = '<meta http-equiv="Content-Security-Policy"'


def scripts(html):
    out, i = [], 0
    while True:
        m = re.compile(r"<script\b[^>]*>", re.I).search(html, i)
        if not m:
            return out
        j = html.lower().index("</script", m.end())
        out.append(html[m.end():j])
        i = j


def policy(html):
    hashes = " ".join("'sha256-" + base64.b64encode(hashlib.sha256(t.encode("utf-8")).digest()).decode() + "'" for t in scripts(html))
    return ("default-src 'none'; script-src " + hashes + "; style-src 'unsafe-inline'; img-src 'self' data: blob:; font-src data:; "
            "media-src data: blob:; connect-src " + HOSTS + " data: blob:; worker-src blob:; manifest-src 'self' data:; "
            "object-src 'none'; frame-src 'none'; base-uri 'none'; form-action 'none'")


def main():
    html = FILE.read_text(encoding="utf-8")
    body = re.sub(r"\n?" + re.escape(MARK) + r'[^>]*>', "", html)           # la pagina senza la riga della policy
    meta = MARK + ' content="' + policy(body) + '">'
    new = body.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">\n' + meta, 1)
    assert MARK in new, "non trovo <meta charset> in testa alla pagina"
    if "--check" in sys.argv:
        ok = new == html
        print("CSP aggiornata" if ok else "CSP NON aggiornata: esegui python3 csp-update.py")
        sys.exit(0 if ok else 1)
    FILE.write_text(new, encoding="utf-8")
    print(f"CSP aggiornata: {len(scripts(body))} script riconosciuti")


if __name__ == "__main__":
    main()
