import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

tabs_css = '''
/* Department Tabs */
.dept-tabs {
    background-color: var(--bg-alt);
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid var(--border-color);
}
.dept-tab-controls {
    display: flex;
    border-bottom: 1px solid var(--border-color);
    background: #ffffff;
}
.dept-tab-label {
    flex: 1;
    text-align: center;
    padding: 0.8rem;
    font-family: var(--font-heading);
    font-weight: 600;
    font-size: 0.95rem;
    color: var(--text-muted);
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 0.5rem;
}
.dept-tab-label:hover {
    color: var(--accent);
}
.dept-tab-label.active {
    color: var(--accent);
    background: var(--bg-alt);
    border-bottom: 2px solid var(--accent);
}
.dept-tab-content {
    display: none;
    padding: 1.5rem;
}
.dept-tab-content.active {
    display: block;
    animation: fadeIn 0.3s ease forwards;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
}
'''

# We can append it at the end of the file since it's global
css = css + tabs_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

