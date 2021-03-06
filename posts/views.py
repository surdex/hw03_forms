from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group
from .forms import PostForm


def index(request):
    latest = Post.objects.all()[:11]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)

    posts = group.posts.all()[:12]
    return render(request, "group.html", {"group": group, "posts": posts})


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            group = form.cleaned_data['group']
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
        return render(request, 'new_post.html', {'form': form})
    form = PostForm()
    return render(request, 'new_post.html', {'form': form})
