import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add meta-item mobile fix
mobile_fix = '''    .hero-meta { flex-direction: column; gap: 1.5rem; }
    .meta-item {
        flex-direction: column;
        text-align: center;
        gap: 0.5rem;
    }'''

css = css.replace('.hero-meta { flex-direction: column; gap: 1rem; }', mobile_fix)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
