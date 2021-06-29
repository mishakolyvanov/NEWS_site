from .models import News
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, DateTimeField


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['news_title', 'news_text', 'tag', 'author']
        widgets = {
            "news_title": TextInput(attrs={
                'placeholder': 'Title'
            }),
            "news_text": Textarea(attrs={
                'placeholder': 'Text'
            }),
            "tag": TextInput(attrs={
                'placeholder': 'Tags'
            }),
            # "pub_date": DateTimeInput(attrs={
            #     'type': 'datetime-local'
            # }),
            "author": TextInput(attrs={
                'placeholder': 'author'
            })
        }
