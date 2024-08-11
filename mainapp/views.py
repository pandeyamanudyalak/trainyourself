from django.shortcuts import render, redirect
from .models import Enquiry

# Create your views here.


def home(request):
    return render(request,'index.html')


def about_us(request):
    return render(request,'about-us.html')


def contact_us(request):
    return render(request,'contact-us.html')


def courses(request):
    return render(request,'courses.html')


def blogs(request):
    return render(request,'blog.html')


def enquiry(request):
    print('RQUET DATA -----',request.POST)
    email = request.POST.get('email')
    message = request.POST.get('message')
    
    if email and message:
        enquiry_inst = Enquiry()
        enquiry_inst.email = email
        enquiry_inst.message = message
        enquiry_inst.save()
        
    return redirect('/')