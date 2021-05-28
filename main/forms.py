from django.forms import ModelForm, Textarea, HiddenInput
from .models import Property
from django.utils.translation import gettext_lazy as _
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
                HiddenInput()
        }
