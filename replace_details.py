import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace AIML Details
aiml_old = '''<details class="mission-details mt-3">
                        <summary><span style="display: flex; align-items: center; gap: 8px;"><i class="fas fa-bullseye text-accent-alt"></i> Our Mission</span></summary>
                        <div class="mission-content">
                            <p class="text-muted mb-2"><strong>M1.</strong> To provide comprehensive education in Artificial Intelligence and Machine Learning, equipping students with the skills and knowledge to excel in their careers and contribute meaningfully to the field.</p>
                            <p class="text-muted mb-2"><strong>M2.</strong> To foster a culture of research and innovation by encouraging students to engage in cutting-edge projects, publish their findings, and develop novel AI and ML solutions to address complex real-world problems.</p>
                            <p class="text-muted mb-2"><strong>M3.</strong> To establish strong industry partnerships, enhancing students' practical experience and prepare them for the tech world.</p>
                            <p class="text-muted mb-0"><strong>M4.</strong> To empower students to apply their AI and ML expertise to drive societal progress and address dynamic challenges in various sectors.</p>
                        </div>
                    </details>'''
aiml_new = '''<div class="dept-mission mt-3">
                        <h5 class="mb-2"><i class="fas fa-bullseye"></i> Mission</h5>
                        <p class="text-muted mb-2"><strong>M1.</strong> To provide comprehensive education in Artificial Intelligence and Machine Learning, equipping students with the skills and knowledge to excel in their careers and contribute meaningfully to the field.</p>
                        <p class="text-muted mb-2"><strong>M2.</strong> To foster a culture of research and innovation by encouraging students to engage in cutting-edge projects, publish their findings, and develop novel AI and ML solutions to address complex real-world problems.</p>
                        <p class="text-muted mb-2"><strong>M3.</strong> To establish strong industry partnerships, enhancing students' practical experience and prepare them for the tech world.</p>
                        <p class="text-muted mb-0"><strong>M4.</strong> To empower students to apply their AI and ML expertise to drive societal progress and address dynamic challenges in various sectors.</p>
                    </div>'''

html = html.replace(aiml_old, aiml_new)

# Replace ISE Details
ise_old = '''<details class="mission-details mt-3">
                        <summary><span style="display: flex; align-items: center; gap: 8px;"><i class="fas fa-bullseye text-accent-alt"></i> Our Mission</span></summary>
                        <div class="mission-content">
                            <p class="text-muted mb-0">To practice outstanding computing professionals in area of Information Science and Engineering and also help the student in appreciating the complete spectrum of computer concepts and effectively training them in the five pillars of Information Technology namely Networking, Programming, Human Computer, Interaction, Databases and Web Systems.</p>
                        </div>
                    </details>'''
ise_new = '''<div class="dept-mission mt-3">
                        <h5 class="mb-2"><i class="fas fa-bullseye"></i> Mission</h5>
                        <p class="text-muted mb-0">To practice outstanding computing professionals in area of Information Science and Engineering and also help the student in appreciating the complete spectrum of computer concepts and effectively training them in the five pillars of Information Technology namely Networking, Programming, Human Computer, Interaction, Databases and Web Systems.</p>
                    </div>'''

html = html.replace(ise_old, ise_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

