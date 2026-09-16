import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add width: 100% to html and body
old_html = '''html {
    scroll-behavior: smooth;
    font-size: 16px;
}'''

new_html = '''html, body {
    width: 100%;
    max-width: 100vw;
    overflow-x: hidden;
}
html {
    scroll-behavior: smooth;
    font-size: 16px;
}'''

css = css.replace(old_html, new_html)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

