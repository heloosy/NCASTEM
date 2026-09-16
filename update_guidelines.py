import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Paper Presentation card
old_card = '''                    <ul class="clean-list">
                        <li>Original work, not submitted or published elsewhere.</li>
                        <li>Plagiarism must be strictly less than 15%.</li>
                        <li>Format: 250 to 300 words (Abstract).</li>
                        <li>Peer review selection process.</li>
                        <li>Published in UGC Care listed journals (Additional Charges) and Conference Proceedings with ISBN.</li>
                    </ul>'''
new_card = '''                    <ul class="clean-list">
                        <li>Original work, not submitted or published elsewhere.</li>
                        <li>Plagiarism must be strictly less than 15%.</li>
                        <li>Full paper submission required in IEEE format.</li>
                        <li>Peer review selection process.</li>
                        <li>Will be published in UGC Care listed journals (Additional Charges) and Conference Proceedings with ISBN.</li>
                    </ul>'''
html = html.replace(old_card, new_card)

# 2. Update the 6-step process to reflect full paper only, IEEE format
old_step1 = '''                    <h4>Prepare</h4>
                    <p>Format a 250-300 word abstract. Ensure original work, strictly &lt;15% plagiarism, and not published elsewhere.</p>'''
new_step1 = '''                    <h4>Prepare</h4>
                    <p>Format your full paper in IEEE format. Ensure original work, strictly &lt;15% plagiarism, and not published elsewhere.</p>'''
html = html.replace(old_step1, new_step1)

old_step2 = '''                    <h4>Submit</h4>
                    <p>Email your abstract along with the full paper to: <br><a href="mailto:tjitconference@tjohngroup.com">tjitconference@tjohngroup.com</a></p>'''
new_step2 = '''                    <h4>Submit</h4>
                    <p>Email your full paper to: <br><a href="mailto:tjitconference@tjohngroup.com">tjitconference@tjohngroup.com</a></p>'''
html = html.replace(old_step2, new_step2)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

