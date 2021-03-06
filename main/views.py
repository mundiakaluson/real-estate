from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import PropertyForm, ProfileForm
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
    TermsAndConditions,
)
from django.utils import timezone
from django.core.exceptions import ValidationError
from user_visit.models import UserVisit
from django.contrib.gis.geoip2 import GeoIP2
from django.http import HttpResponseRedirect
from django.db.models import Avg, Sum
from django_countries.data import COUNTRIES

def home(request):
    latest_properties = Property.objects.all()[:3]
    if request.user.is_authenticated:
        data_capture = UserInformation()
        user_ip_address = UserVisit().remote_addr

        user_checker = UserInformation.objects.filter(
            visitor=request.user
        )
        ip_checker = UserVisit.objects.filter(
            remote_addr=user_ip_address
        )
        if not user_checker and not ip_checker:
            location_object = GeoIP2()
            captured_info = location_object.city('72.14.207.99')  # ! for test purposes
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
    faqs = FAQS.objects.all()


    return render(request, 'main/home.html', {'latest_properties': latest_properties, 'faqs': faqs})


def properties(request):
    all_approved_properties = Property.objects.all()
    return render(request, 'main/properties.html', {'all_approved_properties': all_approved_properties})


def property_details(request, property_id):
    properties = get_object_or_404(Property, pk=property_id)
    if request.user.is_authenticated:
        request_view = PageView.objects.filter(
            viewer=request.user,
            property_viewed=properties,
        )
        if not request_view:
            PageView.objects.create(
                viewer=request.user,
                property_viewed=properties,
                view=1
            )

    nearby_properties = Property.objects.filter(
        property_location=properties.property_location,
        property_active=True
    ).order_by('property_post_date')[:2]
    views = PageView.objects.filter(property_viewed=properties).count()
    return render(request, 'main/property_details.html',
                  {'properties': properties, 'views': views, 'nearby_properties': nearby_properties})


