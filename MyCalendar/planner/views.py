from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q

from .forms import PlannerForm, PlannerEditForm, PlanCreateForm, ItemForm
from .models import Planner, Plan
from .serializers import PlannerSerializer, PlanSerializer


# Create your views here.
@login_required
def homeView(request):
    context = {}
    createPlanForm = PlanCreateForm(initial={"user_id": request.user.pk, "owner": request.user})

    if "selected_planner" in request.GET:
        selected_planner = request.GET["selected_planner"]
        firstPlanner = True
    else:
        firstPlanner = Planner.objects.filter(owner=request.user).first()
        if firstPlanner:
            selected_planner = firstPlanner.planner_id

    # different function?
    if request.POST:
        if request.POST['action'] == 'create':
            form = PlannerForm(request.POST)
            if form.is_valid():
                form.set_owner(request.user)
                form.save()

        if request.POST['action'] == 'edit':
            form = PlannerEditForm(request.POST)
            if form.is_valid():
                form.save(commit=True)

        if request.POST['action'] == 'delete':
            planner = Planner.objects.get(planner_id=request.POST["planner_id"])
            if planner.owner == request.user:
                planner.delete()
                firstPlanner = Planner.objects.filter(owner=request.user).first()
                if firstPlanner:
                    selected_planner = firstPlanner.planner_id

        if request.POST['action'] == 'create_plan':
            form = PlanCreateForm(request.POST)
            if form.is_valid():
                form.set_planner(selected_planner)
                form.save()
                createPlanForm = PlanCreateForm()
            else:
                createPlanForm = form

    queryset_visible = Planner.objects.filter(Q(owner=request.user.pk) | Q(visible_for=request.user))
    queryset_editable = Planner.objects.filter(Q(owner=request.user.pk) | Q(editable_by=request.user))

    context["planners"] = PlannerSerializer(queryset_editable, many=True).data
    context["visible_planners"] = queryset_visible

    context["createform"] = PlannerForm()
    context["editform"] = PlannerEditForm(initial={"user_id": request.user.pk, "owner": request.user})

    if firstPlanner:
        context["selected_planner"] = int(selected_planner)

        planner = Planner.objects.get(planner_id=selected_planner)
        context["plans"] = PlanSerializer(planner.plan_set.all(), many=True).data

    context["plan_createform"] = createPlanForm
    return render(request, 'planner/home.html', context)


@login_required
def plansView(request, id):
    context = {}
    planner = Planner.objects.get(planner_id=id)
    context["plans"] = planner.plan_set.all()
    return render(request, 'planner/plans.html', context)

@login_required
def planView(request, id):
    context = {}
    plan = Plan.objects.get(plan_id=id)
    context["plan"] = plan
    context["create_item"] = ItemForm()
    return render(request, 'planner/plan.html', context)

@login_required
def add_item(request, id):
    return redirect('plan', id=id)