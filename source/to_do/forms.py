from django import forms
from django.forms import widgets


STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class TaskForm(forms.Form):
    name = forms.CharField(max_length=40, required=True, label='Название')
    description = forms.CharField(max_length=500, required=False, label='Описание', widget=widgets.Textarea)
    status = forms.CharField(max_length=50, required=True, label='Статус', widget=forms.Select(choices=STATUS_CHOICES))
    deadline = forms.DateField(required=False, label='Дата выполнения')
