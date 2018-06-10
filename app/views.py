from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Room, RoomType, RoomAgree, Option, RoomStatus, Photo, University, Door
from .forms import RoomForm, FileFieldForm
from .get_geocode import Get_geocode
from . import constant


def room_list(request, university):
    rooms = Room.objects.filter(published_date__lte=timezone.now(), university__name_eng=university).order_by('published_date')
    universitys = University.objects.all()
    
    return render(request, 'app/room_list.html', {'rooms': rooms, 
                                                  'universitys': universitys,
                                                  'university_name': university 
                                                    })

def room_detail(request, university, pk):
    room = get_object_or_404(Room, pk=pk)
    photos = room.photo.all()
    options = [option.name for option in room.room_option.all()]
    university_lng = room.university.location_long
    university_lat = room.university.location_lat
    
    if room.location_long == '0':
        lng = room.door.location_long
        lat = room.door.location_lat
        print(lng, lat)    
    else:
        lng = room.location_long
        lat = room.location_lat
        print(lng, lat)

    return render(request, 'app/room_detail.html', {'room': room, 
                                                'photos': photos,
                                                'options': options,
                                                'lng': lng,
                                                'lat': lat,
                                                'university_lng': university_lng,
                                                'university_lat': university_lat, 
                                                'kakao_key': constant.API_KEY
                                                })

def main(request):
    return render(request, 'app/main.html', {})

@login_required(login_url='log_in')
def room_new(request, university):
    room_types = RoomType.objects.all()
    room_agrees = RoomAgree.objects.all()
    room_status = RoomStatus.objects.all()
    room_options = Option.objects.all()
    university_obj = University.objects.get(name_eng=university)
    gates = Door.objects.filter(university__name_eng=university) # 학교와 연결된 문 가져오기

    
    if request.method == "POST":
        user = User.objects.get(username=request.user.username)
        form = RoomForm(request.POST)
        print(form)
        print(request.FILES)
        files = FileFieldForm(request.FILES)
        file_list = request.FILES.getlist('file_field')

        if form.is_valid():
            print(form.cleaned_data)
            room = form.save(commit=False)
            room.user = user
            room.location_long = Get_geocode(request.POST['address'],constant.API_KEY)[0]
            room.location_lat = Get_geocode(request.POST['address'],constant.API_KEY)[1]
            room.created_date = timezone.now()
            room.published_date = timezone.now()
            room.university = university_obj
            room.save()
            for option in form.cleaned_data['room_option']: # 방 옵션을 저장 many-to-many라서 room 객체 사전에 저장 후 처리.
                room.room_option.add(option)
            room_obj= Room.objects.get(id=room.pk)
            for f in file_list:
                Photo.objects.create(image=f, rooms=room_obj)
            return redirect('room_detail', university=university, pk=room.pk)
    else:
        form = RoomForm()
        files = FileFieldForm()
    return render(request, 'app/room_edit.html', {
    'form': form,
    'files' : files,
    'room_types' : room_types,
    'room_agrees' : room_agrees,
    'room_status': room_status,
    'room_options': room_options,
    'gates': gates
    })


def room_edit(request, university, pk):
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
