from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import UpdateUserForm, UpdateProfileForm
from .models import Profile
from django.contrib.auth.models import User
from workout.models import Exercise
from sleep.models import Sleep
import datetime
import json

@login_required(login_url= '/authentication/login/')

def summary(request):

    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    full_name = request.user.first_name + " " + request.user.last_name
    email = request.user.email
    username = request.user.username
    navbar_name = request.user.get_full_name()

    workout = Exercise.objects.get(user=request.user)
    sleep = Sleep.objects.get(user=request.user)
  
    response = {'profile': profile, 'full_name': full_name, 'email':email, 'workout' : workout, 'sleep' : sleep, 'username':username, 'nama_user':navbar_name}
    return render(request, 'summary.html', response)

def edit_profile(request):
    
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    username = request.user.username
    navbar_name = request.user.get_full_name()
    user_form = UpdateUserForm()
    profile_form = UpdateProfileForm()

    if request.is_ajax:
        user_form = UpdateUserForm(request.POST or None, instance=request.user)
        profile_form = UpdateProfileForm(request.POST or None, instance=profile)
       
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return JsonResponse({
                'message': 'success'
            })

    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form, 'username':username, 'nama_user':navbar_name})

@csrf_exempt
def get_profile(request):

    if request.user.is_authenticated:
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = Profile(user=request.user, age="", gender="", profession="", mobile="", address="")

        user_profile = request.user
        workout = Exercise.objects.get(user=request.user)
        sleep = Sleep.objects.get(user=request.user)

        data = serializers.serialize('json', [user_profile, profile, workout, sleep,])
        return HttpResponse(data, content_type="application/json")
    else:
        return JsonResponse(list({'Login First'}), safe=False)

@csrf_exempt
def post_profile(request):
    data = json.loads(request.body)
    User.objects.filter(user=request.user).update(username=data["username"], first_name=data["first_name"], last_name=data["last_name"], email=data["email"])
    Profile.objects.filter(user=request.user).update(age=data["age"], gender=data["gender"], profession=data["profession"], mobile=data["mobile"], address=data["address"])