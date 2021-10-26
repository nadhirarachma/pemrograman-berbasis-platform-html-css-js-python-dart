from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm
# from workout.models import Workout
# from sleep.models import Sleep

def index(request):
    # profile = Profile.objects.all()
    # workout = Workout.objects.all()
    # sleep = Sleep.objects.all()

    # response = {'profile': profile, 'workout' : workout, 'sleep' : sleep}
    # response = {'profile': profile}
    return render(request, 'summary.html')

def edit_profile(request):
#     form = ProfileForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('/summary')
    
#     response = {'form' : form}
    return render(request, 'edit_profile.html')
  