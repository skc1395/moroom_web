from django.shortcuts import render

def room_list(request):
    return render(request, 'app/room_list.html', {})
