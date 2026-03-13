// Role-based Login Form Injection
const loginContainer = document.getElementById('login-form-container');
const loginBtns = document.querySelectorAll('.role-login-btn');

loginBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        const role = btn.getAttribute('data-role');
        loginContainer.innerHTML = generateLoginForm(role);
    });
});

// Generate role-specific login form
function generateLoginForm(role) {
    return `
        <form class="role-login-form" onsubmit="handleLogin(event, '${role}')">
            <input type="text" placeholder="Username" required>
            <input type="password" placeholder="Password" required>
            <button type="submit">Login as ${role.charAt(0).toUpperCase() + role.slice(1)}</button>
        </form>
    `;
}

// Handle login submission (simulated)
function handleLogin(e, role) {
    e.preventDefault();
    const form = e.target;
    const username = form.querySelector('input[type="text"]').value;
    const password = form.querySelector('input[type="password"]').value;

    if(username && password) {
        alert(`Welcome ${username}! Redirecting to ${role} dashboard...`);
        // Placeholder for actual dashboard page
        window.location.href = `${role}-dashboard.html`;
    } else {
        alert("Please enter valid credentials.");
    }
}