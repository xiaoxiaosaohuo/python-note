from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Room
from .form import RoomForm


# define route


def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html',{'rooms':rooms})


def room(request,pk):
    room = None
    room = Room.objects.get(id=pk)
   
    context = {'room':room}
    return render(request, 'base/room.html',context)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
       form = RoomForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('home')
   

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def updateRoom (request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)