import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_text = '''                    T. John Institute of Technology, in association with IIC'''
new_text = '''                    Department of AIML and Department of ISE, <br> T. John Institute of Technology, in association with IIC'''

html = html.replace(old_text, new_text, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

