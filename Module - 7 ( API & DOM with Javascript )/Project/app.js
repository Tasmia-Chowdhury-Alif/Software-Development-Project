const loadAllProducts = () => {
    fetch('https://fakestoreapi.com/products')
        .then(response => response.json())
        .then(data => {
            console.log(data)
            displayProducts(data)
        })
        .catch(err => console.log(err));

}

const displayProducts = (products) => {
    const productcontainer = document.getElementById("product-container")

    products.forEach(product => {
        const div = document.createElement("div");
        div.classList.add("product-card");

        div.innerHTML = `
        <img class="product-card-img" src="${product.image}" alt="" />
        <h3>${product.title.slice(0, 50)}</h3>
        <p>${product.description}</p>
        <button onclick="singleProduct('${product.id}')">Details</button>
        <button onclick="handleAddToCart('${product.title}', ${product.price}) ">Add to Cart</button>
        
        `;
        productcontainer.appendChild(div);
    });
}

const handleAddToCart = (title, price) => {

    let productCount = parseInt(document.getElementById("count").innerText);

    productCount += 1;
    document.getElementById("count").innerText = productCount
    console.log(productCount)



    console.log(title, price)

    const container = document.getElementById("cart-main-container")

    const div = document.createElement("div")
    div.classList.add("cart-info")

    div.innerHTML = `
    <p>${title.slice(0, 20)}</p> 
    <h3 class="price">${price}</h3>
    `;

    container.appendChild(div);
    updateTotal();
}

const updateTotal = () => {
    const allPrice = document.getElementsByClassName("price");

    let count = 0;
    for (const element of allPrice) {
        count = count + parseFloat(element.innerText)
    }

    document.getElementById("total").innerText = count.toFixed(2);
}

const singleProduct = (id) => {
    console.log(id)
    fetch(`https://fakestoreapi.com/products/${id}`)
        .then(response => response.json())
        .then(data => console.log(data));
}

loadAllProducts();











// const loadAllProducts = () => {
//     fetch('https://fakestoreapi.com/products')
//         .then(res => res.json())
//         .then(data => {
//             displayProducts(data);
//         })
// }

// const displayProducts = (products) => {
//     const productContainer = document.getElementById("product-container");

//     products.forEach(product => {
//         console.log(product);
//         const div = document.createElement("div");
//         div.classList.add("product-card");

//         div.innerHTML = `
//             <img class ="product-card-img" src= ${product.image} alt="">
//             <h4>${product.title}</h4>
//             <p>${product.description}</p>
//             <button class="details-btn">Details</button>
//             <button class="addToCart-btn">Add To Cart</button>
//         `;

//         productContainer.appendChild(div);
//     });
// }

// loadAllProducts();