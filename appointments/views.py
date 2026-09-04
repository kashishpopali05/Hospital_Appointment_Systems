from django.shortcuts import render, redirect, get_object_or_404

from .models import Appointment
from .forms import AppointmentForm


def appointment_list(request):

    appointments = Appointment.objects.select_related(
        "doctor",
        "patient"
    ).order_by(
        "appointment_date",
        "appointment_time"
    )

    return render(
        request,
        "appointments.html",
        {
            "appointments": appointments,
        }
    )


def book_appointment(request):

    if request.method == "POST":

        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("appointment_list")

    else:
        form = AppointmentForm()

    return render(
        request,
        "book_appointment.html",
        {
            "form": form,
        }
    )


def cancel_appointment(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )

    appointment.status = "Cancelled"
    appointment.save()

    return redirect("appointment_list")


def confirm_appointment(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id
    )

    appointment.status = "Confirmed"
    appointment.save()

    return redirect("appointment_list")