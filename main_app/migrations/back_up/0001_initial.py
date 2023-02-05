# Generated by Django 3.1.4 on 2020-12-28 18:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=128)),
                ("second_name", models.CharField(max_length=128)),
                ("email", models.CharField(max_length=128)),
                ("pesel", models.IntegerField()),
                (
                    "data_of_birth",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("person_info", models.CharField(max_length=128)),
                (
                    "register_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
    ]
