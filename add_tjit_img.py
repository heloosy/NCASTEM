import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The original block:
#            <div class="tjit-content fade-up" style="margin-bottom: 5rem;">
#                <p class="lead-text text-muted" style="max-width: 1000px; margin-bottom: 3rem; font-size: 1.1rem; line-height: 1.8;">
#                    T. John Institute of Technology (TJIT) is a premier private Engineering College located in Bangalore, Karnataka. Established in 2006 by Dr. Thomas P. John, the institute is affiliated to VTU and approved by AICTE. We impart science-based engineering education to develop professional skills, preparing students for immediate employment and lifelong learning.
#                </p>
#                
#                <div class="vm-grid">

old_html = '''            <div class="tjit-content fade-up" style="margin-bottom: 5rem;">
                <p class="lead-text text-muted" style="max-width: 1000px; margin-bottom: 3rem; font-size: 1.1rem; line-height: 1.8;">
                    T. John Institute of Technology (TJIT) is a premier private Engineering College located in Bangalore, Karnataka. Established in 2006 by Dr. Thomas P. John, the institute is affiliated to VTU and approved by AICTE. We impart science-based engineering education to develop professional skills, preparing students for immediate employment and lifelong learning.
                </p>
                
                <div class="vm-grid">'''

new_html = '''            <div class="about-tjit-top-grid fade-up" style="margin-bottom: 3rem;">
                <div class="tjit-text">
                    <p class="lead-text text-muted" style="font-size: 1.1rem; line-height: 1.8; margin-bottom: 0; text-align: justify;">
                        T. John Institute of Technology (TJIT) is a premier private Engineering College located in Bangalore, Karnataka. Established in 2006 by Dr. Thomas P. John, the institute is affiliated to VTU and approved by AICTE. We impart science-based engineering education to develop professional skills, preparing students for immediate employment and lifelong learning.
                    </p>
                </div>
                <div class="tjit-img-box">
                    <img src="images/tjit-building.webp" alt="TJIT Campus" class="tjit-building-img">
                </div>
            </div>
            
            <div class="tjit-content" style="margin-bottom: 5rem;">
                <div class="vm-grid">'''

html = html.replace(old_html, new_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add CSS for the new grid
new_css = '''
.about-tjit-top-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    align-items: center;
}
.tjit-building-img {
    width: 100%;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(30, 58, 138, 0.15);
    display: block;
    object-fit: cover;
}
@media (max-width: 992px) {
    .about-tjit-top-grid {
        grid-template-columns: 1fr;
    }
}
'''

if '.about-tjit-top-grid' not in css:
    css = css + new_css
    
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

