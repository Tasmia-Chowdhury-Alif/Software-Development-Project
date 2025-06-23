const handelRegistration = (event) => {
    event.preventDefault();

    const username = getValue("username");
    const first_name = getValue("first_name");
    const last_name = getValue("last_name");
    const email = getValue("email");
    const password = getValue("password");
    const confirm_password = getValue("confirm_password");
    const info = {
        username,
        first_name,
        last_name,
        email,
        password,
        confirm_password,
    };

    if (password === confirm_password) {
        document.getElementById("error").innerHTML = "";

        if (/^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/.test(password)) {
            console.log(info);
            // fetch("https://testing-8az5.onrender.com/patient/register/", {
            //         method: "POST",
            //         headers: { "content-type": "application/json" },
            //         body: JSON.stringify(info),
            // })
            //     .then((res) => res.json())
            //     .then((data) => console.log(data));

            fetch("https://testing-8az5.onrender.com/patient/register/", {
                method: "POST",
                headers: { "content-type": "application/json" },
                body: JSON.stringify(info),
            })
                .then((res) => res.json())
                .then((data) => console.log(data))
                .catch((err) => console.log(err));
        }
        else {
            document.getElementById("error").innerHTML = `
                <li class="text-danger text-start ps-4" style="list-style: inside ;">Ateast 8 characters</li>
                <li class="text-danger text-start ps-4" style="list-style: inside ;">at least one uppercase letter</li>
                <li class="text-danger text-start ps-4" style="list-style: inside ;">at least one lowercase letter</li>
                <li class="text-danger text-start ps-4" style="list-style: inside ;">at least one number</li>
                <li class="text-danger text-start ps-4" style="list-style: inside ;">at least one special character</li>
            `;
        }

    }
    else {
        document.getElementById("error").innerHTML = `
            <li class="text-danger text-start ps-4 py-2" style="list-style: inside ;">Password doesn't match</li>
        `;
        alert("Password doesn't match");
    }
};


const handleLogin = (event) => {
    event.preventDefault();
    const username = getValue("login-username");
    const password = getValue("login-password");
    console.log(username, password);
    if ((username, password)) {
        fetch("https://testing-8az5.onrender.com/patient/login/", {
            method: "POST",
            headers: { "content-type": "application/json" },
            body: JSON.stringify({ username, password }),
        })
            .then((res) => res.json())
            .then((data) => {
                console.log(data);

                if (data.token && data.user_id) {
                    localStorage.setItem("token", data.token);
                    localStorage.setItem("user_id", data.user_id);
                    window.location.href = "index.html";
                }
            })
            .catch((err) => console.log(err));
    }
};



const getValue = (id) => document.getElementById(id).value;



