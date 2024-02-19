from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    projector = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    room = models.ManyToManyField(Room)
    date = models.DateField()
    comment = models.TextField()

    def __str__(self):
        for r in self.room.all():
            return "Tarikh tempahan: {}, bilik: {}".format(self.date, r.name)
    
