from django.db import models

# Create your models here.

class Appointment(models.Model):
    name=models.CharField(max_length=30)
    text=models.CharField(max_length=800)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()

    def __str__(self):
        return self.name