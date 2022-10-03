#import email
from cmath import pi
from datetime import datetime
#import email
from unicodedata import name
#from home.models import C
from numpy import save
from .forms import StudentRegistration
from .models import Registration

#from http.client import HTTPResponse

from django.shortcuts import render,HttpResponseRedirect

#from Hello.home.models import Contact

# Create your views here.

#This function will Add new Item and Show All Items
def index(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Registration(name=nm, email= em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = Registration.objects.all()
    return render(request, 'index.html',{'form':fm, 'stu':stud})

#This function will Update/edit
def update_data(request,id):
    if request.method == 'POST':
        pi = Registration.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Registration.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request,'update.html', {'form':fm })



#This function will Delete 
def delete_data(request, id):
    if request.method == 'POST':
        pi= Registration.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    
    return render(request, 'index.html', {'form':fm}) 
    
#HttpResponse("This is homepage")
def update(request):
    return render(request,'update.html')




    