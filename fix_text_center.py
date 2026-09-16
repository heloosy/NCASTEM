import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_text_center = '.text-center { text-align: center; }'
new_text_center = '''.text-center, .text-center p, .text-center h1, .text-center h2, .text-center h3, .text-center h4, .text-center h5, .text-center h6 { 
    text-align: center !important; 
}
.hero-subtitle {
    text-align: center !important;
}'''

css = css.replace(old_text_center, new_text_center)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
