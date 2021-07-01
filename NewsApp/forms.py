from .models import News, Tag
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['news_title', 'news_text', 'tag', 'author']
        widgets = {
            "news_title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title'
            }),
            "news_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text'
            }),
            "tag": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tags'
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Author'
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



