from django import forms
from django.db.models import fields
from healthy_advice.models import Comment

class NoteForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ['comment']
    
    error_messages = {
        'requires' : 'Input Text Required'
    }
    comment = forms.CharField(label="Comment", required=True, max_length = 100, widget=forms.Textarea(attrs = {'type' : 'text', 'placeholder': 'Leave a constructive comment below'}))