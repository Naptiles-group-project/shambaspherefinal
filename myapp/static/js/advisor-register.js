// document.getElementById("advisorForm").addEventListener("submit", function(e){
//     e.preventDefault();

//     const form = e.target;
//     const data = new FormData(form);

//     fetch("{% url 'advisor_register' %}", {
//         method: "POST",
//         headers: {
//             "X-CSRFToken": getCookie('csrftoken'),
//             "X-Requested-With": "XMLHttpRequest"
//         },
//         body: data
//     })
//     .then(res => res.json())
//     .then(json => {
//         const msg = document.getElementById("message");
//         if(json.success){
//             msg.innerText = json.message;
//             msg.style.color = "green";
//             form.reset();
//         } else {
//             msg.innerText = json.error;
//             msg.style.color = "red";
//         }
//     })
//     .catch(err => console.error(err));
// });

    // Check if email already exists
    // const exists = advisors.some(a => a.email === newAdvisor.email);

    // if(exists){
    //     document.getElementById("message").innerText = "Email already registered!";
    //     document.getElementById("message").style.color = "red";
    //     return;
    // }

    // advisors.push(newAdvisor);

    // localStorage.setItem("advisors", JSON.stringify(advisors));

    // document.getElementById("message").innerText = 
    //     "Registration submitted! Awaiting admin approval.";
    // document.getElementById("message").style.color = "green";

    // this.reset();
// });