def register(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm-password']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'main/register.html', {'error': 'This username exists!'})
            except User.DoesNotExist:
                new_user = User.objects.create_user(
                    username=request.POST['username'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'],
                    password=request.POST['password']
                )
                new_user.is_active = True
                new_profile = Profile.objects.create(user=new_user)
                new_profile.save()
                new_user.save()
                auth.login(request, user)
                return redirect('register_success')

    return render(request, 'main/register.html')


def login(request):
    if request.method == 'POST':
        if not request.POST.get('remember', None):
            request.session.set_expiry(0)
        user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        elif user is None:
            return render(request, 'main/login.html', {'error': 'Username or password does not exist!'})
    return render(request, 'main/login.html')


def register_success(request):
    return render(request, 'main/register_success.html')


def logout(request):
    auth.logout(request)

    return redirect('home')


def add_property(request):
    property_instance = Property()
    property_form = PropertyForm(request.POST, request.FILES, instance=property_instance)

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
        school = property_form.cleaned_data['school']
        school = property_form.cleaned_data['hospital']
        school = property_form.cleaned_data['borehole']
        school = property_form.cleaned_data['bus_stop']
        school = property_form.cleaned_data['internet_service_provider']
        school = property_form.cleaned_data['bank']
        school = property_form.cleaned_data['mall']
        school = property_form.cleaned_data['shops']
        school = property_form.cleaned_data['main_road']
        property_form.property_post_date = timezone.now()
        user_property_form = property_form.save(commit=False)
        user_property_form.property_owner = request.user
        property_form.save()
        return redirect('my_properties')

    return render(request, 'main/add_property.html', {'property_form': property_form})


def my_properties(request):
    property_check = Property.objects.filter(property_owner=request.user).count()
    my_properties = Property.objects.filter(property_owner=request.user)
    return render(request, 'main/my_properties.html',
                  {'my_properties': my_properties, 'property_check': property_check})


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

        # current_user_reviews = Review.objects.filter(reviewed_user=review_object.reviewed_user)
        # current_user_reviews.aggregate(Avg('rating_reviewed'))
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
    # try:
    #     current_profile = Profile.objects.get(user=request.user)
    # except Profile.DoesNotExist:
    #     current_profile = Profile.objects.create(user=request.user)
    profile_form = ProfileForm()
    # if request.method == 'POST':    
    #     if profile_form.is_valid():
    #         # phone_number = profile_form.cleaned_data['phone_number']
    #         # country = profile_form.cleaned_data['country']
    #         # profile_picture = profile_form.cleaned_data['profile_picture']
    #         # region = profile_form.cleaned_data['region']
    #         # registered_as = profile_form.cleaned_data['registered_as']
    #         # user_profile_form = profile_form.save(commit=False)
    #         # user_profile_form.user = request.user
    #         # profile_form.save()
    #         # messages.success(request, 'Profile Changed Successfully! Changes will take place as the server refreshes the Database.', extra_tags='alert')
    #         profile_form.save()
    #         messages.success(request, 'Profile Changed Successfully! Changes will take place as the server refreshes the Database.', extra_tags='alert')
    #     return render(request, 'main/my_profile.html', {'profile_form': profile_form})
    return render(request, 'main/my_profile.html', {'profile_form': profile_form})
    # if request.method == 'POST':
    #     if request.POST['phone_number'] and request.POST['country'] and request.POST['region'] and 'profile_picture' in request.FILES:
    #         current_profile = Profile.objects.get(user=request.user)
    #         current_profile.user = request.user
    #         current_profile.phone_number = request.POST['phone_number']
    #         current_profile.profile_picture = request.FILES.get('profile_picture')
    #         current_profile.country = request.POST['country']
    #         current_profile.region = request.POST['region']
    #         current_profile.save()
    #         print(request.POST['phone_number'])
    #         messages.success(request,
    #                             'Profile Changed Successfully! Changes will take place as the server refreshes the Database.',
    #                             extra_tags='alert')
    #         return render(request, 'main/my_profile.html', {'countries': list(COUNTRIES.values())})

    # return render(request, 'main/my_profile.html', {'countries': list(COUNTRIES.values())})

def update_profile(request):
    try:
        current_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        current_profile = Profile.objects.create(user=request.user)
    profile_form = ProfileForm(request.POST, request.FILES, instance=current_profile)
    if request.method == 'POST':    
        if profile_form.is_valid():
            user_profile = profile_form.save(commit=False)
            user_profile.user = request.user
            profile_form.save()
            messages.success(request, 'Profile Changed Successfully! Changes will take place as the server refreshes the Database.', extra_tags='alert')
        return render(request, 'main/my_profile.html', {'profile_form': profile_form})
    return render(request, 'main/my_profile.html', {'countries': list(COUNTRIES.values())})

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


def for_rent(request):
    for_rent_properties = Property.objects.filter(property_active=True, property_status='For Rent')
    return render(request, 'main/for_rent.html', {'for_rent_properties': for_rent_properties})


def for_sale(request):
    for_sale_properties = Property.objects.filter(property_active=True, property_status='For Sale')
    return render(request, 'main/for_sale.html', {'for_sale_properties': for_sale_properties})


def property_search(request):
    condition = request.POST.getlist('condition')
    print(condition)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def terms_and_conditions(request):
    tac_instances = TermsAndConditions.objects.all()
    return render(request, 'main/terms-and-conditions.html', {'tac_instances': tac_instances})

def delete_property(request, property_id):
    context = {}
    try:
        property_to_delete = Property.objects.get(id=property_id)
        property_to_delete.delete()
        my_properties = Property.objects.filter(property_owner=request.user, property_active=True)
        return render(request, 'main/my_properties.html', {'my_properties': my_properties, 'delete_message': 'Deleted Successfully!'})
    except:
        context['error_message'] = 'Property does not exist!'
        my_properties = Property.objects.filter(property_owner=request.user, property_active=True)
    return render(request, 'main/my_properties.html', {'my_properties': my_properties, 'error_message': 'An error occurred!'})

def property_search(request):
    # if request.method == 'POST':
    #     if request.POST['rent_or_sale'] and request.POST['property_type'] and request.POST['property_type']:
    if 'rent_or_sale' in request.GET and 'property_type' in request.GET and 'location' in request.GET:
        rent_or_sale = request.GET['rent_or_sale']
        property_type = request.GET['property_type']
        location = request.GET['location']

        results = Property.objects.exclude(
            property_status__isnull=False,
            property_type__isnull=False,
            property_location__isnull=False
        ).filter(
            property_status__icontains=rent_or_sale,
            property_type__icontains=property_type,
            property_location__icontains=location,
        )
        result_check = results.count()
    return render(request, 'main/property_search.html', {'results': results, 'result_check': result_check, 'rent_or_sale': rent_or_sale, 'property_type': property_type, 'location': location})