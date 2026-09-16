import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Hero Background Animation
css = css.replace('.hero-bg {\n    position: absolute;', '''@keyframes subtleZoom {
    0% { transform: scale(1); }
    100% { transform: scale(1.08); }
}
.hero-bg {
    position: absolute;
    animation: subtleZoom 25s infinite alternate ease-in-out;''')

# 2. Button Shine Effect
btn_primary_css = '''.btn-primary {
    position: relative;
    overflow: hidden;'''
css = css.replace('.btn-primary {\n    background-color', btn_primary_css + '\n    background-color')

btn_primary_after = '''
.btn-primary::after {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: rgba(255,255,255,0.2);
    transform: rotate(45deg) translateY(-100%);
    transition: transform 0.6s cubic-bezier(0.25, 0.8, 0.25, 1);
}
.btn-primary:hover::after {
    transform: rotate(45deg) translateY(100%);
}
'''
css = css.replace('.btn-primary:hover {', btn_primary_after + '\n.btn-primary:hover {')

# 3. Card Hover Lifts
hover_shadow = 'box-shadow: 0 20px 40px rgba(30, 58, 138, 0.08);'

css = css.replace('.theme-card:hover {\n    border-color: var(--border-hover);\n    transform: translateY(-5px);\n}', 
'''.theme-card:hover {
    border-color: var(--border-hover);
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(30, 58, 138, 0.08);
}''')

# 4. Presentation Card Hover
css = css.replace('.presentation-card {\n    background-color: var(--bg-card);\n    border: 1px solid var(--border-color);\n    padding: 4rem 3rem;\n}', 
'''.presentation-card {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 4rem 3rem;
    transition: var(--transition);
}
.presentation-card:hover {
    transform: translateY(-8px);
    border-color: var(--border-hover);
    box-shadow: 0 20px 40px rgba(30, 58, 138, 0.08);
}''')

# 5. Pricing Card Hover (Popular one already transforms, but let's enhance)
css = css.replace('.pricing-card {\n    background-color: var(--bg-card);\n    border: 1px solid var(--border-color);\n    padding: 3rem 2rem;\n    position: relative;\n    display: flex;\n    flex-direction: column;\n}',
'''.pricing-card {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 3rem 2rem;
    position: relative;
    display: flex;
    flex-direction: column;
    transition: var(--transition);
}
.pricing-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px rgba(30, 58, 138, 0.08);
    border-color: var(--border-hover);
}''')
css = css.replace('.pricing-card.popular {\n    border-color: var(--accent);\n    background-color: rgba(30, 58, 138, 0.03);\n    transform: translateY(-10px);\n}',
'''.pricing-card.popular {
    border-color: var(--accent);
    background-color: rgba(30, 58, 138, 0.03);
    transform: translateY(-10px);
    box-shadow: 0 15px 30px rgba(30, 58, 138, 0.05);
}
.pricing-card.popular:hover {
    transform: translateY(-15px);
    box-shadow: 0 25px 50px rgba(30, 58, 138, 0.12);
}''')

# 6. Profile Cards Hover
css = css.replace('.profile-card.premium {\n    display: flex;\n    gap: 2rem;\n    align-items: center;\n    background-color: var(--bg-card);\n    border: 1px solid var(--border-color);\n    padding: 2.5rem;\n}',
'''.profile-card.premium {
    display: flex;
    gap: 2rem;
    align-items: center;
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 2.5rem;
    transition: var(--transition);
}
.profile-card.premium:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(30, 58, 138, 0.08);
    border-color: var(--border-hover);
}''')

css = css.replace('.profile-card.horizontal {\n    display: flex;\n    gap: 1.5rem;\n    align-items: center;\n    background-color: var(--bg-card);\n    border: 1px solid var(--border-color);\n    padding: 1.5rem;\n}',
'''.profile-card.horizontal {
    display: flex;
    gap: 1.5rem;
    align-items: center;
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 1.5rem;
    transition: var(--transition);
}
.profile-card.horizontal:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(30, 58, 138, 0.08);
    border-color: var(--border-hover);
}''')

css = css.replace('.profile-card.standard {\n    background-color: var(--bg-card);\n    border: 1px solid var(--border-color);\n    padding: 2rem;\n    text-align: center;\n}',
'''.profile-card.standard {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 2rem;
    text-align: center;
    transition: var(--transition);
}
.profile-card.standard:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(30, 58, 138, 0.08);
    border-color: var(--border-hover);
}''')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
