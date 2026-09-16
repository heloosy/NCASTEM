import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_link = '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">'
new_link = '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Inter:wght@300;400;500;600;700&family=Montserrat:wght@800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">'

html = html.replace(old_link, new_link)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

