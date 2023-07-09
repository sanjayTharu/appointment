from django.contrib import admin
from .models import Appointment

# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display=('name','text','start_time','end_time')

admin.site.register(Appointment,AppointmentAdmin)