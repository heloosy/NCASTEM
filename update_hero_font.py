import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('font-size: 7.5rem;', 'font-size: min(9vw, 7rem);')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

