import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace font-size and add white-space: nowrap
old_css = '''    font-size: min(9vw, 7rem);
    font-weight: 900;'''
new_css = '''    font-size: clamp(2rem, 8vw, 7rem);
    font-weight: 900;
    white-space: nowrap;'''
css = css.replace(old_css, new_css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

