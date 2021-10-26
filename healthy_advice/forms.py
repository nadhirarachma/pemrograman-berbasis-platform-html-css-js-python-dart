from django import forms
from django.db.models import fields
from healthy_advice.models import CommentHealthy

class NoteForm(forms.ModelForm):
    class Meta:
        model = CommentHealthy
        # fields = '__all__'
        fields = ['comment_field']
    
    error_messages = {
        'requires' : 'Input Text Required'
    }
    comment_field = forms.CharField(label="Comment", required=True, max_length = 100, widget=forms.Textarea(attrs = {'type' : 'text', 'placeholder': 'Leave a constructive comment below', 'rows':'4', 'cols' : '60'}))