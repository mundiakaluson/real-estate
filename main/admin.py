from django.contrib import admin
from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Property)