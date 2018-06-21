from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    # title = forms.CharField(required=False)
    class Meta:
        model = Post
        fields = {'text', 'title'}
