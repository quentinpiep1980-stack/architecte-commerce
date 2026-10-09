# -*- coding: utf-8 -*-
"""Serveur local imitant cleanUrls de Vercel : /page -> dist/page.html. Usage : python3 -I tools/serve.py [port]"""
import http.server, pathlib, sys, functools
DIST = pathlib.Path(__file__).resolve().parent.parent / 'dist'
class H(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        p = path.split('?')[0].split('#')[0]
        f = DIST / p.lstrip('/')
        if p == '/' : return str(DIST / 'index.html')
        if f.is_file(): return str(f)
        if (DIST / (p.lstrip('/') + '.html')).is_file(): return str(DIST / (p.lstrip('/') + '.html'))
        return str(DIST / '404.html')
    def log_message(self, *a): pass
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
http.server.ThreadingHTTPServer(('127.0.0.1', port), H).serve_forever()
