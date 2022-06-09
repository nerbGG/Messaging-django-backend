from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# from multiselectfield import MultiSelectField

# stores messages between 2 (or more) people
class Room(models.Model):
    # one room can have many users, and each user can be in multiple rooms
    users = models.ManyToManyField(User, blank=True) # room.add(user), user.rooms.add(room)
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(default=datetime.now)

    # one room can have many messages from users in that room
    def __str__(self):
        return "%s's " % self.name


# Create your models here.
class Message(models.Model):
    text = models.TextField(max_length=1500, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_sent = models.DateTimeField(default=datetime.now, blank=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "%s's message %d" % (self.author.username, self.id)

# class MessageThrough(models.Model):
#     message = models.OneToOneField(Message, on_delete=models.CASCADE)

# def __str__(self):
#     return "%d" % ( self.id)
