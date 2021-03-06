# Generated by Django 3.0.8 on 2020-07-19 08:39

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20200707_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='picture_no',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='picture_url',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='upload_date',
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_header',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='web/media/gallery'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(location='web/media/gallery'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='portfoliographic',
            name='graphic',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='web/media/gallery'), upload_to=''),
        ),
    ]
