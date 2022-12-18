from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.conf import settings

posts_on_page = settings.POSTS_ON_PAGE


def index(request):
    posts = Post.objects.select_related('group').all()[:posts_on_page]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:posts_on_page]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
