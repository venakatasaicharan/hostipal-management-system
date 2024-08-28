from django.db import models

class Appointment(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=50, null=False)
    parent_name = models.CharField(max_length=100, null=False)
    mobile_number = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    location = models.CharField(max_length=100, null=False)
    appointment_date = models.DateField(null=False)
    num = models.CharField(max_length=10, null=False, default='asd110')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.appointment_date}"

class Admin(models.Model):
    email = models.EmailField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.email}'

class Add_doctor(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=50, null=False)
    qualification = models.CharField(max_length=100, null=False)
    college = models.CharField(max_length=100, null=False)
    percentage = models.CharField(max_length=100, null=False)
    date_of_birth = models.DateField(null=False)
    mobile_number = models.CharField(max_length=10, null=False)
    email = models.EmailField(max_length=100, null=False)
    experience = models.CharField(max_length=10, null=False)
    doctor_id = models.CharField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=100, null=False, default='123')

    def __str__(self):
        return f'{self.doctor_id}'

class Doctor(models.Model):
    username = models.CharField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.username}'

class Patient(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=False)
    mobile_number = models.BigIntegerField(null=False)
    email = models.EmailField(max_length=100, null=False)
    disease = models.CharField(max_length=100, null=False)
    patient_id = models.CharField(max_length=100, null=False, unique=True, default='123')
    bill = models.BigIntegerField(null=False, default=1499)

    def __str__(self):
        return f'{self.first_name} - {self.patient_id}'
