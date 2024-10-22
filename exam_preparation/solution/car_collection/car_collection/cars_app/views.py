from django.shortcuts import render, redirect, get_object_or_404

from car_collection.auth_app.models import Profile
from car_collection.cars_app.forms import DeleteCarForm, CarForm
from car_collection.cars_app.models import Car
from car_collection.core.utils import get_first_profile


def catalogue_page(request):
    cars = Car.objects.all()
    context = {
        'profile': get_first_profile(),
        'cars': cars
    }

    return render(request, template_name='car/catalogue.html', context=context)


def create_car_page(request):
    form = CarForm(request.POST or None)
    profile = get_first_profile()
    if form.is_valid():
        form.instance.owner_id = profile.pk
        form.save()

        return redirect('catalogue')

    context = {
        'profile': profile,
        'form': form
    }

    return render(request, template_name='car/car-create.html', context=context)


def car_details_page(request, pk):
    car = get_object_or_404(Car, pk=pk)
    context = {
        'profile': get_first_profile(),
        'car': car
    }

    return render(request, template_name='car/car-details.html', context=context)


def edit_car_page(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = CarForm(instance=car)

    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'car': car,
        'form': form,
        'profile': get_first_profile(),
    }
    return render(request, 'car/car-edit.html', context)


def delete_car_page(request, pk):
    car = get_object_or_404(Car, pk=pk)

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')

    form = DeleteCarForm(instance=car)
    context = {
        'profile': get_first_profile(),
        'form': form
    }

    return render(request, 'car/car-delete.html', context)
