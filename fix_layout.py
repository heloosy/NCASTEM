import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Change align-items
old_grid = '''.about-tjit-top-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    align-items: flex-start;
}'''
new_grid = '''.about-tjit-top-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    align-items: center;
}'''
css = css.replace(old_grid, new_grid)

# Change vm-grid to stack vertically to take up more space
old_vm = '''.vm-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
}'''
new_vm = '''.vm-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.5rem;
}'''
css = css.replace(old_vm, new_vm)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

