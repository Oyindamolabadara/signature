from django import forms
from .models import Comment
from django_summernote.widgets import SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    """
    Form class to add a comment
    """
    class Meta:
        model = Comment
        fields = ('body',)