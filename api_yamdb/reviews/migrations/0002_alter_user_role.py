# Generated by Django 3.2 on 2023-06-22 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.TextField(blank=True, choices=[('anonymous', 'анон'), ('user', 'Пользователь'), ('moderator', 'Модератор'), ('admin', 'Админ')], default='user', verbose_name='Пользовательская роль'),
        ),
    ]