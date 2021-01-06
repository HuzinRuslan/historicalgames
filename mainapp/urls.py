from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.CatalogListView.as_view(), name='index'),
    path('update/<int:last_id>/', mainapp.catalog_update, name='update'),
    path('product/<int:pk>/', mainapp.product, name='product'),
]
