from django.db import models


class Book(models.Model):
    title = models.CharField('标题', max_length=20)
    zuo = models.CharField('作者', max_length=20)
    content = models.TextField('内容')

    def __str__(self):
        return self.title
