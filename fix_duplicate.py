import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the duplicate ISE card (the old one)
duplicate_regex = r'<div class="dept-card fade-up delay-1">\s*<i class="fas fa-sitemap dept-icon text-accent-alt"></i>\s*<h3>Department of ISE</h3>\s*<p class="text-muted">Established in 2007 with an intake of 60 students, the Information Science Department offers B.E under VTU, recognized by AICTE. It aims to transform students into potential global leaders.</p>\s*<div class="dept-vision">\s*<h5><i class="far fa-eye text-accent-alt"></i> Vision</h5>\s*<p class="text-muted">To achieve excellence in delivering quality education of global standards, coupled with innovative practices using advanced technology.</p>\s*</div>\s*</div>'

html = re.sub(duplicate_regex, '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

