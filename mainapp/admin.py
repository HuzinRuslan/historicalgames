from django.contrib import admin
from mainapp.models import Product, ProductTag, Gallery

admin.site.register(ProductTag)
admin.site.register(Product)
admin.site.register(Gallery)
