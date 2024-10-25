from recipes_app.utils import get_user_obj
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CreateRecipeForm
from .models import Recipe


def catalogue(request):
    recipes = Recipe.objects.all()
    profile = get_user_obj()

    context = {
        'recipes': recipes,
        'profile': profile
    }
    return render(request, 'common/catalogue.html', context)


def recipe_create(request):
    profile = get_user_obj()

    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = profile
            recipe.save()
            return redirect(reverse_lazy('catalogue'))

    else:
        form = CreateRecipeForm()

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'recipe/create-recipe.html', context)


def recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    profile = get_user_obj()
    ingredients = recipe.ingredients.split(', ')

    context = {
        'recipe': recipe,
        'profile': profile,
        'ingredients': ingredients
    }

    return render(request, 'recipe/details-recipe.html', context)


def edit_page(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    form = CreateRecipeForm(request.POST or None, instance=recipe)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('catalogue'))

    context = {
        'recipe': recipe,
        'form': form,
    }
    return render(request, 'recipe/edit-recipe.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    profile = get_user_obj()

    if request.method == 'POST':
        recipe.delete()

        return redirect(reverse_lazy('catalogue'))

    context = {
        'recipe': recipe,
        'profile': profile
    }

    return render(request, 'recipe/delete-recipe.html', context)
