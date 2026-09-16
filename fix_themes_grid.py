import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Force exactly 3 columns in the themes grid on desktop
css = css.replace('grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));', 'grid-template-columns: repeat(3, 1fr);')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

