import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<h3 class="tier-title">Review & Technical</h3>', '<h3 class="tier-title">Review and Technical Committee</h3>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

