from django.shortcuts import render

posts = [
    {
        'author': 'hilk',
        'title': 'Blog Post 1',
        'content': 'This is the content of the first blog post',
        'date_posted': 'August 20, 2022'
    },
    {
        'author': 'yacht',
        'title': 'Blog Post 2',
        'content': 'This is the content of the second blog post',
        'date_posted': 'August 21, 2022'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
