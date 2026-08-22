from django.contrib import admin

from .models import PatientProfile


@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = (
        "patient_id",
        "user",
        "gender",
        "blood_group",
        "emergency_contact_name",
        "emergency_contact_phone",
    )

    list_filter = (
        "gender",
        "blood_group",
    )

    search_fields = (
        "patient_id",
        "user__username",
        "user__first_name",
        "user__last_name",
        "user__email",
        "user__phone",
    )

    list_select_related = (
        "user",
    )