from django.forms import models
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import BaseFormView, UpdateView, DeleteView

from regular_exam_2024_feb.car.forms import ProfileEditForm
from regular_exam_2024_feb.profile_car.forms import ProfileCreationForm
from regular_exam_2024_feb.profile_car.models import Profile
from regular_exam_2024_feb.utils import get_user_obj


def create_profile(request):
    if request.method == 'POST':
        form = ProfileCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the profile instance
            return redirect(reverse_lazy('catalog-page'))  # Redirect to the success URL
    else:
        form = ProfileCreationForm()

    # Get the user's profile to pass into the context
    user_profile = get_user_obj()

    return render(request, 'profile/profile-create.html', {
        'form': form,
        'profile': user_profile  # Pass the user's profile to the context
    })


def profile_detail(request):
    profile = get_user_obj()
    cars = profile.cars.all()

    total_price = sum(car.price for car in cars)

    # Prepare context data for the template
    context = {
        'profile': profile,
        'cars': cars,
        'total_price': total_price
    }

    # Render the profile details template
    return render(request, 'profile/profile-details.html', context)


def edit_profile(request):
    profile = get_user_obj()  # Get the current user's profile

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)  # Pass the instance here
        if form.is_valid():
            form.save()  # Save the form data directly
            return redirect('profile-details')  # Redirect to profile details page
    else:
        form = ProfileEditForm(instance=profile)  # Pass the instance here to pre-fill the form

    return render(request, 'profile/profile-edit.html', {'form': form, 'profile': profile})


def delete_profile(request):
    profile = get_user_obj()  # Get the profile associated with the logged-in user

    if request.method == 'POST':
        # Delete the profile and all associated cars
        profile.cars.all().delete()  # Assuming a related_name 'cars' for the relationship
        profile.delete()
        return redirect('home')  # Redirect to the Index page or any page you prefer

    return render(request, 'profile/profile-delete.html', {'profile': profile})
