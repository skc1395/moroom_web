from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Room, RoomType, RoomAgree, Option, RoomStatus,Photo
from .forms import RoomForm, FileFieldForm
from .get_geocode import Get_geocode
from . import constant


def room_list(request):
    rooms = Room.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/room_list.html', {'rooms':rooms})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    photos = room.photo.all()
    options = [option.name for option in room.room_option.all()]
    lng = room.location_long
    lat = room.location_lat
    return render(request, 'app/room_detail.html', {'room': room, 
                                                'photos': photos,
                                                'options': options,
                                                'lng': lng,
                                                'lat': lat,
                                                'kakao_key': constant.API_KEY
                                                })

def main(request):
    return render(request, 'app/main.html', {})


def input_data(request):
    return render(request, 'app/input_data.html', {})

@login_required(login_url='log_in')
def room_new(request):
    room_types = RoomType.objects.all()
    room_agrees = RoomAgree.objects.all()

    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        form = RoomForm(request.POST)
        files = FileFieldForm(request.FILES)
        file_list = request.FILES.getlist('file_field')

        if form.is_valid():
            room = form.save(commit=False)
            room.user = user
            room.location_long = Get_geocode(request.POST['address'],constant.API_KEY)[0]
            room.location_lat = Get_geocode(request.POST['address'],constant.API_KEY)[1]
            room.created_date = timezone.now()
            room.published_date = timezone.now()
            room.save()
            room_obj= Room.objects.get(id=room.pk)
            for f in file_list:
                Photo.objects.create(image=f, rooms=room_obj)
            return redirect('room_detail', pk=room.pk)
    else:
        form = RoomForm()
        files = FileFieldForm()
    return render(request, 'app/room_edit.html', {
    'form': form,
    'files' : files,
    'room_types' : room_types,
    'room_agrees' : room_agrees,
    })


def room_edit(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
            room = form.save(commit=False)
            room.user = user
            room.location_long = Get_geocode(request.POST['address'],constant.API_KEY)[0]
            room.location_lat = Get_geocode(request.POST['address'],constant.API_KEY)[1]
            room.created_date = timezone.now()
            room.published_date = timezone.now()
            room.save()
            room_obj= Room.objects.get(id=room.pk)
            for f in file_list:
                Photo.objects.create(image=f, rooms=room_obj)
            return redirect('room_detail', pk=room.pk)
    else:
        form = RoomForm(instance=room)
        files = FileFieldForm()

    return render(request, 'app/room_edit.html', {
    'form': form,
    'files' : files,
    })

def tutorial(request):
    return render(request, 'app/tutorial.html', {})
