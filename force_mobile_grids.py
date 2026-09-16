import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Append fixes to the mobile media query
# Wait, I'll just append a NEW media query at the very bottom to be absolutely safe
mobile_fixes = '''
@media (max-width: 768px) {
    .themes-grid {
        grid-template-columns: 1fr !important;
    }
    .pricing-grid {
        grid-template-columns: 1fr !important;
    }
    .profile-grid {
        grid-template-columns: 1fr !important;
    }
    html, body {
        width: 100vw;
        max-width: 100vw;
        overflow-x: hidden !important;
    }
}
'''

css = css + mobile_fixes

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

