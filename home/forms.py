from .models import FeedBack
from django.forms import ModelForm
from django import forms


class FeedBackForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = ['name', 'the_feedback']
        exclude = ('name',)
    
    the_feedback = forms.CharField(label="Comment", required=True, max_length = 100, widget=forms.Textarea(attrs = {'type' : 'text', 'placeholder': 'Write your feedback'}))
# class NoteForm(forms.ModelForm):
#     class Meta:
#         model = CommentHealthy
#         # fields = '__all__'
#         fields = ['comment_field', 'commentator_name']
#         exclude = ('commentator_name',)
    
#     error_messages = {
#         'requires' : 'Input Text Required'
#     }
#     comment_field = forms.CharField(label="Comment", required=True, max_length = 100, widget=forms.Textarea(attrs = {'type' : 'text', 'placeholder': 'Leave a comment', 'rows':'4', 'cols' : '50'}))