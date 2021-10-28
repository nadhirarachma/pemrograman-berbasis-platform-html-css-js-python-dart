from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Sleep
from .forms import SleepForm, TimeForm, NewDate
from django.contrib.auth.decorators import login_required
import datetime

from django.http import HttpResponse

# Create your views here.


@login_required(login_url='/authentication/login/')
def mainpage_sleep(request):
    e = Sleep.objects.get(user=request.user)
    response = {'sleep': e}
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
    context = {}
    sleep = Sleep.objects.get(user=request.user)
    form = TimeForm(request.POST or None)

    if form.is_valid():
        sleep.time += form.cleaned_data['time']
        sleep.save()
        return redirect('mainpage_s')

    context['form'] = form
    return render(request, "update_sleep.html", context)
