from django.forms.models import ModelForm
from django import forms
from .models import Exercise
import datetime

class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'

class TimeForm(forms.Form):
    time = forms.IntegerField(widget=forms.NumberInput)


class NewDate(forms.Form):
    today = forms.DateField(widget=forms.SelectDateWidget(), initial=datetime.date.today)
    time = forms.IntegerField(widget=forms.NumberInput, initial=0)