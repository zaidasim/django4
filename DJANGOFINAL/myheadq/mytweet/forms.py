from django import forms
from .models import Tweet

class Tweetforms(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['text','photo']