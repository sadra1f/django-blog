from django.shortcuts import render
from blog.models import Post

def home(request):
    post_count = 3
    posts = Post.objects.filter(status=1).order_by('-created_on')[:post_count]
    return render(request, 'blog/index.html', {
        'posts': posts,
    })

def blog(request):
    posts = Post.objects.filter(status=1).order_by('-created_on')
    return render(request, 'blog/blog.html', {
        'posts': posts,
    })

def post(request, slug):
    post = Post.objects.filter(status=1).get(slug=slug)
    return render(request, 'blog/post.html', {
        'post': post,
    })
