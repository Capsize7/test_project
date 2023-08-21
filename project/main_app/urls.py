from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'main_app'

urlpatterns = [
    path('main/', main_page, name='main'),
    path('load_file/', load_file, name='load_file'),
    path('logs_file/<slug:file_slug>/', logs_file, name='logs_file'),
    path('update_file/<slug:file_slug>/', update_file, name='update_file'),
    path('update_file/<slug:file_slug>/<str:delete>/', update_file, name='delete_file')


]
