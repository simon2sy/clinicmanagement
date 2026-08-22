from django.contrib import admin

from .models import (
    MedicalRecord,
    Prescription,
    PrescriptionItem,
    MedicalDocument,
)


class PrescriptionItemInline(admin.TabularInline):
    model = PrescriptionItem
    extra = 1


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = (
        "medical_record",
        "created_at",
    )

    search_fields = (
        "medical_record__patient__patient_id",
        "medical_record__patient__user__first_name",
        "medical_record__patient__user__last_name",
    )

    inlines = [
        PrescriptionItemInline,
    ]

    list_select_related = (
        "medical_record",
        "medical_record__patient",
    )


class MedicalDocumentInline(admin.TabularInline):
    model = MedicalDocument
    extra = 1


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = (
        "patient",
        "doctor",
        "appointment",
        "visit_date",
        "follow_up_date",
    )

    list_filter = (
        "visit_date",
        "follow_up_date",
    )

    search_fields = (
        "patient__patient_id",
        "patient__user__first_name",
        "patient__user__last_name",
        "doctor__user__first_name",
        "doctor__user__last_name",
        "diagnosis",
    )

    date_hierarchy = "visit_date"

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    list_select_related = (
        "patient",
        "patient__user",
        "doctor",
        "doctor__user",
        "appointment",
    )

    inlines = [
        MedicalDocumentInline,
    ]


@admin.register(MedicalDocument)
class MedicalDocumentAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "medical_record",
        "document_type",
        "uploaded_at",
    )

    list_filter = (
        "document_type",
        "uploaded_at",
    )

    search_fields = (
        "title",
        "document_type",
        "medical_record__patient__patient_id",
    )

    readonly_fields = (
        "uploaded_at",
    )