const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirmPassword");
const strengthBar = document.getElementById("strengthBar");
const form = document.getElementById("adminForm");

const profileUpload = document.getElementById("profileUpload");
const profileImage = document.getElementById("profileImage");
const profileName = document.getElementById("profileName");
const profileRole = document.getElementById("profileRole");

/* ===============================
   LOAD PROFILE IF EXISTS
================================= */
window.addEventListener("DOMContentLoaded", () => {
    const savedProfile = JSON.parse(localStorage.getItem("adminProfile"));
    if (savedProfile) {
        profileImage.src = savedProfile.image;
        profileName.innerText = savedProfile.name;
        profileRole.innerText = savedProfile.role;
    }
});

/* ===============================
   PASSWORD STRENGTH
================================= */
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

/* ===============================
   CONFIRM PASSWORD
================================= */
confirmPassword.addEventListener("input", () => {
    if (password.value !== confirmPassword.value) {
        confirmPassword.setCustomValidity("Passwords do not match");
    } else {
        confirmPassword.setCustomValidity("");
    }
});

/* ===============================
   PROFILE IMAGE PREVIEW
================================= */
profileUpload.addEventListener("change", function() {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function() {
            profileImage.src = reader.result;
        };
        reader.readAsDataURL(file);
    }
});

/* ===============================
   FORM SUBMIT
================================= */
form.addEventListener("submit", function(e){
    e.preventDefault();

    const firstName = form.querySelector('input[placeholder="First Name"]').value;
    const lastName = form.querySelector('input[placeholder="Last Name"]').value;
    const role = form.querySelector("select").value;

    const adminData = {
        name: firstName + " " + lastName,
        role: role,
        image: profileImage.src
    };

    localStorage.setItem("adminProfile", JSON.stringify(adminData));

    profileName.innerText = adminData.name;
    profileRole.innerText = adminData.role;

    alert("Admin Registered Successfully!");

    form.addEventListener("submit", function(e){
    e.preventDefault();

    alert("Admin Registered Successfully!");

    window.location.href = "admin-dashboard.html";
});
});