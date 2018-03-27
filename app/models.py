from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class RoomType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class RoomAgree(models.Model):
    agreement = models.CharField(max_length=20)

    def __str__(self):
        return self.agreement

class RoomStatus(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status

class Option(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Door(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=50)
    door = models.ManyToManyField(Door)

    def __str__(self):
        return self.name

class Room(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    deposit_ori = models.IntegerField()
    rentfee_ori = models.IntegerField()
    deposit_new = models.IntegerField()
    rentfee_new = models.IntegerField()
    manage_fee = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    location_long = models.CharField(max_length=50)
    location_lat = models.CharField(max_length=50)
    date_start = models.DateField()
    date_end = models.DateField()
    room_type = models.ForeignKey(RoomType)
    room_agree = models.ForeignKey(RoomAgree)
    room_status = models.ForeignKey(RoomStatus)
    contact = models.CharField(max_length=50)
    room_option = models.ManyToManyField(Option)
    text = models.TextField(default=' ')
    university = models.ForeignKey(University)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
