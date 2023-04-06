from django.shortcuts import render
from .models import Poject

def home(request):
    projects = Poject.objects.all()
    return  render(request, 'home.html', {'projects': projects})