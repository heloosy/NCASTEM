import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

modal_html = '''
    <!-- Registration Modal -->
    <div id="registerModal" class="modal-overlay">
        <div class="modal-content">
            <button class="modal-close" id="closeModal" aria-label="Close">&times;</button>
            <h3 class="modal-title">Registration Process</h3>
            <p class="modal-subtitle text-muted mb-4">Please complete both steps to secure your spot.</p>
            
            <div class="modal-steps-grid">
                <div class="modal-step">
                    <div class="step-header">
                        <div class="step-badge">1</div>
                        <h4>Submission</h4>
                    </div>
                    <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1rem;">Scan the QR code below to access the submission form.</p>
                    <div class="qr-container">
                        <img src="images/qr1.png" alt="Submission QR Code" class="qr-code">
                    </div>
                </div>
                
                <div class="modal-step">
                    <div class="step-header">
                        <div class="step-badge">2</div>
                        <h4>Payment</h4>
                    </div>
                    <p class="text-muted" style="font-size: 0.9rem; margin-bottom: 1rem;">Scan the QR code below to complete your fee payment.</p>
                    <div class="qr-container">
                        <img src="images/qr2.png" alt="Payment QR Code" class="qr-code">
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- 13. Footer -->
'''

html = html.replace('    <!-- 13. Footer -->', modal_html)

# Also update the Register buttons so they don't jump to #themes, but open the modal instead.
# Find <a href="#themes" class="btn btn-outline-primary btn-full">Register Now</a>
old_btn = '<a href="#themes" class="btn btn-outline-primary btn-full">Register Now</a>'
new_btn = '<button class="btn btn-outline-primary btn-full register-trigger">Register Now</button>'
html = html.replace(old_btn, new_btn)

# Also the Register Now in the hero section!
old_hero_btn = '<a href="#registration" class="btn btn-outline-light">Register Now &rarr;</a>'
new_hero_btn = '<button class="btn btn-outline-light register-trigger">Register Now &rarr;</button>'
html = html.replace(old_hero_btn, new_hero_btn)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

