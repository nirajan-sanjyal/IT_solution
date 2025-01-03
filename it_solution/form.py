from django import forms
from .models import LatestNews

class LatestNewsForm(forms.ModelForm):
    class Meta:
        model = LatestNews
        fields = ['title', 'content', 'admin']
