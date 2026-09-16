import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Date
html = html.replace(
    '<span class="glance-value">30 OCT 2026</span>',
    '<i class="fas fa-calendar-alt" style="font-size: 1.8rem; color: var(--accent-alt); margin-bottom: 0.8rem;"></i>\n                <span class="glance-value">30 OCT 2026</span>'
)

# 2. Venue
html = html.replace(
    '<span class="glance-value">TJIT, BENGALURU</span>',
    '<i class="fas fa-map-marker-alt" style="font-size: 1.8rem; color: var(--accent-alt); margin-bottom: 0.8rem;"></i>\n                <span class="glance-value">TJIT, BENGALURU</span>'
)

# 3. Domains
html = html.replace(
    '<span class="glance-value">06</span>\n                <span class="glance-label">RESEARCH DOMAINS</span>',
    '<i class="fas fa-microscope" style="font-size: 1.8rem; color: var(--accent-alt); margin-bottom: 0.8rem;"></i>\n                <span class="glance-value">06</span>\n                <span class="glance-label">RESEARCH DOMAINS</span>'
)

# 4. Formats
html = html.replace(
    '<span class="glance-value">PAPER + POSTER</span>',
    '<i class="fas fa-chalkboard-teacher" style="font-size: 1.8rem; color: var(--accent-alt); margin-bottom: 0.8rem;"></i>\n                <span class="glance-value">PAPER + POSTER</span>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
