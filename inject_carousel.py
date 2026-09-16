import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the start of the pricing grid
old_start = '''            <div class="pricing-grid mt-5">'''
new_start = '''            <div class="pricing-carousel-wrapper mt-5" style="position: relative;">
                <button class="carousel-arrow left-arrow" aria-label="Scroll left" onclick="document.getElementById('pricingGrid').scrollBy({left: -300, behavior: 'smooth'})">
                    <i class="fas fa-chevron-left"></i>
                </button>
                <div class="pricing-grid" id="pricingGrid">'''
html = html.replace(old_start, new_start)

# We need to close the pricing-carousel-wrapper right after the pricing grid ends.
# The pricing grid ends after Card 4.
old_end = '''                    <a href="#themes" class="btn btn-outline-primary btn-full">Register Now</a>
                </div>
            </div>
        </div>
    </section>'''

new_end = '''                    <a href="#themes" class="btn btn-outline-primary btn-full">Register Now</a>
                </div>
                
                </div> <!-- End pricing-grid -->
                <button class="carousel-arrow right-arrow" aria-label="Scroll right" onclick="document.getElementById('pricingGrid').scrollBy({left: 300, behavior: 'smooth'})">
                    <i class="fas fa-chevron-right"></i>
                </button>
            </div> <!-- End carousel-wrapper -->
        </div>
    </section>'''
    
html = html.replace(old_end, new_end)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

