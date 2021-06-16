from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth 
from .forms import PropertyForm, ProfileForm
from django_countries.data import COUNTRIES
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .models import (
    Property, 
    PageView, 
    UserInformation, 
    Review, 
    Article,
    Profile,
    FAQS,
)
from django.utils import timezone
from django.core.exceptions import ValidationError
from user_visit.models import UserVisit
from django.contrib.gis.geoip2 import GeoIP2
from django.http import HttpResponseRedirect
from django.db.models import Avg, Sum

global properties

def home(request):
    latest_properties = Property.objects.filter(property_active=True)[:3]
    if request.user.is_authenticated:
        data_capture = UserInformation()
        user_ip_address = UserVisit().remote_addr

        user_checker = UserInformation.objects.filter(
            visitor = request.user
        )
        ip_checker = UserVisit.objects.filter(
            remote_addr = user_ip_address
        )
        if not user_checker and not ip_checker:
            location_object = GeoIP2()
            captured_info = location_object.city('72.14.207.99') #! for test purposes    
            data_capture.visitor = request.user
            data_capture.city = captured_info.get('city')
            data_capture.continent_code = captured_info.get('continent_code')
            data_capture.continent_name = captured_info.get('continent_name')
            data_capture.country_code = captured_info.get('country_code')
            data_capture.country_name = captured_info.get('country_name')
            data_capture.dma_code = captured_info.get('dma_code')
            data_capture.is_in_european_union = captured_info.get('is_in_european_union')
            data_capture.latitude = captured_info.get('latitude')
            data_capture.longitude = captured_info.get('longitude')
            data_capture.postal_code = captured_info.get('postal_code')
            data_capture.region = captured_info.get('region')
            data_capture.time_zone = captured_info.get('time_zone')
            data_capture.save()
    
    return render(request, 'main/home.html', {'latest_properties': latest_properties})

def properties(request):
    all_approved_properties = Property.objects.filter(property_active=True)
    return render(request, 'main/properties.html', {'all_approved_properties': all_approved_properties})

def property_details(request, property_id):
    properties = get_object_or_404(Property, pk=property_id)
    current_user = request.user
    request_view = PageView.objects.filter(
        viewer = current_user,
        property_viewed= properties,
    )
    if not request_view:
        PageView.objects.create(
            viewer = current_user,
            property_viewed = properties,
            view = 1
        )
    
    nearby_properties = Property.objects.filter(
        property_location = properties.property_location,
        property_active = True
    ).order_by('property_post_date')[:2]
    views = PageView.objects.filter(property_viewed=properties).count()
    return render(request, 'main/property_details.html', {'properties': properties, 'views': views, 'nearby_properties': nearby_properties})

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
    auth.logout(request)
    return redirect('home')

def add_property(request):
    property_instance = Property()
    logged_user = User.objects.get(username=request.user.username)
    property_form = PropertyForm(request.POST, request.FILES,)
    
    if property_form.is_valid():
        
        property_title = property_form.cleaned_data['property_title']
        property_price = property_form.cleaned_data['property_price']
        property_description = property_form.cleaned_data['property_description']
        property_about = property_form.cleaned_data['property_about']
        property_location = property_form.cleaned_data['property_location']
        property_condition = property_form.cleaned_data['property_condition']
        property_status = property_form.cleaned_data['property_status']
        property_square_meters = property_form.cleaned_data['property_square_meters']
        property_posted_by = property_form.cleaned_data['property_posted_by']
        property_type = property_form.cleaned_data['property_type']
        property_pic1 = property_form.cleaned_data['property_pic1']
        property_pic2 = property_form.cleaned_data['property_pic2']
        property_pic3 = property_form.cleaned_data['property_pic3']
        property_pic4 = property_form.cleaned_data['property_pic4']
        property_pic5 = property_form.cleaned_data['property_pic5']
        property_pic6 = property_form.cleaned_data['property_pic6']
        property_pic7 = property_form.cleaned_data['property_pic7']
        property_pic8 = property_form.cleaned_data['property_pic8']
        kitchen = property_form.cleaned_data['kitchen']
        air_condition = property_form.cleaned_data['air_condition']
        balcony = property_form.cleaned_data['balcony']
        gym = property_form.cleaned_data['gym']
        garden = property_form.cleaned_data['garden']
        cctv = property_form.cleaned_data['cctv']
        furnished = property_form.cleaned_data['furnished']
        parking = property_form.cleaned_data['parking']
        playground = property_form.cleaned_data['playground']
        property_form.property_active = False
        property_form.property_post_date = timezone.now()
        user_property_form = property_form.save(commit=False)
        user_property_form.property_owner = request.user
        property_form.save()
        return render(request, 'main/add_property.html', {'property_form': property_form})

    return render(request, 'main/add_property.html', {'property_form': property_form})

def my_properties(request):
    my_properties = Property.objects.filter(property_owner=request.user, property_active=True)
    return render(request, 'main/my_properties.html', {'my_properties': my_properties})

def review(request):
    if request.method == 'POST':
        review_object = Review()
        review_object.date_reviewed = timezone.now()
        review_object.rating_reviewed = request.POST['rating_reviewed']
        review_object.comment_reviewed = request.POST['comment_reviewed']
        review_object.reviewed_user = request.POST['reviewed_user']
        user_rated = request.POST['reviewed_user']
        user_rated_review = request.POST['rating_reviewed']
        review_object.save()

        #current_user_reviews = Review.objects.filter(reviewed_user=review_object.reviewed_user)
        #current_user_reviews.aggregate(Avg('rating_reviewed'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return redirect('home')

def blogs(request):
    articles = Article.objects.all()
    empty_check = Article.objects.all().count()
    return render(request, 'main/blogs.html', {'articles': articles, 'empty_check': empty_check})

def blog_details(request, blog_id):
    article = get_object_or_404(Article, pk=blog_id)
    return render(request, 'main/blog_details.html', {'article': article})

def all_agents(request):
    profiles = Profile.objects.all()
    return render(request, 'main/all_agents.html', {'profiles': profiles})

def faqs(request):
    faqs = FAQS.objects.all()
    return render(request, 'main/faqs.html', {'faqs': faqs})

def my_profile(request):
    current_profile = Profile.objects.get(user=request.user)
    current_user = User.objects.get(username=request.user)
    if request.method == 'POST':
        if request.POST['first_name'] and request.POST['last_name'] and request.POST['phone_number'] and request.POST['profile_picture'] and request.POST['country'] and request.POST['region']:
            current_user.first_name = request.POST['first_name']
            current_user.last_name = request.POST['last_name']
            current_profile.phone_number = request.POST['phone_number']
            current_profile.profile_picture = request.POST['profile_picture']
            current_profile.country = request.POST.get('country')
            current_profile.region = request.POST['region']
            current_user.save()
            current_profile.save()
            messages.success(request, 'Profile Changed Successfully! Changes will take place as the server refreshes the Database.', extra_tags='alert')
            return render(request, 'main/my_profile.html')
    return render(request, 'main/my_profile.html')

def update_profile(request):
    pass

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        comment = request.POST['comment']
        if name and email and subject and comment:
            try:
                send_mail(subject, f'Sender Mail: {email}. \n Message: {comment}', email, ['mundiakaluson@gmail.com'], )
                return render(request, 'main/contact.html', {'success': 'Message Sent!'})
            except BadHeaderError:
                return HttpResponseRedirect('/main/contact', {'error': 'Message could not be sent!'})
    return render(request, 'main/contact.html')