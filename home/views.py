from django.shortcuts import render

# Create your views here.
hello = 'Hello World'
def index(request):
    response = {'hai': hello}
    return render(request, 'index.html', response)

