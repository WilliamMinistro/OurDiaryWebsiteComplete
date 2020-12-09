from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Info
from .forms import InfoForm
from django.contrib.auth.models import User
import time
import random


# Create your views here.
@login_required(login_url='register')
def home(request):
    return render(request, 'myDiary/home.html')

@login_required(login_url='register')
def delete(request, id):
    entry = Info.objects.get(id=id)
    if request.method == 'POST':
        entry.delete()
        return redirect('diary2')
    return render(request, 'myDiary/delete.html', {'entry': entry})

@login_required(login_url='register')
def pics(request):
    entries = Info.objects.all()
    count = Info.objects.all().count()
    value = random.randint(1, count)
    if request.method == "POST":
        entry = InfoForm(request.POST or None)
        entries = Info.objects.all()
        count = Info.objects.all().count()
        value = random.randint(1, count)
        if entry.is_valid():
            entry.save()
        context = {'entries': entries}
        return render(request, 'myDiary/pics.html', {'entries': entries, 'rand': value})
    else:
        context = {'entries': entries}
        return render(request, 'myDiary/pics.html', {'entries': entries, 'rand': value})

@login_required(login_url='register')
def diary(request):
    entries = Info.objects.all()
    if request.method == "POST":
        entry = InfoForm(request.POST or None)
        entries = Info.objects.all()
        count = Info.objects.all().count()
        value = random.randint(0, count)
        if entry.is_valid():
            entry.save()
        time.sleep(2)
        context = {'entries': entries}
        return render(request, 'myDiary/diary.html', {'entries': entries})
    else:
        context = {'entries': entries}
        return render(request, 'myDiary/diary.html', {'entries': entries})

@login_required(login_url='register')
def diary2(request):
    entries2 = Info.objects.all()
    if request.method == "POST":
        entry = InfoForm(request.POST or None)
        entries = Info.objects.all()
        if entry.is_valid():
            entry.save()
        context = {'entries': entries2}
        return render(request, 'myDiary/myDiary.html', context)
    else:
        context = {'entries': entries2}
        return render(request, 'myDiary/myDiary.html', context)


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('register')
