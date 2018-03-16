from django.shortcuts import render
from .models import Post
from .forms import PostForm

from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'note/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'note/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'post/post_new.html', {'form': form})