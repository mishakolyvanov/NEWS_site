from .models import News, Tag
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, DateTimeField
from django import forms


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
    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

# class TagForm(forms.ModelForm):
#     class Meta:
#         model = Tag
#         fields = ['title']
#         widgets = {
#             "title": TextInput(attrs={
#                 'placeholder': 'tag'
#             })
#         }



