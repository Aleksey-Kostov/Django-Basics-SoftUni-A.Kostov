from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from regular_exam_project.author.forms import AuthorCreationForm, AuthorEditForm
from utils import get_user_obj


def create_author(request):
    if request.method == 'POST':
        form = AuthorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('dashboard'))

    else:
        form = AuthorCreationForm()

    author = get_user_obj()

    context = {
        'form': form,
        'author': author
    }
    return render(request, 'author/create-author.html', context)


def details_author(request):
    author = get_user_obj()
    posts = author.post_set.all()
    num_posts = posts.count()
    last_updated_post = posts.order_by('-updated_at').first() if posts.exists() else None

    context = {
        'author': author,
        'posts': posts,
        'num_posts': num_posts,
        'last_updated_post': last_updated_post,
    }

    return render(request, 'author/details-author.html', context)


def edit_author(request):
    author = get_user_obj()
    form = AuthorEditForm(request.POST or None, instance=author)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('details-author'))

    else:
        form = AuthorEditForm(instance=author)

    context = {
        'form': form,
        'author': author
    }
    return render(request, 'author/edit-author.html', context)


def delete_author(request):
    author = get_user_obj()
    posts = author.post_set.all()

    if request.method == 'POST':

        if posts.exists():
            posts.delete()
        author.delete()
        return redirect(reverse_lazy('home'))
    context = {
        'author': author
    }
    return render(request, 'author/delete-author.html', context)
