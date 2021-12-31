from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, UserModel

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
from os import error
from django.http import response
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from .models import *
from .forms import CreateUserForm

from home.views import index as welcome

# workout
from workout.models import Exercise

from sleep.models import Sleep

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				username = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + username)
				Exercise.objects.create(
					user=user,
				)
				Sleep.objects.create(
					user=user,
				)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Incorrect Username or Password ')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect(welcome)

def home(request):
	return redirect(welcome)

@csrf_exempt
def login_flutter(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return JsonResponse({
              "status": True,
              "username": request.user.username,
              "message": "Successfully Logged In!"
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
          "status": False,
          "message": "Failed to Login, check your email/password."
        }, status=401)

@csrf_exempt
def register_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        firstname = data["first_name"]
        lastname = data["last_name"]
        username = data["username"]
        email = data["email"]
        password1 = data["password1"]

        newUser = UserModel.objects.create_user(
        first_name = firstname,
        last_name = lastname,
        username = username, 
        email = email,
        password = password1,
        )

        newUser.save()

        Exercise.objects.create(
            user=newUser,
        )
        Sleep.objects.create(
            user=newUser,
        )

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def logout_flutter(request):
    try:
        logout(request)
        return JsonResponse({
                    "status": True,
                    "message": "Successfully Logged out!"
                }, status=200)
    except:
        return JsonResponse({
          "status": False,
          "message": "Failed to Logout"
        }, status=401)