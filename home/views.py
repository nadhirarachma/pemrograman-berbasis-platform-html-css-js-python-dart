from django.shortcuts import render
from .models import FeedBack, News
from .forms import FeedBackForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserModel

# Create your views here.

def index(request):
    news_list = News.objects.all()
    return render(request, 'index.html')
    

def feedback(request):     
    feedback_list = FeedBack.objects.all()
    
 
    if request.method == 'POST':

        form = FeedBackForm(request.POST)

        # valid
        if form.is_valid():
            form.save()
           
    
    
    else:
        form = FeedBackForm()    

        
    return render(request, 'feedback.html', {'feedback_list': feedback_list, 'form': form})

def news_page(request, slug):
    # return HttpResponse(slug)

    new = News.objects.get(slug=slug)
  
    response = {'new':  new}
    return render(request, 'home_news.html', response)



