from django.db import models
from datetime import datetime

# Create your models here.

class MeetingRoom(models.Model):
    room_name = models.CharField(max_length=100)

    def __str__(self):
        return self.room_name

class User(models.Model):
    username = models.CharField(max_length=50)
    
SERVICE_CHOICES = (
    ("Doctor care", "Doctor care"),
    ("Nursing care", "Nursing care"),
    ("Medical social services", "Medical social services"),
    ("Homemaker or basic assistance care", "Homemaker or basic assistance care"),
    )
    
TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)

class Booking(models.Model):
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Doctor care")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="3 PM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"