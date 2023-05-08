from django.urls import path
from . import views

urlpatterns = [
    path('superlee/attendance', views.attendance, name='attendance'),
    path('superlee/input-attendance', views.input, name='input'),
    path('superlee/registration/', views.registration, name='registration'),
    path('superlee/registration/family-details/', views.family_details, name='family_details'),
    path('superlee/registration/work-agreement/', views.workloc_agreement, name='workloc_agreement'),
    path('superlee/registration/upload-documents/', views.mand_docs, name='mand_docs'),
    path('superlee/registration/schoolings/', views.schoolings, name='schoolings'),
    path('superlee/registration/ug-details/', views.ug_details, name='ug_details'),
    path('superlee/registration/pg-details/', views.pg_details, name='pg_details'),
    path('superlee/registration/others/', views.other_details, name='other_details'),
    path('superlee/registration/acknowledgement/', views.ack, name='ack'),
    path('superlee/test', views.test, name='test'),
    path('superlee/intern-punch/', views.intern_attendance_login, name='intern_attendance_login'),
    path('superlee/intern-punch/signin', views.intern_attendance, name='intern_attendance'),
    path('superlee/intern-punch/signout', views.intern_attendance_out, name='intern_attendance_out'),
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('our-vision', views.vision, name='vision'),
    path('our-mission', views.mission, name='mission'),
    path('contacts', views.contact, name='contact'),
    path('our-top-recruiters', views.companies, name='companies'),
    path('Placement-Process', views.p_process, name='p_process'),
    path('our-infrastructure', views.infrastructure, name='infrastructure'),
]