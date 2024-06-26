from django import forms
from django.db.models import fields
from healthy_advice.models import CommentHealthy

class NoteForm(forms.ModelForm):
    class Meta:
        model = CommentHealthy
        fields = ['comment_field', 'commentator_name']
        exclude = ('commentator_name',)
    
    error_messages = {
        'requires' : 'Input Text Required'
    }
    comment_field = forms.CharField(label="Comment", required=True, max_length = 100, widget=forms.Textarea(attrs = {'type' : 'text', 'placeholder': 'Leave a comment', 'rows':'4', 'cols' : '50'}))
