from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from recipes_app.profile_recipes.forms import CreateProfileForm
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
    return render(request, 'profile/details-profile.html')


def edit_profile(request):
    return render(request, 'profile/edit-profile.html')


def delete_profile(request):
    return render(request, 'profile/delete-profile.html')
