from django.contrib import admin

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "appointment_date",
        "start_time",
        "end_time",
        "patient",
        "doctor",
        "appointment_type",
        "status",
    )

    list_filter = (
        "status",
        "appointment_type",
        "appointment_date",
    )

    search_fields = (
        "patient__patient_id",
        "patient__user__first_name",
        "patient__user__last_name",
        "doctor__user__first_name",
        "doctor__user__last_name",
    )

    date_hierarchy = "appointment_date"

    ordering = (
        "appointment_date",
        "start_time",
    )

    list_select_related = (
        "patient",
        "patient__user",
        "doctor",
        "doctor__user",
    )