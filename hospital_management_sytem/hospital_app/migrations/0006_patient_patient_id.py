# Generated by Django 5.0.4 on 2024-06-23 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0005_patient_alter_add_doctor_mobile_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='patient_id',
            field=models.CharField(default='123', max_length=100, unique=True),
        ),
    ]
