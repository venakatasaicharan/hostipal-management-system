document.addEventListener('DOMContentLoaded', function() {
    var successMessage = document.getElementById('successMessage');

    if (successMessage) {
        if (confirm("Appointment successfully created. Do you want to go back?")) {
            window.location.href = document.getElementById('homeButton').dataset.homeUrl;
        } else {
            pass
        }
    }

    var backButton = document.getElementById('backButton');
    var homeButton = document.getElementById('homeButton');

    if (backButton) {
        backButton.addEventListener('click', function() {
            window.history.back();
        });
    }

    if (homeButton) {
        homeButton.addEventListener('click', function() {
            window.location.href = homeButton.dataset.homeUrl;
        });
    }
});
