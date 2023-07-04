from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn python'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'},
    {'id': 4, 'name': 'Backend developers'},
    {'id': 5, 'name': 'Fullstack developers'},
   
]
# define route


def home(request):
    return render(request, 'base/home.html',{'rooms':rooms})


def room(request):
    return render(request, 'base/room.html')
