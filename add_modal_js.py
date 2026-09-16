import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

modal_js = '''
    // 6. Registration Modal Logic
    const modal = document.getElementById('registerModal');
    const closeBtn = document.getElementById('closeModal');
    const triggers = document.querySelectorAll('.register-trigger');

    if (modal && closeBtn) {
        // Open modal
        triggers.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                modal.classList.add('active');
            });
        });

        // Close modal on X click
        closeBtn.addEventListener('click', () => {
            modal.classList.remove('active');
        });

        // Close modal on outside click
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('active');
            }
        });
    }
'''

# Find the closing brace of DOMContentLoaded and inject the modal logic before it
js = js.replace('});\n', modal_js + '\n});\n')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

