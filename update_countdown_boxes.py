import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the hero-countdown block
old_hero_countdown = '''.hero-countdown {
    display: flex;
    justify-content: center;
    gap: 3rem;
    margin-top: 4rem;
    padding-top: 3rem;
    border-top: 1px solid rgba(0, 0, 0, 0.05);
}'''
new_hero_countdown = '''.hero-countdown {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    margin-top: 4rem;
}'''
css = css.replace(old_hero_countdown, new_hero_countdown)

old_countdown_item = '''.countdown-item {
    display: flex;
    flex-direction: column;
    align-items: center;
}'''
new_countdown_item = '''.countdown-item {
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
}
.countdown-item:hover {
    transform: translateY(-5px);
}'''
css = css.replace(old_countdown_item, new_countdown_item)

old_countdown_count = '''.countdown-item .count {
    font-size: 3rem;
    font-weight: 800;
    font-family: var(--font-heading);
    color: var(--accent);
    line-height: 1;
    margin-bottom: 0.5rem;
}'''
new_countdown_count = '''.countdown-item .count {
    font-size: 3.5rem;
    font-weight: 900;
    font-family: var(--font-body);
    color: var(--accent);
    line-height: 1;
    margin-bottom: 0.5rem;
}'''
css = css.replace(old_countdown_count, new_countdown_count)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
