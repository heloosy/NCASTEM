import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Change the mobile media query threshold for the critical nav and grids
css = css.replace('@media (max-width: 768px) {', '@media (max-width: 992px) {')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

