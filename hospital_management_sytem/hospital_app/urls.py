from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('about_us/', views.about_us, name='about_us'),
    path('appointment/', views.appointment, name='appointment'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('doctor_login/', views.doctor_login, name='doctor_login'),
    path('patient_login/', views.patient_login, name='patient_login'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('doctor_page/', views.doctor_page, name='doctor_page'),
    path('patient_page/', views.patient_page, name='patient_page'),
    path('logout/', views.logout, name='logout'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_patient_doc/', views.add_patient_doc, name='add_patient_doc'),
    path('show_apt/', views.show_apt, name='show_apt'),
    path('delete_appointment/<int:id>/', views.delete_appointment, name='delete_appointment'),
    path('show_doc/', views.show_doc, name='show_doc'),
    path('show_pnt/', views.show_pnt, name='show_pnt'),
    path('show_apt_doc/', views.show_apt_doc, name='show_apt_doc'),
    path('show_pnt_doc/', views.show_pnt_doc, name='show_pnt_doc'),
    path('pnt_details/', views.pnt_details, name='pnt_details'),
    path('settings_admin/', views.settings_admin, name='settings_admin'),
    path('settings_doc/', views.settings_doc, name='settings_doc'),
]
