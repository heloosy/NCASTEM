with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# count braces
open_braces = css.count('{')
close_braces = css.count('}')
print(f'Open braces: {open_braces}, Close braces: {close_braces}')
