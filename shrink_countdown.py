import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace hero-countdown
old_hero_countdown = '''.hero-countdown {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    margin-top: 4rem;
}'''
new_hero_countdown = '''.hero-countdown {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-top: 1.5rem;
}'''
css = css.replace(old_hero_countdown, new_hero_countdown)

# Replace countdown-item
old_countdown_item = '''.countdown-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.9);
    border: 1px solid var(--border-color);
    box-shadow: 0 15px 35px rgba(30, 58, 138, 0.1);
    border-radius: 12px;
    padding: 1.5rem 1rem;
    min-width: 130px;
    backdrop-filter: blur(10px);
    transition: transform 0.3s ease;
}'''
new_countdown_item = '''.countdown-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.95);
    border: 1px solid var(--border-color);
    box-shadow: 0 10px 25px rgba(30, 58, 138, 0.08);
    border-radius: 8px;
    padding: 1rem 0.5rem;
    min-width: 100px;
    backdrop-filter: blur(10px);
    transition: transform 0.3s ease;
}'''
css = css.replace(old_countdown_item, new_countdown_item)

# Replace count
old_count = '''.countdown-item .count {
    font-size: 3.5rem;
    font-weight: 900;
    font-family: var(--font-body);
    color: var(--accent);
    line-height: 1;
    margin-bottom: 0.5rem;
}'''
new_count = '''.countdown-item .count {
    font-size: 2.2rem;
    font-weight: 800;
    font-family: var(--font-body);
    color: var(--accent);
    line-height: 1;
    margin-bottom: 0.3rem;
}'''
css = css.replace(old_count, new_count)

# Replace label
old_label = '''.countdown-item .label {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--text-muted);
    font-weight: 600;
}'''
new_label = '''.countdown-item .label {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--text-muted);
    font-weight: 600;
}'''
css = css.replace(old_label, new_label)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove mt-5 from index.html
html = html.replace('<div class="hero-countdown mt-5 fade-up delay-4">', '<div class="hero-countdown fade-up delay-4">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
