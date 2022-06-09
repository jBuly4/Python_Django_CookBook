from django.shortcuts import render, get_object_or_404
from .models import Recipe, Ingredients, Tags

# Create your views here.


# def index(request):
#     return render(request, 'base.html')


def recipe_lst(request):
    recipes = Recipe.objects.all()  # you can define in models.py your own Model manager instead of objects
    return render(request,
                  'recipes_lst.html',
                  {'recipes': recipes})


def recipe_detail(request, title):
    recipe = get_object_or_404(Recipe, title=title)

    return render(request, 'recipe_detail.html', {'recipe': recipe})  # Django3 by example p28
