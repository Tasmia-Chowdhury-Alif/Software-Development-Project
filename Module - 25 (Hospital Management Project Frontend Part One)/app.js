const loadServices = () => {
    fetch("https://testing-8az5.onrender.com/service")
        .then((response) => response.json())
        .then((data) => displayServices(data))
        .catch((err) => console.log(err))
};

const displayServices = (services) => {
    console.log(services);
    const parent = document.getElementById("service-card-container");
    services.forEach(service => {
        const li = document.createElement("li");
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
        `
        li.classList.add("slide-visible")
        parent.appendChild(li)
    });
};

// const loadDoctors = () => {
//     fetch("https://testing-8az5.onrender.com/doctor/list/")
//         .then(res => res.json())
//         .then(data => displayDoctors(data?.results))
//         .then((err) => console.log(err))
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

        displayDoctors(doctors);           // render once, after everything is in
    }
    catch (err) {
        console.error("Could not load doctors:", err);
    }
};

const displayDoctors = (doctors) => {
    const parent = document.getElementById("doctors");
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
                <p class="doc-details card-text mb-4">Passionate about creating beautiful and functional websites. Always learning and exploring new technologies.</p>
                ${doctor?.specialization?.map((item) => {
                    return `<button type="button" class="btn btn-info btn-sm mx-1 my-1" style="background-color: rgba(0, 126, 133, 1); color: white; border: none;">${item}</button>`
                }).join('')}
            </div>
        `
        parent.appendChild(div);
    });
};

const loadDesignation = () => {
    fetch("https://testing-8az5.onrender.com/doctor/designation/")
    .then((res) => res.json())
    .then((data) => {
        console.log(data);
        data.forEach((item) => {
            parent = document.getElementById("dropdown-designation")
            const li = document.createElement("li");
            li.innerHTML = `
                <a class="dropdown-item" href="">${item?.name}</a>
            `
            parent.appendChild(li);
        });
    });
};

const loadSpecialization = () => {
    fetch("https://testing-8az5.onrender.com/doctor/specialization/")
    .then((res) => res.json())
    .then((data) => {
        console.log(data);
        data.forEach((item) => {
            parent = document.getElementById("dropdown-specialization")
            const li = document.createElement("li");
            li.innerHTML = `
                <a class="dropdown-item" href="">${item?.name}</a>
            `
            parent.appendChild(li);
        });
    });
};

const handleSearch = () => {
    const search = document.getElementById("search").value ;
    fetch(`https://testing-8az5.onrender.com/doctor/list/?search=${
        search ? search : ""}`)
        .then((res) => res.json())
        .then((data) => {
            const parent = document.getElementById("doctors");
            parent.innerHTML = ``
            displayDoctors(data?.results);
        })
        .then((err) => console.log(err))

}



loadServices();
loadDoctors();
loadDesignation();
loadSpecialization();