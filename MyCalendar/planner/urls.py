from django.urls import path

from planner import views

urlpatterns = [
    path('home', views.homeView, name='home'),
    path('plans/<int:id>/', views.plansView, name='plans'),
    path('plan/<int:id>/', views.planView, name='plan'),
    path('plan/<int:id>/add_item', views.planView, name='add_item')
]