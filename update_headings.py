import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update Step 05
old_step5 = '''<div class="step-num">05</div>
                    <h4>Register</h4>'''
new_step5 = '''<div class="step-num">05</div>
                    <h4>Registration</h4>'''
html = html.replace(old_step5, new_step5)

# Update Step 06
old_step6 = '''<div class="step-num">06</div>
                    <h4>Publish & Present</h4>'''
new_step6 = '''<div class="step-num">06</div>
                    <h4>Presentation</h4>'''
html = html.replace(old_step6, new_step6)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

