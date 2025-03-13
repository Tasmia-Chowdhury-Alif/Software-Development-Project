const search_btn = document.getElementById("search-btn");
search_btn.addEventListener("click", () => {
    const search_box = document.getElementById("search-box");
    const search_value = search_box.value;
    search_box.value = "";
    search_result(search_value);
})



const search_result = (search_value) => {
    fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${search_value}`)
        .then(res => res.json())
        .then(data => {
            console.log(data);
            load_products(data.meals);
        })
        .catch(err => console.log(err))
}



const load_products = (products) => {
    const product_container = document.getElementById("product-container");
    product_container.innerHTML = "";

    if (!products) {
        product_container.innerHTML = `<h1 class="text-white">Sorry!!! No Item Found</h1>`;
        return;
    }

    products.forEach(product => {
        const div = document.createElement("div");
        div.classList.add("card");

        const modal_id = `modal-${product.idMeal}`;
        const title_id = `title-${product.idMeal}`;
        // console.log(modal_id);

        div.innerHTML = `
            <img class="card-img" src="${product.strMealThumb}" alt="" />
            <h1 class="card-heading">${product.strMeal}</h1>
            <p>Meal id: ${product.idMeal}</p>
            <p>Category: ${product.strCategory}</p>
            <p>Area: ${product.strArea}</p>
            <div class="icon-container">
                <a class="icon" href="${product.strYoutube}" target="_blank"><i class="fa-brands fa-youtube text-danger"></i></a>
                <a class="icon" href="https://www.facebook.com/" target="_blank"><i class="fa-brands fa-square-facebook text-primary"></i></a>
                <a class="icon" href="https://www.facebook.com/" target="_blank"><i class="fa-brands fa-square-x-twitter text-dark"></i></a>
            </div>
            <div class="d-flex justify-content-between">
            <button class="add-to-cart-btn cart-btn" onclick="addToCart(${product.idMeal})" >Add To Cart</button>
            <button class="details-btn cart-btn bg-info text-dark" onclick="showDetails(${product.idMeal})" data-bs-toggle="modal"  data-bs-target="#detailsModal">Details</button>
            </div>


        `;
        product_container.appendChild(div);
    });
}

function addToCart(id) {
    fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`)
        .then(res => res.json())
        .then(data => {
            product = data.meals[0];
            console.log(data);
            const cart_main_container = document.getElementById("cart-main-container");

            let selectedCount = parseInt(document.getElementById("selected-item").innerText);

            if (selectedCount == 11) {
                alert("Cannot select more than 11 item");
                return;
            }

            document.getElementById("selected-item").innerText = selectedCount + 1;
            console.log(selectedCount)

            let totalPrice = parseFloat(document.getElementById("total").innerText);
            document.getElementById("total").innerText = totalPrice + parseFloat(product.idMeal);

            const h3 = document.createElement("h3");
            h3.innerText = product.strMeal;
            cart_main_container.appendChild(h3);


        })
        .catch(err => console.log(err))
}
// Show details in modal
function showDetails(id) {
    fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`)
        .then(res => res.json())
        .then(data => {
            const meal = data.meals[0];

            document.getElementById("detailsModalLabel").innerText= `${meal.strMeal} Details`

            const modalBody = document.getElementById("modalBody");
            modalBody.innerHTML = `
                <p><strong>Category:</strong> ${meal.strCategory}</p>
                <p><strong>Area:</strong> ${meal.strArea}</p>
                <h3>Ingredients:</h3>
                <ul>${getIngredientsList(meal)}</ul>
                <h3>Instructions:</h3>
                <p>${meal.strInstructions}</p>
            `;
        })
        .catch(err => console.log(err));
}

// Generate ingredients list
function getIngredientsList(meal) {
    let ingredients = "";
    for (let i = 1; i <= 20; i++) {
        if (meal[`strIngredient${i}`]) {
            ingredients += `<li><strong>${meal[`strIngredient${i}`]} -</strong> <span class="badge bg-info rounded-pill">${meal[`strMeasure${i}`]}</span></li>`;
        } else {
            break;
        }
    }
    return ingredients;
}

// deafoult search to show some products
search_result("k");



















































