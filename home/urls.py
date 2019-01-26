from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-home'),
    path('contact/', views.contact, name='contact-home'),
    path('about/', views.about, name='about-home'),
]
