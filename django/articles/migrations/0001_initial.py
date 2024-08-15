# Generated by Django 5.1 on 2024-08-15 16:01

import django.utils.timezone
import mdeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата обновления')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('slug', models.SlugField(unique=True, verbose_name='Человекопонятный URL')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('content', mdeditor.fields.MDTextField(verbose_name='Контент')),
                ('meta_keywords', models.CharField(max_length=100, verbose_name='Мета, ключевые слова')),
            ],
            options={
                'verbose_name': 'статью',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]
