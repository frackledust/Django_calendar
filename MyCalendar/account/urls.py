from django.urls import path

from account import views

urlpatterns = [
    path('profil', views.profilView, name='profil'),

    path('goals', views.goalsView, name='goals'),

    path('category', views.category, name='category'),
    path('add_category', views.add_category, name='add_category'),

    path('goal_form', views.goalFormView, name='goal_form'),
    path('add_goal', views.add_goal, name='add_goal'),
    path('check_goal/<int:id>', views.check_goal, name='check_goal'),
]