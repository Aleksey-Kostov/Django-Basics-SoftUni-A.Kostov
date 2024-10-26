from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from recipes_app.profile_recipes.forms import CreateProfileForm
from recipes_app.recipe.models import Recipe
from recipes_app.utils import get_user_obj


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('catalogue'))

    else:
        form = CreateProfileForm()

    profile = get_user_obj()

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'profile/create-profile.html', context)


def details_profile(request):
    profile = get_user_obj()
    recipes = profile.recipe_set.all()

    context = {
        'profile': profile,
        'recipes': recipes
    }

    return render(request, 'profile/details-profile.html', context)


def edit_profile(request):
    profile = get_user_obj()
    form = CreateProfileForm(request.POST or None, instance=profile)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('details-profile'))

    else:
        form = CreateProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'profile/edit-profile.html', context)


def delete_profile(request):
    profile = get_user_obj()
    recipe = profile.recipe_set.all()

    if request.method == 'POST':

        if recipe.exists():
            recipe.delete()
        profile.delete()
        return redirect(reverse_lazy('home'))
    context = {
        'profile': profile
    }
    return render(request, 'profile/delete-profile.html', context)
