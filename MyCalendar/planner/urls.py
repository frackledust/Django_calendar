from django.urls import path

from planner import views

urlpatterns = [
    path('home', views.homeView, name='home'),
    path('planner/<int:id>/plans/', views.plansView, name='plans'),
    path('planner/<int:planner_id>/delete/<int:plan_id>/', views.plan_delete, name='plan_delete'),
    path('planner/<int:planner_id>/plan/<int:plan_id>/', views.planView, name='plan'),
    path('planner/<int:planner_id>/plan/<int:plan_id>/add_item', views.add_item, name='add_item')
]