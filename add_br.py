import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_org = 'Department of AIML and Department of ISE, T. John Institute of Technology, in association with IIC'
new_org = 'Department of AIML and Department of ISE, T. John Institute of Technology,<br> in association with IIC'

html = html.replace(old_org, new_org)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

