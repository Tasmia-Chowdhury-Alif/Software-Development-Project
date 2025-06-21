const loadServices = () => {
    fetch("https://testing-8az5.onrender.com/services/")
        .then((response) => response.json())
        .then((data) => displayServices(data))
        .catch((err) => console.log(err))
};

const displayServices = (services) => {
    // console.log(services);
    const parent = document.getElementById("service-card-container");
    services.forEach(service => {
        const li = document.createElement("li");
        li.classList.add("slide-visible");
        li.innerHTML = `
            <div class="card shadow h-100">
                <div class="ratio ratio-16x9">
                    <img src=${service?.image} class="card-img-top" loading="lazy" alt="...">
                </div>
                <div class="card-body p-3 p-xl-5">
                    <h3 class="card-title h5">${service?.name}</h3>
                    <p class="card-text">${service?.description.slice(0, 120)}</p>
                    <div><a href="#" class="btn btn-primary">Details</a>
                    </div>
                </div>
            </div>
        `;
        parent.appendChild(li);
    });
};

// const loadDoctors = () => {
//     fetch("https://testing-8az5.onrender.com/doctor/list/")
//         .then(res => res.json())
//         .then(data => displayDoctors(data?.results))
//         .catch((err) => console.log(err))
// };


const loadDoctors = async (startUrl = "https://testing-8az5.onrender.com/doctor/list/") => {
    try {
        const doctors = [];
        let url = startUrl;

        // keep walking through paginated results
        while (url) {
            // Convert "http" to "https" to avoid mixed-content or insecure requests
            if (url.startsWith("http://")) {
                url = url.replace("http://", "https://");
            }

            const res = await fetch(url);
            if (!res.ok) throw new Error(`Request failed: ${res.status}`);

            const data = await res.json();
            doctors.push(...data.results);
            url = data.next;
        }

        displayDoctors(doctors);
    }
    catch (err) {
        console.error("Could not load doctors:", err);
    }
};

const displayDoctors = (doctors) => {
    const parent = document.getElementById("doctors");
    parent.innerHTML = "";
    doctors.forEach(doctor => {
        const div = document.createElement("div");
        div.classList.add("doc-card", "card", "rounded-5", "col-md-4");
        div.innerHTML = `
            <div class="card-body text-center py-5">
                <img src=${doctor?.image} alt="Doctor Profile" class="rounded-circle profile-img mb-3">
                <h3 class="doc-name card-title mb-2">${doctor?.full_name}</h3>
                <p class="doc-designation card-text text-muted mb-3 fw-bold"> 
                    ${doctor?.designation?.map((item) => {
                        return `<span>${item}</span>`
                    }).join('')}
                </p>
                <p class="doc-details card-text mb-4">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officia consequuntur alias mollitia repellat ipsa aperiam natus commodi neque amet eius?</p>
                ${doctor?.specialization?.map((item) => {
                    return `<button type="button" class="btn btn-sm mx-1 my-1" style="background-color: rgba(0, 126, 133, 1); color: white; border: none;">${item}</button>`
                }).join('')}
                <button class="btn d-block mx-auto " style="background-color: rgba(0, 126, 133, 1); border: none;"><a href="doctorDetails.html?doctorId=${doctor.id}" target="_blank" style="text-decoration: none; color: white;">Details</a></button>
            </div>
        `;
        parent.appendChild(div);
    });
};

const loadDesignation = () => {
    fetch("https://testing-8az5.onrender.com/doctor/designation/")
        .then((res) => res.json())
        .then((data) => {
            // console.log(data);
            data.forEach((item) => {
                parent = document.getElementById("dropdown-designation");
                const li = document.createElement("li");
                li.innerHTML = `
                <li class="dropdown-item" onclick="handleSearch('${item.name}')">${item?.name}</li>
                `;
                parent.appendChild(li);
            });
        });
};

const loadSpecialization = () => {
    fetch("https://testing-8az5.onrender.com/doctor/specialization/")
        .then((res) => res.json())
        .then((data) => {
            // console.log(data);
            data.forEach((item) => {
                parent = document.getElementById("dropdown-specialization");
                const li = document.createElement("li");
                li.innerHTML = `
                    <li class="dropdown-item" onclick="handleSearch(${item.name})">${item?.name}</li>
                `;
                parent.appendChild(li);
            });
        });
};

const callSearch = () => {
    const value = document.getElementById("search").value;
    handleSearch(value);
}

const handleSearch = (search) => {
    fetch(`https://testing-8az5.onrender.com/doctor/list/?search=${search ? search : ""}`)
        .then((res) => res.json())
        .then((data) => {
            const parent = document.getElementById("doctors");
            if (data.results.length > 0) {
                displayDoctors(data?.results);
            }
            else {
                parent.innerHTML = "";
                parent.innerHTML = `
                    <div id="nodata" class="w-50 mx-auto mb-auto">
                        <img src="./Images/nodata.png" alt="nodata">
                    </div>
                `;
            }
        })
        .catch((err) => console.log(err))
}


const loadReviews = () => {
    fetch("https://testing-8az5.onrender.com/doctor/review/")
        .then((res) => res.json())
        .then((data) => displayReviews(data))
        .catch((err) => console.log(err))
}

const displayReviews = (reviews) => {
    const parent = document.getElementById("review-container");

    reviews.forEach(review => {
        const li = document.createElement("li");
        li.classList.add("slide-visible", "review-card", "card", "shadow", "h-100");

        li.innerHTML = `
            <div class="review-card-body p-5 m-2">
                <div class="d-flex align-items-center gap-3 w-100 mx-auto">
                    <img src="./Images/girl.png" alt="" />
                    <div>
                        <h4>${review.reviewer}</h4>
                        <h6>${review.rating}</h6>
                    </div>
                </div>
                <p class="p-4">${review.body.slice(0, 100)}</p>
            </div>
        `
        parent.appendChild(li);
    });

};



loadServices();
loadDoctors();
loadDesignation();
loadSpecialization();
loadReviews();