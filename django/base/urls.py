# this urls is for specific app

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-form', views.createRoom, name="create-form"),
    path('update-form/<str:pk>/', views.updateRoom, name="update-form"),
]