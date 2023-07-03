from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# define route


def home(request):
    return HttpResponse("Hello World")


def room(request):
    return HttpResponse("Room")
