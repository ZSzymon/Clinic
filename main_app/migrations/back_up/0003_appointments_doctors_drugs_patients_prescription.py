# Generated by Django 3.1.4 on 2020-12-28 19:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_app', '0002_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            bases=(models.Model, main_app.models.Person),
        ),
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icd_10cm_code', models.IntegerField()),
                ('icd_10_name', models.CharField(max_length=128)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            bases=(models.Model, main_app.models.Person),
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.doctors')),
                ('drug_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.drugs')),
            ],
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.doctors')),
            ],
        ),
    ]