lines_to_change = [260, 338, 379, 530, 597, 598, 607, 608, 681, 722, 933, 985, 1044]

with open('style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in lines_to_change:
    # lists are 0-indexed, so line 260 is index 259
    if i-1 < len(lines):
        lines[i-1] = lines[i-1].replace('var(--accent)', 'var(--accent-alt)')

with open('style.css', 'w', encoding='utf-8') as f:
    f.writelines(lines)
