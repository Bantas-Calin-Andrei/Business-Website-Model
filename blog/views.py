from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_superuser

def blog_view(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog.html', {'posts': posts})

@login_required
@user_passes_test(is_admin)
def blog_admin_view(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog')
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_admin.html', {'form': form})