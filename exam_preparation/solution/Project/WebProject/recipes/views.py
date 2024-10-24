from django.shortcuts import render, redirect, get_object_or_404

from WebProject.recipes.forms import DeleteRecipeForm, RecipeForm
from WebProject.recipes.models import Recipe
from WebProject.utils.get_profile import get_profile


def catalogue_page(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes,
               'profile': get_profile()}

    return render(request, template_name='recipe/catalogue.html', context=context)


def create_recipe_page(request):
    form = RecipeForm(request.POST or None)
    profile = get_profile()
    if form.is_valid():
        form.instance.author_id = profile.pk
        form.save()

        return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, template_name='recipe/create-recipe.html', context=context)


def recipe_details_page(request, recipe_id):

    recipe = get_object_or_404(Recipe, id=recipe_id)
    ingredients_list = recipe.ingredients.split(', ')
    context = {
        'profile': get_profile(),
        'recipe': recipe,
        'ingredients_list': ingredients_list,
    }

    return render(request, template_name='recipe/details-recipe.html', context=context)


def edit_recipe_page(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    form = RecipeForm(instance=recipe)

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'recipe': recipe,
        'form': form,
        'profile': get_profile(),
    }
    return render(request, 'recipe/edit-recipe.html', context)


def delete_recipe_page(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        recipe.delete()
        return redirect('catalogue')

    form = DeleteRecipeForm(instance=recipe)
    context = {
        'profile': get_profile(),
        'form': form
    }

    return render(request, 'recipe/delete-recipe.html', context)
