document.addEventListener("DOMContentLoaded", function () {
  // Mobile Menu
  const mobileMenuBtn = document.querySelector(".mobile-menu-btn");
  const navMenu = document.querySelector(".nav-links");

  if (mobileMenuBtn && navMenu) {
    mobileMenuBtn.addEventListener("click", () => {
      mobileMenuBtn.classList.toggle("active");
      navMenu.classList.toggle("active");
      document.body.style.overflow = navMenu.classList.contains("active") ? "hidden" : "";
    });

    document.querySelectorAll(".nav-links a").forEach((link) => {
      link.addEventListener("click", () => {
        mobileMenuBtn.classList.remove("active");
        navMenu.classList.remove("active");
        document.body.style.overflow = "";
      });
    });
  }

  // Smooth Scrolling for Anchors
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      const targetId = this.getAttribute("href");
      if (targetId.length > 1) {
        e.preventDefault();
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
          window.scrollTo({
            top: targetElement.offsetTop - 80,
            behavior: "smooth",
          });
        }
      }
    });
  });

  // Header and Back to Top
  const header = document.querySelector("header");
  const backToTopBtn = document.getElementById("back-to-top");

  window.addEventListener("scroll", function () {
    if (header) {
      if (window.scrollY > 100) {
        header.classList.add("scrolled");
      } else {
        header.classList.remove("scrolled");
      }
    }

    if (backToTopBtn) {
      if (window.scrollY > 500) {
        backToTopBtn.classList.add("visible");
      } else {
        backToTopBtn.classList.remove("visible");
      }
    }
  });

  if (backToTopBtn) {
    backToTopBtn.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  // Intersection Observer for Animations
  const observerOptions = { root: null, rootMargin: "0px", threshold: 0.1 };
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("animate-in");
      }
    });
  }, observerOptions);

  const animatedElements = document.querySelectorAll(
    ".company-card, .news-item, .goal, .value-card, .trust-item, .phase, .stat"
  );

  animatedElements.forEach((el, index) => {
    el.style.animationDelay = `${(index % 5) * 0.1}s`;
    observer.observe(el);
  });

  // Hero section Parallax and Mouse Move
  const heroVisual = document.querySelector(".hero-visual");
  if (heroVisual) {
    window.addEventListener("scroll", () => {
      const scrolled = window.pageYOffset;
      const parallax = scrolled * 0.4;
      heroVisual.style.transform = `translateY(calc(-50% + ${parallax}px))`;
    });

    window.addEventListener("mousemove", (e) => {
      const x = e.clientX / window.innerWidth;
      const y = e.clientY / window.innerHeight;

      heroVisual.querySelectorAll(".floating-card").forEach((card, index) => {
        const speed = (index + 1) * 5;
        const offsetX = (x - 0.5) * speed;
        const offsetY = (y - 0.5) * speed;
        card.style.transform = `translate(${offsetX}px, ${offsetY}px)`;
      });
    });
  }
});
