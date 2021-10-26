from django.contrib.auth.forms import UserModel
from django.shortcuts import render

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        full_name = request.user.get_full_name()

        context = {'nama_user':full_name}
        return render(request, 'welcome.html', context)
    else:
        return render(request, 'index.html')
	

