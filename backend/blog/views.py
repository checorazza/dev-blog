from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def create_post(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        Post.objects.create(title=title, content=content, author=author)
        return redirect('home')
    return render(request, 'blog/create_post.html')
