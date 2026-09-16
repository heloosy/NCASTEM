import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

tabs_js = '''
// Global function for Department Tabs
function switchDeptTab(element, tabName) {
    const container = element.closest('.dept-tabs');
    if (!container) return;
    
    // Remove active class from all labels
    const labels = container.querySelectorAll('.dept-tab-label');
    labels.forEach(label => label.classList.remove('active'));
    
    // Add active class to clicked label
    element.classList.add('active');
    
    // Hide all contents
    const contents = container.querySelectorAll('.dept-tab-content');
    contents.forEach(content => content.classList.remove('active'));
    
    // Show target content
    const targetContent = container.querySelector('.' + tabName + '-content');
    if (targetContent) {
        targetContent.classList.add('active');
    }
}
'''

js = js + tabs_js

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

