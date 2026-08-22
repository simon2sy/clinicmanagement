from django.contrib import admin

from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        "appointment",
        "amount",
        "method",
        "status",
        "transaction_id",
        "paid_at",
        "created_at",
    )

    list_filter = (
        "status",
        "method",
        "paid_at",
    )

    search_fields = (
        "transaction_id",
        "appointment__patient__patient_id",
        "appointment__patient__user__first_name",
        "appointment__patient__user__last_name",
        "appointment__doctor__user__first_name",
        "appointment__doctor__user__last_name",
    )

    readonly_fields = (
        "created_at",
    )

    list_select_related = (
        "appointment",
        "appointment__patient",
        "appointment__doctor",
    )