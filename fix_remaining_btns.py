import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Line 88 & 743 (REGISTER NOW with arrow)
html = html.replace('<a href="#registration" class="btn btn-outline-light btn-large">REGISTER NOW <i class="fas fa-arrow-right"></i></a>', '<button class="btn btn-outline-light btn-large register-trigger" style="border-radius: 4px;">REGISTER NOW <i class="fas fa-arrow-right"></i></button>')

# Line 535 (The primary button inside the popular pricing card)
html = html.replace('<a href="#themes" class="btn btn-primary btn-full">Register Now</a>', '<button class="btn btn-primary btn-full register-trigger">Register Now</button>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

