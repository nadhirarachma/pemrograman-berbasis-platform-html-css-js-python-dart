from .models import FeedBack
from django.forms import ModelForm
from django import forms


class FeedBackForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = ['name', 'the_comment']
        