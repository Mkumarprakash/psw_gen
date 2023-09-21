// script.js
document.getElementById('generate').addEventListener('click', () => {
    const length = document.getElementById('length').value;
    fetch(`/generate-password?length=${length}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('password').innerText = `Generated Password: ${data.password}`;
        });
});
