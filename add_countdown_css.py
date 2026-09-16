import re

css_to_add = '''
/* Countdown */
.hero-countdown {
    display: flex;
    justify-content: center;
    gap: 3rem;
    margin-top: 4rem;
    padding-top: 3rem;
    border-top: 1px solid rgba(0, 0, 0, 0.05);
}
.countdown-item {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.countdown-item .count {
    font-size: 3rem;
    font-weight: 800;
    font-family: var(--font-heading);
    color: var(--accent);
    line-height: 1;
    margin-bottom: 0.5rem;
}
.countdown-item .label {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: var(--text-muted);
    font-weight: 600;
}
@media (max-width: 768px) {
    .hero-countdown {
        gap: 1.5rem;
    }
    .countdown-item .count {
        font-size: 2rem;
    }
    .countdown-item .label {
        font-size: 0.7rem;
    }
}
'''

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_to_add)
