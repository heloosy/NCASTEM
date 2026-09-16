import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add earth image to tjit-img-box
old_img_box = '''<div class="tjit-img-box">
                    <img src="images/tjit-building.webp" alt="TJIT Campus" class="tjit-building-img">
                </div>'''
new_img_box = '''<div class="tjit-img-box earth-reveal-container">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/2/22/Earth_Western_Hemisphere_transparent_background.png" alt="Earth" class="earth-img">
                    <img src="images/tjit-building.webp" alt="TJIT Campus" class="tjit-building-img">
                </div>'''

html = html.replace(old_img_box, new_img_box)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

