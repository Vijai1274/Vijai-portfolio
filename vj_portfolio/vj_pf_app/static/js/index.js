
const toggleBtn = document.getElementById("menu-toggle");
const navbar = document.getElementById("navbar");

toggleBtn.addEventListener("click", () => {
  navbar.classList.toggle("active");

  // Toggle icon ☰ ↔ ✖
  if (navbar.classList.contains("active")) {
    toggleBtn.innerHTML = "&#10006;"; // ✖
  } else {
    toggleBtn.innerHTML = "&#9776;";  // ☰
  }
});

// Close navbar when any nav link is clicked (for mobile)
document.querySelectorAll(".nav-links a").forEach(link => {
  link.addEventListener("click", () => {
    if (navbar.classList.contains("active")) {
      navbar.classList.remove("active");
      toggleBtn.innerHTML = "&#9776;"; // ☰
    }
  });
});



    const form = document.querySelector("form");
    const submitButton = form.querySelector("button");

    form.addEventListener("submit", function () {
      submitButton.disabled = true;
      submitButton.innerHTML = 'Submitting <span class="loading-spinner"></span>';
    });


    document.addEventListener("DOMContentLoaded", function () {
    const toast = document.getElementById("toast-message");
    if (toast) {
      const msg = toast.getAttribute("data-message");
      const tag = toast.getAttribute("data-tag");

      toast.textContent = msg;

      if (tag === "success") {
        toast.style.backgroundColor = "#4BB543";
      } else if (tag === "error" || tag === "danger") {
        toast.style.backgroundColor = "#e74c3c";
      } else {
        toast.style.backgroundColor = "#3498db";
      }

      toast.classList.remove("hidden");
      toast.classList.add("show");

      setTimeout(() => {
        toast.classList.remove("show");
        toast.classList.add("hidden");
      }, 4000);
    }
  });


  