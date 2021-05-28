from django.contrib import admin
from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    readonly_fields = ['property_post_date',]
    list_display = ['id', 'property_post_date', 'property_title', 'property_owner', 'property_location', 'property_price', 'property_condition', 'property_status', 'property_posted_by']

admin.site.register(Property, PropertyAdmin)