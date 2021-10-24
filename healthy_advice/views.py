from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def healthy_advice(request):
    return render(request, 'healthy_advice.html')