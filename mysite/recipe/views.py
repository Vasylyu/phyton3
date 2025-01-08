
from timeit import default_timer
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


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
        "groups": Group.objects.all(),

    }
    return render(request, 'recipe/groups-list', context=contex)
