import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Remove max-height: 900px from the base .hero
css = css.replace('max-height: 900px;', '')

# 2. Add it back ONLY for desktop via a media query at the bottom
desktop_hero_fix = '''
@media (min-width: 769px) {
    .hero {
        max-height: 900px;
    }
}
'''
css = css + desktop_hero_fix

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

