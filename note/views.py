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
    if request.user.is_active:
        posts = Post.objects.filter(created_date__lte=timezone.now(),author=request.user).order_by('created_date')
    else:
        posts = ()
    return render(request, 'note/post_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        post = get_object_or_404(Post, pk=0)
    return render(request, 'note/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.like()
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
            #post.like = post.like
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'note/post_new.html', {'form': form})
@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.luke()
    return redirect('post_detail', pk=pk)
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


def search_form(request):
    return render_to_response('note/search_form.html')

def search(request):
   if 'title' in request.GET and request.GET['title']:
      title = request.GET['title']
      post = Post.objects.filter(title__icontains=title , author = request.user)
      return render(request, 'note/post_list.html', {'posts': post})
   else:
       return redirect('post_list', pk=0)

"""def post_search(request):
    post = Post.objects.all()
    if request.method == "POST":
        form = request.GET.get('q')
        result = form.base_fields['search']
        input('2')
    if request.user.is_active:
        posts = post.filter(title__icontains = result)
    else:
        posts = ()
    return render(request, 'note/post_list.html', {'posts': posts})"""