# Generated by Django 5.0.7 on 2024-07-30 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_delete_articleproxy_delete_postproxy_article_post'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
            ],
            options={
                'verbose_name': 'фото',
                'verbose_name_plural': 'фотографии',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('photos.photo',),
        ),
    ]