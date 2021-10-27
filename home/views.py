from django.shortcuts import render
from .models import FeedBack, News
from .forms import FeedBackForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserModel

# Create your views here.

def index(request):
    news_list = News.objects.all()
    if request.user.is_authenticated:
        full_name = request.user.get_full_name()

        context = {'nama_user':full_name, 'news_list' : news_list}
        return render(request, 'index(authenticated).html', context)
    else:
        response = {'news_list' : news_list}
        return render(request, 'index.html', response )

    

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



