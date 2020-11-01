from django.shortcuts import render

def home(request):
    return render(request, 'blog/index.html')

def blog(request):
    return render(request, 'blog/blog.html')

def post(request):
    return render(request, 'blog/post.html')
