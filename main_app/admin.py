from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import *
from pharmacy.models import *

from .models import Appointment, Article, Doctor, Patient

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Article)
