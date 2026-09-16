import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

hide_arrows_desktop = '''
@media (min-width: 1200px) {
    .pricing-carousel-wrapper {
        padding: 0;
    }
    .carousel-arrow {
        display: none !important;
    }
    .pricing-grid {
        justify-content: center;
        overflow-x: visible;
    }
}
'''

css = css + hide_arrows_desktop

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

