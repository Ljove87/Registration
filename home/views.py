from django.shortcuts import render
from django.utils import timezone
from .models import Post


def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'home/home.html', {'posts':posts})

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')
