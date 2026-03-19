let user = JSON.parse(localStorage.getItem("currentUser")) || {
    fullName: "John Doe",
    role: "Farmer",
    email: "john@email.com",
    phone: "0712345678",
    location: "Nakuru",
    image: "https://via.placeholder.com/150"
};

/* LOAD PROFILE */
function loadProfile() {
    document.getElementById("fullName").innerText = user.fullName;
    document.getElementById("roleBadge").innerText = user.role;
    document.getElementById("email").innerText = user.email;
    document.getElementById("phone").innerText = user.phone;
    document.getElementById("location").innerText = user.location;
    document.getElementById("profileImage").src = user.image;

    loadRoleSpecificSection();
}

function loadRoleSpecificSection() {
    const section = document.getElementById("roleSpecificSection");

    if(user.role === "Farmer") {
        section.innerHTML = `
            <h4>Farmer Information</h4>
            <p>Total Listings: ${localStorage.getItem("farmerListings") || 0}</p>
            <p>Total Sales: KSh ${localStorage.getItem("farmerSales") || 0}</p>
        `;
    }

    else if(user.role === "Buyer") {
        section.innerHTML = `
            <h4>Buyer Information</h4>
            <p>Total Orders: ${localStorage.getItem("buyerOrders") || 0}</p>
            <p>Items in Cart: ${localStorage.getItem("cartCount") || 0}</p>
        `;
    }

    else if(user.role === "Advisor") {
        section.innerHTML = `
            <h4>Advisor Information</h4>
            <p>Total Advisories Posted: ${localStorage.getItem("advisorPostsCount") || 0}</p>
        `;
    }

    else if(user.role === "Admin") {
        section.innerHTML = `
            <h4>Admin Information</h4>
            <p>Total Users: ${localStorage.getItem("totalUsers") || 0}</p>
            <p>Total Products: ${localStorage.getItem("totalProducts") || 0}</p>
        `;
    }
}

/* EDIT PROFILE */
function openEditModal() {
    document.getElementById("editModal").style.display = "flex";

    document.getElementById("editName").value = user.fullName;
    document.getElementById("editEmail").value = user.email;
    document.getElementById("editPhone").value = user.phone;
    document.getElementById("editLocation").value = user.location;
}

function closeEditModal() {
    document.getElementById("editModal").style.display = "none";
}

function saveProfile() {
    user.fullName = document.getElementById("editName").value;
    user.email = document.getElementById("editEmail").value;
    user.phone = document.getElementById("editPhone").value;
    user.location = document.getElementById("editLocation").value;

    localStorage.setItem("currentUser", JSON.stringify(user));
    loadProfile();
    closeEditModal();
}

/* IMAGE UPLOAD */
document.getElementById("imageUpload").addEventListener("change", function(e) {
    const file = e.target.files[0];
    const reader = new FileReader();

    reader.onload = function() {
        user.image = reader.result;
        localStorage.setItem("currentUser", JSON.stringify(user));
        loadProfile();
    };

    if(file) {
        reader.readAsDataURL(file);
    }
});

/* DARK MODE */
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
    localStorage.setItem("darkMode", document.body.classList.contains("dark-mode"));
}

window.onload = function() {
    if(localStorage.getItem("darkMode") === "true") {
        document.body.classList.add("dark-mode");
    }
    loadProfile();
};

/* LOGOUT */
function logout() {
    localStorage.removeItem("currentUser");
    window.location.href = "login.html";
}