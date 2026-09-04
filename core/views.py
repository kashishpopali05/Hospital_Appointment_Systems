from django.shortcuts import render, redirect, get_object_or_404

from .models import Department, Doctor, Patient
from appointments.models import Appointment


def home(request):
    departments = Department.objects.all()[:4]
    doctors = Doctor.objects.all()[:4]

    return render(
        request,
        "home.html",
        {
            "departments": departments,
            "doctors": doctors,
        }
    )


def doctors(request):
    doctor_list = Doctor.objects.select_related("department").all()

    return render(
        request,
        "doctors.html",
        {
            "doctors": doctor_list,
        }
    )


def patients(request):
    patient_list = Patient.objects.all().order_by("-created_at")

    return render(
        request,
        "patients.html",
        {
            "patients": patient_list,
        }
    )


def add_patient(request):

    if request.method == "POST":

        Patient.objects.create(
            name=request.POST.get("name"),
            age=request.POST.get("age"),
            gender=request.POST.get("gender"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            address=request.POST.get("address"),
            blood_group=request.POST.get("blood_group"),
        )

        return redirect("patients")

    return render(request, "add_patient.html")


def dashboard(request):

    total_doctors = Doctor.objects.count()
    total_patients = Patient.objects.count()
    total_departments = Department.objects.count()
    total_appointments = Appointment.objects.count()

    upcoming = Appointment.objects.select_related(
        "doctor",
        "patient"
    ).order_by("appointment_date", "appointment_time")[:5]

    return render(
        request,
        "dashboard.html",
        {
            "total_doctors": total_doctors,
            "total_patients": total_patients,
            "total_departments": total_departments,
            "total_appointments": total_appointments,
            "upcoming": upcoming,
        }
    )