import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

animation_css = '''
/* Earth Zoom Reveal Animation */
.earth-reveal-container {
    position: relative;
    overflow: hidden;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(30, 58, 138, 0.15);
    background: #020617; /* Deep space dark blue/black */
}

.earth-img {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 60%;
    height: auto;
    transform: translate(-50%, -50%) scale(0.5) rotate(0deg);
    opacity: 0;
    z-index: 2;
    pointer-events: none;
}

.tjit-building-img {
    width: 100%;
    display: block;
    object-fit: cover;
    opacity: 1; /* fallback */
    border-radius: 12px;
}

/* Trigger animation when parent row becomes visible */
.about-tjit-top-grid.visible .earth-img {
    animation: earthZoomReveal 2.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

.about-tjit-top-grid.visible .tjit-building-img {
    animation: buildingReveal 2.8s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

@keyframes earthZoomReveal {
    0% {
        opacity: 0;
        transform: translate(-50%, -50%) scale(0.1) rotate(0deg);
    }
    15% {
        opacity: 1;
        transform: translate(-50%, -50%) scale(0.8) rotate(45deg);
    }
    50% {
        opacity: 1;
        transform: translate(-50%, -50%) scale(1) rotate(180deg);
    }
    75% {
        opacity: 0;
        transform: translate(-50%, -50%) scale(6) rotate(270deg);
    }
    100% {
        opacity: 0;
        transform: translate(-50%, -50%) scale(6) rotate(360deg);
    }
}

@keyframes buildingReveal {
    0% {
        opacity: 0;
        transform: scale(1.5);
    }
    50% {
        opacity: 0;
        transform: scale(1.5);
    }
    70% {
        opacity: 0.5;
        transform: scale(1.2);
    }
    100% {
        opacity: 1;
        transform: scale(1);
    }
}
'''

css = css + animation_css

# Also remove the existing box-shadow and border-radius from .tjit-building-img 
# since we moved it to .earth-reveal-container to prevent the expanding earth from breaking the borders
old_img_css = '''.tjit-building-img {
    width: 100%;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(30, 58, 138, 0.15);
    display: block;
    object-fit: cover;
}'''
new_img_css = '''.tjit-building-img {
    width: 100%;
    display: block;
    object-fit: cover;
}'''
css = css.replace(old_img_css, new_img_css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

