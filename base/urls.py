from django.urls import path
from base import views

urlpatterns = [
    path('', views.home),
    path('patients/', views.list_patient, name="list_patients"),
    path('patients/save', views.save_patient, name="create_patient"),
    path('dentists/', views.list_dentist, name="list_dentists"),
    path('dentists/save', views.save_dentist, name="create_dentist"),
]