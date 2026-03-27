document.addEventListener("DOMContentLoaded", function () {
    // Mobile menu
    const menuToggle = document.getElementById("menuToggle");
    const mobileNav = document.getElementById("mobileNav");

    if (menuToggle && mobileNav) {
        menuToggle.addEventListener("click", function (e) {
            e.stopPropagation();
            mobileNav.classList.toggle("show");
        });

        document.addEventListener("click", function (e) {
            if (!mobileNav.contains(e.target) && !menuToggle.contains(e.target)) {
                mobileNav.classList.remove("show");
            }
        });

        mobileNav.querySelectorAll("a").forEach(link => {
            link.addEventListener("click", function () {
                mobileNav.classList.remove("show");
            });
        });
    }

    // Hero carousel
    let currentSlide = 0;
    const slides = document.querySelectorAll(".slide");
    const prevBtn = document.querySelector(".prev");
    const nextBtn = document.querySelector(".next");

    function showSlide(index) {
        if (!slides.length) return;
        slides.forEach(slide => slide.classList.remove("active"));
        slides[index].classList.add("active");
    }

    if (slides.length && prevBtn && nextBtn) {
        prevBtn.addEventListener("click", function () {
            currentSlide = currentSlide === 0 ? slides.length - 1 : currentSlide - 1;
            showSlide(currentSlide);
        });

        nextBtn.addEventListener("click", function () {
            currentSlide = (currentSlide + 1) % slides.length;
            showSlide(currentSlide);
        });

        setInterval(function () {
            currentSlide = (currentSlide + 1) % slides.length;
            showSlide(currentSlide);
        }, 5000);
    }

    // Feature fade in
    const fCards = document.querySelectorAll(".fade-in");

    function checkFadeIn() {
        fCards.forEach(card => {
            const rect = card.getBoundingClientRect();
            if (rect.top < window.innerHeight - 60) {
                card.classList.add("visible");
            }
        });
    }

    window.addEventListener("scroll", checkFadeIn);
    checkFadeIn();

    // Back to top
    const backToTop = document.createElement("button");
    backToTop.textContent = "↑";
    backToTop.className = "back-to-top";
    document.body.appendChild(backToTop);

    backToTop.addEventListener("click", function () {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });

    window.addEventListener("scroll", function () {
        backToTop.style.display = window.scrollY > 300 ? "block" : "none";
    });

    // Counter animation
    const counters = document.querySelectorAll(".counter");
    let countersStarted = false;

    function runCounters() {
        if (countersStarted) return;
        countersStarted = true;

        counters.forEach(counter => {
            counter.innerText = "0";
            const target = +counter.getAttribute("data-target");
            const increment = Math.ceil(target / 100);

            function updateCounter() {
                const current = +counter.innerText;
                if (current < target) {
                    counter.innerText = Math.min(current + increment, target);
                    setTimeout(updateCounter, 20);
                } else {
                    counter.innerText = target;
                }
            }

            updateCounter();
        });
    }

    const statsSection = document.querySelector(".statistics");
    function checkStats() {
        if (statsSection && statsSection.getBoundingClientRect().top < window.innerHeight - 50) {
            runCounters();
        }
    }

    window.addEventListener("scroll", checkStats);
    checkStats();

    // Testimonials carousel
    let testimonialIndex = 0;
    const testimonialSlides = document.querySelectorAll(".testimonial-slide");
    const prevTestimonial = document.querySelector(".prev-testimonial");
    const nextTestimonial = document.querySelector(".next-testimonial");

    function showTestimonial(index) {
        if (!testimonialSlides.length) return;
        testimonialSlides.forEach(slide => slide.classList.remove("active"));
        testimonialSlides[index].classList.add("active");
    }

    if (testimonialSlides.length && prevTestimonial && nextTestimonial) {
        prevTestimonial.addEventListener("click", function () {
            testimonialIndex = testimonialIndex === 0 ? testimonialSlides.length - 1 : testimonialIndex - 1;
            showTestimonial(testimonialIndex);
        });

        nextTestimonial.addEventListener("click", function () {
            testimonialIndex = (testimonialIndex + 1) % testimonialSlides.length;
            showTestimonial(testimonialIndex);
        });

        setInterval(function () {
            testimonialIndex = (testimonialIndex + 1) % testimonialSlides.length;
            showTestimonial(testimonialIndex);
        }, 6000);
    }

    // Produce carousel
    const produceItems = document.querySelectorAll(".produce-item");
    const prevProduce = document.querySelector(".prev-produce");
    const nextProduce = document.querySelector(".next-produce");
    let produceIndex = 0;

    function getVisibleItems() {
        if (window.innerWidth <= 768) return 1;
        if (window.innerWidth <= 992) return 2;
        return 3;
    }

    function updateProduceCarousel() {
        if (!produceItems.length) return;

        const visibleItems = getVisibleItems();
        produceItems.forEach((item, index) => {
            item.style.display =
                index >= produceIndex && index < produceIndex + visibleItems
                    ? "block"
                    : "none";
        });
    }

    if (produceItems.length && prevProduce && nextProduce) {
        prevProduce.addEventListener("click", function () {
            const visibleItems = getVisibleItems();
            produceIndex = produceIndex <= 0 ? Math.max(produceItems.length - visibleItems, 0) : produceIndex - 1;
            updateProduceCarousel();
        });

        nextProduce.addEventListener("click", function () {
            const visibleItems = getVisibleItems();
            produceIndex = produceIndex + visibleItems >= produceItems.length ? 0 : produceIndex + 1;
            updateProduceCarousel();
        });

        window.addEventListener("resize", function () {
            produceIndex = 0;
            updateProduceCarousel();
        });

        updateProduceCarousel();
    }
});