from django.db.models import Sum
from django.shortcuts import render, redirect

from car_collection.auth_app.forms import ProfileForm, EditProfileForm, DeleteProfileForm
from car_collection.cars_app.models import Car
from car_collection.core.utils import get_first_profile


def create_profile_page(request):
    form = ProfileForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {'form': form}

    return render(request, template_name='profile/profile-create.html', context=context)


def profile_details_page(request):
    profile = get_first_profile()
    total_sum = Car.objects\
        .filter(owner=profile, owner__isnull=False)\
        .aggregate(total_price=Sum('price'))['total_price'] or 0

    context = {
        'profile': profile,
        'total_sum': total_sum
    }

    return render(request, template_name='profile/profile-details.html', context=context)


def edit_profile_page(request):
    profile = get_first_profile()

    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')

    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'profile/profile-edit.html', context)


def delete_profile_page(request):
    profile = get_first_profile()
    form = DeleteProfileForm(instance=profile)

    if request.method == 'POST':
        profile.delete()
        return redirect('home')

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/profile-delete.html', context)
