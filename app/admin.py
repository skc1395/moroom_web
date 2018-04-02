from django.contrib import admin
from .models import Room, RoomType, RoomAgree, Option, University, Door, RoomStatus, Photo

# Register your models here.

admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(RoomAgree)
admin.site.register(Option)
admin.site.register(University)
admin.site.register(Door)
admin.site.register(RoomStatus)
admin.site.register(Photo)
