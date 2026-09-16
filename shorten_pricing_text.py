import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_li = '<li>Will publish in UGC Care listed journals (Additional Charges) and Conference Proceedings with ISBN.</li>'
new_li = '<li>Proceedings with ISBN <br><small style="color: var(--accent-alt); font-weight: 600;">+ UGC Care (Additional Charges)</small></li>'

html = html.replace(old_li, new_li)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

