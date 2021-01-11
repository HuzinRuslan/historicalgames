from django.urls import path
import cart.views as cart

app_name = 'cart'

urlpatterns = [
    path('', cart.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', cart.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart.cart_remove, name='cart_remove'),
    path('cart_edit/<int:pk>/<int:quantity>/', cart.cart_edit, name='cart_edit'),
]
