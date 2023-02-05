# -*- coding: utf-8 -*-
import os
import sys

import pytz
from django.utils import timezone

PROJECT_NAME = "Clinic"
PROJECT_PATH = "/Clinic"
sys.path.append(PROJECT_PATH)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "%s.settings" % PROJECT_NAME)

import django

django.setup()

from datetime import datetime

from django.utils.datetime_safe import datetime
from django.utils.timezone import now
from pytz import UTC

from main_app.models import Appointment, Doctor, Patient


def insert_doctors():
    Doctor.objects.all().delete()
    d = Doctor.objects.create(
        first_name="Tomasz",
        second_name="",
        email="tomasz_mikulski@gmail.com",
        pesel=78041202444,
        data_of_birth=datetime(1978, 4, 12, tzinfo=UTC),
        register_date=now(),
        person_info=None,
        position_id=0,
    )
    d.save()
    # d = Doctor.objects.create(
    #     first_name="Jaroslaw",
    #     second_name="Krzywanski",
    #     email="jaroslaw_krzywanski@gmail.com",
    #     pesel=56041202444,
    #     data_of_birth=datetime(1978, 4, 12, tzinfo=UTC),
    #     register_date=now(),
    #     person_info=None,
    #     position_id=0,
    # )
    # d.save()


def insert_petients():
    Patient.objects.all().delete()
    p = Patient.objects.create(
        first_name="Szymon",
        second_name="Zywko",
        email="szymonzywko@gmail.com",
        pesel=99041202444,
        data_of_birth=datetime(1978, 4, 12, tzinfo=UTC),
        register_date=now(),
        person_info=None,
        position_id=0,
    )
    p.save()
    p = Patient.objects.create(
        first_name="Jan",
        second_name="Kowalski",
        email="jankowalski@gmail.com",
        pesel=99021201567,
        data_of_birth=datetime(1999, 2, 12, tzinfo=UTC),
        register_date=now(),
        person_info=None,
        position_id=0,
    )
    p.save()
    p = Patient.objects.create(
        first_name="Dariusz",
        second_name="Nowak",
        email="dariusznowak@gmail.com",
        pesel=90012205787,
        data_of_birth=datetime(1990, 1, 12, tzinfo=UTC),
        register_date=now(),
        person_info=None,
        position_id=0,
    )
    p.save()


def insert_appointements():
    Appointment.objects.all().delete()
    for doctor in Doctor.objects.all():
        for patient in Patient.objects.all():
            a = Appointment.objects.create(doctor=doctor, patient=patient)
            a.save()


if __name__ == "__main__":

    DEBUG = True
    # insert_petients()
    insert_doctors()
    # insert_appointements()
