# Generated by Django 3.1.4 on 2021-02-04 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20210204_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainslider',
            name='back_image',
            field=models.ImageField(max_length=2048, upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='mainslider',
            name='image',
            field=models.ImageField(blank=True, max_length=2048, upload_to='product_images'),
        ),
    ]