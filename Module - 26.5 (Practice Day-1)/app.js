const loadAllProducts = () => {
    fetch('https://fakestoreapi.com/products')
        .then(response => response.json())
        .then(data => displayAllProducts(data));
};


const displayAllProducts = (products) => {
    const parent = document.getElementById("all-products");
    parent.innerHTML = "";
    products.forEach(product => {
        const div = document.createElement("div");
        div.classList.add("col");
        div.innerHTML = `
            <div class="card h-100 p-5">
                    <img src=${product.image} class="card-img-top p-3" style="width: 100% !important; height: 300px !important;" alt="${product.title}">
                    <div class="card-body">
                        <h5 class="card-title">${product.title}</h5>
                        <p class="card-text">${product.price}</p>
                        <p class="card-text">${product.description.slice(0, 200)}</p>
                        <p class="card-text">${product.category}</p>
                        <a href="./product_details.html?Id=${product.id}" target="_blank" class="btn btn-info">Details</a>
                    </div>
                </div>
        `;
        parent.appendChild(div);
    });
};


const loadAllCatetories = () => {
    fetch('https://fakestoreapi.com/products/categories')
        .then(res => res.json())
        .then(json => displayAllCatetories(json));
}

const displayAllCatetories = (categories) => {
    const parent = document.getElementById("category-container");
    parent.innerHTML = "";

    categories.forEach(category => {
        const btn = document.createElement("button");
        btn.classList.add("btn", "btn-warning");
        btn.innerText = category;
        btn.onclick = () => specificCategoryProducts(category);

        parent.appendChild(btn);
    });
}

const specificCategoryProducts = (category) => {
    fetch(`https://fakestoreapi.com/products/category/${category}`)
        .then(res => res.json())
        .then(json => displayAllProducts(json));
};



loadAllProducts();
loadAllCatetories();