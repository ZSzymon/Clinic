
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import *
from .models import Patient, Appointment, Doctor,Article
from pharmacy.models import *

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Article)