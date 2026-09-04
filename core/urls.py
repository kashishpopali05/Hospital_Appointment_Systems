from django.urls import path
from . import views

urlpatterns = [

    # Home page
    path("", views.home, name="home"),

    # Dashboard
    path("dashboard/", views.dashboard, name="dashboard"),

    # Doctors
    path("doctors/", views.doctors, name="doctors"),

    # Patients
    path("patients/", views.patients, name="patients"),

    # Add patient
    path("patients/add/", views.add_patient, name="add_patient"),

    # Book appointment
    path(
        "book-appointment/",
        views.book_appointment,
        name="book_appointment"
    ),
]