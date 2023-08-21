from django.db import models
from django.urls import reverse

from accounts.models import User


# Create your models here.

class File(models.Model):
    class Status(models.TextChoices):
        NEW = 'NEW', 'New'
        UPDATED = 'UPD', 'Updated'
        CHECKED = 'CHK', 'Checked'

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    name = models.CharField(max_length=250, unique=True, verbose_name='Имя файла')
    description = models.TextField(blank=True, verbose_name='Описание')
    file = models.FileField(upload_to='files', verbose_name='Файл')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    status = models.CharField(max_length=3, choices=Status.choices, default=Status.NEW, verbose_name='Статус')
    slug = models.SlugField(max_length=250, unique_for_date='created', db_index=True, verbose_name='Слаг')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Файлы'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main_app:update_file', args=[self.slug])


class Log(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, verbose_name='Файл')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    description = models.TextField(default='Файл успешно проверен')
    send = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Логи'
        verbose_name_plural = 'Логи'