import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_html = '''                <div class="hero-eyebrow fade-up">NATIONAL CONFERENCE &middot; 2026</div>
                
                <h1 class="hero-title fade-up delay-1">'''

new_html = '''                <p class="hero-organizer fade-up" style="font-size: 1rem; font-weight: 700; letter-spacing: 1.5px; color: #334155; margin-bottom: 0.8rem; text-transform: uppercase; line-height: 1.5;">
                    T. John Institute of Technology, <br>in association with IIC
                </p>
                <div class="hero-eyebrow fade-up delay-1" style="margin-bottom: 1.5rem;">NATIONAL CONFERENCE &middot; 2026</div>
                
                <h1 class="hero-title fade-up delay-2">'''

html = html.replace(old_html, new_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
