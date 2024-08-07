from django.shortcuts import render
from .models import Property

# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def all_properties(request):
    property_list = Property.objects.all()
    return render(request, 'properties.html', 
                  {'property_list': property_list} )