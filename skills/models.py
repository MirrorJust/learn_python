from django.db import models


# id - int
# name_skill - text
# created_at- DateTime
# update_at - DateTime
# photo - Image
class Skill(models.Model):
    name_skill = models.CharField(max_length=50, verbose_name='Название навыка')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Навык поулчен?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.name_skill

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
        ordering = ['created_at']


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название категории', db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
