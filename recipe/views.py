from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
from recipe.forms import CommentForm
from recipe.models import Comment
from django.http import HttpResponse, JsonResponse
from django.core import serializers
# Create your views here.

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


def recipe_page(request):
    notes = Comment.objects.all()
    form = CommentForm()
    if request.is_ajax():
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.username = request.user 
            # print(obj)
            obj.save()
            return HttpResponseRedirect("/recipe")
        
    response = {'notes' : notes, 'form' : form}
    return render(request, 'recipe_page.html', response)

def get_all_comment(request):
    all_comment = Comment.objects.all()
    data = serializers.serialize('json', all_comment)
    return HttpResponse(data, content_type="application/json")

def delete_comment(request, id):
    obj = get_object_or_404(Comment, id = id)
    
    if request.method == "POST":
        # delete object
        obj.delete()
        
    data = serializers.serialize('json', Comment.objects.all())

    return HttpResponse(data, content_type='application/json')

def edit_comment(request, id):
    obj = get_object_or_404(Comment, id = id)
    if request.is_ajax():
        new_comment = request.POST.get('content')
        obj.content = new_comment
        obj.save()
    data = serializers.serialize('json', [obj, ])    
    return HttpResponse(data, content_type = 'application/json')