from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from regular_exam_2024_feb.profile_car.forms import ProfileCreationForm
from regular_exam_2024_feb.profile_car.models import Profile
from regular_exam_2024_feb.utils import get_user_obj


class AlbumCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'profile/profile-create.html'
    success_url = reverse_lazy('catalog-page')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class CatalogueView(ListView):
    model = Profile  # Assuming you want to list profiles
    template_name = 'common/catalogue.html'  # Your template to display the catalogue
    context_object_name = 'profiles'  # Name of the variable in the template

    def get_queryset(self):
        return Profile.objects.all()
