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

class University(models.Model):
    """
    name_eng : 대학교 영어명(url로 이용됨) -> 학교 약자가 아님 전체이름으로 사용 ex. 경북대학교 -> kyungpook
    name_kor : 대학교 이름
    address : 중앙 좌표에 대한 주소값을 저장한다.
    location : 학교의 중앙 좌표값을 저장한다.
    """
    name_eng = models.CharField(max_length=50)
    name_kor = models.CharField(max_length=50)
    address = models.CharField(max_length=100, default="")
    location_long = models.CharField(max_length=50)
    location_lat = models.CharField(max_length=50)


    def __str__(self):
        return self.name_kor

class Door(models.Model):
    """
    name : 문 이름(학교마다 동일한 이름이 존재할 수 있음) 경북대학교 - 동문
    address : 문에 대한 주소를 검색
    location : 문 부근의 좌표 저장
    * 사용자가 방 정보를 입력시에 주소값이 올바르지 않으면 잘못된 좌표값 요청
      따라서, 잘못된 값을 가지고 있을시(0,0) 문의 좌표값으로 방의 위치를 대체함.
    """
    name = models.CharField(max_length=30)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default="")
    location_long = models.CharField(max_length=50)
    location_lat = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Room(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    deposit = models.IntegerField()
    rentfee = models.IntegerField()
    fee_new = models.CharField(max_length=50)
    manage_fee = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    location_long = models.CharField(max_length=50) # 방이 위치한 좌표.
    location_lat = models.CharField(max_length=50) # 방이 위치한 좌표.
    date_start = models.DateField()
    date_end = models.DateField()
    room_type = models.ForeignKey(RoomType)
    room_agree = models.ForeignKey(RoomAgree)
    room_status = models.ForeignKey(RoomStatus)
    contact = models.CharField(max_length=50)
    room_option = models.ManyToManyField(Option)
    text = models.TextField(default=' ')
    university = models.ForeignKey(University)
    door = models.ForeignKey(Door)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Photo(models.Model):
    image = models.ImageField()
    rooms = models.ForeignKey(Room, related_name='photo')

    def __str__(self):
        return '{0} - {1}'.format(self.rooms.title, self.image)