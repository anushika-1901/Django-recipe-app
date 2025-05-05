from . import views
from django.urls import path
urlpatterns=[
    path('',views.home,name='home'),
    path('my_recipes/',views.my_recipes,name='my_recipes'),
    path('create_recipe/',views.create_recipe,name='create_recipe'),
    path('update_recipe/<int:pk>/',views.update_recipe,name='update_recipe'),
    path('delete_recipe/<int:pk>/',views.delete_recipe,name='delete_recipe'),
    path('toggle_favorite<int:pk>/',views.toggle_favorite,name='toggle_favorite'),
    path('favorite_recipes/',views.favorite_recipes,name='favorite_recipes'),
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login_view'),
    path('logout/',views.logout_view,name='logout_view')
]