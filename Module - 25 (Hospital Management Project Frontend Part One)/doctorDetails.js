const getparams = () => {
    const param = new URLSearchParams(window.location.search).get("doctorId");
    fetch(`https://testing-8az5.onrender.com/doctor/list/${param}/`)
    .then(res => res.json())
    .then(data => displayDetails(data))
    .catch(err => console.log(err))
    
    fetch(`https://testing-8az5.onrender.com/doctor/review/?doctor_id=${param}`)
    .then(res => res.json())
    .then(data => displayDoctorReviews(data))
    .catch(err => console.log(err))

    loadTime(param);
};


const displayDetails = (doctor) => {
    const parent = document.getElementById("doctor-details");
    const div = document.createElement("div");
    
    div.innerHTML = `
        <div class="card mb-3 rounded-5 mx-auto" style="max-width: 75%;">
            <div class="row g-0 p-5 ms-md-5">
                <div class="col-md-4">
                    <img class="doctor-details-img img-fluid" src=${doctor.image} alt="doctor's image">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h1 class="card-title">${doctor.full_name}</h1>
                        <h5 class="card-text doc-designation card-text text-muted mb-3 fw-bold">
                            ${doctor?.designation?.map((item) => {
                                return `<span>${item}</span>`
                            }).join('')}
                        </h5>
                        <h6 ><b>Specializations :</b>
                            ${doctor?.specialization?.map((item) => {
                                return `${item}`
                            }).join(', ')}
                        </h6>
                        <p class="card-text w-50 py-3">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Officia consequuntur alias mollitia repellat ipsa aperiam natus commodi neque amet eius?</p>
                        <h5 class="card-text w-50"><b>Available Time : </b> ${doctor?.available_time?.map((item) => {
                                                return `<span class="fw-normal">${item}</span>`
                                            }).join(', ')}
                        </h5>
                        <button type="button" class="btn d-block rounded-4 my-4" style="color: white; background-color: rgba(0, 126, 133, 1); " data-bs-toggle="modal" data-bs-target="#exampleModal" >Take Appointment</button>
                    </div>
                </div>
            </div>

            <h1 class="text-center my-4" style="font-family: DM Sans;">RATINGS FROM PATIENTS</h1>

            <div id="doctor-review-container" class="row justify-content-around m-5 pb-5">
            </div>
        </div>
    `;
    parent.appendChild(div);
};


const displayDoctorReviews = (reviews) => {
    const parent = document.getElementById("doctor-review-container");

    reviews.forEach(review => {
        const div = document.createElement("div");
        div.classList.add("review-card", "card", "col-md-6");
        div.style.width = "40%" ;

        div.innerHTML = `
            <div class="p-5">
                <div class="d-flex align-items-center gap-3 w-100 mx-auto">
                    <img src="./Images/girl.png" alt="" />
                    <div>
                        <h4>${review.reviewer}</h4>
                        <h6>${review.rating}</h6>
                    </div>
                </div>
                <p class="p-4">${review.body.slice(0, 100)}</p>
            </div>
        `;
        parent.appendChild(div);
    });

};


const loadTime = (id) => {
    fetch(`https://testing-8az5.onrender.com/doctor/availabletime/?doctor_id=${id}`)
    .then(res => res.json())
    .then(data => {
        data.forEach(item => {
            const parent = document.getElementById("time-container");
            const option = document.createElement("option");
            option.value = item.id ;
            option.innerText = item.name ;
            parent.appendChild(option);
        });
    })
    .catch(err => console.log(err))
};

const handleAppointment = () => {
    const param = new URLSearchParams(window.location.search).get("doctorId");

    const status = document.getElementsByName("status");
    const selected = Array.from(status).find((button) => button.checked);

    const symptom = document.getElementById("symptom").value ;

    const time = document.getElementById("time-container");
    const selectedTime = time.options[time.selectedIndex];
    console.log(selected.value, symptom, selectedTime.value);

    const info = {
        "appointment_type": selected.value,
        "appointment_status":"Pending",
        "time": selectedTime.value,
        "symptom": symptom,
        "cancel": false,
        "patient": 1,
        "doctor": param,
    };
    console.log(info);

    fetch("https://testing-8az5.onrender.com/appointment/", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(info),
    })
    .then((res) => res.json())
    .then((data) => {
        console.log(data);
    });

};



getparams();