from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView

from regular_exam_2024_feb.car.forms import CarsCreateForm
from regular_exam_2024_feb.car.models import Car
from regular_exam_2024_feb.utils import get_car_obj, get_user_obj


def catalogue_view(request):
    profile = get_user_obj()  # Get the user profile
    cars = Car.objects.all()  # Fetch all cars

    if request.method == 'POST':
        form = CarsCreateForm(request.POST)  # Create a form instance with POST data
        if form.is_valid():
            car = form.save(commit=False)  # Create car instance but don't save it yet
            car.owner = profile  # Associate with the user profile
            car.save()  # Save the car instance to the database
            return redirect('catalog-page')  # Redirect to the catalogue page
    else:
        form = CarsCreateForm()  # If GET request, create an empty form

    return render(request, 'common/catalogue.html', {
        'form': form,
        'profile': profile,
        'cars': cars
    })


class CreateCar(CreateView):
    model = Car
    form_class = CarsCreateForm
    success_url = reverse_lazy('catalog-page')  # Redirect to the catalogue page after success

    def get_template_names(self):
        # Optionally, implement logic here to determine the template to render
        return ['car/car-create.html']  # Use the create car template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_obj()  # Use the first Profile object
        return context

    def form_valid(self, form):
        car = form.save(commit=False)  # Create car object without saving to the database yet
        car.owner = get_user_obj()  # Assign the owner field to the first Profile object

        if car.owner is None:
            # Handle the case where the profile does not exist (unlikely, but safe to check)
            return self.form_invalid(form)  # If no owner, return invalid form response

        car.save()  # Save the car object to the database
        return super().form_valid(form)  # Redirect to the success URL


class CarDetailView(DetailView):
    model = Car
    template_name = 'car/car-details.html'
    context_object_name = 'cars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_user_obj()  # Add profile to context
        return context


class EditCarView(UpdateView):
    model = Car
    form_class = CarsCreateForm
    template_name = 'car/car-edit.html'  # Adjust the template name if necessary
    success_url = reverse_lazy('catalog-page')

    def get_object(self, queryset=None):
        return super().get_object(queryset)


class DeleteCarView(DeleteView):
    model = Car
    template_name = 'car/car-delete.html'
    success_url = reverse_lazy('catalog-page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = self.object  # Pass the car instance to the template
        return context
