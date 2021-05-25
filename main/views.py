from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth 

def home(request):
    return render(request, 'main/home.html')

def properties(request):
    return render(request, 'main/properties.html')

def property_details(request):
    return render(request, 'main/property_details.html')

def register(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm-password']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'main/register.html', {'error': 'This username exists!'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username = request.POST['username'],
                    first_name = request.POST['first_name'],
                    last_name = request.POST['last_name'],
                    email = request.POST['email'],
                    password = request.POST['password']
                )
                user.is_active = True
                user.save()
                auth.login(request, user)
                return redirect('register_success')

    return render(request, 'main/register.html')

def login(request):
    if request.method == 'POST':
        if not request.POST.get('remember', None):
            request.session.set_expiry(0)
        user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        elif user is None:
            return render(request, 'main/login.html', {'error': 'You have not registered!'})
    return render(request, 'main/login.html')

def register_success(request):
    return render(request, 'main/register_success.html')

def logout(request):
    auth.logout(request, user)
    return redirect('home')