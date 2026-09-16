import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Footer text
old_footer = '<p class="mt-3">A premier Multidisciplinary National Conference hosted by T. John Institute of Technology, in association with IIC.</p>'
new_footer = '<p class="mt-3">A premier Multidisciplinary National Conference hosted by Department of AIML & ISE, T. John Institute of Technology.</p>'
html = html.replace(old_footer, new_footer)

# 2. Update IEEE format link
old_link = '<a href="https://drive.google.com/file/d/1fPeRSiXjubTbLYVIqIH-_vI517KnwptC/view?usp=sharing" target="_blank" style="color: var(--accent); text-decoration: underline;">IEEE format</a>'
new_link = '<a href="https://drive.google.com/file/d/1pGefPEcUm4n6PI62njn-oJFyHeSlZsuM/view?usp=drive_link" target="_blank" style="color: var(--accent); text-decoration: underline;">IEEE format</a>'
html = html.replace(old_link, new_link)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

