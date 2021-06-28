from django.db import models


class News(models.Model):
    news_title = models.CharField('Заголовок', max_length=200)
    news_text = models.TextField('Текст новости')
    pub_date = models.DateTimeField('Время публикации новости')

    def __str__(self):
        return self.news_title