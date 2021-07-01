from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
import datetime


class News(models.Model):
    news_title = models.CharField('Заголовок', max_length=200)
    news_text = models.TextField('Текст новости')
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    views_count = models.IntegerField(default=0)
    tags = TaggableManager()
    author = models.CharField('Автор', max_length=200)

    def __str__(self):
        return self.news_title
