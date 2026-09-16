import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_process = r'''            <div class="process-grid mt-5">
                <div class="process-step fade-up">
                    <div class="step-num">01</div>
                    <h4>Prepare</h4>
                    <p>Write your 250-300 word abstract ensuring &lt;15% plagiarism.</p>
                </div>
                <div class="process-step fade-up delay-1">
                    <div class="step-num">02</div>
                    <h4>Submit</h4>
                    <p>Email your abstract to: <a href="mailto:tjitconference@tjohngroup.com">tjitconference@tjohngroup.com</a></p>
                </div>
                <div class="process-step fade-up delay-2">
                    <div class="step-num">03</div>
                    <h4>Review</h4>
                    <p>Undergo rigorous peer review by technical committee.</p>
                </div>
                <div class="process-step fade-up delay-3">
                    <div class="step-num">04</div>
                    <h4>Acceptance</h4>
                    <p>Receive official notification of acceptance via email.</p>
                </div>
                <div class="process-step fade-up delay-4">
                    <div class="step-num">05</div>
                    <h4>Register</h4>
                    <p>Complete participant registration & fee payment.</p>
                </div>
                <div class="process-step fade-up delay-5">
                    <div class="step-num">06</div>
                    <h4>Present</h4>
                    <p>Deliver your research on October 30th, 2026.</p>
                </div>
            </div>'''

new_process = '''            <div class="process-grid mt-5">
                <div class="process-step fade-up">
                    <div class="step-num">01</div>
                    <h4>Prepare</h4>
                    <p>Format a 250-300 word abstract. Ensure original work, strictly &lt;15% plagiarism, and not published elsewhere.</p>
                </div>
                <div class="process-step fade-up delay-1">
                    <div class="step-num">02</div>
                    <h4>Submit</h4>
                    <p>Email your abstract along with the full paper to: <br><a href="mailto:tjitconference@tjohngroup.com">tjitconference@tjohngroup.com</a></p>
                </div>
                <div class="process-step fade-up delay-2">
                    <div class="step-num">03</div>
                    <h4>Review</h4>
                    <p>Undergo a rigorous peer review selection process by the technical committee.</p>
                </div>
                <div class="process-step fade-up delay-3">
                    <div class="step-num">04</div>
                    <h4>Acceptance</h4>
                    <p>Receive official notification of acceptance via email.</p>
                </div>
                <div class="process-step fade-up delay-4">
                    <div class="step-num">05</div>
                    <h4>Register</h4>
                    <p>Complete participant registration & fee payment.</p>
                </div>
                <div class="process-step fade-up delay-5">
                    <div class="step-num">06</div>
                    <h4>Publish & Present</h4>
                    <p>Deliver your research. Published in UGC Care listed journals (Additional Charges) and Conference Proceedings with ISBN.</p>
                </div>
            </div>'''

# We will use simple string replace
if old_process in html:
    html = html.replace(old_process, new_process)
else:
    print("Could not find the exact old_process block.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

