with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

open_braces = js.count('{')
close_braces = js.count('}')
print(f'Open braces: {open_braces}, Close braces: {close_braces}')
