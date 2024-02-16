from django.shortcuts import render
from .models import Room, Reservation
from datetime import datetime


# Create your views here.

today = datetime.today().strftime("%Y-%m-%d")


def index(request):
    rooms = Room.objects.all()
    status = {}

    for room in rooms:
        if room.reservation_set.filter(date=today):
            status[room.id] = "Sibuk"
        else:
            status[room.id] = "free"

            ctx = {
                "rooms": rooms,
                "status": status,
            }
            return render(request, "booking/index.html", ctx)

def room(request, id):
    id = int(id)
    room = Room.objects.get(pk=id)
    reservation = room.reservation_set.filter(date__gte=today).order_by('date')
    rooms = Room.objects.all()
    if room.projector == True:
        projector = "YA"
    else:
        projector = "TIDAK"
    ctx = {
        "room": room,
        "projector": projector,
        "rooms":rooms
    }
    
    return render(request, 'booking/room.html', ctx)

