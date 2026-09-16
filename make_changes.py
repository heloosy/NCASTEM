import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Organized By text
html = html.replace('<p>T. John Institute of Technology, in association with IIC</p>', '<p>Department of AIML & ISE, T. John Institute of Technology</p>')

# 2. Date
html = html.replace('<div class="node-date">07 SEP 2026</div>', '<div class="node-date">20 SEP 2026</div>')

# 3. Format link
old_prepare = '<p>Format your full paper in <a href="https://drive.google.com/file/d/1fPeRSiXjubTbLYVIqIH-_vI517KnwptC/view?usp=sharing" target="_blank" style="color: var(--accent); text-decoration: underline;">IEEE format</a>. Ensure original work, strictly &lt;15% plagiarism, and not published elsewhere.</p>'
new_prepare = '<p>Format your full paper in the <a href="https://drive.google.com/file/d/1pGefPEcUm4n6PI62njn-oJFyHeSlZsuM/view?usp=sharing" target="_blank" style="color: var(--accent); text-decoration: underline;">attached format</a>. Ensure original work, strictly &lt;15% plagiarism, and not published elsewhere.</p>'
html = html.replace(old_prepare, new_prepare)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

