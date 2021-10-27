from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def recipe_page(request):
    return render(request, 'recipe_page.html')

def recipe_detail_bruschetta(request):
    return render(request, 'recipe_detail_bruschetta.html')


def recipe_detail_shrimp(request):
    return render(request, 'recipe_detail_shrimp.html')

def recipe_detail_bruschetta(request):
    return render(request, 'recipe_detail_bruschetta.html')  