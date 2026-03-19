// ================= SAMPLE DATA =================
let users = JSON.parse(localStorage.getItem("users")) || [
    {name:"John Farmer", email:"john@mail.com", role:"Farmer", suspended:false},
    {name:"Mary Buyer", email:"mary@mail.com", role:"Buyer", suspended:false}
];

let products = JSON.parse(localStorage.getItem("products")) || [
    {id:1, name:"Tomatoes", farmer:"John Farmer", price:200, status:"Pending"},
    {id:2, name:"Maize", farmer:"John Farmer", price:1500, status:"Available"}
];

let orders = JSON.parse(localStorage.getItem("orders")) || [
    {id:1, product:"Tomatoes", buyer:"Mary Buyer", price:200, date:new Date().toLocaleDateString()}
];

// ================= DOM =================
const usersContainer = document.getElementById("usersContainer");
const productsContainer = document.getElementById("productsContainer");
const ordersContainer = document.getElementById("ordersContainer");
const logContainer = document.getElementById("logContainer");

// ================= USERS =================
function renderUsers(){
    usersContainer.innerHTML = "";

    users.forEach(user=>{
        usersContainer.innerHTML += `
            <div class="card">
                <strong>${user.name}</strong> (${user.email})
                <p>Role:
                    <select onchange="changeRole('${user.email}', this.value)">
                        <option ${user.role==="Farmer"?"selected":""}>Farmer</option>
                        <option ${user.role==="Buyer"?"selected":""}>Buyer</option>
                        <option ${user.role==="Advisor"?"selected":""}>Advisor</option>
                    </select>
                </p>
                <p>Status: ${user.suspended ? "Suspended" : "Active"}</p>
                <button class="suspend" onclick="suspendUser('${user.email}')">Suspend</button>
            </div>
        `;
    });
}

function suspendUser(email){
    users = users.map(u =>
        u.email === email ? {...u, suspended:true} : u
    );
    saveUsers();
    notify("User Suspended");
    logActivity("Suspended user: " + email);
}

function changeRole(email, newRole){
    users = users.map(u =>
        u.email === email ? {...u, role:newRole} : u
    );
    saveUsers();
    notify("Role Updated");
    logActivity("Changed role of " + email + " to " + newRole);
}

function saveUsers(){
    localStorage.setItem("users", JSON.stringify(users));
    renderUsers();
}

// ================= PRODUCTS =================
function renderProducts(){
    productsContainer.innerHTML = "";

    products.forEach(product=>{
        productsContainer.innerHTML += `
            <div class="card">
                <strong>${product.name}</strong>
                <p>Farmer: ${product.farmer}</p>
                <p>Price: KSh ${product.price}</p>
                <p>Status: ${product.status}</p>

                ${product.status==="Pending" ? `
                    <button class="approve" onclick="approveProduct(${product.id})">Approve</button>
                    <button class="reject" onclick="rejectProduct(${product.id})">Reject</button>
                ` : ""}
            </div>
        `;
    });
}

function approveProduct(id){
    updateProductStatus(id,"Available");
}

function rejectProduct(id){
    updateProductStatus(id,"Rejected");
}

function updateProductStatus(id,status){
    products = products.map(p =>
        p.id === id ? {...p, status:status} : p
    );
    saveProducts();
    notify("Product " + status);
    logActivity(status + " product ID: " + id);
}

function saveProducts(){
    localStorage.setItem("products", JSON.stringify(products));
    renderProducts();
}

// ================= ORDERS =================
function renderOrders(){
    ordersContainer.innerHTML = "";

    orders.forEach(order=>{
        ordersContainer.innerHTML += `
            <div class="card">
                <strong>${order.product}</strong>
                <p>Buyer: ${order.buyer}</p>
                <p>Price: KSh ${order.price}</p>
                <p>Date: ${order.date}</p>
            </div>
        `;
    });
}

// ================= CSV EXPORT =================
function exportCSV(){
    let csv = "Name,Email,Role,Status\n";

    users.forEach(u=>{
        csv += `${u.name},${u.email},${u.role},${u.suspended?"Suspended":"Active"}\n`;
    });

    const blob = new Blob([csv], {type:"text/csv"});
    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "users-report.csv";
    a.click();

    notify("CSV Exported");
    logActivity("Exported users report");
}

// ================= NOTIFICATIONS =================
function notify(message){
    const notification = document.getElementById("notification");
    notification.innerText = message;
    notification.style.display = "block";

    setTimeout(()=>{
        notification.style.display = "none";
    },3000);
}

// ================= ACTIVITY LOG =================
function logActivity(action){
    let logs = JSON.parse(localStorage.getItem("adminLogs")) || [];

    logs.push({
        action: action,
        date: new Date().toLocaleString()
    });

    localStorage.setItem("adminLogs", JSON.stringify(logs));
    renderLogs();
}

function renderLogs(){
    const logs = JSON.parse(localStorage.getItem("adminLogs")) || [];
    logContainer.innerHTML = "";

    logs.forEach(log=>{
        logContainer.innerHTML += `
            <div class="card">
                ${log.date} - ${log.action}
            </div>
        `;
    });
}

// ================= DJANGO BACKEND READY =================
/*
Replace localStorage with:

fetch("http://127.0.0.1:8000/api/products/")
.then(res => res.json())
.then(data => {
    products = data;
    renderProducts();
});

And similar POST/PATCH requests for:
- Approve product
- Suspend user
- Change role
- Fetch orders
*/

// ================= INIT =================
renderUsers();
renderProducts();
renderOrders();
renderLogs();