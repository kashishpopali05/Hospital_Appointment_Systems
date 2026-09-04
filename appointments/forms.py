from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            "doctor",
            "patient",
            "appointment_date",
            "appointment_time",
            "reason",
        ]

        widgets = {

            "appointment_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-input",
                }
            ),

            "appointment_time": forms.TimeInput(
                attrs={
                    "type": "time",
                    "class": "form-input",
                }
            ),

            "reason": forms.Textarea(
                attrs={
                    "class": "form-input",
                    "rows": 4,
                    "placeholder": "Reason for appointment",
                }
            ),
        }

        