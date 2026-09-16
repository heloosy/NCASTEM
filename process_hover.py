import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('.process-step:hover {\n    border-top-color: var(--accent-alt);\n}',
'''.process-step:hover {
    border-top-color: var(--accent-alt);
    transform: translateY(-5px);
}''')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
