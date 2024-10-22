from django.shortcuts import render
from .models import Room
from django.views.generic.detail import DetailView

# Create your views here.


def home(request):
    rooms = Room.objects.all()
    return render(request, 'chat/home.html', {
        'rooms': rooms
    })


class RoomDetailView(DetailView):
    model = Room
    template_name = 'chat/list-messages.html'
