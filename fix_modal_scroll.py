import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix modal-overlay
old_overlay = '''.modal-overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(5px);
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s ease;
}'''
new_overlay = '''.modal-overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(5px);
    z-index: 9999;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    overflow-y: auto;
    padding: 2rem 1rem;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s ease;
}'''
css = css.replace(old_overlay, new_overlay)

# Fix modal-content
old_content = '''.modal-content {
    background: #ffffff;
    border-radius: 12px;
    padding: 3rem;
    width: 90%;
    max-width: 800px;
    position: relative;
    transform: translateY(20px);
    transition: transform 0.3s ease;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
}'''
new_content = '''.modal-content {
    background: #ffffff;
    border-radius: 12px;
    padding: 3rem;
    width: 100%;
    max-width: 800px;
    margin: auto;
    position: relative;
    transform: translateY(20px);
    transition: transform 0.3s ease;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
}'''
css = css.replace(old_content, new_content)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

