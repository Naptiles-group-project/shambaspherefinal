document.getElementById("advisorForm").addEventListener("submit", function(e){

    e.preventDefault();

    let advisors = JSON.parse(localStorage.getItem("advisors")) || [];

    const newAdvisor = {
        id: Date.now(),
        fullName: document.getElementById("fullName").value,
        email: document.getElementById("email").value,
        phone: document.getElementById("phone").value,
        specialization: document.getElementById("specialization").value,
        bio: document.getElementById("bio").value,
        password: document.getElementById("password").value,
        role: "Advisor",
        status: "Pending", // Must be approved by Admin
        date: new Date().toLocaleString()
    };

    // Check if email already exists
    const exists = advisors.some(a => a.email === newAdvisor.email);

    if(exists){
        document.getElementById("message").innerText = "Email already registered!";
        document.getElementById("message").style.color = "red";
        return;
    }

    advisors.push(newAdvisor);

    localStorage.setItem("advisors", JSON.stringify(advisors));

    document.getElementById("message").innerText = 
        "Registration submitted! Awaiting admin approval.";
    document.getElementById("message").style.color = "green";

    this.reset();
});