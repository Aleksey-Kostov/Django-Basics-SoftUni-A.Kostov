from django.shortcuts import render

from WebProject.profiles.models import Profile


# Create your views here.

def home_page(request):
    profile = Profile.objects.first()
    context = {'profile': profile}

    return render(request, template_name='common/home-page.html', context=context)