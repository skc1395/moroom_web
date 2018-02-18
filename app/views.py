from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Room, RoomType, RoomAgree, Option
from .forms import RoomForm

def room_list(request):
    rooms = Room.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/room_list.html', {'rooms':rooms})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'app/room_detail.html', {'room': room})

def main(request):
    return render(request, 'app/main.html', {})

def room_input(request):
    return render(request, 'app/room_input.html', {})

def input_data(request):
    return render(request, 'app/input_data.html', {})

def room_new(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.created_date = timezone.now()
            room.published_date = timezone.now()
            room.save()
            return redirect('room_detail', pk=room.pk)
    else:
        form = RoomForm()
    return render(request, 'app/room_edit.html', {'form': form})

def room_edit(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            room = form.save(commit=False)
            room.created_date = timezone.now()
            room.published_date = timezone.now()
            room.save()
            return redirect('room_detail', pk=room.pk)
    else:
        form = RoomForm(instance=room)
    return render(request, 'app/room_edit.html', {'form': form})
