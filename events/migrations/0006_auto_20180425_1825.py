# Generated by Django 2.0.4 on 2018-04-25 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20180425_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='details',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(help_text='Please use the following format: <em>HH:MM:SS<em>'),
        ),
    ]