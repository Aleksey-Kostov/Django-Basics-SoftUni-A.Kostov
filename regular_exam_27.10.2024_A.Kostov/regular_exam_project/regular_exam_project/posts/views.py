from django.shortcuts import render


def post_create(request):
    # profile = get_user_obj()
    #
    # if request.method == 'POST':
    #     form = CreateRecipeForm(request.POST)
    #
    #     if form.is_valid():
    #         recipe = form.save(commit=False)
    #         recipe.author = profile
    #         recipe.save()
    #         return redirect(reverse_lazy('catalogue'))
    #
    # else:
    #     form = CreateRecipeForm()
    #
    # context = {
    #     'form': form,
    #     'profile': profile
    # }
    return render(request, 'posts/create-post.html')


def post_details(request, pk):
    # recipe = Recipe.objects.get(pk=pk)
    # profile = get_user_obj()
    # ingredients = recipe.ingredients.split(', ')
    #
    # context = {
    #     'recipe': recipe,
    #     'profile': profile,
    #     'ingredients': ingredients
    # }

    return render(request, 'posts/details-post.html')


def post_edit(request, pk):
    # recipe = Recipe.objects.get(pk=pk)
    # form = CreateRecipeForm(request.POST or None, instance=recipe)
    #
    # if request.method == 'POST':
    #     if form.is_valid():
    #         form.save()
    #         return redirect(reverse_lazy('catalogue'))
    #
    # context = {
    #     'recipe': recipe,
    #     'form': form,
    # }
    return render(request, 'posts/edit-post.html')


def post_delete(request, pk):
    # recipe = Recipe.objects.get(pk=pk)
    # profile = get_user_obj()
    #
    # if request.method == 'POST':
    #     recipe.delete()
    #
    #     return redirect(reverse_lazy('catalogue'))
    #
    # context = {
    #     'recipe': recipe,
    #     'profile': profile
    # }

    return render(request, 'posts/delete-post.html')
