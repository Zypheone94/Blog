from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import SignupForm, ConnectForm


def index(request):
    username = ""
    is_auth = ""
    if request.user.is_authenticated:
        username = request.user.username
        is_auth = True
        print(username)
    else :
        username = "null"
        is_auth = False



    return render(request, 'Blog/index.html', context={'username': username, 'is_auth' : is_auth})

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            staff = 0
            super = 0
            pseudo = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = make_password(form.cleaned_data['password'], salt="coucou")

            user = User(username=pseudo, first_name=first_name, last_name=last_name, password=password, is_staff=staff, is_superuser=super, email=email)
            user.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'signup.html', context={"form": form})

def connect(request):
    form = ConnectForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = authenticate(username='magna', password="Zypheone94")
            if user is not None:
                login(request, user)