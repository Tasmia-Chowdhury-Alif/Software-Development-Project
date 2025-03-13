// const target = document.getElementsByTagName("h1")[0];

// target.style.color = "red"; 

// const allbox = document.getElementsByClassName("box");

// console.log(allbox);

// for (let i = 0; i < allbox.length; i++) {
//     const element = allbox[i];



//     if(element.innerText == "Box - 6"){
//         element.style.backgroundColor = "red";
//     }
//     else{
//         element.style.backgroundColor = "green";
//     }
// }

document.getElementById("handle-click").addEventListener("click", (event) => {
    const inputVal = document.getElementById("search-box").value;

    const cmt_container = document.getElementById("comment-container");

    const p = document.createElement("p");
    p.classList.add("child");

    p.innerText = inputVal;
    cmt_container.appendChild(p);

    document.getElementById("search-box").value = "";

    const allComments = document.getElementsByClassName("child");

    for (const element of allComments) {
        element.addEventListener("click", (event) => {
            event.target.parentNode.removeChild(element);
        })
    }

});


fetch("https://jsonplaceholder.typicode.com/users")
    .then(res => res.json())
    .then(data => {
        console.log(data)
        displaydata(data)
    })
    .catch(error => console.log(error))


const displaydata = (userdata) => {
    const container = document.getElementById("userdata-container");

    userdata.forEach(element => {
        const div = document.createElement("div");
        div.classList.add("user");
        div.innerHTML = `
        <h4>Title</h4>
        <p>Description</p>
        <button>Details</button>
        `;

        container.appendChild(div)
    });
}





























// fetch("https://jsonplaceholder.typicode.com/users")
//     .then(res => res.json())
//     .then(data => {
//         displaydata(data);
//     })
//     .catch(err => console.log(err));


// const displaydata = (data) => {
//     const container = document.getElementById("userdata-container");

//     data.forEach(element => {
//         const div = document.createElement("div");
//         div.classList.add("user");

//         div.innerHTML = `
//             <h4>Title</h4>
//             <p>Description</p>
//             <button>Details</button>
//         `

//         container.appendChild(div);
//     });
// }