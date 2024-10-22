from django.shortcuts import render

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import BaseFormView

from regular_exam_2024_feb.profile_car.models import Profile
from regular_exam_2024_feb.utils import get_user_obj


def home_page(request):
    profile = get_user_obj()
    context = {
        'profile': profile
    }
    return render(request, 'common/index.html', context)


