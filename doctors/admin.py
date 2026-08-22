from django.contrib import admin

from .models import (
    Specialization,
    DoctorProfile,
    DoctorSchedule,
)


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )

    search_fields = (
        "name",
    )


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "specialization",
        "license_number",
        "experience_years",
        "consultation_fee",
        "is_available",
    )

    list_filter = (
        "specialization",
        "is_available",
    )

    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "license_number",
        "qualification",
    )

    list_select_related = (
        "user",
        "specialization",
    )


@admin.register(DoctorSchedule)
class DoctorScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "doctor",
        "weekday",
        "start_time",
        "end_time",
        "slot_duration",
        "is_active",
    )

    list_filter = (
        "weekday",
        "is_active",
    )

    search_fields = (
        "doctor__user__first_name",
        "doctor__user__last_name",
        "doctor__license_number",
    )

    list_select_related = (
        "doctor",
        "doctor__user",
    )