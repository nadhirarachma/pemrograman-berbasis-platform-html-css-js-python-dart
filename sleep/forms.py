from django.forms.models import ModelForm
from django import forms
from .models import Sleep
import datetime

class SleepForm(ModelForm):
    class Meta:
        model = Sleep
        fields = '__all__'

class TimeForm(forms.Form):
    time = forms.IntegerField(widget=forms.NumberInput, initial=0)


class NewDate(forms.Form):
    today = forms.DateField(widget=forms.SelectDateWidget(), initial=datetime.date.today)
    time = forms.IntegerField(widget=forms.NumberInput, initial=0)