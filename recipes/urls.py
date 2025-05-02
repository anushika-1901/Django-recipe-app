from . import views
from django.urls import path
urlpatterns=[
    path('',views.home,name='home'),
    path('recipes/',views.recipe_list,name='recipe_list'),
    path('recipes/add/',views.recipe_add,name='recipe_add'),
    path('recipes/<int:pk>/edit/',views.recipe_edit,name='recipe_edit'),
    path('recipes/<int:pk>/delete/',views.recipe_delete,name='recipe_delete'),
    path('toggle_favorite/<int:pk>/',views.toggle_favorite,name='toggle_favorite')
]