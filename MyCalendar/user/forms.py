from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import MyUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['email', 'nick_name', 'password1', 'password2']


class UserAuthentificationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['email', 'password']

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                self.add_error("password", 'Wrong email or password')
                raise forms.ValidationError('Wrong email or password')
