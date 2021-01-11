from django.contrib import admin
from django.utils.safestring import mark_safe

from mainapp.models import Product, ProductTag, Gallery, MainSlider, ProductCategory


def unbound_callable(emp):
    return emp.gallery.get(is_main=True).image


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'image_show', 'price', 'discount', 'is_active', 'quantity', 'metacritic']
    list_filter = ['is_active', 'discount', 'category']
    list_editable = ['price', 'discount', 'is_active']

    def image_show(self, obj):
        main_image = obj.gallery.get(is_main=True).image
        if main_image:
            return mark_safe(f'<img src="/media/{main_image}" width="60" />')
        return "None"

    image_show.__name__ = 'Product image'


admin.site.register(ProductTag)
admin.site.register(Gallery)
admin.site.register(MainSlider)
admin.site.register(ProductCategory)
