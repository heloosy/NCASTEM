import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Limit hero height to fix the massive zooming on tall mobile screens running desktop mode
css = css.replace('min-height: 100vh;', 'min-height: 100vh;\n    max-height: 900px;')

# 2. Force exactly 4 columns in the pricing grid on desktop
css = css.replace('grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));', 'grid-template-columns: repeat(4, 1fr);')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

