from django.db import models

from .disease import Disease
from .hospital import Hospital

patientStates = [("1", "Diagnosed"), ("2", "Hospitalized"), ("3", "Discharged")]
previousDiseases = [("1", "Respiratory"), ("2", "Heart"), ("3", "Inflammatory")]


class Patient(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    state = models.CharField(max_length=15, choices=patientStates, default="1")
    disease = models.OneToOneField(Disease, on_delete=models.SET_NULL, null=True, related_name="disease_of")
    previousDiseases = models.CharField(max_length=15, null=True, choices=previousDiseases)
    previousMedicine = models.TextField(null=True)
