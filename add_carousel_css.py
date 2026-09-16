import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_addition = '''
/* Pricing Carousel Styles */
.pricing-carousel-wrapper {
    position: relative;
    padding: 0 40px; /* Room for arrows */
}

.pricing-grid {
    display: flex !important;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    gap: 2rem;
    padding-bottom: 2rem;
    scrollbar-width: none; /* Firefox */
}
.pricing-grid::-webkit-scrollbar {
    display: none; /* Chrome/Safari */
}

.pricing-card {
    min-width: 280px;
    flex: 0 0 auto;
    scroll-snap-align: start;
}

.carousel-arrow {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 40px;
    height: 40px;
    background: var(--accent);
    color: white;
    border: none;
    border-radius: 50%;
    cursor: pointer;
    z-index: 10;
    box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: var(--transition);
}
.carousel-arrow:hover {
    background: var(--accent-hover);
    transform: translateY(-50%) scale(1.1);
}
.left-arrow { left: 0; }
.right-arrow { right: 0; }

@media (max-width: 768px) {
    .pricing-carousel-wrapper {
        padding: 0;
    }
    .carousel-arrow {
        display: none; /* Hide arrows on true mobile where users naturally swipe */
    }
    .pricing-grid {
        flex-direction: column; /* Stack on true mobile */
    }
    .pricing-card {
        min-width: 100%;
    }
}
'''

css = css + css_addition

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

