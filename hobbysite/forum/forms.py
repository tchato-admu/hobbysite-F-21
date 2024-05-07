from django import forms
from .models import Thread, Comment


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'author', 'category', 'entry', 'image']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)