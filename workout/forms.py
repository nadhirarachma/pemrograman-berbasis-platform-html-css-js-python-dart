from django.forms.models import ModelForm
from django import forms
from .models import Exercise, Time

class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'

class TimeForm(forms.Form):
    time = forms.IntegerField(widget=forms.NumberInput)