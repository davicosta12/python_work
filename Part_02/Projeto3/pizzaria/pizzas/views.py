from django.shortcuts import render

from pizzas.models import Pizza

# Create your views here.


def index(request):
    return render(request, 'pizzas/index.html')


def pizzas(request):
    """Mostra todos as pizzas."""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)


def toppings(request, pizza_id):
    """Mostra a pizza de cada pizzaria"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/toppings.html', context)
