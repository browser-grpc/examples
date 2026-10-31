#!/usr/bin/env python3
"""Check every URL in README.md answers (stdlib only).
403 counts as alive (bot walls); anything else >= 400 fails."""
import re, sys, urllib.request

text = open('README.md').read()
urls = sorted(set(re.findall(r'https://[^\s)\]]+', text)))
bad = []
for u in urls:
    try:
        req = urllib.request.Request(u, method='HEAD',
                                     headers={'User-Agent': 'link-check'})
        code = urllib.request.urlopen(req, timeout=20).status
    except Exception as e:
        code = getattr(e, 'code', 0) or 0
        if code == 403:
            code = 200
        if code == 0 or code >= 400:
            bad.append((u, code or str(e)))
    print(code, u)
print('checked', len(urls), 'links;', len(bad), 'bad')
sys.exit(1 if bad else 0)
