# Generated by Django 5.0.4 on 2024-07-01 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0008_alter_admin_email_alter_patient_bill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_doctor',
            name='mobile_number',
            field=models.CharField(max_length=10),
        ),
    ]
