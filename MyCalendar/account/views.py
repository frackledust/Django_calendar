from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Event, Mission, Category
from .forms import MissionForm


def index(request):
    events = Event.objects.all()
    return render(request, 'account/index.html', {'events': events})


def event(request, id):
    event = get_object_or_404(Event, pk=id)
    missions = Mission.objects.filter(event=event)

    mission_form = MissionForm()

    return render(request, 'account/event.html', {'event': event, 'missions': missions, 'mission_form': mission_form})


def add_mission(request, id):
    event = get_object_or_404(Event, pk=id)
    if request.method == 'POST':
        mission_form = MissionForm(request.POST)
        if mission_form.is_valid():
            text = mission_form.cleaned_data['text']
            category = mission_form.cleaned_data['category']
            mission = Mission(event=event, text=text, category=category)
            mission.save()
    return redirect('event', id=id)