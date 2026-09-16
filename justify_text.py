import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add p { text-align: justify; } to base styles
base_styles = '''/* Reset & Base */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: var(--font-body);
    background-color: var(--bg-main);
    color: var(--text-main);
    line-height: 1.6;
    overflow-x: hidden;
}

p {
    text-align: justify;
}'''

# Replace the base styles section
old_base_styles = '''/* Reset & Base */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: var(--font-body);
    background-color: var(--bg-main);
    color: var(--text-main);
    line-height: 1.6;
    overflow-x: hidden;
}'''

if old_base_styles in css:
    css = css.replace(old_base_styles, base_styles)
else:
    # Fallback if the exact string doesn't match
    css = css.replace('overflow-x: hidden;\n}', 'overflow-x: hidden;\n}\n\np {\n    text-align: justify;\n}')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
