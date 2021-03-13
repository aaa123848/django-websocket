# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'ws_test/index.html')

def room(request, room_name):
    return render(request, 'ws_test/room.html', {
        'room_name': room_name
    })