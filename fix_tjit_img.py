import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_img = '''.tjit-building-img {
    width: 100%;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(30, 58, 138, 0.15);
    display: block;
    object-fit: cover;
}'''
new_img = '''.tjit-building-img {
    width: 100%;
    aspect-ratio: 21 / 9;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(30, 58, 138, 0.15);
    display: block;
    object-fit: cover;
}'''
css = css.replace(old_img, new_img)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

