from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    projector = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.TextField(null=True)

    def __str__(self):
        return self.comment
    
