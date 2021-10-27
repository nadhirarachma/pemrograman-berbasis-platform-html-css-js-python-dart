from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateProfileForm
# from workout.models import Workout
# from sleep.models import Sleep

def index(request):
    profile = request.user.profile
    full_name = request.user.first_name + " " + request.user.last_name
    email = request.user.email
    username = request.user.username
    # workout = Workout.objects.all()
    # sleep = Sleep.objects.all()

    # response = {'profile': profile, 'workout' : workout, 'sleep' : sleep}
    response = {'profile': profile, 'full_name': full_name, 'email':email, 'username':username}
    return render(request, 'summary.html', response)

@login_required
def edit_profile(request):
    username = request.user.username
    user_form = UpdateUserForm(request.POST or None, instance=request.user)
    profile_form = UpdateProfileForm(request.POST or None, instance=request.user.profile)

    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        return redirect('/summary')

    response = {'user_form': user_form, 'profile_form': profile_form, 'username':username}
    return render(request, 'edit_profile.html', response)

  