from django.shortcuts import render

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