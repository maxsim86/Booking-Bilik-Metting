from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.PositiveIntegerField()

    
    def __str__(self):
        return self.name

class Booking(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    organizer_name = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    comment = models.TextField(null=True)
    
