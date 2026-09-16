import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the vm-grid block
vm_grid_match = re.search(r'<div class="vm-grid">.*?</div>\s*</div>', html, re.DOTALL)
if vm_grid_match:
    vm_grid_html = vm_grid_match.group(0)
    # Remove it from its current position
    html = html.replace(vm_grid_html, '')
    
    # Inject it directly after the text paragraph inside tjit-text
    # We will also add a mt-4 to separate it from the paragraph
    new_vm_grid = vm_grid_html.replace('<div class="vm-grid">', '<div class="vm-grid" style="margin-top: 2rem;">')
    
    target = '''T. John Institute of Technology (TJIT) is a premier private Engineering College located in Bangalore, Karnataka. Established in 2006 by Dr. Thomas P. John, the institute is affiliated to VTU and approved by AICTE. We impart science-based engineering education to develop professional skills, preparing students for immediate employment and lifelong learning.
                    </p>'''
    
    html = html.replace(target, target + '\n' + new_vm_grid)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

