# Generated by Django 4.1.3 on 2022-11-04 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0003_todolist_created_add'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='created_add',
            new_name='created_at',
        ),
    ]