function appointment() {
    window.location.href = "/appointment/";
}

function redirectTo(role) {
    if (role === 'admin_login') {
        window.location.href = "/admin_login/";
    } else if (role === 'doctor_login') {
        window.location.href = "/doctor_login/";
    } else if (role === 'patient_login') {
        window.location.href = "/patient_login/";
    }
}
