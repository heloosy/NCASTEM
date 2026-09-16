import re

css_to_add = '''
@media (max-width: 768px) {
    .vm-grid, .dept-grid {
        grid-template-columns: 1fr;
    }
}
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_to_add)
