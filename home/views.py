from django.shortcuts import render

from .forms import FeedBackForm
from django.http import HttpResponse, HttpResponseRedirect, response
from django.contrib.auth.forms import UserModel
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.http.response import HttpResponseRedirect,  HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import FeedBack, News

# Create your views here.
@login_required(login_url="/admin/login/")
def feedback(request):     
    feedback_list = FeedBack.objects.all() 
    news_list = News.objects.all()  
    response = {'news_list': news_list, 'feedback_list': feedback_list}
    return render(request, 'feedback.html', response )

@csrf_exempt
def get_all_news(request):
    all_news = FeedBack.objects.all()
    data = serializers.serialize('json', all_news)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def get_all_feedback(request):
    all_feedback = News.objects.all()
    data = serializers.serialize('json', all_feedback)
    return HttpResponse(data, content_type="application/json")

def index(request):
    news_list = News.objects.all()
    if request.user.is_authenticated:

        if request.method == 'POST':
            form = FeedBackForm(request.POST)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.name = request.user
                obj.save()
                return HttpResponseRedirect("/home")
        
        else:
            form = FeedBackForm()
        return render(request, 'index.html', {'news_list': news_list, 'form': form})
    
    else:
        return render(request, 'index.html', {'news_list': news_list})

    
    

def news_page(request, slug):
    # return HttpResponse(slug)

    new = News.objects.get(slug=slug)
  
    response = {'new':  new}
    return render(request, 'home_news.html', response)

