from django.urls import path
from mainapp import  views


urlpatterns = [
    path('', views.home),
    path('about-us', views.about_us),
    path('contact-us', views.contact_us),
    path('courses', views.courses),
    path('enquiry', views.enquiry),
    
    # path('blogs', views.blogs),
]
