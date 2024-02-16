from django.urls import path
from . import views



urlpatterns = [
    path('room/', views.index, name='home'),
    path('room/<str:pk>/', views.room, name='room'),

]