from django.shortcuts import render, redirect

from django.contrib import messages

from datetime import date

from .models import Appointment, Admin, Add_doctor, Patient, Doctor

import random, string

def create_id(length=5):
    characters = string.ascii_letters + string.digits
    id = ''.join(random.choice(characters) for _ in range(length))
    return id


def home(request):
    return render(request, 'hospital_app/home.html')

def services(request):
    return render(request, 'hospital_app/services.html')

def contact_us(request):
    return render(request, 'hospital_app/contact_us.html')

def about_us(request):
    return render(request, 'hospital_app/about_us.html')

def appointment(request):
    if request.method == 'POST':
        try:
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            pname = request.POST['parent_name']
            mobile = request.POST['mobile_number']
            em = request.POST['email']
            lc = request.POST['location']
            apt_date = request.POST['appointment_date']

            numb = create_id()

            appointment = Appointment(
                first_name = fname,
                last_name = lname,
                parent_name = pname,
                mobile_number = mobile,
                email = em,
                location = lc,
                appointment_date = apt_date,

                num = numb
            )
            appointment.save()

            messages.success(request, 'Appointment successfully created.')

        except ValueError:
            messages.error(request, 'Invalid date format. Please use YYYY-MM-DD.')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
            return redirect('appointment')

        
    return render(request, 'hospital_app/appointment.html')

def admin_login(request):
    if request.method == 'POST':
        em = request.POST['username']
        pwd = request.POST['password']

        admin = Admin.objects.filter(email = em, password = pwd).exists()
        if admin == True:
            return redirect('admin_page')
        else:
            messages.error(request, 'Login falied.')

    return render(request, 'hospital_app/admin_login.html')


def doctor_login(request):
    if request.method == 'POST':
        user = request.POST['username']
        pwd = request.POST['password']

        doc = Add_doctor.objects.filter(doctor_id = user, password = pwd).exists()
        if doc == True:
            return redirect('doctor_page')
        else:
            messages.error(request, 'Login falied.')

    return render(request, 'hospital_app/doctor_login.html')

def patient_login(request):
    if request.method == 'POST':
        user = request.POST['username']

        pnt = Patient.objects.filter(patient_id=user).exists()
        if pnt:
            request.session['patient_id'] = user
            return redirect('pnt_details')
        else:
            messages.error(request, 'Login failed')

    return render(request, 'hospital_app/patient_login.html')


def admin_page(request):
    return render(request, 'hospital_app/admin_page.html')

def doctor_page(request):
    return render(request, 'hospital_app/doctor_page.html')

def patient_page(request):
    return render(request, 'hospital_app/patient_page.html')

def logout(request):
    return redirect('home')

def add_doctor(request):
    if request.method == 'POST':
        try:
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            qua = request.POST['qualification']
            clg = request.POST['college']
            percent = request.POST['percentage']
            dob = request.POST['dob']
            ph_num = request.POST['phone']
            em = request.POST['email']
            exp = request.POST['experience']
            
            doc_id = create_id()

            add_doc = Add_doctor(
                first_name = fname,
                last_name = lname,
                qualification = qua,
                college = clg,
                percentage = percent,
                date_of_birth = dob,
                mobile_number = ph_num,
                email = em,
                experience = exp,
                doctor_id = doc_id
            )
            add_doc.save()

            messages.success(request, 'Doctor successfully added.')
        except Exception as e:
            e = 'Enter details correctly'
            messages.error(request, f'{e}')

    return render(request, 'hospital_app/add_doctor.html')

def add_patient(request):
    if request.method == 'POST':
        try:
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            dob = request.POST['dob']
            ph_num = request.POST['phone']
            em = request.POST['email']
            dse = request.POST['disease']
            bill = request.POST['bill']
            pnt_id = create_id()

            add_pnt = Patient(
                first_name = fname,
                last_name = lname,
                date_of_birth = dob,
                mobile_number = ph_num,
                email = em,
                disease = dse,
                patient_id =pnt_id,
                bill = bill
            )
            add_pnt.save()

            messages.success(request, 'Patient successfully added.')
        except Exception as e:
            e = 'Enter details correctly'
            messages.error(request, f'{e}')


    return render(request, 'hospital_app/add_patient.html')

