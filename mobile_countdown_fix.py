import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

mobile_css_old = '''@media (max-width: 768px) {
    .hero-countdown {
        gap: 1.5rem;
    }
    .countdown-item .count {
        font-size: 2rem;
    }
    .countdown-item .label {
        font-size: 0.7rem;
    }
}'''

mobile_css_new = '''@media (max-width: 768px) {
    .hero-countdown {
        gap: 0.8rem;
        flex-wrap: wrap;
    }
    .countdown-item {
        min-width: 80px;
        padding: 1rem 0.5rem;
    }
    .countdown-item .count {
        font-size: 2rem;
    }
    .countdown-item .label {
        font-size: 0.7rem;
    }
}'''

css = css.replace(mobile_css_old, mobile_css_new)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
