from django.forms import ModelForm, Textarea
from .models import Property
from django.utils.translation import gettext_lazy as _
from material import Layout, Row, Fieldset, Column

class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
        """error_messages = {
            'property_description': {
                'max_length': _('Max character are 1000 for this section!')
            }
        }
        widgets = {
            'property_about':
                Textarea(attrs = {
                    'rows': 10,
                    'cols': 40
                })
        }"""

        layuot = Layout(
            Row(
                'property_title', 'property_price'
            ),
            'property_description', 'property_about'
        )

        """
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Row(
                    Column(
                        'property_title', css_class='form-group col-md-6 mb-0'
                    ),
                    Column(
                        'property_price', css_class='form-group col-md-6 mb-0'
                    ),
                    css_class='form-row'
                    ),
                    'property_description',
                    'property_about',
                
                Row(
                    Column(
                        'property_location', css_class='form-group col-md-6 mb-0'
                    ),
                    Column(
                        'property_condition', css_class='form-group col-md-4 mb-0'
                    ),
                    Column(
                        'property_status', css_class='form-group col-md-2 mb-0'
                    ),
                    css_class='form-row'
                    ),

                )
                """
