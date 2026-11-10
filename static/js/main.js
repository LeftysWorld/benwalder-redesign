/* Ben Walder Healing Arts — site interactions */
(function () {
  "use strict";
  document.documentElement.classList.remove("no-js");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Header shadow on scroll ---------- */
  var header = document.querySelector(".site-header");
  function onScrollHeader() {
    if (header) header.classList.toggle("is-scrolled", window.scrollY > 8);
  }

  /* ---------- Mobile nav ---------- */
  var mobileNav = document.getElementById("mobile-nav");
  var openBtn = document.querySelector("[data-nav-open]");
  var closeBtn = document.querySelector("[data-nav-close]");
  function setNav(open) {
    if (!mobileNav) return;
    mobileNav.classList.toggle("is-open", open);
    document.body.style.overflow = open ? "hidden" : "";
    if (openBtn) openBtn.setAttribute("aria-expanded", String(open));
    if (open && closeBtn) closeBtn.focus();
    if (!open && openBtn) openBtn.focus();
  }
  if (openBtn) openBtn.addEventListener("click", function () { setNav(true); });
  if (closeBtn) closeBtn.addEventListener("click", function () { setNav(false); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && mobileNav && mobileNav.classList.contains("is-open")) setNav(false);
  });

  /* ---------- Sticky mobile Book/Call bar ---------- */
  var stickyBar = document.querySelector(".sticky-bar");
  var heroEl = document.querySelector(".hero, .page-hero");
  function onScrollSticky() {
    if (!stickyBar) return;
    var threshold = heroEl ? heroEl.getBoundingClientRect().bottom : 200;
    var nearFooter = false;
    var footer = document.querySelector(".site-footer");
    if (footer) nearFooter = footer.getBoundingClientRect().top < window.innerHeight - 40;
    stickyBar.classList.toggle("is-visible", threshold < 0 && !nearFooter);
  }

  /* ---------- Reveal on scroll ---------- */
  var reveals = document.querySelectorAll(".reveal");
  if (reduceMotion || !("IntersectionObserver" in window)) {
    reveals.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("is-in"); io.unobserve(entry.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Signature thread: one continuous line through the homepage ---------- */
  var wrap = document.querySelector(".thread-wrap");
  var svg, path, length = 0;
  function buildThread() {
    if (!wrap) return;
    var anchors = wrap.querySelectorAll("[data-thread]");
    if (anchors.length < 2) return;
    var wrapRect = wrap.getBoundingClientRect();
    var width = wrapRect.width;
    var mobile = width < 900;
    var pts = [];
    anchors.forEach(function (el, i) {
      var r = el.getBoundingClientRect();
      var fx = parseFloat(el.getAttribute("data-thread")) || 0.5;
      var fy = parseFloat(el.getAttribute("data-thread-y") || "0.5");
      var x = mobile ? (i % 2 === 0 ? 8 : 13) : Math.max(18, Math.min(width - 18, width * fx));
      var y = r.top - wrapRect.top + r.height * fy;
      pts.push([x, y]);
    });
    var d = "M" + pts[0][0] + " " + pts[0][1];
    for (var i = 1; i < pts.length; i++) {
      var p0 = pts[i - 1], p1 = pts[i];
      var dy = (p1[1] - p0[1]) * 0.5;
      d += " C" + p0[0] + " " + (p0[1] + dy) + " " + p1[0] + " " + (p1[1] - dy) + " " + p1[0] + " " + p1[1];
    }
    if (!svg) {
      svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
      svg.setAttribute("class", "thread-svg");
      svg.setAttribute("aria-hidden", "true");
      path = document.createElementNS("http://www.w3.org/2000/svg", "path");
      svg.appendChild(path);
      wrap.insertBefore(svg, wrap.firstChild);
    }
    svg.setAttribute("viewBox", "0 0 " + width + " " + wrapRect.height);
    path.setAttribute("d", d);
    length = path.getTotalLength();
    path.style.strokeDasharray = length + " " + length;
    drawThread();
  }
  function drawThread() {
    if (!path || !length) return;
    if (reduceMotion) { path.style.strokeDashoffset = "0"; return; }
    var r = wrap.getBoundingClientRect();
    var progress = (window.innerHeight * 0.8 - r.top) / r.height;
    progress = Math.max(0, Math.min(1, progress));
    path.style.strokeDashoffset = String(length * (1 - progress));
  }

  /* ---------- Concept forms: don't submit anywhere ---------- */
  document.querySelectorAll("form[data-concept]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var note = form.querySelector(".form-status");
      if (note) {
        note.textContent = "Concept preview: this form isn't connected yet. On the live site it would go to Ben's email list or booking system.";
        note.setAttribute("role", "status");
      }
    });
  });

  /* ---------- Wire up ---------- */
  var ticking = false;
  window.addEventListener("scroll", function () {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(function () {
      onScrollHeader(); onScrollSticky(); drawThread();
      ticking = false;
    });
  }, { passive: true });
  var resizeTimer;
  window.addEventListener("resize", function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(buildThread, 150);
  });
  window.addEventListener("load", buildThread);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(buildThread);
  onScrollHeader(); onScrollSticky(); buildThread();
})();
