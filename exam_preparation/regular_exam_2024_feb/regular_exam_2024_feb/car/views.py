from django.views.generic import ListView
from django.views.generic.edit import BaseFormView

from regular_exam_2024_feb.car.models import Car
from regular_exam_2024_feb.profile_car.models import Profile


class CatalogueView(ListView, BaseFormView):
    model = Profile  # Assuming you want to list profiles
    template_name = 'common/catalogue.html'  # Your template to display the catalogue
    context_object_name = 'cars'  # Name of the variable in the template

    def get_queryset(self):
        return Car.objects.all()
