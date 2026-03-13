const form = document.getElementById("farmerForm");
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirmPassword");
const email = document.getElementById("email");
const confirmEmail = document.getElementById("confirmEmail");
const strengthBar = document.getElementById("strengthBar");
const profilePic = document.getElementById("profilePic");
const previewImage = document.getElementById("previewImage");

/* Email validation */
confirmEmail.addEventListener("input", () => {
    if (email.value !== confirmEmail.value) {
        confirmEmail.setCustomValidity("Emails do not match");
    } else {
        confirmEmail.setCustomValidity("");
    }
});

/* Password validation */
confirmPassword.addEventListener("input", () => {
    if (password.value !== confirmPassword.value) {
        confirmPassword.setCustomValidity("Passwords do not match");
    } else {
        confirmPassword.setCustomValidity("");
    }
});

/* Password strength meter */
password.addEventListener("input", () => {
    let strength = 0;
    if (password.value.length > 6) strength += 25;
    if (/[A-Z]/.test(password.value)) strength += 25;
    if (/[0-9]/.test(password.value)) strength += 25;
    if (/[^A-Za-z0-9]/.test(password.value)) strength += 25;

    strengthBar.style.width = strength + "%";

    if (strength <= 25) strengthBar.style.background = "red";
    else if (strength <= 50) strengthBar.style.background = "orange";
    else if (strength <= 75) strengthBar.style.background = "yellow";
    else strengthBar.style.background = "green";
});

/* Image preview */
profilePic.addEventListener("change", function() {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function() {
            previewImage.src = reader.result;
            previewImage.style.display = "block";
        };
        reader.readAsDataURL(file);
    }
});

/* Display errors under the relevant inputs */
function displayErrors(errors) {
    // Clear previous errors
    document.querySelectorAll(".error-message").forEach(e => e.remove());

    for (const [field, message] of Object.entries(errors)) {
        const input = document.querySelector(`[name=${field}]`);
        if (input) {
            const span = document.createElement("span");
            span.classList.add("error-message");
            span.style.color = "red";
            span.textContent = message;
            input.parentNode.insertBefore(span, input.nextSibling);
        } else {
            // fallback alert if input not found
            alert(message);
        }
    }
}

/* Form submission */
form.addEventListener("submit", async function(e) {
    e.preventDefault();

    // Clear previous errors
    document.querySelectorAll(".error-message").forEach(e => e.remove());

    const formData = new FormData(form);

    try {
        const response = await fetch("/farmer-register/", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (data.success) {
            alert("Farmer registered successfully!");
            window.location.href = data.redirect_url;
        } else if (data.errors) {
            displayErrors(data.errors);
        } else if (data.error) {
            alert(data.error);
        }

    } catch (err) {
        console.error("Error:", err);
        alert("An unexpected error occurred. Please try again.");
    }
});