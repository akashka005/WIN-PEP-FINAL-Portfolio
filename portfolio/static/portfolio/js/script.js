document.addEventListener('DOMContentLoaded', function () {
    const themeToggle = document.getElementById('theme-toggle');
    const themeIcon = themeToggle.querySelector('i');

    const savedTheme = localStorage.getItem('theme') || 'light';
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-theme');
        themeIcon.classList.replace('fa-moon', 'fa-sun');
    }

    themeToggle.addEventListener('click', function () {
        document.body.classList.toggle('dark-theme');

        if (document.body.classList.contains('dark-theme')) {
            localStorage.setItem('theme', 'dark');
            themeIcon.classList.replace('fa-moon', 'fa-sun');
        } else {
            localStorage.setItem('theme', 'light');
            themeIcon.classList.replace('fa-sun', 'fa-moon');
        }
    });

    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('.nav-menu');

    menuToggle.addEventListener('click', function () {
        navMenu.classList.toggle('active');
        this.innerHTML = navMenu.classList.contains('active')
            ? '<i class="fas fa-times"></i>'
            : '<i class="fas fa-bars"></i>';
    });

    document.addEventListener('click', function (event) {
        if (!event.target.closest('.nav') && navMenu.classList.contains('active')) {
            navMenu.classList.remove('active');
            menuToggle.innerHTML = '<i class="fas fa-bars"></i>';
        }
    });
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                const offset = 80;
                const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - offset;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                navMenu.classList.remove('active');
                menuToggle.innerHTML = '<i class="fas fa-bars"></i>';
            }
        });
    });

    const counters = document.querySelectorAll('.stat-number');

    const animateCounter = (counter) => {
        const target = parseInt(counter.getAttribute('data-count'));
        const duration = 1500;
        const increment = target / (duration / 16);
        let current = 0;

        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                counter.textContent = target;
                clearInterval(timer);
            } else {
                counter.textContent = Math.floor(current);
            }
        }, 16);
    };
    const skillBars = document.querySelectorAll('.skill-level');

    const animateSkillBars = () => {
        skillBars.forEach(bar => {
            const level = bar.getAttribute('data-level');
            bar.style.width = level + '%';
        });
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');

                if (entry.target.id === 'home') {
                    counters.forEach(animateCounter);
                }

                if (entry.target.id === 'skills') {
                    animateSkillBars();
                }
            }
        });
    }, { threshold: 0.3 });

    document.querySelectorAll('section').forEach(section => {
        observer.observe(section);
    });

    const projectDetailsButtons = document.querySelectorAll('.view-details');
    const modal = document.getElementById('project-modal');
    const closeModal = document.querySelector('.close-modal');

    projectDetailsButtons.forEach(button => {
        button.addEventListener('click', function () {
            const project = {
                title: this.getAttribute('data-title'),
                date: this.getAttribute('data-date'),
                description: this.getAttribute('data-description'),
                details: this.getAttribute('data-details'),
                tech: this.getAttribute('data-tech').split(','),
                github: this.getAttribute('data-github')
            };

            const modalBody = document.getElementById('modal-body');

            modalBody.innerHTML = `
                <h2>${project.title}</h2>
                <p class="modal-date">${project.date}</p>
                
                <div class="modal-section" style="margin-top: 20px;">
                    <h3>Description</h3>
                    <p style="margin-top: 10px;">${project.description}</p>
                    <p style="margin-top: 10px;">${project.details}</p>
                </div>
                
                <div class="modal-section" style="margin-top: 20px;">
                    <h3>Technologies</h3>
                    <div class="modal-tech" style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px;">
                        ${project.tech.map(tech => `<span class="tech-tag" style="padding: 4px 10px; background: var(--bg-secondary); border: 1px solid var(--border-primary); border-radius: 4px; font-size: 12px;">${tech.trim()}</span>`).join('')}
                    </div>
                </div>
                
                <div class="modal-actions" style="margin-top: 30px; display: flex; gap: 10px;">
                    ${project.github ? `
                    <a href="${project.github}" target="_blank" class="btn btn-primary">
                        <i class="fab fa-github"></i> View Code
                    </a>` : ''}
                    <button class="btn btn-outline close-modal-btn">Close</button>
                </div>
            `;

            modal.style.display = 'block';
            document.body.style.overflow = 'hidden';

            document.querySelector('.close-modal-btn')?.addEventListener('click', () => {
                modal.style.display = 'none';
                document.body.style.overflow = 'auto';
            });
        });
    });

    closeModal.addEventListener('click', () => {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    });

    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });

    const contactForm = document.getElementById('contact-form');

    if (contactForm && !contactForm.hasAttribute('action')) {
        contactForm.addEventListener('submit', function (e) {
            const submitBtn = this.querySelector('button[type="submit"]');
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
        });
    }
    
    const resumeBtn = document.getElementById('resume-btn');
        if (resumeBtn) {
            resumeBtn.addEventListener('click', function (e) {
                e.preventDefault();
                const pdfUrl = this.href;
                const originalText = this.innerHTML;
                this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Downloading...';
                fetch(pdfUrl)
                .then(response => response.blob())
                .then(blob => {
                    const blobUrl = window.URL.createObjectURL(blob);
                    const link = document.createElement('a');
                    link.href = blobUrl;
                    link.download = 'Akash Resume.pdf';
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);
                    window.URL.revokeObjectURL(blobUrl);
                    this.innerHTML = '<i class="fas fa-check"></i> Downloaded';
                    setTimeout(() => {
                        this.innerHTML = originalText;
                    }, 2000);
                })
                .catch(error => {
                    console.error('Download failed:', error);
                    this.innerHTML = '<i class="fas fa-exclamation-circle"></i> Failed';
                    setTimeout(() => {
                        this.innerHTML = originalText;
                    }, 2000);
                });
            });
        
        }
    const backToTop = document.querySelector('.back-to-top');

    window.addEventListener('scroll', function () {
        if (window.pageYOffset > 300) {
            backToTop.classList.add('visible');
        } else {
            backToTop.classList.remove('visible');
        }
    });

    backToTop.addEventListener('click', function () {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    window.addEventListener('load', function () {
        setTimeout(() => {
            counters.forEach(animateCounter);
        }, 500);
    });
});