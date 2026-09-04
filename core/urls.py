from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("doctors/", views.doctors, name="doctors"),

    path("patients/", views.patients, name="patients"),

    path("patients/add/", views.add_patient, name="add_patient"),

]