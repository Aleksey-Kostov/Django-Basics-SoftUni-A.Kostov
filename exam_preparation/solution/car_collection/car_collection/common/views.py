from django.shortcuts import render

from car_collection.core.utils import get_first_profile


def home_page(request):
    profile = get_first_profile()
    context = {'profile': profile}

    return render(request, template_name='index.html', context=context)
