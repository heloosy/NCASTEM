import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace 1
old_1 = "<li>Full paper submission required in IEEE format.</li>"
new_1 = '<li>Full paper submission required in <a href="https://drive.google.com/file/d/1fPeRSiXjubTbLYVIqIH-_vI517KnwptC/view?usp=sharing" target="_blank" style="color: var(--accent); text-decoration: underline;">IEEE format</a>.</li>'
html = html.replace(old_1, new_1)

# Replace 2
old_2 = "<p>Format your full paper in IEEE format. Ensure original work, strictly &lt;15% plagiarism, and not published elsewhere.</p>"
new_2 = '<p>Format your full paper in <a href="https://drive.google.com/file/d/1fPeRSiXjubTbLYVIqIH-_vI517KnwptC/view?usp=sharing" target="_blank" style="color: var(--accent); text-decoration: underline;">IEEE format</a>. Ensure original work, strictly &lt;15% plagiarism, and not published elsewhere.</p>'
html = html.replace(old_2, new_2)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

