from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth 
from .forms import PropertyForm
from .models import Property
from django.utils import timezone

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

def add_property(request):
    property_instance = Property()
    property_form = PropertyForm(request.POST or None, request.FILES or None, instance=property_instance)
    if request.method == 'POST':
        if property_form.is_valid():
            property_owner = request.user
            property_title = property_form.cleaned_data['property_title']
            property_price = property_form.cleaned_data['property_price']
            property_description = property_form.cleaned_data['property_descriptions']
            property_about = property_form.cleaned_data['property_about']
            property_location = property_form.cleaned_data['property_location']
            property_condition = property_form.cleaned_data['property_condition']
            property_status = property_form.cleaned_data['property_status']
            property_square_meters = property_form.cleaned_data['property_square_meters']
            property_posted_by = property_form.cleaned_data['property_posted_by']
            property_type = property_form.cleaned_data['property_type']
            property_pic1 = property_form.cleaned_data['property_pic1']
            property_pic1 = property_form.cleaned_data['property_pic2']
            property_pic1 = property_form.cleaned_data['property_pic3']
            property_pic1 = property_form.cleaned_data['property_pic4']
            property_pic1 = property_form.cleaned_data['property_pic5']
            property_pic1 = property_form.cleaned_data['property_pic6']
            property_pic1 = property_form.cleaned_data['property_pic7']
            property_pic1 = property_form.cleaned_data['property_pic8']
            kitchen = property_form.cleaned_data['kitchen']
            air_condition = property_form.cleaned_date['air_condition']
            balcony = property_form.cleaned_data['balcony']
            gym = property_form.cleaned_data['gym']
            garden = property_form.cleaned_data['garden']
            cctv = property_form.cleaned_data['cctv']
            furnished = property_form.cleaned_data['furnished']
            parking = property_form.cleaned_data['parking']
            property_form.property_active = False
            property_form.property_post_date = timezone.now()

    return render(request, 'main/add_property.html', {'property_form': property_form})