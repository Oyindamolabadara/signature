from django import forms
from .models import Comment, Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    """
    Form class to add a comment
    """
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': SummernoteWidget
        }

class PostForm(forms.ModelForm):
    """
    Form class to add a comment
    """
    class Meta:
        model = Post
        fields = ('content',)
        widgets = {
            'content': SummernoteWidget
        }