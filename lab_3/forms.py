from django import forms
from lab_1.models import Friend

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = "__all__"
