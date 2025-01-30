from timeit import default_timer
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Product, Order


def recipe_index(request: HttpRequest):
    products = [
        ('cake', 1999),
        ('puncake', 2999),
        ('cakesik', 3000),
    ]
    contex = {
        "time_running": default_timer(),
        'products': products,

    }
    return render(request, 'recipe/recipe-index.html', context=contex)


def groups_list(request: HttpRequest):
    contex = {
        "groups": Group.objects.prefetch_related('permissions').all(),

    }
    return render(request, 'recipe/groups-list.html', context=contex)


def products_list(request: HttpRequest):
    context = {"products": Product.objects.all(), }
    return render(request, 'recipe/products-list.html', context=context)


def orders_list(request: HttpRequest):
    context = {"orders": Order.objects.select_related("user").prefetch_related("products").all(),

               }
    return render(request, 'recipe/orders-list.html', context=context)
