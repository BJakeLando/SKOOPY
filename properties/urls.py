from django.contrib import admin
from django.urls import path
from .views import (
    home,
    all_properties,

)

urlpatterns = [
    path('', home, name='home'),
    path('properties', all_properties, name='properties'),

]