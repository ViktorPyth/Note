from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib import auth
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators import csrf
from django.shortcuts import render_to_response
from django.template.context_processors import csrf


def register( request):
   args = {}
   args.update(csrf(request))
   args['form']= UserCreationForm()
   if request.POST:
       newuser_form= UserCreationForm(request.POST)
       if newuser_form.is_valid():
           newuser_form.save()
           newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
           auth.login(request,newuser)
           return redirect('/')
       else:
           args['form'] = newuser_form
   return render_to_response ('registration/regis.html', args)


def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'note/post_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'note/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.like = False
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'note/post_new.html', {'form': form})
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = post.created_date
            post.like = post.like
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'note/post_new.html', {'form': form})
@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.like()
    return redirect('post_detail', pk=pk)
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')