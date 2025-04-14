from django.db import models
from apps.users.models import User

class MedicalHistory(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medical_histories')
    condition = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    diagnosed_on = models.DateField()

    def __str__(self):
        return f"{self.patient.get_full_name()} - {self.condition}"


class Prescription(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='issued_prescriptions')
    medication = models.TextField()
    dosage = models.TextField()
    instructions = models.TextField(blank=True)
    prescribed_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient.get_full_name()} on {self.prescribed_on}"


class LabResult(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lab_results')
    test_name = models.CharField(max_length=255)
    result = models.TextField()
    normal_range = models.CharField(max_length=255, blank=True)
    conducted_on = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.test_name} for {self.patient.get_full_name()} on {self.conducted_on}"
