from django import forms
from .models import Image,Comment
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['pubdate']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name']