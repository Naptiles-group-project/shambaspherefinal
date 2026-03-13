/* ===============================
   LOAD PRODUCTS
=================================*/

// Load farmer products from localStorage
let products = JSON.parse(localStorage.getItem("products")) || [];

// Load cart from storage
let cart = JSON.parse(localStorage.getItem("cart")) || [];

// DOM
const productsContainer = document.getElementById("productsContainer");
const cartModal = document.getElementById("cartModal");
const cartItemsContainer = document.getElementById("cartItems");
const cartTotalElement = document.getElementById("cartTotal");
const cartCountElement = document.getElementById("cartCount");

/* ===============================
   RENDER PRODUCTS
=================================*/

function renderProducts(productList = products) {

    productsContainer.innerHTML = "";

    if(productList.length === 0){
        productsContainer.innerHTML = "<p>No products available.</p>";
        return;
    }

    productList.forEach(product => {

        // Only show available products
        if(product.status && product.status !== "Available") return;

        const card = document.createElement("div");
        card.classList.add("product-card");

        card.innerHTML = `
            <img src="${product.image || 'https://via.placeholder.com/300'}" alt="${product.name}">
            <h4>${product.name}</h4>
            <p>KSh ${product.price}</p>
            <button onclick="addToCart(${product.id})">Add to Cart</button>
        `;

        productsContainer.appendChild(card);
    });
}

renderProducts();


/* ===============================
   SEARCH FUNCTION
=================================*/

document.getElementById("searchInput").addEventListener("input", function(){

    const value = this.value.toLowerCase();

    const filtered = products.filter(product =>
        product.name.toLowerCase().includes(value)
    );

    renderProducts(filtered);
});


/* ===============================
   CATEGORY FILTER
=================================*/

function filterCategory(category){

    if(category === "All"){
        renderProducts(products);
        return;
    }

    const filtered = products.filter(product =>
        product.category === category
    );

    renderProducts(filtered);
}


/* ===============================
   CART FUNCTIONS
=================================*/

function toggleCart(){
    cartModal.classList.toggle("active");
}

function addToCart(id){

    const product = products.find(p => p.id === id);

    if(!product) return;

    cart.push(product);

    saveCart();
    updateCart();
}

function removeFromCart(index){
    cart.splice(index,1);
    saveCart();
    updateCart();
}

function clearCart(){
    cart = [];
    saveCart();
    updateCart();
}

function updateCart(){

    cartItemsContainer.innerHTML = "";

    let total = 0;

    cart.forEach((item,index)=>{

        total += Number(item.price);

        cartItemsContainer.innerHTML += `
            <div class="cart-item">
                <span>${item.name} - KSh ${item.price}</span>
                <button onclick="removeFromCart(${index})">❌</button>
            </div>
        `;
    });

    cartTotalElement.innerText = total;
    cartCountElement.innerText = cart.length;
}

function cashout(){

    if(cart.length === 0){
        alert("Cart is empty!");
        return;
    }

    let total = cart.reduce((sum,item)=> sum + Number(item.price),0);

    alert("Payment successful! Total Paid: KSh " + total);

    cart = [];
    saveCart();
    updateCart();

    toggleCart();
}

function saveCart(){
    localStorage.setItem("cart", JSON.stringify(cart));
}


/* ===============================
   INITIALIZE CART ON LOAD
=================================*/

updateCart();