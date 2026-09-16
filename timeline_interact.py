import re
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('.time-node:hover .node-dot {\n    border-color: var(--accent-alt);\n    background-color: var(--accent-alt);\n    box-shadow: 0 0 15px rgba(30, 58, 138, 0.3);\n}',
'''.time-node:hover .node-dot {
    border-color: var(--accent-alt);
    background-color: var(--accent-alt);
    box-shadow: 0 0 15px rgba(30, 58, 138, 0.3);
    transform: translateX(-50%) scale(1.4);
}''')

css = css.replace('.node-highlight .node-dot {\n    border-color: var(--accent-alt);\n    background-color: var(--accent-alt);\n    box-shadow: 0 0 15px rgba(30, 58, 138, 0.3);\n}',
'''.node-highlight .node-dot {
    border-color: var(--accent-alt);
    background-color: var(--accent-alt);
    box-shadow: 0 0 20px rgba(214, 137, 16, 0.5);
    transform: translateX(-50%) scale(1.2);
}''')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
