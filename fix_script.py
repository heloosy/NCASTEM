clean_js = '''document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Navbar Scroll Effect
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 2. Mobile Menu Toggle
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    
    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.classList.toggle('active');
        });
        
        document.querySelectorAll('.nav-links a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                hamburger.classList.remove('active');
            });
        });
    }

    // 3. Scroll Reveal Animations (.fade-up)
    const revealElements = document.querySelectorAll('.fade-up');
    
    const revealOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };
    
    const revealOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);
    
    revealElements.forEach(el => {
        revealOnScroll.observe(el);
    });

    // 4. FAQ Accordion Logic
    const faqItems = document.querySelectorAll('.faq-item');
    
    faqItems.forEach(item => {
        const questionBtn = item.querySelector('.faq-question');
        const answerDiv = item.querySelector('.faq-answer');
        
        if (questionBtn && answerDiv) {
            questionBtn.addEventListener('click', () => {
                const isOpen = item.classList.contains('active');
                
                faqItems.forEach(otherItem => {
                    otherItem.classList.remove('active');
                    const otherAnswer = otherItem.querySelector('.faq-answer');
                    if(otherAnswer) otherAnswer.style.maxHeight = null;
                });
                
                if (!isOpen) {
                    item.classList.add('active');
                    answerDiv.style.maxHeight = answerDiv.scrollHeight + "px";
                }
            });
        }
    });
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if(targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                const headerOffset = 80;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
  
                window.scrollTo({
                    top: offsetPosition,
                    behavior: "smooth"
                });
            }
        });
    });

    // 5. Countdown Logic
    const targetDate = new Date('October 30, 2026 09:00:00').getTime();
    const daysEl = document.getElementById('cd-days');
    const hoursEl = document.getElementById('cd-hours');
    const minsEl = document.getElementById('cd-minutes');
    const secsEl = document.getElementById('cd-seconds');

    if(daysEl && hoursEl && minsEl && secsEl) {
        function updateCountdown() {
            const now = new Date().getTime();
            const distance = targetDate - now;

            if (distance < 0) {
                daysEl.innerText = '00';
                hoursEl.innerText = '00';
                minsEl.innerText = '00';
                secsEl.innerText = '00';
                return;
            }

            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            daysEl.innerText = days < 10 ? '0' + days : days;
            hoursEl.innerText = hours < 10 ? '0' + hours : hours;
            minsEl.innerText = minutes < 10 ? '0' + minutes : minutes;
            secsEl.innerText = seconds < 10 ? '0' + seconds : seconds;
        }

        updateCountdown();
        setInterval(updateCountdown, 1000);
    }

    // 6. Registration Modal Logic
    const modal = document.getElementById('registerModal');
    const closeBtn = document.getElementById('closeModal');
    const triggers = document.querySelectorAll('.register-trigger');

    if (modal && closeBtn) {
        // Open modal
        triggers.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                modal.classList.add('active');
            });
        });

        // Close modal on X click
        closeBtn.addEventListener('click', () => {
            modal.classList.remove('active');
        });

        // Close modal on outside click
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('active');
            }
        });
    }

    // 7. Pricing Carousel Logic
    const carouselTrack = document.getElementById('pricingTrack');
    const prevBtn = document.getElementById('carouselPrev');
    const nextBtn = document.getElementById('carouselNext');

    if(carouselTrack && prevBtn && nextBtn) {
        prevBtn.addEventListener('click', () => {
            carouselTrack.scrollBy({ left: -300, behavior: 'smooth' });
        });
        nextBtn.addEventListener('click', () => {
            carouselTrack.scrollBy({ left: 300, behavior: 'smooth' });
        });
    }

});
'''

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(clean_js)

