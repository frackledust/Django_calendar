from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from user import views

urlpatterns = [
    path('', views.loginView, name='login'),
    path('reg', views.registrationView, name='registration'),
    path('logout', views.logoutView, name='logout'),

    path('account/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='user/registration/password_change_done.html'),
         name='password_change_done'),

    path('account/password_change/', auth_views.PasswordChangeView.as_view(template_name='user/registration/password_change.html'),
         name='password_change'),

    path('account/password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='user/registration/password_reset_done.html'),
         name='password_reset_done'),

    path('account/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('account/password_reset/', auth_views.PasswordResetView.as_view(template_name='user/registration/password_reset_form.html'), name='password_reset'),

    path('account/reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='user/registration/password_reset_complete.html'),
         name='password_reset_complete'),
]