from django.shortcuts import render, redirect
from forumApp.posts.forms import PostCreateForm, PostDeleteForm, SearchPostForm, PostEditForm
from forumApp.posts.models import Post


def index(request):
    return render(request, 'base.html')


def dashboard(request):
    posts = Post.objects.all()
    form = SearchPostForm(request.GET)

    if request.method == 'GET':
        if form.is_valid():
            query = form.cleaned_data['query']
            post = posts.filter(title__icontains=query)

    context = {
        'posts': posts,
        'form': form
    }

    return render(request, 'posts/dashboard.html', context)


def add_post(request):
    form = PostCreateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(dashboard)

    context = {
        'form': form
    }

    return render(request, 'posts/add-post.html', context)


def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)

    if request.method == 'POST':
        post.delete()
        return redirect(dashboard)

    context = {
        'form': form,
        'post': post
    }

    return render(request, 'posts/delete-post.html', context)


def details_page(request, pk: int):
    post = Post.objects.get(pk=pk)

    context = {
        'post': post
    }

    return render(request, 'posts/details.html', context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostEditForm(request.POST or None, instance=post)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(dashboard)

    context = {
        'form': form,
        'post': post
    }

    return render(request, 'posts/edit-post.html', context)