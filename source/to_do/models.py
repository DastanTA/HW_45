from django.db import models


class ToDoList(models.Model):
    description = models.TextField(max_length=400, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=50, verbose_name="Статус", default="new")
    deadline = models.DateField(verbose_name="к дате", null=True, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return f'{self.id}. {self.description}'
