from .models import Post
from django.forms import ModelForm
from django import forms

class PostCreationForm(ModelForm):
    body = forms.CharField(required=True)

    class Meta:
        model = Post

class PostChangeOrUpdateForm(ModelForm):
    body = forms.CharField(required=True)

    class Meta:
        model = Post
