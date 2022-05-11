from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Category, Goal
from .forms import GoalForm, CategoryForm


@login_required
def profilView(request):
    context = {'user': request.user}
    return render(request, 'account/profil.html', context)


@login_required
def goalsView(request):
    context = {'goals': Goal.objects.filter(owner=request.user)}

    return render(request, 'account/goals.html', context)


@login_required
def goalFormView(request):
    context = {'goal_form': GoalForm()}
    if "goal" in request.GET:
        goal = Goal.objects.filter(goal_id=request.GET['goal']).first()
        info = {'title': goal.title, 'description': goal.description, 'category': goal.category}
        context['goal_form'] = GoalForm(info)

    return render(request, 'account/goal_form.html', context)


@login_required
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


@login_required
def check_goal(request, id):
    goal = Goal.objects.filter(goal_id=id).first()
    goal.done = True
    goal.save()
    return redirect('goals')


@login_required
def category(request):
    context = {'category_form': CategoryForm()}
    print(context)
    return render(request, 'account/category.html', context)

@login_required
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