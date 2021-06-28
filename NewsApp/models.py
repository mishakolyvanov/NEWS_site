from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class News(models.Model):
    news_title = models.CharField('Заголовок', max_length=200)
    news_text = models.TextField('Текст новости')
    pub_date = models.DateTimeField('Время публикации новости')
    tags = TaggableManager()
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.news_title

