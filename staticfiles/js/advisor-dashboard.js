/*crsf function
function getCSRFToken() {
    return document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken'))
        .split('=')[1];
}




const form = document.getElementById("postForm");
const postsContainer = document.getElementById("postsContainer");
const profileWrapper = document.getElementById("profileWrapper");
const profileDropdown = document.getElementById("profileDropdown");

/* =========================
   PROFILE DROPDOWN
========================= */
profileWrapper.addEventListener("click", () => {
    profileDropdown.style.display =
        profileDropdown.style.display === "flex" ? "none" : "flex";
});

/* Close dropdown when clicking outside */
document.addEventListener("click", (e) => {
    if (!profileWrapper.contains(e.target)) {
        profileDropdown.style.display = "none";
    }
});

/* =========================
   DARK MODE
========================= */
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");

    const isDark = document.body.classList.contains("dark-mode");
    localStorage.setItem("advisorDarkMode", isDark);
}

/* Load dark mode preference */
window.addEventListener("DOMContentLoaded", () => {
    const darkMode = localStorage.getItem("advisorDarkMode") === "true";
    if (darkMode) {
        document.body.classList.add("dark-mode");
    }
});

/* =========================
   LOGOUT
========================= */
function logout() {
    alert("Logged out successfully!");
    window.location.href = "/logout/";
 // adjust if needed
}

/* =========================
   EDIT PROFILE
========================= */
function openEditProfile() {
    const name = prompt("Enter new name:");
    const specialization = prompt("Enter specialization:");

    if (name) {
        document.getElementById("advisorName").innerText = name;
    }

    if (specialization) {
        document.getElementById("advisorSpecialization").innerText = specialization;
    }

    profileDropdown.style.display = "none";
}

/* =========================
   CREATE POST
========================= */
/*form.addEventListener("submit", function(e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append("title", document.getElementById("postTitle").value);
    formData.append("category", document.getElementById("category").value);
    formData.append("content", document.getElementById("postContent").value);
       
    const imageFile = document.getElementById("postImage").files[0];
    if (imageFile) {
    formData.append("image", imageFile);
}

    fetch("/create-advisor-post/", {
        method: "POST",
        body: formData,
        headers: {
            "X-CSRFToken": getCSRFToken()
        }
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            alert("Post created!");
            form.reset();
        }
    });
});


/* =========================
   RENDER POSTS
========================= */
function renderPosts() {
    postsContainer.innerHTML = "";

    posts.forEach(post => {
        const card = document.createElement("div");
        card.classList.add("post-card");

        card.innerHTML = `
            <h3>${post.title}</h3>
            <p><strong>Category:</strong> ${post.category}</p>
            <p>${post.content}</p>
            <button onclick="deletePost(${post.id})">Delete</button>
        `;

        postsContainer.appendChild(card);
    });

    document.getElementById("totalPosts").innerText = posts.length;
}

/*function deletePost(id) {
    posts = posts.filter(p => p.id !== id);
    /*localStorage.setItem("advisorPosts", JSON.stringify(posts));
    /*renderPosts();
}

renderPosts();

<link rel="stylesheet" href="{% static 'myapp/advisor-dashboard.css' %}">
<script src="{% static 'myapp/advisor-dashboard.js' %}"></script>


