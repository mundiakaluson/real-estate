from django.contrib import admin
from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    readonly_fields = ['property_post_date',]
    list_display = ['id', 'property_post_date', 'property_title', 'property_owner', 'property_location', 'property_price', 'property_condition', 'property_status', 'property_posted_by']
    list_filter = ['property_post_date', 'property_owner', 'property_location', 'property_price', 'property_condition', 'property_status', 'property_posted_by']
    actions = ['approve_property', 'dissaprove_property']

    def approve_property(self, request, queryset):
        queryset.update(property_active=True)

    def dissaprove_property(self, request, queryset):
        queryset.update(property_active=False)

admin.site.register(Property, PropertyAdmin)