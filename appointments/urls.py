from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.appointment_list,
        name="appointment_list"
    ),

    path(
        "book/",
        views.book_appointment,
        name="book_appointment"
    ),

    path(
        "cancel/<int:appointment_id>/",
        views.cancel_appointment,
        name="cancel_appointment"
    ),

    path(
        "confirm/<int:appointment_id>/",
        views.confirm_appointment,
        name="confirm_appointment"
    ),

]