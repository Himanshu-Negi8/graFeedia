# Generated by Django 2.1.4 on 2019-11-16 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='slug',
        ),
    ]