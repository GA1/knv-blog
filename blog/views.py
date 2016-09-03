from django.shortcuts import render
from django.utils import timezone
from .models import Post
import sys
import re

def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    for post in posts:
    	post.text = post.text[:100] + "......."
    return render(request, 'blog/post_list.html', {'posts':posts})

def post(request, title):
    post = Post.objects.filter(title=title).first()
    if post == None:
        return no_page_found(request)
    return render(request, 'blog/post.html', {'post':post})

def no_page_found(request):
    return render(request, 'blog/no_page_found.html', status=404)



