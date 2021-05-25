from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def properties(request):
    return render(request, 'main/properties.html')

def property_details(request):
    return render(request, 'main/property_details.html')

def register(request):
    return render(request, 'main/register.html')

def login(request):
    return render(request, 'main/login.html')