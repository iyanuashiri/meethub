# Generated by Django 5.2.4 on 2025-07-07 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_auto_20180523_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
