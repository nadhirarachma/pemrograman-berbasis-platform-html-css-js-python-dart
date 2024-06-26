from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from lab_1.models import Friend
from lab_3.forms import FriendForm

@login_required(login_url= '/admin/login/')
def index(request):
    friends = Friend.objects.all()  
    response = {'friends': friends}
    return render(request, 'lab3_index.html', response)

def add_friend(request):
    form = FriendForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/lab-3')
    
    response = {'form' : form}
    return render(request, 'lab3_form.html', response)
        
       