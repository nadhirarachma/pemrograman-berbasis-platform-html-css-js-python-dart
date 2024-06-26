from django.shortcuts import render, redirect
from lab_2.models import Note
from lab_4.forms import NoteForm

def index(request):
    notes = Note.objects.all() 
    response = {'notes': notes}
    return render(request, 'lab4_index.html', response)

def add_note(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/lab-4')
    
    response = {'form' : form}
    return render(request, 'lab4_form.html', response)

def note_list(request):
    notes = Note.objects.all() 
    response = {'notes': notes}
    return render(request, 'lab4_note_list.html', response)