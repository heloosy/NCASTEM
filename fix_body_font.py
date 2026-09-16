import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Change body back to Inter
css = css.replace("body {\n    font-family: 'Montserrat', sans-serif;", "body {\n    font-family: var(--font-body);")

# Change subtitle back to Inter
css = css.replace(".hero-subtitle {\n    font-family: 'Montserrat', sans-serif;", ".hero-subtitle {\n    font-family: var(--font-body);")

# Change benefits back to Inter
css = css.replace(".benefit-item h5 {\n    color: var(--text-main);\n    letter-spacing: 1px;\n    margin-bottom: 1rem;\n    font-size: 0.95rem;\n    font-family: 'Montserrat', sans-serif;", ".benefit-item h5 {\n    color: var(--text-main);\n    letter-spacing: 1px;\n    margin-bottom: 1rem;\n    font-size: 0.95rem;\n    font-family: var(--font-body);")

# Change countdown back to Inter (or maybe Montserrat is cool for numbers? Let's leave Montserrat for countdown numbers!)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
