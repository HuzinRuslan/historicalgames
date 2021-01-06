from django.contrib import admin
from mainapp.models import Product, ProductTag, Gallery, MainSlider, ProductCategory

admin.site.register(ProductTag)
admin.site.register(Product)
admin.site.register(Gallery)
admin.site.register(MainSlider)
admin.site.register(ProductCategory)
