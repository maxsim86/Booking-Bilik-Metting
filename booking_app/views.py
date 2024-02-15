from django.shortcuts import render
from .models import Room, Booking
# Create your views here.

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'booking/room_list.html', {'room':rooms})


def make_reservation(request):
    if request.method == 'POST':
        pass
    else:
        pass