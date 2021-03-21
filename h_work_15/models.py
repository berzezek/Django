from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class News(models.Model):
    slug = models.SlugField('Короткая ссылка', max_length=100, default="")
    long_link = models.TextField('Длинная ссылка')
    date = models.DateTimeField('Дата', default=timezone.now)
    title = models.CharField('Описание', max_length=100)
    autor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)



    views = models.IntegerField('Просмотры', default=1)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Ссылку'
        verbose_name_plural = 'Ссылки'

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})
