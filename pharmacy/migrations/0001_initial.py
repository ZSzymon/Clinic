# Generated by Django 4.1.5 on 2023-01-21 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'required': 'Your Name is Required'}, max_length=128, null=True, unique=True, verbose_name='Name')),
                ('price', models.FloatField(blank=True, default=55, null=True, verbose_name='Price')),
                ('image', models.ImageField(default='drugs/d1.jpg', upload_to='products/')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(limit_choices_to={'type': 'DOCTOR'}, on_delete=django.db.models.deletion.CASCADE, related_name='Doctor', to=settings.AUTH_USER_MODEL)),
                ('drug', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Drug', to='pharmacy.drug')),
                ('patient', models.ForeignKey(limit_choices_to={'type': 'PATIENT'}, on_delete=django.db.models.deletion.CASCADE, related_name='Patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
