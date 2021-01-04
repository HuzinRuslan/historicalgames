from django.db import models


# class ProductCategory(models.Model):
#     name = models.CharField(max_length=64, unique=True, verbose_name='Имя')
#     description = models.TextField(blank=True, verbose_name='Описание')
#     is_active = models.BooleanField(default=True)
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#     def __str__(self):
#         return self.name


class ProductTag(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Имя тега')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name='имя')
    short_desc = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    tags = models.ManyToManyField(ProductTag)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name}'


# class Contact(models.Model):
#     phone = models.CharField(max_length=15, verbose_name='номер телефона')
#     email = models.CharField(max_length=50, verbose_name='почта')
#     city = models.CharField(max_length=20, verbose_name='город')
#     address = models.TextField(blank=True)
#
#     def __str__(self):
#         return f'Контакт {self.city} {self.email}'


class Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery')
    is_main = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product_images', blank=True)

    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлерея'

    def get_all_gallery(self):
        pass

