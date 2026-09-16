import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Modify themes section padding
html = html.replace('<section id="themes" class="section themes-section">', '<section id="themes" class="section themes-section" style="padding-bottom: 3rem;">')

# Modify dates section padding
html = html.replace('<section id="dates" class="section dates-section">', '<section id="dates" class="section dates-section" style="padding-top: 2rem;">')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
