from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserAuthentificationForm, RegistrationForm


# Create your views here.
def loginView(request):
    context = {}
    if request.POST:
        form = UserAuthentificationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')

    else:
        form = UserAuthentificationForm()

    context['form'] = form
    return render(request, 'user/login.html', context)


def logoutView(request):
    logout(request)
    return redirect("login")


def registrationView(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()

    context['form'] = form
    return render(request, 'user/registration.html', context)