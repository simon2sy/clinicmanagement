from django.db import models

from patients.models import PatientProfile
from doctors.models import DoctorProfile
from appointments.models import Appointment


class MedicalRecord(models.Model):

    patient = models.ForeignKey(
        PatientProfile,
        on_delete=models.PROTECT,
        related_name="medical_records",
    )

    doctor = models.ForeignKey(
        DoctorProfile,
        on_delete=models.PROTECT,
        related_name="medical_records",
    )

    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.PROTECT,
        related_name="medical_record",
        null=True,
        blank=True,
    )

    visit_date = models.DateField()

    chief_complaint = models.TextField(blank=True)

    symptoms = models.TextField(blank=True)

    diagnosis = models.TextField(blank=True)

    treatment = models.TextField(blank=True)

    notes = models.TextField(blank=True)

    follow_up_date = models.DateField(
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-visit_date", "-created_at"]

    def __str__(self):
        return f"{self.patient} - {self.visit_date}"


class Prescription(models.Model):

    medical_record = models.ForeignKey(
        MedicalRecord,
        on_delete=models.CASCADE,
        related_name="prescriptions",
    )

    instructions = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription #{self.pk}"


class PrescriptionItem(models.Model):

    prescription = models.ForeignKey(
        Prescription,
        on_delete=models.CASCADE,
        related_name="items",
    )

    medicine_name = models.CharField(max_length=255)

    dosage = models.CharField(
        max_length=100,
        help_text="Example: 500 mg",
    )

    frequency = models.CharField(
        max_length=100,
        help_text="Example: Twice daily",
    )

    duration = models.CharField(
        max_length=100,
        help_text="Example: 7 days",
    )

    route = models.CharField(
        max_length=50,
        blank=True,
        help_text="Example: Oral",
    )

    instructions = models.TextField(blank=True)

    def __str__(self):
        return self.medicine_name


class MedicalDocument(models.Model):

    medical_record = models.ForeignKey(
        MedicalRecord,
        on_delete=models.CASCADE,
        related_name="documents",
    )

    title = models.CharField(max_length=255)

    file = models.FileField(
        upload_to="medical_documents/%Y/%m/",
    )

    document_type = models.CharField(
        max_length=100,
        blank=True,
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title