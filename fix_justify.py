import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the global p { text-align: justify; }
css = css.replace('p {\n    text-align: justify;\n}', '')

# Add justify to specific body copy classes
targeted_justify = '''.lead-text, 
.text-muted, 
.benefit-item p, 
.presentation-card p, 
.process-step p, 
.faq-answer p, 
.tjit-content p, 
.dept-card p, 
.vm-card p, 
.about-right p {
    text-align: justify;
}
'''

# Find a good place to put it, like after body { ... }
if 'overflow-x: hidden;\n}' in css:
    css = css.replace('overflow-x: hidden;\n}', 'overflow-x: hidden;\n}\n\n' + targeted_justify)

# Ensure CTA is centered
css = css.replace('.cta-heading {', '.cta-heading {\n    text-align: center;')
css = css.replace('.cta-subheading {', '.cta-subheading {\n    text-align: center;')

# Ensure Pricing card text is centered
css = css.replace('.pricing-card {', '.pricing-card {\n    text-align: center;')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
