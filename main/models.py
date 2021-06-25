from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms
from .extras import (
    get_pic_name, 
    validate_image, 
    blog_pictures,
    profile_picture,
)
from django_countries.fields import CountryField
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

class Property(models.Model):
    #Main details
    CONDITIONS = [
        ('New', 'New'),
        ('Renovated', 'Renovated'),
        ('Old', 'Old'),
    ]

    STATUS = [
        ('For Rent', 'For Rent'),
        ('For Sale', 'For Sale'),
        ('Sold Out', 'Sold Out'),
    ]

    POST_OWNER = [
        ('Property Owner', 'Property Owner'),
        ('Property Agent', 'Property Agent'),
        ('Property Manager', 'Property Manager'),
        ('Real Estate Company', 'Real Estate Company')
    ]

    TYPES = [
        ('House', 'House'),
        ('Apartment', 'Apartment'),
        ('Commercial', 'Commercial'),
        ('Land', 'Land')
    ]

    property_owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    property_title = models.CharField(max_length=256)
    property_description = models.CharField(max_length=1024)
    property_about = models.TextField()
    property_rooms = models.IntegerField(choices=[(i, i) for i in range (30)], null=True, blank=True)
    property_bathroom = models.IntegerField(choices=[(i, i) for i in range (30)], null=True, blank=True)
    property_location = models.CharField(max_length=128)
    property_price = models.CharField(max_length=64)
    property_condition = models.CharField(max_length=64, choices=CONDITIONS)
    property_status = models.CharField(max_length=64, choices=STATUS)
    property_square_meters = models.CharField(max_length=64)
    property_posted_by = models.CharField(max_length=64, choices=POST_OWNER)
    property_post_date = models.DateTimeField(auto_now_add=True, editable=True)
    property_type = models.CharField(max_length=64, choices=TYPES)
    property_active = models.BooleanField(default=False)
    property_pic1 = models.ImageField(upload_to=get_pic_name, blank=True, null=True, validators=[validate_image])
    property_pic2 = models.ImageField(upload_to=get_pic_name, blank=True, null=True, validators=[validate_image])
    property_pic3 = models.ImageField(upload_to=get_pic_name, blank=True, null=True, validators=[validate_image])
    property_pic4 = models.ImageField(upload_to=get_pic_name, blank=True, null=True, validators=[validate_image])
    property_pic5 = models.ImageField(upload_to=get_pic_name, blank=True, null=True, validators=[validate_image])
    property_pic6 = models.ImageField(upload_to=get_pic_name, blank=True, null=True, validators=[validate_image])
    property_pic7 = models.ImageField(upload_to=get_pic_name, blank=True, null=True, validators=[validate_image])
    property_pic8 = models.ImageField(upload_to=get_pic_name, blank=True, null=True, validators=[validate_image])

    #Property Extras
    kitchen = models.BooleanField()
    air_condition = models.BooleanField()
    balcony = models.BooleanField()
    gym = models.BooleanField()
    garden = models.BooleanField()
    cctv = models.BooleanField()
    playground = models.BooleanField()
    furnished = models.BooleanField()
    parking = models.BooleanField()

    def __str__(self):
        return self.property_title

class PageView(models.Model):
    viewer = models.ForeignKey(User, on_delete=models.CASCADE)
    property_viewed = models.ForeignKey(Property, on_delete=models.CASCADE)
    view = models.PositiveIntegerField()

class UserInformation(models.Model):
    visitor = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=64, null=True, blank=True)
    continent_code = models.CharField(max_length=64, null=True, blank=True)
    continent_name = models.CharField(max_length=64, null=True, blank=True)
    country_code = models.CharField(max_length=64, null=True, blank=True)
    country_name = models.CharField(max_length=64, null=True, blank=True)
    dma_code = models.PositiveIntegerField(null=True, blank=True)
    is_in_european_union = models.BooleanField(null=True, blank=True)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    region = models.CharField(max_length=8, null=True, blank=True)
    time_zone = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return "Data for user: %s in country: %s" % (self.visitor, self.country_name)

class Review(models.Model):
    RATINGS = [
        (1.0, 1.0),
        (2.0, 2.0),
        (3.0, 3.0),
        (4.0, 4.0),
        (5.0, 5.0),
    ]
    reviewed_user = models.CharField(max_length=256)
    comment_reviewed = models.TextField(null=True, blank=True)
    rating_reviewed = models.FloatField(max_length=5, null=True, blank=True, choices=RATINGS)
    average_review = models.FloatField(max_length=5, null=True, blank=True)
    date_reviewed = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return "Review for %s left on %s" % (self.reviewed_user, self.date_reviewed)

class Article(models.Model):
    article_title = models.CharField(max_length=256)
    article_intro = models.CharField(max_length=512)
    article_post_date = models.DateField(max_length=64)
    article_author = models.ForeignKey(User, on_delete=models.CASCADE)
    article_tag = models.CharField(max_length=64)
    article_picture = models.ImageField(blank=True, null=True, upload_to=blog_pictures)
    article_content = models.TextField()

class Profile(models.Model):
    REGISTERED_AS = (
        ('Admin', 'Admin'),
        ('Agent', 'Agent'),
        ('Real Estate Developer', 'Real Estate Developer'),
        ('Auctioneer', 'Auctioneer'),
        ('Client', 'Client'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=profile_picture)
    country = CountryField(blank_label='(Please Select your Country)')
    region = models.CharField(max_length=128)
    registered_as = models.CharField(max_length=32, choices=REGISTERED_AS, null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(models.signals.post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class FAQS(models.Model):
    faqs_headline = models.CharField(max_length=256, null=True, blank=True)
    faqs_point1 = models.TextField(null=True, blank=True)
    faqs_point2 = models.TextField(null=True, blank=True)
    faqs_point3 = models.TextField(null=True, blank=True)
    faqs_point4 = models.TextField(null=True, blank=True)
    faqs_point5 = models.TextField(null=True, blank=True)
    faqs_point6 = models.TextField(null=True, blank=True)
    faqs_point7 = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.faqs_headline

class TermsAndConditions(models.Model):
    tac_heading = models.CharField(max_length=128, null=True, blank=True)
    tac_instance = models.TextField()

    def __str__(self):
        return str(self.tac_heading)
