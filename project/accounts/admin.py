from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

from .models import *
# Register your models here.
@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_per_page = 3
    list_display = ('user', 'created', 'profile_photo', 'bio')
    list_filter = ['user']
    search_fields = ['user']
    prepopulated_fields = {'slug': ('user',)}
    date_hierarchy = 'created'
    ordering = ['-created']

    def profile_photo(self, object):
        if object.avatar:
            return mark_safe(f"<img src='{object.avatar.url}' width=80>")
