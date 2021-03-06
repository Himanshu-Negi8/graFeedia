# Generated by Django 2.1.4 on 2019-11-16 22:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorial', '0002_auto_20191117_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialseries',
            name='series_slug',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 17, 3, 31, 50, 695705), verbose_name='date published'),
        ),
    ]
