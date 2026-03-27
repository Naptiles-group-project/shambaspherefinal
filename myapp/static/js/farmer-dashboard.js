document.addEventListener("DOMContentLoaded", function () {
    // ---------------- Menu Toggle ----------------
    const menuToggle = document.getElementById("menuToggle");
    const mobileNav = document.getElementById("mobileNav");

    if (menuToggle && mobileNav) {
        menuToggle.addEventListener("click", function (e) {
            e.stopPropagation();
            mobileNav.classList.toggle("show");
        });

        document.addEventListener("click", function (e) {
            if (!mobileNav.contains(e.target) && !menuToggle.contains(e.target)) {
                mobileNav.classList.remove("show");
            }
        });
    }

    // ---------------- Image Preview ----------------
    const imageUpload = document.getElementById("image-upload");
    const imagePreview = document.getElementById("image-preview");

    if (imageUpload && imagePreview) {
        imageUpload.addEventListener("change", function () {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    imagePreview.src = e.target.result;
                    imagePreview.style.display = "block";
                };
                reader.readAsDataURL(file);
            }
        });
    }

    // ---------------- CSRF Helper ----------------
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let cookie of cookies) {
                cookie = cookie.trim();
                if (cookie.startsWith(name + "=")) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie("csrftoken");

    // ---------------- Add Produce ----------------
    const addProduceForm = document.getElementById("add-produce-form");
    if (addProduceForm) {
        addProduceForm.addEventListener("submit", function (e) {
            e.preventDefault();
            const form = e.target;
            const data = new FormData(form);

            fetch(form.action || window.location.href, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrftoken,
                    "X-Requested-With": "XMLHttpRequest"
                },
                body: data
            })
            .then(res => res.json())
            .then(json => {
                if (json.success) {
                    const produce = json.produce;
                    const produceList = document.getElementById("produce-list");

                    const div = document.createElement("div");
                    div.className = "produce-item";
                    div.id = `produce-${produce.id}`;
                    div.innerHTML = `
                        <img src="${produce.image_url}" alt="${produce.name}" width="100">
                        <p>${produce.name}</p>
                        <p>${produce.quantity} kg</p>
                        <p>KSh ${produce.price}</p>
                        <p>Status: ${produce.status}</p>
                        <button class="edit-btn" data-id="${produce.id}">Edit</button>
                        <button class="delete-btn" data-id="${produce.id}">Delete</button>
                    `;
                    produceList.prepend(div);

                    attachEditDeleteEvents(div, produce.id);

                    if (produce.status === "Available") {
                        const marketplaceList = document.getElementById("marketplace-list");
                        if (marketplaceList) {
                            const divMarket = document.createElement("div");
                            divMarket.className = "marketplace-item";
                            divMarket.id = `marketplace-${produce.id}`;
                            divMarket.innerHTML = `
                                <img src="${produce.image_url}" alt="${produce.name}" width="100">
                                <p>${produce.name}</p>
                                <p>${produce.quantity} kg</p>
                                <p>KSh ${produce.price}</p>
                                <p>Farmer: ${produce.farmer_username}</p>
                            `;
                            marketplaceList.prepend(divMarket);
                        }
                    }

                    form.reset();
                    if (imagePreview) {
                        imagePreview.style.display = "none";
                        imagePreview.src = "";
                    }
                } else {
                    alert("Failed to add produce: " + json.error);
                }
            })
            .catch(err => console.error(err));
        });
    }

    // ---------------- Edit & Delete ----------------
    function attachEditDeleteEvents(container, produceId) {
        const editBtn = container.querySelector(".edit-btn");
        const deleteBtn = container.querySelector(".delete-btn");

        if (editBtn) {
            editBtn.addEventListener("click", () => {
                document.getElementById("editName").value = container.querySelector("p:nth-of-type(1)").innerText;
                document.getElementById("editQuantity").value = container.querySelector("p:nth-of-type(2)").innerText.replace(" kg", "");
                document.getElementById("editPrice").value = container.querySelector("p:nth-of-type(3)").innerText.replace("KSh ", "");
                document.getElementById("editStatus").value = container.querySelector("p:nth-of-type(4)").innerText.replace("Status: ", "");
                document.getElementById("saveChangesBtn").setAttribute("data-id", produceId);
                document.getElementById("editModal").style.display = "flex";
            });
        }

        if (deleteBtn) {
            deleteBtn.addEventListener("click", () => {
                if (!confirm("Are you sure you want to delete this produce?")) return;

                fetch(`/delete-produce/${produceId}/`, {
                    method: "POST",
                    headers: { "X-CSRFToken": csrftoken }
                })
                .then(res => res.json())
                .then(json => {
                    if (json.success) {
                        container.remove();
                        const marketItem = document.getElementById(`marketplace-${produceId}`);
                        if (marketItem) marketItem.remove();
                    } else {
                        alert("Delete failed: " + json.error);
                    }
                })
                .catch(err => console.error(err));
            });
        }
    }

    document.querySelectorAll(".produce-item").forEach(div => {
        const produceId = div.id.split("-")[1];
        attachEditDeleteEvents(div, produceId);
    });

    // ---------------- Close Modal ----------------
    const closeBtn = document.querySelector(".close-btn");
    if (closeBtn) {
        closeBtn.addEventListener("click", () => {
            document.getElementById("editModal").style.display = "none";
        });
    }

    // ---------------- Save Changes ----------------
    const saveChangesBtn = document.getElementById("saveChangesBtn");
    if (saveChangesBtn) {
        saveChangesBtn.addEventListener("click", () => {
            const produceId = saveChangesBtn.getAttribute("data-id");
            const data = new FormData();

            data.append("name", document.getElementById("editName").value);
            data.append("quantity", document.getElementById("editQuantity").value);
            data.append("price", document.getElementById("editPrice").value);
            data.append("status", document.getElementById("editStatus").value);

            const imageFile = document.getElementById("editImage").files[0];
            if (imageFile) data.append("image", imageFile);

            fetch(`/edit-produce/${produceId}/`, {
                method: "POST",
                headers: { "X-CSRFToken": csrftoken },
                body: data
            })
            .then(res => res.json())
            .then(json => {
                if (json.success) {
                    const container = document.getElementById(`produce-${produceId}`);
                    container.querySelector("p:nth-of-type(1)").innerText = json.produce.name;
                    container.querySelector("p:nth-of-type(2)").innerText = json.produce.quantity + " kg";
                    container.querySelector("p:nth-of-type(3)").innerText = "KSh " + json.produce.price;
                    container.querySelector("p:nth-of-type(4)").innerText = "Status: " + json.produce.status;

                    if (json.produce.image_url) {
                        container.querySelector("img").src = json.produce.image_url;
                    }

                    const marketItem = document.getElementById(`marketplace-${produceId}`);
                    if (json.produce.status === "Available") {
                        if (marketItem) {
                            marketItem.querySelector("p:nth-of-type(1)").innerText = json.produce.name;
                            marketItem.querySelector("p:nth-of-type(2)").innerText = json.produce.quantity + " kg";
                            marketItem.querySelector("p:nth-of-type(3)").innerText = "KSh " + json.produce.price;
                            if (json.produce.image_url) {
                                marketItem.querySelector("img").src = json.produce.image_url;
                            }
                        }
                    } else if (marketItem) {
                        marketItem.remove();
                    }

                    document.getElementById("editModal").style.display = "none";
                } else {
                    alert("Update failed: " + json.error);
                }
            })
            .catch(err => console.error(err));
        });
    }
});