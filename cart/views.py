from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from cart.cart import Cart
from mainapp.models import Product


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


def cart_edit(request, pk, quantity):
    product = get_object_or_404(Product, pk=pk)
    cart = Cart(request)
    if request.is_ajax():
        quantity = int(quantity)
        if quantity > 0:
            cart.add(product=product, quantity=quantity, update_quantity=True)
            cart.save()
        else:
            cart.remove(product=product)

        content = {
            'cart': cart
        }

        result = render_to_string('cart/includes/inc_cart_list.html', content)
        return JsonResponse({'result': result})
