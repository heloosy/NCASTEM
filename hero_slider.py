import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add slideshow CSS
slideshow_css = '''
.hero-slideshow {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    z-index: -2;
    background-color: var(--bg-main);
}
.hero-slide {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background-size: cover;
    background-position: center;
    opacity: 0;
    animation: slideFade 24s infinite;
}
.hero-slide:nth-child(1) { animation-delay: 0s; }
.hero-slide:nth-child(2) { animation-delay: 6s; }
.hero-slide:nth-child(3) { animation-delay: 12s; }
.hero-slide:nth-child(4) { animation-delay: 18s; }

@keyframes slideFade {
    0% { opacity: 0; transform: scale(1); }
    8% { opacity: 1; transform: scale(1.02); }
    25% { opacity: 1; transform: scale(1.06); }
    33% { opacity: 0; transform: scale(1.08); }
    100% { opacity: 0; transform: scale(1.1); }
}
'''
css = css + slideshow_css

# Fix hero title typography
old_title = '''.hero-title {
    font-size: 6rem;
    font-weight: 700;
    letter-spacing: -2px;
    line-height: 1;
    margin-bottom: 1.5rem;
    text-transform: uppercase;
}'''

new_title = '''.hero-title {
    font-size: 7.5rem;
    font-weight: 900;
    letter-spacing: -1px;
    line-height: 1;
    margin-bottom: 1.5rem;
    text-transform: uppercase;
    font-family: var(--font-body);
    color: #0b1120;
}'''
css = css.replace(old_title, new_title)

# Fix hero subtitle
old_subtitle = '''.hero-subtitle {
    font-family: var(--font-body);
    font-size: 1.5rem;
    font-weight: 400;
    color: var(--text-muted);
    line-height: 1.5;
    margin-bottom: 3rem;
}'''
new_subtitle = '''.hero-subtitle {
    font-family: var(--font-body);
    font-size: 1.6rem;
    font-weight: 500;
    color: #334155;
    line-height: 1.6;
    margin-bottom: 3rem;
    max-width: 850px;
    margin-left: auto;
    margin-right: auto;
}'''
css = css.replace(old_subtitle, new_subtitle)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
