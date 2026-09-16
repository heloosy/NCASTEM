import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# AIML Card
aiml_old = '''<div class="dept-vision">
                        <h5><i class="far fa-eye text-accent-alt"></i> Vision</h5>
                        <p class="text-muted">To enrich students with Artificial Intelligence and Machine Learning skills, fostering a culture of research, innovation, and development, thereby empowering them to efficiently address dynamic and evolving societal challenges.</p>
                    </div>
                    <div class="dept-mission mt-3">
                        <h5 class="mb-2"><i class="fas fa-bullseye"></i> Mission</h5>
                        <p class="text-muted mb-2"><strong>M1.</strong> To provide comprehensive education in Artificial Intelligence and Machine Learning, equipping students with the skills and knowledge to excel in their careers and contribute meaningfully to the field.</p>
                        <p class="text-muted mb-2"><strong>M2.</strong> To foster a culture of research and innovation by encouraging students to engage in cutting-edge projects, publish their findings, and develop novel AI and ML solutions to address complex real-world problems.</p>
                        <p class="text-muted mb-2"><strong>M3.</strong> To establish strong industry partnerships, enhancing students' practical experience and prepare them for the tech world.</p>
                        <p class="text-muted mb-0"><strong>M4.</strong> To empower students to apply their AI and ML expertise to drive societal progress and address dynamic challenges in various sectors.</p>
                    </div>'''

aiml_new = '''<div class="dept-tabs mt-4">
                        <div class="dept-tab-controls">
                            <div class="dept-tab-label active" onclick="switchDeptTab(this, 'vision')"><i class="far fa-eye"></i> Vision</div>
                            <div class="dept-tab-label" onclick="switchDeptTab(this, 'mission')"><i class="fas fa-bullseye"></i> Mission</div>
                        </div>
                        <div class="dept-tab-content vision-content active">
                            <p class="text-muted mb-0">To enrich students with Artificial Intelligence and Machine Learning skills, fostering a culture of research, innovation, and development, thereby empowering them to efficiently address dynamic and evolving societal challenges.</p>
                        </div>
                        <div class="dept-tab-content mission-content">
                            <p class="text-muted mb-2"><strong>M1.</strong> To provide comprehensive education in AI and ML, equipping students with skills to excel in their careers.</p>
                            <p class="text-muted mb-2"><strong>M2.</strong> To foster a culture of research and innovation by encouraging cutting-edge projects and developing novel AI/ML solutions.</p>
                            <p class="text-muted mb-2"><strong>M3.</strong> To establish strong industry partnerships to prepare students for the tech world.</p>
                            <p class="text-muted mb-0"><strong>M4.</strong> To empower students to drive societal progress and address dynamic challenges.</p>
                        </div>
                    </div>'''
                    
html = html.replace(aiml_old, aiml_new)

# ISE Card
ise_old = '''<div class="dept-vision">
                        <h5><i class="far fa-eye text-accent-alt"></i> Vision</h5>
                        <p class="text-muted">To achieve excellence in delivering quality education of global standards, coupled with innovative practices using advanced technology and expertise, transforming the student community in to potential global leaders with accountability to meet societal, national and dynamic global challenges.</p>
                    </div>
                    <div class="dept-mission mt-3">
                        <h5 class="mb-2"><i class="fas fa-bullseye"></i> Mission</h5>
                        <p class="text-muted mb-0">To practice outstanding computing professionals in area of Information Science and Engineering and also help the student in appreciating the complete spectrum of computer concepts and effectively training them in the five pillars of Information Technology namely Networking, Programming, Human Computer, Interaction, Databases and Web Systems.</p>
                    </div>'''

ise_new = '''<div class="dept-tabs mt-4">
                        <div class="dept-tab-controls">
                            <div class="dept-tab-label active" onclick="switchDeptTab(this, 'vision')"><i class="far fa-eye"></i> Vision</div>
                            <div class="dept-tab-label" onclick="switchDeptTab(this, 'mission')"><i class="fas fa-bullseye"></i> Mission</div>
                        </div>
                        <div class="dept-tab-content vision-content active">
                            <p class="text-muted mb-0">To achieve excellence in delivering quality education of global standards, coupled with innovative practices using advanced technology and expertise, transforming the student community in to potential global leaders with accountability to meet societal, national and dynamic global challenges.</p>
                        </div>
                        <div class="dept-tab-content mission-content">
                            <p class="text-muted mb-0">To practice outstanding computing professionals in area of Information Science and Engineering and also help the student in appreciating the complete spectrum of computer concepts and effectively training them in the five pillars of Information Technology namely Networking, Programming, Human Computer, Interaction, Databases and Web Systems.</p>
                        </div>
                    </div>'''

html = html.replace(ise_old, ise_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

