from random import randint

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from account.models import Account


class Drug(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=128,
        null=True,
        blank=False,
        unique=True,
        error_messages={"required": "Your Name is Required"},
    )
    price = models.FloatField(_("Price"), null=True, blank=True, default=55)
    image = models.ImageField(upload_to="products/", default="drugs/d1.jpg")

    def __str__(self):
        return "%s %s$" % (self.name, self.price)


class Prescription(models.Model):
    doctor = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name=_("Doctor"),
        limit_choices_to={"type": Account.Types.DOCTOR},
    )
    patient = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name=_("Patient"),
        limit_choices_to={"type": Account.Types.PATIENT},
    )
    drug = models.ForeignKey(
        Drug,
        on_delete=models.SET_NULL,
        related_name=_("Drug"),
        null=True,
        blank=False,
    )
    quantity = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} -> {} ".format(self.drug, self.patient)
