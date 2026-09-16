import re

html_to_inject = '''                <div class="hero-cta fade-up delay-4">
                    <a href="#guidelines" class="btn btn-primary btn-large">SUBMIT PAPER <i class="fas fa-arrow-right"></i></a>
                    <a href="#registration" class="btn btn-outline-light btn-large">REGISTER NOW <i class="fas fa-arrow-right"></i></a>
                </div>
                
                <div class="hero-countdown mt-5 fade-up delay-4">
                    <div class="countdown-item">
                        <span class="count" id="cd-days">00</span>
                        <span class="label">Days</span>
                    </div>
                    <div class="countdown-item">
                        <span class="count" id="cd-hours">00</span>
                        <span class="label">Hours</span>
                    </div>
                    <div class="countdown-item">
                        <span class="count" id="cd-minutes">00</span>
                        <span class="label">Minutes</span>
                    </div>
                    <div class="countdown-item">
                        <span class="count" id="cd-seconds">00</span>
                        <span class="label">Seconds</span>
                    </div>
                </div>'''

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the cta block to inject the countdown below it
pattern = r'<div class="hero-cta fade-up delay-4">.*?</div>'
html = re.sub(pattern, html_to_inject, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
