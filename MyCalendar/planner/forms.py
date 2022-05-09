from django import forms
from django.db.models import Q

from user.models import MyUser
from .models import Planner, Plan, Item


class PlannerForm(forms.ModelForm):
    visible_for = forms.CharField(required=False)
    editable_by = forms.CharField(required=False)

    class Meta:
        model = Planner
        exclude=['owner', 'visible_for', 'editable_by']

    def set_owner(self, user):
        planner = self.instance
        planner.owner_id = user.pk
        self.instance = planner

    def save(self, commit=True):
        planner = self.instance

        planner.save() # will this destroy the code?

        for email in self.cleaned_data['visible_for'].split(','):
            if MyUser.objects.filter(email=email).exists():
                user = MyUser.objects.filter(email=email).get()
                planner.visible_for.add(user.pk)

        for email in self.cleaned_data['editable_by'].split(','):
            if MyUser.objects.filter(email=email).exists():
                user = MyUser.objects.filter(email=email).get()
                planner.editable_by.add(user.pk)

        if commit:
            planner.save()

        return planner


def get_planners(user_id):
    planners = Planner.objects.filter(Q(owner=user_id) | Q(editable_by=user_id))
    choices = []

    for planner in planners:
        choices.append((planner.pk, planner.name))

    return choices


class PlannerEditForm(forms.ModelForm):
    visible_for = forms.CharField(required=False)
    editable_by = forms.CharField(required=False)
    planner_id = forms.CharField(required=True)

    class Meta:
        model = Planner
        exclude = ['visible_for', 'editable_by']

    def __init__(self, *args, **kwargs):
        super(PlannerEditForm, self).__init__(*args, **kwargs)
        if self.initial:
            # get planners from user as choices for planners
            user_id = self.initial["user_id"]
            choices = get_planners(user_id)

            self.fields["planners"] = forms.ChoiceField(choices=choices, required=True)

    def save(self, commit=True):
        planner = Planner.objects.get(planner_id=self.cleaned_data["planner_id"])
        planner.name = self.cleaned_data["name"]
        planner.editable_by.clear()
        planner.visible_for.clear()

        for email in self.cleaned_data['visible_for'].split(','):
            if MyUser.objects.filter(email=email).exists():
                user = MyUser.objects.filter(email=email).get()
                planner.visible_for.add(user.pk)

        for email in self.cleaned_data['editable_by'].split(','):
            if MyUser.objects.filter(email=email).exists():
                user = MyUser.objects.filter(email=email).get()
                planner.visible_for.add(user.pk)

        if commit:
            planner.save()

        return planner


class PlanCreateForm(forms.ModelForm):

    start_date = forms.DateTimeField(input_formats=["%d.%m.%y %H:%M"], required=True)
    end_date = forms.DateTimeField(input_formats=["%d.%m.%y %H:%M"], required=False)

    def __init__(self, *args, **kwargs):
        super(PlanCreateForm, self).__init__(*args, **kwargs)
        if self.initial:
            # get planners from user as choices for planners
            user_id = self.initial["user_id"]
            choices = get_planners(user_id)

            self.fields["planner"] = forms.ChoiceField(choices=choices, required=True)

    def set_planner(self, planner_id):
        plan = self.instance
        plan.planner_id = planner_id
        self.instance = plan

    class Meta:
        model = Plan
        exclude = []


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = []