import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .dept-tabs
old_tabs_1 = '''.dept-tabs {
    background-color: var(--bg-alt);
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid var(--border-color);
}'''
new_tabs_1 = '''.dept-tabs {
    background-color: var(--bg-alt);
    border-radius: 0 8px 8px 0;
    overflow: hidden;
    border: 1px solid var(--border-color);
    border-left: 4px solid var(--accent-alt);
}'''
css = css.replace(old_tabs_1, new_tabs_1)

old_tabs_2 = '''.dept-tab-label.active {
    color: var(--accent);
    background: var(--bg-alt);
    border-bottom: 2px solid var(--accent);
}'''
new_tabs_2 = '''.dept-tab-label.active {
    color: var(--accent-alt);
    background: var(--bg-alt);
    border-bottom: 2px solid var(--accent-alt);
}'''
css = css.replace(old_tabs_2, new_tabs_2)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

