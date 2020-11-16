from django.shortcuts import get_object_or_404, render
from blog.models import Post, Comment
from blog.forms import CommentForm


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
    post = get_object_or_404(Post.objects.filter(status=1), slug=slug)
    comments = Comment.objects.filter(
        active=True, post=post).order_by('-created_on')
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post.html', {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    })
