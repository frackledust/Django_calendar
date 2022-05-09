from django.urls import path

from planner import views

urlpatterns = [
    path('home', views.homeView, name='home'),
]