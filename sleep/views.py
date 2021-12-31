from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Sleep
from .forms import SleepForm, TimeForm, NewDate
from django.contrib.auth.decorators import login_required
import datetime

from django.http import HttpResponse

from django.http import HttpResponse, JsonResponse
from django.http.response import HttpResponseRedirect,  HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def get_sleeps(request):
    if request.user.is_authenticated:
        e = Sleep.objects.get(user=request.user)
        response = {'s_counter': e.time, 's_username': e.user.username, 's_today': e.today}
        return JsonResponse(response)
    else:
        return JsonResponse({'s_username': ''})


@csrf_exempt
def reset_sleeps(request):
    if request.user.is_authenticated:
        e = Sleep.objects.get(user=request.user)
        e.time = 0
        if (datetime.date.today() != e.today):
            e.today = datetime.date.today()
        e.save()
        response = {'s_counter': e.time, 's_username': e.user.username}
        return JsonResponse(response)
    else:
        return JsonResponse({'s_username': ''})


@csrf_exempt
def post_sleeps(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if request.user.is_authenticated:
            e = Sleep.objects.get(user=request.user)
            if (datetime.date.today() != e.today):
                e.today = datetime.date.today()
                e.time = data["add"]
            else:
                e.time += data["add"]
                if e.time > 24:
                    e.time = 24
                elif e.time < 0:
                    e.time = 0

            e.save()
            response = {'s_counter': e.time, 's_username': e.user.username}
            return JsonResponse(response)
        else:
            return JsonResponse({'s_username': ''})


@login_required(login_url='/authentication/login/')
def mainpage_sleep(request):
    try:
        e = Sleep.objects.get(user=request.user)
        response = {'sleep': e}
        return render(request, 'mainpage_sleep.html', response)
    except:
        objNew = Sleep.objects.create()
        objNew.time = 0
        objNew.user = request.user
        objNew.today = datetime.datetime.now()
        objNew.save()
        response = {'sleep': objNew}
        return render(request, 'mainpage_sleep.html', response)


@login_required(login_url='/authentication/login/')
def new_sleep(request):
    context = {}
    sleep = Sleep.objects.get(user=request.user)
    form = NewDate(request.POST or None)

    if form.is_valid():
        sleep.today = form.cleaned_data['today']
        sleep.time = form.cleaned_data['time']
        sleep.save()
        return redirect('mainpage_s')

    context['form'] = form
    return render(request, "new_sleep.html", context)


@login_required(login_url='/authentication/login/')
def update_sleep(request):
    sleep = Sleep.objects.get(user=request.user)

    sleep.time = request.POST["time"]
    sleep.save()

    return HttpResponse(200)


@login_required(login_url='/authentication/login/')
def reset_sleep(request):
    sleep = Sleep.objects.get(user=request.user)

    sleep.time = 0
    sleep.save()

    return HttpResponse(200)
