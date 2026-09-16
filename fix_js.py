import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# The duplicate block starts at '// 5. Countdown Logic' and goes to the end.
# We will just split by '// 5. Countdown Logic' and only keep the first one.
parts = js.split('// 5. Countdown Logic')

if len(parts) > 2:
    # re-assemble using only the first split (before the first occurrence) and the second split (the first occurrence block)
    fixed_js = parts[0] + '// 5. Countdown Logic' + parts[1] + '\n});\n'
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(fixed_js)
