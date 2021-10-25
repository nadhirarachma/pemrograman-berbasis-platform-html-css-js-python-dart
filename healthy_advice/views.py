from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from healthy_advice.models import Rating

# Create your views here.
def healthy_advice(request):
    return render(request, 'healthy_advice.html')

def rate_anu(request):
    if request.is_ajax():
        el_id =request.POST.get('el_id')
        val = request.POST.get('val')
        obj = Rating.objects.get(id=el_id)
        print(obj)
        obj.save()
        return JsonResponse({'success' : 'true', 'score': val}, safe=False)

    return JsonResponse({'success' : 'false'})