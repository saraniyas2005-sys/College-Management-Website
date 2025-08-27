document.addEventListener("DOMContentLoaded", function () {
    const mobileMenuBtn = document.querySelector(".mobile-menu button");
    const navList = document.querySelector(".navbar ul");

    // Mobile Menu Toggle
    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener("click", function () {
            navList.classList.toggle("show");
        });
    }

    // Close Menu When Clicking Outside
    document.addEventListener("click", function (event) {
        if (!navList.contains(event.target) && !mobileMenuBtn.contains(event.target)) {
            navList.classList.remove("show");
        }
    });

    // Dropdown Hover Effect for Main Menus
    const dropdowns = document.querySelectorAll(".dropdown");

    dropdowns.forEach((dropdown) => {
        dropdown.addEventListener("mouseenter", function () {
            const dropdownMenu = this.querySelector(".dropdown-menu");
            if (dropdownMenu) {
                dropdownMenu.style.display = "block";
                setTimeout(() => {
                    dropdownMenu.style.opacity = "1";
                    dropdownMenu.style.visibility = "visible";
                    dropdownMenu.style.transform = "translateY(10px)";
                }, 10);
            }
        });

        dropdown.addEventListener("mouseleave", function () {
            const dropdownMenu = this.querySelector(".dropdown-menu");
            if (dropdownMenu) {
                dropdownMenu.style.opacity = "0";
                dropdownMenu.style.visibility = "hidden";
                dropdownMenu.style.transform = "translateY(-20px)";
                setTimeout(() => {
                    dropdownMenu.style.display = "none";
                }, 300);
            }
        });
    });

    // Dropdown Hover Effect for Undergraduate Courses (Same as "About")
    const courseDropdown = document.querySelector(".course-dropdown");

    if (courseDropdown) {
        courseDropdown.addEventListener("mouseenter", function () {
            const submenu = this.querySelector(".dropdown-menu");
            if (submenu) {
                submenu.style.display = "block";
                setTimeout(() => {
                    submenu.style.opacity = "1";
                    submenu.style.visibility = "visible";
                    submenu.style.transform = "translateY(10px)";
                }, 10);
            }
        });

        courseDropdown.addEventListener("mouseleave", function () {
            const submenu = this.querySelector(".dropdown-menu");
            if (submenu) {
                submenu.style.opacity = "0";
                submenu.style.visibility = "hidden";
                submenu.style.transform = "translateY(-20px)";
                setTimeout(() => {
                    submenu.style.display = "none";
                }, 300);
            }
        });
    }

    // Sticky Navbar Effect (Same as Before)
    const navbar = document.querySelector(".navbar");

    window.addEventListener("scroll", function () {
        if (window.scrollY > 50) {
            navbar.style.background = "linear-gradient(135deg, #2C3E50, #34495E)"; // Deep Navy to Elegant Steel
            navbar.style.boxShadow = "0 4px 15px rgba(0, 0, 0, 0.4)";
        } else {
            navbar.style.background = "linear-gradient(135deg, #1B2631, #2C3E50)"; // Classic Dark Blue Gradient
            navbar.style.boxShadow = "0 4px 12px rgba(0, 0, 0, 0.2)";
        }
    });
});
