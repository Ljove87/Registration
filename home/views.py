from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post

from django.contrib import messages
from .forms import UserRegisterForm


def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now())
    return render(request, 'home/home.html', {'posts':posts})

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account {username} has been created! You can log in now!')
            return redirect('login')
    else:
        form = UserRegisterForm
    return render(request, 'home/register.html', {'form': form})

