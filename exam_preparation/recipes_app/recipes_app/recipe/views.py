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


def recipe_details(request, recipe_pk):
    recipe = Recipe.objects.get(recipe_pk=recipe_pk)
    profile = get_user_obj()
    comment_form = CreateRecipeForm(instance=profile)

    context = {
        'recipe': recipe,
        'profile': profile,
        'comment_form': comment_form
    }

    return render(request, 'recipe/details-recipe.html', context)


def edit_page(request, recipe_pk):
    return render(request, 'recipe/edit-recipe.html')


def delete_recipe(request, recipe_pk):
    return render(request, 'recipe/delete-recipe.html')
