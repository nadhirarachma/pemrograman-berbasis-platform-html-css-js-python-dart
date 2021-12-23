from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import json
from os import error
from django.http import response
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status


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
	data = json.loads(request.body)

	username = request["username"]
	password = request["password"]

	user = authenticate(username=username, password=password)
	if user is not None:
		# print("Hore")
		return JsonResponse(data, status=status.HTTP_201_CREATED)
	else:
		# print("Sad")
		return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
