// Sticky Navbar
window.addEventListener("scroll", function () {
    const header = document.querySelector("header");
    if (header) {
      header.classList.toggle("sticky", window.scrollY > 60);
    }
  });
  
  // Hamburger Toggle Functionality
  const menuToggle = document.querySelector(".menu-toggle");
  const navLinks = document.querySelector(".nav-links");
  
  if (menuToggle && navLinks) {
    menuToggle.addEventListener("click", () => {
      navLinks.classList.toggle("active");
      menuToggle.classList.toggle("open");
    });
  
    // Close menu on nav link click (optional for mobile)
    document.querySelectorAll(".nav-links a").forEach(link =>
      link.addEventListener("click", () => {
        navLinks.classList.remove("active");
        menuToggle.classList.remove("open");
      })
    );
  }
  
