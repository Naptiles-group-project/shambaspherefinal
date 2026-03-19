// advisor-register.js

// =========================
// GET CSRF TOKEN
// =========================
function getCSRFToken() {
    const cookie = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken'));
    return cookie ? cookie.split('=')[1] : '';
}

// =========================
// DOM READY
// =========================
document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("advisorForm");
    const messageEl = document.getElementById("message");

    if (!form) {
        console.error("Advisor form not found!");
        return;
    }

    form.addEventListener("submit", function(e) {
        e.preventDefault();

        const formData = new FormData(form);

        // 🔹 Debug: log all FormData entries
        console.log("FormData entries:");
        for (let [key, value] of formData.entries()) {
            console.log(key, value);
        }

        // Simple front-end validation
        if (!formData.get("username") || !formData.get("fullName") || !formData.get("email") || !formData.get("password")) {
            messageEl.innerText = "Please fill in all required fields!";
            messageEl.style.color = "red";
            return;
        }

        fetch("/advisor-register/", {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": getCSRFToken(),
                "X-Requested-With": "XMLHttpRequest"
            }
        })
        .then(res => res.json())
        .then(json => {
            console.log("Server response:", json);
            messageEl.innerText = json.success ? json.message : (json.error || "Registration failed!");
            messageEl.style.color = json.success ? "green" : "red";
            if(json.success) form.reset();
        })
        .catch(err => {
            console.error(err);
            messageEl.innerText = "An unexpected error occurred!";
            messageEl.style.color = "red";
        });
    });

});