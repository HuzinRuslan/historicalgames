from django.http import JsonResponse, request
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from cart.cart import Cart
from mainapp.models import Product, MainSlider


def get_similar_products(product):
    same_products = Product.objects.exclude(pk=product.pk).filter(category_id=product.category_id)[:4]
    if len(same_products) < 4:
        prods_len = 4 - len(same_products)
        new_products = Product.objects.exclude(category_id=product.category_id).order_by("?")[:prods_len]
        same_products |= new_products
    return same_products


class Main(ListView):
    model = Product
    template_name = 'mainapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        context['object_list'] = context['object_list'][:4]
        context['title'] = 'Главная'
        context['cart'] = cart

        return context


def contacts(request):
    cart = Cart(request)

    content = {
        'title': 'Контакты',
        'cart': cart
    }

    return render(request, 'mainapp/contacts.html', content)


class CatalogListView(ListView):
    model = Product
    template_name = 'mainapp/catalog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart(self.request)
        context['object_list'] = context['object_list'][:8]
        context['title'] = 'Каталог'
        context['big_products'] = Product.objects.filter(gallery__is_big=True)[:2]
        context['cart'] = cart

        return context


def product(request, pk=None):
    cart = Cart(request)

    product_item = get_object_or_404(Product, pk=pk)

    similar_products = get_similar_products(product_item)

    title = product_item.name
    content = {
        'title': title,
        'product': product_item,
        "similar_products": similar_products,
        'cart': cart
    }

    return render(request, 'mainapp/product.html', content)


def main_slider(request):
    data_list = []
    sliders = MainSlider.objects.all()
    for id, slider in enumerate(sliders):
        content = dict()
        content['id'] = id
        content['header'] = slider.header
        content['text'] = slider.text
        content['short_text'] = slider.short_text
        content['image'] = slider.image.__str__()
        content['back_image'] = slider.back_image.__str__()
        data_list.append(content)

    return JsonResponse(data_list, safe=False)


def catalog_update(request, last_id):
    if request.is_ajax():
        products = Product.objects.filter(id__gt=last_id)[:4]

        content = {
            'object_list': products
        }

        result = render_to_string('mainapp/includes/inc_catalog_products.html', content)

        return JsonResponse({'result': result})
