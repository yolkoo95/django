from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Post
from datetime import datetime 

# Create your views here.

def homepage(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'now': datetime.now(),
    }

    return render(request, 'blogsite/index.html', context)

def post(request, slug):
    try:
        post = Post.objects.get(slug = slug)
        context = {
            'post': post,
        }

        if post is not None:
            return render(request, 'blogsite/post.html', context)
    
    except:
        return HttpResponseRedirect(reverse('homepage'))