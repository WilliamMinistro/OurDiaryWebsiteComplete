from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime


def login(request):
    return render(request, 'accounts/login.html')


# Create your views here.

