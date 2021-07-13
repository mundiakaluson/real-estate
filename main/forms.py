from django.forms import ModelForm, Textarea, HiddenInput, TextInput
from .models import Property, Profile
from django.utils.translation import gettext_lazy as _
from django_countries.data import COUNTRIES
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
        error_messages = {
            'property_description': {
                'max_length': _('Max character are 1000 for this section!')
            }
        }
        widgets = {
            'property_about':
                Textarea(attrs = {
                    'rows': 10,
                    'cols': 40
                }),
            'property_owner':
                HiddenInput(), 
            'property_active':
                HiddenInput(),
            'property_post_date':
                HiddenInput(),
        }
        labels = {
            'property_pic1': '',
            'property_pic2': '',
            'property_pic3': '',
            'property_pic4': '',
            'property_pic5': '',
            'property_pic6': '',
            'property_pic7': '',
            'property_pic8': '',
            'property_location': 'Property Location'

        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'phone_number', 'country', 'profile_picture', 'region', 'registered_as']
        widgets = {
            'user': HiddenInput(),
            'phone_number': PhoneNumberPrefixWidget(),
        }
        labels = { 
            'phone_number': '',
            'country': '',
            'profile_picture': '',
            'region': '',
            'registered_as': ''
        }