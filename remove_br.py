import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Organizer
old_org = 'Department of AIML and Department of ISE, <br> T. John Institute of Technology, in association with IIC'
new_org = 'Department of AIML and Department of ISE, T. John Institute of Technology, in association with IIC'
html = html.replace(old_org, new_org)

# Subtitle
old_sub = 'Multidisciplinary National Conference on Advances in<br>\n                    Science, Technology, Engineering, and Management'
new_sub = 'Multidisciplinary National Conference on Advances in Science, Technology, Engineering, and Management'
html = html.replace(old_sub, new_sub)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

