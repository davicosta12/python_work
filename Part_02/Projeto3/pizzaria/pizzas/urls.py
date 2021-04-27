from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pizzas', views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>', views.toppings, name='toppings'),
]
