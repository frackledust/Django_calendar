from django.contrib import admin

from .models import Planner, Plan, Item

admin.site.register(Planner)
admin.site.register(Plan)
admin.site.register(Item)