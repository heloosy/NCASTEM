import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

mission_css = '''
/* Mission Interactive Accordion */
details.mission-details {
    background: rgba(30, 58, 138, 0.03);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 1rem;
    transition: all 0.3s ease;
}
details.mission-details summary {
    font-family: var(--font-heading);
    font-weight: 600;
    color: var(--text-main);
    list-style: none; /* removes default arrow */
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    margin: 0;
}
details.mission-details summary::-webkit-details-marker {
    display: none;
}
details.mission-details summary::after {
    content: '+';
    font-size: 1.2rem;
    font-weight: 700;
    color: var(--accent);
    transition: transform 0.3s ease;
}
details[open].mission-details summary::after {
    content: '-';
    transform: rotate(180deg);
}
.mission-content {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid var(--border-color);
    text-align: left;
}
.mission-content p {
    font-size: 0.95rem;
    line-height: 1.6;
}
'''

css = css + mission_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

