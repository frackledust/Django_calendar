from django import forms
from .models import Mission, Goal, Category
from user.models import MyUser


class GoalForm(forms.ModelForm):

    class Meta:
        model = Goal
        exclude = ['owner']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = []