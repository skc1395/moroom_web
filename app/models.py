from django.db import models

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
    deposit_ori = models.IntegerField()
    rentfee_ori = models.IntegerField()
    deposit_new = models.IntegerField()
    rentfee_new = models.IntegerField()
    manage_fee = models.CharField(max_length=30)
    date_start = models.DateField()
    date_end = models.DateField()
    room_type = models.ForeignKey(RoomType)
    room_agree = models.ForeignKey(RoomAgree)
    room_option = models.ManyToManyField(Option)

    def __str__(self):
        return self.title
