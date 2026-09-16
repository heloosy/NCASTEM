import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_vm = '''.vm-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.5rem;
}'''
new_vm = '''.vm-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
}'''
css = css.replace(old_vm, new_vm)

# I should also revert align-items: flex-start on .about-tjit-top-grid? 
# In the previous step I actually set it to align-items: center. I will leave it as center since that's what it was before.

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

