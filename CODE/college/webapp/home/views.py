from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
import requests
from .models import *
from django.http import JsonResponse
import random
from datetime import datetime
from datetime import timedelta
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    user = request.user
    u = User.objects.filter(username=user.username)[0]
    today = datetime.today()
    date = today.strftime("%d-%m-%Y")
    print(date)
    r = Reminder.objects.filter(alarm=date, user=u)
    print(r)
    return render(request, "home/index.html", {'data': r})


def GetCollegeAdd(request):
    add_details = Branch.objects.all()
    js = list(add_details.values())
    return JsonResponse(js, safe=False)


def GetCollegePlacements(request):
    placement = placements.objects.all()
    js = list(placement.values())
    return JsonResponse(js, safe=False)


def getInfra(request):
    infra = AboutCollege.objects.all()
    return JsonResponse(infra[0].infra, safe=False)


def getHostelfees(request):
    infra = AboutCollege.objects.all()
    return JsonResponse(infra[0].hostel, safe=False)


def getcolEnv(request):
    infra = AboutCollege.objects.all()
    return JsonResponse(infra[0].env, safe=False)


def getcolach(request):
    infra = AboutCollege.objects.all()
    return JsonResponse(infra[0].achievements, safe=False)


def getcolnaac(request):
    infra = AboutCollege.objects.all()
    return JsonResponse(infra[0].naac, safe=False)


def getcolnirf(request):
    infra = AboutCollege.objects.all()
    return JsonResponse(infra[0].NIRF, safe=False)

def setReminder(request):
    user = request.GET['user']
    u = User.objects.filter(username=user)[0]
    date = request.GET['date']
    event = request.GET['event']
    r = Reminder(user= u, alarm=date, Event=event)
    r.save()
    return JsonResponse("Reminder Set", safe=False)

def sendReminder(request):
    user = request.user
    u = User.objects.filter(username=user.username)[0]
    today = datetime.today()
    date = today.strftime("%d-%m-%Y")
    r = Reminder.objects.filter(alarm=date, user=u)
    rjs = list(r.values())
    return JsonResponse(rjs, safe=False)

def home(request):
    return render(request, 'home/homepage.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return render(request, 'home/signup.html', {'data': 'Signup Successful'})
    return render(request, 'home/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'home/signin.html', {'data': 'Signin Failed'})
    return render(request, 'home/signin.html')


def lgt(request):
    logout(request)
    return redirect('home')