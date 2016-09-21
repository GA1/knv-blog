from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Writing
import sys
import re

def post_list(request):
  posts = Post.objects.all().filter(is_draft=False).order_by('-created_date')
  for post in posts:
    post.text = post.text[:100] + "......."
  return render(request, 'blog/post_list.html', {'posts':posts})

def post(request, title):
  post = Post.objects.filter(is_draft=False, title=title).first()
  if post == None:
    return no_page_found(request)
  return render(request, 'blog/post.html', {'post':post})

def writing_list(request):
  writings = Writing.objects.all().order_by('-created_date')
  for writing in writings:
    writing.text = writing.text[:100] + "......."
  return render(request, 'blog/writing_list.html', {'writings':writings})

def writing(request, title):
  writing = Writing.objects.filter(title=title).first()
  if writing == None:
    return no_page_found(request)
  return render(request, 'blog/writing.html', {'writing':writing})

def no_page_found(request):
  return render(request, 'blog/no_page_found.html', status=404)



