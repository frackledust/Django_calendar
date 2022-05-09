from django.urls import path

from account import views

urlpatterns = [
    path('goals', views.goalsView, name='goals'),
    path('goal_form', views.goalFormView, name='goal_form'),
    path('add_goal', views.add_goal, name='add_goal'),
    path('check_goal/<int:id>', views.check_goal, name='check_goal'),

    path('', views.index, name='index'),
    path('event/<int:id>/', views.event, name='event'),
    path('event/<int:id>/add_mission', views.add_mission, name='add_mission'),
]