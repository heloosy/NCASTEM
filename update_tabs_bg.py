import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_controls = '''.dept-tab-controls {
    display: flex;
    border-bottom: 1px solid var(--border-color);
    background: #ffffff;
}'''
new_controls = '''.dept-tab-controls {
    display: flex;
    border-bottom: 1px solid var(--border-color);
    background: #f1f5f9;
}'''
css = css.replace(old_controls, new_controls)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

