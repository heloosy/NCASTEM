import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_fonts = 'family=Space+Grotesk:wght@500;700&display=swap'
new_fonts = 'family=Space+Grotesk:wght@500;700&family=Montserrat:wght@700;800;900&family=Playfair+Display:wght@700;900&display=swap'

html = html.replace(old_fonts, new_fonts)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I will change the hero title to Montserrat for a very modern, punchy, wide tech look.
old_title_font = 'font-family: var(--font-body);'
new_title_font = "font-family: 'Montserrat', sans-serif;"

css = css.replace(old_title_font, new_title_font)

# Fix muddy gradient
old_grad = 'background: linear-gradient(135deg, var(--accent) 0%, #3b82f6 40%, var(--accent-alt) 100%);'
new_grad = 'background: linear-gradient(135deg, #1e3a8a 0%, #4f46e5 45%, #ea580c 80%, #d68910 100%);'
css = css.replace(old_grad, new_grad)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

