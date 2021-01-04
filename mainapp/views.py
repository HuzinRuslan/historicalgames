from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


# class Main(ListView):
#     template_name = 'adminapp/users.html'

def main(request):
    content = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', content)


def contacts(request):
    content = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contacts.html', content)


def catalog(request):
    content = {
        'title': 'Каталог'
    }
    return render(request, 'mainapp/catalog.html', content)


def product(request):
    content = {
        'title': 'Продукт'
    }
    return render(request, 'mainapp/product.html', content)
