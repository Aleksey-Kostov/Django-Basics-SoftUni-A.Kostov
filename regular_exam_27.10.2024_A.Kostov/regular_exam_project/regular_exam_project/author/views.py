from django.shortcuts import render


def create_author(request):
    # if request.method == 'POST':
    #     form = CreateProfileForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect(reverse_lazy('catalogue'))
    #
    # else:
    #     form = CreateProfileForm()
    #
    # profile = get_user_obj()
    #
    # context = {
    #     'form': form,
    #     'profile': profile
    # }
    return render(request, 'author/create-author.html')


def details_author(request):
    # profile = get_user_obj()
    # recipes = profile.recipe_set.all()
    #
    # context = {
    #     'profile': profile,
    #     'recipes': recipes
    # }

    return render(request, 'author/details-author.html')


def edit_author(request):
    # profile = get_user_obj()
    # form = CreateProfileForm(request.POST or None, instance=profile)
    #
    # if request.method == 'POST':
    #     if form.is_valid():
    #         form.save()
    #         return redirect(reverse_lazy('details-profile'))
    #
    # else:
    #     form = CreateProfileForm(instance=profile)
    #
    # context = {
    #     'form': form,
    #     'profile': profile
    # }
    return render(request, 'author/edit-author.html')


def delete_author(request):
    # profile = get_user_obj()
    # recipe = profile.recipe_set.all()
    #
    # if request.method == 'POST':
    #
    #     if recipe.exists():
    #         recipe.delete()
    #     profile.delete()
    #     return redirect(reverse_lazy('home'))
    # context = {
    #     'profile': profile
    # }
    return render(request, 'author/delete-author.html')
