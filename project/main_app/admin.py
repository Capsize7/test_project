from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

# Register your models here.
@admin.register(File)
class File(ModelAdmin):
    list_per_page = 5
    list_display = ('author', 'name', 'file', 'created', 'updated', 'status')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['author']
    search_fields = ['author']
    date_hierarchy = 'created'
    ordering = ['-created']


@admin.register(Log)
class Log(ModelAdmin):
    list_per_page = 5
    list_display = ('file', 'created', 'description', 'send')
    list_filter = ['file']
    search_fields = ['file']
    date_hierarchy = 'created'
    ordering = ['-created']
