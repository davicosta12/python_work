"""Define padrões de URL para meal_plans."""

from django.urls import include, path

from . import views

urlpatterns = [
    # Página inicial
    path('', views.index, name='index'),
]
