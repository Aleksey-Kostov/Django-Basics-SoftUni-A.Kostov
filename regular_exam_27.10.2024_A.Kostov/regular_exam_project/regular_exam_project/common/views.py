from django.shortcuts import render


def home_page(request):
    # profile = get_user_obj()
    #
    # context = {
    #     'profile': profile
    # }

    return render(request, 'common/index.html')


def dashboard(request):
    # recipes = Recipe.objects.all()
    # profile = get_user_obj()
    #
    # context = {
    #     'recipes': recipes,
    #     'profile': profile
    # }
    return render(request, 'common/dashboard.html')
