# Generated by Django 3.1.4 on 2021-01-06 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_remove_product_is_big'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_big',
            field=models.BooleanField(default=False),
        ),
    ]
