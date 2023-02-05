from django import forms
from django.forms import ModelForm

from pharmacy.models import *


class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ("name", "price")


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = (
            "doctor",
            "patient",
            "drug",
            "quantity",
        )
