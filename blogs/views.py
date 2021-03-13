from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all()

    return render(request, 'blogs/index.html', {'posts': posts})


def about(request):
    return render(request, 'blogs/about.html')


def contact(request):
    return render(request, 'blogs/contact.html')


def post(request):
    return render(request, 'blogs/post.html')
