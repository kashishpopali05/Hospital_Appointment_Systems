document.addEventListener("DOMContentLoaded", function () {

    const buttons = document.querySelectorAll(".action-cancel");

    buttons.forEach(function (button) {

        button.addEventListener("click", function (event) {

            const confirmed = confirm(
                "Are you sure you want to cancel this appointment?"
            );

            if (!confirmed) {
                event.preventDefault();
            }

        });

    });


    const appointmentDate =
        document.querySelector('input[type="date"]');

    if (appointmentDate) {

        const today =
            new Date().toISOString().split("T")[0];

        appointmentDate.setAttribute(
            "min",
            today
        );

    }

});