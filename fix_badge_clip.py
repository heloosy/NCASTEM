import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_css = '''
.pricing-grid {
    display: flex !important;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    gap: 2rem;
    padding-bottom: 2rem;
    scrollbar-width: none; /* Firefox */
}'''

new_css = '''
.pricing-grid {
    display: flex !important;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    gap: 2rem;
    padding-top: 2rem;
    padding-bottom: 2rem;
    scrollbar-width: none; /* Firefox */
}'''

css = css.replace(old_css, new_css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

