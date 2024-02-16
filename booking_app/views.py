from django.shortcuts import render, redirect
from .models import Room, Reservation
from datetime import datetime
from django.views import View


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


class NewRoomView(View):
    def get(self, request):
        
        try:
            name = request.POST.get("name")
            capacity = request.POST.get("capacity")
            projector = request.POST.get("projector")
            proj = True if projector == 'True' else False
            
            Room.objects.create(name=name, capacity=capacity, projector=proj)

            return redirect("/bookconfroom/")
        except Exception as e:
            message = "Data tidak betul: {}".format(e)
            ctx = {
                "message":message,
            }
            return render(request, "booking/new_room.html", ctx)

class ModifyView(View):
    def get(self, request, id):
        room = Room.objects.get(pk=id)
        ctx = {
            "room": room,
        }
        return render(request, 'booking/modify.html', ctx)
    
    def post(self, request, id):
        name = request.POST.get("name")
        capacity = request.POST.get("capacity")
        projector = True if request.POST.get('projector') else False
        room = Room.objects.get(pk=id)
        try:
            room.name =name
            room.capacity = capacity
            room.projector = projector
            room.save()
            return redirect('/bookconfroom')
        except Exception as e:
            message = "Data tidak betul: {}".format(e)
            ctx = {
                "message": message,
                "room": room,
            }
            return render(request, 'booking/modify.html', ctx)
        
class DeleteView(View):
    def get(self, request, id):
        room = Room.objects.get(pk=id)
        ctx = {
            "room":room,
        }
        return render(request, 'booking/delete.html', ctx)

    def post(self, request, id):
        action = request.POST.get('submit')

        if action == "YA":
            room = Room.objects.get(pk=id)
            room.delete()

        return redirect("/bookconfroom")

