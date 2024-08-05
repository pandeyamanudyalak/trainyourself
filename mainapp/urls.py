from django.urls import path
from mainapp import  views


urlpatterns = [
    path('', views.home),
    path('about-us', views.about_us),
    path('contact-us', views.contact_us),
    path('services', views.services),
    path('blogs', views.blogs),
]
