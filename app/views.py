from django.shortcuts import render,redirect
from .models import Appointment
# Create your views here.

def createAppointment(request):
    if request.method=='POST':
        name=request.POST.get('name')
        text=request.POST.get('text')
        start_time=request.POST.get('start_time')
        end_time=request.POST.get('end_time')
        a=Appointment(name=name,text=text,start_time=start_time,end_time=end_time)
        a.save()
        return redirect('success')
    else:
        return render(request,'app/home.html')
    
def success(request):
    return render(request,'app/success.html')
