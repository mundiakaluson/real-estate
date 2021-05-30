from django.contrib import admin
from .models import Property, PageView, UserInformation


class PropertyAdmin(admin.ModelAdmin):
    readonly_fields = ['property_post_date',]
    list_display = ['id', 'property_post_date', 'property_title', 'property_owner', 'property_location', 'property_price', 'property_condition', 'property_status', 'property_posted_by']
    list_filter = ['property_post_date', 'property_owner', 'property_location', 'property_price', 'property_condition', 'property_status', 'property_posted_by', 'property_active']
    actions = ['approve_property', 'dissaprove_property']

    def approve_property(self, request, queryset):
        queryset.update(property_active=True)

    def dissaprove_property(self, request, queryset):
        queryset.update(property_active=False)

class PageViewAdmin(admin.ModelAdmin):
    readonly_fields = ['viewer', 'property_viewed', 'view']
    list_display = ['viewer', 'property_viewed', 'view']

class UserInformationAdmin(admin.ModelAdmin):
    readonly_fields = ['visitor', 'city', 'continent_code', 'continent_name', 'country_code', 'country_name', 'dma_code', 'is_in_european_union', 'latitude', 'longitude', 'postal_code', 'region', 'time_zone']
    list_display = ['visitor', 'city', 'country_name', 'latitude', 'longitude', 'time_zone']

admin.site.register(Property, PropertyAdmin)
admin.site.register(PageView, PageViewAdmin)
admin.site.register(UserInformation, UserInformationAdmin)