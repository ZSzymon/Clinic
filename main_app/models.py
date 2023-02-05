from django.db import models
from django.utils import timezone
from django.urls import reverse
#from django.contrib.auth.models import User, AbstractUser
import random
from dataclasses import dataclass
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from account.models import Account

User = get_user_model()

class DoctorManager(models.Manager):
   def get_queryset(self, *args, **kwargs):
       return super().get_queryset(*args, **kwargs).filter(type=User.Types.DOCTOR)


class PatientManager(models.Manager):
   def get_queryset(self, *args, **kwargs):
       return super().get_queryset(*args, **kwargs).filter(type=User.Types.PATIENT)


class Doctor(Account):
    objects = DoctorManager()
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Types.DOCTOR
        return super().save(*args, **kwargs)


class Patient(User):
    objects = PatientManager()

    class Meta:
        proxy = True

    def save(self,*args,**kwargs):
        if not self.pk:
            self.type = User.Types.PATIENT
        return super().save(*args, **kwargs)


class Appointment(models.Model):
    appointment_start_time = models.DateTimeField(_("Appointment start:"),default=timezone.now)
    appointment_end_time = models.DateTimeField(_("End time"),default=timezone.now)
    doctor = models.ForeignKey(Doctor, related_name=_('DoctorName'), on_delete=models.CASCADE, null=True, blank=False)
    patient = models.ForeignKey(Patient, related_name=_('PatientName'),  on_delete=models.CASCADE, null=True, blank= False)

    def __str__(self):
        return '{} -> {} on {} '.format(self.doctor, self.patient, self.appointment_start_time)

class Article(models.Model):
    pub_date = models.DateField(auto_now_add=True)
    headline = models.CharField(max_length=512)
    content = models.TextField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.headline}  --> {self.author}'
