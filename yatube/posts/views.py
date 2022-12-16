from django.shortcuts import render
from django.http import HttpResponse

context = {
        'index_text': 'Это главная страница проекта Yatube',
        'groups_text': 'Здесь будет информация о группах проекта Yatube',
    }


def index(request):
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    return render(request, 'posts/group_list.html', context)
