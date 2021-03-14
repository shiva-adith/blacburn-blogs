from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all().reverse()[:3]

    return render(request, 'blogs/index.html', {'posts': posts})


def about(request):
    return render(request, 'blogs/about.html')


def contact(request):
    return render(request, 'blogs/contact.html')


def post(request):
    posts = Post.objects.all().order_by('date_posted')
    
    return render(request, 'blogs/post.html', {'posts': posts})
