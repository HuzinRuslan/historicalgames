# Generated by Django 3.1.4 on 2021-01-04 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_product_subname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subname',
        ),
    ]