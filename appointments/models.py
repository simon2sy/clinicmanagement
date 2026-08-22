from django.db import models
from django.core.exceptions import ValidationError

from doctors.models import DoctorProfile
from patients.models import PatientProfile


class Appointment(models.Model):

    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        CONFIRMED = "CONFIRMED", "Confirmed"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"
        NO_SHOW = "NO_SHOW", "No Show"

    class Type(models.TextChoices):
        IN_PERSON = "IN_PERSON", "In Person"
        ONLINE = "ONLINE", "Online"

    patient = models.ForeignKey(
        PatientProfile,
        on_delete=models.PROTECT,
        related_name="appointments",
    )

    doctor = models.ForeignKey(
        DoctorProfile,
        on_delete=models.PROTECT,
        related_name="appointments",
    )

    appointment_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    appointment_type = models.CharField(
        max_length=20,
        choices=Type.choices,
        default=Type.IN_PERSON,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    reason = models.TextField(blank=True)

    doctor_notes = models.TextField(blank=True)

    cancellation_reason = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["appointment_date", "start_time"]

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError(
                "End time must be after start time."
            )

    def __str__(self):
        return (
            f"{self.patient} - "
            f"{self.doctor} - "
            f"{self.appointment_date}"
        )