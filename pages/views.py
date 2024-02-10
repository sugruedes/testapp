from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'pages/home.html', context)

def about(request):
    return render(request, 'pages/about.html', {})

def shopping(request):
    return render(request, 'pages/shopping.html', {})

def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'pages/login.html', {'form': form })
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('project_index')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'pages/login.html', {'form': form})

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')            


def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'pages/register.html', { 'form': form}) 
    
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have signed up successfully.')
            login(request, user)
            return redirect('project_index')
        else:
            return render(request, 'pages/register.html', {'form': form})

