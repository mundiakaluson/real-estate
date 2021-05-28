from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify
from django import forms

def get_pic_name(instance, pic_name):
    title = instance.property_title
    slug = slugify(title)
    return "properties/%s/%s-%s" % (title, slug, pic_name)

def validate_image(image):
        file_size = image.file.size
        limit_kb = 150
        if file_size > limit_kb:
            raise forms.ValidationError("Max size of file is %s KB" % limit)
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
    ]

    TYPES = [
        ('Mansion', 'Mansion'),
        ('Bungalow', 'Bungalow'),
        ('Cottage', 'Cottage'),
        ('Apartment', 'Apartment'),
        ('Condo', 'Condo'),
        ('Villa', 'Villa'),
        ('Ranch House', 'Ranch House'),
        ('Beach House', 'Beach House'),
        ('Hostel', 'Hostel'),
        ('Pent House', 'Pent House'),
        ('Bedsitter', 'Bedsitter'),
        ('Cabin', 'Cabin'),
        ('Castle', 'Castle'),
        ('Houseboats', 'Houseboats'),
        ('Ranch', 'Ranch'),
        ('Farm House', 'Farm House'),
        ('Office', 'Office'),
        ('Mall', 'Mall'),
        ('Store', 'Store'),
        ('Shop', 'Shop'),
        ('Hotel', 'Hotel'),
        ('Land', 'Land'),
        ('Plot', 'Plot'),
    ]

    property_owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    property_title = models.CharField(max_length=256)
    property_description = models.CharField(max_length=1024)
    property_about = models.TextField()
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
