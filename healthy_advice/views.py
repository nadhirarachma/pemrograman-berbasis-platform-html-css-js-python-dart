from django.shortcuts import render
from django.http import response
from django.http.response import HttpResponseRedirect
from healthy_advice.models import Comment
from healthy_advice.forms import NoteForm
from django.http import HttpResponse, JsonResponse
# from healthy_advice.models import Rating

# Create your views here.
def healthy_advice(request):
    notes = Comment.objects.all()
    response = {'notes' : notes}
    return render(request, 'healthy_advice.html', response)

def add_note(request):
    response ={}
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/healthy_advice")
    response['form']= form
    return render(request, 'healthy_advice_form.html', response)

def note_list(request):
    # ngeload
    notes = Comment.objects.all()
    response = {'notes': notes}
    return render(request, 'healthy_advice_list.html', response)

def manfaat_istirahat(request):
    return render(request, 'article_1.html')

# def rate_anu(request):
#     if request.is_ajax():
#         el_id =request.POST.get('rate-form')
#         val = request.POST.get('val')
#         obj = Rating.objects.get(id=el_id)
#         print(obj)
#         obj.save()
#         return JsonResponse({'success' : 'true', 'score': val}, safe=False)

#     return JsonResponse({'success' : 'false'})