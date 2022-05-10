from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Event, Mission, Category, Goal
from .forms import MissionForm, GoalForm, CategoryForm
from django.views.generic import UpdateView


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


def goalsView(request):
    context = {}
    context['goals'] = Goal.objects.filter(owner=request.user)

    return render(request, 'account/goals.html', context)


def goalFormView(request):
    context = {}
    context['goal_form'] = GoalForm()
    if "goal" in request.GET:
        goal = Goal.objects.filter(goal_id=request.GET['goal']).first()
        info = {'title': goal.title, 'description': goal.description, 'category': goal.category}
        context['goal_form'] = GoalForm(info)

    return render(request, 'account/goal_form.html', context)


def add_goal(request):
    if request.method == 'POST':
        goal_form = GoalForm(request.POST)
        if goal_form.is_valid():
            title = goal_form.cleaned_data['title']
            goal = Goal.objects.filter(title=title).first()
            if goal is None:
                goal = Goal(owner=request.user, title=title)
            goal.description = goal_form.cleaned_data['description']
            goal.category = goal_form.cleaned_data['category']
            goal.save()
    return redirect('goals')


def check_goal(request, id):
    goal = Goal.objects.filter(goal_id=id).first()
    goal.done = True
    goal.save()
    return redirect('goals')


def category(request):
    context = {}
    context['category_form'] = CategoryForm()
    print(context)
    return render(request, 'account/category.html', context)


def add_category(request):
    context = {}
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            urgency_level = form.cleaned_data['urgency_level']
            category = Category.objects.filter(name=name).first()
            if category is None:
                category = Category(name=name, urgency_level=urgency_level)
            category.save()
            return redirect('goals')
        else:
            context['category_form'] = form
    else:
        context['category_form'] = CategoryForm()
    return render(request, 'account/category.html', context)