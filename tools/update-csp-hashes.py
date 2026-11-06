#!/usr/bin/env python3
"""Refresh or verify the CSP hashes for inline scripts in published HTML."""
import argparse
import base64
import hashlib
from html.parser import HTMLParser
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
HEADERS = ROOT / '_headers'

class Scripts(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.capture = False
        self.parts = []
        self.scripts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'script' and 'src' not in attrs and attrs.get('type', '').lower() not in ('application/ld+json', 'application/json'):
            self.capture = True
            self.parts = []

    def handle_data(self, data):
        if self.capture:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if tag == 'script' and self.capture:
            self.scripts.append(''.join(self.parts))
            self.capture = False

def inline_hashes():
    hashes = set()
    for path in ROOT.rglob('*.html'):
        if '.git' in path.parts:
            continue
        parser = Scripts()
        parser.feed(path.read_text(encoding='utf-8'))
        for source in parser.scripts:
            digest = base64.b64encode(hashlib.sha256(source.encode()).digest()).decode()
            hashes.add("'sha256-" + digest + "'")
    return sorted(hashes)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='report stale hashes without modifying files')
    args = parser.parse_args()
    text = HEADERS.read_text(encoding='utf-8')
    match = re.search(r"(?m)^(  Content-Security-Policy: .*?script-src )([^;]+)", text)
    if not match:
        raise SystemExit('Could not find the script-src directive in _headers')
    sources = [x for x in match.group(2).split() if not x.startswith("'sha256-")]
    updated = text[:match.start(2)] + ' '.join(sources + inline_hashes()) + text[match.end(2):]
    if args.check:
        if updated != text:
            raise SystemExit('CSP hashes are stale; run python3 tools/update-csp-hashes.py')
        print('CSP inline script hashes match the HTML files.')
    else:
        HEADERS.write_text(updated, encoding='utf-8')
        print('Updated CSP inline script hashes in _headers.')

if __name__ == '__main__':
    main()
