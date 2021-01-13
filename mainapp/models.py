from django.db import models
from django.urls import reverse


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Имя')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class ProductTag(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Имя тега')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class Product(models.Model):
    BAD = 'Bad'
    ALRIGHT = 'Alright'
    GOOD = 'Good'
    PERFECT = 'Perfect'

    RATING_CHOICES = (
        (BAD, 'Bad'),
        (ALRIGHT, 'Alright'),
        (GOOD, 'Good'),
        (PERFECT, 'Perfect')
    )

    name = models.CharField(max_length=128, verbose_name='имя')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, default="")
    short_desc = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveSmallIntegerField(default=0)
    discount = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_big = models.BooleanField(default=False)
    tags = models.ManyToManyField(ProductTag)
    metacritic = models.PositiveSmallIntegerField(default=0)
    pcGamer = models.PositiveSmallIntegerField(default=0)
    OpenCritic = models.CharField(max_length=16, choices=RATING_CHOICES, verbose_name='Оценка OpenCritic', default=BAD)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} {self.category.name}'

    def get_main_image(self):
        return self.gallery.get(is_main=True).image

    def get_first_small_image(self):
        return self.gallery.filter(is_main=False, is_big=False)[0]

    def get_other_small_images(self):
        return self.gallery.filter(is_main=False, is_big=False)[1:]

    def get_big_image(self):
        return self.gallery.get(is_big=True).image

    def get_subname(self):
        name = str(self.name)

        subname_start = name.find(':')
        if subname_start != -1:
            return name[name.find(':') + 2:]
        return ''

    def get_name(self):
        name = str(self.name)

        name_end = name.find(':')
        if name_end != -1:
            return name[:name.find(':') + 1]
        return name

    def get_tags(self):
        tags = self.tags.values()
        return tags

    def get_new_price(self):
        price = str(self.price)
        discount = str(self.discount)

        return float(price) - float(price) * (float(discount) / 100)

    def get_absolute_url(self):
        return reverse('catalog:product', args=[self.id])


class Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery')
    is_main = models.BooleanField(default=False)
    is_big = models.BooleanField(default=False)
    image = models.ImageField(upload_to='product_images', blank=True)

    class Meta:
        verbose_name = 'Галлерея'
        verbose_name_plural = 'Галлерея'


class MainSlider(models.Model):
    header = models.CharField(max_length=128, verbose_name='Заголовок')
    text = models.CharField(max_length=512, verbose_name='Текст')
    short_text = models.CharField(max_length=256, verbose_name='Короткий текст', blank=True)
    image = models.ImageField(upload_to='product_images', blank=True)
    back_image = models.ImageField(upload_to='product_images')
