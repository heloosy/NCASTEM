import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace root variables
new_root = ''':root {
    /* Color Palette - Premium Light */
    --bg-main: #ffffff;
    --bg-alt: #f8fafc;
    --bg-card: #ffffff;
    --bg-card-hover: #f1f5f9;
    
    --text-main: #0f172a;
    --text-muted: #475569;
    
    --accent: #1e3a8a;
    --accent-hover: #1e40af;
    --accent-alt: #d68910;
    
    --border-color: rgba(0, 0, 0, 0.1);
    --border-hover: rgba(30, 58, 138, 0.3);
    
    /* Typography */
    --font-heading: 'Space Grotesk', sans-serif;
    --font-body: 'Inter', sans-serif;
    --font-logo: 'Cinzel', serif;
    
    /* Transitions */
    --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}'''
css = re.sub(r':root\s*\{[^}]+\}', new_root, css, count=1)

# Fix button colors
css = css.replace('color: #000;', 'color: #ffffff;') # btn-primary text
css = css.replace('background-color: rgba(255, 255, 255, 0.05);', 'background-color: rgba(0, 0, 0, 0.05);') # outline light hover

# Fix Navbar
css = css.replace('background-color: rgba(5, 10, 21, 0.95);', 'background-color: rgba(255, 255, 255, 0.95);')
css = css.replace('background-color: var(--bg-main);', 'background-color: #ffffff;')

# Fix Hero Overlay
css = css.replace('background: linear-gradient(135deg, rgba(5, 10, 21, 0.95) 0%, rgba(5, 10, 21, 0.8) 100%);', 'background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(255, 255, 255, 0.8) 100%);')

# Fix Theme numbers
css = css.replace('color: rgba(255,255,255,0.05);', 'color: rgba(0,0,0,0.05);')
css = css.replace('color: rgba(0, 229, 255, 0.1);', 'color: rgba(30, 58, 138, 0.1);')

# Fix Glance Strip
css = css.replace('background-color: rgba(10, 15, 31, 0.5);', 'background-color: rgba(248, 250, 252, 0.8);')

# Fix Timeline nodes
css = css.replace('box-shadow: 0 0 15px rgba(0,229,255,0.5);', 'box-shadow: 0 0 15px rgba(30, 58, 138, 0.3);')

# Fix Registration Popular badge
css = css.replace('background-color: rgba(0, 229, 255, 0.02);', 'background-color: rgba(30, 58, 138, 0.03);')

# Fix Final CTA Overlay
css = css.replace('background: linear-gradient(0deg, rgba(5, 10, 21, 1) 0%, rgba(5, 10, 21, 0.8) 50%, rgba(5, 10, 21, 1) 100%);', 'background: linear-gradient(0deg, rgba(255, 255, 255, 1) 0%, rgba(255, 255, 255, 0.8) 50%, rgba(255, 255, 255, 1) 100%);')

# Fix Box Shadows
css = css.replace('box-shadow: 0 10px 20px rgba(0, 229, 255, 0.2);', 'box-shadow: 0 10px 20px rgba(30, 58, 138, 0.2);')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
