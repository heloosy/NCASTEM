import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make section titles underline gold
css = css.replace('background: var(--accent);', 'background: var(--accent-alt);', 1) 
# wait, there are multiple 'background: var(--accent);'

# Let's replace specific classes
css = css.replace('.section-title::after {\n    content: \'\';\n    position: absolute;\n    bottom: 0;\n    left: 0;\n    width: 60px;\n    height: 2px;\n    background: var(--accent);\n}', '.section-title::after {\n    content: \'\';\n    position: absolute;\n    bottom: 0;\n    left: 0;\n    width: 60px;\n    height: 2px;\n    background: var(--accent-alt);\n}')

# Make popular badge gold with black text
css = css.replace('.popular-badge {\n    position: absolute;\n    top: -12px;\n    left: 50%;\n    transform: translateX(-50%);\n    background-color: var(--accent);\n    color: #ffffff;\n    padding: 0.3rem 1rem;', '.popular-badge {\n    position: absolute;\n    top: -12px;\n    left: 50%;\n    transform: translateX(-50%);\n    background-color: var(--accent-alt);\n    color: #000000;\n    padding: 0.3rem 1rem;')

# Make step-num gold
css = css.replace('.step-num {\n    font-family: var(--font-heading);\n    font-size: 1rem;\n    color: var(--accent);\n    margin-bottom: 1rem;\n}', '.step-num {\n    font-family: var(--font-heading);\n    font-size: 1rem;\n    color: var(--accent-alt);\n    margin-bottom: 1rem;\n}')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
