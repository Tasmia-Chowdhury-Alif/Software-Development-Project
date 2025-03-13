const search_btn = document.getElementById("search-btn");

search_btn.addEventListener("click", () => {
    const search_box = document.getElementById("search-box");
    const search_value = search_box.value;
    search_box.value ="";
    console.log(search_value);
    show_search_reasult(search_value);
});

const show_search_reasult = (search_value) => {
    fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${search_value}`)
        .then(res => res.json())
        .then(data => {
            console.log(data)

            const card_container = document.getElementById("card-container");
            card_container.innerHTML = "";

            const meals = data.meals;
            if (!meals) {
                card_container.innerHTML = `
                <h1 class="text-white">Sorry!!! No Item Found</h1>
                `;
                return;
            }
            meals.forEach(element => {
                const div = document.createElement("div");
                div.classList.add("card");

                div.innerHTML = `
                <img class="card-img" src="${element.strMealThumb}" alt="">
                <h1 class="card-heading">${element.strMeal}</h1>
                `;

                div.addEventListener("click", () => {
                    const selected_card = document.getElementById("selected-card");
                    selected_card.innerHTML = "";

                    const div2 = document.createElement("div");
                    div2.classList.add("card");
                    div2.innerHTML = `
                    <img class="card-img" src="${element.strMealThumb}" alt="">
                    <h1 class="card-heading">${element.strMeal}</h1>
                    <ul id="ingredients">
                    </ul>
                    `;

                    selected_card.appendChild(div2);
                    const ingredients = document.getElementById("ingredients"); 
                    
                    let i = 1 ;
                    while(true){
                        if(element[`strIngredient${i}`] && element[`strIngredient${i}`].trim() !== ""){
                            const li = document.createElement("li");
                            li.innerText = element[`strIngredient${i}`] ;
                            ingredients.appendChild(li);
                            i++;
                        }
                        else{
                            break;
                        }
                    }
                })
                card_container.appendChild(div);

            });

        })
        .catch(err => console.log(err))
}