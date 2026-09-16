import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# I will find the block starting with <div class="dept-card fade-up"> containing AIML
# and ending at the </div> before </div> </div> </section>

old_html_regex = r'<div class="dept-card fade-up">\s*<i class="fas fa-brain dept-icon text-accent-alt"></i>\s*<h3>Department of AIML</h3>.*?</div>\s*</div>'

new_html = '''<div class="dept-card fade-up">
                    <i class="fas fa-brain dept-icon text-accent-alt"></i>
                    <h3>Department of AIML</h3>
                    <p class="text-muted">Department of Artificial Intelligence & Machine Learning was established at T. John Institute of Technology in the year 2022. The courses are offered under the auspices of VTU and are recognized by Govt. of Karnataka and AICTE, New Delhi.</p>
                    <p class="text-muted">The department seeks to excel as a technology hub processing research and educating students in current technological developments. It is equipped with the state of the art infrastructure and supported by a team of dedicated and qualified staff members.</p>
                    <div class="dept-vision mt-4">
                        <h5 class="mb-2"><i class="far fa-eye text-accent-alt"></i> Vision</h5>
                        <p class="text-muted">To enrich students with Artificial Intelligence and Machine Learning skills, fostering a culture of research, innovation, and development, thereby empowering them to efficiently address dynamic and evolving societal challenges.</p>
                    </div>
                    <details class="mission-details mt-3">
                        <summary><span style="display: flex; align-items: center; gap: 8px;"><i class="fas fa-bullseye text-accent-alt"></i> Our Mission</span></summary>
                        <div class="mission-content">
                            <p class="text-muted mb-2"><strong>M1.</strong> To provide comprehensive education in Artificial Intelligence and Machine Learning, equipping students with the skills and knowledge to excel in their careers and contribute meaningfully to the field.</p>
                            <p class="text-muted mb-2"><strong>M2.</strong> To foster a culture of research and innovation by encouraging students to engage in cutting-edge projects, publish their findings, and develop novel AI and ML solutions to address complex real-world problems.</p>
                            <p class="text-muted mb-2"><strong>M3.</strong> To establish strong industry partnerships, enhancing students' practical experience and prepare them for the tech world.</p>
                            <p class="text-muted mb-0"><strong>M4.</strong> To empower students to apply their AI and ML expertise to drive societal progress and address dynamic challenges in various sectors.</p>
                        </div>
                    </details>
                </div>
                
                <div class="dept-card fade-up delay-1">
                    <i class="fas fa-sitemap dept-icon text-accent-alt"></i>
                    <h3>Department of ISE</h3>
                    <p class="text-muted">The Information Science Department at TJIT was established in 2007. It offers B.E in Information Science under the auspices of VTU and recognized by AICTE. Every year the department has an intake of 60 students each BE Information Science Engineering (ISE).</p>
                    <div class="dept-vision mt-4">
                        <h5 class="mb-2"><i class="far fa-eye text-accent-alt"></i> Vision</h5>
                        <p class="text-muted">To achieve excellence in delivering quality education of global standards, coupled with innovative practices using advanced technology and expertise, transforming the student community in to potential global leaders with accountability to meet societal, national and dynamic global challenges.</p>
                    </div>
                    <details class="mission-details mt-3">
                        <summary><span style="display: flex; align-items: center; gap: 8px;"><i class="fas fa-bullseye text-accent-alt"></i> Our Mission</span></summary>
                        <div class="mission-content">
                            <p class="text-muted mb-0">To practice outstanding computing professionals in area of Information Science and Engineering and also help the student in appreciating the complete spectrum of computer concepts and effectively training them in the five pillars of Information Technology namely Networking, Programming, Human Computer, Interaction, Databases and Web Systems.</p>
                        </div>
                    </details>
                </div>'''

html = re.sub(old_html_regex, new_html, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

