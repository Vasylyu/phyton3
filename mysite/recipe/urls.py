from django.urls import path
from .views import recipe_index, groups_list, products_list, orders_list
app_name = 'recipe'
urlpatterns = [
    path("", recipe_index, name="index"),
    path("groups/", groups_list, name="groups_list"),
    path("products/", products_list, name="products_list"),
    path("orders/", orders_list, name="orders_list"),
]
