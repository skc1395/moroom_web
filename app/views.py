from django.shortcuts import render
from django.utils import timezone
from .models import Room, RoomType, RoomAgree, Option

def room_list(request):
    rooms = Room.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/room_list.html', {'rooms':rooms})
