from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique=True)
    text = models.TextField('Основной текст статьи')
    date = models.DateTimeField('Дата',default=timezone.now)
    autor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)

    

    views = models.IntegerField('Просмотры', default=1)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
