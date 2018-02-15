from django.db import models
from django.utils import timezone

# Create your models here.

class RoomType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class RoomAgree(models.Model):
    agreement = models.CharField(max_length=20)

    def __str__(self):
        return self.agreement

class Option(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Room(models.Model):
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    deposit_ori = models.IntegerField()
    rentfee_ori = models.IntegerField()
    deposit_new = models.IntegerField()
    rentfee_new = models.IntegerField()
    manage_fee = models.CharField(max_length=30)
    date_start = models.DateField()
    date_end = models.DateField()
    room_type = models.ForeignKey(RoomType)
    room_agree = models.ForeignKey(RoomAgree)
    contact = models.CharField(max_length=50)
    room_option = models.ManyToManyField(Option)
    text = models.TextField(default=' ')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
