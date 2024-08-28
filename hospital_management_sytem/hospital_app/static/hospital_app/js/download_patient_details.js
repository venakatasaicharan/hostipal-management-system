document.addEventListener("DOMContentLoaded", function() {
    const { jsPDF } = window.jspdf;

    document.getElementById("downloadBtn").addEventListener("click", function() {
        const doc = new jsPDF();
        const patientDetails = [
            ["Patient ID", document.getElementById("patient_id").innerText],
            ["First Name", document.getElementById("first_name").innerText],
            ["Last Name", document.getElementById("last_name").innerText],
            ["Date of Birth", document.getElementById("date_of_birth").innerText],
            ["Mobile Number", document.getElementById("mobile_number").innerText],
            ["Email", document.getElementById("email").innerText],
            ["Disease", document.getElementById("disease").innerText],
            ["Bill", document.getElementById("bill").innerText]
        ];

        doc.autoTable({
            head: [['Field', 'Value']],
            body: patientDetails,
        });
        doc.save("patient_details.pdf");
    });
});
