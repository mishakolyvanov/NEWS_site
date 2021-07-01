from .models import News
from django.forms import ModelForm, TextInput, Textarea


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['news_title', 'news_text', 'tags', 'author']
        widgets = {
            "news_title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            "news_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text'
            }),
            "tags": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tags'
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Author'
            })
        }
