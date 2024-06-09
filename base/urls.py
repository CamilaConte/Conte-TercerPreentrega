from django.urls import path
from base import views

urlpatterns = [
    path('', views.home, name="home"),
    path('dentists/', views.list_dentist, name="list_dentists"),
    path('dentists/save/', views.save_dentist, name="create_dentist"),
]