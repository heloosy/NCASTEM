import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_title = '''.hero-title {
    font-size: 7.5rem;
    font-weight: 900;
    letter-spacing: -1px;
    line-height: 1;
    margin-bottom: 1.5rem;
    text-transform: uppercase;
    font-family: var(--font-body);
    color: #0b1120;
}'''

new_title = '''.hero-title {
    font-size: 7.5rem;
    font-weight: 900;
    letter-spacing: -1px;
    line-height: 1;
    margin-bottom: 1.5rem;
    text-transform: uppercase;
    font-family: var(--font-body);
    
    /* Beautiful Gradient Text */
    background: linear-gradient(135deg, var(--accent) 0%, #3b82f6 40%, var(--accent-alt) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
}'''

if old_title in css:
    css = css.replace(old_title, new_title)
else:
    # Let's do a fallback replacement just in case
    pattern = r'\.hero-title\s*\{[^}]*color:\s*#0b1120;\s*\}'
    css = re.sub(pattern, new_title, css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
