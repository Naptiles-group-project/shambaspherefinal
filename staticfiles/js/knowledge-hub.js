// ================= GET CURRENT USER =================
let currentUser = JSON.parse(localStorage.getItem("currentUser")) || {
    name: "Demo User",
    role: "Buyer" // Change to Admin / Advisor / Farmer / Buyer to test
};

let posts = JSON.parse(localStorage.getItem("knowledgePosts")) || [];

// ================= DOM =================
const createSection = document.getElementById("createPostSection");
const postsContainer = document.getElementById("postsContainer");

// ================= ROLE CONTROL =================
if(currentUser.role !== "Admin" && currentUser.role !== "Advisor"){
    createSection.style.display = "none";
}

// ================= CREATE POST =================
function createPost(){

    const title = document.getElementById("postTitle").value.trim();
    const content = document.getElementById("postContent").value.trim();

    if(!title || !content){
        alert("Please fill all fields");
        return;
    }

    const newPost = {
        id: Date.now(),
        title,
        content,
        author: currentUser.name,
        role: currentUser.role,
        date: new Date().toLocaleString()
    };

    posts.unshift(newPost);
    savePosts();

    document.getElementById("postTitle").value = "";
    document.getElementById("postContent").value = "";
}

// ================= RENDER POSTS =================
function renderPosts(){

    postsContainer.innerHTML = "";

    posts.forEach(post => {

        // Only show Advisor & Admin posts publicly
        if(post.role !== "Advisor" && post.role !== "Admin") return;

        const card = document.createElement("div");
        card.classList.add("post-card");

        card.innerHTML = `
            <h4>${post.title}</h4>
            <div class="post-meta">
                By ${post.author} (${post.role}) | ${post.date}
            </div>
            <p>${post.content}</p>
        `;

        // Edit/Delete only for Admin or post author Advisor
        if(currentUser.role === "Admin" || 
           (currentUser.role === "Advisor" && post.author === currentUser.name)){

            const actions = document.createElement("div");
            actions.classList.add("post-actions");

            actions.innerHTML = `
                <button class="edit-btn" onclick="editPost(${post.id})">Edit</button>
                <button class="delete-btn" onclick="deletePost(${post.id})">Delete</button>
            `;

            card.appendChild(actions);
        }

        postsContainer.appendChild(card);
    });
}

// ================= EDIT =================
function editPost(id){

    const post = posts.find(p => p.id === id);

    const newTitle = prompt("Edit Title", post.title);
    const newContent = prompt("Edit Content", post.content);

    if(newTitle && newContent){
        post.title = newTitle;
        post.content = newContent;
        savePosts();
    }
}

// ================= DELETE =================
function deletePost(id){
    posts = posts.filter(p => p.id !== id);
    savePosts();
}

// ================= SAVE =================
function savePosts(){
    localStorage.setItem("knowledgePosts", JSON.stringify(posts));
    renderPosts();
}

// ================= INIT =================
renderPosts();


/* ================= DJANGO BACKEND READY =================

Replace localStorage logic with:

GET:    /api/knowledge-posts/
POST:   /api/knowledge-posts/
PUT:    /api/knowledge-posts/:id/
DELETE: /api/knowledge-posts/:id/

And enforce permissions in Django:

- Only Admin & Advisor can POST
- Buyers & Farmers: READ ONLY
- Only author or admin can edit/delete

*/