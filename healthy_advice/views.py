from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.http import response
from django.http.response import HttpResponseRedirect,  HttpResponse, JsonResponse
from healthy_advice.models import CommentHealthy, HealthyArticle
from healthy_advice.forms import NoteForm
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

# from healthy_advice.models import Rating

# Create your views here.
def healthy_advice(request):
    notes = CommentHealthy.objects.all()
    articles = HealthyArticle.objects.all()
    form = NoteForm()
    for note in notes:
        # print(str(note.commentator_name) == str(request.user))
        if (str(note.commentator_name) == str(request.user)):
            flag=True
            break
    if request.is_ajax():
        form = NoteForm(request.POST)
        if form.is_valid():
            print(request.user)
            obj = form.save(commit=False)
            obj.commentator_name = request.user
            # print(obj)
            obj.save()
            # print(obj.commentator_name)
            return HttpResponseRedirect("/healthy_advice")
        
    response = {'notes' : notes, 'form' : form, 'articles':articles}
    return render(request, 'healthy_advice.html', response)

@csrf_exempt
def get_all_comment(request):
    all_comment = CommentHealthy.objects.all()
    data = serializers.serialize('json', all_comment)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def delete_comment(request, id):
    obj = get_object_or_404(CommentHealthy, id = id)
    
    if request.method == "POST":
        # delete object
        obj.delete()
        
    data = serializers.serialize('json', CommentHealthy.objects.all())

    return HttpResponse(data, content_type='application/json')
    
@csrf_exempt
def edit_comment(request, id):
    obj = get_object_or_404(CommentHealthy, id = id)
    if request.is_ajax():
        new_comment = request.POST.get('comment_field')
        obj.comment_field = new_comment
        obj.save()
    data = serializers.serialize('json', [obj, ])    
    return HttpResponse(data, content_type = 'application/json')



def detail_article(request, id):
    article = HealthyArticle.objects.all().get(id=id)
    response = {
        'details' : article
    }
    return render(request, 'article_detail.html', response)

@csrf_exempt
def get_all_article(request):
    all_article = HealthyArticle.objects.all()
    data = serializers.serialize('json', all_article)
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def post_comment_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Add Failed"}, status=400)

    if request.method == 'POST':

        data = json.loads(request.body)

        # commentator_name = data["commentator_name"]
        comment_field = data["comment_field"]

        comment_healthy = CommentHealthy(commentator_name=request.user, comment_field=comment_field)

        comment_healthy.save()

        return JsonResponse({"status": "success"}, status=200)
    
    else:
        return JsonResponse({"status": "error"}, status=401)
