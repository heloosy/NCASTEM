import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('.theme-card:hover .theme-num {\n    color: rgba(30, 58, 138, 0.1);\n    transform: scale(1.1);\n}',
'''.theme-card:hover .theme-num {
    color: rgba(214, 137, 16, 0.15); /* Gold ghost number */
    transform: scale(1.4) translate(-10px, 5px);
}''')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
