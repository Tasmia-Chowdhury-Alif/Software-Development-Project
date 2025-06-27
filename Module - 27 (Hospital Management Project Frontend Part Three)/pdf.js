const handlePdf = () => {
    const doctor_id = new URLSearchParams(window.location.search).get("doctorId");
    console.log(doctor_id);
    const user_id = localStorage.getItem("user_id");
    console.log(`https://testing-8az5.onrender.com/users/${user_id}`);
    fetch(`https://testing-8az5.onrender.com/doctor/list/${doctor_id}`)
        .then((res) => res.json())
        .then((data) => {
            fetch(`https://testing-8az5.onrender.com/users/${user_id}`)
                .then((res) => res.json())
                .then((user_data) => {
                    const newData = [data, user_data];
                    const doctor = newData[0];
                    const user = newData[1];
                    console.log(doctor);
                    console.log(user);
                    const parent = document.getElementById("pdf-container");
                    const div = document.createElement("div");
                    // div.innerHTML = `
                    //     <div class="pd d-flex justify-content-around align-items-center p-5">
                        //     <div class="patient doctor p-5">
                
                        //         <h1>${newData[1].username}</h1>
                        //         <h1>${newData[1].first_name} ${newData[1].last_name}</h1>
                        //         <h4>${newData[1].email}</h4>
                            
                        //     </div>
                        //     <div class="doctor p-5">
                        //     <img class="w-25" src=${newData[0].image}/>
                        //         <h2 class="doc-name">${newData[0].full_name}</h2>
                        //         <h3>designation: designation</h3>
                        //         <h5>specialization: specialization</h5>
                        //     </div>
                    //     </div>
                    //     <input id="pdf-symtom" class="symtom" type="text" />
                    //     <h1 id="pdf-fees" class="text-center p-2 mt-3">Fees: ${newData[0].fee}BDT</h1>
                    // `;
                    div.innerHTML = `
                        <div class="row text-start">
                            <div class="col-md-6 mb-4">
                                <h3 class="highlight">Patient Information</h3>
                                <p><strong>Name:</strong> ${user.first_name} ${user.last_name}</p>
                                <p><strong>Username:</strong> ${user.username}</p>
                                <p><strong>Email:</strong> ${user.email}</p>
                            </div>
                            <div class="col-md-6 mb-4 text-center">
                                <h3 class="highlight">Doctor Details</h3>
                                <img src="${doctor.image}" class="doctor-img mb-2" />
                                <p><strong>Name:</strong> ${doctor.full_name}</p>
                                <p><strong>Designation:</strong> ${doctor.designation?.join(', ')}</p>
                                <p><strong>Specialization:</strong> ${doctor.specialization?.join(', ')}</p>
                            </div>
                        </div>
                        <div class="mt-3">
                            <p><strong class="highlight">Appointment Fee:</strong> ${doctor.fee} BDT</p>
                            <p><strong class="highlight">Symptoms:</strong> [Your input or description]</p>
                        </div>
                    `;

                    parent.appendChild(div);
                    donwloadPdf();
                });

        });
};

const donwloadPdf = () => {
    const element = document.getElementById("pdf-container");

    // Define the options for html2pdf
    const options = {
        margin: 10,
        filename: "appointment.pdf",
        image: { type: "jpg", quality: 0.98 },
        html2canvas: { scale: 2 },
        jsPDF: { unit: "mm", format: "a4", orientation: "portrait" },
    };

    // Use html2pdf to generate and download the PDF
    html2pdf(element, options);

};
handlePdf();
