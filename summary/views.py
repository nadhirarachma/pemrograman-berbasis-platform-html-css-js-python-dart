from django.shortcuts import render

def index(request):
    return render(request, 'summary.html')

def edit_profile(request):
    return render(request, 'editprofile.html')
  