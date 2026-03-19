const counties = [
"Baringo","Bomet","Bungoma","Busia","Elgeyo-Marakwet","Embu",
"Garissa","Homa Bay","Isiolo","Kajiado","Kakamega","Kericho",
"Kiambu","Kilifi","Kirinyaga","Kisii","Kisumu","Kitui",
"Kwale","Laikipia","Lamu","Machakos","Makueni","Mandera",
"Marsabit","Meru","Migori","Mombasa","Murang'a","Nairobi",
"Nakuru","Nandi","Narok","Nyamira","Nyandarua","Nyeri",
"Samburu","Siaya","Taita-Taveta","Tana River","Tharaka-Nithi",
"Trans Nzoia","Turkana","Uasin Gishu","Vihiga","Wajir",
"West Pokot"
];

// Populate counties
const countySelect = document.getElementById("county");
counties.forEach(county => {
    let option = document.createElement("option");
    option.value = county;
    option.textContent = county;
    countySelect.appendChild(option);
});

// Profile image preview
document.getElementById("profileImage").addEventListener("change", function(){
    const reader = new FileReader();
    reader.onload = function(e){
        document.getElementById("profilePreview").src = e.target.result;
    }
    reader.readAsDataURL(this.files[0]);
});

// Password toggle
function togglePassword(id) {
    const field = document.getElementById(id);
    field.type = field.type === "password" ? "text" : "password";
}

// Password strength
document.getElementById("password").addEventListener("input", function(){
    const strengthMessage = document.getElementById("strengthMessage");
    const val = this.value;

    if (val.length < 6) {
        strengthMessage.textContent = "Weak password";
        strengthMessage.style.color = "red";
    } else if (val.match(/[A-Z]/) && val.match(/[0-9]/)) {
        strengthMessage.textContent = "Strong password";
        strengthMessage.style.color = "green";
    } else {
        strengthMessage.textContent = "Medium strength password";
        strengthMessage.style.color = "orange";
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');
const form = document.getElementById("buyerRegisterForm");

form.addEventListener("submit", async function(e) {
    e.preventDefault();

    // Validation
    const email = document.getElementById("email").value;
    const confirmEmail = document.getElementById("confirmEmail").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;
    const phone = document.getElementById("phone").value;
    const terms = document.getElementById("terms").checked;
    const message = document.getElementById("message");

    if (email !== confirmEmail) {
        message.textContent = "Emails do not match!";
        message.style.color = "red";
        return;
    }

    if (password !== confirmPassword) {
        message.textContent = "Passwords do not match!";
        message.style.color = "red";
        return;
    }

    if (!terms) {
        message.textContent = "You must accept Terms & Conditions.";
        message.style.color = "red";
        return;
    }

    if (!/^07\d{8}$/.test(phone)) {
        message.textContent = "Invalid Kenyan phone number.";
        message.style.color = "red";
        return;
    }

    // Submit via AJAX
    const formData = new FormData(form);

    try {
        const response = await fetch("/buyer-register/", {
            method: "POST",
            headers: {
                "X-CSRFToken": csrftoken
            },
            body: formData
        });

        const data = await response.json();

        if (data.success) {
            window.location.href = data.redirect_url;
        } else {
            message.textContent = data.error;
            message.style.color = "red";
        }
    } catch (err) {
        message.textContent = "An error occurred. Try again.";
        message.style.color = "red";
        console.error(err);
    }
});