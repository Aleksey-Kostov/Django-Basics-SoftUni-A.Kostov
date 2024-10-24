from django.shortcuts import render

from recipes_app.utils import get_user_obj


def home_page(request):
    profile = get_user_obj()

    context = {
        'profile': profile
    }

    return render(request, 'common/home-page.html', context)



