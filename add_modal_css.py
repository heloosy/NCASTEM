import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

modal_css = '''
/* Modal Styles */
.modal-overlay {
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
}
.modal-overlay.active {
    opacity: 1;
    pointer-events: auto;
}
.modal-content {
    background: #ffffff;
    border-radius: 12px;
    padding: 3rem;
    width: 90%;
    max-width: 800px;
    position: relative;
    transform: translateY(20px);
    transition: transform 0.3s ease;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
}
.modal-overlay.active .modal-content {
    transform: translateY(0);
}
.modal-close {
    position: absolute;
    top: 1.5rem;
    right: 1.5rem;
    background: transparent;
    border: none;
    font-size: 2rem;
    line-height: 1;
    color: var(--text-muted);
    cursor: pointer;
    transition: color 0.3s ease;
}
.modal-close:hover {
    color: var(--primary);
}
.modal-title {
    font-family: var(--font-heading);
    color: var(--primary);
    font-size: 2rem;
    margin-bottom: 0.5rem;
    text-align: center;
}
.modal-subtitle {
    text-align: center;
}
.modal-steps-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    margin-top: 2rem;
}
.modal-step {
    background: var(--bg-alt);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 2rem;
    text-align: center;
}
.step-header {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 1rem;
}
.step-badge {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: var(--accent);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
}
.step-header h4 {
    margin: 0;
    color: var(--primary);
}
.qr-container {
    background: white;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    display: inline-block;
}
.qr-code {
    width: 200px;
    height: 200px;
    object-fit: contain;
}

@media (max-width: 768px) {
    .modal-content {
        padding: 2rem 1.5rem;
    }
    .modal-steps-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }
    .qr-code {
        width: 150px;
        height: 150px;
    }
}
'''

css = css + modal_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

