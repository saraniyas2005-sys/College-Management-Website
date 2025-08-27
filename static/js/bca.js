function toggleSemester(id) {
    var element = document.getElementById(id);
    if (element.style.display === "block") {
        element.style.display = "none";
    } else {
        element.style.display = "block";
    }
}
function toggleSubjects(id) {
    const element = document.getElementById(id);
    if (element.style.display === "block") {
      element.style.display = "none";
    } else {
      // Hide others
      document.querySelectorAll('.subject-box').forEach(box => {
        box.style.display = "none";
      });
      // Show selected
      element.style.display = "block";
    }
  }