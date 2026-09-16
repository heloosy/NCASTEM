import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .profile-card.premium
old_premium = '''.profile-card.premium {
    display: flex;
    gap: 2rem;
    align-items: center;
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 2.5rem;
    transition: var(--transition);
}'''
new_premium = '''.profile-card.premium {
    display: flex;
    gap: 1.5rem;
    align-items: center;
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 1.5rem;
    transition: var(--transition);
    box-shadow: 0 8px 24px rgba(214, 137, 16, 0.1);
}'''
css = css.replace(old_premium, new_premium)

# Update hover for premium
old_premium_hover = '''.profile-card.premium:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(30, 58, 138, 0.08);
    border-color: var(--border-hover);
}'''
new_premium_hover = '''.profile-card.premium:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(214, 137, 16, 0.25);
    border-color: var(--accent-alt);
}'''
css = css.replace(old_premium_hover, new_premium_hover)

# Update premium image size
old_premium_img = '''.profile-card.premium .profile-img-wrap {
    width: 150px;
    height: 150px;
    flex-shrink: 0;
}'''
new_premium_img = '''.profile-card.premium .profile-img-wrap {
    width: 100px;
    height: 100px;
    flex-shrink: 0;
}'''
css = css.replace(old_premium_img, new_premium_img)

# 2. Update .profile-card.horizontal
old_horizontal = '''.profile-card.horizontal {
    display: flex;
    gap: 1.5rem;
    align-items: center;
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 1.5rem;
    transition: var(--transition);
}'''
new_horizontal = '''.profile-card.horizontal {
    display: flex;
    gap: 1.2rem;
    align-items: center;
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 1rem 1.5rem;
    transition: var(--transition);
    box-shadow: 0 8px 20px rgba(214, 137, 16, 0.08);
}'''
css = css.replace(old_horizontal, new_horizontal)

old_horizontal_hover = '''.profile-card.horizontal:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(30, 58, 138, 0.08);
    border-color: var(--border-hover);
}'''
new_horizontal_hover = '''.profile-card.horizontal:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 25px rgba(214, 137, 16, 0.2);
    border-color: var(--accent-alt);
}'''
css = css.replace(old_horizontal_hover, new_horizontal_hover)

old_horizontal_img = '''.profile-card.horizontal .profile-img-wrap {
    width: 100px;
    height: 100px;
    flex-shrink: 0;
}'''
new_horizontal_img = '''.profile-card.horizontal .profile-img-wrap {
    width: 80px;
    height: 80px;
    flex-shrink: 0;
}'''
css = css.replace(old_horizontal_img, new_horizontal_img)


# 3. Update .profile-card.standard
old_standard = '''.profile-card.standard {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 2rem;
    text-align: center;
    transition: var(--transition);
}'''
new_standard = '''.profile-card.standard {
    background-color: var(--bg-card);
    border: 1px solid var(--border-color);
    padding: 1.5rem;
    text-align: center;
    transition: var(--transition);
    box-shadow: 0 8px 20px rgba(214, 137, 16, 0.05);
}'''
css = css.replace(old_standard, new_standard)

old_standard_hover = '''.profile-card.standard:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(30, 58, 138, 0.08);
    border-color: var(--border-hover);
}'''
new_standard_hover = '''.profile-card.standard:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 25px rgba(214, 137, 16, 0.15);
    border-color: var(--accent-alt);
}'''
css = css.replace(old_standard_hover, new_standard_hover)

old_standard_img = '''.profile-card.standard .profile-img-wrap {
    width: 120px;
    height: 120px;
    margin: 0 auto 1.5rem;
}'''
new_standard_img = '''.profile-card.standard .profile-img-wrap {
    width: 90px;
    height: 90px;
    margin: 0 auto 1.2rem;
}'''
css = css.replace(old_standard_img, new_standard_img)


with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
