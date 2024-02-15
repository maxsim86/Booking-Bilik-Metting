from django.urls import path
from . import views



urlpatterns = [
    path('room/', views.room_list, name='room_list'),
    path('reservation/', views.make_reservation, name='make_reservations'),

]