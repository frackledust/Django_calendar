from django.contrib import admin
from .models import Event, Mission, Category

# Register your models here.
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Mission)