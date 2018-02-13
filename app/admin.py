from django.contrib import admin
from .models import Room, RoomType, RoomAgree, Option

# Register your models here.
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(RoomAgree)
admin.site.register(Option)
