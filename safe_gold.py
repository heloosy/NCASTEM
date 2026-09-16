import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

def replace_in_class(class_name, old_val, new_val, css_text):
    # Regex to find the class block
    pattern = r'(' + re.escape(class_name) + r'\s*\{[^}]*)' + re.escape(old_val)
    return re.sub(pattern, r'\1' + new_val, css_text)

# We want to change the color/background in specific classes to var(--accent-alt)
classes_to_update = [
    '.hero-eyebrow',
    '.meta-item i',
    '.stat-icon',
    '.card-icon',
    '.time-node:hover .node-dot',
    '.node-highlight .node-dot',
    '.process-step:hover',
    '.pricing-card.popular',
    '.faq-question i',
    '.cta-subheading',
    '.footer-contact-col li i',
    '.logo-year',
    '.clean-list li::before'
]

for cls in classes_to_update:
    css = replace_in_class(cls, 'var(--accent)', 'var(--accent-alt)', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
