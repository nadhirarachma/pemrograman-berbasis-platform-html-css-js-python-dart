from django import forms
from lab_2.models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = "__all__"
