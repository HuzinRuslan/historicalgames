import json
import os

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from mainapp.models import Product, ProductTag, Gallery

FILE_PATH = os.path.join(settings.BASE_DIR, 'mainapp/json')


def load_from_json(file_name):
    with open(os.path.join(FILE_PATH, file_name + '.json'), encoding="utf-8") as json_file:
        return json.load(json_file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        tags = load_from_json('tags')
        ProductTag.objects.all().delete()

        for tag in tags:
            ProductTag.objects.create(**tag)

        products = load_from_json('products')
        Product.objects.all().delete()
        for prod in products:
            tags = prod['tags']
            tag_lst = []
            for tag in tags:
                tag_lst.append(ProductTag.objects.get(name=tag))
            del prod['tags']
            p = Product.objects.create(**prod)
            for t in tag_lst:
                p.tags.add(t)

        gallery = load_from_json('gallery')

        Gallery.objects.all().delete()

        for image in gallery:
            prod = Product.objects.get(name=image['product'])
            image['product'] = prod
            Gallery.objects.create(**image)

        User.objects.create_superuser(username='django', password='geekbrains')
