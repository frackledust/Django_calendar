from django.contrib import admin

# Register your models here.
from .models import Planner, Plan

admin.site.register(Planner)
admin.site.register(Plan)