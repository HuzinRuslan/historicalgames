from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.CatalogView.as_view(), name='index'),
    # path('<int:pk>/<page>/', mainapp.catalog, name='category'),
    path('product/<int:pk>/', mainapp.product, name='product'),
]
