from lab_2.models import Note
from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import JsonResponse
from django.core import serializers
from lab_5.forms import NoteForm


def index(request):
    notes = Note.objects.all() 
    form = NoteForm(); 
    response = {'form': form, 'notes': notes}
    return render(request, 'lab5_index.html', response)

def postFriend(request):

    if request.is_ajax and request.method == "POST":

        form = NoteForm(request.POST or None)

        if form.is_valid():

            instance = form.save()

            ser_instance = serializers.serialize('json', [ instance, ])

            return JsonResponse({"instance": ser_instance}, status=200)


# def get_note(request, id):
#     # dictionary for initial data with
#     # field names as keys
#     context ={}
 
#     # add the dictionary during initialization
#     context["data"] = Note.objects.get(id = id)
         
#     return render(request, "lab5_index.html", context)

# def update_note(request, id):
#     # dictionary for initial data with
#     # field names as keys
#     context ={}
 
#     # fetch the object related to passed id
#     obj = get_object_or_404(Note, id = id)
 
#     # pass the object as instance in form
#     form = NoteForm(request.POST or None, instance = obj)
 
#     # save the data from the form and
#     # redirect to detail_view
#     if form.is_valid():
#         form.save()
#         return redirect("/"+id)
 
#     # add form dictionary to context
#     context["form"] = form
 
#     return render(request, "lab5_index.html", context)

# def delete_note(request, id):
#     # dictionary for initial data with
#     # field names as keys
#     context ={}
 
#     # fetch the object related to passed id
#     obj = get_object_or_404(Note, id = id)
 
 
#     if request.method =="POST":
#         # delete object
#         obj.delete()
#         # after deleting redirect to
#         # home page
#         return redirect("/")
 
#     return render(request, "lab5_index.html", context)


