from django.shortcuts import render

def post_list(request):
    return render(request, 'note/post_list.html', {})