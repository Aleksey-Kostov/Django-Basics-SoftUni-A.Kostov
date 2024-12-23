from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView

from regular_exam_project.posts.forms import PostCreationForm, PostEditForm, PostDeleteForm
from regular_exam_project.posts.models import Post
from utils import get_user_obj


def post_create(request):
    author = get_user_obj()

    if request.method == 'POST':
        form = PostCreationForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = author
            post.save()
            return redirect(reverse_lazy('dashboard'))

    else:
        form = PostCreationForm()

    context = {
        'form': form,
        'author': author
    }
    return render(request, 'posts/create-post.html', context)


# def post_details(request, pk):
#     post = Post.objects.get(pk=pk)
#     author = get_user_obj()
#
#     context = {
#         'post': post,
#         'author': author,
#     }
#
#     return render(request, 'posts/details-post.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/details-post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = get_user_obj()
        return context


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    form = PostEditForm(request.POST or None, instance=post)
    author = get_user_obj()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('dashboard'))

    context = {
        'post': post,
        'form': form,
        'author': author,
    }
    return render(request, 'posts/edit-post.html', context)


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    author = get_user_obj()
    form = PostDeleteForm(instance=post)

    if request.method == 'POST':
        post.delete()
        return redirect(reverse_lazy('dashboard'))

    context = {
        'post': post,
        'author': author,
        'form': form
    }

    return render(request, 'posts/delete-post.html', context)
