import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('.benefit-item h5 {\n    color: var(--text-main);\n    letter-spacing: 1px;\n    margin-bottom: 1rem;\n}',
'''.benefit-item h5 {
    color: var(--text-main);
    letter-spacing: 1px;
    margin-bottom: 1rem;
    font-size: 0.95rem;
    font-family: var(--font-body);
    font-weight: 700;
}''')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('class="benefits-grid mt-5 pt-5 border-top fade-up"', 'class="benefits-grid mt-4 pt-3 border-top fade-up"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
