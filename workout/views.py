from django.shortcuts import render, redirect
from .models import Exercise
from .forms import ExerciseForm, TimeForm
from django.contrib.auth.decorators import login_required
import datetime

from django.http import HttpResponse

# Create your views here.
