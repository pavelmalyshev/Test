from django.forms import ModelForm
from django import forms
from django.db import models
from note.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('who', 'text',)


    