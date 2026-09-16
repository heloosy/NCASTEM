import re

html_to_inject = '''
    <!-- 3.5 About TJIT & Departments -->
    <section class="section about-tjit-section bg-alt">
        <div class="container">
            <!-- About TJIT -->
            <div class="section-header fade-up" style="margin-bottom: 2rem;">
                <h2 class="section-title">About <span class="text-accent-alt">TJIT</span></h2>
            </div>
            
            <div class="tjit-content fade-up" style="margin-bottom: 5rem;">
                <p class="lead-text text-muted" style="max-width: 1000px; margin-bottom: 3rem; font-size: 1.1rem; line-height: 1.8;">
                    T. John Institute of Technology (TJIT) is a premier private Engineering College located in Bangalore, Karnataka. Established in 2006 by Dr. Thomas P. John, the institute is affiliated to VTU and approved by AICTE. We impart science-based engineering education to develop professional skills, preparing students for immediate employment and lifelong learning.
                </p>
                
                <div class="vm-grid">
                    <div class="vm-card fade-up delay-1">
                        <div class="vm-header">
                            <i class="far fa-eye text-accent-alt"></i>
                            <h4>Vision</h4>
                        </div>
                        <p class="text-muted">To achieve excellence in delivering quality education of global standards, coupled with innovative practices using advanced technology and expertise. We aim to transform the student community into potential global leaders ready to meet dynamic global challenges.</p>
                    </div>
                    
                    <div class="vm-card fade-up delay-2">
                        <div class="vm-header">
                            <i class="fas fa-rocket text-accent-alt"></i>
                            <h4>Mission</h4>
                        </div>
                        <p class="text-muted">To bring about overall personality development by fostering a caring and creative environment. We strive to instill remarkable resilience and adaptation to a competitive society through lifelong learning, employment, and entrepreneurship.</p>
                    </div>
                </div>
                
                <div class="text-center mt-5 fade-up delay-3" style="margin-top: 3rem; text-align: center;">
                    <a href="https://www.google.com/maps/dir//VH2W%2B33X+T+John+Institute+Of+Technology,+%2386%2F1,+Gottigere,+Bannerghatta+Road,+Bohra+Layout,+Gottigere,+Doddakammanahalli,+Basavanapura,+Bengaluru,+Karnataka+560083/data=!4m6!4m5!1m1!4e2!1m2!1m1!1s0x3bae6ac114cdcaf3:0xf645f28fa98fbd74?sa=X&ved=1t:57443&ictx=111" target="_blank" class="btn btn-primary" style="border-radius: 30px;">
                        <i class="fas fa-map-marker-alt" style="color: white;"></i> VIEW COLLEGE ON MAP
                    </a>
                </div>
            </div>
            
            <!-- Departments -->
            <div class="dept-grid mt-5">
                <div class="dept-card fade-up">
                    <i class="fas fa-brain dept-icon text-accent-alt"></i>
                    <h3>Department of AIML</h3>
                    <p class="text-muted">Established in 2022, the AI & ML department seeks to excel as a technology hub, processing research and educating students in current technological developments. It is equipped with state-of-the-art infrastructure.</p>
                    <div class="dept-vision">
                        <h5><i class="far fa-eye text-accent-alt"></i> Vision</h5>
                        <p class="text-muted">To enrich students with AI and ML skills, fostering a culture of research, innovation, and development to address societal challenges.</p>
                    </div>
                </div>
                
                <div class="dept-card fade-up delay-1">
                    <i class="fas fa-sitemap dept-icon text-accent-alt"></i>
                    <h3>Department of ISE</h3>
                    <p class="text-muted">Established in 2007 with an intake of 60 students, the Information Science Department offers B.E under VTU, recognized by AICTE. It aims to transform students into potential global leaders.</p>
                    <div class="dept-vision">
                        <h5><i class="far fa-eye text-accent-alt"></i> Vision</h5>
                        <p class="text-muted">To achieve excellence in delivering quality education of global standards, coupled with innovative practices using advanced technology.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 4. Conference Themes -->
'''

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<!-- 4. Conference Themes -->', html_to_inject)

# Also fix the themes section bg-alt to just be normal bg so it alternates properly
html = html.replace('<section id="themes" class="section themes-section bg-alt">', '<section id="themes" class="section themes-section">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
