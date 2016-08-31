from django.shortcuts import render
from django.utils import timezone
from .models import Post
import sys

def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    for post in posts:
    	post.text = extract_first_three_lines_or_200_Charspost(text[:200] + "........")
    	print(post.text)
    return render(request, 'blog/post_list.html', {'posts':posts})

def post(request, title):
    post = Post.objects.filter(title=title).first()
    if post == None:
        return no_page_found(request)
    return render(request, 'blog/post.html', {'post':post})

def no_page_found(request):
    return render(request, 'blog/no_page_found.html', status=404)



