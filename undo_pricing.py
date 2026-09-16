import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

bad_end = '''                </div>
                
                <button class="carousel-arrow right-arrow" aria-label="Scroll right" onclick="document.getElementById('pricingGrid').scrollBy({left: 300, behavior: 'smooth'})">
                    <i class="fas fa-chevron-right"></i>
                </button>
            </div>
        </div>
    </section>'''

good_end = '''                </div>
            </div>
        </div>
    </section>'''

html = html.replace(bad_end, good_end)

bad_start = '''            <div class="pricing-carousel-wrapper mt-5">
                <button class="carousel-arrow left-arrow" aria-label="Scroll left" onclick="document.getElementById('pricingGrid').scrollBy({left: -300, behavior: 'smooth'})">
                    <i class="fas fa-chevron-left"></i>
                </button>
                
                <div class="pricing-grid" id="pricingGrid">'''
                
good_start = '''            <div class="pricing-grid mt-5">'''

html = html.replace(bad_start, good_start)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

