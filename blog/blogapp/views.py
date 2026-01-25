from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):

    return render(request, 'home/home.html')

def register(request):



    return render(request, 'auth/register.html')


def login_view(request):



    return render(request, 'auth/login.html')

