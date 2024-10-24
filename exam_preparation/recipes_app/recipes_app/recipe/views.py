from django.shortcuts import render


def catalogue(request):
    return render(request, 'common/catalogue.html')


def recipe_create(request):
    return render(request, 'recipe/create-recipe.html')


def recipe_details(request, recipe_pk):
    return render(request, 'recipe/details-recipe.html')


def edit_page(request, recipe_pk):
    return render(request, 'recipe/edit-recipe.html')


def delete_recipe(request, recipe_pk):
    return render(request, 'recipe/delete-recipe.html')
