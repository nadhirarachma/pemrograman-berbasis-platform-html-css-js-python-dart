from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
# from django.shortcuts import redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .forms import CommentForm

# Create your views here.
def recipe_page(request):
    return render(request, 'recipe_page.html')

def recipe_detail_bruschetta(request):
    return render(request, 'recipe_detail_bruschetta.html')


def recipe_detail_shrimp(request):
    return render(request, 'recipe_detail_shrimp.html')

def recipe_detail_salad(request):
    return render(request, 'recipe_detail_salad_caprese.html')  

def recipe_detail_greek_chicken(request):
    return render(request, 'recipe_detail_greek_chicken.html')  

def recipe_detail_salmon(request):
    return render (request, 'recipe_detail_salmon.html')

