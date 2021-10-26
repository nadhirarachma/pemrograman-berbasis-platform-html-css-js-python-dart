from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.http import response
from django.http.response import HttpResponseRedirect,  HttpResponse, JsonResponse
from healthy_advice.models import CommentHealthy
from healthy_advice.forms import NoteForm
from django.http import HttpResponse, JsonResponse
from django.core import serializers
# from healthy_advice.models import Rating

# Create your views here.
def healthy_advice(request):
    notes = CommentHealthy.objects.all()
    form = NoteForm()
    if request.is_ajax():
        form = NoteForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.commentator_name = request.user
            # print(obj)
            obj.save()
            return HttpResponseRedirect("/healthy_advice")
        
    response = {'notes' : notes, 'form' : form}
    return render(request, 'healthy_advice.html', response)

def get_all_comment(request):
    all_comment = CommentHealthy.objects.all()
    data = serializers.serialize('json', all_comment)
    return HttpResponse(data, content_type="application/json")

def delete_comment(request, id):
    obj = get_object_or_404(CommentHealthy, id = id)
    
    if request.method == "POST":
        # delete object
        obj.delete()
        
    data = serializers.serialize('json', CommentHealthy.objects.all())

    return HttpResponse(data, content_type='application/json')

def manfaat_istirahat(request):
    return render(request, 'manfaat_istirahat.html')
