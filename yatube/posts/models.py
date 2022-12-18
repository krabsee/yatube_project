from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Сообщество')
    slug = models.SlugField(unique=True, verbose_name='Запись в URL')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'


class Post(models.Model):
    text = models.TextField(max_length=200, verbose_name='Название поста')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Сообщество',
        related_name='posts',
    )

    class Meta:
        ordering = ['-pub_date', ]
