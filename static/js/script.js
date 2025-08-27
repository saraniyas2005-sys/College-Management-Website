document.addEventListener("DOMContentLoaded", () => {
  const dropdowns = document.querySelectorAll(".navbar .dropdown");

  dropdowns.forEach(dropdown => {
    const menu = dropdown.querySelector(".dropdown-menu");
    let hideTimeout;

    // Show dropdown
    dropdown.addEventListener("mouseenter", () => {
      clearTimeout(hideTimeout);
      menu.style.display = "block";
      requestAnimationFrame(() => {
        menu.style.opacity = "1";
        menu.style.visibility = "visible";
        menu.style.transform = "translateY(10px)";
      });
    });

    // Hide dropdown
    dropdown.addEventListener("mouseleave", () => {
      menu.style.opacity = "0";
      menu.style.transform = "translateY(-10px)";
      menu.style.visibility = "hidden";
      hideTimeout = setTimeout(() => {
        menu.style.display = "none";
      }, 300); // Match CSS transition
    });
  });
});
