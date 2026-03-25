// ================= FARMERS DATA =================
let farmers = [
    {
        name: "Farmer John",
        produce: [],
        orders: []
    },
    {
        name: "Farmer Mary",
        produce: [],
        orders: []
    }
];

// Simulate logged in farmer
let loggedInFarmerIndex = 0;
let currentEditIndex = null;
let uploadedImageBase64 = "";

// ================= DOM ELEMENTS =================
const addProduceForm = document.getElementById("add-produce-form");
const produceList = document.getElementById("produce-list");
const marketplaceList = document.getElementById("marketplace-list");
const ordersList = document.getElementById("orders-list");

const imageUpload = document.getElementById("image-upload");
const imagePreview = document.getElementById("image-preview");

const totalListingsEl = document.getElementById("total-listings");
const totalOrdersEl = document.getElementById("total-orders");
const totalIncomeEl = document.getElementById("total-income");

// ================= IMAGE PREVIEW =================
imageUpload.addEventListener("change", function () {
    const file = this.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function (e) {
        uploadedImageBase64 = e.target.result;
        imagePreview.src = uploadedImageBase64;
        imagePreview.style.display = "block";
    };
    reader.readAsDataURL(file);
});

// ================= ADD PRODUCE =================
addProduceForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const name = addProduceForm[0].value;
    const quantity = parseFloat(addProduceForm[1].value);
    const price = parseFloat(addProduceForm[2].value);

    const image = uploadedImageBase64 || 
        "https://via.placeholder.com/200x120.png?text=Produce";

    const status = quantity > 0 ? "Available" : "Sold";

    const newProduce = { name, quantity, price, image, status };

    farmers[loggedInFarmerIndex].produce.push(newProduce);

    addProduceForm.reset();
    imagePreview.style.display = "none";
    uploadedImageBase64 = "";

    renderProduce();
    renderMarketplace();
    updateStats();
});

// ================= RENDER FARMER PRODUCE =================
function renderProduce() {
    const farmer = farmers[loggedInFarmerIndex];
    produceList.innerHTML = "";

    farmer.produce.forEach((item, index) => {

        item.status = item.quantity > 0 ? "Available" : "Sold";

        const card = document.createElement("div");
        card.className = "produce-card";

        card.innerHTML = `
            <span class="status-badge ${item.status === "Available" ? "available" : "sold"}">
                ${item.status}
            </span>
            <img src="${item.image}" alt="${item.name}">
            <h4>${item.name}</h4>
            <p>Qty: ${item.quantity} kg</p>
            <p>Price: KSh ${item.price}/kg</p>
            <button onclick="editProduce(${index})">Edit</button>
            <button onclick="deleteProduce(${index})">Delete</button>
        `;

        produceList.appendChild(card);
    });
}

// ================= RENDER MARKETPLACE =================
function renderMarketplace() {
    marketplaceList.innerHTML = "";

    farmers.forEach((farmer) => {
        farmer.produce.forEach((item) => {

            item.status = item.quantity > 0 ? "Available" : "Sold";

            const card = document.createElement("div");
            card.className = "produce-card";

            card.innerHTML = `
                <span class="status-badge ${item.status === "Available" ? "available" : "sold"}">
                    ${item.status}
                </span>
                <img src="${item.image}" alt="${item.name}">
                <h4>${item.name}</h4>
                <p>Qty: ${item.quantity} kg</p>
                <p>Price: KSh ${item.price}/kg</p>
                <p><strong>Farmer:</strong> ${farmer.name}</p>
            `;

            marketplaceList.appendChild(card);
        });
    });
}

// ================= OPEN EDIT MODAL =================
function editProduce(index) {
    currentEditIndex = index;

    const farmer = farmers[loggedInFarmerIndex];
    const item = farmer.produce[index];

    document.getElementById("editName").value = item.name;
    document.getElementById("editQuantity").value = item.quantity;
    document.getElementById("editPrice").value = item.price;
    document.getElementById("editStatus").value = item.status;

    document.getElementById("editModal").style.display = "block";
}

// ================= CLOSE MODAL =================
function closeModal() {
    document.getElementById("editModal").style.display = "none";
}

// ================= SAVE CHANGES =================
function saveChanges() {
    const farmer = farmers[loggedInFarmerIndex];
    const item = farmer.produce[currentEditIndex];

    const newName = document.getElementById("editName").value;
    const newQuantity = parseFloat(document.getElementById("editQuantity").value);
    const newPrice = parseFloat(document.getElementById("editPrice").value);
    const newStatus = document.getElementById("editStatus").value;
    const imageInput = document.getElementById("editImage");

    item.name = newName;
    item.quantity = newQuantity;
    item.price = newPrice;
    item.status = newStatus;

    if (newStatus === "Sold") {
        item.quantity = 0;
    }

    // If new image selected
    if (imageInput.files.length > 0) {
        const reader = new FileReader();
        reader.onload = function (e) {
            item.image = e.target.result;
            refreshUI();
        };
        reader.readAsDataURL(imageInput.files[0]);
    } else {
        refreshUI();
    }

    closeModal();
}

// ================= DELETE PRODUCE =================
function deleteProduce(index) {
    if (confirm("Delete this produce?")) {
        farmers[loggedInFarmerIndex].produce.splice(index, 1);
        refreshUI();
    }
}

// ================= UPDATE STATS =================
function updateStats() {
    const farmer = farmers[loggedInFarmerIndex];

    totalListingsEl.innerText = farmer.produce.length;
    totalOrdersEl.innerText = farmer.orders.length;

    const income = farmer.orders
        .filter(o => o.status === "Accepted")
        .reduce((acc, o) => acc + (o.quantity * o.price), 0);

    totalIncomeEl.innerText = `KSh ${income}`;
}

// ================= REFRESH EVERYTHING =================
function refreshUI() {
    renderProduce();
    renderMarketplace();
    updateStats();
}

// ================= INITIAL LOAD =================
refreshUI();