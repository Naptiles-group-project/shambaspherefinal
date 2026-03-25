let products = JSON.parse(localStorage.getItem("products")) || [];
let orders = JSON.parse(localStorage.getItem("buyerOrdersData")) || [];

const productsContainer = document.getElementById("productsContainer");
const ordersContainer = document.getElementById("ordersContainer");

/* RENDER PRODUCTS */
function renderProducts() {
    productsContainer.innerHTML = "";

    products
        .filter(p => p.status === "Available")
        .forEach(product => {

            const card = document.createElement("div");
            card.classList.add("product-card");

            card.innerHTML = `
                <img src="${product.image || 'https://via.placeholder.com/250'}">
                <h3>${product.name}</h3>
                <p>Seller: ${product.farmerName || "Farmer"}</p>
                <p>KSh ${product.price}</p>
                <button onclick="placeOrder(${product.id})">Order Now</button>
            `;

            productsContainer.appendChild(card);
        });
}

/* PLACE ORDER */
function placeOrder(id) {
    const product = products.find(p => p.id === id);

    if(product) {
        orders.push({
            ...product,
            orderDate: new Date().toLocaleString()
        });

        localStorage.setItem("buyerOrdersData", JSON.stringify(orders));

        alert("Order placed successfully!");
        renderOrders();
        updateStats();
    }
}

/* RENDER ORDERS */
function renderOrders() {
    ordersContainer.innerHTML = "";

    orders.forEach(order => {
        const card = document.createElement("div");
        card.classList.add("order-card");

        card.innerHTML = `
            <h4>${order.name}</h4>
            <p>Price: KSh ${order.price}</p>
            <p>Seller: ${order.farmerName}</p>
            <p>Date: ${order.orderDate}</p>
        `;

        ordersContainer.appendChild(card);
    });
}

/* UPDATE STATS */
function updateStats() {
    document.getElementById("totalOrders").innerText = orders.length;

    let total = orders.reduce((sum, item) => sum + Number(item.price), 0);
    document.getElementById("totalSpent").innerText = "KSh " + total;

    localStorage.setItem("buyerOrders", orders.length);
}

/* LOGOUT */
function logout() {
    localStorage.removeItem("currentUser");
    window.location.href = "login.html";
}

/* INITIALIZE */
renderProducts();
renderOrders();
updateStats();