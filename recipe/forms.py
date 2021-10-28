from django import forms
from .models import Comment
 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'username']
        exclude = ('username',)
    
    error_messages = {
        'requires' : 'Input Text Required'
    }
    content = forms.CharField(label="Comment", required=True, max_length = 100, widget=forms.Textarea(attrs = {'type' : 'text', 'placeholder': 'Leave a comment', 'rows':'4', 'cols' : '50'}))