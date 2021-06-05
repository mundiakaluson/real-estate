from django.contrib import admin
from .models import (
    Property, 
    PageView, 
    UserInformation,
    Review, 
    Article,
    Profile
)
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

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

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ['reviewed_user', 'comment_reviewed', 'rating_reviewed', 'average_review', 'date_reviewed']
    list_display = ['reviewed_user', 'rating_reviewed', 'average_review', 'date_reviewed']

class ArticleAdmin(admin.ModelAdmin):
    pass

class ProfileInline(admin.StackedInLine):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    
    def gef_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.register(Property, PropertyAdmin)
admin.site.register(PageView, PageViewAdmin)
admin.site.register(UserInformation, UserInformationAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)