const getparams = () => {
    const param = new URLSearchParams(window.location.search).get("Id");
    console.log(param);
    fetch(`https://fakestoreapi.com/products/${param}`)
        .then(response => response.json())
        .then(data => loadSingleProduct(data));
};

const loadSingleProduct = (product) => {
    const parent = document.getElementById("product-details");
    parent.innerHTML = "";

    const div = document.createElement("div");
    div.className = "row g-0" ;
    div.innerHTML = `
        <div class="col-md-4">
            <img src="${product.image}" class="img-fluid rounded-start p-5" alt="${product.title}">
        </div>
        <div class="col-md-8 p-5">
            <div class="card-body">
                <h1 class="card-title">${product.title}</h1>
                <p class="card-text py-3">${product.description}</p>
                <p class="card-text fs-5">Category : ${product.category}</p>
                <p class="card-text fs-5">Price : ${product.price} BDT</p>
            </div>
        </div>
    `;
    parent.appendChild(div);
};


getparams();