import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

mission_css = '''
.dept-mission {
    padding: 1.5rem;
    background-color: var(--bg-alt);
    border-left: 4px solid var(--accent);
    border-radius: 0 8px 8px 0;
}
.dept-mission h5 {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
    color: var(--accent);
}
.dept-mission h5 i {
    font-size: 1rem;
}
'''

# insert after .dept-vision
css = css.replace('.dept-vision h5 i {\n    font-size: 1rem;\n}', '.dept-vision h5 i {\n    font-size: 1rem;\n}\n' + mission_css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

