from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class ToDoList(models.Model):
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name="Описание")
    name = models.CharField(max_length=40, null=False, blank=False, verbose_name="Название", default="task")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, verbose_name="Статус", default=STATUS_CHOICES[0][0])
    deadline = models.DateField(null=True, blank=True, verbose_name="Дата выполнения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return f'{self.id}. {self.name}'
