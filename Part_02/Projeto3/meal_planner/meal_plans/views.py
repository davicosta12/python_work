from django.shortcuts import render

# Create your views here.


def index(request):
    """A página inicial de meal_plans"""
    return render(request, 'meal_plans/index.html')
