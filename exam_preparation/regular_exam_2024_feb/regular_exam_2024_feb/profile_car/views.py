from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView
from django.views.generic.edit import BaseFormView

from regular_exam_2024_feb.profile_car.forms import ProfileCreationForm
from regular_exam_2024_feb.profile_car.models import Profile
from regular_exam_2024_feb.utils import get_user_obj


class AlbumCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('create-page')

    def get_template_names(self):
        profile = get_user_obj()  # None or QuerySet

        if profile:
            return ['common/catalogue.html']

        return ['profile/profile-create.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
