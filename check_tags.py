from html.parser import HTMLParser

class TagParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_elements = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag not in self.void_elements:
            if self.stack and self.stack[-1] == tag:
                self.stack.pop()
            else:
                print(f"Mismatched tag: expected {self.stack[-1] if self.stack else 'NONE'}, got {tag}")

with open('index.html', 'r', encoding='utf-8') as f:
    parser = TagParser()
    parser.feed(f.read())
    if parser.stack:
        print(f"Unclosed tags remaining: {parser.stack}")
    else:
        print("All tags balanced!")
