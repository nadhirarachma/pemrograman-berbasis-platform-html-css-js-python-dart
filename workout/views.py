from django.shortcuts import render, redirect
from .models import Exercise
from .forms import ExerciseForm, TimeForm, NewDate
from django.contrib.auth.decorators import login_required
import datetime

from django.http import HttpResponse

# Create your views here.
@login_required(login_url='/authentication/login/')
def workout_page(request):
    e = Exercise.objects.get(user=request.user)
    if (datetime.date.today() != e.today):
        e.today = datetime.date.today()
        e.time = 0
        e.save()
    response = {'exercise': e}
    return render(request, 'workout_page.html', response)

@login_required(login_url='/authentication/login/')
def new_workout(request):
    context = {}
    exercise = Exercise.objects.get(user=request.user)
    form = NewDate(request.POST or None)


    if form.is_valid():
        exercise.today = form.cleaned_data['today']
        exercise.time = form.cleaned_data['time']
        exercise.save()
        return redirect('w_page')

    context['form'] = form
    return render(request, "workout_new.html", context)

@login_required(login_url='/authentication/login/')
def update_workout(request):
    context = {}
    exercise = Exercise.objects.get(user=request.user)
    form = TimeForm(request.POST or None)

    if form.is_valid():
        exercise.time += form.cleaned_data['time']
        exercise.save()
        return redirect('w_page')

    context['form'] = form
    return render(request, "workout_update.html", context)