# Generated by Django 3.1.4 on 2021-01-06 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20210105_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='is_big',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='is_big',
            field=models.BooleanField(default=False),
        ),
    ]