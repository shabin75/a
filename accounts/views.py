from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from .forms import ImageForm
from .models import Image
from .location import Location
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def indexView(request):
    return render(request, 'index.html')


@login_required
def dashboardView(request):
    return render(request, 'dashboard.html')


def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    latlon = []
    for x in img:
        print(type(x.photo), "aaaaaaaaaaaaaaaaaaaaaaaaa")
        latlon.append(Location.location(x.photo))
    return render(request, 'myapp/home.html', {'img': img, 'form': form, 'latlon': latlon})


def registerView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')

    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def test(request):
    return render(request, 'login.html')


def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('accounts:home_url')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('accounts:login_url')


def register_view(request):
    if request.method =='POST':
        First_name = request.POST.get('fname')
        Last_name = request.POST.get('lname')
        user_name = request.POST.get('uname')
        email = request.POST.get('email')
        password1 = request.POST.get('p1')
        password2 = request.POST.get('p2')

        if password1 == password2:
            if User.objects.filter(username=user_name).exists() or User.objects.filter(email=email).exists():
                return render(request, 'register.html')

            else:
                User.objects.create_user(first_name=First_name, last_name=Last_name, username=user_name, password=password1,
                                         email=email)
                return redirect('accounts:login_url')
        else:
            return render(request, 'register.html')

    else:
        return render(request, 'register.html')