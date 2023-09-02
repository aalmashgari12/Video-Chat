const loginForm = document.getElementById('login-form');
const signupForm = document.getElementById('signup-form');
const loginLink = document.getElementById('login-link');
const signupLink = document.getElementById('signup-link');

loginLink.addEventListener('click', (event) => {
    event.preventDefault();
    signupForm.style.display = 'none';
    loginForm.style.display = 'block';

    setTimeout(() => {
        signupForm.style.opacity = 0;
        loginForm.style.opacity = 1;
    }, 10);
});

signupLink.addEventListener('click', (event) => {
    event.preventDefault();
    loginForm.style.display = 'none';
    signupForm.style.display = 'block';

    setTimeout(() => {
        loginForm.style.opacity = 0;
        signupForm.style.opacity = 1;
    }, 10);
});


const new_username = document.getElementById('new_username');
const button = document.getElementById('submit');





button.addEventListener('click', function () {
    var uname = new_username.value;
    var special = ['!', '@', '#', '$'];

    if (uname.length > 5) {
        for (let a of special) {
            console.log(a)
            console.log(uname.split(""))

            if (uname.split("").includes(a)) {
                alert("Special characters present");

            }
        }

    }

});


