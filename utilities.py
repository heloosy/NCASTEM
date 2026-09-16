import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove grayscale filter
css = css.replace('filter: grayscale(100%) contrast(1.2);', '/* filter: grayscale(100%) contrast(1.2); */')
css = css.replace('.profile-card:hover .profile-img-wrap img {\n    filter: grayscale(0%);\n}', '')

# Add utility classes
utility_css = '''
/* Utilities */
.mt-1 { margin-top: 0.5rem; }
.mt-2 { margin-top: 1rem; }
.mt-3 { margin-top: 1.5rem; }
.mt-4 { margin-top: 2rem; }
.mt-5 { margin-top: 3rem; }
.mt-6 { margin-top: 5rem; }

.mb-1 { margin-bottom: 0.5rem; }
.mb-2 { margin-bottom: 1rem; }
.mb-3 { margin-bottom: 1.5rem; }
.mb-4 { margin-bottom: 2rem; }
.mb-5 { margin-bottom: 3rem; }
.mb-6 { margin-bottom: 5rem; }

.pt-1 { padding-top: 0.5rem; }
.pt-2 { padding-top: 1rem; }
.pt-3 { padding-top: 1.5rem; }
.pt-4 { padding-top: 2rem; }
.pt-5 { padding-top: 3rem; }
.pt-6 { padding-top: 5rem; }

.pb-1 { padding-bottom: 0.5rem; }
.pb-2 { padding-bottom: 1rem; }
.pb-3 { padding-bottom: 1.5rem; }
.pb-4 { padding-bottom: 2rem; }
.pb-5 { padding-bottom: 3rem; }
.pb-6 { padding-bottom: 5rem; }

.text-center { text-align: center; }
'''

css = css + utility_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
