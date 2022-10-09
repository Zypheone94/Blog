from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from .forms import SignupForm, ConnectForm
from blog_post.models import Post


def index(request):
    posts = Post.objects.order_by('-date')[:5]
    top = []
    posts = list(posts)

    for i in range(1):
        top.append(posts.pop(0))

    username = ""
    is_auth = ""
    if request.user.is_authenticated:
        username = request.user.username
        is_auth = True
    else :
        username = "null"
        is_auth = False
    for i in posts:
        if i.mainImage == 'Null':
            print('lala')
        print(i.mainImage)
    return render(request, 'Blog/index.html', context={'username': username, 'is_auth' : is_auth, 'posts': posts, 'top': top})

def post(request, id):
    myPost = get_object_or_404(Post, pk=id)
    return render(request, 'Blog/post.html', context={'post': myPost})

def userBoard(request, id):
    print(type(id), type(request.user.id))
    if request.user.id == int(id):
        user = get_object_or_404(User, id=id)
        articles = Post.objects.filter(author_id=id).order_by('-date')[:5]
        print(articles)
        return render(request, 'user/userBoard.html', context={'user': user, 'articles': articles})
    else:
        return render(request, 'user/badUser.html')

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
        form = ConnectForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'connect.html', context={"form": form, "invalide": True})
    return render(request, 'connect.html', context={"form": form, 'invalide': False})

def logout_view(request):
    logout(request)
    return redirect('home')