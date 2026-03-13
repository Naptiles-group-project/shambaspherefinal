// // Simulated multi-farmer data
// let farmers = [
//     {
//         name: 'Farmer John',
//         produce: [],
//         orders: []
//     },
//     {
//         name: 'Farmer Mary',
//         produce: [],
//         orders: []
//     }
// ];

// // Simulate logged in farmer
// let loggedInFarmerIndex = 0;

// // DOM Elements
// const addProduceForm = document.getElementById('add-produce-form');
// const produceList = document.getElementById('produce-list');
// const marketplaceList = document.getElementById('marketplace-list');
// const ordersList = document.getElementById('orders-list');
// const imageUpload = document.getElementById('image-upload');
// const imagePreview = document.getElementById('image-preview');

// const totalListingsEl = document.getElementById('total-listings');
// const totalOrdersEl = document.getElementById('total-orders');
// const totalIncomeEl = document.getElementById('total-income');

// let uploadedImageBase64 = "";

// // ================= IMAGE PREVIEW =================
// imageUpload.addEventListener('change', function () {
//     const file = this.files[0];
//     if (file) {
//         const reader = new FileReader();
//         reader.onload = function (e) {
//             uploadedImageBase64 = e.target.result;
//             imagePreview.src = uploadedImageBase64;
//             imagePreview.style.display = "block";
//         };
//         reader.readAsDataURL(file);
//     }
// });

// // ================= ADD PRODUCE =================
// addProduceForm.addEventListener('submit', (e) => {
//     e.preventDefault();

//     const name = addProduceForm[0].value;
//     const quantity = parseFloat(addProduceForm[1].value);
//     const price = parseFloat(addProduceForm[2].value);

//     const image = uploadedImageBase64 || 
//         'https://via.placeholder.com/200x120.png?text=Produce';

//     const status = quantity > 0 ? "Available" : "Sold";

//     const newProduce = { name, quantity, price, image, status };

//     farmers[loggedInFarmerIndex].produce.push(newProduce);

//     addProduceForm.reset();
//     imagePreview.style.display = "none";
//     uploadedImageBase64 = "";

//     renderProduce();
//     renderMarketplace();
//     updateStats();
// });

// // ================= RENDER FARMER LISTINGS =================
// function renderProduce() {
//     const farmer = farmers[loggedInFarmerIndex];
//     produceList.innerHTML = '';

//     farmer.produce.forEach((item, index) => {

//         item.status = item.quantity > 0 ? "Available" : "Sold";

//         const card = document.createElement('div');
//         card.className = 'produce-card';

//         card.innerHTML = `
//             <span class="status-badge ${item.status === "Available" ? "available" : "sold"}">
//                 ${item.status}
//             </span>
//             <img src="${item.image}" alt="${item.name}">
//             <h4>${item.name}</h4>
//             <p>Qty: ${item.quantity} kg</p>
//             <p>Price: KSh ${item.price}/kg</p>
//             <button onclick="editProduce(${index})">Edit</button>
//             <button onclick="deleteProduce(${index})">Delete</button>
//         `;

//         produceList.appendChild(card);
//     });
// }

// // ================= RENDER MARKETPLACE =================
// function renderMarketplace() {
//     marketplaceList.innerHTML = '';

//     farmers.forEach((farmer) => {
//         farmer.produce.forEach((item) => {

//             item.status = item.quantity > 0 ? "Available" : "Sold";

//             const card = document.createElement('div');
//             card.className = 'produce-card';

//             card.innerHTML = `
//                 <span class="status-badge ${item.status === "Available" ? "available" : "sold"}">
//                     ${item.status}
//                 </span>
//                 <img src="${item.image}" alt="${item.name}">
//                 <h4>${item.name}</h4>
//                 <p>Qty: ${item.quantity} kg</p>
//                 <p>Price: KSh ${item.price}/kg</p>
//                 <p><strong>Farmer:</strong> ${farmer.name}</p>
//             `;

//             marketplaceList.appendChild(card);
//         });
//     });
// }

// // ================= EDIT PRODUCE =================
// function editProduce(index) {
//     const farmer = farmers[loggedInFarmerIndex];
//     const item = farmer.produce[index];

//     const newQuantity = prompt("Edit Quantity (kg):", item.quantity);

//     if (newQuantity !== null) {
//         item.quantity = parseFloat(newQuantity);
//         item.status = item.quantity > 0 ? "Available" : "Sold";
//     }

//     renderProduce();
//     renderMarketplace();
//     updateStats();
// }

// // ================= DELETE PRODUCE =================
// function deleteProduce(index) {
//     if (confirm("Delete this produce?")) {
//         farmers[loggedInFarmerIndex].produce.splice(index, 1);
//         renderProduce();
//         renderMarketplace();
//         updateStats();
//     }
// }

// // ================= DASHBOARD STATS =================
// function updateStats() {
//     const farmer = farmers[loggedInFarmerIndex];

//     totalListingsEl.innerText = farmer.produce.length;
//     totalOrdersEl.innerText = farmer.orders.length;

//     const income = farmer.orders
//         .filter(o => o.status === 'Accepted')
//         .reduce((acc, o) => acc + (o.quantity * o.price), 0);

//     totalIncomeEl.innerText = `KSh ${income}`;
// }

// // Initial render
// renderProduce();
// renderMarketplace();
// updateStats();


// Image preview before uploading
const imageUpload = document.getElementById('image-upload');
const imagePreview = document.getElementById('image-preview');

if (imageUpload) {
    imageUpload.addEventListener('change', function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                imagePreview.src = e.target.result;
                imagePreview.style.display = 'block';
            };
            reader.readAsDataURL(file);
        }
    });
}