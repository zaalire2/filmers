const tabs = document.querySelectorAll('.tab');
const forms = document.querySelectorAll('.form');

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        forms.forEach(form => form.classList.remove('active'));
        document.getElementById(tab.dataset.target).classList.add('active');
    });
});

function showForgotPassword() {
    document.getElementById('login').style.display = 'none';
    document.getElementById('forgot-password').style.display = 'block';
}

function backToLogin() {
    document.getElementById('forgot-password').style.display = 'none';
    document.getElementById('login').style.display = 'block';
}
