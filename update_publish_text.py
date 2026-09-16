import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_text = '''<p>Deliver your research. Published in UGC Care listed journals (Additional Charges) and Conference Proceedings with ISBN.</p>'''
new_text = '''<p>Deliver your research. Papers will be published in UGC Care listed journals (Additional Charges) and Conference Proceedings with ISBN.</p>'''
html = html.replace(old_text, new_text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

