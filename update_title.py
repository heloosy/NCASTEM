import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_title = '''<h1 class="hero-title fade-up delay-2">
                    NCASTEM
                </h1>'''
new_title = '''<h1 class="hero-title fade-up delay-2">
                    NCASTEM 2K26
                </h1>'''

html = html.replace(old_title, new_title)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

