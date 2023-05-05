from django.shortcuts import render


posts = [
    {
        'author': 'Tatyana',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 2, 2023'
    },
    {
        'author': 'Denys',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 3, 2023'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "About"})

