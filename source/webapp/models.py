from django.contrib.auth import get_user_model
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок',)
    description = models.TextField(max_length=3000, verbose_name='Описание')
    category_id = models.ManyToManyField('webapp.Category', related_name='articles', blank=True,
                                         verbose_name='Категория')
    user_id = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1,
                                related_name='articles', verbose_name='Пользователь')
    image = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Фото')

    def __str__(self):
        return "{}. {}".format(self.pk, self.title)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок',)
    parent_id = models.OneToOneField('webapp.Category', on_delete=models.PROTECT, null=True, blank=True,
                                     verbose_name='Основная категория')

    def __str__(self):
        return "{}. {}".format(self.pk, self.title)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
