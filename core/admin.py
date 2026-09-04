from django.contrib import admin
from .models import Department, Doctor, Patient


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "specialization",
        "department",
        "experience",
        "phone",
    )

    list_filter = ("department",)
    search_fields = ("name", "specialization")


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "age",
        "gender",
        "phone",
        "blood_group",
    )

    search_fields = ("name", "phone", "email")