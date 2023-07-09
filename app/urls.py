from django.urls import path
from . import views

urlpatterns=[
    path('',views.createAppointment,name="appointment"),
    path('success/',views.success,name="success"),
]