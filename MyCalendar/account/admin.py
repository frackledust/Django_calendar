from django.contrib import admin
from .models import Event, Mission, Category, Goal

admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Mission)
admin.site.register(Goal)