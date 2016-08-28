from django.shortcuts import render
from django.utils import timezone
from .models import Post
import sys

def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all().order_by('published_date')
    for post in posts:
    	post.text = post.text[:200] + "........"
    	print(post.text)
    return render(request, 'blog/post_list.html', {'posts':posts})

def post(request, title):
    posts = Post.objects.filter(title=title)
    return render(request, 'blog/post.html', {'posts':posts})

def no_page_found(request):
    return render(request, 'blog/no_page_found.html',)