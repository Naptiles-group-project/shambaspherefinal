// ==========================
// Hero Carousel Logic
// ==========================
let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');

function showSlide(index) {
    slides.forEach(slide => slide.classList.remove('active'));
    slides[index].classList.add('active');
}

// Prev/Next Button Events
prevBtn.addEventListener('click', () => {
    currentSlide = (currentSlide === 0) ? slides.length -1 : currentSlide -1;
    showSlide(currentSlide);
});

nextBtn.addEventListener('click', () => {
    currentSlide = (currentSlide +1) % slides.length;
    showSlide(currentSlide);
});

// Auto-slide every 5 seconds
setInterval(() => {
    currentSlide = (currentSlide +1) % slides.length;
    showSlide(currentSlide);
}, 5000);

// ==========================
// Scroll Animation for Feature Cards
// ==========================
const fCards = document.querySelectorAll('.feature-card');
function checkFadeIn() {
    fCards.forEach(card => {
        const rect = card.getBoundingClientRect();
        if(rect.top < window.innerHeight - 50) {
            card.classList.add('fade-in', 'visible');
        }
    });
}
window.addEventListener('scroll', checkFadeIn);
checkFadeIn(); // Run on page load

// ==========================
// Learn More Button Smooth Scroll
// ==========================
document.getElementById('learnMoreBtn').addEventListener('click', () => {
    window.scrollTo({
        top: document.getElementById('features').offsetTop,
        behavior: 'smooth'
    });
});

// ==========================
// Role-based Form Injection
// ==========================
const formContainer = document.getElementById('form-container');
const roleButtons = document.querySelectorAll('.role-btn');

roleButtons.forEach(btn => {
    btn.addEventListener('click', () => {
        const role = btn.getAttribute('data-role');
        formContainer.innerHTML = generateForm(role);
    });
});

// Generate role-specific registration/login form
function generateForm(role) {
    let extraFields = '';
    if (role === 'farmer') {
        extraFields = `
            <input type="text" placeholder="Farm Name" required>
            <input type="text" placeholder="Location" required>
            <input type="text" placeholder="Crops Grown" required>
        `;
    } else if (role === 'buyer') {
        extraFields = `
            <input type="text" placeholder="Company Name / Full Name" required>
            <input type="text" placeholder="Location" required>
        `;
    } else if (role === 'institution') {
        extraFields = `
            <input type="text" placeholder="Institution Name" required>
            <input type="text" placeholder="Department / Expertise" required>
        `;
    }

    return `
        <form class="role-form" onsubmit="handleFormSubmit(event, '${role}')">
            <input type="text" placeholder="Username" required>
            <input type="email" placeholder="Email" required>
            <input type="password" placeholder="Password" required>
            ${extraFields}
            <button type="submit">Register / Login as ${role.charAt(0).toUpperCase() + role.slice(1)}</button>
        </form>
    `;
}

// ==========================
// Handle Form Submission
// ==========================
function handleFormSubmit(e, role) {
    e.preventDefault();
    alert(`Welcome ${role}! Redirecting to your dashboard...`);
    // Placeholder for dashboard redirection:
    // Example: window.location.href = `${role}-dashboard.html`;
}

// ==========================
// Optional: Back-to-Top Button
// ==========================
const backToTop = document.createElement('button');
backToTop.textContent = "↑";
backToTop.className = "back-to-top";
document.body.appendChild(backToTop);

backToTop.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

window.addEventListener('scroll', () => {
    if(window.scrollY > 300){
        backToTop.style.display = "block";
    } else {
        backToTop.style.display = "none";
    }
});


// ==========================
// Statistics Counters Animation
// ==========================
const counters = document.querySelectorAll('.counter');

function runCounters() {
    counters.forEach(counter => {
        counter.innerText = '0';
        const updateCounter = () => {
            const target = +counter.getAttribute('data-target');
            const current = +counter.innerText;
            const increment = Math.ceil(target / 100);
            if(current < target) {
                counter.innerText = current + increment;
                setTimeout(updateCounter, 20);
            } else {
                counter.innerText = target;
            }
        };
        updateCounter();
    });
}

window.addEventListener('scroll', () => {
    const statsSection = document.querySelector('.statistics');
    if(statsSection.getBoundingClientRect().top < window.innerHeight - 50) {
        runCounters();
    }
});

// ==========================
// Testimonials Carousel
// ==========================
let testimonialIndex = 0;
const testimonialSlides = document.querySelectorAll('.testimonial-slide');
const prevTestimonial = document.querySelector('.prev-testimonial');
const nextTestimonial = document.querySelector('.next-testimonial');

function showTestimonial(index) {
    testimonialSlides.forEach(slide => slide.classList.remove('active'));
    testimonialSlides[index].classList.add('active');
}

prevTestimonial.addEventListener('click', () => {
    testimonialIndex = (testimonialIndex === 0) ? testimonialSlides.length -1 : testimonialIndex -1;
    showTestimonial(testimonialIndex);
});

nextTestimonial.addEventListener('click', () => {
    testimonialIndex = (testimonialIndex +1) % testimonialSlides.length;
    showTestimonial(testimonialIndex);
});

// Auto-rotate every 6 seconds
setInterval(() => {
    testimonialIndex = (testimonialIndex +1) % testimonialSlides.length;
    showTestimonial(testimonialIndex);
}, 6000);

// ==========================
// Produce Carousel
// ==========================
const produceCarousel = document.querySelector('.produce-carousel');
const produceItems = document.querySelectorAll('.produce-item');
const prevProduce = document.querySelector('.prev-produce');
const nextProduce = document.querySelector('.next-produce');

let produceIndex = 0;
const visibleItems = 3; // items visible in carousel

function updateProduceCarousel() {
    produceItems.forEach((item, idx) => {
        item.style.display = (idx >= produceIndex && idx < produceIndex + visibleItems) ? 'block' : 'none';
    });
}

prevProduce.addEventListener('click', () => {
    produceIndex = (produceIndex <= 0) ? produceItems.length - visibleItems : produceIndex -1;
    updateProduceCarousel();
});

nextProduce.addEventListener('click', () => {
    produceIndex = (produceIndex + visibleItems >= produceItems.length) ? 0 : produceIndex +1;
    updateProduceCarousel();
});

updateProduceCarousel(); // initialize