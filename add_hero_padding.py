import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

mobile_hero_padding = '''
@media (max-width: 768px) {
    .hero {
        padding-top: 120px !important;
        padding-bottom: 60px !important;
    }
}
'''
css = css + mobile_hero_padding

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

