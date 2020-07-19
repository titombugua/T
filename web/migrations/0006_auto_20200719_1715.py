# Generated by Django 3.0.8 on 2020-07-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20200719_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_header',
            field=models.ImageField(upload_to='blog_header'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.ImageField(blank=True, upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='portfoliographic',
            name='graphic',
            field=models.ImageField(upload_to='portfolio'),
        ),
    ]
