import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_benefits = '<div class="benefits-grid mt-4 pt-3 border-top fade-up">'
new_benefits = '''<div class="fade-up mt-5 pt-5 border-top" style="text-align: center;">
                <h3 style="font-family: var(--font-heading); font-size: 1.8rem; color: var(--text-main); margin-bottom: 2.5rem; font-weight: 700;">Why Participate?</h3>
            </div>
            <div class="benefits-grid fade-up">'''

html = html.replace(old_benefits, new_benefits)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

