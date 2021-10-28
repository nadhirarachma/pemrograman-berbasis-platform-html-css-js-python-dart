from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateProfileForm
from .models import Profile
# from workout.models import Workout
# from sleep.models import Sleep
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
    # workout = Workout.objects.all()
    # sleep = Sleep.objects.all()

    # response = {'profile': profile, 'workout' : workout, 'sleep' : sleep}
    response = {'profile': profile, 'full_name': full_name, 'email':email, 'username':username, 'nama_user':navbar_name}
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