from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Drug, Prescription

admin.site.register(Drug)
admin.site.register(Prescription)
