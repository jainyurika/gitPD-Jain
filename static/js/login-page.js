const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

var code = "";
function allowDrop(ev) {
    ev.preventDefault();
}
function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}
function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
    var res = document.getElementById(data).id;
    code = code.concat(res);
    if (code === "wasd") {
        document.getElementById("login-form-submit").className =
            document.getElementById("login-form-submit").className.replace
                (/(?:^|\s)disabled(?!\S)/g, '')
    }
}

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username !== null && password !== null) {
        
    } else {
        alert("Incorrect username or password");
    }
})

function showPosition() {
    result = document.getElementById("location");
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
        result.innerHTML = "Getting the position information...";
    } else {
        alert("Sorry, your browser does not support HTML5 geolocation.");
    }
};

function successCallback(position) {
    result.innerHTML = "Your current position is <br>" + "Latitude: " + position.coords.latitude + "<br>" + "Longitude: " + position.coords.longitude;
}

function errorCallback(position) {
    result.innerHTML = "You denied location permission request.";
}

const submitButton = document.getElementById("login-form-submit");
const registerForm = document.getElementById("register-form");
function hidingMyDiv() {
    var x = document.getElementById("new-div");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
submitButton.addEventListener("click", (e) => {
    const name = registerForm.fullname.value;
    e.preventDefault();
    console.log(name);
    document.getElementById("old-div").style.display = "none";
    document.getElementById("new-div").style.display = "grid";
    document.getElementById("new-div-content").innerHTML = "<h1>Hello " + name + ", your message has been sent.</h1><h2>Thank you for contacting us. We will get back to you soon.</h2>";
})