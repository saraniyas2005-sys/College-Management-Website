document.addEventListener("DOMContentLoaded", function() {
    let selectedRating = 0;

    // Load and display reviews
    function loadReviews() {
        const reviewsList = document.getElementById("reviewsList");
        if (!reviewsList) return;

        reviewsList.innerHTML = "";
        let reviews = JSON.parse(localStorage.getItem("reviews")) || [];

        reviews.forEach(review => {
            const reviewItem = document.createElement("div");
            reviewItem.classList.add("review-item");
            reviewItem.innerHTML = `
                <p><strong>${review.name}</strong></p>
                <p>${review.review}</p>
                <p>⭐ ${"★".repeat(review.rating)}</p>
            `;
            reviewsList.appendChild(reviewItem);
        });
    }

    // Handle star rating selection
    document.querySelectorAll('.star').forEach(star => {
        star.addEventListener('click', function() {
            selectedRating = parseInt(this.getAttribute('data-value'));

            // Reset all stars first
            document.querySelectorAll('.star').forEach(s => s.classList.remove('selected'));

            // Highlight all selected stars up to the clicked one
            for (let i = 0; i < selectedRating; i++) {
                document.querySelectorAll('.star')[i].classList.add('selected');
            }
        });
    });

    // Handle review form submission
    const reviewForm = document.getElementById("reviewForm");
    if (reviewForm) {
        reviewForm.addEventListener("submit", function(event) {
            event.preventDefault();

            let name = document.getElementById("reviewerName").value;
            let review = document.getElementById("reviewText").value;

            if (selectedRating === 0) {
                alert("Please select a rating!");
                return;
            }

            let reviews = JSON.parse(localStorage.getItem("reviews")) || [];
            reviews.push({ name, review, rating: selectedRating });
            localStorage.setItem("reviews", JSON.stringify(reviews));

            // Reset form and rating
            document.getElementById("reviewerName").value = "";
            document.getElementById("reviewText").value = "";
            selectedRating = 0;
            document.querySelectorAll('.star').forEach(s => s.classList.remove('selected'));

            // Redirect to review page
            window.location.href = "review.html";
        });
    }

    loadReviews(); // Load existing reviews on page load
});
