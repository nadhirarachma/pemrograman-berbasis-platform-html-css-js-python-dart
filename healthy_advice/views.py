from django.shortcuts import render
from django.http import HttpResponse
from healthy_advice.models import Rating

# Create your views here.
def healthy_advice(request):
    return render(request, 'healthy_advice.html')
