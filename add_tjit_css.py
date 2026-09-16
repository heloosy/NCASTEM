import re

css_to_add = '''
/* About TJIT & Departments */
.vm-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
}
.vm-card {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 3rem;
    border-radius: 12px;
    transition: var(--transition);
}
.vm-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(30, 58, 138, 0.05);
    border-color: var(--border-hover);
}
.vm-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
}
.vm-header i {
    font-size: 1.5rem;
}
.vm-header h4 {
    margin: 0;
    font-size: 1.5rem;
}

.dept-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
}
.dept-card {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 12px;
    padding: 3rem;
    transition: var(--transition);
}
.dept-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(30, 58, 138, 0.05);
    border-color: var(--border-hover);
}
.dept-icon {
    font-size: 2.5rem;
    margin-bottom: 1.5rem;
}
.dept-card h3 {
    font-size: 1.5rem;
    margin-bottom: 1.5rem;
}
.dept-vision {
    margin-top: 2rem;
    padding: 1.5rem;
    background-color: var(--bg-alt);
    border-left: 4px solid var(--accent-alt);
    border-radius: 0 8px 8px 0;
}
.dept-vision h5 {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
    color: var(--accent-alt);
}
.dept-vision h5 i {
    font-size: 1rem;
}
.text-muted {
    color: var(--text-muted) !important;
}
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_to_add)

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix benefits grid spacing
css = css.replace('.benefits-grid {\n    display: grid;\n    grid-template-columns: repeat(4, 1fr);\n    gap: 2rem;\n}', 
'''.benefits-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 4rem; /* Increased gap */
    text-align: left;
}''')

# Also fix the general text-muted class to exist, wait I just added it.

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
