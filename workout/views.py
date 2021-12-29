from django.shortcuts import render, redirect
from .models import Exercise
from .forms import TimeForm
from django.contrib.auth.decorators import login_required
import datetime

from django.http import HttpResponse, JsonResponse
from django.http.response import HttpResponseRedirect,  HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def get_exercise(request):
    if request.user.is_authenticated:
        e = Exercise.objects.get(user=request.user)
        if (datetime.date.today() != e.today):
            e.today = datetime.date.today()
            e.time = 0
            e.save()
        response = {'w_counter': e.time, 'w_username': e.user.username}
        return JsonResponse(response)
    else:
        return JsonResponse({'w_username': ''})

@csrf_exempt
def freset_exercise(request):
    if request.user.is_authenticated:
        e = Exercise.objects.get(user=request.user)
        e.time = 0
        if (datetime.date.today() != e.today):
            e.today = datetime.date.today()
        e.save()
        response = {'w_counter': e.time, 'w_username': e.user.username}
        return JsonResponse(response)
    else:
        return JsonResponse({'w_username': ''})

@csrf_exempt
def post_exercise(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if request.user.is_authenticated:
            e = Exercise.objects.get(user=request.user)
            if (datetime.date.today() != e.today):
                e.today = datetime.date.today()
                e.time = data["add"]
            else:
                e.time += data["add"]
                if e.time > 1440:
                    e.time = 1440
                elif e.time < 0:
                    e.time = 0

            e.save()
            response = {'w_counter': e.time, 'w_username': e.user.username}
            return JsonResponse(response)
        else:
            return JsonResponse({'w_username': ''})

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
def reset_workout(request):
    e = Exercise.objects.get(user=request.user)
    e.time = 0
    e.save()
    return redirect('w_page')

@login_required(login_url='/authentication/login/')
def update_workout(request):
    context = {}
    exercise = Exercise.objects.get(user=request.user)
    form = TimeForm(request.POST or None)

    if (datetime.date.today() != exercise.today):
        exercise.today = datetime.date.today()
        exercise.time = 0
        exercise.save()

    if form.is_valid():
        exercise.time += form.cleaned_data['time']
        if exercise.time > 1440:
            exercise.time = 1440
        elif exercise.time < 0:
            exercise.time = 0
        exercise.save()
        return redirect('w_page')

    context['form'] = form
    return render(request, "workout_update.html", context)
