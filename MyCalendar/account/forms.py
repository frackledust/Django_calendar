from django import forms
from .models import Mission, Goal


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        exclude = ['event','done']


class GoalForm(forms.ModelForm):

    class Meta:
        model = Goal
        exclude = ['owner']
