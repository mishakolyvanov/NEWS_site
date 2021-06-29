from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import datetime
import datetime

class Tag(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class News(models.Model):
    # csrf_token = models.TextField('Токен')
    news_title = models.CharField('Заголовок', max_length=200)
    news_text = models.TextField('Текст новости')
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    views_count = models.IntegerField(default=0)
    tag = models.ManyToManyField(Tag, blank=True)
    author = models.CharField('Автор', max_length=200)

    def __str__(self):
        return self.news_title
