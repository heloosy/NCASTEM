import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

slideshow_html = '''<div class="hero-slideshow">
            <div class="hero-slide" style="background-image: url('images/campus1.webp');"></div>
            <div class="hero-slide" style="background-image: url('images/campus2.webp');"></div>
            <div class="hero-slide" style="background-image: url('images/campus3.webp');"></div>
            <div class="hero-slide" style="background-image: url('images/campus4.webp');"></div>
        </div>
        <div class="hero-overlay"></div>'''

html = html.replace('<div class="hero-bg">\n            <div class="hero-overlay"></div>\n        </div>', slideshow_html)
html = html.replace('<div class="hero-bg">\r\n            <div class="hero-overlay"></div>\r\n        </div>', slideshow_html)

# Also let's update the text styling for "NCASTEM" and the subtitle.
# In the user's image, "NCASTEM" is very bold, black/deep-blue, and uses Inter or Roboto.
# I will add a new class 'hero-rich-title' and 'hero-rich-subtitle' or just modify the existing in CSS.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
