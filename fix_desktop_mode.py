import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Revert 992px back to 768px
css = css.replace('@media (max-width: 992px) {', '@media (max-width: 768px) {')

# 2. Remove the 1024px media query that stacked leadership cards
old_1024 = '''@media (max-width: 1024px) {
    .editorial-heading { font-size: 3rem; }
    .hero-title { font-size: 4.5rem; }
    .about-grid { gap: 3rem; }
    .leadership-premium-grid { grid-template-columns: 1fr; }
}'''
css = css.replace(old_1024, '')

# 3. Fix the minmax values so 4 items fit in a 980px viewport
css = css.replace('minmax(280px, 1fr)', 'minmax(220px, 1fr)') # Pricing grid
css = css.replace('minmax(350px, 1fr)', 'minmax(280px, 1fr)') # Themes grid
css = css.replace('minmax(250px, 1fr)', 'minmax(200px, 1fr)') # Profile grid

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

