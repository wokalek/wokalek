# Generated by Django 5.0.6 on 2024-07-03 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_alter_galleryimage_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryimage',
            name='section',
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='section',
            field=models.ManyToManyField(null=True, to='gallery.gallerysection', verbose_name='Раздел'),
        ),
    ]
