import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace in Pricing Cards
old_li = '<li>Proceeding Publication</li>'
new_li = '<li>Will publish in UGC Care listed journals (Additional Charges) and Conference Proceedings with ISBN.</li>'
html = html.replace(old_li, new_li)

# Replace in FAQ
old_faq = '<p>The registration fee includes full access to the conference, proceeding publication, and GST. Extra team members can be added for a small additional fee.</p>'
new_faq = '<p>The registration fee includes full access to the conference, conference proceedings with ISBN, and GST. Publication in UGC Care listed journals is available for additional charges.</p>'
html = html.replace(old_faq, new_faq)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

