from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class News(models.Model):
    news_title = models.CharField('Заголовок', max_length=200)
    news_text = models.TextField('Текст новости')
    pub_date = models.DateTimeField('Время публикации новости')
    views_count = models.IntegerField(default=0)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.news_title
