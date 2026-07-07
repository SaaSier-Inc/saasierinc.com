document.addEventListener("DOMContentLoaded", function () {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  /* ---- Mobile menu (with aria state) ---- */
  const mobileMenuBtn = document.querySelector(".mobile-menu-btn");
  const navMenu = document.querySelector(".nav-links");

  const setMenu = (open) => {
    mobileMenuBtn.classList.toggle("active", open);
    navMenu.classList.toggle("active", open);
    mobileMenuBtn.setAttribute("aria-expanded", String(open));
    document.body.style.overflow = open ? "hidden" : "";
  };

  if (mobileMenuBtn && navMenu) {
    mobileMenuBtn.addEventListener("click", () => {
      setMenu(mobileMenuBtn.getAttribute("aria-expanded") !== "true");
    });
    navMenu.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => setMenu(false));
    });
    // Close on Escape
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && navMenu.classList.contains("active")) {
        setMenu(false);
        mobileMenuBtn.focus();
      }
    });
  }

  /* ---- Smooth scrolling for in-page anchors ---- */
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      const targetId = this.getAttribute("href");
      if (targetId.length <= 1) return; // ignore bare "#"
      const target = document.querySelector(targetId);
      if (!target) return;
      e.preventDefault();
      const top = target.getBoundingClientRect().top + window.scrollY - 80;
      window.scrollTo({ top, behavior: reduceMotion.matches ? "auto" : "smooth" });
    });
  });

  /* ---- Scroll-driven UI (header shrink + back-to-top), rAF-batched ---- */
  const header = document.querySelector("header");
  const backToTopBtn = document.getElementById("back-to-top");
  let ticking = false;

  const onScrollFrame = () => {
    const y = window.scrollY;
    if (header) header.classList.toggle("scrolled", y > 100);
    if (backToTopBtn) backToTopBtn.classList.toggle("visible", y > 500);
    ticking = false;
  };
  const requestScroll = () => {
    if (!ticking) { ticking = true; requestAnimationFrame(onScrollFrame); }
  };
  window.addEventListener("scroll", requestScroll, { passive: true });
  onScrollFrame();

  if (backToTopBtn) {
    backToTopBtn.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: reduceMotion.matches ? "auto" : "smooth" });
    });
  }

  /* ---- Scroll reveal (enhances an already-visible default) ---- */
  if ("IntersectionObserver" in window && !reduceMotion.matches) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("animate-in");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    document
      .querySelectorAll(".company-card, .news-item, .goal, .value-card, .trust-item, .phase, .stat, .metric-card, .press-kit-item, .resource-card, .fact-item, .evidence-item, .routing-link, .next-step-card, .update-row")
      .forEach((el, i) => {
        el.style.animationDelay = `${(i % 4) * 0.07}s`;
        observer.observe(el);
      });
  }

  /* ---- Count-up for [data-target] metrics (progressive enhancement) ----
     HTML holds the real final value, so no-JS / reduced-motion users see it.
     JS animates from 0 up to the target when it scrolls into view. */
  const metrics = document.querySelectorAll("[data-target]");
  if (metrics.length && "IntersectionObserver" in window && !reduceMotion.matches) {
    const animateCount = (el) => {
      const target = parseFloat(el.dataset.target);
      if (isNaN(target)) return;
      const decimals = (el.dataset.target.split(".")[1] || "").length;
      const duration = 1400;
      const start = performance.now();
      const step = (now) => {
        const p = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - p, 3); // ease-out cubic
        el.textContent = (target * eased).toLocaleString("en-US", {
          minimumFractionDigits: decimals,
          maximumFractionDigits: decimals,
        });
        if (p < 1) requestAnimationFrame(step);
        else el.textContent = target.toLocaleString("en-US", {
          minimumFractionDigits: decimals,
          maximumFractionDigits: decimals,
        });
      };
      requestAnimationFrame(step);
    };
    const mo = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) { animateCount(entry.target); mo.unobserve(entry.target); }
        });
      },
      { threshold: 0.5 }
    );
    metrics.forEach((el) => mo.observe(el));
  }
});
