from .models import FeedBack
from django.forms import ModelForm
from django import forms


class FeedBackForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = ['name', 'the_feedback']
        exclude = ('name',)
    
    the_feedback = forms.CharField(label="Comment", required=True, max_length = 100, widget=forms.Textarea(attrs = {'type' : 'text', 'placeholder': 'Write your feedback'}))
