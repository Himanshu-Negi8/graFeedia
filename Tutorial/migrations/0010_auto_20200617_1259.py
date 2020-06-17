# Generated by Django 2.1.4 on 2020-06-17 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorial', '0009_auto_20200617_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialseries',
            name='img',
            field=models.ImageField(blank=True, upload_to='photo/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 17, 12, 59, 1, 451554), verbose_name='date published'),
        ),
    ]
