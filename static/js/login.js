document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("loginForm").addEventListener("submit", function (e) {
        e.preventDefault(); // Prevent form submission

        // Get input values
        let email = document.getElementById("loginEmail").value.trim();
        let password = document.getElementById("loginPassword").value.trim();

        // Validate email format
        if (!validateEmail(email)) {
            showError("loginEmail", "Enter a valid email address");
            return;
        }

        // Validate password length
        if (password.length < 6) {
            showError("loginPassword", "Password must be at least 6 characters long");
            return;
        }

        // If validation passes, redirect
        alert("Login Successful! Redirecting...");
        window.location.href = "index.html";
    });
});

// Function to validate email format
function validateEmail(email) {
    let emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailPattern.test(email);
}

// Function to show error messages
function showError(inputId, message) {
    let inputField = document.getElementById(inputId);
    inputField.style.border = "2px solid red";
    inputField.style.boxShadow = "0 0 10px rgba(255, 0, 0, 0.7)";

    // Show alert (You can replace this with a tooltip or custom error message)
    alert(message);

    // Remove the red border after 2 seconds
    setTimeout(() => {
        inputField.style.border = "";
        inputField.style.boxShadow = "";
    }, 2000);
}
