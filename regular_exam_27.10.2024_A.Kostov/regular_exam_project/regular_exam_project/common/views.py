from django.shortcuts import render

from regular_exam_project.posts.models import Post
from utils import get_user_obj


def home_page(request):
    author = get_user_obj()

    context = {
        'author': author
    }

    return render(request, 'common/index.html', context)


def dashboard(request):
    posts = Post.objects.all()
    author = get_user_obj()

    context = {
        'posts': posts,
        'author': author
    }
    return render(request, 'common/dashboard.html', context)
