from django.db import models

class Articals(models.Model):
    title = models.CharField('Название', max_length=50)
    factors = models.CharField('Факторы', max_length=250)
    full_text = models.TextField('Описание')
    data = models.DateTimeField('Дата')