def add_patient_doc(request):
    if request.method == 'POST':
        try:
            fname = request.POST['first_name']
            lname = request.POST['last_name']
            dob = request.POST['dob']
            ph_num = request.POST['phone']
            em = request.POST['email']
            dse = request.POST['disease']
            bill = request.POST['bill']
            pnt_id = create_id()

            add_pnt = Patient(
                first_name = fname,
                last_name = lname,
                date_of_birth = dob,
                mobile_number = ph_num,
                email = em,
                disease = dse,
                patient_id =pnt_id,
                bill = bill
            )
            add_pnt.save()

            messages.success(request, 'Patient successfully added.')
        except Exception as e:
            e = 'Enter details correctly'
            messages.error(request, f'An error occurred: {e}')


    return render(request, 'hospital_app/add_patient_doc.html')


def show_apt(request):
    appointments = Appointment.objects.all()
    return render(request, 'hospital_app/show_apt.html', {'appointments':appointments})

def delete_appointment(request, id):
    Appointment.objects.filter(id=id).delete()
    messages.success(request, 'Appointment successfully deleted.')
    return redirect('show_apt')

def show_doc(request):
    doc = Add_doctor.objects.all()
    return render(request, 'hospital_app/show_doc.html', {'doc':doc})

def show_apt_doc(request):
    appointments = Appointment.objects.all()
    return render(request, 'hospital_app/show_apt_doc.html', {'appointments':appointments})

def show_pnt(request):
    pnt = Patient.objects.all()
    return render(request, 'hospital_app/show_pnt.html', {'pnt':pnt})

def show_pnt_doc(request):
    pnt = Patient.objects.all()
    return render(request, 'hospital_app/doc_pnt_show.html', {'pnt':pnt})

def pnt_details(request):
    if request.method == 'POST':
        search = request.POST.get('username')
        pnt = Patient.objects.filter(patient_id=search)

        if pnt.exists():
            return render(request, 'hospital_app/pnt_details.html', {'pnt': pnt})
        else:
            messages.error(request, 'Patient ID not found.')
            return redirect('patient_login')
    else:
        patient_id = request.session.get('patient_id')
        if patient_id:
            pnt = Patient.objects.filter(patient_id=patient_id)
            if pnt.exists():
                return render(request, 'hospital_app/pnt_details.html', {'pnt': pnt})
            else:
                messages.error(request, 'Patient ID not found in session.')
        return redirect('patient_login')


def settings_admin(request):
    if request.method == 'POST':
            try:
                admin_email = request.POST['admin_id']
                new_password = request.POST['password']
                re_enter_password = request.POST['re_enter_password']

                if new_password != re_enter_password:
                    messages.error(request, 'Passwords do not match.')
                    return redirect('settings_admin')

                admin = Admin.objects.get(email=admin_email)
                admin.password = new_password
                admin.save()

                messages.success(request, 'Password successfully updated.')
            except Admin.DoesNotExist:
                messages.error(request, 'Admin ID does not exist.')
            except Exception as e:
                e = 'Something went wrong'
                messages.error(request, f'An error occurred: {e}')

    return render(request, 'hospital_app/settings_admin.html')

def settings_doc(request):
    if request.method == 'POST':
        try:
            doctor_id = request.POST['doc_id']
            new_password = request.POST['password']
            re_enter_password = request.POST['re_enter_password']

            if new_password != re_enter_password:
                messages.error(request, 'Passwords do not match.')
                return redirect('settings_doc')

            doctor = Add_doctor.objects.get(doctor_id=doctor_id)
            doctor.password = new_password
            doctor.save()

            messages.success(request, 'Password successfully updated.')
        except Add_doctor.DoesNotExist:
            messages.error(request, 'Doctor ID does not exist.')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')

    return render(request, 'hospital_app/settings_doc.html')
