from django.urls import path
from .views import recipe_index, groups_list
app_name = 'recipe'
urlpatterns = [
    path("", recipe_index, name="index"),
    path("groups/", groups_list, name="groups_list")
]
