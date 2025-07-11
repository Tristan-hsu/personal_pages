// Main JavaScript file for the portfolio website

document.addEventListener('DOMContentLoaded', function() {
    // Initialize components
    initializeNavigation();
    initializeScrollEffects();
    initializeAnimations();
    initializeContactForm();
    loadGitHubStats();
});

// Navigation functionality
function initializeNavigation() {
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    const sections = document.querySelectorAll('section[id]');
    
    // Update active navigation link on scroll
    window.addEventListener('scroll', function() {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (pageYOffset >= sectionTop - 200) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    });
    
    // Smooth scrolling for navigation links
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            if (this.getAttribute('href').startsWith('#')) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
}

// Scroll effects
function initializeScrollEffects() {
    // Navbar background on scroll
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
    
    // Parallax effect for hero section
    const heroSection = document.querySelector('.hero-section');
    if (heroSection) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const parallax = scrolled * 0.5;
            heroSection.style.transform = `translateY(${parallax}px)`;
        });
    }
}

// Animations
function initializeAnimations() {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
            }
        });
    }, observerOptions);
    
    // Observe cards and timeline items
    document.querySelectorAll('.card, .timeline-item').forEach(el => {
        observer.observe(el);
    });
    
    // Counter animation for stats
    animateCounters();
}

// Counter animation
function animateCounters() {
    const counters = document.querySelectorAll('[data-count]');
    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-count'));
        const increment = target / 100;
        let current = 0;
        
        const updateCounter = () => {
            if (current < target) {
                current += increment;
                counter.textContent = Math.ceil(current);
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target;
            }
        };
        
        // Start animation when element is visible
        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    updateCounter();
                    observer.unobserve(entry.target);
                }
            });
        });
        
        observer.observe(counter);
    });
}

// Contact form handling
function initializeContactForm() {
    const contactForm = document.querySelector('#contact form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            const submitButton = this.querySelector('button[type="submit"]');
            const originalText = submitButton.innerHTML;
            
            // Show loading state
            submitButton.innerHTML = '<span class="loading"></span> Sending...';
            submitButton.disabled = true;
            
            // Reset button after 3 seconds (form will redirect on success)
            setTimeout(() => {
                submitButton.innerHTML = originalText;
                submitButton.disabled = false;
            }, 3000);
        });
    }
}

// GitHub stats loading
function loadGitHubStats() {
    fetch('/api/github-stats')
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                console.warn('GitHub stats not available:', data.error);
                return;
            }
            
            // Update GitHub stats display
            updateGitHubStats(data);
        })
        .catch(error => {
            console.warn('Failed to load GitHub stats:', error);
        });
}

// Update GitHub stats in UI
function updateGitHubStats(stats) {
    const statsContainer = document.querySelector('.github-stats');
    if (statsContainer && stats) {
        // Update repositories count
        const repoCount = statsContainer.querySelector('.repo-count');
        if (repoCount) {
            repoCount.textContent = stats.total_repos;
        }
        
        // Update stars count
        const starsCount = statsContainer.querySelector('.stars-count');
        if (starsCount) {
            starsCount.textContent = stats.total_stars;
        }
        
        // Update forks count
        const forksCount = statsContainer.querySelector('.forks-count');
        if (forksCount) {
            forksCount.textContent = stats.total_forks;
        }
        
        // Update top languages
        const languagesContainer = statsContainer.querySelector('.top-languages');
        if (languagesContainer && stats.languages) {
            const topLanguages = Object.entries(stats.languages)
                .sort(([,a], [,b]) => b - a)
                .slice(0, 5)
                .map(([lang]) => lang);
            
            languagesContainer.innerHTML = topLanguages
                .map(lang => `<span class="badge bg-primary me-1">${lang}</span>`)
                .join('');
        }
    }
}

// Utility functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Add scroll event listener with debounce
window.addEventListener('scroll', debounce(() => {
    // Handle scroll events
    const scrollTop = window.pageYOffset;
    
    // Add/remove classes based on scroll position
    if (scrollTop > 100) {
        document.body.classList.add('scrolled');
    } else {
        document.body.classList.remove('scrolled');
    }
}, 10));

// Handle form validation
function validateForm(form) {
    const inputs = form.querySelectorAll('input[required], textarea[required]');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            input.classList.add('is-invalid');
        } else {
            input.classList.remove('is-invalid');
        }
    });
    
    return isValid;
}

// Add fade-in animation class
const style = document.createElement('style');
style.textContent = `
    .animate-fade-in {
        animation: fadeIn 0.8s ease-in-out;
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(style);

// Handle external links
document.addEventListener('click', function(e) {
    if (e.target.tagName === 'A' && e.target.getAttribute('href')?.startsWith('http')) {
        e.target.setAttribute('rel', 'noopener noreferrer');
    }
});

// Error handling for images
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('img');
    images.forEach(img => {
        img.addEventListener('error', function() {
            this.style.display = 'none';
        });
    });
});
